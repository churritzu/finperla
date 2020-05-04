import datetime
import re

class CLIIncome():
	_amount = 0.00
	_date = datetime.date.today().strftime("%Y-%m-%d")
	_desc = ""

	def __init__(self):
		print("** Welcome to the Cli Income Interface. **\n")
		self.setAmount()
		self.setDate()
		self.setDescription()

		print(self._amount)
		print(self._date)
		print(self._desc)
		print(self.getDate())

	def getAmount(self): return self._amount
	
	def getDescription(self): return self._desc
	
	def getDate(self): 
		rawDateNumbers = "".join(self._date.split("-"))
		return rawDateNumbers[0:4] +"-"+rawDateNumbers[4:6]+"-"+rawDateNumbers[6:]

	def setAmount(self):
		while self._amount < 0.01:
			try:
				self._amount = float(input("Please enter the amount you received: "))
			except:
				print('\033[93m' + "Notice: "+ '\033[0m' + "The income value has to be greater than 0.00.\n")
			
	def setDate(self):
		check = False

		while check == False:
			d = input("Enter the day of the operation (default: " + self._date + "): ")
			
			if d and self.__checkDateFormat(d):
				self._date = d
				check = True
			elif d and not self.__checkDateFormat(d):
				print('\033[93m' + "Notice: "+ '\033[0m' + "The correct format is YYYY-MM-DD.\n")
			else: 
				check = True

	def setDescription(self):
		self._desc = input("Description of the transaction:\n")

	def __checkDateFormat(self, str):
		# YYYY-mm-dd Format
		yyyymmdd = '[12]\d{3}-?(0[0-9]|1[0-2])-?([0-2][0-9]|3[0-1])'

		return re.fullmatch(yyyymmdd, str.strip())