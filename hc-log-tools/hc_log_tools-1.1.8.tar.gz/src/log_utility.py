from datetime import datetime, timedelta
from sqlite3 import Timestamp
from dateutil.parser import parse
import gzip
import json
import os
from os import SEEK_END
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import re

def is_file_in_time_range(file_path, delta_mins=10, date_selected=datetime.now()):
    """检测文件是否符合期望的时间要求

    Args:
        file_path (_type_): 文件路径
        delta_mins (int, optional): 期望的时间窗口，前后N分钟
        date_selected (_type_, optional): 日志查询窗口的中心时间戳

    Returns:
        _type_: _description_
    """
    try:
        mt = os.path.getmtime(file_path)
        ct = os.path.getctime(file_path)

        time_range_start_timestamp = (date_selected - timedelta(minutes=delta_mins)).timestamp()
        time_range_end_timestamp = (date_selected + timedelta(minutes=delta_mins)).timestamp()

        # 最后编辑时间小于范围开始时间
        if mt < time_range_start_timestamp:
            print(f"{file_path} not in time range")
            return False

        if file_path.endswith("gz"):
            print(f"{file_path} is checking ...")
            with gzip.open(os.path.join(file_path), mode="rt") as f:
                return check_line_in_a_file(f, delta_mins, date_selected)
        else:
            print(f"{file_path} is checking ...")
            with open(os.path.join(file_path), mode="r", encoding="utf-8") as f:
                return check_line_in_a_file(f, delta_mins, date_selected)

    except FileNotFoundError as file_not_find_error:
        print(str(file_not_find_error))


def check_line_in_a_file(f, delta_mins, date_selected=datetime.now()):
    """检测数据是否符合时间预期

    Args:
        f (_type_): 已经打开的文件
        delta_mins (int, optional): 期望的时间窗口，前后N分钟
        date_selected (_type_, optional): 日志查询窗口的中心时间戳

    Returns:
        _type_: _description_
    """
    if f.closed:
        return False

    try:
        first_line = f.readline()
        # read list line most efficient from f
        f.seek(0, SEEK_END)
        size = f.tell()
        f.seek(max(size-1024, 0), 0)
        lines = f.readlines()
        last_line = lines[-1]


        if not first_line and not last_line:
            return False

        log_start_timestamp_string = json.loads(first_line)["timestamp"]
        log_end_timestamp_string = json.loads(last_line)["timestamp"]
    except Exception:
        try:
            #2022-09-14T19:00:02.778000+
            log_start_timestamp_string = find_datetime_in_line(first_line)
            log_end_timestamp_string = find_datetime_in_line(last_line)
        except Exception:
            return False

    log_start_timestamp = parse(log_start_timestamp_string).timestamp()
    log_end_timestamp = parse(log_end_timestamp_string).timestamp()

    # print(f"{log_start_timestamp} --- {log_start_timestamp}")

    time_range_start_timestamp = (date_selected - timedelta(minutes=delta_mins)).timestamp()
    time_range_end_timestamp = (date_selected + timedelta(minutes=delta_mins)).timestamp()

    if time_range_start_timestamp > log_end_timestamp:
        return False

    if time_range_end_timestamp < log_start_timestamp:
        return False

    return True


def read_data_lines(data_f, date_selected, time_range):
    """ 读取log数据，并进行清洗

    Args:
        f (file_stream): 打开的文件描述符
    """
    if data_f.closed:
        raise RuntimeError("文件描述符不存在")

    # print(f"time_range: {time_range}")

    time_range_start_timestamp = (date_selected - timedelta(minutes=time_range)).timestamp()
    time_range_end_timestamp = (date_selected + timedelta(minutes=time_range)).timestamp()

    timestamp_points = []
    cur_voltage_values = []
    torque_values = []

    for line in data_f:
        data = json.loads(line.strip("\n"))
        # 选取传入时间戳范围内的所有时间
        log_line_time = parse(data["timestamp"])
        log_line_timestamp = log_line_time.timestamp()

        if log_line_timestamp < time_range_start_timestamp or log_line_timestamp > time_range_end_timestamp:
            continue

        # 获取相关的电压，扭矩，时间数据
        if (('message' in data.keys()) == False):
            if data["type"] == "n":
                continue

            timestamp_points.append(log_line_time)
            cur_voltage_values.append(data['v'])
            torque_values.append(data['t'])
        else:
            timestamp_points.append(log_line_time)
            cur_voltage_values.append(json.loads(data['message'])["curVoltageMainPower"])
            torque_values.append(json.loads(data['message'])["torque_actual_value"])

    return (timestamp_points, cur_voltage_values, torque_values)


