import ntpath
import os

from diclass import DictClass


def get_path_info(path : str) -> DictClass:
    """it a path and returns following information as class object:
    'directory': the directory path where the file/folder resides
    'file_name': the name of the file/folder
    'base_name': the file name without extentation example.zip -> example
    Args:
        file_path (str): path to a file
    Returns:
        DictClass: file info in DictClass format
    """
        
    direcotry = os.path.dirname(path)
    name = ntpath.basename(path)
    base_name, extention = os.path.splitext(name)
    info_dict = {"directory": direcotry,
                 "base_name": base_name,
                 "name":name,
                 "extention":extention}
    return DictClass(info_dict)