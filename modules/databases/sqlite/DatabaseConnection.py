import sqlite3

class DatabaseConnection:
	
	def __init__(self):
		self.connection = sqlite3.connect("./db/main.db")
		self.cursor = self.connection.cursor()

	def query(self, sql):
		result = self.cursor.execute(sql)
		self.cursor.close()
		return result