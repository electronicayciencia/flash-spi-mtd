Create custom devicetree for non jedec device and custom partitions.

Decompile:

    dtc -I dtb -O dts -o ~/jedec-spi-nor.dts /boot/overlays/jedec-spi-nor.dtbo

Compile new:

    dtc -@ -I dts -O dtb -o /boot/overlays/eyc-spi-nor.dtbo eyc-spi-nor.dts


