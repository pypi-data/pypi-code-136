#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re


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
	help = "\n Usage : detectchange [options]\n\n" + " [options] are optionnal, no options run the tool in default mode\n\n"

	for command in LIST_COMMANDS:
		if LIST_COMMANDS[command].startswith('ref::'):
			continue
		help += f'{searchForReference(command)}{LIST_COMMANDS[command]}\n'
	return help



def main():
	if len(sys.argv) == 1:
		from changedetector import detectchange
		detectchange.activate(SHELL_ARG=True)

	if len(sys.argv) == 2:
		if sys.argv[1] in LIST_COMMANDS:
			if sys.argv[1] in ['--help', '-h']:
				print(create_help())
			elif sys.argv[1] in ['--version', '-v']:
				print(version)
			elif sys.argv[1] in ['--langs', '-ls']:
				for lang in LANGS:
					print(f' {lang} {LANGS[lang]}')
		else:
			print(create_help())
			if similar := searchSimilarCommand(sys.argv[1]):
				print(f' You probably meant {similar}')
			print(f' detectchange : error : {sys.argv[1]} is not a valid command')
	else:
		print(create_help())
		arguments = ', '.join(sys.argv[1:])
		print(f' detectchange : error : "{arguments}" are not valid commands')


if __name__ == '__main__':
	main()
