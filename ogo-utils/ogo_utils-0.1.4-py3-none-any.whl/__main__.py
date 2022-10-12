# __main__.py

import sys
from getpass import getpass

from ogo_utils import decryption, encryption


list_of_actions = ['decryption', 'd', 'encryption', 'e']


def main():
    """Utils for ogoclients project"""

    # If an article ID is given, then show the article
    if len(sys.argv) > 1:
        action = sys.argv[1]
        if action in list_of_actions:
            if action in ['encryption', 'e']:
                directory = input('Input directory for encrypt: ')
                passwd = getpass('Input password: ')
                encryption.walk_to_encrypt(directory, passwd)
            if action in ['decryption', 'd']:
                directory = input('Input directory for decrypt: ')
                passwd = input('Input password:')
                decryption.walk_to_decrypt(directory, passwd)
        else:
            print('There is no such action')
    # If no ID is given, then show a list of all articles
    else:
        print(f'You can use these actions: {list_of_actions}')


if __name__ == "__main__":
    main()
