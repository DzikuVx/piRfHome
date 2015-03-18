import smbus
import time

# define I2C bus number
BUS_NUMBER = 1

# define device address
DEVICE_ADDR = 0x43

bus = smbus.SMBus(BUS_NUMBER)

for i in range(0, 9):

	val = bus.read_byte(DEVICE_ADDR)

	print str.join("", ("%02x" % val))
