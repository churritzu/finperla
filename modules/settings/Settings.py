from configparser import ConfigParser

class Settings:
	config = ConfigParser()
	config['global'] = {
		"debug": "true"
	}
	config['db'] = {
		'dbName': "finperla",
		'dbHost': "localhost",
		'dbPort': "3306"
	}

	@staticmethod
	def createSettingsFile(creating=False):
		response = "yes" if creating else input("Are you sure you want to reset the configuration file? (yes|no) ")
		if(response == 'yes' or response == "y"):
			with open("./config.cfg", "w") as f:
				Settings.config.write(f)