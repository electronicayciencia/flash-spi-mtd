Create custom devicetree for non jedec device and custom partitions.

Decompile:

    dtc -I dtb -O dts -o ~/jedec-spi-nor.dts /boot/overlays/eyc-spi-nor.dtbo

Compile new:

    sudo dtc -I dts -O dtb -o /boot/overlays/eyc-spi-nor.dtbo eyc-spi-nor.dts


