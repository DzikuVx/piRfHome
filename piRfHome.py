import virtualwire
import time
import pigpio

class rf():

	def __init__(self, vw, sender):
		self.vw = vw
		self.sender = sender
		self.messageId = 0
		self.retriesCount = 1
		self.retriesDelay = 0.2

	def _generateMessageId(self):
		self.messageId = self.messageId + 1;

		if self.messageId == 256:
			self.messageId = 0

	def setRetries(self, count, delay):
		self.retriesCount = count
		self.retriesDelay = delay

	def send(self, receiver, messageType, dataType, message):

		msg = []

		msg.append(receiver)
		msg.append(messageType)
		msg.append(self.sender)
		msg.append(dataType)
		msg.append(self.messageId)

		if dataType == 0x02:
			# uint32
			msg = msg + [(message>>(8*i))&0xff for i in range(3,-1,-1)]
		elif dataType == 0x05:
			# int32
			msg = msg + [(message>>(8*i))&0xff for i in range(3,-1,-1)]

		self._generateMessageId()

		# Message is prepared
		bGo = True
		iIndex = 0

		while bGo:

			self.vw.put(msg)
			self.vw.waitForReady()

			iIndex = iIndex + 1
			if iIndex > self.retriesCount:
				bGo = False
			else:
				time.sleep(self.retriesDelay)