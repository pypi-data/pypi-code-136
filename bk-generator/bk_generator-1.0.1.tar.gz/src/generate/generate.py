import pathlib
import random
import re

import pyperclip

if __package__ is None or __package__ == "":
    from argument_parsing import parse_args
else:
    from generate.argument_parsing import parse_args

# Use secure system random number generator
# (uses /dev/urandom on Unix and CryptGenRandom on Windows)
system_random = random.SystemRandom()
re_wordlist = re.compile("^(?P<wordlist>.*?)([.]txt)?([.](gz|bz2|xz|lzma))?$")


def get_wordlist(wordlist="eff_large_wordlist.txt"):
    """Return a wordlist from the wordlists directory."""
    wordlist = re_wordlist.match(wordlist).group("wordlist")
    wordlist_path = pathlib.Path(__file__).parent / "wordlists" / wordlist
    if wordlist_path.exists():
        return wordlist_path
    else:
        raise FileNotFoundError("Wordlist not found: {}".format(wordlist))


def read_wordlist(wordlist):
    """Read a wordlist from the wordlists directory."""
    wordlist_path = get_wordlist(wordlist)
    with wordlist_path.open() as f:
        return [line.strip() for line in f]


def generate_passphrase(wordlist, num_words, separator, capitalize, include_numbers):
    passphrase = []

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


def generate_username(wordlist, include_numbers):
    """Generate a username."""
    username = generate_passphrase(
        wordlist=wordlist,
        num_words=2,
        separator="",
        capitalize=True,
        include_numbers=include_numbers,
    )
    return username


def copy_to_clipboard(passphrase):
    """Copy to clipboard."""
    pyperclip.copy(passphrase)
    print("Passphrase copied to clipboard.")


def main(
    command,
    wordlist,
    copy,
    include_numbers,
    num_words=None,
    separator=None,
    no_separator=None,
    capitalize=None,
):
    """Main function."""
    wordlist = list(set(read_wordlist(wordlist)))
    result = ""
    if no_separator:
        separator = ""
    if command == "passphrase":
        result = generate_passphrase(
            wordlist, num_words, separator, capitalize, include_numbers
        )
    if command == "username":
        result = generate_username(wordlist, include_numbers)
    print(result)
    if copy:
        copy_to_clipboard(result)


def entry_point():
    """Entry point for console_scripts."""
    args = parse_args()
    main(**vars(args))


if __name__ == "__main__":
    args = parse_args()
    main(**vars(args))
