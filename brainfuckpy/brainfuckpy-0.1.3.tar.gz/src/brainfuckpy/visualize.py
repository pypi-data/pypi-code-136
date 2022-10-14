from . import brainfuck
from rich.console import Console
import time

console = Console()

CODE_ACCENT = "bold red"
TAPE_ACCENT = "bold red"

SECOND_PER_REFRESH = 0.1

outputs = []


def _visualization_output_callback(byte: int):
	outputs.append(chr(byte))


def _visualization_input_callback() -> int:
	return int(console.input("\n"))


def get_subset(tape: list[str], centered_at: int, length: int=40) -> list[str]:
	"""Gets a subset of the tape of length `length` in order to make the visualizer wrap lines better."""
	minimum = centered_at - length//2
	maximum = centered_at + length//2

	if minimum < 0 or maximum > brainfuck.TAPE_SIZE:
		return tape[minimum:] + tape[:maximum]
	else:
		return tape[minimum:maximum]


def write_visualization(program: str, tape: list[int], code_pointer: int, head_position: int):
	"""Writes a single cycle of the visualization, means clearing and displaying the information."""
	# construct the tape
	tape_with_highlight = [i for i in tape]
	tape_with_highlight[head_position] = f"[{TAPE_ACCENT}]{tape[head_position]}[/{TAPE_ACCENT}]"
	tape_with_highlight = get_subset(tape_with_highlight, head_position)
	tape_text = ", ".join(str(i) for i in tape_with_highlight)

	# construct the program
	program_text = program[:code_pointer] + f"[{CODE_ACCENT}]" + program[code_pointer] + f"[/{CODE_ACCENT}]" + program[code_pointer+1:]

	# construct the outputs
	output_text = "".join(outputs)

	console.clear()
	console.print(tape_text)
	console.print("\n")
	console.print(program_text)
	console.print("\n")
	console.print(output_text)

	time.sleep(SECOND_PER_REFRESH)


def visualize_evaluation(program: str):
	"""Completely visualizes the execution of `program`."""
	brainfuck.evaluate_brainfuck(
		program,
		input_callback=_visualization_input_callback,
		output_callback=_visualization_output_callback,
		do_visualization=True
	)

