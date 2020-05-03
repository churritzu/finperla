import argparse

class CLIArgs:
	_args = None

	def __init__(self):
		parser = argparse.ArgumentParser(description='FinPerla CLI.')
		parser.add_argument("-i", "--income", metavar="", type=None, help="Create and income")
		parser.add_argument("-e", "--expense", metavar="", type=None, help="Create an expense")
		self._args = parser.parse_args()
	
	def getArgs(self): return self._args
