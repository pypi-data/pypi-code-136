# encoding: utf-8
"""
@project: sky-excel->main
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis:
@created_time: 2022/9/28 18:18
"""

from sky_excel.main.v2.excel_exporter import ExcelExport

global_export_data = [
    {"col_1": "row1", "col_2": "row1", "col_3": "row1", "col_4": "row1"},
    {"col_1": "row2", "col_2": "row1", "col_3": "row1", "col_4": "row1"},
    {"col_1": "row3", "col_2": "row1", "col_3": "row1", "col_4": "row1"},
    {"col_1": "row4", "col_2": "row1", "col_3": "row1", "col_4": "row1"},
    {"col_1": "row5", "col_2": "row1", "col_3": "row1", "col_4": "row1"},
    {"col_1": "row6", "col_2": "row1", "col_3": "row1", "col_4": "row1"},
    {"col_1": "row7", "col_2": "row1", "col_3": "row1", "col_4": "row1"},
]
#
# 导出数据测试
export_instance = ExcelExport(excel_templet_path="./templet/templet.xls")
data, err = export_instance.additional_write(input_dict=global_export_data)

data, err = export_instance.save(workbook=export_instance.additional_write_wb, save_path="D:\\PySet/sky-excel/sky_excel/export/")

