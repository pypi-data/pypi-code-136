# encoding: utf-8
"""
@project: sky-excel->parsed_cell
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis:
@created_time: 2022/9/29 16:34
"""
from openpyxl.worksheet.merge import MergedCellRange, CellRange


class ParsedCell():
    # 表头单元格属性
    is_merge_cell = False
    boundary = None
    coordinate = None  # 坐标如：A1:B2..
    value = None

    def __init__(self, cell, sheet=None):
        if isinstance(cell, MergedCellRange):  # python3.0版本,openpyxl 3.0.* 以上版本
            self.is_merge_cell = True
            self.value = cell.start_cell.value
            self.start_cell_coord = cell.start_cell.coordinate
            self.coordinate = str(cell)
            self.row = cell.start_cell.row
            self.column = cell.start_cell.column

        elif isinstance(cell, CellRange):  # python2.0版本,openpyxl2.6.*版本
            self.is_merge_cell = True
            self.coordinate = str(cell)
            self.start_cell = sheet[self.coordinate][0][0]
            self.value = self.start_cell.value
            self.start_cell_coord = self.start_cell.coordinate
            self.row = self.start_cell.row
            self.column = self.start_cell.column

        else:  # 是普通的单元格
            self.is_merge_cell = False
            self.value = cell.value
            self.start_cell_coord = str(cell.coordinate)
            self.coordinate = str(cell.coordinate)
            self.row = cell.row
            self.column = cell.column

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    # 单元格是否在选取内判断
    # def is_in_boundary(self, cell):
    #     if not isinstance(cell, Cell):
    #         return None, "cell必须是一个单元实例"
    #     # 表头单元格实例
    #     from shapely import geometry
    #     Points = (cell.column, cell.row)
    #     top, right, bottom, left = self.boundary
    #     boundary = top + right + bottom + left
    #     line = geometry.LineString(boundary)
    #     point = geometry.Point(Points)
    #     polygon = geometry.Polygon(line)
    #     return polygon.contains(point), None

    def __str__(self):
        return self.value
