# -*- coding: utf-8 -*-
import warnings
from typing import Optional, Union


class ExcelBaseObject(object):
    def __init__(self, name: str, path: Optional[str] = ''):
        self._name = name
        self._path = path

        self._xl = None
        self._sheet = None

        self.open_xl()

    def open_xl(self):
        """ 初始化表格 """
        raise NotImplementedError

    def set_sheet(self, sheet: Union[int, str, None] = 0) -> None:
        """ 设置表格读取的工作簿 """
        raise NotImplementedError

    @property
    def sheet(self):
        return self._sheet

    @property
    def sheet_name(self) -> str:
        """
        当前读取中的工作表名称

        Returns:
            工作表名称
        """
        raise NotImplementedError

    @property
    def name(self) -> str:
        return self._name

    @property
    def path(self) -> str:
        return self._path

    @property
    def max_row(self) -> int:
        """
        返回表格最大列数

        Returns:
            最大列数
        """
        raise NotImplementedError

    @property
    def max_column(self) -> int:
        """
        返回表格最大列数

        Returns:
            最大列数
        """
        raise NotImplementedError

    def get_rows(self):
        """ 获取所有列的单元格 """
        raise NotImplementedError

    def get_row(self, rowx: int, start_colx: Optional[int] = 0, end_colx: int = None):
        """
        获取对应行的所有单元格

        Args:
            rowx: 行数
            start_colx: 左切片列数
            end_colx: 右切片列数

        Returns:
            返回这一行所有单元格
        """
        raise NotImplementedError

    def get_row_len(self, rowx: int, start_colx: Optional[int] = 0, end_colx: int = None):
        """
        获取对应行有效单元格的数量

        Args:
            rowx: 行数
            start_colx: 左切片列数
            end_colx: 右切片列数

        Returns:
            有效单元格数量
        """
        raise NotImplementedError

    def get_row_value(self, rowx: int, start_colx: Optional[int] = 0, end_colx: int = None):
        """
        获取表格内对应行中的所有单元格的数据

        Args:
            rowx: 行数
            start_colx: 左切片列数
            end_colx: 右切片列数

        Returns:
            返回这一行所有数据组成的列表
        """
        raise NotImplementedError

    def get_col(self, colx: int, start_rowx: Optional[int] = 0, end_rowx: Optional[int] = None):
        """
        获取表格内对应列中的所有单元格

        Args:
            colx: 行数
            start_rowx: 左切片行数
            end_rowx: 右切片行数

        Returns:
            返回这一列所有单元格
        """
        raise NotImplementedError

    def get_col_value(self, colx: int, start_rowx: Optional[int] = 0, end_rowx: Optional[int] = None):
        """
        获取表格内对应列中的所有单元格的数据

        Args:
            colx: 行数
            start_rowx: 左切片行数
            end_rowx: 右切片行数

        Returns:
            返回这一列所有数据组成的列表
        """
        raise NotImplementedError

    def get_cell(self, rowx: int, colx: int):
        """
        获取单元格

        Args:
            rowx: 列数
            colx: 行数

        Returns:
            行列对应单元格
        """
        raise NotImplementedError

    def get_cell_value(self, rowx: int, colx: int):
        """
        获取单元格内数据

        Args:
            rowx: 列数
            colx: 行数

        Returns:
            行列对应单元格中的数据
        """
        raise NotImplementedError
