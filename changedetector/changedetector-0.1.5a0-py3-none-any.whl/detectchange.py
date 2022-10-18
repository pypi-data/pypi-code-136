import time
import os
import pathlib
import sys
import re
import argparse

from watchdog.observers import Observer
from pyfiglet import Figlet

# add the base directory to the path
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from colors import Colors
from menu import menu
from wrapperComponents import WrapperComponents as wp

# handlers
from wrs import WrsHandler
from wro import WroHandler

class Entries:
    def __init__(self):
        self.entries = {}

    def add(self, name: str, value):
        self.entries[name] = value

    def get(self, name: str) -> str | list | None | bool | int | list[str]:
        return self.entries[name]

    def makeMode(self):
        MODE = menu(["Watch and Run Self (WRS)", "Watch and Run Other (WRO)"],
                    "Choose the mode you want to use:")
        if MODE == "Watch and Run Self (WRS)":
            self.add("mode", "wrs")
        elif MODE == "Watch and Run Other (WRO)":
            self.add("mode", "wro")

    def makeLang(self):
        self.language = menu(["python", "ruby", "c", "c++"],
                        "Choose the language you want to use:")
        self.add("lang", self.language)

    def makeCParams(self):
        wywu = wp.textWrapBold("Enter the compiler name you want to use : ")
        ccho = wp.textWrapBold("( g++ | gcc | ...) ", Colors.GREEN)
        CMD = input(f"{wywu}{ccho}")
        self.add("cmd", CMD)
        opt1 = wp.textWrapBold("Enter flags you want to use : ")
        default = wp.textWrapBold("(none) ", Colors.GREEN)
        FLAGS = input(f"{opt1}{default}").split(" ")
        if FLAGS in ["none", "", " "]:
            FLAGS = [""]
        self.add("flags", FLAGS)
        output = wp.textWrapBold(
            "Enter the output attributes you want to use: ")
        default = wp.textWrapBold("(-o) ", Colors.GREEN)
        OUTPUT_ATTRIBUTE = input(f"{output}{default}")
        if OUTPUT_ATTRIBUTE in ["", " "]:
            OUTPUT_ATTRIBUTE = "-o"
        self.add("output_attr", OUTPUT_ATTRIBUTE)
        output_name = wp.textWrapBold("Enter the output name you want: ")
        default = wp.textWrapBold("(out) ", Colors.GREEN)
        OUTPUT_FILE = input(f"{output_name}{default}").lower()
        if OUTPUT_FILE in ["", " "]:
            OUTPUT_FILE = "out"
        self.add("output_file", OUTPUT_FILE)

    def makeCommand(self):
        try:
            if self.language == "python":
                CMD = ["py", "python"]
                self.add("cmd", CMD)
            elif self.language == "ruby":
                CMD = ["ruby", "ruby"]
                self.add("cmd", CMD)
            elif self.language in ["c++", "c"]:
                self.makeCParams()
            else:
                err = wp.textWrapBold("Wrong language", Colors.RED)
                print(f"❌ {err}")
                sys.exit(1)
        except KeyboardInterrupt:
            print(f"\n{Colors.RED}{Colors.BOLD}Error:{Colors.END} KeyboardInterrupt")
            sys.exit(1)

    def makePaths(self):
        # Automatic detection of the working directory
        BASE_DIR = pathlib.Path(__file__).parent.absolute().cwd()
        self.add("base_dir", BASE_DIR)
        try:
            FILE = input(
                f"{Colors.BOLD}Enter the file you want to run in the working directory\n|-> {BASE_DIR}... \n{Colors.END}")
            if self.get("mode") == "wro":
                FILE_TO_WATCH = input(
                    f"{Colors.BOLD}Enter the file you want to watch in the working directory\n|-> {BASE_DIR}... \n{Colors.END}")

        except KeyboardInterrupt:
            print(f"\n{Colors.RED}{Colors.BOLD}Error:{Colors.END} KeyboardInterrupt")
            sys.exit(1)
        THE_FILE = os.path.join(self.get("base_dir"), f'{FILE}')
        self.add("the_file", THE_FILE)
        if self.get("mode") == "wro":
            THE_FILE_TO_WATCH = os.path.join(self.get("base_dir"), f'{FILE_TO_WATCH}')
            self.add("the_file_to_watch", THE_FILE_TO_WATCH)
        print(self.get("the_file"))
        # Check if the file's path is valid exist
        if not os.path.exists(THE_FILE):
            err = wp.textWrapBold(f"The file {THE_FILE} doesn't exist", Colors.RED)
            print(f"❌ {err}")
            sys.exit(1)

        # Check if the file's path to watch is valid exist
        if self.get("mode") == "wro" and not os.path.exists(THE_FILE_TO_WATCH):
            err = wp.textWrapBold(
                f"The file {THE_FILE_TO_WATCH} doesn'tOUTPUT_FILE exist", Colors.RED)
            print(f"❌ {err}")
            sys.exit(1)

        if self.get("lang") in ["c++", "c"]:
            COMMAND_LIST = [self.get("cmd")]
            if self.get("flags")[0] != "":
                COMMAND_LIST.extend(iter(self.get("flags")))
            COMMAND_LIST.append(self.get("the_file"))
            COMMAND_LIST.append(self.get("output_attr"))
            COMMAND_LIST.append(self.get("output_file"))
            self.add("command_list", COMMAND_LIST)
        else:
            self.add("command_list", None)

    def make(self):
        self.makeMode()
        self.makeLang()
        self.makeCommand()
        self.makePaths()

    def __str__(self):
        return str(self.entries)

    def __repr__(self):
        return str(self.entries)



