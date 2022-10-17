
from pathlib import Path
import json
import yaml

# DATABASE = Path() / "data" / "xiuxian"
DATABASE = Path() / "xiuxian"

class XiuConfig:

    def __init__(self):
        self.config_jsonpath = DATABASE / "config.json"


    def read_data(self):
        """配置数据"""
        with open(self.config_jsonpath, 'r', encoding='utf-8') as e:
            data = json.load(e)
            print(data)
            return data

    def write_data(self, user_id):
        json_data = self.read_data()
        json_data[user_id] = True
        with open(self.config_jsonpath, 'w+') as f:
            json.dump(json_data, f)


if __name__ == '__main__':
    # XiuConfig().write_data("抢灵石")
    # DATA = XiuConfig().read_data()

    name = '开启'
    if name in "开启":
        print('pass')