from modules.incomes.Income import Income
from modules.cli.CLIargs import CLIArgs

if __name__ == "__main__":
	cliargs = CLIArgs()
	args = cliargs.getArgs()
	
	print(args)

	if(args.income): print("The Income flag has called", args.income)
	elif(args.expense): print("The Expense flag has called", args.expense)
	else:	print(cliargs.getParser().print_help())