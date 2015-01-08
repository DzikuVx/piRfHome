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
	tx = virtualwire.tx(pi, 4, 2000) # Specify Pi, tx gpio, and baud.

	sender = piRfHome.rf(tx, 1);

	#send 102010 as Weather/Pressure to device 0x02 with datatype uint32
	# sender.send(0x02, 0x41, 0x02, 102011)
	
	while True:
		#send timestamp

		pi.write(23, 1)

		sender.send(0x02, 0x00, 0x02, int(time.time()))
		tx.waitForReady()

		pi.write(23, 0)

		time.sleep(1)

	tx.cancel()
	pi.stop()