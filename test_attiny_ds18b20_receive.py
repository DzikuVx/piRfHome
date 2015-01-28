#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
Requires http://abyz.co.uk/rpi/pigpio/
'''

import virtualwire
import time
import pigpio
import piRfHome
import string

if __name__ == "__main__":

	pi = pigpio.pi()

	rx = virtualwire.rx(pi, 18, 1000) # Specify Pi, tx gpio, and baud.
	count = 0
	while True:
		pi.write(24, 0)

		while rx.ready():
			count = count + 1
			pi.write(24, 1)
			
			out = rx.get();

			deffed = []

			for v in out:
				deffed.append(chr(v))
				
			# print deffed

			print '%d : %f' %(count, float(''.join(deffed))/10)

			# print count + " " + int(''.join(deffed))
			# temp = out[0] * 65536;
			# temp = temp + (out[1] * 256)
			# temp = temp + out[2] 

			# print(out)
			# print(temp)
			# print(327670 - reduce(lambda x, y: (x<<8) + y, out))

		time.sleep(0.1)

	rx.cancel()
	pi.stop()
