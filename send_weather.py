#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Requires http://abyz.co.uk/rpi/pigpio/
'''
import virtualwire
import time
import pigpio
import piRfHome
import sqlite3, os

if __name__ == "__main__":

	pi = pigpio.pi()
	tx = virtualwire.tx(pi, 4, 2000) # Specify Pi, tx gpio, and baud.

	sender = piRfHome.rf(tx, 0x01)

	# set 5 retries with 0.2 second delay
	sender.setRetries(2, 1)

	#send 102010 as Weather/Pressure to device 0x02 with datatype uint32
	# sender.send(0x02, 0x41, 0x02, 102011)

	# We are prepared, so let's connect to db

	conn = sqlite3.connect(os.path.dirname(os.path.realpath(__file__)) + '/data.db')

	cur = conn.cursor()
	cur.execute('SELECT Temperature, Humidity FROM readouts_external ORDER BY `Date` DESC LIMIT 1')

	data = cur.fetchone()

	if data == None:
		exit()

	cur = conn.cursor()
	cur.execute('SELECT Pressure, WindSpeed FROM external_data ORDER BY `Date` DESC LIMIT 1')

	dataExt = cur.fetchone()

	if dataExt == None:
		exit()

	conn.close()

	pi.write(23, 1)

	#send tempearture
	val = int(round(data[0]))
	sender.send(0x00, 0x40, 0x05, val)

	time.sleep(1)

	#send pressure
	val = int(round(dataExt[0] * 100))
	print("Pressure: " + str(val));
	sender.send(0x00, 0x41, 0x05, val)

	time.sleep(1)

	#send humidity
	val = int(round(data[1]))
	sender.send(0x00, 0x42, 0x05, val)

	time.sleep(1)

	#send windspeed
	val = int(round(dataExt[1]))
	sender.send(0x00, 0x49, 0x05, val)

	pi.write(23, 0)

	# count = 0
	
	# while True:
	# 	count = count + 1
	# 	#send timestamp

	# 	pi.write(23, 1)

	# 	sender.send(0x02, 0x00, 0x02, int(time.time()))

	# 	pi.write(23, 0)

	# 	print(count)

	# 	time.sleep(1)

	tx.cancel()
	pi.stop()
