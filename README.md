# piRfHome
Raspberry Pi RF 433 MHz protocol implementation for Home Automation 

## Description

This python module for Raspberry Pi allows to send and receive wireless messages over variety of cheap RF modules.
It is using VirtualWire protocol known from Arduino and adds additional layter on top of it.

##Dependiences

### pigpio library http://abyz.co.uk/rpi/pigpio/

```
wget abyz.co.uk/rpi/pigpio/pigpio.zip
unzip pigpio.zip
cd PIGPIO
make
make install
```

pigpio has to be running as a service. To start:
`sudo /home/pi/PIGPIO/pigpiod`

##Hardware
This has been tested with FS1000A sender and XY-MK5V receiver. Communication over Virtual Wire was successful with Arduino Uno and Arduino Pro Micro.
