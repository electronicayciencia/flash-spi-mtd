Proof of Concept about embeded devices security.

MTD has three partitions:
- setup: jffs2 image with these files.
- key: blob with the filesystem key.
- data: encrypted jffs2.

Create jffs2 image:

    mkfs.jffs2 -p setup -o /tmp/setup.jffs2
    dd if=/tmp/setup.jffs2 of=/dev/mtd0

Mount:

    mkdir -p /tmp/setup
    mount -t jffs2 mtd0 /tmp/setup -o ro

