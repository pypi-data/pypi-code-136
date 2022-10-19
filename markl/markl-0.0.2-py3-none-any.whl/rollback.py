from .config import Config
from .get_tsxs import get_tsxs


def rollback(dir='.'):
    for file_name in get_tsxs(dir):
        print(file_name)
        with open(file_name) as file:
            file_body = file.read()

        for tag in Config.TAGS:
            idx = 0
            while (idx := file_body.find('<' + tag + ' mark=', idx + 1)) != -1:
                file_body = file_body[:idx + 1 + len(tag)] + file_body[idx + 1 + len(tag) + 6 + 36 + 2 + 1:]

        with open(file_name, 'w') as file:
            file.write(file_body)
