# -*- coding: utf-8 -*-

import ctypes
from muswmm.lib import *
import datetime
import os

class Simulator:

    # SWMM OBJECT
    SWMM_GAGE = 0
    SWMM_SUBCATCH = 1
    SWMM_NODE = 2
    SWMM_LINK = 3
    SWMM_SYSTEM = 100

    # SWMM NODE TYPE
    SWMM_JUNCTION = 0
    SWMM_OUTFALL = 1
    SWMM_STORAGE = 2
    SWMM_DIVIDER = 3

    # SWMM LINK TYPE
    SWMM_CONDUIT = 0
    SWMM_PUMP = 1
    SWMM_ORIFICE = 2
    SWMM_WEIR = 3
    SWMM_OUTLET = 4

    # GAGE PROPERTY
    SWMM_GAGE_RAINFALL = 100

    # SUBCATCH PROPERTY
    SWMM_SUBCATCH_AREA = 200
    SWMM_SUBCATCH_RAINGAGE = 201
    SWMM_SUBCATCH_RAINFALL = 202
    SWMM_SUBCATCH_EVAP = 203
    SWMM_SUBCATCH_INFIL = 204
    SWMM_SUBCATCH_RUNOFF = 205
    SWMM_SUBCATCH_RPTFLAG = 206

    # NODE PROPERTY
    SWMM_NODE_TYPE = 300
    SWMM_NODE_ELEV = 301
    SWMM_NODE_MAXDEPTH = 302
    SWMM_NODE_DEPTH = 303
    SWMM_NODE_HEAD = 304
    SWMM_NODE_VOLUME = 305
    SWMM_NODE_LATFLOW = 306
    SWMM_NODE_INFLOW = 307
    SWMM_NODE_OVERFLOW = 308
    SWMM_NODE_RPTFLAG = 309
    
    # LINK PROPERTY
    SWMM_LINK_TYPE = 400
    SWMM_LINK_NODE1 = 401
    SWMM_LINK_NODE2 = 402
    SWMM_LINK_LENGTH = 403
    SWMM_LINK_SLOPE = 404
    SWMM_LINK_FULLDEPTH = 405
    SWMM_LINK_FULLFLOW = 406
    SWMM_LINK_SETTING = 407
    SWMM_LINK_TIMEOPEN = 408
    SWMM_LINK_TIMECLOSED = 409
    SWMM_LINK_FLOW = 410
    SWMM_LINK_DEPTH = 411
    SWMM_LINK_VELOCITY = 412
    SWMM_LINK_TOPWIDTH = 413
    SWMM_LINK_RPTFLAG = 414

    # SYSTEM PROPERTY
    SWMM_STARTDATE = 0
    SWMM_CURRENTDATE = 1
    SWMM_ELAPSEDTIME = 2
    SWMM_ROUTESTEP = 3
    SWMM_MAXROUTESTEP = 4
    SWMM_REPORTSTEP = 5
    SWMM_TOTALSTEPS = 6
    SWMM_NOREPORT = 7
    SWMM_FLOWUNITS = 8

    def __init__(self, inp, rpt = None, out = None):
        self._swmm = SWMM_ENGINE
        self._inp = inp
        if rpt == None:
            rpt = os.path.dirname(inp) + '\\' + self.__path_getFileName(inp) + '.rpt'
        if out == None:
            out = os.path.dirname(inp) + '\\' + self.__path_getFileName(inp) + '.out'
        self._rpt = rpt
        self._out = out
        
    def __path_getFileName(self, file_name, with_suffix = False):
        if with_suffix:
            return os.path.split(file_name)[-1]
        else:
            return os.path.split(file_name)[-1].split('.')[0]
        
    def run(self):
        return self._swmm.swmm_run(self._inp.encode('utf-8'),
                                   self._rpt.encode('utf-8'),
                                   self._out.encode('utf-8'))
    
    def open(self):
        return self._swmm.swmm_open(self._inp.encode('utf-8'),
                                   self._rpt.encode('utf-8'),
                                   self._out.encode('utf-8'))
    
    def start(self, saveFlag):
        return self._swmm.swmm_start(ctypes.c_int(saveFlag))
    
    def step(self):
        if not hasattr(self, 'cur_date_time'):
            self.cur_date_time = 0.0
        elapsed_time = ctypes.c_double()
        err_code = self._swmm.swmm_step(ctypes.byref(elapsed_time))
        self.cur_date_time = elapsed_time.value
        return err_code, elapsed_time.value    
    
    def stride(self, strideStep):
        if not hasattr(self, 'cur_date_time'):
            self.cur_date_time = 0.0
        elapsed_time = ctypes.c_double()
        err_code = self._swmm.swmm_stride(ctypes.c_int(strideStep), ctypes.byref(elapsed_time))
        self.cur_date_time = elapsed_time.value
        return err_code, elapsed_time.value

    def report(self):
        return self._swmm.swmm_report()
    
    def end(self):
        return self._swmm.swmm_end()
    
    def getMassBalErr(self):
        runoffErr = ctypes.c_float()
        flowErr = ctypes.c_float()
        qualErr = ctypes.c_float()
        err_code = self._swmm.swmm_getMassBalErr(ctypes.byref(runoffErr),
                                                     ctypes.byref(flowErr), 
                                                     ctypes.byref(qualErr))
        return err_code, runoffErr.value, flowErr.value, qualErr.value

    def getVersion(self):
        return self._swmm.swmm_getVersion()

    def getError(self, msgLen):
        err_msg = ctypes.create_string_buffer(1025)
        err_code = self._swmm.swmm_getError(err_msg, ctypes.c_int(msgLen))
        return err_code, bytes.decode(err_msg.value)

    def getWarnings(self):
        return self._swmm.swmm_getWarnings()
    
    def close(self):
        return self._swmm.swmm_close()
    
    def getDateTime(self):
        start_date_time = ctypes.c_double()
        end_date_time = ctypes.c_double()
        err_code = self._swmm.swmm_getStartAndEndTime(ctypes.byref(start_date_time),
                                                         ctypes.byref(end_date_time))
        return err_code, self.__time_fromReal(start_date_time.value), self.__time_fromReal(end_date_time.value)
        
    def getCurrentTime(self):
        if not hasattr(self, 'cur_date_time'):
            self.cur_date_time = 0.0
        return self.getDateTime()[1] + datetime.timedelta(self.cur_date_time)
    
    # 数值型时间转日期型时间
    # private
    def __time_fromReal(self, time):
        return datetime.datetime.strptime('1899-12-30','%Y-%m-%d') + datetime.timedelta(time)

    def getCount(self, objType):
        return self._swmm.swmm_getCount(ctypes.c_int(objType))

    def getName(self, objType, index):
        name = ctypes.create_string_buffer(256)
        self._swmm.swmm_getName(ctypes.c_int(objType),
                                ctypes.c_int(index),
                                name,
                                ctypes.c_int(256))
        return bytes.decode(name.value)

    def getIndex(self, objType, name):
        obj_name = ctypes.c_char_p(str.encode(name))
        return self._swmm.swmm_getIndex(ctypes.c_int(objType),
                                        obj_name)

    def getValue(self, property, index):
        self._swmm.swmm_getValue.restype = ctypes.c_double
        value = self._swmm.swmm_getValue(ctypes.c_int(property),
                                        ctypes.c_int(index))
        
        return value
    
    def setValue(self, property, index, value):
        self._swmm.swmm_setValue(ctypes.c_int(property),
                                 ctypes.c_int(index),
                                 ctypes.c_double(value))
    
    # 仅在end和close之间调用
    def getSavedValue(self, property, index, period):
        self._swmm.swmm_getSavedValue.restype = ctypes.c_double
        value = self._swmm.swmm_getSavedValue(ctypes.c_int(property),
                                              ctypes.c_int(index),
                                              ctypes.c_int(period))
        return value