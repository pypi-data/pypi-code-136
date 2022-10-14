from .brainfuck import evaluate_brainfuck
from .visualize import visualize_evaluation
import sys, os, select


def incorrect_usage():
	sys.stdout.write("Incorrect usage: use the -h flag to display a help message. \n")


def help_message():
	sys.stdout.write("""NAME	
	evaluate_brainfuck.py -- A lightweight pure python evaluate_brainfuck interpreter

SYNOPSIS
	brainfuckpy [-h] [-vis] [file|program]

DESCRIPTION
	Either pipe in, provide as an argument or provide a file containing a valid program.
	
	-vis --visualize
			Run the code visualizer.
	-h, --help
			Display this message.\n""")


def main():
	evaluator = evaluate_brainfuck
	if "-vis" in sys.argv or "--visualize" in sys.argv:
		evaluator = visualize_evaluation

	if len(sys.argv) == 1 and select.select([sys.stdin, ], [], [], 0.0)[0]:
		prgm = sys.stdin.read()
		evaluator(prgm)
	elif len(sys.argv) == 1:
		incorrect_usage()
	elif os.path.isfile(sys.argv[-1]):
		with open(sys.argv[-1]) as file:
			prgm = file.read()
		evaluator(prgm)
	elif sys.argv[1] in {"-h", "--help"}:
		help_message()
	elif sys.argv[-1]:
		prgm = sys.argv[-1]
		evaluator(prgm)
	else:
		incorrect_usage()


if __name__ == '__main__':
	main()
