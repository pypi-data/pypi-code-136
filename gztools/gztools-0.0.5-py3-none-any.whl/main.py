from .base import *

from functools import lru_cache  #增加缓存
from collections.abc import Iterable
from typing import Union


class Canggan(Dao):
    _all = DIZHI

    def __init__(self, x: Union[int, str]):
        super().__init__(x)
        self.__canggan = []

    @property
    def benqi(self):
        return self[0]

    @property
    def zhongqi(self):
        return self[1]

    @property
    def yuqi(self):
        return self[2]

    @property
    def all(self):
        if not self.__canggan:
            self.__canggan = Canggan.get_canggan(self.index)
        return self.__canggan

    def __getitem__(self, index):
        return self.all[index]

    def __str__(self):
        return f"{self.name}中藏{self.all}"
    
    def __repr__(self):
        return f"{self.__class__.__name__}<{self.name}>{self.all}"

    @staticmethod
    def get_canggan(dz:Union[int , str])->tuple:
        """地支藏干
        返回：天干Tuple
        0      1     2     3     4     5     6     7     8     9 
        "甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"
        """
        dz = convert2index(Dizhi,dz)
        cg = [(9,),(5,9,7),(0,2,4),(1,),(4,1,9),(2,6,4),(3,5),(5,3,1),(6,8,4),(7,),(4,7,3),(8,0)]
        return tuple((create_tiangan(i) for i in cg[dz]))



class Dizhi(Dao):
    _all = DIZHI
    
    def get_canggan(self)->iter:
        return create_canggan(self.index)
    

    

class Tiangan(Dao):
    _all = TIANGAN
    
    def get_shishen(self,arg:Union[int , str , Tiangan, Dizhi , list])->list:
        """获取十神,以自身为太极点，求十神
        """ 
        if type(arg) is str:
            for x in arg:
                if x in Dizhi._all:
                    return self.get_shishen(Dizhi(x))
                elif x not in self._all:
                    raise ValueError(f"'{x}',参数错误")
        
        elif isinstance(arg,Dizhi):
            return self.get_shishen(arg.canggan)
            
        elif isinstance(arg,Iterable):
            res = []
            for x in arg:
                res+=self.get_shishen(x)
            return res
        
        arg = convert2index(Tiangan,arg)
        return [Shishen.get_shishen(self.index,arg)]


@lru_cache(maxsize=None)
class Shishen(Dao):
    _all= SHISHEN

    def get_shishen(tg:Union[int , str , Tiangan],tg2:Union[int , str , Tiangan]):
        """获取十神 以tg为太极点，求tg2是tg的什么十神
        返回：十神类
        """      
        tg = convert2index(Tiangan,tg)
        tg2 = convert2index(Tiangan,tg2)
        
        i = tg2-tg
        if i%2!=0 and tg%2!=0:
            i = (i+2)%10
            return Shishen(i)
        return Shishen(i%10)



class Ganzhi(Dao):
    _all = GANZHI
    
    @property
    def tiangan(self):
        return create_tiangan(self.name[0])
    
    @property
    def dizhi(self):
        return create_dizhi(self.name[1])
    


@lru_cache(maxsize=None)
def create_tiangan(x:Union[int , str]):
    return Tiangan(x)

@lru_cache(maxsize=None)
def create_dizhi(x:Union[int , str]):
    return Dizhi(x)

@lru_cache(maxsize=None)
def create_ganzhi(x:Union[int , str]):
    return Ganzhi(x)

@lru_cache(maxsize=None)
def create_shishen(x:Union[int , str]):
    return Shishen(x)

@lru_cache(maxsize=None)
def create_canggan(x:Union[int , str]):
    return Canggan(x)
