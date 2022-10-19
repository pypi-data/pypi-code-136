# -*- coding: cp1252 -*-


#   Copyright 2017 - 2022 Jäger Computergesteuerte Messtechnik GmbH
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


import array
import ctypes
import inspect
import struct
import sys

if sys.platform == 'win32':
    if (sys.version_info[0] == 3):
        import winreg as _winreg
    else:
        import _winreg

try:
    import numpy as np
    _isNumpyAvailable = True
except:
    _isNumpyAvailable = False

version = '0.5'


# ADwin-Exception
class ADwinError(Exception):
    def __init__(self, functionName, errorText, errorNumber):
        self.functionName = functionName
        self.errorText = str(errorText)
        self.errorNumber = errorNumber

    def __str__(self):
        if sys.version_info[0] == 3:
            return 'Function %s, errorNumber %d: %s' % (self.functionName, self.errorNumber, self.errorText.removeprefix('b\'').removesuffix('\''))
        else:
            return 'Function ' + self.functionName + ', errorNumber ' + str(self.errorNumber) + ': ' + str(self.errorText)


class ADsim:
    __err = ctypes.c_int32(0)
    __errPointer = ctypes.pointer(__err)

    def __init__(self, DeviceNo=1, raiseExceptions=1, useNumpyArrays=0):

        if useNumpyArrays and not _isNumpyAvailable:
            raise ModuleNotFoundError("No module named 'numpy'")

        if sys.platform.startswith('linux'):
            try:
                if sys.version_info[0] == 3:
                    f = open('/etc/adwin/ADWINDIR', 'r')
                else:
                    f = file('/etc/adwin/ADWINDIR', 'r')
                self.ADwindir = f.readline()[:-1] + '/'  # without newline at the end
                self.dll = ctypes.CDLL(self.ADwindir + 'lib/libadsim.so')
            except:
                raise ADwinError('__init__', 'shared library libadsim.so not found.', 200)
            f.close()
            self.dll.Set_DeviceNo(DeviceNo)

        if sys.platform.startswith("win32"):
            try:
                aKey = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, r"SOFTWARE\Jäger Meßtechnik GmbH\ADwin\Directory")
                self.ADwindir = str(_winreg.QueryValueEx(aKey, 'BTL')[0])
                _winreg.CloseKey(aKey)
            except:
                try:
                    aKey = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Jäger Meßtechnik GmbH\ADwin\Directory")
                    self.ADwindir = str(_winreg.QueryValueEx(aKey, 'BTL')[0])
                    _winreg.CloseKey(aKey)
                except:
                    try:
                        aKey = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Wow6432Node\ADwin\Directory")
                        self.ADwindir = str(_winreg.QueryValueEx(aKey, 'BTL')[0])
                        _winreg.CloseKey(aKey)
                    except:
                        raise ADwinError('__init__', 'Could not read Registry.', 200)
            try:
                if struct.calcsize("P") == 4:
                    self.dll = ctypes.WinDLL('c:\\windows\\adsim32.dll')
                else:
                    self.dll = ctypes.WinDLL('c:\\windows\\adsim64.dll')
                    # self.dll = ctypes.WinDLL('adsim64.dll')
                self.dll.DeviceNo = DeviceNo
            except:
                raise ADwinError('__init__', 'ADsim-DLL not found.', 200)

        self.raiseExceptions = raiseExceptions
        self.DeviceNo = DeviceNo
        self.useNumpyArrays = useNumpyArrays

    def __checkError(self, functionName):
        if self.__err.value != 0 and self.raiseExceptions != 0:
            raise ADwinError(functionName, self.ADsim_Get_Last_Error_Text(self.__err.value), self.__err.value)

    # system control and system information

    # Set_DeviceNo
    def ADsim_Set_DeviceNo(self, DeviceNo):
        '''ADsim_Set_DeviceNo sets the device number for the ADwin system on which the Simulink model is runnning. Necessary to use ADsim functions. '''
        if sys.platform.startswith("win32"):
            self.dll.Set_DeviceNo(DeviceNo)
        else:
            self.dll.Set_DeviceNo_ADsim(DeviceNo)
        self.__checkError(inspect.currentframe().f_code.co_name)

    # Register_Value
    def Register_Value(self, Filename, NodePath):
        '''%Register_Value  registers the address of a specified node in the model and returns a unique valueID.'''
        if (sys.version_info[0] == 3):
            valueID = self.dll.Register_Value(Filename.encode(), NodePath.encode(), self.__errPointer)
        else:
            valueID = self.dll.Register_Value(Filename, NodePath, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)
        return valueID

    def Register_Value_MultipleDevices(self, Filename, NodePath, DevNo, ProcNo):
        '''%Register_Value  registers the address of a specified node in the model and returns a unique valueID.'''
        if (sys.version_info[0] == 3):
            valueID = self.dll.Register_Value_MultipleDevices(Filename.encode(), NodePath.encode(), DevNo, ProcNo, self.__errPointer)
        else:
            valueID = self.dll.Register_Value_MultipleDevices(Filename, NodePath, DevNo, ProcNo, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)
        return valueID

    def __Register_Value_MultipleDevices_Zero_Based(self, Filename, NodePath, DevNo, ProcNo):
        '''%Register_Value  registers the address of a specified node in the model and returns a unique valueID.'''
        if (sys.version_info[0] == 3):
            valueID = self.dll.Register_Value_MultipleDevices_Zero_Based(Filename.encode(), NodePath.encode(), DevNo, ProcNo, self.__errPointer)
        else:
            valueID = self.dll.Register_Value_MultipleDevices_Zero_Based(Filename, NodePath, DevNo, ProcNo, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)
        return valueID

    def Register_Value_MD0(self, Filename, NodePath, DevNo, ProcNo):
        '''%Register_Value_MD0 registers the address of a specified node in the model and returns a unique valueID.'''
        return self.__Register_Value_MultipleDevices_Zero_Based(Filename, NodePath, DevNo, ProcNo)

    def Register_Value_MD1(self, Filename, NodePath, DevNo, ProcNo):
        '''%Register_Value_MD1 registers the address of a specified node in the model and returns a unique valueID.'''
        return self.Register_Value_MultipleDevices(Filename, NodePath, DevNo, ProcNo)

    # Process control

    # Transfer of global variables
    def Get_Int8(self, ValueID):
        '''Get_Int8 returns the value of a simulink model parameter or signal, from a model runnning on an ADwin system as int8.'''
        self.dll.Get_Int8.restype = ctypes.c_byte
        ret = self.dll.Get_Int8(ValueID, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)
        return ret

    def Set_Int8(self, ValueID, Value):
        '''Set_Int8 sets the value of a simulink model parameter or signal, from a model runnning on an ADwin system as int8.'''
        self.dll.Set_Int8(ValueID, Value, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)

    def Get_UInt8(self, ValueID):
        '''Get_UInt8 returns the value of a simulink model parameter or signal, from a model runnning on an ADwin system as uint8.'''
        self.dll.Get_UInt8.restype = ctypes.c_uint8
        ret = self.dll.Get_UInt8(ValueID, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)
        return ret

    def Set_UInt8(self, ValueID, Value):
        '''Set_UInt8 sets the value of a simulink model parameter or signal, from a model runnning on an ADwin system as uint8.'''
        self.dll.Set_UInt8(ValueID, Value, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)

    def Get_Int16(self, ValueID):
        '''Get_Int16 returns the value of a simulink model parameter or signal, from a model runnning on an ADwin system as int16.'''
        self.dll.Get_Int16.restype = ctypes.c_int16
        ret = self.dll.Get_Int16(ValueID, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)
        return ret

    def Set_Int16(self, ValueID, Value):
        '''Set_Int16 sets the value of a simulink model parameter or signal, from a model runnning on an ADwin system as int16.'''
        self.dll.Set_Int16(ValueID, Value, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)

    def Get_UInt16(self, ValueID):
        '''Get_UInt16 returns the value of a simulink model parameter or signal, from a model runnning on an ADwin system as uint16.'''
        self.dll.Get_UInt16.restype = ctypes.c_uint16
        ret = self.dll.Get_UInt16(ValueID, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)
        return ret

    def Set_UInt16(self, ValueID, Value):
        '''Set_UInt16 sets the value of a simulink model parameter or signal, from a model runnning on an ADwin system as uint16.'''
        self.dll.Set_UInt16(ValueID, Value, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)

    def Get_Int32(self, ValueID):
        '''Get_Int32  returns the value of a simulink model parameter or signal, from a model runnning on an ADwin system as int32.'''
        self.dll.Get_Long.restype = ctypes.c_int32
        ret = self.dll.Get_Long(ValueID, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)
        return ret

    def Set_Int32(self, ValueID, Value):
        '''Set_Int32 sets the value of a simulink model parameter or signal, from a model runnning on an ADwin system as int32.'''
        self.dll.Set_Long(ValueID, Value, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)

    def Get_UInt32(self, ValueID):
        '''Get_UInt32  returns the value of a simulink model parameter or signal, from a model runnning on an ADwin system as uint32.'''
        self.dll.Get_ULong.restype = ctypes.c_uint32
        ret = self.dll.Get_ULong(ValueID, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)
        return ret

    def Set_UInt32(self, ValueID, Value):
        '''Set_UInt32 sets the value of a simulink model parameter or signal, from a model runnning on an ADwin system as uint32.'''
        self.dll.Set_ULong(ValueID, Value, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)

    def Set_Single(self, ValueID, Value):
        '''Set_Single sets the value of a simulink model parameter or signal, from a model runnning on an ADwin system as single.'''
        _val = ctypes.c_float(Value)
        self.dll.Set_Float(ValueID, _val, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)

    def Get_Single(self, ValueID):
        '''Get_Single returns the value of a global float variable.'''
        self.dll.Get_Float.restype = ctypes.c_float
        ret = self.dll.Get_Float(ValueID, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)
        return ret

    def Set_Double(self, ValueID, Value):
        '''Set_Double sets the value of a simulink model parameter or signal, from a model runnning on an ADwin system as double.'''
        _val = ctypes.c_double(Value)
        self.dll.Set_Double(ValueID, _val, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)

    def Get_Double(self, ValueID):
        '''Get_Double returns the value of a global double variable.'''
        self.dll.Get_Double.restype = ctypes.c_double
        ret = self.dll.Get_Double(ValueID, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)
        return ret

    def Set_Bool(self, ValueID, Value):
        '''Set_Bool sets the value of a simulink model parameter or signal, from a model runnning on an ADwin system as uint8.'''
        _val = ctypes.c_uint8(Value)
        self.dll.Set_Bool(ValueID, _val, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)

    def Get_Bool(self, ValueID):
        '''Get_Bool returns the value of a global uint8 variable.'''
        self.dll.Get_Bool.restype = ctypes.c_uint8
        ret = self.dll.Get_Bool(ValueID, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)
        return ret

    # Array
    def GetArray_Int8(self, ValueID, Startindex, Count):
        '''GetArray_Int8  returns the array values of a simulink model parameter or signal, from a model runnning on an ADwin system as int8.'''
        dataType = ctypes.c_int8 * Count
        values = dataType(0)
        self.dll.GetArray_Int8(ValueID, values, Startindex, Count, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)
        if self.useNumpyArrays:
            return np.array(values, dtype=np.int8)
        else:
            return values

    def SetArray_Int8(self, ValueID, Values, Startindex, Count):
        '''SetArray_Int8 transfers int8 data from the PC into a DATA array of the ADwin system.'''
        if _isNumpyAvailable:
            data = np.array(Values, dtype=np.int8)
            ptr = data.ctypes.data_as(ctypes.POINTER(ctypes.c_int8))
            self.dll.SetArray_Int8(ValueID, ptr, Startindex, Count, self.__errPointer)
        else:
            if type(Values) in [list, array.array]:
                # convert list to ctypes.c_int8_Array
                dataType = ctypes.c_int8 * Count
                values = dataType(0)
                for i in range(Count):
                    values[i] = Values[i]
            else:  # ctypes-array
                values = Values
            self.dll.SetArray_Int8(ValueID, values, Startindex, Count, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)

    def GetArray_UInt8(self, ValueID, Startindex, Count):
        '''GetArray_UInt8  returns the array values of a simulink model parameter or signal, from a model runnning on an ADwin system as uint8.'''
        dataType = ctypes.c_uint8 * Count
        values = dataType(0)
        self.dll.GetArray_UInt8(ValueID, values, Startindex, Count, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)
        if self.useNumpyArrays:
            return np.array(values, dtype=np.uint8)
        else:
            return values

    def SetArray_UInt8(self, ValueID, Values, Startindex, Count):
        '''SetArray_UInt8 transfers uint8 data from the PC into a DATA array of the ADwin system.'''
        if _isNumpyAvailable:
            data = np.array(Values, dtype=np.uint8)
            ptr = data.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8))
            self.dll.SetArray_UInt8(ValueID, ptr, Startindex, Count, self.__errPointer)
        else:
            if type(Values) in [list, array.array]:
                # convert list to ctypes.c_uint8_Array
                dataType = ctypes.c_uint8 * Count
                values = dataType(0)
                for i in range(Count):
                    values[i] = Values[i]
            else:  # ctypes-array
                values = Values
            self.dll.SetArray_UInt8(ValueID, values, Startindex, Count, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)

    def GetArray_Int16(self, ValueID, Startindex, Count):
        '''GetArray_Int16  returns the array values of a simulink model parameter or signal, from a model runnning on an ADwin system as int16.'''
        dataType = ctypes.c_int16 * Count
        values = dataType(0)
        self.dll.GetArray_Int16(ValueID, values, Startindex, Count, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)
        if self.useNumpyArrays:
            return np.array(values, dtype=np.int16)
        else:
            return values

    def SetArray_Int16(self, ValueID, Values, Startindex, Count):
        '''SetArray_Int16 transfers uint16 data from the PC into a DATA array of the ADwin system.'''
        if _isNumpyAvailable:
            data = np.array(Values, dtype=np.int16)
            ptr = data.ctypes.data_as(ctypes.POINTER(ctypes.c_int16))
            self.dll.SetArray_Int16(ValueID, ptr, Startindex, Count, self.__errPointer)
        else:
            if type(Values) in [list, array.array]:
                # convert list to ctypes.c_int16_Array
                dataType = ctypes.c_int16 * Count
                values = dataType(0)
                for i in range(Count):
                    values[i] = Values[i]
            else:  # ctypes-array
                values = Values
            self.dll.SetArray_Int16(ValueID, values, Startindex, Count, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)

    def GetArray_UInt16(self, ValueID, Startindex, Count):
        '''GetArray_UInt16  returns the array values of a simulink model parameter or signal, from a model runnning on an ADwin system as uint16.'''
        dataType = ctypes.c_uint16 * Count
        values = dataType(0)
        self.dll.GetArray_UInt16(ValueID, values, Startindex, Count, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)
        if self.useNumpyArrays:
            return np.array(values, dtype=np.uint16)
        else:
            return values

    def SetArray_UInt16(self, ValueID, Values, Startindex, Count):
        '''SetArray_UInt16 transfers uint16 data from the PC into a DATA array of the ADwin system.'''
        if _isNumpyAvailable:
            data = np.array(Values, dtype=np.uint16)
            ptr = data.ctypes.data_as(ctypes.POINTER(ctypes.c_uint16))
            self.dll.SetArray_UInt16(ValueID, ptr, Startindex, Count, self.__errPointer)
        else:
            if type(Values) in [list, array.array]:
                # convert list to ctypes.c_uint16_Array
                dataType = ctypes.c_uint16 * Count
                values = dataType(0)
                for i in range(Count):
                    values[i] = Values[i]
            else:  # ctypes-array
                values = Values
            self.dll.SetArray_UInt16(ValueID, values, Startindex, Count, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)

    def GetArray_Int32(self, ValueID, Startindex, Count):
        '''GetArray_Int32  returns the array values of a simulink model parameter or signal, from a model runnning on an ADwin system as int32.'''
        dataType = ctypes.c_int32 * Count
        values = dataType(0)
        self.dll.GetArray_Long(ValueID, values, Startindex, Count, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)
        if self.useNumpyArrays:
            return np.array(values, dtype=np.int32)
        else:
            return values

    def SetArray_Int32(self, ValueID, Values, Startindex, Count):
        '''SetArray_Int32 transfers int32 data from the PC into a DATA array of the ADwin system.'''
        if _isNumpyAvailable:
            data = np.array(Values, dtype=np.int32)
            ptr = data.ctypes.data_as(ctypes.POINTER(ctypes.c_int32))
            self.dll.SetArray_Long(ValueID, ptr, Startindex, Count, self.__errPointer)
        else:
            if type(Values) in [list, array.array]:
                # convert list to ctypes.c_int32_Array
                dataType = ctypes.c_int32 * Count
                values = dataType(0)
                for i in range(Count):
                    values[i] = Values[i]
            else:  # ctypes-array
                values = Values
            self.dll.SetArray_Long(ValueID, values, Startindex, Count, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)

    def GetArray_UInt32(self, ValueID, Startindex, Count):
        '''GetArray_UInt32  returns the array values of a simulink model parameter or signal, from a model runnning on an ADwin system as uint32.'''
        dataType = ctypes.c_uint32 * Count
        values = dataType(0)
        self.dll.GetArray_ULong(ValueID, values, Startindex, Count, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)
        if self.useNumpyArrays:
            return np.array(values, dtype=np.uint32)
        else:
            return values

    def SetArray_UInt32(self, ValueID, Values, Startindex, Count):
        '''SetArray_UInt32 transfers uint32 data from the PC into a DATA array of the ADwin system.'''
        if _isNumpyAvailable:
            data = np.array(Values, dtype=np.uint32)
            ptr = data.ctypes.data_as(ctypes.POINTER(ctypes.c_uint32))
            self.dll.SetArray_ULong(ValueID, ptr, Startindex, Count, self.__errPointer)
        else:
            if type(Values) in [list, array.array]:
                # convert list to ctypes.c_uint32_Array
                dataType = ctypes.c_uint32 * Count
                values = dataType(0)
                for i in range(Count):
                    values[i] = Values[i]
            else:  # ctypes-array
                values = Values
            self.dll.SetArray_ULong(ValueID, values, Startindex, Count, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)

    def GetArray_Single(self, ValueID, Startindex, Count):
        '''GetArray_Single returns the array element value of a simulink model parameter or signal,
        from a model runnning on an ADwin system as float32.'''
        dataType = ctypes.c_float * Count
        values = dataType(0)
        self.dll.GetArray_Float(ValueID, values, Startindex, Count, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)
        if self.useNumpyArrays:
            return np.array(values, dtype=np.float32)
        else:
            return values

    def SetArray_Single(self, ValueID, Values, Startindex, Count):
        '''SetArray_Single set the array values of a simulink model parameter or signal, from a model runnning on an ADwin system as float32.'''
        if _isNumpyAvailable:
            data = np.array(Values, dtype=np.float32)
            ptr = data.ctypes.data_as(ctypes.POINTER(ctypes.c_float))
            self.dll.SetArray_Float(ValueID, ptr, Startindex, Count, self.__errPointer)
        else:
            if type(Values) in [list, array.array]:
                # convert list to ctypes.c_float_Array
                dataType = ctypes.c_float * Count
                values = dataType(0)
                for i in range(Count):
                    values[i] = Values[i]
            else:  # ctypes.c_float_Array
                values = Values
            self.dll.SetArray_Float(ValueID, values, Startindex, Count, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)

    def GetArray_Double(self, ValueID, Startindex, Count):
        '''GetArray_Double returns the array element value of a simulink model parameter or signal,
        from a model runnning on an ADwin system as double.'''
        dataType = ctypes.c_double * Count
        values = dataType(0)
        self.dll.GetArray_Double(ValueID, values, Startindex, Count, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)
        if self.useNumpyArrays:
            return np.array(values, dtype=np.double)
        else:
            return values

    def SetArray_Double(self, ValueID, Values, Startindex, Count):
        '''SetArray_Double set the array values of a simulink model parameter or signal, from a model runnning on an ADwin system as double.'''
        if _isNumpyAvailable:
            data = np.array(Values, dtype=np.double)
            ptr = data.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
            self.dll.SetArray_Double(ValueID, ptr, Startindex, Count, self.__errPointer)
        else:
            if type(Values) in [list, array.array]:
                # convert list to ctypes.c_double_Array
                dataType = ctypes.c_double * Count
                values = dataType(0)
                for i in range(Count):
                    values[i] = Values[i]
            else:  # ctypes.c_double_Array
                values = Values
            self.dll.SetArray_Double(ValueID, values, Startindex, Count, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)

    def GetArray_Bool(self, ValueID, Startindex, Count):
        '''GetArray_Bool returns the array values of a simulink model parameter or signal, from a model runnning on an ADwin system as uint8.'''
        dataType = ctypes.c_uint8 * Count
        values = dataType(0)
        self.dll.GetArray_Bool(ValueID, values, Startindex, Count, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)
        if self.useNumpyArrays:
            return np.array(values, dtype=np.bool8)
        else:
            return [bool(element) for element in values]

    def SetArray_Bool(self, ValueID, Values, Startindex, Count):
        '''SetArray_Bool transfers uint8 data from the PC into a DATA array of the ADwin system.'''
        if _isNumpyAvailable:
            data = np.array(Values, dtype=np.uint8)
            ptr = data.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8))
            self.dll.SetArray_UInt8(ValueID, ptr, Startindex, Count, self.__errPointer)
        else:
            if type(Values) in [list, array.array]:
                # convert list to ctypes.c_uint8_Array
                dataType = ctypes.c_uint8 * Count
                values = dataType(0)
                for i in range(Count):
                    values[i] = Values[i]
            else:  # ctypes-array
                values = Values
            self.dll.SetArray_UInt8(ValueID, values, Startindex, Count, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)

    # ArrayElement
    def GetArrayElement_Int32(self, ValueID, Index):
        '''GetArrayElement_Int32  returns the array element value of a simulink model parameter or signal,
        from a model runnning on an ADwin system as int32.'''
        self.dll.GetArrayElement_Long.restype = ctypes.c_int32  # default
        ret = self.dll.GetArrayElement_Long(ValueID, Index, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)
        return ret

    def SetArrayElement_Int32(self, ValueID, Value, Index):
        '''SetArrayElement_Int32 sets the value of a simulink model parameter or signal, from a model runnning on an ADwin system as int32.'''
        self.dll.SetArrayElement_Long(ValueID, Value, Index, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)

    def GetArrayElement_Single(self, ValueID, Index):
        '''GetArray_Single returns the array element value of a simulink model parameter or signal,
        from a model runnning on an ADwin system as single.'''
        self.dll.GetArrayElement_Float.restype = ctypes.c_float
        ret = self.dll.GetArrayElement_Float(ValueID, Index, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)
        return ret

    def SetArrayElement_Single(self, ValueID, Value, Index):
        '''SetArrayElement_Single sets the value of a simulink model parameter or signal, from a model runnning on an ADwin system as single.'''
        _val = ctypes.c_float(Value)
        self.dll.SetArrayElement_Float(ValueID, _val, Index, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)

    def GetArrayElement_Double(self, ValueID, Index):
        '''GetArray_Double returns the array element value of a simulink model parameter or signal,
        from a model runnning on an ADwin system as double.'''
        self.dll.GetArrayElement_Double.restype = ctypes.c_double
        ret = self.dll.GetArrayElement_Double(ValueID, Index, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)
        return ret

    def SetArrayElement_Double(self, ValueID, Value, Index):
        '''SetArrayElement_Double sets the value of a simulink model parameter or signal, from a model runnning on an ADwin system as double.'''
        _val = ctypes.c_double(Value)
        self.dll.SetArrayElement_Double(ValueID, _val, Index, self.__errPointer)
        self.__checkError(inspect.currentframe().f_code.co_name)

    #  Control and error handling
    def ADsim_Get_Last_Error_Text(self, Last_Error):
        '''ADsim_Get_Last_Error_Text returns an error text related to an error number.'''
        text = ctypes.create_string_buffer(256)
        pText = ctypes.byref(text)
        if sys.platform == 'win32':
            self.dll.Get_Last_Error_Text(Last_Error, pText, 256)
        else:
            self.dll.ADsim_Get_Last_Error_Text(Last_Error, pText, 256)
        return text.value

    def ADsim_Get_Last_Error(self):
        '''ADsim_Get_Last_Error returns the number of the last error.'''
        if sys.platform == 'win32':
            self.dll.Get_Last_Error()
        else:
            self.dll.ADsim_Get_Last_Error()
        return self.__err.value
