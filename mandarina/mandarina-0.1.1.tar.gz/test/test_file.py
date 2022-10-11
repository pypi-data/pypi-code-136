from mandarina.file import *
import unittest
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

class FileTest(unittest.TestCase):
    def test(self):
        pass

    # def test_create_dir_if_doesnt_exist(self):
    #     dir_path = "./test"
    #     create_dir_if_doesnt_exist(dir_path)
    #     self.assertTrue(os.path.exists(dir_path))
    #     delete_dir(dir_path)

    def test_convert_size_bytes_to_human_readable_fomat(self):
        bytes = [1024 * i for i in range(5)]
        for size in bytes:
            result = convert_size_bytes_to_human_readable_format(size)
