import time
import os
import sys
import pathlib
from watchdog.observers import Observer
from pyfiglet import Figlet

# add the base directory to the path
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from purcent import Loader as __Loader
from colors import Colors
from menu import menu
from wrapperComponents import WrapperComponents as wp

# handlers
from wrs import WrsHandler
from wro import WroHandler


os.system('cls' if os.name == 'nt' else 'clear')
f = Figlet(font='colossal', width=80)
print(f.renderText('Change'))
print(f.renderText('Detect'))
global language
global MODE
MODE = menu(["Watch and Run Self (WRS)", "Watch and Run Other (WRO)"], "Choose the mode you want to use:")
language = menu(["python", "ruby", "c", "c++"], "Choose the language you want to use:")

try:
    if language == "python":
        CMD = ["py", "python"]
    elif language == "ruby":
        CMD = ["ruby", "ruby"]
    elif language in ["c++", "c"]:
        wywu = wp.textWrapBold("Enter the compiler name you want to use : ")
        ccho = wp.textWrapBold("( g++ | gcc | ...) ", Colors.GREEN)
        CMD = input(f"{wywu}{ccho}")
        opt1 = wp.textWrapBold("Enter flags you want to use : ")
        default = wp.textWrapBold("(none) ", Colors.GREEN)
        FLAGS = input(f"{opt1}{default}").split(" ")
        if FLAGS in ["none", "", " "]:
            FLAGS = [""]
        output = wp.textWrapBold("Enter the output attributes you want to use: ")
        default = wp.textWrapBold("(-o) ", Colors.GREEN)
        OUTPUT_ATTRIBUTE = input(f"{output}{default}")
        if OUTPUT_ATTRIBUTE in ["", " "]:
            OUTPUT_ATTRIBUTE = "-o"
        output_name = wp.textWrapBold("Enter the output name you want: ")
        default = wp.textWrapBold("(out) ", Colors.GREEN)
        OUTPUT_FILE = input(f"{output_name}{default}").lower()
        if OUTPUT_FILE in ["", " "]:
            OUTPUT_FILE = "out"
    else:
        err = wp.textWrapBold("Wrong language", Colors.RED)
        print(f"❌ {err}")
        sys.exit(1)

except KeyboardInterrupt:
    print(f"\n{Colors.RED}{Colors.BOLD}Error:{Colors.END} KeyboardInterrupt")
    sys.exit(1)

# Automatic detection of the working directory
BASE_DIR = pathlib.Path(__file__).parent.absolute().cwd()
try:
    FILE = input(f"{Colors.BOLD}Enter the file you want to run in the working directory\n|-> {BASE_DIR}... \n{Colors.END}")
    if MODE == "Watch and Run Other (WRO)":
        FILE_TO_WATCH = input(f"{Colors.BOLD}Enter the file you want to watch in the working directory\n|-> {BASE_DIR}... \n{Colors.END}")
except KeyboardInterrupt:
    print(f"\n{Colors.RED}{Colors.BOLD}Error:{Colors.END} KeyboardInterrupt")
    sys.exit(1)
THE_FILE = os.path.join(BASE_DIR, f'{FILE}')
if MODE == "Watch and Run Other (WRO)":
    THE_FILE_TO_WATCH = os.path.join(BASE_DIR, f'{FILE_TO_WATCH}')
print(THE_FILE)
# Check if the file's path is valid exist
if not os.path.exists(THE_FILE):
    err = wp.textWrapBold(f"The file {THE_FILE} doesn't exist", Colors.RED)
    print(f"❌ {err}")
    sys.exit(1)

# Check if the file's path to watch is valid exist
if MODE == "Watch and Run Other (WRO)" and not os.path.exists(THE_FILE_TO_WATCH):
    err = wp.textWrapBold(f"The file {THE_FILE_TO_WATCH} doesn't exist", Colors.RED)
    print(f"❌ {err}")
    sys.exit(1)

if language in ["c++", "cpp", "c"]:
    COMMAND_LIST = [CMD]
    if FLAGS[0] != "":
        COMMAND_LIST.extend(iter(FLAGS))
    COMMAND_LIST.append(THE_FILE)
    COMMAND_LIST.append(OUTPUT_ATTRIBUTE)
    COMMAND_LIST.append(OUTPUT_FILE)

else:
    COMMAND_LIST = None


def __language_output():
    h = __Loader()
    h.run()
    # clear the terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    if language in ["ruby", "rb"]:
        __ruby_output()
    elif language in ["python", "py", "python3"]:
        __python_output()
    elif language in ["c++", "cpp"]:
        __cpp_output()
    elif language == "c":
        __c_output()

def __cpp_output():
    custom_fig = Figlet(font='colossal')
    print(custom_fig.renderText('C++'))
    print(f"{THE_FILE}")

def __c_output():
    custom_fig = Figlet(font='colossal')
    print(custom_fig.renderText('C'))
    print(f"{THE_FILE}")

def __python_output():
    custom_fig = Figlet(font='colossal')
    print(custom_fig.renderText('Python'))
    print(f"{THE_FILE}")


def __ruby_output():
    custom_fig = Figlet(font='colossal')
    print(custom_fig.renderText('Ruby'))
    print(f"{THE_FILE}")

__language_output()

class _Watcher:
    DIRECTORY_TO_WATCH = BASE_DIR

    def __init__(self, handler_type: WrsHandler):
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


def activate(SHELL_ARG:bool=False) -> None:
    """
    ACTIVATE
    ========
    Detect change in the working directory and execute the program chosen.
    Two modes of execution are available to you:
        * Based on observing a specific file for changes and executing another file. (Watch and Run Other) `WRO`
        * Observing a certain file and using the same file to conduct the test. (Watch and Run Self) `WRS`

    ```python
    from changedetector import detectchange
    detectchange.activate()
    ```
    """
    try:
        if MODE == "Watch and Run Self (WRS)":
            wh = WrsHandler(the_file=THE_FILE, command_list=COMMAND_LIST, language=language, base_dir=BASE_DIR, cmd=CMD)
            mode = wp.textWrapBold("(WRS)", Colors.GREEN)
        else:
            wh = WroHandler(the_file=THE_FILE, the_file_to_watch=THE_FILE_TO_WATCH, command_list=COMMAND_LIST, language=language, base_dir=BASE_DIR, cmd=CMD)
            mode = wp.textWrapBold("(WRO)", Colors.GREEN)
        w = _Watcher(wh)
        print(" ")
        print(f"Watching in {mode} mode...")
        print(" ")
        w.run()
    except KeyboardInterrupt:
        # pipe the error number to the shell
        print(f"\n{Colors.GREEN}{Colors.BOLD}Change Detector Stopped{Colors.END}")
        if SHELL_ARG:
            sys.exit(1)
        else:
            sys.exit(0)

if __name__ == '__main__':
    activate()
