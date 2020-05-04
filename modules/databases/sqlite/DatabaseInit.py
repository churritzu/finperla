from modules.databases.sqlite.DatabaseConnection import DatabaseConnection

class DatabaseInit:

	@staticmethod
	def init():
		DatabaseInit.initIncomeTable()

	@staticmethod
	def initIncomeTable():
		print("Creating income database table....")
		db = DatabaseConnection()

		sql = """
			CREATE TABLE IF NOT EXISTS incoming (
				id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
				amount FLOAT NOT NULL,
				trans_date DATE NOT NULL,
				description TEXT NULL)"""

		incomeTable = db.query(sql)
		if incomeTable: print("Sqlite3 income table successfull created.\n")
		else: print('\033[93m' + "Notice: "+ '\033[0m' + "There was a problem creating the Sqlite3 income table.\n")