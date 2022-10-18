#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import argparse


version = ''
with open('__init__.py') as f:
	version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE)[1]

LIST_COMMANDS = {
        '--help': '\tShow this help message',
        '-h' : 'ref::--help',
        '--version': '\tShow the version of the program',
        '-v' : 'ref::--version',
		'--langs': '\tShow the list of supported languages',
		'-ls': 'ref::--langs',
}

LANGS = {
	''	: 'C++',
	''	: 'C',
	''	: 'Python',
	''	: 'Ruby',
}

def searchForReference(command):
	return next((f' {key}, {command}' for key, value in LIST_COMMANDS.items() if value.startswith('ref::') and value[5:] == command), command)

def searchSimilarCommand(command):
	"""Search for a similar command in the list of commands
	   ex : searchSimilarCommand('--hlp') -> '--help',
	        searchSimilarCommand('--vers') -> '--version'
			searchSimilarCommand('--versio') -> '--version'
			searchSimilarCommand('--h') -> '-h'
	"""
	if command in LIST_COMMANDS:
		return command
	if command in ['-h', '-v', '-ls']:
		return command
	if command.startswith('--'):
		return next((key for key in LIST_COMMANDS if key.startswith(command)), None)
	if command.startswith('-'):
		first_letter = command[1]
		return next((key for key in LIST_COMMANDS if key.startswith('-') and key[1] == first_letter), None)
	return None

def create_help():
	help = "\n detectchange [options]\n\n" + " [options] are optionnal, no options run the tool in default mode\n\n"

	for command in LIST_COMMANDS:
		if LIST_COMMANDS[command].startswith('ref::'):
			continue
		help += f'{searchForReference(command)}{LIST_COMMANDS[command]}\n'
	return help



def main():
	parser = argparse.ArgumentParser(description='Detect changes in a directory and execute a program on saved changes', usage=create_help())
	parser.add_argument('--version', action='version', version=f'{version}')
	parser.add_argument('-v', action='version', version=f'{version}')
	parser.add_argument('--langs', action='store_true', help='Show the list of supported languages')
	parser.add_argument('-ls', action='store_true', help='Show the list of supported languages')

	try:
		args = parser.parse_args()
		# if no arguments are given, run the tool in default mode
		run = len(sys.argv) == 1
	except SystemExit as e:
		# If the user enter a wrong command
		if e.code == 2:
			# Get the command
			command = sys.argv[1]
			if similar_command := searchSimilarCommand(command):
				print(f'Unknown command : {command}, did you mean : {similar_command} ?')
			else:
				print(f'Unknown command : {command}')
			sys.exit(1)
		else:
			sys.exit(e.code)

	if args.langs:
		for icon in LANGS:
			print(f'{icon} {LANGS[icon]}')
		return

	if args.ls:
		for icon in LANGS:
			print(f'{icon} {LANGS[icon]}')
		return

	if run:
		from changedetector import detectchange
		detectchange.activate(SHELL_ARG=True)

if __name__ == '__main__':
	main()
