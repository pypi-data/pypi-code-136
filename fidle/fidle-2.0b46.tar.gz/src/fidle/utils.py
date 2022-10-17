# ==================================================================
#            ______ _     _ _        __  __           _ 
#           |  ____(_)   | | |      |  \/  |         | |
#           | |__   _  __| | | ___  | \  / | ___   __| |
#           |  __| | |/ _` | |/ _ \ | |\/| |/ _ \ / _` |
#           | |    | | (_| | |  __/ | |  | | (_) | (_| |
#           |_|    |_|\__,_|_|\___| |_|  |_|\___/ \__,_|
#                                                        fidle.utils
# ==================================================================
# A simple module to host usefull functions for Fidle practical work
# Jean-Luc Parouty 2022

from genericpath import isdir
import os, sys
import string
import random
import numpy as np
from pathlib import Path
from glob import glob
import yaml


from collections.abc import Iterable
import datetime
from IPython.display import display,Image,Markdown,HTML

import fidle.config as config



__version__   = config.VERSION


# -------------------------------------------------------------
# Display md
# -------------------------------------------------------------

def subtitle(t):
    '''
    Display a markdown subtitle
    args:
        text to print
    return:
        none
    '''
    display(Markdown(f'<br>**{t}**'))
    

def display_md(text):
    '''
    Display a markdown text
    args:
        text to print
    return:
        none
    '''
    display(Markdown(text))


def display_html(text):
    '''
    Display a HTML text
    args:
        html to print
    return:
        none
    '''
    display(HTML(text))


def display_img(img):
    '''
    Display an image
    args:
        image to print
    return:
        none
    '''
    display(Image(img))


def np_print(*args, precision=3, linewidth=120):
    '''
    Print numpy vectors with a given precision
    args:
        *args : list of numpy vectors
        precision : print precision (3)
        linewidth : line width (120)
    return:
        nothing
    '''
    with np.printoptions(precision=precision, linewidth=linewidth):
        for a in args:
            print(a)


# -------------------------------------------------------------
# Format data
# -------------------------------------------------------------

