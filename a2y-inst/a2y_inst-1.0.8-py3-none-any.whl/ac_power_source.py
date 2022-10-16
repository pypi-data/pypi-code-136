# 搜索国内品牌的可程控交流电源，发现几个品牌使用的外观（按键布局、显示屏类型）极为类似，
# 而且都同样的功率为 350VA 的型号都默认不带通讯口，价格也都基本一致（可以说一分不差）。
# 可合理怀疑这几个品牌的产品全都来自同一个祖宗。估计通信协议也不会有啥区别。
# 这个驱动为它而作。希望它们能够真的互相兼容，和平相处。
from a2y_modbus import FixMaster as _MBMaster
from serial import Serial as _Serial
from typing import Union as _Union


class ACPowerSource:
	def __init__(self, port: _Union[str, _Serial], station: int = 1, timeout: float = 0.3):
		if isinstance(port, str):
			com = _Serial(port=port, baudrate=9600, timeout=timeout)
			self.__com = com
		else:
			# 如果传入的 port 参数是一个已经构建好的 Serial 对象，则此对象的关闭操作由其构建者执行。
			# 本对象不管理此 Serial 对象。见本类的 close 成员函数。
			com = port
			self.__com = None
		self.__mb = _MBMaster(com, station=station, timeout=timeout)

	def set_frequency(self, hz: float):
		"""
		设置交流电源输出的频率。传入参数的单位是赫兹（Hz），传给仪器时需要使用 16bit 整数，单位是 0.1Hz。
		"""
		value = int(round(hz * 10, 0))
		self.__mb.write_register(7, value)

	def set_voltage(self, volt: float):
		"""
		设置交流电源的输出电压。传入参数的单位是伏（V），传给仪器时需要使用 16bit 整数，单位是 0.1V。
		"""
		value = int(round(volt * 10, 0))
		self.__mb.write_register(8, value)

	def out_on(self):
		self.__mb.write_register(9, 1)

	def out_off(self):
		self.__mb.write_register(9, 0)

	def close(self):
		if isinstance(self.__com, _Serial):
			self.__com.close()

	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.close()
