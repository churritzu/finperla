from modules.incomes.CLIIncome import CLIIncome
from modules.settings.Settings import Settings
from modules.cli.CLIargs import CLIArgs

if __name__ == "__main__":
	cliargs = CLIArgs()
	args = cliargs.getArgs()
	
	if(args.income): income = CLIIncome()
	elif(args.expense): print("The Expense flag has called", args.expense)
	elif(args.reset_conf): Settings.createSettingsFile()
	else:	print(cliargs.getParser().print_help())