from . import visualize
from typing import Callable
import sys

TAPE_SIZE = 30_000


def get_matching_brackets(program: str) -> tuple[dict[int, int], dict[int, int]]:
	"""Gets the mappings required to match opening brackets to their closings, and vice-versa.

	Returns:
		A tuple containing two elements, the first of which mapping the opening brackets to their closing brackets. The
		second element is the opposite, mapping the closing brackets to their respective opening brackets."""
	opening_to_closing, closing_to_opening = {}, {}
	opened_brackets = []
	for pointer, command in enumerate(program):
		if command == "[":
			opened_brackets.append(pointer)
		if command == "]":
			matching_opening = opened_brackets.pop(-1)
			opening_to_closing[matching_opening] = pointer
			closing_to_opening[pointer] = matching_opening

	return opening_to_closing, closing_to_opening


def strip_bad_characters(program: str) -> str:
	"""Removes any characters that are not evaluate_brainfuck commands, ensuring comments and whitespace are allowed."""
	return "".join(filter(lambda x: x in [">", "<", "+", "-", ".", ",", "[", "]"], program))


def evaluate_processed(program: str,
					   input_callback: Callable[[], int] = None,
					   output_callback: Callable[[int], None] = None,
					   do_visualization: bool = False):
	"""Interprets `program`. Note that `program` should only contain evaluate_brainfuck commands, if any other characters are
	passed, it will likely behave fine, but undefined.

	Args:
		program: The program to run.
		input_callback: The function that is called when the program requests input (i.e. encounters a `,`). This should
			return an integer to write to the cell. Will default to prompting the user for input if left blank.
		output_callback: The function that is called when the program wants to output a byte. Should take an integer as
			an argument. Will default to writing to stdout if left blank.
		do_visualization: Whether the function should display its operations. Defaults to `False`."""
	if input_callback is None:
		input_callback = lambda: int(input())
	if output_callback is None:
		output_callback = lambda x: sys.stdout.write(chr(x))
	tape = [0 for _ in range(TAPE_SIZE)]
	head_position = 0
	code_position = 0

	opening_to_closing, closing_to_opening = get_matching_brackets(program)

	while code_position < len(program):
		cmd = program[code_position]

		if cmd == ">":
			head_position += 1
		elif cmd == "<":
			head_position -= 1
		elif cmd == "+":
			tape[head_position] += 1
		elif cmd == "-":
			tape[head_position] -= 1
		elif cmd == ".":
			output_callback(tape[head_position])
		elif cmd == ",":
			tape[head_position] = input_callback()

		if cmd == "[" and tape[head_position] == 0:
			code_position = opening_to_closing[code_position]
		elif cmd == "]" and tape[head_position] != 0:
			code_position = closing_to_opening[code_position]

		if do_visualization:
			visualize.write_visualization(program, tape, code_position, head_position)
		code_position += 1


def evaluate_brainfuck(program: str, **kwargs):
	"""Completely evaluates and runs `program`.

	Args:
		program: The program to run.
		*args: For usage please see `evaluate_brainfuck.evaluate_processed`."""
	program = strip_bad_characters(program)
	evaluate_processed(program, **kwargs)
