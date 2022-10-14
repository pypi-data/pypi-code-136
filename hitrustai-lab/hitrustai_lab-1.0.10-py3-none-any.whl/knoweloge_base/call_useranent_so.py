from ctypes import c_char_p, POINTER, c_longlong, Structure, cdll


class GoSlice(Structure):
    _fields_ = [("data", POINTER(c_char_p)),
                ("len", c_longlong), ("cap", c_longlong)]


class UAInfo(Structure):
    _fields_ = [('DeviceType', c_char_p), ('DeviceModel', c_char_p), ('DeviceBrand', c_char_p),
                ('CPUArch', c_char_p), ('OSName',
                                        c_char_p), ('OSVersion', c_char_p),
                ('BrowserName', c_char_p), ('BrowserVersion',
                                            c_char_p), ('BrowserEngine', c_char_p)
                ]


def call_so(lib_path="../include/ua.so"):
    lib_ua = cdll.LoadLibrary(lib_path)
    return lib_ua


class UserAgentDecoder:
    def __init__(self, lib_path):
        self.lib_ua = self.read_so(lib_path=lib_path)

    def read_so(self, lib_path):
        lib_ua = cdll.LoadLibrary(lib_path)
        return lib_ua

    def run(self, ua, width, height, ratio, platform, gpuName):
        self.lib_ua.UADetection.argtypes = [GoSlice]
        self.lib_ua.UADetection.restype = UAInfo

        ua_result = self.lib_ua.UADetection(GoSlice((c_char_p * 6)(
            ua.encode(),
            width.encode(),
            height.encode(),
            ratio.encode(),
            platform.encode(),
            gpuName.encode()
        ), 6, 6))
        dict_ua = {
            "DeviceType": ua_result.DeviceType.decode(),
            "DeviceModel": ua_result.DeviceModel.decode(),
            "DeviceBrand": ua_result.DeviceBrand.decode(),
            "OSName": ua_result.OSName.decode(),
            "OSVersion": ua_result.OSVersion.decode(),
            "Browser": ua_result.BrowserName.decode(),
            "BrowserVersion": ua_result.BrowserVersion.decode(),
            "CPUArch": ua_result.CPUArch.decode(),
            "BrowserEngine": ua_result.BrowserEngine.decode(),
        }
        return dict_ua


def main():
    ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.158 Safari/537.36"
    width = "1680"
    height = "1050"
    ratio = "2"
    platform = "iPad"
    gpuName = "Apple GPU"
    uad = UserAgentDecoder("../../Gitlab/hitrustai/Module/useragent/ua.so")
    dict_ua = uad.run(ua, width, height, ratio, platform, gpuName)
    print(dict_ua)


if __name__ == '__main__':
    main()
