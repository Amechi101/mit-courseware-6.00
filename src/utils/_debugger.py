import sys
import time

def debugger(debugger, name):

	if debugger:
		sys.stdout.write(name + "\n" )
		time.sleep(1.0)
		sys.stdout.flush()
