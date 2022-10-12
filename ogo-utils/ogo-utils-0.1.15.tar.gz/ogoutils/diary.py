import os
from datetime import datetime
from pathlib import Path

from ogoutils.encryption import encryption
from ogoutils.decryption import decryption

pwd = Path.cwd()

file_path = str(pwd / 'diary')
crp_file_path = str(pwd / 'diary.crp')

def write_diary():
    """ Write your thoughts into the diary file """
    password = input('Введите пароль: ')

    with open(file_path, 'a+') as f:
        note = input('OGO-DIARY: Привет! Напиши о чем думаешь:\n>>>')
        f.write(f'{datetime.now().isoformat()}\n{note}\n\n')

    with open(file_path, 'r') as f:
        print(f.read())

    encryption(file=file_path, password=password)


def read_diary():
    password = input('Введите пароль: ')
    decryption(file=crp_file_path, password=password)
    with open(file_path, 'r') as f:
        print(f.read())


if __name__ == "__main__":
    write_diary()
    read_diary()
