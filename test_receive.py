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

	rx = virtualwire.rx(pi, 18, 2000) # Specify Pi, tx gpio, and baud.

	while True:

		pi.write(24, 0)

		while rx.ready():
			pi.write(24, 1)
			print(rx.get())

		time.sleep(0.1)

	rx.cancel()
	pi.stop()