import os
from datetime import datetime, timedelta
import json
import warnings
import gzip
from dateutil.parser import parser
import argparse
from src.log_utility import *

# import numpy as np

# 屏蔽所有 告警
warnings.filterwarnings("ignore")

# 默认图片存储地址，如不存在则新建该地址
OUTPUT_FILE = r"/tmp/chart/voltage_torque.jpg"

if not os.path.exists("/tmp/chart/"):
    os.mkdir("/tmp/chart/")


# 参数分别为机器人ID，时间戳，log根目录，输出图片保存路径
def generate_chart(input_args):
    """生成图表总入口

    Args:
        args: 通过命令行传入的参数
    """

    data_files = set(get_file_in_time_range(input_args))

    if not data_files:
        raise RuntimeError(f"没有时间点 {input_args.timestamp} 的相关数据")

    diagram_input_data = list(
        collection_data_for_plot(
            data_files, parse(input_args.timestamp), input_args.time_range
        )
    )

    if len(data_files) == 0:
        raise RuntimeError("所选时间范围内没有数据")

    # 绘图
    create_diagram(diagram_input_data, input_args)

    print(f"图表已生成，保存路径：{input_args.output_file}")


def collection_data_for_plot(data_files, date_selected, time_range):
    """根据要求的时间收集数据

    Args:
        data_files (set): 目标log的集合, 单次查询可能获取跨文件的数据
        date_selected (datetime): 要分析的日志的时间戳
        time_range (int): 分钟，截取的日志范围，距离当前时间前后多少分钟
    """
    res = (list(), list(), list())

    for file in data_files:
        if file.endswith("gz"):
            with gzip.open(file, mode="rt") as data_f:
                one_file_res = read_data_lines(data_f, date_selected, time_range)
                res = (
                    res[0] + one_file_res[0],
                    res[1] + one_file_res[1],
                    res[2] + one_file_res[2],
                )
        else:
            with open(file, mode="r") as data_f:
                one_file_res = read_data_lines(data_f, date_selected, time_range)
                res = (
                    res[0] + one_file_res[0],
                    res[1] + one_file_res[1],
                    res[2] + one_file_res[2],
                )

    return res


def init_input_args(sub_parser):
    sub_parser.add_argument("--prd_type", help="产品类型：sort or pick", required=True)
    sub_parser.add_argument(
        "--time_range",
        type=int,
        help="产品类型：分钟，截取的日志范围，距离时间点（--timestamp）前后多少分钟。默认1分钟",
        choices=range(1, 6),
        metavar="[1 ~ 6]",
        required=True,
    )
    sub_parser.add_argument("--log_root_dir", help="log 文件的根目录", required=True)
    sub_parser.add_argument(
        "--timestamp",
        help="时间点, 例如：2022-09-05 09:53:10。 默认为当前时间",
        default=datetime.now().strftime("%m-%d-%Y %H:%M:%S"),
    )
    sub_parser.add_argument("--robot_id", help="目标机器人的编号，例如：F48A57S", required=True)
    sub_parser.add_argument(
        "--output_file", help=f"输出文件的路径, 默认路径：{OUTPUT_FILE}", default=OUTPUT_FILE
    )
    sub_parser.add_argument("--plot_show", action="store_true", help="是否直接输出图像, 仅供调试使用")
    return sub_parser


def init_input_args_warp(sub_parser):
    res_parser = init_input_args(sub_parser)
    return res_parser.parse_args()


if __name__ == "__main__":
    res_json = {"code": 0, "message": "操作成功"}

    try:
        parser = argparse.ArgumentParser()
        args = init_input_args_warp(parser)
        generate_chart(args)

    except Exception as e:
        res_json["code"] = 1
        res_json["message"] = str(e)

    print(json.dumps(res_json, ensure_ascii=False, indent=4, sort_keys=True))

    # args = init_input_args()
    # generate_chart(args)
