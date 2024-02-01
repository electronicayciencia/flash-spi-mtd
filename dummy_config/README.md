These are dummy "default configuration files".

To create the image file:

    mke2fs -m 0 -b 1024 -t ext2 -d . /tmp/conf.fs 128

To flash the MTD:

    flash_erase   /dev/mtd0 0 0 
    dd if=/tmp/conf.fs of=/dev/mtd0

or:

    flashcp -v /tmp/conf.fs /dev/mtd0

