# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 14:04:22 2021

@author: Darshan Rathod
"""

import numpy as _np
import pandas as _pd
import datetime as _dtm
import os as _os

from .base import davis_set as _ds
from .utils import *
from . import shared as _shared

class velocity_set(_ds):
    '''
    velocity_set object which provides functionalities to work with velocity and image set of a perticular case.
    Images can only be accessed if the .set file of velocity is within the subdirectories of recording folder.
    '''
    
    def __init__(self,filepath,load=True,rec_path=None,load_rec=False):
        '''

        Parameters
        ----------
        filepath : string or os.path object
            path to .set file or folder
        load :bool, optional, default = True
            whether to load the file. lvreader by default does not load the buffer into the memory. If this is True then buffer is loaded into the memory.
        rec_path : string or os.path object, optional, default= None
            path to .set file of recording folder. If this is supplied then recording image can directly be loaded by calling image method.
        load_rec : BOOL, optional, default= False
            whether to load the recording set or not. MAke it True when the parent folders of .set file contains the recording set, if not then the error will arise.

        Returns
        -------
        velocity_set object

        '''
        super().__init__(filepath=filepath,load=load,rec_path=rec_path)
        if load_rec:
            self.recording_set = _ds(self.recording_foldpath)
    
    def __repr__(self):
        return f'velocity_set object'
    
    def __len__(self):
        return len(self.s)
    
    def __getitem__(self,i):
        return self.s[i]
        
    def image(self,n:int=0,frame:int=0):
        '''
        Returns the nth recorded image, and nth frame of the image. Generally there are 2 frames in PIV.

        Parameters
        ----------
        n : int, optional
            image number. The default is 0.
        frame : int, optional
            frame number of given image. The default is 0.

        Returns
        -------
        Image as numpy masked array.

        '''
        return self.recording_set[n][frame].as_masked_array()
    
    def image_masks(self,n:int=0,frame:int=0):
        '''
        Returns the mask of an Image.

        Parameters
        ----------
        n : int, optional
            image number. The default is 0.
        frame : int, optional
            frame number of given image. The default is 0.

        Returns
        -------
        Image mask as numpy masked array.

        '''
        
        return self.recording_set[n][frame].masks[0]
    
    def image_plot(self,n=0,frame=0,**kwargs):
        '''
        

        Parameters
        ----------
        n : int, optional
            image number. The default is 0.
        frame : int, optional
            frame number of given image. The default is 0.
        **kwargs : TYPE
            DESCRIPTION.

        Returns
        -------
        matplotlib.pyplot like
            plots the image

        '''
        return self.recording_set[n][frame].plot(**kwargs)
        
    
    def image_offsets(self,n=0,frame=0):
        return self.recording_set[n][frame].scales.x.offset ,self.recording_set[n][frame].scales.y.offset
    
    def image_slopes(self,n=0,frame=0):
        return self.recording_set[n][frame].scales.x.slope ,self.recording_set[n][frame].scales.y.slope
    
    def image_masks(self,n=0,frame=0):
        return self.recording_set[n][frame].masks[0]
    
    def limits(self,n=0,frame=0):
        xs,ys = self.image_slopes(n=n,frame=frame)
        xo,yo = self.image_offsets(n=n,frame=frame)
        lny,lnx = self.image().shape
        dict1 = {}
        dict1['xlim'] = [xo,xo + lnx*xs]
        dict1['ylim'] = [yo+lny*ys,yo]
        return dict1
    
    def image_coords(self,n=0,frame=0):
        '''
        Returns the meshgrid of X and Y coordinates of image.

        '''
        xs,ys = self.image_slopes(n=n,frame=frame)
        xo,yo = self.image_offsets(n=n,frame=frame)
        lny,lnx = self.image(n=0,frame=0).shape
        xc = _np.linspace(xo,xo+lnx*xs,lnx)
        yc = _np.linspace(yo,yo+lny*ys,lny)
        # xc,yc = rotate_coordinates_degrees(x=xc,y=yc,angle=angle)
        
        return _np.meshgrid(xc,yc)
    
    def vector_coords(self,n=0):
        '''
        Returns the meshgrid of X and Y coordinates of vectors
        '''
        xs,ys = self.vector_slopes(n=n)
        xo,yo = self.vector_offsets(n=n)
        lny,lnx = self.u(n=n).shape
        gx,gy = self.grid(n=n)
        xc = _np.linspace(xo,xo+lnx*gx*xs,lnx)
        yc = _np.linspace(yo,yo+lny*gy*ys,lny)
        xc,yc=_np.meshgrid(xc,yc)
        # xc,yc = rotate_coordinates_degrees(x=xc,y=yc,angle=angle)
        return xc,yc
    
    def vector_linspace(self,n=0):
        xs,ys = self.vector_slopes(n=n)
        xo,yo = self.vector_offsets(n=n)
        lny,lnx = self.u(n=n).shape
        gx,gy = self.grid(n=n)
        xc = _np.linspace(xo,xo+lnx*gx*xs,lnx)
        yc = _np.linspace(yo,yo+lny*gy*ys,lny)
        return xc,yc[::-1]
    
    
    def x(self,n=0):
        x,y = self.vector_coords(n=n)
        x = _np.ma.masked_array(x,mask=self.vector_masks(n=n),fill_value=0,dtype='float64')
        return x
    
    def y(self,n=0):
        x,y = self.vector_coords(n=n)
        y = _np.ma.masked_array(y,mask=self.vector_masks(n=n),fill_value=0,dtype='float64')
        return y
    
    
    
    def vector_offsets(self,n=0):
        return self.s[n][0].scales.x.offset ,self.s[n][0].scales.y.offset
    
    def vector_slopes(self,n=0):
        return self.s[n][0].scales.x.slope ,self.s[n][0].scales.y.slope
    
    def vector_masks(self,n=0):
        # return (self.s[n][0].masks[0] == 0).astype('int')
        return self.s[n][0].masks[0] == 0
    
    
    
    
    def get_keys_list(self,n=0):
        return list(self.s[n][0][0].keys())
    
    def get_component(self,key,n=0):
        return self.s[n][0].components[key]
    
    def get_arr(self,n=0,key='U0'):
        '''
        Get the array of required scalar.
        ex. key = 'U0' gives the Vx component. key = 'TKE' gives the turbulent kinetic energy if it is computed in the .set file.
        '''
        # arr1 = self.s[n][0][0][key]
        # arr1 = _np.ma.masked_array(arr1,mask=self.vector_masks(n=n),fill_value=0,dtype='float64')
        
        comp1 = self.get_component(key=key,n=n)
        arr1 = comp1[0]
        arr1 = _np.ma.masked_array(arr1,mask=self.vector_masks(n=n),fill_value=0,dtype='float64')
        arr1 = comp1.scale.offset + arr1 * comp1.scale.slope
        return arr1
    
    def u(self,n=0):
        # return self.s[n][0].as_masked_array()['u']
        # return self.s[n][0].scales.i.offset + self.get_arr(n=n,key='U0') * self.s[n][0].scales.i.slope
        return self.get_arr(n=n,key='U0')
    
    def v(self,n=0):
        # return self.s[n][0].as_masked_array()['v']
        # return self.s[n][0].scales.i.offset + self.get_arr(n=n,key='V0') * self.s[n][0].scales.i.slope
        return self.get_arr(n=n,key='V0') * -1
    
    
    def u_proj(self,n=0,angle=0):
        u,v = self.u(n=n),self.v(n=n)
        u,v = rotate_coordinates_degrees(x=u,y=v,angle=angle)
        u = _np.ma.masked_array(u,mask=self.vector_masks(n=n),fill_value=0,dtype='float64')
        return u
    
    def v_proj(self,n=0,angle=0):
        u,v = self.u(n=n),self.v(n=n)
        u,v = rotate_coordinates_degrees(x=u,y=v,angle=angle)
        v = _np.ma.masked_array(v,mask=self.vector_masks(n=n),fill_value=0,dtype='float64')
        return v
    
    
    def TKE(self,n=0):
        # return self.s[n][0].components['TS:Turbulent kinetic energy'][0]
        return self.get_arr(n=n,key='TS:Turbulent kinetic energy')
    
    def velocity_magnitude(self,n=0):
        return  _np.sqrt(self.u(n=n)**2 + self.v(n=n)**2)
    
    
    def omega_z(self,n=0):
        x,y = self.vector_coords(n=n)
        u = self.get_arr(n=n,key='U0')
        v = self.get_arr(n=n,key='V0') * -1
        
        # dvy = _np.diff(v,axis=1,append=0)
        # dvy = _np.diff(v,axis=1,prepend=0)
        # dx = _np.diff(x,axis=1)[0,0]
        
        # # dvx = _np.diff(u,axis=0,append=0)
        # dvx = _np.diff(u,axis=0,prepend=0)
        # dy = _np.diff(y,axis=0)[0,0]
        
        # wz = (dvy/dx - dvx/dy) * 1000
        # wz= _np.ma.masked_array(wz,mask=self.vector_masks(n=n),fill_value=0,dtype='float64')
        
        dx = _np.diff(x,axis=1)[0,0]
        dy = _np.diff(y,axis=0)[0,0]
        wz = (_np.gradient(v,dx,axis=1) - _np.gradient(u,dy,axis=0))*1000
        
        return wz
    
    
    
    
    def plot(self,n=0):
        return self.s[n][0].plot()
    
    def grid(self,n=0):
        return self.s[n][0].grid.x , self.s[n][0].grid.y
    
   
    def make_contour_data(self,n=0,z='u',unit=False):
        '''
        Parameters
        ----------
        n = frame number
        z : TYPE, string
            DESCRIPTION. value for plotting. either from 'u,v,velocity_magnitude'
        unit: Type, Bool
            Description. if unit for z in output data is required. default False

        Returns
        -------
        dictionary of 'x,y,z,unit'

        '''
        data = {}
        data['x'],data['y'] = self.vector_coords(n=n)
        
        if (z == 'u') or (z == 'U0'):
            data['z'] = self.u(n=n)
            z = 'U0'
        elif (z == 'v') or (z == 'V0'):
            data['z'] = self.v(n=n)
            z = 'V0'            
        elif z == 'velocity_magnitude':
            data['z'] = _np.sqrt(self.u(n=n)**2 + self.v(n=n)**2)
            z = 'U0'
        elif z == 'TKE':
            data['z'] = self.TKE(n=n)
        elif (z.upper() =='WZ') or (z.upper() == 'OMEGA_Z'):
            data['z'] = self.omega_z(n=n)
        else:
            data['z'] = self.get_arr(n=n,key=z)
            
        if unit:
            if (z.upper() =='WZ') or (z.upper() == 'OMEGA_Z'):
                data['unit'] = '1/s'
            else:
                data['unit'] = self.get_component(key=z,n=n).scale.unit
            
        return data
    
    def make_data(self,n=0):
        data = {}
        data['x'],data['y'] = self.vector_coords(n=n)
        data['u'],data['v'] = self.u(n=n),self.v(n=n)
        return data
    
    
    def make_image_data(self,n=0,frame=0):
        
        data = {}
        data['x'],data['y'] = self.image_coords(n=n,frame=frame)
        data['z'] = self.image(n=n,frame=frame)
        
        return data
    
    def make_streamline_data(self,n=0):
        data = {}
        
        data['u'],data['v'] = self.u(n=n),self.v(n=n)
        data['x'],data['y'] = self.vector_linspace(n=n)
        return data
    

def save_set(vel_set,set_name,set_foldpath,n_start=0,n_end=-1,print_info=True):
    ls1 = local_set(set_name,set_foldpath,make_folder=True)
    ls1.save_case(case=vel_set,n_start=n_start,n_end=n_end,print_info=print_info)

    
class local_set:
    
    def __init__(self,set_name,set_foldpath,make_folder = False):
        '''
        class to access locally saved data. The class provides major functionalities as elocity_set, mainly make_data() function.
        

        Parameters
        ----------
        set_name : str
            name of the velocity_set.
        set_path : str or path type
            path of the velocity_set folder
        make_folder : BOOL, optional
            whether to make folder or not. If class is used to save the data then this attribute should be True. The default is False.

        Returns
        -------
        None.

        '''
        foldpath = _os.path.join(set_foldpath,set_name)
        self.xfp = _os.path.join(foldpath,'x.npy')
        self.yfp = _os.path.join(foldpath,'y.npy')
        self.maskfp = _os.path.join(foldpath,'mask.npy')
        self.Ufp = _os.path.join(foldpath,'Us')
        self.Vfp = _os.path.join(foldpath,'Vs')
        
        self.SVDfp = _os.path.join(foldpath,'SVD')
        self.uv1fp = _os.path.join(foldpath,'uv1.npy')
        self.Usfp = _os.path.join(foldpath,'Us.npy')
        self.Vsfp = _os.path.join(foldpath,'Vs.npy')
        
        if make_folder:
            make_dir(foldpath)
            make_dir(self.Ufp)
            make_dir(self.Vfp)
            # make_dir(self.SVDfp)
            self.req_loaded = False
        else:
            self.load_reqs()
    
    
    @classmethod
    def from_foldpath(cls,foldpath,*args,**kwargs):
        set_name = _os.path.basename(foldpath)
        set_foldpath = _os.path.dirname(foldpath)
        return cls(set_name,set_foldpath,*args,**kwargs)
    
    
    
    def __repr__(self):
        return f'local_set object'
    
    def __len__(self):
        return len(get_file_name(self.Ufp))
    
    def __getitem__(self,i):
        return self.make_data(i)
    
    
    def save_coords(self,data):
        _np.save(file=self.xfp,arr=data['x'])
        _np.save(file=self.yfp,arr=data['y'])
    
    def save_mask(self,data):
        _np.save(file=self.maskfp,arr=data['u'].mask)
        
    
    def load_reqs(self):
        self.x = _np.load(self.xfp)
        self.y = _np.load(self.yfp)
        self.mask = _np.load(self.maskfp)
        self.req_loaded = True
        
    def u(self,n=0):
        fname = str(n) + '.npy'
        return _np.ma.masked_array(_np.load(_os.path.join(self.Ufp,fname)),
                                   mask=self.mask,
                                   fill_value=0,dtype='float64')
    
    def v(self,n=0):
        fname = str(n) + '.npy'
        return _np.ma.masked_array(_np.load(_os.path.join(self.Vfp,fname)),
                                   mask=self.mask,
                                   fill_value=0,dtype='float64')
    
    
    def load_uv1(self):
        return _np.load(self.uv1fp)
    
    def save_uv1(self,data):
        return _np.save(file=self.uv1fp, arr=data)
    
    
    def save_SVD(self,U,eps,V_T):
        _np.save(file = _os.path.join(self.SVDfp,'U.npy'),
                 arr=U)
        _np.save(file = _os.path.join(self.SVDfp,'eps.npy'),
                 arr=eps)
        _np.save(file = _os.path.join(self.SVDfp,'V_T.npy'),
                 arr=V_T)
        
    def load_SVD(self):
        U = _np.load(file = _os.path.join(self.SVDfp,'U.npy'))
        eps = _np.load(file = _os.path.join(self.SVDfp,'eps.npy'))
        V_T = _np.load(file = _os.path.join(self.SVDfp,'V_T.npy'))
        return U,eps,V_T
        
    def save_uv(self,data,n=-1):
        if  n == -1:
            fname = '_1.npy'
        else:
            fname = str(n) + '.npy'
        _np.save(file = _os.path.join(self.Ufp,fname),
                 arr=data['u'].data)
        _np.save(file = _os.path.join(self.Vfp,fname),
                 arr=data['v'].data)
    
    def save_case(self,case,n_start=0,n_end=-1,print_info=True):
        d1 = case.make_data(n=n_start)
        self.save_coords(d1)
        self.save_mask(d1)
        if n_end == -1:
            n_end = len(case)
        if print_info:
            print(f'saving velocities')
        for i in range(n_start, n_end):
            if print_info:
                print(i)
            d1 = case.make_data(n=i)
            self.save_uv(d1,n=i)
        return
    
    def make_data(self,n=0):
        data = {}
        if not self.req_loaded:
            self.load_reqs()
        data['x'],data['y'] = self.x, self.y
        data['u'],data['v'] = self.u(n=n),self.v(n=n)
        return data
    
    def make_streamline_data(self,n=0):
        data = self.make_data(n=n)
        data['x'],data['y'] = meshgrid_to_linspace(data['x'],data['y'])
        return data
    
    def get_multiple_u(self,n_start=0,n_end=-1):
        if n_end == -1:
            n_end = len(self)
        n = n_start
        fname = str(n) + '.npy'
        u1 = _np.load(_os.path.join(self.Ufp,fname))
        for n in range(n_start+1,n_end):
            fname = str(n) + '.npy'
            utemp = _np.load(_os.path.join(self.Ufp,fname))
            u1 = _np.dstack((u1,utemp))
        return u1
    
    def get_multiple_v(self,n_start=0,n_end=-1):
        if n_end == -1:
            n_end = len(self)
        n = n_start
        fname = str(n) + '.npy'
        u1 = _np.load(_os.path.join(self.Vfp,fname))
        for n in range(n_start+1,n_end):
            fname = str(n) + '.npy'
            utemp = _np.load(_os.path.join(self.Vfp,fname))
            u1 = _np.dstack((u1,utemp))
        return u1
    
    def save_UVs(self,n_start=0,n_end=-1):
        u1 = self.get_multiple_u(n_start=n_start,n_end=n_end)
        _np.save(file = self.Usfp,
                 arr=u1)
        
        u1 = self.get_multiple_v(n_start=n_start,n_end=n_end)
        _np.save(file = self.Vsfp,
                 arr=u1)
    
    @property
    def Us(self):
        return _np.load(file = self.Usfp)
    
    @property
    def Vs(self):
        return _np.load(file = self.Vsfp)

    
