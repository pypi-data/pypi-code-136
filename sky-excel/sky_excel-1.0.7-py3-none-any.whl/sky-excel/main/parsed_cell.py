# encoding: utf-8
"""
@project: sky-excel->parsed_cell
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis:
@created_time: 2022/9/29 16:34
"""
from openpyxl.cell import Cell
from openpyxl.worksheet.merge import MergedCellRange
from shapely import geometry


# 表头单元格实例
class ParsedCell():
    # 表头单元格属性
    is_merge_cell = False
    boundary = None
    coordinate = None  # 坐标如：A1:B2..
    value = None

    def __init__(self, cell):
        if isinstance(cell, MergedCellRange):
            self.is_merge_cell = True
            self.value = cell.start_cell.value
            self.coordinate = str(cell)
            self.boundary = (cell.top, cell.right, cell.bottom, cell.left)
            self.row = cell.start_cell.row
            self.column = cell.start_cell.column
        else:
            self.is_merge_cell = False
            self.value = cell.value
            self.coordinate = str(cell.coordinate)
            self.boundary = ((cell.column, cell.row), (cell.column, cell.row), (cell.column, cell.row), (cell.column, cell.row))
            self.row = cell.row
            self.column = cell.column

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def is_in_boundary(self, cell):
        if not isinstance(cell, Cell):
            return None, "cell必须是一个单元实例"
        Points = (cell.column, cell.row)
        top, right, bottom, left = self.boundary
        boundary = top + right + bottom + left
        line = geometry.LineString(boundary)
        point = geometry.Point(Points)
        polygon = geometry.Polygon(line)
        return polygon.contains(point), None

    def __str__(self):
        return self.value
