These are dummy "default configuration files".

## Create image

To create the image file:

    mke2fs -m 0 -b 1024 -t ext2 -d . /tmp/conf.fs 128

To flash the MTD:

    flash_erase   /dev/mtd0 0 0 
    dd if=/tmp/conf.fs of=/dev/mtd0

or:

    flashcp -v /tmp/conf.fs /dev/mtd0

## Protect the flash

See datasheet to protect the lower 1/4 of the flash.

## Mount filesystems

Create mount points

    mkdir -p /tmp/userconfig
    mkdir -p /opt/conf

Mount RO filesystem with default config
    
    mount /dev/mtdblock0 /opt/conf -o ro

Mount user customized files

    mount -t jffs2 mtd1 /tmp/userconfig

Prepare for overlay

    mkdir -p /tmp/userconfig/config /tmp/userconfig/work

Create overlay to marge both config systems

    mount -t overlay -o lowerdir=/opt/conf,upperdir=/tmp/userconfig/config,workdir=/tmp/userconfig/work mergedcfg /opt/conf

Outcome:

    # mount
    /dev/mtdblock0 on /opt/conf       type ext2    (ro,relatime)
    mtd1           on /tmp/userconfig type jffs2   (rw,relatime)
    mergedcfg      on /opt/conf       type overlay (rw,relatime,lowerdir=/opt/conf,upperdir=/tmp/userconfig/config,workdir=/tmp/userconfig/work/)



