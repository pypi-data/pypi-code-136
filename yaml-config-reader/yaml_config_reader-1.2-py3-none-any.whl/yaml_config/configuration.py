import os
import yaml


def cut_protocol(url: str) -> str:
    """
    Функция, обрезающая из домена протокол.

    :param url: Полный URL;

    :return: URL без протокола.
    """
    url_parts = url.split('://', 1)

    if len(url_parts) > 1:
        return url_parts[1]

    return url


def open_config(*args: str) -> dict:
    """
    Функция для получения объекта конфигурации.

    :param args: Пути до файлов конфигурации;

    :return: Объект конфигурации из первого найденного файла.
        Проверка осуществляется в порядке следования.
    """

    def format_constructor(loader: yaml.BaseLoader, node: yaml.Node):
        template, *values = loader.construct_sequence(node)

        return template.format(*values)

    yaml.add_constructor('!format', format_constructor)

    for path in args:
        if os.path.exists(path):
            with open(path, 'r') as file:
                return yaml.load(file, Loader=yaml.FullLoader)

    raise FileNotFoundError('Configuration file not found')
