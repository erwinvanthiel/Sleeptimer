import time

class Clock:

	def __init__(self, hours=0, minutes=0, seconds=0):
		self.hours = hours
		self.minutes = minutes
		self.seconds = seconds

	def count_down(self, callback):
		done = (self.hours == 0) and (self.seconds == 0) and (self.minutes == 0)	
		while not done:
			callback(self)
			time.sleep(1)
			if not self.seconds == 0:
				self.seconds -= 1
			else:
				if not self.minutes == 0:
					self.seconds = 59
					self.minutes -= 1
				else:
					if not self.hours == 0:
						self.seconds = 59
						self.minutes = 59
						self.hours -= 1


	def format_time(self):
		hours = str(self.hours)
		if len(hours) == 1:
			hours = '0{0}'.format(hours)
		minutes = str(self.minutes)
		if len(minutes) == 1:
			minutes = '0{0}'.format(minutes)
		seconds = str(self.seconds)
		if len(seconds) == 1:
			seconds = '0{0}'.format(seconds)
		return '{0}:{1}:{2}'.format(hours, minutes, seconds)
