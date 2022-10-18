from numbers import Number
from pyConfObj import ConfObj

class PgServerConf(ConfObj):
    ip: str = ""
    port: Number = 5432
    username:str = ""
    password:str = ""

    def check_pass(self) -> bool:
        for el in [self.ip, self.username, self.password]:
            if el in ["", None]:
                return False
        if self.port in[0, None]:
            return False
        return True
class MainConf(ConfObj):
    pgconf: PgServerConf = PgServerConf()
    timezone:str = "UTC"


if __name__ == "__main__":
    import sys
    print(sys.path)

    conf = MainConf()
    print("Default configuration:")
    print(conf.as_json())
    print(f"Valid configuration: {conf.check()}")
    conf.pgconf.username = "admin"
    conf.pgconf.ip = "1.1.1.1"
    conf.pgconf.password = "qwerty"
    print("Modified configuration for pg: ")
    print(conf.pgconf.as_json())
    print(f"Valid configuration: {conf.check()}")
