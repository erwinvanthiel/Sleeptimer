import subprocess

def shutdown(delay):

	if check_platform() == 'Windows':
		command = ['shutdown','-s','-t',delay]
	elif check_platform() == 'Linux':
		command = ['shutdown','-h',delay]
	elif check_platform() == 'OSX':
		command = ['']
		
	o = subprocess.check_output(command, shell=True)


def check_platform():
	from sys import platform
	if platform == "linux" or platform == "linux2":
	    return 'Linux'
	elif platform == "darwin":
	    return 'OSX'
	elif platform == "win32":
	    return 'Windows'

