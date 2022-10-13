import argparse
import pathlib
import random
import re
from math import inf

import pyperclip

# Use secure system random number generator
# (uses /dev/urandom on Unix and CryptGenRandom on Windows)
system_random = random.SystemRandom()
re_wordlist = re.compile("^(?P<wordlist>.*?)([.]txt)?([.](gz|bz2|xz|lzma))?$")


def get_wordlist(wordlist):
    """Return a wordlist from the wordlists directory."""
    wordlist = re_wordlist.match(wordlist).group("wordlist")
    wordlist_path = pathlib.Path(__file__).parent / "wordlists" / wordlist
    if wordlist_path.exists():
        return wordlist_path
    else:
        raise FileNotFoundError("Wordlist not found: {}".format(wordlist))


def read_wordlist(wordlist="eff_large_wordlist"):
    """Read a wordlist from the wordlists directory."""
    wordlist_path = get_wordlist(wordlist)
    with wordlist_path.open() as f:
        return [line.strip() for line in f]


def generate_passphrase(
    num_words: bool, separator: str, capitalize: bool, include_numbers: bool
):
    """
    generate a passphrase

    Args:
        num_words (bool): number of words to include in passphrase
        separator (str): a separator to use between words (ie: "-")
        capitalize (bool): capitalize first letter of each word
        include_numbers (bool): include numbers at random spot in passphrase

    Returns:
        str: passphrase
    """
    passphrase = []

    wordlist = list(set(read_wordlist()))
    # determine random location for number
    num_location = 1
    if include_numbers:
        num_location = system_random.randint(1, num_words)

    for i in range(num_words):
        word = system_random.choice(wordlist)
        # strip diceware generated numbers from list
        word = re.sub(r"^.*\t", "", word)

        if capitalize:
            word = word.capitalize()
        if include_numbers and len(passphrase) == num_location - 1:
            word += str(system_random.randint(0, 99))
        passphrase.append(word)

    full_passphrase = separator.join(passphrase)
    return full_passphrase


def generate_username(include_numbers: bool):
    """
    Generate a username. Uses logic of passphrase generation with some forced parameters included.

    Args:
        include_numbers (bool): flag to include numbers in username

    Returns:
        str: username
    """ """."""
    username = generate_passphrase(
        num_words=2,
        separator="",
        capitalize=True,
        include_numbers=include_numbers,
    )
    return username


def copy_to_clipboard(passphrase):
    """
    Copy to output clipboard automatically (used for cli)

    Args:
        passphrase (str): passphrase to copy to clipboard
    """
    pyperclip.copy(passphrase)
    print("Passphrase copied to clipboard.")


def ranged_type(min_value=0, max_value=inf):
    """
    Return a function that checks if a value is within a range.
    Used for argparse to require a minimum or maximum integer value.

    Args:
        min_value (int, optional): min value of number of words. Defaults to 0.
        max_value (_type_, optional): max value of number of words. Defaults to inf.
    """

    def check_range(value):
        value = int(value)
        if value < min_value or value > max_value:
            raise argparse.ArgumentTypeError(
                "Value must be between {} and {}".format(min_value, max_value)
            )
        return value

    return check_range


def main(
    command: str = None,
    include_numbers: bool = False,
    num_words: ranged_type() = None,
    separator: str = None,
    no_separator: bool = None,
    capitalize: bool = None,
    copy: bool = False,
):
    """
    main function

    Args:
        command (str, optional): command to generate either {'username','passphrase'}. Defaults to None.
        include_numbers (bool, optional): include numbers in output. Defaults to False.
        num_words (ranged_type, optional): number of words to use. Defaults to None.
        separator (str, optional): word separated by string. Defaults to None.
        no_separator (bool, optional): flag to prevent passphrase from having the default '-'
            (doesnt apply to usernames). Defaults to None.
        capitalize (bool, optional): capitalize first letter of each word in output. Defaults to None.
        copy (bool, optional): for cli use, copy output to clipboard?. Defaults to False.
    """
    result = ""
    if no_separator:
        separator = ""
    if command == "passphrase":
        result = generate_passphrase(num_words, separator, capitalize, include_numbers)
    if command == "username":
        result = generate_username(include_numbers)
    print(result)
    if copy:
        copy_to_clipboard(result)


def entry_point():
    """Entry point for console_scripts."""
    args = parse_args()
    main(**vars(args))


def parse_args():
    """"""
    parser = argparse.ArgumentParser(description="Generate a username or passphrase.")
    # add parent for shared commands between subparsers
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument(
        "-C", "--copy", action="store_true", help="Copy passphrase to clipboard"
    )
    parent_parser.add_argument(
        "-i",
        "--include-numbers",
        action="store_true",
        help="Include numbers in passphrase",
    )

    # add sub commands
    subparsers = parser.add_subparsers(
        help="command to run",
        required=True,
        dest="command",
        title="commands",
        description="valid commands",
    )

    parser_passphrase = subparsers.add_parser("passphrase", parents=[parent_parser])
    parser_username = subparsers.add_parser("username", parents=[parent_parser])

    # passphrase specific args
    parser_passphrase.add_argument(
        "-n",
        "--num-words",
        type=ranged_type(min_value=1),
        default=3,
        help="Number of words in passphrase (default: %(default)s)",
    )
    parser_passphrase.add_argument(
        "-c",
        "--capitalize",
        action="store_true",
        help="Capitalize the first letter of each word",
    )
    s_group = parser_passphrase.add_argument_group("Separator options")
    separator_group = s_group.add_mutually_exclusive_group()
    separator_group.add_argument(
        "-s",
        "--separator",
        default="-",
        help="Separator between words (default: %(default)s)",
    )
    separator_group.add_argument(
        "-xs",
        "--no-separator",
        action="store_true",
        help="Do not use a separator between words",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(**vars(args))
