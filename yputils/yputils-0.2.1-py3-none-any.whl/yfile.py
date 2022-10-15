from genericpath import isfile
import os
import pathlib
import hashlib

IMG_TYPE = ['JPG', 'JPEG', 'PNG', 'jpg', 'jpeg', 'png']


def list_file(f_path: str, f_ext: list[str]) -> list[str]:
    exts = ['.'+ext for ext in f_ext]
    files: list[str] = []
    for f in os.listdir(f_path):
        ext = ''.join(pathlib.Path(f).suffixes)
        if ext in exts:
            files.append(f)
    return files


def list_file_path(f_path: str, f_ext: list[str]) -> list[str]:
    return [os.path.join(f_path, f) for f in list_file(f_path, f_ext)]


def list_imgs(f_path: str, f_ext: list[str] = IMG_TYPE) -> list[str]:
    return list_file(f_path, f_ext)


def lsit_imgs_path(f_path: str, f_ext: list[str] = IMG_TYPE) -> list[str]:
    return list_file_path(f_path, f_ext)


def mkdir(dirpath: str) -> None:
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)


def hash(file_path: str, hash_type: str) -> str:
    if os.path.isfile(file_path):
        result = ''
        with open(file_path, 'rb') as f:
            match hash_type:
                case 'sha256':
                    sha256_obj = hashlib.sha256()
                    sha256_obj.update(f.read())
                    result = sha256_obj.hexdigest()
                case 'md5':
                    md5_obj = hashlib.md5()
                    md5_obj.update(f.read())
                    result = md5_obj.hexdigest()
                case _:
                    result = 'Invalid Hash Type'
        return result
    else:
        return 'Invalid File'
