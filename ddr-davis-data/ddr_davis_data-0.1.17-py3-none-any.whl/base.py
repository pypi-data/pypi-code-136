# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 13:18:33 2021

@author: Darshan Rathod

This module defines davis_set object which gives basic functionalities to handle davis set files. Class calib_file extracts the calibration information of the davis set object.

"""

from lvreader import read_set as _rs
import os as _os
import pandas as _pd
import numpy as _np
import datetime as _dtm
import concurrent.futures as _conf
import xml.etree.ElementTree as _ET

from .utils import *


def analyze_set(foldpath,load=True,rec_path=None):
    s1 = davis_set(foldpath,load=load,rec_path=rec_path)
    ans1 = {'recording':False,'image':False,'vector':False,'Avg_vector':False}
    ans1[s1.data_type] = True
    ans1['recording_foldpath'] = s1.recording_foldpath
    ans1['foldpath'] = s1.foldpath
    ans1['parent_fold_len'] = s1.parent_fold_len
    return _pd.DataFrame(ans1,index=[0])




class davis_set:
    '''
    Adds functionality to handle davis set file
    '''
    
    def __init__(self,filepath: str,load: bool = True, rec_path: str = None):
        '''

        Parameters
        ----------
        filepath : string or os.path object
            path to .set file or folder
        load :bool, optional, default = True
            whether to load the file. lvreader by default does not load the buffer into the memory. If this is True then buffer is loaded into the memory.
        rec_path : string or os.path object, optional, default= None
            path to .set file of recording folder. If this is supplied then recording image can directly be loaded by calling image method.

        Returns
        -------
        davis_set object

        '''
        self.filepath = filepath
        self.s = _rs(self.filepath)
        if load:
            self.buffer = self.s[0]
        self.rec_path = rec_path
    
    @property
    def is_closed(self):
        return self.s.closed
    
    def close(self):
        return self.s.close()
    
    def __repr__(self):
        return f'davis_set object'
    
    def __len__(self):
        return len(self.s)
    
    def __getitem__(self,i):
        return self.s[i]
    
    def __type__(self):
        return 'davis_set'
    
    @property
    def project_foldpath(self):
        return _os.path.dirname(self.recording_foldpath)
    
    @property
    def project_foldname(self):
        return _os.path.basename(self.project_foldpath)
    
    
    @property
    def recording_foldpath(self):
        '''
        Returns
        -------
        path of the recording folder
        '''
        if self.rec_path != None:
            return self.rec_path
        if self.data_type == 'recording':
            return self.foldpath
        else:
            s1 = davis_set(_os.path.dirname(self.foldpath))
            return s1.recording_foldpath
    
    @property
    def recording_foldname(self):
        return _os.path.basename(self.recording_foldpath)
    
    
    @property
    def name(self):
        return _os.path.basename(self.foldpath)
    
    @property
    def data_type(self):
        str1 = self.s.type_id
        if str1 == 'SET_TYPE_ID_RECORDING':
            return 'recording'
        elif str1 == 'SET_TYPE_ID_IMAGE':
            return 'image'
        elif str1 == 'SET_TYPE_ID_VECTOR':
            if 'Avg' in self.name:
                return 'Avg_vector'
            else:
                return 'vector'
    
    @property
    def attributes(self):
        return self.buffer.attributes
    
    
    @property
    def foldpath(self):
        return self.buffer.attributes['LoadSet'] 
    
    @property
    def dt(self):
        '''
        Returns
        -------
        dt in micro-seconds

        '''
        return self.buffer.attributes['DevDataTrace2'][0,0]
    
    @property
    def cam1_exposure(self):
        '''
        Returns
        -------
        Exposure time in micro-seconds
        '''
        return self.buffer.attributes['DevDataTrace0'][0,0]
    
    @property
    def ref_time(self):
        '''
        Returns
        -------
        reference time in mili-seconds
        '''
        return self.buffer.attributes['DevDataTrace1'][0,0]
    
    @property
    def laser_powers(self):
        '''
        Returns
        -------
        laser power in % for laser A and B respectively
        '''
        return self.buffer.attributes['DevDataTrace3'][0,0] , self.buffer.attributes['DevDataTrace4'][0,0]
    
    @property
    def trigger_rate(self):
        '''
        Returns
        -------
        triggering frequency in Hz
        '''
        return self.buffer.attributes['DevDataTrace5'][0,0]
    
    @property
    def recording_rate(self):
        '''
        Returns
        -------
        recording frequency in Hz
        '''
        return self.buffer.attributes['DevDataTrace6'][0,0]
    
    @property
    def time0(self):
        '''
        Returns
        -------
        starting time as datetime.datetime object
        '''
        
        dt1 = [int(x) for x in self.buffer.attributes['_Date'].split('.')]
        lt1 = self.buffer.attributes['_Time'].split('.')
        us1 = int(lt1[1])*1000
        t1 = [int(x) for x in lt1[0].split(':')]
        return _dtm.datetime(dt1[2]+2000,dt1[1],dt1[0],t1[0],t1[1],t1[2],us1)
    
    @property
    def parent_fold_len(self):
        if self.data_type != 'recording':
            fp = _os.path.dirname(self.foldpath)
            s1 = davis_set(fp)
            return len(s1)
        else:
            return len(self.s)

    
    def get_analysis_list(self):
        ls1 = [x[0] for x in _os.walk(self.foldpath)]
        if self.data_type == 'recording':
            rec_path = self.foldpath
        else:
            rec_path = self.rec_path
        ans1 = _pd.DataFrame()
        for f in ls1:
            ans1 = ans1.append(analyze_set(f,rec_path=rec_path),ignore_index=True)
        self.analysis_list = ans1
        return ans1
    
    
    @property
    def calibration_foldpath(self):
        return _os.path.join(_os.path.dirname(self.recording_foldpath),'Properties','Calibration')
    
    def load_calibration(self):
        fp1 = _os.path.join(self.calibration_foldpath,'Calibration.xml')
        self.calibration = calib_file(fp1)
        return self.calibration
    



class calib_file:
    
    def __init__(self,filepath):
        self.filepath = filepath
        self.tree = _ET.parse(filepath)
        self.root = self.tree.getroot()
        
    @property
    def foldpath(self):
        return _os.path.dirname(self.filepath)
    
    def get_image(self,n_camera=1):
        fp1 = _os.path.join(self.foldpath,'camera'+str(n_camera))
        s1 = davis_set(fp1)
        return s1[0][0].as_masked_array()
        
    
    def get_view(self,n_view=1):
        return self.root[n_view-1][0]
    
    def get_camera(self,n_camera=1,n_view=1):
        return self.get_view(n_view=n_view)[n_camera-1]
    
    
    def get_scales(self,n_camera=1,n_view=1):
        d1 = {}
        for i in self.get_camera(n_camera=n_camera,n_view=n_view)[0][4]:
            d1[i.tag] = i.attrib
        self.scales = _pd.DataFrame(d1)
        return self.scales
    
    def get_external_camera_parameters(self,n_camera=1,n_view=1):
        d1 = {}
        for i in self.get_camera(n_camera=n_camera,n_view=n_view)[0][3]:
            d1[i.tag] = i.attrib
        self.external_camera_parameters = d1
        return self.external_camera_parameters
    
    def get_internal_camera_parameters(self,n_camera=1,n_view=1):
        d1 = {}
        for i in self.get_camera(n_camera=n_camera,n_view=n_view)[0][2]:
            d1[i.tag] = i.attrib
        self.internal_camera_parameters = d1
        return self.internal_camera_parameters
    
    def get_common_parameters(self,n_camera=1,n_view=1):
        d1 = {}
        for i in self.get_camera(n_camera=n_camera,n_view=n_view)[0][0]:
            d1[i.tag] = i.attrib
        self.common_parameters = d1
        return self.common_parameters
    
    def get_rotation_angles(self,n_camera=1,n_view=1):
        return _pd.DataFrame(self.get_external_camera_parameters(n_camera=n_camera,n_view=n_view)['RotationAngles'],index=['Radians'],dtype='float')
    
    def get_translation_mm(self,n_camera=1,n_view=1):
        return _pd.DataFrame(self.get_external_camera_parameters(n_camera=n_camera,n_view=n_view)['TranslationMm'],index=[0],dtype='float')
        
    def get_focal_length(self,n_camera=1,n_view=1):
        return float(self.get_internal_camera_parameters(n_camera=n_camera,n_view=n_view)['FocalLengthMm']['Value'])
        
    def get_RMS_fit(self,n_camera=1,n_view=1):
        return float(self.get_common_parameters(n_camera=n_camera,n_view=n_view)['FitError']['RMS'])
    
    def get_pixcel_per_mm(self,n_camera=1,n_view=1):
        return float(self.get_common_parameters(n_camera=n_camera,n_view=n_view)['PixelPerMmFactor']['Value'])
    
    def get_calibration_plate_image(self,n_camera=1):
        fp1 = _os.path.dirname(self.filepath)
        fp1 = _os.path.join(fp1,'camera'+str(n_camera))
        self.calib_plate = _rs(fp1)[0][0].as_masked_array()
        return self.calib_plate
    
    
    @property
    def version(self):
        return self.root.attrib['Version']
    
    
class davis_project:
    
    def __init__(self,foldpath):
        self.foldpath = foldpath
    
    def __repr__(self):
        return f'davis_project object'
    
    def __len__(self):
        return len(self.all_sets)
    
    @property
    def name(self):
        return _os.path.basename(self.foldpath)
    
    @property
    def all_sets(self):
        ls1 = []
        for x in get_file_name(self.foldpath):
            if '.set' in x:
                if 'Properties' in x:
                    pass
                else:
                    ls1.append(x)
        # ls1.pop(ls1.index('Properties.set'))
        return ls1
    
    @property
    def all_sets_filepath(self):
        ls1 = []
        for x in self.all_sets:
            ls1.append(_os.path.join(self.foldpath,x))        
        return ls1
    
    @property
    def all_sets_foldpath(self):
        ls1 = []
        for x in get_dir_name(self.foldpath):
            if 'Properties' in x:
                pass
            else:
                ls1.append(_os.path.join(self.foldpath,x))        
        return ls1
    
    
    def get_analysis_list(self):
        def func1(fp):
            s1 = davis_set(fp)
            return s1.get_analysis_list()
        
        if len(self.all_sets) == 0:
            return
        
        ls1 = self.all_sets_foldpath
        ans1 = _pd.DataFrame()
        with _conf.ThreadPoolExecutor(max_workers=len(ls1)) as exe:
            for f in ls1:
                ans1 = ans1.append(exe.submit(func1,f).result(),ignore_index=True)
        self.analysis_list = ans1
        return ans1













    