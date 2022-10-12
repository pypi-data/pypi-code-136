# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 14:04:37 2021

@author: Darshan Rathod
"""


import matplotlib as _mpl
import matplotlib.pyplot as _plt
import numpy as _np
import pandas as _pd
import os as _os

from . import shared as _shared


def make_dir(path1):
    try:
        _os.mkdir(path1)
    except FileExistsError as e:
        pass


def get_dir_path(fname):
    return [_os.path.join(fname,x) for x in _os.listdir(fname) if _os.path.isdir(_os.path.join(fname,x))]

def get_file_path(fname):
    return [_os.path.join(fname,x) for x in _os.listdir(fname) if _os.path.isfile(_os.path.join(fname,x))]

def get_dir_name(fname):
    return [x for x in _os.listdir(fname) if _os.path.isdir(_os.path.join(fname,x))]

def get_file_name(fname):
    return [x for x in _os.listdir(fname) if _os.path.isfile(_os.path.join(fname,x))]



def move_origin(d1,xnew=0, ynew=0):
    d1['x'] = d1['x'] - xnew
    d1['y'] = d1['y'] - ynew
    return d1

def rotate_coordinates_degrees(x,y,angle=0):
    xy1 = _np.array([x.flatten(),y.flatten()])
    cos1 = _np.cos(angle*_np.pi/180)
    sin1 = _np.sin(angle*_np.pi/180)
    Rv = _np.array([[cos1,-sin1],[sin1,cos1]])
    xy1 = _np.matmul(Rv,xy1)
    x = xy1[0,:].reshape(x.shape)
    y = xy1[1,:].reshape(y.shape)
    return x,y

def rotate_bases(d1,angle=0):
    '''Rotates the coordinate bases

    Parameters
    ----------
    d1 : TYPE
        DESCRIPTION.
    angle : TYPE, optional
        DESCRIPTION. The default is 0.

    Returns
    -------
    d1 : TYPE
        DESCRIPTION.

    '''
    
    mask1 = d1['u'].mask
    uv = _np.array([d1['u'].data.flatten(),d1['v'].data.flatten()])
    theta1 = angle * _np.pi/180
    A = _np.array([[_np.cos(theta1),_np.sin(theta1)],[-_np.sin(theta1),_np.cos(theta1)]]).T
    Ainv = _np.linalg.inv(A)
    uv1 = _np.matmul(Ainv,uv)
    d1['u'] = uv1[0,:].reshape(d1['u'].shape)
    d1['u'] = _np.ma.masked_array(d1['u'],mask=mask1,fill_value=0,dtype='float64')
    d1['v'] = uv1[1,:].reshape(d1['v'].shape)
    d1['v'] = _np.ma.masked_array(d1['v'],mask=mask1,fill_value=0,dtype='float64')
    return d1

def get_data_at_point(data,px=0,py=0,dx=None,dy=None):
    '''
    calculates the data['z'] at (px,py) point in the domain. Data is interpolated using distance weighted average from its neighbouring points.

    Parameters
    ----------
    data : dict
        s1.make_data() type of data. It has x,y,z values. x,y are coordinates meshgrid. and z is the scalar of interest in the domain.
    px : float, optional
        X coordinate. The default is 0.
    py : float, optional
        Y coordinate. The default is 0.
    dx : float, optional
        delta x in the data['x']. This value is utilized to filter out the neighbours. The code looks at px +/- dx coordinates for all the points.
        then from obtained coordinates, it calculates the weighted average. The default is None. If None then code calculated dx from itself.
    dy : float, optional
        delta y in the data['y']. The default is None.

    Returns
    -------
    pz : float
        weighted average of data['z'].

    '''
    if dx is None:
        dx = _np.diff(_np.unique(data['x']))[0]
    if dy is None:
        dy = _np.diff(_np.unique(data['y']))[0]
        
    f1 = data['x'] >= (px - dx)
    f1 = f1 & (data['x'] <= (px + dx))
    f1 = f1 & (data['y'] >= (py - dy))
    f1 = f1 & (data['y'] <= (py + dy))
    
    px1 = data['x'][f1]
    py1 = data['y'][f1]
    pz1 = data['z'].data[f1]
    
    ws = ((px1 - px)**2 + (py1 - py)**2)**0.5
    pz = (ws*pz1).sum()/ws.sum()
    return pz

def make_line(x1:float,y1:float,x2:float,y2:float,n_points:int=100):
    '''
    generates coordinates (=n_points) over the line passing from (x1,y1) and (x2,y2)

    Parameters
    ----------
    x1 : float
        x - coordinate
    y1 : float
        y - coordinate
    x2 : float
        x - coordinate
    y2 : float
        y - coordinate
    n_points : int, optional
        number of points between (x1,y1) and (x2,y2). The default is 100.

    Returns
    -------
    x : numpy_array like
        x-coordinates
    y : numpy_array like
        y-coordinates

    '''
    # if the ilne is verticle then "division by zero" error will come
    if x2 == x1:
        x = _np.zeros(n_points) + x2
        y = _np.linspace(y1,y2,n_points)
    else:
        m = (y2-y1) / (x2-x1)
        c = y2 - m*x2
        x = _np.linspace(x1,x2,n_points)
        y = m*x + c
    return x,y


def get_data_at_line(data,x1,y1,x2,y2,n_points=100,dx=None,dy=None):
    '''
    generates coordinates (=n_points) over the line passing from (x1,y1) and (x2,y2) and calculates the interpolated data['z'] over the line.
    
    The code utilizes the function make_line() to get line coordinates, and get_data_at_point() function to get data at individual point over the line.
    Hence the detail explanation of all the arguments of this function can be obtained from the above two functions.

    Parameters
    ----------
    x1 : float
        x - coordinate
    y1 : float
        y - coordinate
    x2 : float
        x - coordinate
    y2 : float
        y - coordinate
    n_points : int, optional
        number of points between (x1,y1) and (x2,y2). The default is 100.
    dx : float, optional
        delta x in the data['x']. This value is utilized to filter out the neighbours. The code looks at px +/- dx coordinates for all the points.
        then from obtained coordinates, it calculates the weighted average. The default is None. If None then code calculated dx from itself.
    dy : float, optional
        delta y in the data['y']. The default is None.    

    Returns
    -------
    x : numpy_array like
        x-coordinates
    y : numpy_array like
        y-coordinates
    z : numpy_array like
        data['z'] values over x and y

    '''
    x,y = make_line(x1,y1,x2,y2,n_points=n_points)
    z = _np.zeros(x.shape)
    i = 0
    for xp,yp in zip(x,y):
        z[i] = get_data_at_point(data,px=xp,py=yp,dx=dx,dy=dy)
        i += 1
    return x,y,z



def imshow(img,*args,**kwargs):
    _plt.imshow(img,*args,**kwargs)
    _plt.xticks([])
    _plt.yticks([])

def meshgrid_to_linspace(x,y):
    '''
    converts x and y meshgrid to numpy.linspace type array

    Parameters
    ----------
    x : 2-D numpy array
    y : 2-D numpy array

    Returns
    -------
    x1 : 1-D numpy array
    y1 : 1-D numpy array

    '''
    x1 = _np.linspace(x.min(),x.max(),x.shape[1])
    y1 = _np.linspace(y.min(),y.max(),y.shape[0])
    return x1,y1













