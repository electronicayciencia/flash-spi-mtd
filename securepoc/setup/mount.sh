#!/bin/bash
# Mount data filesystem.

set -e
set -u
modprobe mtdblock
modprobe aes
modprobe cryptoloop

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

mkdir -p $MOUNTPOINT
mount -t jffs2 $MTDLOOP $MOUNTPOINT


