import time

def sec_timer(callback, seconds):
	clock = seconds
	while clock >= 0:
		callback(clock)
		clock -= 1
		time.sleep(1)
