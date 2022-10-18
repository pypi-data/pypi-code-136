from numbers import Number
from pyConfObj import ConfObj

class PgServerConf(ConfObj):
    ip: str = ""
    port: Number = 5432
    username:str = ""
    password:str = ""

class MainConf(ConfObj):
    pgconf: PgServerConf = PgServerConf()
    timezone:str = "UTC"


if __name__ == "__main__":
    conf = MainConf()
    print("Default configuration:")
    print(conf.as_json())
    conf.pgconf.username = "admin"
    print("Modified configuration for pg: ")
    print(conf.pgconf.as_json())