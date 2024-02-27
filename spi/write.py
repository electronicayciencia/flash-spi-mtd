# Interact with a w25p08 flash in python using raw SPI commands.
import spidev

# Open SPI
spi = spidev.SpiDev()
spi.open(bus = 0, device = 0)

# Set SPI speed and mode
spi.max_speed_hz = 500000
spi.mode = 0

# Enable write
data = [0x06]
print("Sent: " + " ".join("{:02x}".format(n) for n in data))
spi.xfer(data)
print("Recv: " + " ".join("{:02x}".format(n) for n in data))


# Write
data = [0x02, 0x11, 0x22, 0x33, 0x31, 0x32, 0x33, 0x34, 0x35]
print("Sent: " + " ".join("{:02x}".format(n) for n in data))
spi.xfer(data)
print("Recv: " + " ".join("{:02x}".format(n) for n in data))

