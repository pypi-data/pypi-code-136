from boatrace.models import (
    Disqualification,
    MotorParts,
    RaceLaps,
    Weather,
    WinningTrick,
)


class DisqualificationFactory:
    @staticmethod
    def create(name: str):
        if "転" in name:
            return Disqualification.CAPSIZE
        elif "落" in name:
            return Disqualification.FALL
        elif "沈" in name:
            return Disqualification.SINKING
        elif "妨" in name:
            return Disqualification.VIOLATION
        elif "失" in name:
            return Disqualification.DISQUALIFICATION_AFTER_START
        elif "エ" in name:
            return Disqualification.ENGINE_STOP
        elif "不" in name:
            return Disqualification.UNFINISHED
        elif "返" in name:
            return Disqualification.REPAYMENT_OTHER_THAN_FLYING_AND_LATENESS
        elif "Ｆ" in name:
            return Disqualification.FLYING
        elif "Ｌ" in name:
            return Disqualification.LATENESS
        elif "欠" in name:
            return Disqualification.ABSENT
        elif "＿" in name:
            # NOTE: これは失格ではない
            # レース不成立で着順が定まらなかったケース
            # 例)
            # http://boatrace.jp/owpc/pc/race/raceresult?rno=11&jcd=23&hd=20170429
            # TODO:
            return None
        else:
            raise ValueError


class MotorPartsFactory:
    @staticmethod
    def create(name: str):
        if "電気" in name:
            return MotorParts.ELECTRICAL_SYSTEM
        elif "キャブ" in name:
            return MotorParts.CARBURETOR
        elif "ピストン" == name:
            return MotorParts.PISTON
        elif "リング" in name:
            return MotorParts.PISTON_RING
        elif "シリンダ" in name:
            return MotorParts.CYLINDER
        elif "ギア" in name:
            return MotorParts.GEAR_CASE
        elif "ギヤ" in name:
            return MotorParts.GEAR_CASE
        elif "キャリ" in name:
            return MotorParts.CARRIER_BODY
        else:
            raise ValueError


class RaceLapsFactory:
    METRE_PER_A_LAP = 600

    @classmethod
    def create(cls, metre: int):
        return RaceLaps(metre / cls.METRE_PER_A_LAP)


class WinningTrickFactory:
    @staticmethod
    def create(name: str):
        if "逃げ" == name:
            return WinningTrick.NIGE
        elif "差し" == name:
            return WinningTrick.SASHI
        elif "まくり" == name:
            return WinningTrick.MAKURI
        elif "まくり差し" == name:
            return WinningTrick.MAKURIZASHI
        elif "抜き" == name:
            return WinningTrick.NUKI
        elif "恵まれ" == name:
            return WinningTrick.MEGUMARE
        else:
            raise ValueError


class WeatherFactory:
    @staticmethod
    def create(name: str):
        if "晴" in name:
            return Weather.FINE
        elif "曇" in name:
            return Weather.CLOUDY
        elif "雨" in name:
            return Weather.RAINY
        elif "雪" in name:
            return Weather.SNOWY
        elif "台風" in name:
            return Weather.TYPHOON
        elif "霧" in name:
            return Weather.FOG
        else:
            raise ValueError
