# Interact with a w25p08 flash in python.
# Using raw SPI commands.
#
import spidev
from time import sleep
from binascii import hexlify

bus = 0     #spi0
device = 0  #.0  (chip select pin)

# Enable SPI
spi = spidev.SpiDev()
spi.open(bus, device)

# Set SPI speed and mode
spi.max_speed_hz = 500000
spi.mode = 0

CMD_PAGE_WRITE    = 0x02
CMD_PAGE_READ     = 0x03
CMD_WRITE_DISABLE = 0x04
CMD_WRITE_ENABLE  = 0x06
CMD_JEDEC_ID      = 0x9F
CMD_CHIP_ERASE    = 0xC7
CMD_BLOCK_ERASE   = 0xD8  # block is 65k 0x10000
CMD_READ_STATUS1  = 0x05
CMD_READ_STATUS2  = 0x35
CMD_READ_STATUS3  = 0x15
CMD_WRITE_STATUS1  = 0x01
CMD_WRITE_STATUS2  = 0x31
CMD_WRITE_STATUS3  = 0x11


def xfer(spi, cmd, n = 0):
    """ xfer the cmd followed by n zeros to read the response """
    data = spi.xfer(cmd + n * [0x00])
    return data[len(cmd):]

def print_hex(l):
    """ Format a list as hex, with zero padding. """
    print(" ".join("{:02x}".format(n) for n in l))

def busy(spi):
    """ Check status 1 byte 0 """
    data = xfer(spi, [CMD_READ_STATUS1], 1)
    return (data[0] & 0x01)


# Get JEDEC ID
#data = xfer(spi, [CMD_JEDEC_ID], 3)
#print_hex(data)


addr = [0x00, 0x00, 0x00]

# Erase block
xfer(spi, [CMD_WRITE_ENABLE])
#xfer(spi, [CMD_BLOCK_ERASE] + addr)
xfer(spi, [CMD_CHIP_ERASE])

while busy(spi):
    pass


# Read data
data = xfer(spi, [CMD_PAGE_READ] + addr, 10)
print_hex(data)

## Write data
#data = 10 * [0xAF]
#xfer(spi, [CMD_WRITE_ENABLE])
#data = xfer(spi, [CMD_PAGE_WRITE] + addr + data)

## Read data
#data = xfer(spi, [CMD_PAGE_READ] + addr, 10)
#print_hex(data)

