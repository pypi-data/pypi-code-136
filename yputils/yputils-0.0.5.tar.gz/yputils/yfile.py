import os
import pathlib
import hashlib


def get_file_list(file_dir: str, f_exts: list[str]) -> list[str]:
    f_exts = ['.' + t for t in f_exts]
    files = []

    for f in os.listdir(file_dir):
        ext = ''.join(pathlib.Path(f).suffixes)
        if ext in f_exts:
            files.append(f)

    return files


def get_file_path_list(file_dir: str, f_exts: list[str]) -> list[str]:
    return [os.path.join(file_dir, f) for f in get_file_list(file_dir, f_exts)]


def get_img_list(img_dir: str, img_exts: list[str] = ['jpg', 'JPG', 'png', 'PNG']) -> list[str]:
    img_exts = ['.'+ext for ext in img_exts]
    imgs = []

    for img in os.listdir(img_dir):
        ext = ''.join(pathlib.Path(img).suffixes)
        if ext in img_exts:
            imgs.append(img)
    return imgs


def get_img_path_list(img_dir: str, img_exts: list[str] = ['jpg', 'JPG', 'png', 'PNG']) -> list[str]:
    return [os.path.join(img_dir, img) for img in get_img_list(img_dir, img_exts=img_exts)]


def is_dir_exists(path) -> bool:
    return os.path.exists(path)


def is_dir(dirpath: str) -> bool:
    return os.path.isdir(dirpath)


def is_file(path) -> bool:
    return os.path.isfile(path)


def is_file_exists(path) -> bool:
    return os.path.exists(path)


def mkdir(dirpath: str) -> None:
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)


def sha256(filename: str) -> str:
    file_names = os.path.split(filename)
    file_path = ''
    if len(file_names) == 2 and file_names[0] == '':
        file_path = os.path.join(os.getcwd(), file_names[1])
    else:
        file_path = filename

    if os.path.exists(file_path):
        with open(file_path, 'rb') as f:
            sha256_obj = hashlib.sha256()
            sha256_obj.update(f.read())

            return sha256_obj.hexdigest()
    else:
        return 'Invalid File'
