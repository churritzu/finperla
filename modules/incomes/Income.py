from modules.databases.sqlite.Database import Database

class Income(Database):
	table = "income"

	id = None
	amount = None
	trans_date = None
	description = None

	def __init__(self, **kwargs): self.__dict__.update(kwargs)

	def getId(self): return self.id if self.id else None
	def getAmount(self): return self.amount if self.amount else 0.00
	def getTransDate(self): return self.trans_date if self.trans_date else "0000-00-00"
	def getDescription(self): return self.description if self.description else ""