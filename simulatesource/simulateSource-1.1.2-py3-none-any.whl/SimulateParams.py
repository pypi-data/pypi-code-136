from enum import Enum


# 模拟参数类
class SimulateParams():
    utcTime = None
    enableLocalEph = False
    localEphFile = None
    simulateTimeList = [0 for _ in range(7)]

    # 时间格式检验
    def simulateTimetest(self, year, month, day, hour, minute, second):
        if month<=12 and day<=31 and hour<=24 and minute<=60 and second<=60:
            # 判断时间数据格式
            self.simulateTimeList[0] = (year >> 8) & 0xFF
            self.simulateTimeList[1] = year & 0xff
            self.simulateTimeList[2] = month
            self.simulateTimeList[3] = day
            self.simulateTimeList[4] = hour
            self.simulateTimeList[5] = minute
            self.simulateTimeList[6] = second
            return self.simulateTimeList
        else:
            print("时间数据格式错误，重新模拟")

    # 增益等级类
    class Gain(Enum):
        GAIN_Lv_1 = 0
        GAIN_Lv_2 = 1
        GAIN_Lv_3 = 2
        GAIN_Lv_4 = 3
        GAIN_Lv_5 = 4
        GAIN_Lv_6 = 5
        GAIN_Lv_7 = 6
        GAIN_Lv_8 = 7
        GAIN_off = 8


