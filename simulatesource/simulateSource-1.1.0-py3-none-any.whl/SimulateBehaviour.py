from simulateSource.SimulateSource import SimulateSource
class SimulateBehaviour(SimulateSource.ISimulateSourceInterface):

    def __init__(self, com):
        self.com = com
        self.simulateSource = SimulateSource(self.com)
        self.simulateSource.register(self)
        # traceSimulateParams = self.simulateSource.getTraceSimulateParams()
        # # 设置模拟增益traceSimulateParams.Gain['gain_Lv1']
        # traceSimulateParams.traceGain = traceSimulateParams.Gain.GAIN_Lv_1.value
        # # 输轨迹文件名（NMEA格式）
        # traceSimulateParams.fileName = "role.txt"
        # # 设置模拟时间
        # traceSimulateParams.simulateTime = traceSimulateParams.simulateTimetest(2022,12,1,16,30,10)
        # # 读取轨迹文件内容
        # self.simulateSource.readTrackFile(traceSimulateParams.fileName)
        # # 设置模拟参数
        # self.simulateSource.setTraceSimulateParams(traceSimulateParams)
        # # 开始轨迹模拟

        # self.simulateSource.startTraceModeSimulate()

        singleSimulateParams = self.simulateSource.getSingleSimulateParams()
        # 设置单点参数
        singleSimulateParams.longitude = 123.397128
        singleSimulateParams.latitude = 59.916527
        singleSimulateParams.altitude= 100
        # 设置模拟增益traceSimulateParams.Gain['gain_Lv1']
        singleSimulateParams.singleGain= singleSimulateParams.Gain.GAIN_Lv_1.value
        # 设置模拟时间
        singleSimulateParams.simulateTime =  singleSimulateParams.simulateTimetest(2022, 8, 1, 16, 30, 10)
        # 开始单点仿真
        self.simulateSource.setSingleSimulateParams(singleSimulateParams)
        self.simulateSource.startSingleModeSimulate()






    def onSimulateState(self, simulateState):
        print("模拟状态simulateState: ", simulateState)


    def onSimulateMode(self, Mode):
        print("仿真模式SimulateMode: ", Mode)

    def onCurrentGian(self, gain):
        print("onCurrentGian: ", gain)


    def onListenSetSimulateTime(self, year, month, day, hour, minute):
        print("监听设置模拟时间onListenSetSimulateTime: ", year, month, day, hour, minute)


    def onListenSimulateTrackSpeed(self, speed):
        print("监听轨迹模拟速度onListenSimulateTrackSpeed: ", speed)


    def onEnableLocalEPH(self, enable):
        print("使能本地星历数据onEnableLocalEPH: ", enable)



    def onListenStartTrackSimulate(self, startTrackSimulate):
        print("开始轨迹模拟", startTrackSimulate)


    def onListenStopTrackSimulate(self, stopTrackSimulate):
        print("正在结束轨迹仿真", stopTrackSimulate)


    def onListenStartInitTackSimulate(self, maxValue):
        print("正在初始化轨迹模拟")

    def onListenCountInitTrackSimulate(self, countInitTrackSimulate):
        print("初始化轨迹模拟计数：%d" %countInitTrackSimulate)


    def onListenReInitTrackSimulate(self, state):
        print("正在重新初始化轨迹模拟", state)

    def onListenEndInitTrackSimulate(self, state):
        print("结束初始化", state)

    def onListenSendDoneTrackSimulate(self, state):
        print("完成轨迹发送", state)


    def onListenSendTrackTimeOut(self, state):
        print("轨迹数据发送超时", state)


    def onListenFailInitTrackSimulate(self, state):
        print("初始化失败", state)


    def onListenStartSingleSimulate(self, startSingleSimulate):
        print("单点仿真已开启：", startSingleSimulate)

    def onListenStopSingleSimulate(self, stopSingleSimulate):
        print("正在结束单点仿真", stopSingleSimulate)

if __name__ == "__main__":
    simulateBehaviour = SimulateBehaviour("COM3")
