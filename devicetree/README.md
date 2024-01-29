Create custom devicetree for non jedec device and custom partitions.

Decompile:

    dtc -I dtb -O dts -o ~/my-spi-nor.dts /boot/overlays/jedec-spi-nor.dtbo

Compile new:

    sudo dtc -I dts -O dtb -o /boot/overlays/my-spi-nor.dtbo my-spi-nor.dts


