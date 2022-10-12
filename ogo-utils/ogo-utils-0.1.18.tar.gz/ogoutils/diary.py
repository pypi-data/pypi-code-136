import os
from datetime import datetime
from pathlib import Path

from ogoutils.encryption import encryption
from ogoutils.decryption import decryption

pwd = Path.cwd()

file_path = str(pwd / 'diary')
crp_file_path = str(pwd / 'diary.crp')


def read_diary():
    password = input('Введите пароль: ')
    res = decryption(file=crp_file_path, password=password)

    if not res:
        return read_diary()

    with open(file_path, 'r') as f:
        print(f.read())

    encryption(file=file_path, password=password)


def write_diary():
    """ Write your thoughts into the diary file """
    password = input('Введите пароль: ')

    is_diary_exists = os.path.isfile(crp_file_path)

    if is_diary_exists:
        res = decryption(file=crp_file_path, password=password)
        if not res:
            return write_diary()

    with open(file_path, 'a+') as f:
        note = input('\nOGO-DIARY: Привет! Напиши о чем думаешь:\n>>> ')
        f.write(f'{datetime.now().isoformat()}\n{note}\n\n')

    with open(file_path, 'r') as f:
        print('\nПоследние записи:')
        print('\n', f.read())

    encryption(file=file_path, password=password)


if __name__ == "__main__":
    read_diary()
    # read_diary()
