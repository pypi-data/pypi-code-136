import click
import dumper
import haggis.logs
import logging
import os
import re
import sys
import traceback


def get_variable_name(stack_back=-2):
    """
    Called by dumps()

    Pulls the variable names from the function that called this function

    This function traces back through the call stack, so we have to subtract -1
    for every intermediate function, including this function.

    Subtract -1 for every intermediate step in the call stack.
    So we have: -1 for this function -1 for whoever called it = -2, which is the default.

    If there are more functions in the middle then subtract -1 for each of them. For example:
    -1 for this function -1 for dumps(), and -1 for whoever called dumps = -3.

    :param stack_back: How far back we need to go in the stack (see above description)
    :return: Returns the variable name(s)
    """
    stack = traceback.extract_stack()
    caller_name = stack[-2].name
    caller_len = len(caller_name)
    line = stack[stack_back].line
    # Example line: print('fu', 'bar/', argel1200.utilities.dumps(header), '/foobar')
    my_line = re.sub(r'(\s|\u180B|\u200B|\u200C|\u200D|\u2060|\uFEFF)+', '', line)  # Remove all whitespace
    caller_start = my_line.find(caller_name + '(')  # Find where the caller string is (e.g. where "dumps(" starts)
    caller_end = caller_start + caller_len  # And where it ends (the index of the '(' in "dumps("  )
    my_line_substr = my_line[caller_end:]  # Get a substr of everything past the caller (e.g. "dumps").

    # Now let's find all the variable names passed in
    vars_passed_in = []
    parens = 0
    str_start = None
    for idx, char in enumerate(my_line_substr):
        if char == '(':
            parens += 1
            str_start = idx + 1
        elif char == ',' or char == ')':
            vars_passed_in.append(my_line_substr[str_start:idx])
            str_start = idx + 1
            if char == ')':
                parens -= 1
                if parens == 0:
                    break
    return vars_passed_in


def dumps(*items):
    """
    Front end to dumper.dumps that does some helpful things like
    finding the variable names and adding them to the output string
    """
    dumper.max_depth = 10
    item_names = get_variable_name(-3)
    ret_str = ""
    for idx, item in enumerate(items):
        if idx > 0:
            ret_str += f"\n"
        item_name = item_names[idx]
        ret_str += f"'{item_name}' = "
        ret_str += dumper.dumps(item)  # string version of dump
    return ret_str


def import_class_from_string(path, parent_class_name=''):
    """
    Takes a string name of a class and returns an actual instance of that class.
    Useful when you need to (or it's just more elegant to) dynamically determine the class.

    :param path: The full class path.  (For example:  package.module.class)
    :param parent_class_name: Name of the parent class (For example: BaseClass)
    :return: The class, the parent class, or None
    """
    from importlib import import_module
    module_path, _, class_name = path.rpartition('.')
    mod = import_module(module_path)
    try:
        klass = getattr(mod, class_name)
    except:
        if parent_class_name:
            try:
                klass = getattr(mod, parent_class_name)
            except:
                return None
        else:
            return None
    return klass


def logging_init(return_logger=False):
    """
    Uses haggis to create some additional "debug" style logging levels, and then it
    configures the logging module.

    TRACE is for more detail beyond DEBUG
    MEMDUMP for even more detail than TRACE.

    Note: YOu need to use the lowercase version of the names:  logging.trace and logging.memdump
    """
    haggis.logs.add_logging_level('TRACE', logging.DEBUG - 1)
    haggis.logs.add_logging_level('MEMDUMP', logging.DEBUG - 9)
    logging.basicConfig(level=logging.MEMDUMP, format='%(asctime)s - %(levelname)s - %(message)s')

    log_levels = {
        'memdump': logging.MEMDUMP,
        'trace': logging.TRACE,
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL,
        }

    if return_logger:
        logger = logging.getLogger()
        return [logger, log_levels]
    else:
        return log_levels


def open_file(filename, mode='r', newline='', encoding='utf-8'):
    """
    Opens a file, with some error handling.
    :param encoding: Encoding used by the file
    :param filename: The name of the file to pass to open()
    :param mode: The read write mode to pass to open()
    :param newline: The newline to pass to open()
    :return: The file handle (or it exits if there is an error)
    """
    try:
        if mode == 'rb' or mode == 'wb':  # Binary mode
            file_handle = open(filename, mode)
        else:
            file_handle = open(filename, mode, newline=newline, encoding=encoding)
    except FileNotFoundError:
        print(f"ERROR: File {filename} not found.  Aborting")
        sys.exit(1)
    except OSError as err:
        print(f"ERROR: Cannot open file (OSerror.errno: {err.errno}; mode: {mode}): ", filename, file=sys.stderr)
        sys.exit(os.EX_OSFILE)
    except Exception as err:
        print(f"ERROR: Unexpected error opening {filename}: ", repr(err))
        sys.exit(1)
    return file_handle


def process_cli_using_click(my_cli):
    """
    Because we are *not* using click's standalone mode we need to do our own error handling.
    This function takes core of that.

    :param my_cli:  The function you defined via click to process the command line arguments
    """
    click_invoke_rc = None

    try:
        click_invoke_rc = my_cli(standalone_mode=False)
    except click.exceptions.NoSuchOption as err:
        print(f"{err}")
        print(f"Try running the program with -h or --help.")
        exit(3)
    except click.exceptions.UsageError as err:
        print(f"{err}")
        print(f"Try running the program with -h or --help.")
        exit(5)
    except:
        err = sys.exc_info()[0]
        print(f"An unexpected command line processing error occurred:")
        print(f"{err}")
        print(f"Try running the program with -h or --help.")
        exit(10)

    if click_invoke_rc == 0:  # Catch if -h, --help, --version, or something unknown was specified
        exit(1)

