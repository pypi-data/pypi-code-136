from core.constant import _AIR_CN_HOSTS, _AIR_SG_HOSTS
from core.region import Region


class Param(object):
    def __init__(self):
        self.application_id: str = ""
        self.tenant_id: str = ""
        self.token: str = ""
        self.retry_times: int = 0
        self.schema: str = "https"
        self.hosts: list = []
        self.headers: dict = {}
        self.region: Region = Region.UNKNOWN
        self.ak: str = ""
        self.sk: str = ""
        self.use_air_auth: bool = False


class Context(object):
    def __init__(self, param: Param):
        self._check_required_field(param)
        self.tenant: str = param.application_id
        self.tenant_id: str = param.tenant_id
        self.token: str = param.token
        self.customer_headers: dict = param.headers
        self.schema: str = param.schema
        self.use_air_auth: bool = param.use_air_auth
        self.hosts: list = []
        self.volc_auth_conf: VolcAuthConf = VolcAuthConf(param)
        self._adjust_hosts(param)

    @staticmethod
    def _check_required_field(param: Param) -> None:
        if len(param.application_id) == 0:
            raise Exception("Application id is empty")
        if len(param.tenant_id) == 0:
            raise Exception("Tenant id is emtpy")
        if param.region == Region.UNKNOWN:
            raise Exception("Region is empty")
        Context._check_auth_required_field(param)

    @staticmethod
    def _check_auth_required_field(param: Param) -> None:
        if param.use_air_auth and param.token == "":
            raise Exception("Token is empty")

        if not param.use_air_auth and (param.sk == "" or param.ak == ""):
            raise Exception("Ak or sk is empty")

    def _adjust_hosts(self, param: Param) -> None:
        if len(param.hosts) > 0:
            self.hosts = param.hosts
            return
        if param.region == Region.AIR_CN:
            self.hosts = _AIR_CN_HOSTS
            return
        if param.region == Region.AIR_SG:
            self.hosts = _AIR_SG_HOSTS
            return


class VolcAuthConf(object):
    def __init__(self, param: Param):
        self.ak: str = param.ak
        self.sk: str = param.sk
        self.region: str = self._parse_region(param)

    def _parse_region(self, param: Param):
        return "cn-north-1"
