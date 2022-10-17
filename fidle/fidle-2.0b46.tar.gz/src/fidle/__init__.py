# ==================================================================
#            ______ _     _ _        __  __           _ 
#           |  ____(_)   | | |      |  \/  |         | |
#           | |__   _  __| | | ___  | \  / | ___   __| |
#           |  __| | |/ _` | |/ _ \ | |\/| |/ _ \ / _` |
#           | |    | | (_| | |  __/ | |  | | (_) | (_| |
#           |_|    |_|\__,_|_|\___| |_|  |_|\___/ \__,_|
#                                                          
# ==================================================================
# A simple module to host usefull functions for Fidle practical work
# Jean-Luc Parouty CNRS/MIAI/SIMaP 2022

import os,sys,platform
import glob
import shutil
import pathlib

from random import randint
import matplotlib

from IPython.display import display,HTML

import fidle.config
import fidle.scrawler
import fidle.utils

from fidle.Chrono   import Chrono


__version__   = fidle.config.VERSION

__run_id        = None
__run_dir       = None
__datasets_dir  = None

utils           = fidle.utils
plot            = fidle.scrawler
config          = fidle.config
chrono          = Chrono()


# -------------------------------------------------------------
# init
# -------------------------------------------------------------
#
'''
Initialization with parameters run_id and run_dir.
These two parameters can be overridden via environment variables
FIDLE_OVERRIDE_run_id and FIDLE_OVERRIDE_run_dir.
datasets_dir is retrieved via the environment variable <datasets_env_var>.
params:
    run_id           : Run id for the notebook (random number if None)           (None)
    run_dir          : Run directory (./run/{run_id} if None)                    (None)
    datasets_env_var : Name of env. var. specifying the location of the datasets (FIDLE_DATASETS_DIR)
return:
    run_id, run_dir, datasets_dir
'''
def init(run_id=None, run_dir=None, datasets_env_var='FIDLE_DATASETS_DIR'):
    global __run_id
    global __run_dir
    global __datasets_dir
    
    # ---- run_id
    # 
    # If None, we choose
    __run_id    = str(randint(10000,99999)) if run_id  is None else run_id

    # Overrided ?
    __run_id    = __get_override_env('run_id', __run_id)

    # ---- run_dir 
    # 
    # If None, we set it
    __run_dir   = f'./run/{__run_id}'       if run_dir is None else run_dir

    # Override run_dir ?
    __run_dir   = __get_override_env('run_dir', __run_dir)
    
    # Create run_dir    
    utils.mkdir(__run_dir)

    # ---- Parameters from config.py
    #
    mplstyle  = config.FIDLE_MPLSTYLE
    cssfile   = config.FIDLE_CSSFILE
    
    # ---- Load matplotlib style and css
    #
    module_dir = pathlib.Path(__file__).parent
    matplotlib.style.use(f'{module_dir}/{mplstyle}')
    __load_cssfile(f'{module_dir}/{cssfile}')
    
    # ---- Get datasets location 
    #      From env var or by looking for
    #      Raise an exception if cannot be found.
    #
    __datasets_dir=utils.get_datasets_dir(datasets_env_var)
            
    # ---- Update Keras cache
    #
    updated = __update_keras_cache()

    # ---- Tensorflow log level
    #
    log_level = int(os.getenv('TF_CPP_MIN_LOG_LEVEL', 0 ))
    str_level = ['Info + Warning + Error','Warning + Error','Error only'][log_level]
    
    # ---- Today, now and hostname
    #
    chrono.start('__global__')
    h = platform.uname()
    
    # ---- Save figs
    #
    save_figs = os.getenv('FIDLE_SAVE_FIGS', str(config.SAVE_FIGS) )
    save_figs = (save_figs.lower() == 'true')
    figs_dir  = f'{__run_dir}/figs'

    plot.set_save_fig( save = save_figs, 
                  figs_dir  = figs_dir, 
                  figs_name = f'fig_{__run_id}_', 
                  figs_id   = 0 )

    # ---- Hello world
    #
    utils.display_md('<br>**FIDLE - Environment initialization**')
    print('Version              :', config.VERSION)
    print('Run id               :', __run_id)
    print('Run dir              :', __run_dir)
    print('Datasets dir         :', __datasets_dir)
    print('Start time           :', chrono.get_start('__global__'))
    print('Hostname             :', f'{h[1]} ({h[0]})')
    print('Tensorflow log level :', str_level,f' (={log_level})')
    print('Update keras cache   :', updated)
    print('Save figs            :', figs_dir, f'({save_figs})')
    
    # ---- Modules versions
    #
    for m in config.USED_MODULES:
        if m in sys.modules:
            print(f'{m:21s}:', sys.modules[m].__version__)

    # ---- Overrided ?
    #
    if run_id != __run_id:  
        print(f'\n** run_id has been overrided from {run_id} to {__run_id}')


    return __run_id, __run_dir, __datasets_dir

