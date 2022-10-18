from .brainfuck import evaluate_brainfuck
from .visualize import visualize_evaluation, set_visualization_refresh_rate
import sys, os, select


def incorrect_usage():
	sys.stdout.write("Incorrect usage: use the -h flag to display a help message. \n")
	sys.exit(1)


def help_message():
	sys.stdout.write("""NAME	
	brainfuck.py -- A lightweight pure python brainfuck interpreter

SYNOPSIS
	brainfuckpy [-h] [-vis [-vrr rate]] [file|program]

DESCRIPTION
	Either pipe in, provide as an argument or provide a file containing a valid program.
	
	-vis --visualize
			Run the code visualizer. Optionally the -vrr flag can be used to set a refresh rate of the visualization.
	-vrr --visualization-refresh-rate
			Set the amount of times per second the visualizer updates. Provide this refresh rate as the immediate next
			argument.
	-h, --help
			Display this message.\n""")


def main():
	# Please ignore this entire first block, it is distinctly awful
	evaluator = evaluate_brainfuck
	if "-vis" in sys.argv or "--visualize" in sys.argv:
		evaluator = visualize_evaluation
		try:
			if "-vrr" in sys.argv:
				speed_index = sys.argv.index("-vrr") + 1
				set_visualization_refresh_rate(float(sys.argv[speed_index]))
			elif "--visualization-refresh-rate" in sys.argv:
				speed_index = sys.argv.index("--visualization-refresh-rate") + 1
				set_visualization_refresh_rate(float(sys.argv[speed_index]))
		except ValueError:
			incorrect_usage()
	elif "-vrr" in sys.argv or "--visualization-refresh-rate" in sys.argv:
		incorrect_usage()

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
