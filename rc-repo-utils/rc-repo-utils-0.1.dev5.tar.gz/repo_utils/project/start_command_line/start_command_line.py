""" Command line utility for repository """
import fire
import repo_utils


def start_command_line():
    """Command-line interface for the repository.
    Specify the definition to execute and then any arguments.
    e.g. "define <name>".
    The Fire library converts the specified function or object into a command-line utility.
    """

    fire.Fire(repo_utils)
