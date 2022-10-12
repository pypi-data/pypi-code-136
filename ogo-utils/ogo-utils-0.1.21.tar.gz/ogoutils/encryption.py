import traceback

import pyAesCrypt
import os


def encryption(file, password) -> None:
    """
    Функция для шифрования файла
    :rtype: None
    """

    buffer_size = 512 * 1024

    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        password,
        buffer_size
    )

    # Имя зашифрованного файла
    print(f'[Файл {str(os.path.splitext(file)[0])} - зашифрован')

    # удалим исходный файл
    os.remove(file)


def walk_to_encrypt(directory: str, passwd: str) -> None:
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
                encryption(path, passwd)
            except Exception as ex:
                traceback.print_exception(ex)

        else:
            walk_to_encrypt(path, passwd)


if __name__ == '__main__':
    password = input('Введите пароль для шифрования: ')
    dir_to_encrypt = input('Введите дирректорию которую хотите зашифровать')
    walk_to_encrypt(dir_to_encrypt, password)
