import typing

import os
import shutil
import filecmp


class PathCacheManager(object):
    cache_dict: typing.Dict[(str, str)] = {}
    cache_root_folder_path = "./_pathcache"

    def __init__(self) -> None:
        self.cache_root_folder_path = os.path.abspath(
            self.cache_root_folder_path)
        pass

    def pathstr(self, path: str, foldercontext=False, refresh=False) -> str:
        # get the absolute path
        abs_path = os.path.abspath(path)

        result_path = abs_path

        if abs_path not in self.cache_dict:
            if abs_path[0] == '/':
                self.cache_dict[abs_path] = os.path.join(
                    self.cache_root_folder_path, abs_path[1:])
            elif abs_path.split(':')[1][0] == '/' or abs_path.split(':')[1][0] == '\\':
                self.cache_dict[abs_path] = os.path.join(
                    self.cache_root_folder_path, abs_path.split(':')[0], abs_path.split(':')[1][1:])
            refresh = True
        result_path = self.cache_dict[abs_path]

        if refresh:
            if os.path.isfile(abs_path):
                if foldercontext:
                    if os.path.exists(os.path.split(self.cache_dict[abs_path])[0]):
                        os.rmdir(os.path.split(self.cache_dict[abs_path])[0])
                    shutil.copytree(os.path.split(abs_path)[
                        0], os.path.split(self.cache_dict[abs_path])[0])
                else:
                    os.makedirs(os.path.split(self.cache_dict[abs_path])[0], exist_ok=True)

                if os.path.exists(abs_path):
                    if os.path.exists(self.cache_dict[abs_path]):
                        if not filecmp.cmp(abs_path, self.cache_dict[abs_path]):
                            shutil.copy(abs_path, self.cache_dict[abs_path])
                    else:
                        shutil.copy(abs_path, self.cache_dict[abs_path])
            else:
                if foldercontext:
                    if os.path.exists(self.cache_dict[abs_path]):
                        shutil.rmtree(self.cache_dict[abs_path])
                    shutil.copytree(
                        abs_path, self.cache_dict[abs_path])
                else:
                    os.makedirs(self.cache_dict[abs_path], exist_ok=True)

        return result_path

    def refresh(self, foldercontext=False):
        for key in self.cache_dict:
            self.cpypath1(key, self.cache_dict[key])

    def upload(self, foldercontext=False):
        for key in self.cache_dict:
            self.cpypath1(self.cache_dict[key], key)

    def clean(self):
        if os.path.exists(self.cache_root_folder_path):
            os.rmdir(self.cache_root_folder_path)

    def refresh1(self, key: str):
        self.cpypath1(key, self.cache_dict[key])

    def upload1(self, key: str):
        self.cpypath1(self.cache_dict[key], key)

    def cpypath1(self, path1: str, path2: str, foldercontext=False):
        if os.path.isfile(path1):
            shutil.copytree(os.path.split(path1)[0], os.path.split(path2)[0])

            if os.path.exists(path1):
                if os.path.exists(path2):
                    if not filecmp.cmp(path1, path2):
                        shutil.copy(path1, path2)
                else:
                    shutil.copy(path1, path2)
        else:
            if foldercontext:
                shutil.copytree(path1, path2, copy_function=shutil.copy)
            else:
                shutil.copytree(path1, path2)


manager = PathCacheManager()

pathcachestr = manager.pathstr
