#!/usr/bin/python
#coding = utf-8

from RiskQuantLib.Property.NumberProperty.numberProperty import numberProperty

class duration(numberProperty):
    def __init__(self,value,unit = ''):
        super(duration,self).__init__(value,unit)



