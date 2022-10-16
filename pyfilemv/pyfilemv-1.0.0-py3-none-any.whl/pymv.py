import time
import re
import os
import sys
import argparse
import shutil
from colorama import Fore, Style
import textwrap as tr

p = argparse.ArgumentParser()

p.add_argument("source", type=str, help="Source file.")

p.add_argument("destination", type=str, help="Destination of the source file after the move.")

p.add_argument("-r", "--root", type=str, required=False,
               help="Specify the absolute path to a directory. All files that are part of that directory "
                    "(and also subdirectories) are checked if they contain the file you want to move.")

p.add_argument("-e", "--extension", type=str, required=False, nargs="+",
               help="Specify file extensions which should be included in the search. "
                    "Should look like this: -e ext1 ext2 ext3.\nBy default, the program searches in "
                    "the following files: R, Rmd, RMD, txt, py, ipynb, md, pl, cpp, c, java")

p.add_argument("-a", "--absolute", action="store_true", required=False,
               help="If you set this flag, the program will search for the absolute filepath.")

args = p.parse_args()

# check if file exists
if not os.path.exists(args.source):
    sys.exit("The source file does not exist. Exiting.")

# get the width of the terminal, so we can wrap text accordingly
TERMINAL_WIDTH = shutil.get_terminal_size()[0]

logo = '''
 __        __       _                                       _           
 \ \      / / ___  | |   ___    ___    _ __ ___     ___    | |_    ___  
  \ \ /\ / / / _ \ | |  / __|  / _ \  | '_ ` _ \   / _ \   | __|  / _ \ 
   \ V  V / |  __/ | | | (__  | (_) | | | | | | | |  __/   | |_  | (_) |
    \_/\_/   \___| |_|_ \___|  \___/  |_|_|_|_|_|  \___|    \__|  \___/ 
                        _ __    _   _   _ __ ___    _   _
                       | '_ \  | | | | | '_ ` _ \  \ \ / /                
                       | |_) | | |_| | | | | | | |  \ V /                 
                       | .__/   \__, | |_| |_| |_|   \_/                  
                       |_|      |___/                                     
'''


def fileList(source, extensions):
    matches = []
    for root, dirnames, filenames in os.walk(source):
        for filename in filenames:
            if filename.endswith(tuple(extensions)):
                matches.append(os.path.join(root, filename))
    return matches


def styled_print(string, type):
    formated_string = f"{type}{string}{Style.RESET_ALL}"
    return formated_string


def add_padding(string, width):
    n_space = width - len(string) + 1
    mod_string = f"# {string}" + " " * n_space + "#"
    return mod_string


def flatten(lst):
    """Flatten a list using generators comprehensions.
        Returns a flattened version of list lst.
    """
    for sublist in lst:
        if isinstance(sublist, list):
            for item in sublist:
                yield item
        else:
            yield sublist