def get_file_in_time_range(input_args, **kwargs):
    """_summary_

    Args:
        input_args (_type_): _description_

    Raises:
        RuntimeError:  输入错误的参数，kwargs['download_log']不为True的情况下，input_args的值不为"sort"或"pick"

    Returns:
        _type_: _description_
    """

    # if input_args.log_root_dir is None or empty, raise error
    if not input_args.log_root_dir:
        raise FileNotFoundError(f"--log_root_dir 不能为空")

    if "download_log" in kwargs and kwargs["download_log"]:
        return get_file_in_time_range_for_download(input_args.log_root_dir, input_args.time_range, parse(input_args.timestamp), **kwargs)

    # if input_args.robot_id is empty or None, raise RuntimeError
    if not input_args.robot_id:
        raise RuntimeError("robot_id is empty")

    if input_args.prd_type == "sort":
        return get_file_in_time_range_sort(input_args.robot_id, input_args.log_root_dir, input_args.time_range, parse(input_args.timestamp))

    if input_args.prd_type == "pick":
        return get_file_in_time_range_pick(input_args.robot_id, input_args.log_root_dir, input_args.time_range, parse(input_args.timestamp))

    raise RuntimeError("prd_type 参数错误， 不是sort或pick")


def get_file_in_time_range_sort(robot_id,  log_root_folder, time_range_in_mins=10, date_selected=datetime.now()):
    """ 遍历所有文件并保存所有日志文件

    Args:
        robot_id (string): 机器人编号
        log_root_folder (string): 日志文件根目录
        time_range_in_mins (int, optional): 基于选取日志的时间，确定选取日志范围的时间窗口
        date_selected (datetime, optional): 选取日志的时间

    Yields:
        generator(string): 目标文件路径的生成器
    """
    for maybe_shuttle_debug_folder in os.listdir(log_root_folder):
        if "shuttle-debug" not in maybe_shuttle_debug_folder:
            continue

        # 潜在可能的有效数据目录
        maybe_path = os.path.join(log_root_folder, maybe_shuttle_debug_folder)

        if not os.path.isdir(maybe_path):
            continue

        # pattern = re.compile(r".*[0-9]$")

        # 只读取log类型且格式为"shuttle-debug"的文件
        for single_log_file in os.listdir(maybe_path):
            if robot_id not in single_log_file:
                continue

            if is_file_in_time_range(os.path.join(maybe_path, single_log_file), time_range_in_mins, date_selected):
                yield os.path.abspath(os.path.join(maybe_path, single_log_file))


def get_file_in_time_range_pick(robot_id,  log_root_folder, time_range_in_mins=10, date_selected=datetime.now()):
    """ 遍历所有文件并保存所有日志文件

    Args:
        robot_id (string): 机器人编号
        log_root_folder (string): 日志文件根目录
        time_range_in_mins (int, optional): 基于选取日志的时间，确定选取日志范围的时间窗口
        date_selected (datetime, optional): 选取日志的时间

    Yields:
        generator(string): 目标文件路径的生成器
    """

    for root, dirs, files in os.walk(log_root_folder):
        for file_name in files:
            res = pick_load_file_match_res(file_name)
            log_file_full_path = os.path.abspath(os.path.join(root, file_name))

            if bool(res) and bool(re.search(rf"{robot_id}$", root)) and is_file_in_time_range(log_file_full_path, time_range_in_mins, date_selected):
                yield log_file_full_path


