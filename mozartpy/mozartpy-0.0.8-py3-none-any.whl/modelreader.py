import os
import clr
import pandas as pd
import mozartpy.dataconverter as dc

filedir = os.path.dirname(os.path.abspath(__file__))
dllFolder = os.path.join(filedir, 'dlls')
clr.AddReference(os.path.join(dllFolder, 'Mozart.Task.Model.dll'))
clr.AddReference(os.path.join(dllFolder, 'Mozart.DataActions.dll'))

from Mozart.Task.Model import ModelEngine
from Mozart.DataActions import ILocalAccessor

class Model:
    """
    Baseclass for various mozart objects.
    """
    engine = None
    name = ''
    path = ''
    results = []
    inputs = []
    outputs = []

    def __init__(self, path):
        ''' 모델의 Input 아이템들 중에 key 해당하는 값을 찾아서 dataframe 형식으로 반환

        :param
            path(string): 모델파일의 path
        '''

        self.path = path
        self.__readModel()

    def __readModel(self):
        ''' 초기 입력된 model path 의 파일을 읽어서 Inputs, Outputs, Results 정보를 읽어 변수에 저장

        '''
        self.engine = ModelEngine.Load(self.path)
        self.name = self.engine.Name

        for item in self.engine.Inputs.ItemArray:
            self.inputs.append(item.Name)

        for result in self.engine.Experiments[0].ResultList:
            self.results.append(result.Key)

        for item in self.engine.Outputs.ItemArray:
            self.outputs.append(item.Name)

    def GetInputItem(self, key):
        ''' 모델의 Input 아이템들 중에 key 해당하는 값을 찾아서 dataframe 형식으로 반환

        :param
            key(string): input 아이템의 이름
        :return
            dataframe : key 에 해당하는 input table을 dataFrame 형식으로 변환하여 반환
        '''
        acc = ILocalAccessor(self.engine.LocalAccessorFor(key))
        dt = acc.QueryTable('', -1, -1)
        df = dc.TableToDataFrame(dt)
        return df

    def GetOutputItem(self, rname, key):
        ''' 모델의 Output 아이템들 중에 key 해당하는 값을 찾아서 dataframe 형식으로 반환

        :param
            key(string): output 아이템의 이름
            rname(string) : 모델의 result 이름
        :return
            dataframe : key 에 해당하는 output table을 dataFrame 형식으로 변환하여 반환
        '''
        if key == '':
            print('{0} is not found key'.format(key))
            pass

        if not self.outputs.__contains__(key):
            print('{0} is not found output item name'.format(key))
            pass

        result = self.GetResult(rname)
        if result is None:
            print('{0} is not found result'.format(rname))
            pass

        try:
            acc = ILocalAccessor(result.LocalAccessorFor(key))
            dt = acc.QueryTable('', -1, -1)
            df = dc.TableToDataFrame(dt)
            return df
        except Exception as err:
            print(str(err))

    def GetOutputItemByCvs(self,  rname, key):
        if key == '':
            print('{0} is empty'.format(key))
            pass

        if not self.outputs.__contains__(key):
            print('{0} is not found key'.format(key))
            pass

        result = self.GetResult(rname)
        if result is None:
            print('{0} is not found result'.format(rname))
            pass

        try:
            acc = ILocalAccessor(result.LocalAccessorFor(key))
            filepath = os.path.join(acc.DataDirectory, key)
            df = pd.read_csv(filepath + '.csv')
            return df
        except Exception as err:
            print(str(err))

    def GetResult(self, key):
        for result in self.engine.Experiments[0].ResultList:
            if result.Key == key:
                return result
