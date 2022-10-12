# __main__.py

import sys
from getpass import getpass
from ogoutils import encryption, decryption
from ogoutils import diary

list_of_actions = ['decryption', '-d', 'encryption', '-e', 'write_diary', 'wd', 'read_diary', 'rd']


def main():
    """Utils for ogoclients project"""

    # If an article ID is given, then show the article
    if len(sys.argv) > 1:
        action = sys.argv[1]
        if action in list_of_actions:
            if action in ['encryption', '-e']:
                directory = input('Input directory for encrypt: ')
                passwd = getpass('Input password: ')
                encryption.walk_to_encrypt(directory, passwd)
            if action in ['decryption', '-d']:
                directory = input('Input directory for decrypt: ')
                passwd = input('Input password:')
                decryption.walk_to_decrypt(directory, passwd)
            if action in ['write_diary', 'wd']:
                diary.write_diary()
            if action in ['read_diary', 'rd']:
                diary.read_diary()
        else:
            print('There is no such action')
    # If no ID is given, then show a list of all articles
    else:
        print(f'Команды доступные к использованию: \n')
        print()
        print('decryption,  -d', ' -- Расшифровать файл')
        print()
        print('encryption, -e', ' -- Зашифровать файл')
        print()
        print('write_diary, wd', ' -- Сделать запись в дневник')
        print()
        print('read_diary, rd', ' -- Читать дневник')



if __name__ == "__main__":
    main()
