from functools import lru_cache  #增加缓存
from collections.abc import Iterable
from typing import Union


class Dao:
    _all = ""
    def __init__(self,x:Union[int , str]):
        self.__index = _convert2index(self,x)
        
    @property
    def index(self):
        return self.__index
        
    @property
    def name(self):
        return self._all[self.index]    
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"{self.__class__.__name__}<{self.name}>"
    
class Tiangan:
    pass
class Dizhi:
    pass
@lru_cache(maxsize=None)
class Dizhi(Dao):
    _all='子丑寅卯辰巳午未申酉戌亥'
    
    @property
    def canggan(self)->iter:
        return Dizhi.getCangGan(self.index)
    
    def getCangGan(dz:Union[int , str])->tuple:
        """地支藏干
        返回：天干Tuple
        0      1     2     3     4     5     6     7     8     9 
        "甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"
        """
        dz = _convert2index(Dizhi,dz)
        cg = [(9,),(5,9,7),(0,2,4),(1,),(4,1,9),(2,6,4),(3,5),(5,3,1),(6,8,4),(7,),(4,7,3),(8,0)]
        return tuple((Tiangan(i) for i in cg[dz]))
    
@lru_cache(maxsize=None)
class Tiangan(Dao):
    _all='甲乙丙丁戊己庚辛壬癸'
    
    def getShiSheng(self,arg:Union[int , str , Tiangan, Dizhi , list])->list:
        """获取十神,以自身为太极点，求十神
        """ 
        if type(arg) is str:
            for x in arg:
                if x in Dizhi._all:
                    return self.getShiSheng(Dizhi(x))
                elif x not in self._all:
                    raise ValueError(f"'{x}',参数错误")
        
        elif isinstance(arg,type(Dizhi(0))):
            return self.getShiSheng(arg.canggan)
            
        elif isinstance(arg,Iterable):
            res = []
            for x in arg:
                res+=self.getShiSheng(x)
            return res
        
        arg = _convert2index(Tiangan,arg)
        return [Shishen.getShiSheng(self.index,arg)]


@lru_cache(maxsize=None)
class Shishen(Dao):
    _all= ['比肩','劫财','食神','伤官','偏财','正财','七杀','正官','偏印','正印']

    def getShiSheng(tg:Union[int , str , Tiangan],tg2:Union[int , str , Tiangan]):
        """获取十神 以tg为太极点，求tg2是tg的什么十神
        返回：十神类
        """      
        tg = _convert2index(Tiangan,tg)
        tg2 = _convert2index(Tiangan,tg2)
        
        i = tg2-tg
        if i%2!=0 and tg%2!=0:
            i = (i+2)%10
            return Shishen(i)
        return Shishen(i%10)


def _convert2index(cls,x:Union[int, str , Tiangan , Dizhi]):
    """将参数转换为索引"""
    if type(x) is int:
        assert x<=len(cls._all), "The 'index' out of bounds."
        return x

    elif type(x) is str:
        assert x in cls._all, "arg 'x' is wrong."
        return cls._all.index(x)
    
    elif isinstance(x,type(Tiangan(0))) or isinstance(x,type(Dizhi(0))):
        return x.index
    else:
        assert False, "arg is wrong"


    
@lru_cache(maxsize=None)
class Ganzhi(Dao):
    _all =  [ "甲子","乙丑","丙寅","丁卯","戊辰","己巳","庚午","辛未","壬申","癸酉",
            "甲戌","乙亥","丙子","丁丑","戊寅","己卯","庚辰","辛巳","壬午","癸未",
            "甲申","乙酉","丙戌","丁亥","戊子","己丑","庚寅","辛卯","壬辰","癸巳",
            "甲午","乙未","丙申","丁酉","戊戌","己亥","庚子","辛丑","壬寅","癸卯",
            "甲辰","乙巳","丙午","丁未","戊申","己酉","庚戌","辛亥","壬子","癸丑",
            "甲寅","乙卯","丙辰","丁巳","戊午","己未","庚申","辛酉","壬戌","癸亥"]
    
    @property
    def tiangan(self):
        return Tiangan(self.name[0])
    
    @property
    def dizhi(self):
        return Dizhi(self.name[1])
    
