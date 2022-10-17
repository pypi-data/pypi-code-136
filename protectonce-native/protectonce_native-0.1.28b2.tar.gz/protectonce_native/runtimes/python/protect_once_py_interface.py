from ctypes import c_char_p, cast, cdll, c_bool, c_int, c_size_t, byref, RTLD_GLOBAL, CDLL
import os.path as path
from shutil import ExecError


class ProtectOnceInterface:
    def __init__(self):
        libagent_core = path.join(path.dirname(path.abspath(
            path.join(__file__, "../.."))), 'out/libagent_core.so')
        self._core_interface = CDLL(libagent_core)

    def init_core(self):
        core_index_file = path.join(path.dirname(path.abspath(
            path.join(__file__, "../.."))), 'core/core.js')
        self._core_interface.protect_once_start.restype = c_char_p
        started = self._core_interface.protect_once_start(
            core_index_file.encode('utf-8'))

    def invoke(self, function_name, data):
        self._core_interface.core_interface.restype = c_char_p
        result = self._core_interface.core_interface(
            function_name.encode('UTF-8'), data.encode('UTF-8'))
        return cast(result, c_char_p).value

    def shutdown_core(self):
        stopped = self._core_interface.protectonce_shutdown()

    def _to_bytes(self, strValue):
        try:
            if (isinstance(strValue, bytes)):
                return strValue

            return strValue.encode('utf-8')
        except:
            # TODO: print exception
            return b''
