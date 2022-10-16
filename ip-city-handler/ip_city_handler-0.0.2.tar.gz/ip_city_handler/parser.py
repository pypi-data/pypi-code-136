import datetime
import logging
import os
import struct

from ip_city_handler.constents import IP_DATA_VERSION
from ip_city_handler.data import IpCityInfo

logger = logging.getLogger("ip_city")


class IpDataParser(object):
    LIBRARY_NUMBER = 1

    def __init__(self, path: str):
        self.data_file = None
        self.path = path
        self.city_number = 0
        self.city_code_length = 0
        self.ip_length = 0
        self.ip_number = 0
        self.city_struct_flag = ""
        self.city_list = []
        self.ip_list = []
        self.city_index_list = []

    def _check_data_file(self) -> int:
        """
        检查IP数据文件
        :return:
        0: 文件正常
        -2: 文件格式错误
        -3: 文件版本不匹配
        -4: 数据版本错误
        """
        magic, version, library = struct.unpack(">4sBB", self.data_file.read(6))
        logger.info("magic: %s, version: %s, library: %s", magic, version, library)
        if magic != b"ipCT":
            return -2
        if version != IP_DATA_VERSION:
            return -4
        if library != self.LIBRARY_NUMBER:
            return -3
        return 0

    def _parser_header(self) -> int:
        """
        解析数据文件头部
        :return:
        0: 文件正常
        -2: 文件格式错误
        -3: 文件版本不匹配
        -4: 数据版本过旧
        """
        check_result = self._check_data_file()
        if check_result != 0:
            logger.error("check data file field, error code: %s", check_result)
            return check_result
        (
            self.ip_length,
            self.city_code_length,
            self.city_number,
            self.ip_number,
            update_time,
            create_time,
        ) = struct.unpack(">BBIIII", self.data_file.read(18))
        if self.city_number > 65536:
            self.city_struct_flag = ">I"
        elif self.city_number > 256:
            self.city_struct_flag = ">H"
        else:
            self.city_struct_flag = ">B"
        update_time = datetime.datetime.fromtimestamp(update_time)
        create_time = datetime.datetime.fromtimestamp(create_time)
        logger.info(
            "IP Data UpdateTime: %s Data File CreateTime: %s",
            update_time.strftime("%Y-%m-%d %H:%M:%S"),
            create_time.strftime("%Y-%m-%d %H:%M:%S"),
        )
        return 0

    def _load_city_info(self):
        """
        加载城市信息
        :return:
        """
        self.city_list = [
            IpCityInfo(
                *tuple(self.data_file.readline().decode("utf8").strip("\n").split("\t"))
            )
            for _ in range(self.city_number)
        ]

    def _load_ip_info(self):
        """
        加载IP信息
        :return:
        """
        for _ in range(self.ip_number):
            buffer = self.data_file.read(self.ip_length)
            self.ip_list.append(struct.unpack(">I", buffer)[0])
            buffer = self.data_file.read(self.city_code_length)
            self.city_index_list.append(
                struct.unpack(
                    self.city_struct_flag,
                    (b"\0" + buffer) if self.city_code_length == 3 else buffer,
                )[0]
            )

    def load_data(self) -> int:
        """
        载入IP数据库
        :return:
        0: 成功
        -1: 文件不存在
        -2: 文件格式错误
        -3: 文件版本不匹配
        -4: 数据版本过旧
        """
        if not os.path.exists(self.path):
            return -1
        with open(self.path, "rb") as self.data_file:
            check_result = self._parser_header()
            if check_result != 0:
                return check_result
            self._load_city_info()
            self._load_ip_info()
        return 0


class Ipv6DataParser(IpDataParser):
    LIBRARY_NUMBER = 2

    def _load_ip_info(self):
        """
        加载IP信息
        :return:
        """
        for _ in range(self.ip_number):
            buffer = self.data_file.read(self.ip_length)
            self.ip_list.append(struct.unpack(">Q", buffer)[0])
            buffer = self.data_file.read(self.city_code_length)
            self.city_index_list.append(
                struct.unpack(
                    self.city_struct_flag,
                    (b"\0" + buffer) if self.city_code_length == 3 else buffer,
                )[0]
            )
