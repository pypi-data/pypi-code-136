"""This is the description.

  example: src/pack_log.py --prd_type=sort --time_range=100  --timestamp="2022-09-13 17:55:00" --log_root_dir=/tmp/66log
"""
from src.log_utility import *
import argparse
import tarfile
import os
from datetime import datetime
from alive_progress import alive_bar

OUTPUT_DIR = "/tmp/log_trans/"
OUTPUT_FILE = f"{OUTPUT_DIR}log.tar.gz"


def init_input_args(sub_parser):
    """解析shell传入的参数, 返回结果
    Returns:
        parser Namespace: 返回解析后的结果
    """
    # sub_parser.add_argument("--prd_type", help="产品类型：sort or pick", required=False)
    sub_parser.add_argument(
        "--time_range",
        type=int,
        help="希望抓取日志的有效时间范围：默认前后30分钟。截取的日志范围，距离时间点（--timestamp）前后多少分钟。",
        default=30,
        choices=range(1, 60),
        metavar="[1 ~ 60]",
    )
    sub_parser.add_argument("--log_root_dir", help="log 文件的根目录", required=True)
    sub_parser.add_argument(
        "--timestamp",
        help="时间点, 例如：2022-09-05 09:53:10。 默认为当前时间",
        default=datetime.now().strftime("%m-%d-%Y %H:%M:%S"),
    )
    sub_parser.add_argument(
        "--output_file", help=f"输出文件的路径, 默认路径：{OUTPUT_FILE}", default=OUTPUT_FILE
    )

    # DON'T want to allow --feature and --no-feature at the same time
    feature_recursive_parser = sub_parser.add_mutually_exclusive_group(required=False)
    feature_recursive_parser.add_argument('--recursive', dest='recursive', action='store_true', help='递归处理log文件目录的子目录, 默认激活该选项')
    feature_recursive_parser.add_argument('--no-recursive', dest='recursive', action='store_false', help='不处理log文件目录的子目录')
    sub_parser.set_defaults(recursive=True)

    feature_compress_parser = sub_parser.add_mutually_exclusive_group(required=False)
    feature_compress_parser.add_argument('--compress', dest='compress', action='store_true', help="压缩输出文件, 默认激活该选项")
    feature_compress_parser.add_argument('--no-compress', dest='compress', action='store_false', help="不压缩输出文件")
    sub_parser.set_defaults(compress=True)

    return sub_parser


def init_input_args_warp(sub_parser):
    res_parser = init_input_args(sub_parser)
    return res_parser.parse_args()


def pack_log(input_args):
    """找到指定的log，并打包
    Args:
        input_args: shell 传入的参数
    """

    try:
        if not os.path.exists(OUTPUT_DIR):
            os.mkdir(OUTPUT_DIR)

        if os.path.exists(input_args.output_file):
            os.remove(input_args.output_file)
    except (FileNotFoundError, IsADirectoryError):
        pass

    print(f"input_args.recursive: {input_args.recursive}")
    log_files = set(
        get_file_in_time_range(
            input_args, download_log=True, recursive=input_args.recursive
        )
    )
    print(f"log_files: {log_files}")

    if len(log_files) == 0:
        print("no log files in range")
        return

    print(f"totlal {len(log_files)} files, compress start ...")

    # if input_args.compress, tar with gzip
    if input_args.compress:
        with alive_bar(len(log_files),  title='pack with compress') as bar:
            with tarfile.open(input_args.output_file, "w:gz") as tar:
                for log_file in log_files:
                    try:
                        tar.add(log_file)
                        bar()
                    except FileNotFoundError:
                        print(f"file {log_file} is not exist")

    # else, tar without gzip
    else:
        with alive_bar(len(log_files),  title='pack without compress') as bar:
            with tarfile.open(input_args.output_file, "w") as tar:
                for log_file in log_files:
                    try:
                        tar.add(log_file)
                        bar()
                    except FileNotFoundError:
                        print(f"file {log_file} is not exist")

    # terminal process bar for compress with alive-progress
    print(f"pack complete, total {len(log_files)} files, output file: {input_args.output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    input_args = init_input_args_warp(parser)
    pack_log(input_args)
