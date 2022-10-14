colors = {
	'clear': '\033[m',
	'black': '\033[30m',
	'red': '\033[31m',
	'green': '\033[32m',
	'yellow': '\033[33m',
	'blue': '\033[34m',
	'magenta': '\033[35m',
	'cyan': '\033[36m',
	'white': '\033[37m'
}
backgroundColors = {
	'black': '\033[40m',
	'red': '\033[41m',
	'green': '\033[42m',
	'yellow': '\033[43m',
	'blue': '\033[44m',
	'magenta': '\033[45m',
	'cyan': '\033[46m',
	'white': '\033[47m'
}
types = {
	1:'--',
	2:'=-',
	3:'*-',
	4:'==',
	5:'++',
	6:'**',
	7:'+-'
}

def info():
	print("""
Package Info:
Version: 1.0 (Alpha)
Author: WillyPyDev
Last modified: 10/10/2022 (MM/DD/AA)
""")

def help():
	printLine(type=3, amount=15, backgroundColor=None, color=None, reverse=False, end=True)
	print("HELP" + f"{types[3]}" * 15)
	print("""
It is extremely important to specify each variable in the function, or write each one in the correct order:
type, quantity, background color, font color, reverse or not, and final line break.

Each variable has a type, and if placed wrong it results in an error.

type( Type of character pair ) = int
amount( Amount of pairs ) = int
backgroundColor( Background Color ) = 'red' or any other available color
color( Letter color ) = 'green' or any other available.
reverse( Whether the pair should be in reverse order or not ) = True or False
end( New line break at the end ) = True or False

Correct order:
(type, amount, backgroundColor, color, reverse, end)

To see all available colors and backgrounds, access the repository.
""")

def help_error():
	print("""Key Error!
Please declare the arguments for each type specified.
For more information go to X or issue the help() command in the Python terminal.
""")

def whatColors():
	print(colors, end='\n')
	print(backgroundColors)

def printLine(type=int, amount=int, backgroundColor=str, color=str, reverse=bool, end=bool):
	try:
		if (backgroundColor == None):
			if (color == None):
				if (reverse == True):
					if (end == True):
						print(f"{types[type][::-1]}" * amount, end='')
				else:
					if (end == True):
						print(f"{types[type]}" * amount, end='')
					else:
						print(f"{types[type]}" * amount)
			else:
				if (reverse == True):
					if (end == True):
						print(f"{colors[color]}{types[type][::-1]}{colors['clear']}" * amount, end='')
					else:
						print(f"{colors[color]}{types[type][::-1]}{colors['clear']}" * amount)
				else:
					if (end == True):
						print(f"{colors[color]}{types[type]}{colors['clear']}" * amount, end='')
					else:
						print(f"{colors[color]}{types[type]}{colors['clear']}" * amount)
		else:
			if (color == None):
				if (reverse ==  True):
					if (end == True):
						print(f"{backgroundColors[backgroundColor]}{types[type][::-1]}{colors['clear']}" * amount, end='')
					else:
						print(f"{backgroundColors[backgroundColor]}{types[type][::-1]}{colors['clear']}" * amount)
				else:
					if (end == True):
						print(f"{backgroundColors[backgroundColor]}{types[type]}{colors['clear']}" * amount, end='')
					else:
						print(f"{backgroundColors[backgroundColor]}{types[type]}{colors['clear']}" * amount)
			else:
				if (reverse ==  True):
					if (end == True):
						print(f"{backgroundColors[backgroundColor]}{colors[color]}{types[type][::-1]}{colors['clear']}" * amount, end='')
					else:
						print(f"{backgroundColors[backgroundColor]}{colors[color]}{types[type][::-1]}{colors['clear']}" * amount)
				else:
					if (end == True):
						print(f"{backgroundColors[backgroundColor]}{colors[color]}{types[type]}{colors['clear']}" * amount, end='')
					else:
						print(f"{backgroundColors[backgroundColor]}{colors[color]}{types[type]}{colors['clear']}" * amount)
	except KeyError:
		help_error()
