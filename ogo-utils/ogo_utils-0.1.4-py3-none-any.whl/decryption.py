import traceback

import pyAesCrypt
import os


def decryption(file, password) -> None:
    """
    Функция для дешифрования файла
    :rtype: None
    """

    buffer_size = 512 * 1024

    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )

    # Имя зашифрованного файла
    print(f'[Файл {str(os.path.splitext(file)[0])} - дешифрован')

    # удалим исходный файл
    os.remove(file)


def walk_to_decrypt(directory: str, passwd: str) -> None:
    """
    Функция сканирования директорий
    :type passwd: str
    :param directory: директория которую сканируем
    :param passwd: пароль
    """
    for name in os.listdir(directory):
        path = os.path.join(directory, name)

        if os.path.isfile(path):

            try:
                decryption(path, passwd)
            except Exception as ex:
                traceback.print_exc(ex)

        else:
            walk_to_decrypt(path, passwd)


if __name__ == '__main__':
    password = input('Введите пароль для расшифровки: ')
    dir_to_decrypt = input('Введите дирректорию которую хотите расшифровать')
    walk_to_decrypt(dir_to_decrypt, password)