def get_file_in_time_range_for_download(log_root_folder, time_range_in_mins=10, date_selected=datetime.now(), **kwargs):
    """ 遍历所有文件并保存所有日志文件名,日志下载用

    Args:
        log_root_folder (string): 日志文件根目录
        time_range_in_mins (int, optional): 基于选取日志的时间，确定选取日志范围的时间窗口
        date_selected (datetime, optional): 选取日志的时间

    Yields:
        generator(string): 目标文件路径的生成器
    """
    if 'recursive' in kwargs and not kwargs['recursive']:
        for file in os.listdir(log_root_folder):
            log_file_full_path = os.path.abspath(os.path.join(log_root_folder, file))

            if os.path.isdir(log_file_full_path):
                continue

            if is_file_in_time_range(log_file_full_path, time_range_in_mins, date_selected):
                yield log_file_full_path

    if 'recursive' not in kwargs or ('recursive' in kwargs and kwargs['recursive']):
        for root, dirs, files in os.walk(log_root_folder):
            for file_name in files:
                log_file_full_path = os.path.abspath(os.path.join(root, file_name))

                if is_file_in_time_range(log_file_full_path, time_range_in_mins, date_selected):
                    yield log_file_full_path


def create_diagram(input_data, input_args):
    """生成图表

    Args:
        input_data (tuple): (timestamp_points(list),torque_values(list), cur_voltage_value(list))
        input_args (tuple): shell传入的参数
    """

    timestamp_points, cur_voltage_values, torque_values = input_data

    # 这步骤操作在 read_data_lines 的方法里直接做了,减少一次运算
    # log_datetime = np.vectorize(mdates.date2num)(timestamp_points)
    log_datetime = timestamp_points
    date_format = mdates.DateFormatter('%d-%m-%Y/%H:%M:%S')

    rect1 = [0.10, 0.5, 0.80, 0.40]
    ax1 = plt.axes(rect1)

    ax1.xaxis_date()
    ax1.plot(log_datetime, torque_values)

    ax1.set_yticks(range(-1400, 1400, 200))
    ax1.xaxis.set_major_formatter(date_format)
    ax1.tick_params(axis='both', labelsize=7)

    ax1.set_ylabel("torque")
    plt.setp(ax1.get_xticklabels(), rotation=30, ha="right")



    # # 绘制电压时间子图
    rect2 = [0.10, 0.15, 0.80, 0.15]
    ax2 = plt.axes(rect2)

    ax2.xaxis_date()
    ax2.plot(log_datetime, cur_voltage_values, linewidth=1, c='red')

    ax2.set_yticks(range(0, 70, 10))
    ax2.xaxis.set_major_formatter(date_format)

    ax2.tick_params(axis='both', labelsize=7)
    plt.setp(ax2.get_xticklabels(), rotation=30, ha="right")

    ax2.set_ylabel("voltage")

    plt.savefig(input_args.output_file)

    if input_args.plot_show:
        plt.show()


def pick_load_file_match_res(file_name):
    """匹配pick的负载log类型的文件名

    Args:
        file_name (string): log文件名

    Returns:
        match objects: Match objects
    """
    log_name_pattern = re.compile( r"""
                                    ^load-                   # 以load开头
                                    \d{4}-\d{2}-\d{2}        # 日期
                                    \.log                    # load-2022-08-19.log
                                    (?P<log_serial_number>\.\d)?     # 如load-2022-08-18.log.1.gz
                                    (?P<log_zip_suffix>\.gz)?     # 如load-2022-08-18.log.1.gz
                                    """, re.X)

    return log_name_pattern.search(file_name)


def find_datetime_in_line(line):
    """匹配log文件一行中的时间戳

    Args:
        line (string): log文件中的一行

    Returns:
        string: 时间戳的字符串格式
    """

    timestamp_pattern = re.compile(r"(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6})")
    m = re.search(timestamp_pattern, line)
    return m[0]