class BeautifulOutput:
    def __init__(self, e: Entries=None) -> None:
        self.lang = e.get("lang") if e else None
        self.the_file = e.get("the_file") if e else None

    def _start(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        f = Figlet(font='colossal', width=80)
        print(f.renderText('Change'))
        print(f.renderText('Detect'))

    def _out(self, lang: str):
        custom_fig = Figlet(font='colossal')
        print(custom_fig.renderText(lang))
        print(f"{Colors.BOLD}File: {Colors.END}{self.the_file}")

    def _run(self):
        # clear the terminal
        os.system('cls' if os.name == 'nt' else 'clear')
        if self.lang in ["ruby", "rb"]:
            self._out("Ruby")
        elif self.lang in ["python", "py", "python3"]:
            self._out("Python")
        elif self.lang in ["c++", "cpp"]:
            self._out("C++")
        elif self.lang == "c":
            self._out("C")

    def __str__(self):
        return f"BeautifulOutput({self.lang}, {self.the_file})"

class _Watcher:

    def __init__(self, handler_type: WrsHandler, dir_to_watch: str):
        self.DIRECTORY_TO_WATCH = dir_to_watch
        self.observer = Observer()
        self.handler_type = handler_type

    def run(self):
        event_handler = self.handler_type
        self.observer.schedule(
            event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except Exception or KeyboardInterrupt as e:
            self.observer.stop()
            print (f"{Colors.RED}{Colors.BOLD}Error:{Colors.END} {e}")

        self.observer.join()


def activate() -> None:
    """
    ACTIVATE
    --------
    Detect change in the working directory and execute the program chosen.
    Two modes of execution are available to you:
        * Based on observing a specific file for changes and executing another file. (Watch and Run Other) `WRO`
        * Observing a certain file and using the same file to conduct the test. (Watch and Run Self) `WRS`
    """

    BeautifulOutput()._start()

    try:
        e = Entries()
        e.make()

        if e.get("mode") == "wrs":
            wh = WrsHandler(
                the_file=e.get("the_file"),
                command_list=e.get("command_list"),
                language=e.get("lang"),
                base_dir=e.get("base_dir"),
                cmd=e.get("cmd")
            )
            BeautifulOutput(e)._run()
            mode = wp.textWrapBold("(WRS)", Colors.GREEN)
        else:
            wh = WroHandler(
                the_file=e.get("the_file"),
                the_file_to_watch=e.get("the_file_to_watch"),
                command_list=e.get("command_list"),
                language=e.get("lang"),
                base_dir=e.get("base_dir"),
                cmd=e.get("cmd")
            )
            BeautifulOutput(e)._run()
            mode = wp.textWrapBold("(WRO)", Colors.GREEN)
        w = _Watcher(wh, e.get("base_dir"))
        print(" ")
        print(f"Watching in {mode} mode...")
        print(" ")
        w.run()
    except KeyboardInterrupt:
        # pipe the error number to the shell
        print(f"\n{Colors.GREEN}{Colors.BOLD}Change Detector Stopped{Colors.END}")
        sys.exit(0)


class Assets:
    base_dir = os.path.dirname(os.path.abspath(__file__))

    @classmethod
    def get_version(cls):
        with open(os.path.join(cls.base_dir, '__init__.py')) as f:
            version = re.search(
                r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE)[1]
        return version

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
	return next((f' {key}, {command}' for key, value in Assets.LIST_COMMANDS.items() if value.startswith('ref::') and value[5:] == command), command)

def searchSimilarCommand(command):
	"""Search for a similar command in the list of commands
	   ex : searchSimilarCommand('--hlp') -> '--help',
	        searchSimilarCommand('--vers') -> '--version'
			searchSimilarCommand('--versio') -> '--version'
			searchSimilarCommand('--h') -> '-h'
	"""
	if command in Assets.LIST_COMMANDS:
		return command
	if command in ['-h', '-v', '-ls']:
		return command
	if command.startswith('--'):
		return next((key for key in Assets.LIST_COMMANDS if key.startswith(command)), None)
	if command.startswith('-'):
		first_letter = command[1]
		return next((key for key in Assets.LIST_COMMANDS if key.startswith('-') and key[1] == first_letter), None)
	return None

def create_help():
	help = "\n detectchange [options]\n\n" + " [options] are optionnal, no options run the tool in default mode\n\n"

	for command in Assets.LIST_COMMANDS:
		if Assets.LIST_COMMANDS[command].startswith('ref::'):
			continue
		help += f'{searchForReference(command)}{Assets.LIST_COMMANDS[command]}\n'
	return help



def main():
	parser = argparse.ArgumentParser(description='Detect changes in a directory and execute a program on saved changes', usage=create_help())
	parser.add_argument('--version', action='version', version=f'{Assets.get_version()}')
	parser.add_argument('-v', action='version', version=f'{Assets.get_version()}')
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
		for icon in Assets.LANGS:
			print(f'{icon} {Assets.LANGS[icon]}')
		return

	if args.ls:
		for icon in Assets.LANGS:
			print(f'{icon} {Assets.LANGS[icon]}')
		return

	if run:
		activate()


if __name__ == '__main__':
    main()
