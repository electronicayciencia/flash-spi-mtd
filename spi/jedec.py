# Interact with a w25p08 flash in python using raw SPI commands.
import spidev

# Open SPI
spi = spidev.SpiDev()
spi.open(bus = 0, device = 0)

# Set SPI speed and mode
spi.max_speed_hz = 500000
spi.mode = 0

# Transfer data
data = [0x9F, 0x00, 0x00, 0x00]
print("Sent: " + " ".join("{:02x}".format(n) for n in data))

spi.xfer(data)

print("Recv: " + " ".join("{:02x}".format(n) for n in data))

