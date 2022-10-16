import bisect
import ipaddress
import logging
import socket
import struct

from ip_city_handler.constents import IPV4_TYPE, IPV6_TYPE
from ip_city_handler.data import IpCityInfo
from ip_city_handler.exception import IpDataNotReadyException
from ip_city_handler.parser import IpDataParser, Ipv6DataParser

logger = logging.getLogger("ip_city")


class IpCityHandler(object):
    """
    IPCity类，处理IP搜索请求
    """

    def __init__(self, v4_path: str, v6_path: str = None):
        self.v4_path: str = v4_path
        self.v6_path: str = v6_path
        self.city_list: list = []
        self.ip_list: list = []
        self.city_index_list: list = []
        self.v6_city_list: list = []
        self.v6_ip_list: list = []
        self.v6_city_index_list: list = []
        self.data_file = None
        self.load_data()

    def load_data(self) -> None:
        if self.v4_path:
            v4_parser = IpDataParser(self.v4_path)
            v4_parser.load_data()
            self.city_list = v4_parser.city_list
            self.ip_list = v4_parser.ip_list
            self.city_index_list = v4_parser.city_index_list
        if self.v6_path:
            v6_parser = Ipv6DataParser(self.v6_path)
            v6_parser.load_data()
            self.v6_city_list = v6_parser.city_list
            self.v6_ip_list = v6_parser.ip_list
            self.v6_city_index_list = v6_parser.city_index_list

    def get_v4_city_index(self, ip_digit: int):
        if not self.ip_list:
            raise IpDataNotReadyException
        ip_index = bisect.bisect(self.ip_list, ip_digit) - 1
        return self.city_index_list[ip_index]

    def get_v6_city_index(self, ip_digit: int):
        if not self.ip_list:
            raise IpDataNotReadyException
        ip_index = bisect.bisect(self.v6_ip_list, ip_digit) - 1
        return self.v6_city_index_list[ip_index]

    def _search_v4(self, ip_digit: int) -> IpCityInfo:
        city_index = self.get_v4_city_index(ip_digit)
        return self.city_list[city_index]

    def _search_v6(self, ip_digit: int) -> IpCityInfo:
        city_index = self.get_v6_city_index(ip_digit)
        return self.v6_city_list[city_index]

    def _validate_ip_str(self, ip: str, ip_type: str) -> bool:
        """
        校验IP地址合法性
        """
        try:
            ipaddress.IPv6Address(
                ip
            ) if ip_type == IPV6_TYPE else ipaddress.IPv4Address(ip)
            return True
        except Exception as err:
            logger.error("IPAddress Invalid: %s", err)
            return False

    def search_v4(self, ip: str) -> (bool, IpCityInfo):
        if not self._validate_ip_str(ip, IPV4_TYPE):
            return False, IpCityInfo()
        ip_digit = struct.unpack("!I", socket.inet_pton(socket.AF_INET, ip))[0]
        return True, self._search_v4(ip_digit)

    def search_v6(self, ip: str) -> (bool, IpCityInfo):
        if not self._validate_ip_str(ip, IPV6_TYPE):
            return False, IpCityInfo()
        network_num, host_num = struct.unpack(
            "!QQ", socket.inet_pton(socket.AF_INET6, ip)
        )
        if network_num == 0 and ((host_num & 0xFFFF00000000) == 0xFFFF00000000):
            return True, self._search_v4(host_num)
        else:
            return True, self._search_v6(network_num)

    def search(self, ip: str) -> (bool, IpCityInfo):
        if ":" in ip:
            return self.search_v6(ip)
        else:
            return self.search_v4(ip)
