#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
Requires http://abyz.co.uk/rpi/pigpio/
'''

import virtualwire
import time
import pigpio

class PapayaRF():

	def __init__(self, vw, sender):
		self.vw = vw
		self.sender = sender

	def send(self, receiver, messageType, dataType, message):

		msg = []

		msg.append(receiver)
		msg.append(messageType)
		msg.append(self.sender)
		msg.append(dataType)

		if dataType == 0x02:
			msg = msg + [(message>>(8*i))&0xff for i in range(3,-1,-1)]

		self.vw.put(msg)

if __name__ == "__main__":

	pi = pigpio.pi()
	tx = virtualwire.tx(pi, 17, 2000) # Specify Pi, tx gpio, and baud.

	sender = PapayaRF(tx, 1);

	#send 102010 as Weather/Pressure to device 0x02 with datatype uint32
	# sender.send(0x02, 0x41, 0x02, 102011)
	
	while True:
		#send timestamp

		pi.write(23, 1)

		sender.send(0x02, 0x00, 0x02, int(time.time()))
		tx.waitForReady()

		pi.write(23, 0)

		time.sleep(1)

	#after sending we have to make a delay
	# tx.waitForReady()

	tx.cancel()
	pi.stop()