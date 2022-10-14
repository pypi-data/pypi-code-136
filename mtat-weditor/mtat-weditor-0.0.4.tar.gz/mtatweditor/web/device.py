# coding: utf-8
#

import abc

import adbutils
import uiautomator2 as u2
import wda
from logzero import logger
from PIL import Image
from tidevice import Usbmux, ConnectionType

from . import uidumplib


class DeviceMeta(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def screenshot(self) -> Image.Image:
        pass

    def dump_hierarchy(self) -> str:
        pass

    @abc.abstractproperty
    def device(self):
        pass


class _AndroidDevice(DeviceMeta):
    def __init__(self, device_url):
        d = u2.connect(device_url)
        # 登陆界面无法截图，就先返回空图片
        d.settings["fallback_to_blank_screenshot"] = True
        self._d = d

    def screenshot(self):
        return self._d.screenshot()

    def dump_hierarchy(self):
        return uidumplib.get_android_hierarchy(self._d)

    def dump_hierarchy2(self):
        current = self._d.app_current()
        page_xml = self._d.dump_hierarchy(pretty=True)
        page_json = uidumplib.android_hierarchy_to_json(
            page_xml.encode('utf-8'))
        return {
            "xmlHierarchy": page_xml,
            "jsonHierarchy": page_json,
            "activity": current['activity'],
            "packageName": current['package'],
            "windowSize": self._d.window_size(),
        }

    @property
    def device(self):
        return self._d


class _AppleDevice(DeviceMeta):
    def __init__(self, device_url):
        logger.info("ios connect: %s", device_url)
        if device_url.startswith('http'):
            c = wda.Client(device_url)
        elif device_url != "":
            c = wda.USBClient(device_url)
        else:
            c = wda.USBClient()
        self._client = c
        self.__scale = c.scale
        self.__device_url = device_url

    def screenshot(self):
        self.check_wda()
        return self._client.screenshot(format='pillow')

    def dump_hierarchy(self):
        self.check_wda()
        return uidumplib.get_ios_hierarchy(self._client, self.__scale)

    def dump_hierarchy2(self):
        self.check_wda()
        return {
            "jsonHierarchy":
            uidumplib.get_ios_hierarchy(self._client, self.__scale),
            "windowSize":
            self._client.window_size(),
        }

    def check_wda(self):
        try:
            self._client.status()
        except:
            if not self.__device_url.startswith('http'):
                logger.info("ios connect: %s", self.__device_url)
                c = wda.USBClient(self.__device_url)
                self._client = c
                self.__scale = c.scale

    @property
    def device(self):
        return self._client


cached_devices = {}


def connect_device(platform, device_url):
    """
    Returns:
        deviceId (string)
    """
    device_id = platform + ":" + device_url
    if platform == 'android':
        d = _AndroidDevice(device_url)
    elif platform == 'ios':
        d = _AppleDevice(device_url)
    else:
        raise ValueError("Unknown platform", platform)

    cached_devices[device_id] = d
    return device_id


def get_device(id):
    d = cached_devices.get(id)
    if d is None:
        platform, uri = id.split(":", maxsplit=1)
        connect_device(platform, uri)
    return cached_devices[id]


def get_devices(platform):
    if platform == 'android':
        ds = adbutils.adb.device_list()
        ds = [info.serial for info in ds]
    elif platform == 'ios':
        ds = Usbmux().device_list()
        ds = [info.udid for info in ds if info.conn_type == ConnectionType.USB]
    return ds

