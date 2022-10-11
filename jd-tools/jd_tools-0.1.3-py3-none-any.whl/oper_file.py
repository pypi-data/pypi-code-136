# -*- coding:utf-8 -*-
# 文件:  operate_file.py
# 日期:  2021/11/17 14:49
import os
import zipfile
import shutil
from .logs import logger

__version__ = '1.0.5'
__all__ = ['move_file', 'copy_file', 'zip_dir', 'make_dirs']


def move_file(src: str, dst: str):
    if not os.path.isfile(src):
        logger.error("move_file src file not exist [%s]!" % src)
        return False
    else:
        filepath, filename = os.path.split(dst)    # 分离文件名和路径
        if not os.path.exists(filepath):
            os.makedirs(filepath)   # 创建路径
        shutil.move(src, dst)   # 移动文件
        # logger.debug("move %s -> %s" % (src, dst))
        return True


def copy_file(src: str, dst: str):
    if not os.path.isfile(src):
        logger.error("copy_file src file not exist [%s]!" % src)
        return False
    else:
        filepath, filename = os.path.split(dst)    # 分离文件名和路径
        if not os.path.exists(filepath):
            os.makedirs(filepath)   # 创建路径
        shutil.copyfile(src, dst)   # 复制文件
        # logger.debug("copy %s -> %s" % (src, dst))
        return True


def zip_dir(dir_path, out_full_name):
    """
    压缩指定文件夹
    :param dir_path: 目标文件夹路径
    :param out_full_name: 压缩文件保存路径+xxx.zip
    :return: 无
    """
    z = zipfile.ZipFile(out_full_name, "w", zipfile.ZIP_DEFLATED)
    for path, dir_names, filenames in os.walk(dir_path):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        f_path = path.replace(dir_path, '')
        for filename in filenames:
            z.write(os.path.join(path, filename), os.path.join(f_path, filename))
    z.close()


def make_dirs(full_path, last_file=False):
    if last_file:
        pathname = full_path.rsplit('/')[0]
    else:
        pathname = full_path
    if not os.path.exists(pathname):
        os.makedirs(pathname)
