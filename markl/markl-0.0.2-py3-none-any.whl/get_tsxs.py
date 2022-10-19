import os


def get_tsxs(dir):
    for dir_path, dirs, file_names in os.walk(dir):
        for file_name in file_names:
            if '.tsx' in file_name:
                yield dir_path + '/' + file_name
