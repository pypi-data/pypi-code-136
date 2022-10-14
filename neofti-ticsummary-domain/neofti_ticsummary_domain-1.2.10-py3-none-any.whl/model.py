from tracemalloc import start
from ticsummary_domain import dataTIC, databaseMYSQL, inputDataHandler
from ticsummary_domain.ui.mainWindow import MainWindow, ModeInterface as MWModeInterface
from ticsummary_domain.ui.connectionConfigurationDialog import ConnectionConfiguration
from ticsummary_domain.ui.openSqlDataDialog import OpenSQLData
from ticsummary_domain.ui.chooseRecordDialog import ChooseRecordDialog
from ticsummary_domain import databaseMYSQL
from ticsummary_domain.backWorking import factoryThreadByTask
from ticsummary_domain import modeShowData as modeSD
from ticsummary_domain import outputDataHandler

from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QMessageBox
import numpy as np

class Model(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.__initView__()
        self.__initSignal__()
        self.__initThreadPool__()
        self.sqlParameters = None
        self.currentModeSD = modeSD.modeShowData.MANUALMODE
        self.profileXDescriptionDevice = dataTIC.DescriptionDevice("profileX",0,31)
        self.profileYDescriptionDevice = dataTIC.DescriptionDevice("profileY",32,63)

        self.currentManualIdData = 1
        self.currentManualSumIdData = 1
        self.currentManualSumCountData = 2
    def __initView__(self):
        self.mainWindow = MainWindow(version='1.2.10')
        self.mainWindow.show()
    def __initThreadPool__(self):
        self.threadPool = QtCore.QThreadPool.globalInstance()
        self.threadPool.setMaxThreadCount(60)
        
    def __initSignal__(self):
        self.mainWindow.comboBoxType.currentIndexChanged.connect(self.__typeChanged)
        self.mainWindow.actionConnectionSqlDatabase.triggered.connect(self.openConnectionConfiguration)
        self.mainWindow.actionFrom_sql_database.triggered.connect(self.startOpenSQLData)
        self.mainWindow.pushButtonChooseRecord.clicked.connect(self.openChooseRecordDialog)
        self.mainWindow.sigIterationValueId.connect(self.iterationData)
        self.mainWindow.sigSetNewId.connect(self.setIdData)
        self.mainWindow.sigSetNewCountSum.connect(self.setNewCountSum)
        self.mainWindow.actionExportDataToCsv.triggered.connect(self.exportData)
        #self.mainWindow.connectSignalIterationValueId(self.iterationData)
        #self.mainWindow.ui.comboBoxListData.currentTextChanged.connect(self.loadDataByIdAndPlot)
    
    def __del__(self):
        if hasattr(self, "connector"):
            self.connector.close()
    
    def openConnectionConfiguration(self):
        connectionConfigurationDialog = ConnectionConfiguration(parent=self.mainWindow, parameters=self.sqlParameters)
        connectionConfigurationDialog.setModal(True)
        connectionConfigurationDialog.exec()
        if connectionConfigurationDialog.result() == QtWidgets.QDialog.DialogCode.Accepted:
            #self.mainWindow.setInfinityProgress(True)
            self.sqlParameters = connectionConfigurationDialog.getNewParameters()
            self.connector = databaseMYSQL.openConnection(self.sqlParameters)
            self.updateSizeDB(databaseMYSQL.getCountRecords(self.sqlParameters.table, self.connector))
            self.currentModeSD.uninit(self)
            self.currentModeSD = modeSD.modeShowData.MANUALMODE
            self.mainWindow.setMode(self.currentModeSD.modeInterface)
            self.currentModeSD.init(self)

    def __loadNewConnection__(self,sqlParameters):
        self.listData = databaseMYSQL.getListId(self.sqlParameters)

    def loadDataByIdAndPlot(self,id:str, connector=None):
        i = 0
        if connector == None:
            self.controllerBWTask = factoryThreadByTask(self.__loadDataById__,self.__plotData__,id=int(id),connector=self.connector)
        else:
            self.controllerBWTask = factoryThreadByTask(self.__loadDataById__,self.__plotData__,id=int(id),connector=connector)
        self.controllerBWTask.start()

    '''def __loadDataById__(self,id,connector):
        dataB1 = databaseMYSQL.getRecordByIdFirstBank(self.sqlParameters.table, self.connector, id)
        dataB2 = databaseMYSQL.getRecordByIdSecondBank(self.sqlParameters.table, self.connector, id)
        self.loadedData = (dataB1.matrix,dataB1.timeslice,dataB2.matrix,dataB2.timeslice,dataB1,dataB2)'''
        #resultSignature = namedtuple('SingleResult','MatrixB1','TimeSliceB1','MatrixB2','TimeSliceB2','DataB1','DataB2','DateTime')
    def __plotData__(self,loadedData):
        self.profileX1Data = inputDataHandler.getMatrixByFromToFilter(loadedData.matrixB1, self.profileXDescriptionDevice.channelFrom, self.profileXDescriptionDevice.channelTo)
        self.profileY1Data = inputDataHandler.getMatrixByFromToFilter(loadedData.matrixB1, self.profileYDescriptionDevice.channelFrom, self.profileYDescriptionDevice.channelTo)
        self.profileX2Data = inputDataHandler.getMatrixByFromToFilter(loadedData.matrixB2, self.profileXDescriptionDevice.channelFrom, self.profileXDescriptionDevice.channelTo)
        self.profileY2Data = inputDataHandler.getMatrixByFromToFilter(loadedData.matrixB2, self.profileYDescriptionDevice.channelFrom, self.profileYDescriptionDevice.channelTo)
        self.scaleChannelToMM = 2
        self.mainWindow.setData(
            self.profileX1Data,
            float(loadedData.timeSliceB1/(10**6)),
            0,#float(loadedData.delayB1/(10**6)),
            self.profileY1Data,
            float(loadedData.timeSliceB1/(10**6)),
            0,#float(loadedData.delayB1/(10**6)),
            self.profileX2Data,
            float(loadedData.timeSliceB2/(10**6)),
            0,#float(loadedData.delayB2/(10**6)),
            self.profileY2Data,
            float(loadedData.timeSliceB2/(10**6)),
            0,#float(loadedData.delayB2/(10**6)),
            self.scaleChannelToMM)
        self.descriptionLoadedData = loadedData.description
        self.mainWindow.setDataInfo(loadedData.description)
        self.checkBorderIdValue()
        if self.mainWindow.isBusy:
            self.mainWindow.setBusyMode(False)
        self.mainWindow.enableControlDataMode()
        #self.mainWindow.loadPrevModeInterface()
        #self.mainWindow.flagControlKeysOff = False

    def iterationData(self,it):
        #if self.mainWindow.flagControlKeysOff:
        #    return
        self.currentModeSD.iterationId(self,it)
        '''
        self.mainWindow.flagControlKeysOff = True
        if self.typeShow == 0:
            if (self.currentManualIdData + it > -1 or self.currentManualIdData + it < self.countRecordsInDB):
                self.__setValueCurrentId(self.currentManualIdData + it)
                self.controlerBWTask = factoryThreadByTask(self.__backThreadLoadData__, self.__plotData__,id=self.currentManualIdData,connector=self.connector)
                self.controlerBWTask.start()
        elif self.typeShow == 2:
            self.firstIdManualSum = self.firstIdManualSum + self.countManualSum*it
            self.loadSumDataPlot(self.firstIdManualSum, self.countManualSum)
            self.mainWindow.setIdValue(self.firstIdManualSum)
            self.mainWindow.flagControlKeysOff = False'''

    def setIdData(self,value):
        self.currentModeSD.setId(self,value)

        '''self.mainWindow.flagControlKeysOff = True
        if self.typeShow == 0:
            if (value > -1 or value < self.countRecordsInDB):
                self.__setValueCurrentId(value)
                self.__backThreadLoadData__(self.currentManualIdData,self.connector)
                self.__plotData__()
        elif self.typeShow == 2:
            self.firstIdManualSum = value
            self.mainWindow.setIdValue(self.firstIdManualSum)
            self.loadSumDataPlot(self.firstIdManualSum, self.countManualSum)
        self.mainWindow.flagControlKeysOff = False'''


    def updateSizeDB(self,value=None):
        if (value==None):
            value = databaseMYSQL.getCountRecordsByParameters(self.sqlParameters)
        self.countRecordsInDB = value
        self.mainWindow.setRangeId(0, self.countRecordsInDB)

    def __typeChanged(self,id):
        self.currentModeSD.uninit(self)
        if id == 0:
            self.currentModeSD = modeSD.modeShowData.MANUALMODE
        if id == 1:
            self.currentModeSD = modeSD.modeShowData.ONLINE
        if id == 2:
            self.currentModeSD = modeSD.modeShowData.MANUALSUMMODE
        self.currentModeSD.init(self)
        self.mainWindow.setMode(self.currentModeSD.modeInterface)

    def checkBorderIdValue(self):
        if self.currentModeSD == modeSD.modeShowData.MANUALMODE:
            self.mainWindow.setButtonPrevEnabled(not self.currentManualIdData == 1)
            self.mainWindow.prevEnabled = not self.currentManualIdData == 1
            self.mainWindow.setButtonNextEnabled(not self.currentManualIdData == self.countRecordsInDB)
            self.mainWindow.nextEnabled = not self.currentManualIdData == self.countRecordsInDB
        elif self.currentModeSD == modeSD.modeShowData.MANUALSUMMODE:
            self.mainWindow.setButtonPrevEnabled(not self.currentManualSumIdData - self.currentManualSumCountData < 1)
            self.mainWindow.prevEnabled = not self.currentManualSumIdData - self.currentManualSumCountData < 1
            self.mainWindow.setButtonNextEnabled(not self.currentManualSumIdData + self.currentManualSumCountData > self.countRecordsInDB)
            self.mainWindow.nextEnabled = not self.currentManualSumIdData + self.currentManualSumCountData > self.countRecordsInDB

    def setNewCountSum(self,value):
        self.currentManualSumCountData = value
        self.currentModeSD.setId(self,self.currentManualSumIdData)

    def openChooseRecordDialog(self):
        chooseRecordDialog = ChooseRecordDialog(self.mainWindow,self)
        chooseRecordDialog.setIdRecordSignal.connect(self.setIdData)
        #chooseRecordDialog.setModal(True)
        chooseRecordDialog.show()

    '''def loadSumData(self,id,count):
        dataB1List = list()
        dataB2List = list()
        for i in range(id, id + count):
            dataB1List.append(databaseMYSQL.getRecordByIdFirstBank(self.sqlParameters.table, self.connector, i))
            dataB2List.append(databaseMYSQL.getRecordByIdSecondBank(self.sqlParameters.table, self.connector, i))
        sumDataB1 = np.zeros(shape=(np.size(dataB1List[0].matrix,0),np.size(dataB1List[0].matrix,1)))
        sumDataB2 = np.zeros(shape=(np.size(dataB2List[0].matrix,0),np.size(dataB2List[0].matrix,1)))
        for i in range(count):
            sumDataB1 += dataB1List[i].matrix
            sumDataB2 += dataB2List[i].matrix
        self.loadedData = (sumDataB1,dataB1List[0].timeslice,sumDataB2,dataB2List[0].timeslice)'''
    def startOpenSQLData(self):
        self.mainWindow.setInfinityProgress()
        self.handlerTaskOpenData = runTask(self.taskOpenData,self.endOpenSqlData)
        
    def taskOpenData(self):
        self.openSQLData = OpenSQLData(self.sqlParameters, lambda result: self.setNewListData(result))
        
    def endOpenSqlData(self):
        self.mainWindow.unsetInfinityProgress()
        self.openSQLData.show()

    def setNewConnectionParameters(self, parameters):
        self.sqlParameters = parameters
        
    def setNewListData(self, list):
        self.listData = list

    def exportData(self):
        outputDataHandler.saveDataToCSV(self.mainWindow, [['X Buffer 1',self.profileX1Data ],['Y Buffer 1',self.profileY1Data ],['X Buffer 2',self.profileX2Data ],['Y Buffer 2',self.profileY2Data ]], f'{self.descriptionLoadedData} Scale_Channel_MM={self.scaleChannelToMM}')