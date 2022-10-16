from dataclasses import dataclass


@dataclass
class IpCityInfo:
    """
    IPInfo数据类，保存地区数据运营商等数据
    """

    nation: str = None
    province: str = None
    city: str = None
    district: str = None
    isp: str = None
    backbone_isp: str = None
    nation_code: int = None
    district_code: int = None

    def __str__(self) -> str:
        msg = "国家: {}|省: {}|市: {}|区: {}|接入运营商: {}|骨干运营商: {}".format(
            self.nation,
            self.province,
            self.city,
            self.district,
            self.isp,
            self.backbone_isp,
        )
        return msg

    @property
    def data(self):
        return {key: val for key, val in self.__dict__.items()}
