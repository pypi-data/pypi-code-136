from watchdog.events import FileSystemEventHandler
import subprocess
import time
import os

from colors import Colors

class WroHandler(FileSystemEventHandler):

    def __init__(self, the_file: str, the_file_to_watch: str, language: str, command_list: list[str], base_dir: str, cmd: list) -> None:
        super().__init__()
        self.the_file = the_file
        self.the_file_to_watch = the_file_to_watch
        self.language = language
        self.command_list = command_list
        self.base_dir = base_dir
        self.cmd = cmd

    def on_any_event(self, event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print(f"{Colors.GREEN}{Colors.BOLD}+{Colors.END} {Colors.BOLD}Received created event - {event.src_path}.{Colors.END}")

        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            if event.src_path == self.the_file_to_watch:
                print("O U T P U T")
                print("═══════════════════════════════════════════════════════════")
                if self.language not in ["c++", "cpp", "c"]:
                    now = time.perf_counter()
                    cm = ''
                    cm = self.cmd[0] if os.name == 'nt' else self.cmd[1]
                    subprocess.call([cm, f'{self.the_file}'])
                    end = time.perf_counter()
                else:
                    now = time.perf_counter()
                    subprocess.call(self.command_list)
                    print(self.command_list)
                    end = time.perf_counter()
                    print(
                        f"{Colors.GREEN}{Colors.BOLD}COMPLILATON COMPLETED{Colors.END}")
                print("═══════════════════════════════════════════════════════════")
                print(f"{Colors.PURPLE}{Colors.BOLD}{end - now}s{Colors.END}")

                print(" ")
                print("---")
                print(
                    f"✅ {Colors.GREEN}{Colors.BOLD}Listening for changes...{Colors.END}")
            elif event.src_path == f'{self.base_dir}/detectchange.py':
                print(
                    f"❗{Colors.RED}{Colors.BOLD}RESTART THE PROGRAM FOR APPLY CHANGES{Colors.END}❗")
            else:
                print(
                    f"{Colors.GREEN}{Colors.BOLD}+{Colors.END} Received modified event - {event.src_path}.")
        elif event.event_type == 'deleted':
            # Taken any action here when a file is deleted.
            print(
                f"{Colors.RED}{Colors.BOLD}-{Colors.END} Received deleted event - {event.src_path}.")
