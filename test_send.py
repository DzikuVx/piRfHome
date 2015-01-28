#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Requires http://abyz.co.uk/rpi/pigpio/
'''
import virtualwire
import time
import pigpio
import piRfHome

if __name__ == "__main__":

	pi = pigpio.pi()
	tx = virtualwire.tx(pi, 4, 1000) # Specify Pi, tx gpio, and baud.

	sender = piRfHome.rf(tx, 1)

	# set 5 retries with 0.2 second delay
	sender.setRetries(0, 0.5)

	#send 102010 as Weather/Pressure to device 0x02 with datatype uint32
	# sender.send(0x02, 0x41, 0x02, 102011)

	count = 0
	
	while True:
		count = count + 1
		#send timestamp

		pi.write(23, 1)

		sender.send(0x02, 0x00, 0x02, int(time.time()))

		pi.write(23, 0)

		print(count)

		time.sleep(1)

	tx.cancel()
	pi.stop()