def hdelay(delay):
    '''
    Returns a duration in human readable format, like 01:14:28 543ms
    delay can be timedelta or seconds
    args:
        delay : in seconds or as a timedelta
    reurns:
        strings
    '''
    if delay is None or isinstance(delay,str) : return
    if type(delay) is not datetime.timedelta:
        delay=datetime.timedelta(seconds=delay)
    sec = delay.total_seconds()
    hh = sec // 3600
    mm = (sec // 60) - (hh * 60)
    ss = sec - hh*3600 - mm*60
    ms = (sec - int(sec))*1000
    return f'{hh:02.0f}:{mm:02.0f}:{ss:02.0f} {ms:03.0f}ms'


def hsize(num, suffix='o'):
    '''
    Returns a size in human readable version, like 4.3G
    args:
        num: size in bytes
    return:
        String
    '''
    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            return f'{num:3.1f} {unit}{suffix}'
        num /= 1024.0
    return f'{num:.1f} Y{suffix}'



# -------------------------------------------------------------
# Folder cooking
# -------------------------------------------------------------


def mkdir(path):
    '''
    Create a subdirectory
    Mode is 0750, do nothing if exist
    args:
        path : directory to create
    return:
        none
    '''
    os.makedirs(path, mode=0o750, exist_ok=True)
    

def get_directory_size(path):
    """
    Return the directory size, but only 1 level
    args:
        path : directory path
    return:
        size in Mo
    """
    size=0
    for f in os.listdir(path):
        if os.path.isfile(path+'/'+f):
            size+=os.path.getsize(path+'/'+f)
    return size/(1024*1024)


# -------------------------------------------------------------
# Datasets cooking
# -------------------------------------------------------------


def shuffle_np_dataset(*data):
    """
    Shuffle a list of dataset
    args:
        *data : datasets
    return:
        *datasets mixed
    """
    print('Datasets have been shuffled.')
    p = np.random.permutation(len(data[0]))
    out = [ d[p] for d in data ]
    return out[0] if len(out)==1 else out


def rescale_dataset(*data, scale=1):
    '''
    Rescale numpy array with 'scale' factor
    args:
        *data : arrays
        scale : scale factor
    return:
        arrays of rescaled data
    '''
    print('Datasets have been resized with a factor ', scale)
    out = [ d[:int(scale*len(d))] for d in data ]
    return out[0] if len(out)==1 else out


def pick_dataset(*data,n=5):
    '''Return random subsets of n elements'''
    # ii = np.random.choice(range(len(data[0])), n)
    ii=np.random.choice( len(data[0]), n, replace=False)
    out = [ d[ii] for d in data ]
    return out[0] if len(out)==1 else out


# -------------------------------------------------------------
# Misc
# -------------------------------------------------------------


def update_progress(what,i,imax, redraw=False, verbosity=2, total_max=None):
    """
    Display a text progress bar, as :
    My progress bar : ############# 34%

    Args:
        what      : Progress bar name
        i         : Current progress
        imax      : Max value for i
        verbosity : progress bar verbosity (0: no bar, 1: progress bar, 2: one line)
        
    Returns:
        nothing
    """
    if verbosity==0:   return
    if verbosity==2 and i<imax: return
    if total_max is None : total_max = imax 
    bar_length = min(40,imax)
    if (i%int(imax/bar_length))!=0 and i<imax and not redraw:
        return
    progress  = float(i/imax)
    block     = int(round(bar_length * progress))
    endofline = '\r' if progress<1 else '\n'
    text = "{:16s} [{}] {:>5.1f}% of {}".format( what, "#"*block+"-"*(bar_length-block), progress*100, total_max)
    print(text, end=endofline)

    
def rmax(l):
    """
    Recursive max() for a given iterable of iterables
    Should be np.array of np.array or list of list, etc.
    args:
        l : Iterable of iterables
    return: 
        max value
    """
    maxi = float('-inf')
    for item in l:
        if isinstance(item, Iterable):
            t = rmax(item)
        else:
            t = item
        if t > maxi:
            maxi = t
    return maxi


def rmin(l):
    """
    Recursive min() for a given iterable of iterables
    Should be np.array of np.array or list of list, etc.
    args:
        l : Iterable of iterables
    return: 
        min value
    """
    mini = float('inf')
    for item in l:
        if isinstance(item, Iterable):
            t = rmin(item)
        else:
            t = item
        if t < mini:
            mini = t
    return mini

# def random_id(size=8, chars=string.ascii_letters + string.digits):
def random_id(size=8, chars='ABCDEFGHJKLMNPQRSTUVWXYZ0123456789abcdefghijkmnpqrstuvwxyz'):
    '''
    Return a random string id
    args:
        size  : id size (8)
        chars : Characters used
    return:
        id string
    '''
    return ''.join(random.choice(chars) for _ in range(size))



# -------------------------------------------------------------
# Fidle
# -------------------------------------------------------------

def get_datasets_dir(datasets_env_var='FIDLE_DATASETS_DIR'):
    '''
    Return dataset directory.
    If an env_var is defined, get, verify and return this defined path.
    If no env_var is defined, try to find a fidle datasets directory.
    If no valid datasets directory can be found, raise an Exception
    args:
        datasets_env_var : Environment var giving the location of the datasets
    return:
        datasets directory 
    '''

    # ---- Method 1 : env var
    #
    datasets_dir = os.getenv(datasets_env_var, None)
    if datasets_dir is not None:
        # Defined and exist, good
        if os.path.isdir(datasets_dir) : return datasets_dir
        # Defined, but cannot be found : erreur
        print('** OUPS !!\n----')
        print(f'** The directory specified by the {datasets_env_var} environment variable cannot be found...')
        print(f'** You should check this variable.\n')
        print('----')
        raise ValueError( f'datasets folder not found, please check {datasets_env_var} env var.' )

    # ---- Method 2 : We look around...
    #
    notebooks,datasets = looking_about()
    # No datasets dir found
    if len(datasets) == 0:
        print('** OUPS !!\n----')
        print(f'** No directory containing the datasets was found !')
        print('** The datasets are essential for this practical work.')
        print(f'** If you have installed datasets somewhere, you can specify the path via the {datasets_env_var} environment variable')
        print(f'** For more details, you can consult the installation procedure at : https://fidle.cnrs.fr/installation')
        print('----')
        raise ValueError( f'datasets folder not found, please check {datasets_env_var} env var.' )

    # ---- Get one, resolve tilde and return
    #
    datasets_dir = datasets[0]['path']
    datasets_dir = os.path.expanduser(datasets_dir)
    return  datasets_dir


def __looking_down_4about(path, depth):
    '''
    Search some fidle/about.yml files in a descending and recurring manner
    Note: Do not look further down when an instance is found
    args:
        path : path to explore
        p    : maximum depth
    '''
    # ---- Y a t-il un fichier about.yml ici ?
    if os.path.isfile(f'{path}/fidle/about.yml'): return [f'{path}/fidle/about.yml']
    # ---- Sinon, est-ce que l'on regarde dessous ?
    depth=depth-1
    # ---- Ben non, on est descendu assez bas
    if depth<0 : return []
    # ---- Ben oui, on regarde dessous
    abouts=[]
    dirs   = [d for d in glob(f'{path}/**', recursive=False) if os.path.isdir(d)]
    for d in dirs:
        sub_abouts=__looking_down_4about(d,depth)
        abouts.extend(sub_abouts)
    return abouts


def __looking_up_4about(path, up_depth, down_depth):
    '''
    Search fidle/about.yml files in an ascending and descending way, all around...
    args:
        path : starting point to explore
        up_depth   : maximum ascending depth
        down_depth : maximum descending path
    return:
        list of path, sorted and unique
    '''
    pp=Path(path)
    abouts=[]
    for i in range(up_depth):
        # print(pp)
        a=__looking_down_4about(pp, down_depth)
        abouts.extend(a)
        pp=pp.parent.absolute()
    # Supp. doublons + classement
    abouts = sorted( list(set(abouts)) )
    return abouts


def looking_about(path=None, up_depth=3, down_depth=3):
    '''
    Search fidle/about.yml files in an ascending and descending way 
    and extract informations from these files (Fidle internal use)
    args:
        path : starting point to explore, if None take current directory (None)
        up_depth   : maximum ascending depth (3)
        down_depth : maximum descending path (3)
    return:
        (notebooks, datasets) where notebooks, datasets are some array of descriptions
    '''
    # ---- Path None mean here
    #
    if path is None : path = os.getcwd()

    # ---- Clean path
    #
    path = os.path.expanduser(path)
    path = os.path.abspath(path)
    
    # ---- Get abbout files arround path
    #
    about_files = __looking_up_4about(path, up_depth,down_depth)
    
    # ---- Retrieve infos 
    #
    notebooks, datasets = [],[]
    for path in about_files:
        with open(path) as f:  about = yaml.full_load(f)
        path        = path.replace('/fidle/about.yml','')
        version     = about.get('version',     '??')
        content     = about.get('content',     '??')
        name        = about.get('name',        '??')
        description = about.get('description', '??')     

        entry = dict( path=path, version=version, content=content, name=name, description=description )

        if content == 'datasets':  datasets.append(entry)
        if content == 'notebooks': notebooks.append(entry)
    
    return notebooks,datasets
        