def main():
    # By default, the script will look for matches in files with the following extension.
    FILE_EXTENSIONS_CHECK = ["R", "Rmd", "RMD", "txt", "py", "ipynb",
                             "md", "pl", "cpp", "c", "java", "qmd"]

    # You can add extensions, by adding extensions to the file ~/.pyfilemv
    # Add one extension per line.

    # Check if user set the extension flat:
    if args.extension is not None:
        FILE_EXTENSIONS_CHECK.extend(args.extension)

    # Check if the user added custion file extensions and if yes, add them to the list.
    HOME = os.path.expanduser('~')
    if os.path.exists(f"{HOME}/.pyfilemv"):
        with open(f"{HOME}/.pyfilemv", "r") as f:
            contents = f.readlines()
            contents = [i.strip() for i in contents if i.strip() != ""]  # remove \n and also empty extensions
        FILE_EXTENSIONS_CHECK.extend(contents)

    # Depending on the user setting, either search for absolut path or for only the file name.
    if args.absolute:
        origin = os.path.abspath(args.source)
        destination = os.path.abspath(args.destination)
    else:
        origin = os.path.sep + args.source
        destination = os.path.sep + args.destination

    # determine the files were we look for matches
    if args.root is not None:
        root_directory = args.root
    elif "PYFILEMVROOT" in os.environ:
        print("Getting the Root directory from the enviromental variables")
        root_directory = os.environ["PYFILEMVROOT"]
    else:
        sys.exit(
            "You have to specify a root directory. All files that are part of this directory are searched. "
            "You can specify the root directory either by setting the --root flag or the enviromental variable PYFILEMVROOT.")
    files_to_search = fileList(root_directory, FILE_EXTENSIONS_CHECK)

    # this can be improved, but I think that it should still work instantly..
    # we first iterate through all files and look for a match. If we find one, we record the line of the match as well as one above and below and save it
    # then we show it to the user how stuff would change. If the user wishes to continue. we loop again through the files and do the replacement.
    n_matches = 0
    print(logo)
    time.sleep(0.5)
    for file in files_to_search:
        std_out_lines = []
        try:
            with open(file, "r") as f:
                lines = f.readlines()
                lines = [i.strip() for i in lines if i.strip() != ""]
        except UnicodeDecodeError:
            print(f"Tried to open file {file} but failed. Skipping it.")
        for index, l in enumerate(lines):
            # check if we find a match.
            if origin in l.strip():
                n_matches += 1
                # get the old lines without changing the color
                old_lines = tr.wrap(lines[index], width=TERMINAL_WIDTH - 5)
                # see how the new line would look like:
                replacement = lines[index].replace(origin, destination)
                new_lines = tr.wrap(replacement, width=TERMINAL_WIDTH - 5)

                # now we prepare the output
                file_found = f"Found a match in file {file}:"

                # we want to wrap the output in '#', so we have to determine the longest sentence
                longest_string = len(max(list(set(flatten([file_found, old_lines, new_lines]))), key=len))

                old_lines = [add_padding(i, longest_string) for i in old_lines]
                new_lines = [add_padding(i, longest_string) for i in new_lines]

                old_lines = "\n".join(old_lines)
                new_lines = "\n".join(new_lines)

                # create the output sting
                std_out_lines.append(
                    "\n".join(
                        ["#" * (longest_string + 4),
                         add_padding(f"Found a match in file {file}:", longest_string),
                         add_padding("OLD: ", longest_string),
                         old_lines,
                         add_padding("", longest_string),
                         add_padding("NEW: ", longest_string),
                         new_lines,
                         "#" * (longest_string + 4),
                         ""]))

        for out in std_out_lines:
            # now color the relevant parts:
            out = re.sub(origin, Fore.LIGHTRED_EX + origin + Style.RESET_ALL, out)
            out = re.sub(destination, Fore.LIGHTGREEN_EX + destination + Style.RESET_ALL, out)
            out = re.sub(file, Fore.LIGHTBLUE_EX + file + Style.RESET_ALL, out)
            print(out)

            user_input = str(input("Do you wish to make the indicated substitution? (y/n/continue): "))
            if user_input == "y":
                with open(file, "r") as read_file:
                    content = read_file.read()
                new_content = content.replace(origin, destination)
                with open(file, "w")as write_file:
                    write_file.write(new_content)
                print("Replacement successful.")
            elif user_input == "n":
                sys.exit("Existing Program. Choose 'continue' if you want to see the other edits.")
            elif user_input == "continue":
                print(styled_print("Continuing", Fore.RED))
                continue
            else:
                sys.exit("You have to enter 'y', 'n', 'continue'. Quitting program.")

    if n_matches == 0:
        print(f"Didnt find a match in any file. Root directory was: {root_directory}")
    else:
        print(f"All done :)\nIn total, {n_matches} substitutions were done.")

    shutil.move(args.source, args.destination)


if __name__ == '__main__':
    main()
