from configparser import ConfigParser
from modules.databases.sqlite.DatabaseInit import DatabaseInit as SqliteInit
import os

class DatabaseInit:
	config = ConfigParser()

	@staticmethod
	def checkDbStatus():
		DatabaseInit.config.read("./config.cfg")
		dbType = DatabaseInit.config.get('db', 'dbType')

		# If Sqlite3
		if dbType == "sqlite" and not os.path.exists("./db/main.db"):
			if not os.path.exists("./db") : os.mkdir("./db")
			with open('./db/main.db', 'w') : pass
			SqliteInit.init()