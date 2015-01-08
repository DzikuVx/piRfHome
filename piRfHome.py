import virtualwire
import time
import pigpio

class rf():

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