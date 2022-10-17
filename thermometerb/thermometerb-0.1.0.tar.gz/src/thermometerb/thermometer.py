"""Class for Thermometer state machine."""
from typing import Any, Optional, Union


class Thermometer:
    """A class that represents a thermometer. The class acts as a state machine
    keeping track of the last 3 temperatures supplied. Determining increase
    and decrease in temperature is a comparison between the current and previous
    temperature unless determining changes by full degrees. Full degree changes
    include comparison to the third temperature to determine if a full degree
    change has occurred.

    The class is configurable as to boiling and freezing points. When either
    of those points are reached notifications happen unless configured differently.
    Notification can be configured to occur only on full degree changes or in a
    specific direction (increase/decrease). All configurations can be set when an
    instance of the class is instantiated or changed on the fly with each new
    temperature reading.
    """

    BOOL_DEFAULT: bool = False
    HUNDRED_CELSIUS: float = 100.0
    ZERO_CELSIUS: float = 0.0

    def __init__(self, **kwargs: Any):
        """A class that represents a thermometer.

        :keyword boil: Float of temperature threshold in Celsius for boiling.
            Defaults to 100.0ºC.
        :keyword freeze: Float of temperature threshold in Celsius for freezing.
            Defaults to 0.0ºC.
        :keyword full_degree: Bool if a notification should only be sent when a
            threshold has been exceeded by a full degree point (whole number not
            decimal). Default False.
        :keyword increase: Bool if a notification should only be sent if previous temp was an
            increase to reach boil/freeze threshold. Default False.
        :keyword decrease: Bool if a notification should only be sent if previous temp was a
            decrease to reach boil/freeze threshold. Default False.
        :raise ValueError: If boil or freeze temperature data can not be converted to a float.
        """

        self.boil: float = self.HUNDRED_CELSIUS
        self.freeze: float = self.ZERO_CELSIUS
        self.full_degree: bool = self.BOOL_DEFAULT
        self.increase: bool = self.BOOL_DEFAULT
        self.decrease: bool = self.BOOL_DEFAULT
        # memory works by keeping the three most recent temperatures.
        # index 0 = current temperature
        # index 1 = previous temperature
        # index 2 = oldest temperature
        self.__memory__: list = [
            self.ZERO_CELSIUS,
            self.ZERO_CELSIUS,
            self.ZERO_CELSIUS,
        ]

        self.__set_data_attributes(**kwargs)

    def __call__(self, temperature: float, **kwargs) -> dict:
        """
        :param temperature: Float of new temperature.
        :keyword boil: Float of temperature threshold in Celsius for boiling.
            Defaults to 100.0ºC.
        :keyword freeze: Float of temperature threshold in Celsius for freezing.
            Defaults to 0.0ºC.
        :keyword full_degree: Bool if a notification should only be sent when a
            threshold has been exceeded by a full degree point (whole number not
            decimal). Default False.
        :keyword increase: Bool if a notification should only be sent if previous temp was an
            increase to reach boil/freeze threshold. Default False.
        :keyword decrease: Bool if a notification should only be sent if previous temp was a
            decrease to reach boil/freeze threshold. Default False.
        :raise ValueError: If boil, freeze, or temperature data can not be converted to a float.
        :return: Dictionary of temperature in Celsius and Fahrenheit. Includes notification
            if threshold is met.
        """
        self.__set_data_attributes(**kwargs)
        c_temp = self.current_temp(temperature)
        c_temp_dict: dict = {
            "celsius": c_temp,
            "fahrenheit": self.current_temp_fahrenheit(),
            "notification": self.notification(),
        }
        return c_temp_dict

    def current_temp(self, temperature: Optional[float] = None) -> float:
        """Set the current temperature.
        :param temperature: Float of the current temperature.
        :return: Float of the current temperature in Celsius.
        :raise ValueError: If temperature can not be converted to a float.
        """
        if temperature is not None:
            cache_memory: list = self.__memory__

            self.__memory__.pop()
            try:
                self.__memory__.insert(0, float(temperature))
            except ValueError as exc:
                self.__memory__ = cache_memory
                raise ValueError(
                    self.__value_error_msg("current_temp", str(temperature), "float")
                ) from exc
        return self.__memory__[0]

    def current_temp_fahrenheit(self) -> float:
        """:return: Float of the current temperature in Fahrenheit."""
        return self.__celsius_to_fahrenheit(self.current_temp())

    def previous_temp(self) -> float:
        """:return: Float of the previous temperature in Celsius."""
        return self.__memory__[1]

    def previous_temp_fahrenheit(self) -> float:
        """:return: Float of the previous temperature in Fahrenheit."""
        return self.__celsius_to_fahrenheit(self.previous_temp())

    @staticmethod
    def __celsius_to_fahrenheit(temperature: float) -> float:
        """Convert Celsius temperature to Fahrenheit.
        :param temperature: Float of the Celsius temperature to convert.
        :return: Fahrenheit temperature.
        """
        return (temperature * 1.8) + 32.0

    def notification(self) -> Union[str, None]:
        """Notification message if the threshold is met via a change in temperature.

        Note - If the temperature is unchanged, no notification is sent as the threshold
        was already met.

        :return: Notification if threshold is met.
        """
        boiling: str = "You have reached the boiling point."
        freezing: str = "You have reached the freezing point."
        notice = None

        if self.current_temp() == self.boil:
            notice = self.__message_for_temp_change(boiling)
        elif self.current_temp() == self.freeze:
            notice = self.__message_for_temp_change(freezing)

        return notice

    def __message_for_temp_change(self, msg: str) -> Union[str, None]:
        """
        :param msg: String message to return if there is a temperature change.
        :return: String message or None if no temperature change.
        """
        if self.increase or self.decrease:
            if self.increase and self.__temperature_increase():
                notice = msg
            elif self.decrease and self.__temperature_decrease():
                notice = msg
            else:
                notice = None
        elif self.__temperature_increase() or self.__temperature_decrease():
            notice = msg
        else:
            notice = None

        return notice

    def __set_data_attributes(self, **kwargs: Any):
        """Set data attributes based kwargs supplied.

        :keyword boil: Float of temperature threshold in Celsius for boiling.
            Defaults to 100.0ºC.
        :keyword freeze: Float of temperature threshold in Celsius for freezing.
            Defaults to 0.0ºC.
        :keyword full_degree: Bool if a notification should only be sent when a
            threshold has been exceeded by a full degree point (whole number not
            decimal). Default False.
        :keyword increase: Bool if a notification should only be sent if previous temp was an
            increase to reach boil/freeze threshold. Default False.
        :keyword decrease: Bool if a notification should only be sent if previous temp was a
            decrease to reach boil/freeze threshold. Default False.
        :raise ValueError: If boil or freeze temperature data can not be converted to a float.
        """
        if "boil" in kwargs:
            try:
                self.boil: float = float(kwargs["boil"])
            except ValueError as exc:
                raise ValueError(
                    self.__value_error_msg("boil", kwargs["boil"], "float")
                ) from exc

        if "freeze" in kwargs:
            try:
                self.freeze: float = float(kwargs["freeze"])
            except ValueError as exc:
                raise ValueError(
                    self.__value_error_msg("freeze", kwargs["freeze"], "float")
                ) from exc

        if "full_degree" in kwargs:
            self.full_degree: bool = bool(kwargs["full_degree"])
        if "increase" in kwargs:
            self.increase: bool = bool(kwargs["increase"])
        if "decrease" in kwargs:
            self.decrease: bool = bool(kwargs["decrease"])

    def __temperature_increase(self) -> bool:
        """:return Bool of the temperature change."""
        if self.full_degree:
            temp_increase = int(self.previous_temp()) < int(self.current_temp())
            temp_equal = int(self.previous_temp()) == int(self.current_temp())
            if not temp_increase and temp_equal:
                temp_increase = int(self.__memory__[2]) < int(self.current_temp())
        else:
            temp_increase = self.previous_temp() < self.current_temp()
        return temp_increase

    def __temperature_decrease(self) -> bool:
        """:return Bool of the temperature change."""
        if self.full_degree:
            temp_decrease = int(self.previous_temp()) > int(self.current_temp())
            temp_equal = int(self.previous_temp()) == int(self.current_temp())
            if not temp_decrease and temp_equal:
                temp_decrease = int(self.__memory__[2]) > int(self.current_temp())
        else:
            temp_decrease = self.previous_temp() > self.current_temp()
        return temp_decrease

    @staticmethod
    def __value_error_msg(location: str, value: str, cast_type: str) -> str:
        """
        Format an error message for ValueError.
        :param location: String of the data attribute.
        :param value: String of the value being converted.
        :param cast_type: String of the type being cast to.
        :return: String of formatted error message.
        """
        return f"Can not convert {location} value {value} to a {cast_type}."
