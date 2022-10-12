import binascii
import time
import base64


class ConvertBase64:

    @staticmethod
    def encode(text: str):
        return base64.b64encode(text.encode('ascii')).decode('ascii')

    @staticmethod
    def decode(text: str):
        try:
            return base64.b64decode(text.encode('ascii')).decode('ascii')
        except binascii.Error:
            return base64.b64decode(text.encode('ascii') + b"==").decode('ascii')


class Stopwatch:

    def __init__(self):
        self._time = 0

    def start(self):
        self._time = time.time()
        return self

    def stop(self):
        self._time = time.time() - self._time

    def print(self, unit=None, precision=2, show_unit=1):
        division_table = {'h': 360, 'm': 60, 's': 1, 'ms': 0.001}
        unit_table = {'ms': "milliseconds", 's': "seconds", 'm': "minutes", 'h': "hours"}
        if unit not in division_table:
            for key, val in division_table.items():
                if self._time >= val:
                    unit = key
                    break
            else:
                unit = 'ms'
        unit_text = ""
        if show_unit == 1:
            unit_text = " " + unit
        elif show_unit == 2:
            unit_text = " " + unit_table[unit]
        elif show_unit == 3:
            unit_text = " " + unit_table[unit].capitalize()
        return f"{(self._time / division_table[unit]):.{precision}f}{unit_text}"

    def __str__(self):
        return str(self._time)
