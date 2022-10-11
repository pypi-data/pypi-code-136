# encoding: utf-8
"""
@project: sky-excel->main
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis:
@created_time: 2022/9/28 18:18
"""

from .main.excel_exporter import ExcelExport

global_export_data = [
    {"index1": "row1", "index_7": "row1", "index_6": "row1", "index_5": "row1"},
    {"index1": "row2", "index_7": "row2", "index_6": "row2", "index_5": "row2"},
    {"index1": "row3", "index_7": "row3", "index_6": "row3", "index_5": "row3"},
    {"index1": "row4", "index_7": "row4", "index_6": "row4", "index_5": "row4"},
    {"index1": "row5", "index_7": "row5", "index_6": "row5", "index_10": "row5"},
    {"index_6": "row4", "index1": "row4", "index_7": "row4", "index_5": "row4"},
]

# 导出数据测试
export_instance = ExcelExport(input_dict=global_export_data, excel_templet_path="./templet/templet.xlsx", save_path="D:\\PySet/sky-excel/templet/")
data, err = export_instance.export()
