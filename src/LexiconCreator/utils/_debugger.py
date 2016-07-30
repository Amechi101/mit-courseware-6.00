import sys
import time


class Debugger( object ):
	
	debugger_sleeper = 1.0

	def __init__(self, debugger, name):
		self.debugger = debugger
		self.name = name

	def logger(self):

		if self.debugger:
			sys.stdout.write(self.name + "\n" )
			time.sleep( Debugger.debugger_sleeper )
			sys.stdout.flush()
