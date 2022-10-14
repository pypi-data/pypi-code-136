import os

from notesecret import read_secret
from tqdm import tqdm

from lanzou.api import LanZouCloud
from lanzou.api.models import FolderList
from lanzou.api.types import *


class ProgressWrap:
    def __init__(self, callback: tqdm = None):
        self.callback: tqdm = callback
        self.last_size = 0

    def init(self, file_name, total_size):
        if self.callback is None:
            self.callback = tqdm(unit='B', unit_scale=True, unit_divisor=1024, desc=file_name, total=total_size)

    def update(self, now_size):
        self.callback.update(now_size - self.last_size)
        self.last_size = now_size


class LanZouDrive(LanZouCloud):
    def __init__(self):
        super(LanZouDrive, self).__init__()

    def _upload_small_file(self, *args, callback=None, **kwargs) -> int:
        wrap = ProgressWrap()

        def clb(file_name, total_size, now_size):
            wrap.init(file_name, total_size)
            wrap.update(now_size)

        return super(LanZouDrive, self)._upload_small_file(*args, callback=clb, **kwargs)

    def down_file_by_url(self, *args, callback=None, **kwargs) -> int:
        """通过分享链接下载文件(需提取码)
        :param callback 用于显示下载进度 callback(file_name, total_size, now_size)
        :param overwrite 文件已存在时是否强制覆盖
        :param downloaded_handler 下载完成后进一步处理文件的回调函数 downloaded_handle(file_path)
        """

        wrap = ProgressWrap()

        def clb(file_name, total_size, now_size):
            wrap.init(file_name, total_size)
            wrap.update(now_size)

        return super(LanZouDrive, self).down_file_by_url(*args, callback=clb, **kwargs)

    def login_by_cookie(self, cookie: dict = None, ylogin=None, phpdisk_info=None) -> int:
        """通过cookie登录"""
        cookie = cookie or {
            'ylogin': read_secret("drive", "lanzou", 'ylogin', value=ylogin),
            'phpdisk_info': read_secret("drive", "lanzou", 'phpdisk_info', value=phpdisk_info)
        }
        return super(LanZouDrive, self).login_by_cookie(cookie)

    def sync_files(self, path_root, folder_id, only_directory=False, overwrite=False, filter_fun=None,
                   remove_local=False):
        """
        将本地的文件同步到云端，单向同步
        :param path_root: 本地路径
        :param folder_id: 云端路径
        :param only_directory: 是否只同步文件夹
        :param overwrite: 是否需要覆盖重写
        :param filter_fun: 针对部分文件需要过滤
        :param remove_local: 同步完成后是否删除本地文件
        :return: 文件到folder_id的映射关系
        """
        yun_dir_list = self.get_dir_list(folder_id)
        yun_file_list = self.get_file_list(folder_id)
        yun_dir_dict = dict([(yun.name, yun.id) for yun in yun_dir_list])
        yun_file_dict = dict([(yun.name, yun.id) for yun in yun_file_list])

        file_dict = {}
        for file in (os.listdir(path_root)):
            local_path = os.path.join(path_root, file)
            # 根据传入的函数进行过滤，某些文件可以不同步
            if filter_fun is not None and (filter_fun(local_path) or filter_fun(file)):
                continue

            # 文件夹同步，支持递归同步
            if os.path.isdir(local_path):
                if file in yun_dir_dict.keys():
                    yun_id = yun_dir_dict[file]
                else:
                    yun_id = self.mkdir(parent_id=folder_id, folder_name=file, desc=file)
                file_dict[local_path] = yun_id
                file_dict.update(self.sync_files(local_path, yun_id, only_directory=only_directory,
                                                 overwrite=overwrite, filter_fun=filter_fun, remove_local=remove_local))
            else:
                # 只同步文件夹
                if only_directory:
                    continue
                # 文件在云端已存在，如果覆盖重写，删除云端文件，重新上传
                if file in yun_file_dict.keys():
                    if overwrite:
                        self.delete(yun_file_dict[file], is_file=True)
                        yun_id = self.upload_file(file_path=local_path, folder_id=folder_id)
                    else:
                        yun_id = yun_file_dict[file]
                else:
                    yun_id = self.upload_file(file_path=local_path, folder_id=folder_id)

                file_dict[local_path] = yun_id
                # if yun_id > 100 and remove_local:
                #     os.remove(local_path)
                os.remove(local_path)

        return file_dict

    def sync_directory(self, path_root, folder_id, *args, **kwargs):
        return self.sync_files(path_root, folder_id, *args, **kwargs)

    def get_full_path(self, folder_id=-1) -> FolderList:
        """获取文件夹完整路径"""
        path_list = FolderList()
        path_list.append(FolderId('LanZouCloud', -1))
        post_data = {'task': 47, 'folder_id': folder_id}
        resp = self._post(self._doupload_url, post_data)
        if not resp:
            return path_list
        for folder in resp.json()['info']:
            if folder['folderid'] and folder['name']:  # 有时会返回无效数据, 这两个字段中某个为 None
                path_list.append(FolderId(id=int(folder['folderid']), name=folder['name']))
        return path_list


def download(url, dir_pwd='./download', pwd=''):
    downer = LanZouDrive()
    downer.ignore_limits()
    downer.down_file_by_url(url, save_path=dir_pwd, pwd=pwd)