# ------------------------------------------------------------------
# Update keras cache
# ------------------------------------------------------------------
# Try to sync ~/.keras/cache with datasets/keras_cache
# because sometime, we cannot access to internet... (IDRIS..)
#
def __update_keras_cache():
    updated = False
    if os.path.isdir(f'{__datasets_dir}/keras_cache'):
        from_dir = f'{__datasets_dir}/keras_cache/*.*'
        to_dir   = os.path.expanduser('~/.keras/datasets')
        utils.mkdir(to_dir)
        for pathname in glob.glob(from_dir):
            filename=os.path.basename(pathname)
            destname=f'{to_dir}/{filename}'
            if not os.path.isfile(destname):
                shutil.copy(pathname, destname)
                updated=True
    return updated


# ------------------------------------------------------------------
# Override
# ------------------------------------------------------------------
#  
    
def override(*names, module_name='__main__', verbose=True, return_attributes=False):
    '''
    Try to override attributes given par name with environment variables.
    Environment variables name must be : FIDLE_OVERRIDE_<NAME>
    If no env variable is available for a given name, nothing is change.
    If type is str, substitution is done with 'notebook_id' and 'datasets_dir'
    Example : override('image_size','nb_epochs')
    params:
       names : list of attributes names as a str list
               if empty, all attributes can be override
    return :
       dict {name=new value}
    '''
    # ---- Where to override
    #
    module=sys.modules[module_name]
    
    # ---- No names : mean all
    #
    if len(names)==0:
        names=[]
        for name in dir(module):
            if name.startswith('_'): continue
            v=getattr(module,name)
            if type(v) not in [str, int, float, bool, tuple, list, dict]: continue
            names.append(name)
            
    # ---- Search for names
    #
    overrides={}
    for name in names:
        
        # ---- Variable doesn't exist
        #
        if not hasattr(module,name):
            print(f'** Warning : You try to override an inexistant variable ({name})')
            continue

        # ---- Get override environment variable name
        #
        env_value = __get_override_env(name, None)

        # ---- Environment variable doesn't exist
        #
        if env_value is None: continue

        # ---- Environment variable and variable exist both
        #
        value_old  = getattr(module,name)
        value_type = type(value_old)
        
        if value_type in [ str ] : 
            new_value = env_value.format(datasets_dir=__datasets_dir, run_id=__run_id)

        if value_type in [ int, float, bool, tuple, list, dict, type(None)]:
            new_value = eval(env_value)
    
        # ---- Override value
        #
        setattr(module,name,new_value)
        overrides[name]=new_value

    if verbose and len(overrides)>0:
        print('** Overrided parameters : **')
        for name,value in overrides.items():
            print(f'{name:20s} : {value}')
            
    if return_attributes:
        return overrides
       
  
def __get_override_env(name, default_value=None):
    env_name  = f'FIDLE_OVERRIDE_{name}'
    env_value = os.environ.get(env_name, default_value) 
    return env_value


# def __has_override_env(name):
#     env_name  = f'FIDLE_OVERRIDE_{name}'
#     return (env_name in os.environ)



def __load_cssfile(cssfile):
    if cssfile is None: return
    styles = open(cssfile, "r").read()
    display(HTML(styles))
    
     

    
     
def end():
    chrono.stop('__global__')
    end_time = chrono.get_end('__global__')
    duration = chrono.get_delay('__global__', format='human')
    site_url = "https://fidle.cnrs.fr"
    md = f'**End time :** {end_time}  \n'
    md+= f'**Duration :** {duration}  \n'
    md+= f'This notebook ends here :-)  \n'
    md+= f'[{site_url}]({site_url})'
    utils.display_md(md)
     
     
