import os
from os import system
from os.path import expanduser
import platform
import time
import sys

def get_timespan(_t0):
    t1 = time.time()
    span = t1 - _t0
    return span

_t0 = time.time()

from tyjuliasetup import use_sysimage, use_backend
# use_backend('jnumpy')

# 初始化
def init_with_sysimage(sysimage_path="", need_use_sysimage=True):
    """
    使用映像初始化

    Parameters
    ----------
        sysimage_path : String
            映像文件路径：若为空则使用默认的映像文件路径，位于`<.julia>/environments/v1.7/JuliaSysimage.{dll,so}`
            
        need_use_sysimage : Bool
            是否使用映像：默认为True
    """
    if need_use_sysimage:
        if platform.system().lower() == 'windows':
            sysimage_path = sysimage_path if sysimage_path!="" else "C:/Users/Public/TongYuan/.julia/environments/v1.7/JuliaSysimage.dll"            
        elif platform.system().lower() == 'linux':
            sysimage_path = sysimage_path if sysimage_path!="" else expanduser("~/TongYuan/.julia/environments/v1.7/JuliaSysimage.so")

        if os.path.exists(sysimage_path):
            use_sysimage(sysimage_path)        
        else:
            print("%s 文件不存在！"%sysimage_path)
            
    import tyjuliacall
    print(f"导入tyjuliacall: {get_timespan(_t0):.2f} s")
    