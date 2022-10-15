from typing import Union

class Dao:
    _all = ""
    def __init__(self,x:Union[int , str]):
        self.__index = convert2index(self,x)
        
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
class Ganzhi:
    pass
class Shishen:
    pass


DIZHI = "子丑寅卯辰巳午未申酉戌亥"
TIANGAN = "甲乙丙丁戊己庚辛壬癸"
GANZHI = [ "甲子","乙丑","丙寅","丁卯","戊辰","己巳","庚午","辛未","壬申","癸酉",
            "甲戌","乙亥","丙子","丁丑","戊寅","己卯","庚辰","辛巳","壬午","癸未",
            "甲申","乙酉","丙戌","丁亥","戊子","己丑","庚寅","辛卯","壬辰","癸巳",
            "甲午","乙未","丙申","丁酉","戊戌","己亥","庚子","辛丑","壬寅","癸卯",
            "甲辰","乙巳","丙午","丁未","戊申","己酉","庚戌","辛亥","壬子","癸丑",
            "甲寅","乙卯","丙辰","丁巳","戊午","己未","庚申","辛酉","壬戌","癸亥"]

SHISHEN = ['比肩','劫财','食神','伤官','偏财','正财','七杀','正官','偏印','正印']


def convert2index(cls,x:Union[int, str, Dao]):
    """将参数转换为索引"""
    if type(x) is int:
        assert x<=len(cls._all), "The 'index' out of bounds."
        return x

    elif type(x) is str:
        assert x in cls._all, "arg 'x' is wrong."
        return cls._all.index(x)
    
    elif isinstance(x,Dao):
        return x.index
    else:
        assert False, "arg is wrong"
        

