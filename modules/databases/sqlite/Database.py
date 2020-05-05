from modules.databases.sqlite.DatabaseConnection import DatabaseConnection

class Database:
	def __init__(self): pass

	def getTable(self): return self.table

	def query(self, sql): DatabaseConnection().query(sql)

	def add(self):print("Saving Record...")
	
	def update(self): print("Updating Record...")

	def deleteRecord(self): print("Deleting Record...")

	def save(self): self.update() if self.getId() else self.add()
		
		