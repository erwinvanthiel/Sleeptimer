
def shutdown(delay):

	command = ['shutdown','-h',delay]
	#o = subprocess.check_output(command, shell=True)