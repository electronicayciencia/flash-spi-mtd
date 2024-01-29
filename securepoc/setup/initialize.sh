#!/bin/bash
# Create new key files.
# Initialize key block.
# Initialize data filesystem.
# Mount data filesystem.

set -e
set -u
modprobe mtdblock
modprobe aes
modprobe cryptoloop

# Create secret files
openssl rand -hex 32 > /root/secret.key
openssl rand -hex 16 > /root/secret.iv

# Create key block
LABEL="key"
MTDKEY=$(cat /proc/mtd | grep $LABEL | cut -d ':' -f 1)

flash_erase  /dev/$MTDKEY 0 0
openssl rand -base64 32 | \
openssl enc -aes-256-cbc -K `cat /root/secret.key` -iv `cat /root/secret.iv` | \
dd of=/dev/$MTDKEY

# Initialize loop filesystem
LABEL="data"
MTDSEC=$(cat /proc/mtd | grep $LABEL | cut -d ':' -f 1)
MTDBLSEC=${MTDSEC/mtd/mtdblock}
LOOPDEV=$(losetup -f)
HWID=$(cat /proc/cpuinfo | grep Serial | cut -d ' ' -f 2)
LOOPKEY=$(dd if=/dev/mtd1 bs=48 count=1 | openssl enc -d -aes-256-cbc -K `cat /root/secret.key` -iv `cat /root/secret.iv`)
echo "$HWID$LOOPKEY" | losetup -e aes256 -p0 $LOOPDEV /dev/$MTDBLSEC

# Initialice jffs2 filesystem
MOUNTPOINT="/tmp/secret"

modprobe block2mtd block2mtd=${LOOPDEV},65536
MTDLOOP=$(cat /proc/mtd | grep "$LOOPDEV" | cut -d ':' -f 1)
flash_erase -j /dev/$MTDLOOP 0 0

mkdir -p $MOUNTPOINT
mount -t jffs2 $MTDLOOP $MOUNTPOINT


