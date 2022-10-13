import time
import json
import hashlib
from robot.api.deco import keyword

class Util(object):
    @keyword("get current time")
    def get_current_time(self,format):
        """
        获取当前时间的日期，并格式化
        """
        localtime = time.localtime()
        formatetime = time.strftime(format,localtime)
        print(formatetime)
        return formatetime

    @keyword("decode")
    def decode(self, customstr, mode):
        return customstr.decode(mode)

    @keyword("stringToJson")
    def stringToJson(self,body):
        ini_string = json.dumps(body)
        final_dictionary = json.loads(ini_string)
        return final_dictionary

    @keyword("GET MD5")
    def get_md5(self, str):
        """
        将字符转换md5
        """
        md5Key = hashlib.md5()
        str_utf8 = str.encode(encoding="utf-8")
        md5Key.update(str_utf8)
        md5_str = md5Key.hexdigest()
        return md5_str



if __name__ == '__main__':
    util=Util()
    util.get_current_time("%Y-%m-%d %H:%M:%S")
    body = {'vishesh': 1, 'ram': 5, 'prashant': 10, 'vishal': 15}
    util.stringToJson(body)