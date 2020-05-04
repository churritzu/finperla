import argparse

class CLIArgs:
	
	def __init__(self):
		self._parser = argparse.ArgumentParser(description='FinPerla CLI.')
		self._parser.add_argument("-i", "--income", action="store_true", help="Create and income")
		self._parser.add_argument("-e", "--expense", action="store_true", help="Create an expense")
		self._parser.add_argument("--reset-conf", action="store_true", help="Reset the configuration file")
		self._args = self._parser.parse_args()
	
	def getParser(self): return self._parser
	def getArgs(self): return self._args
