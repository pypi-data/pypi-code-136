from pydantic import BaseModel, Field, validator,parse_obj_as
from typing import Dict, Union, List
from enum import Enum
import pandas as pd
from datetime import date, datetime
from numpy import unique

class FreqEnum(str, Enum):
    A = 'A'
    M = 'M'
    D = 'D'

class RecoveryEnum(str, Enum):
    total = 'total'
    primary = 'primary'
    secondary = 'secondary'
    associated = 'associated' 
    
class TypeDataEnum(str, Enum):
    measured = 'measured'
    estimated = 'estimated'
    forecast = 'forecast' 

class LevelEnum(str, Enum):
    well = 'well'
    formation = 'formation'
    layer = 'layer'

class FormatEnum(str, Enum):
    calendar = 'calendar'
    effective = 'effective'
    volume = 'volume'


class Record(BaseModel):
    fmt: str = Field('%Y-%m-%d')
    freq: FreqEnum = Field(default=FreqEnum.M)
    period: Union[pd.Period,date,pd.Timestamp,str] = Field(...)
    oil: Union[float,None] = Field(None, ge=0, description='Daily oil rate')
    water: Union[float,None] = Field(None, ge=0, description='Daily Water Rate')
    gas: Union[float,None] = Field(None, ge=0, description='Daily gas Rate')
    water_inj: Union[float,None] = Field(None, ge=0, description='Daily WaterInj Rate')
    gas_inj: Union[float,None] = Field(None, ge=0, description='Daily Gas Inj Rate')
    uptime: float = Field(1, ge=0, le=1)
    recovery: RecoveryEnum = Field(default=RecoveryEnum.total)
    type: TypeDataEnum = Field(default=TypeDataEnum.measured)
    level: LevelEnum = Field(default=LevelEnum.well)
    format: FormatEnum = Field(default=FormatEnum.calendar)
    scenario: str = Field(...)
    fields: Union[Dict[str, Union[float,int,str]],None] = Field(None)
    
    
    class Config:
        extra = 'ignore'
        validate_assigment = True
        arbitrary_types_allowed = True
        underscore_attrs_are_private = True
        json_encoders = {
            pd.Period: lambda x: x.strftime('%Y-%m-%d')
        }
    
    @validator('period')
    def check_period_type(cls, v, values):
        if isinstance(v,pd.Period):
            return v 
        elif isinstance(v,(pd.Timestamp,date)):
            freq = values['freq']
            return  pd.Period(v, freq=freq)
        elif isinstance(v,str):
            fmt = values['fmt']
            freq = values['freq']
            return pd.Period(datetime.strptime(v,fmt),freq=freq)
            
    
    def to_series(self):
        d = self.dict(exclude={'fields','fmt'})
        if self.fields:
            d.update(self.fields)
            
        return pd.Series(d)
    
    def to_volume(self, which = None):
        obj = self.copy()
        list_props = ['oil','water','gas','water_inj','gas_inj']
        if which is None:
            prop = list_props.copy()
        elif isinstance(which,str):
            prop = [which]
        if any([i not in list_props for i in prop]):
            raise ValueError(f'any of next values: {which} is not in {list_props}')

        if self.format == 'calendar':
            uptime = 1
        elif self.format == 'effective':
            uptime = self.uptime
        else:
            return obj

        start_time = self.period.start_time
        end_time = self.period.end_time
        delta = end_time - start_time
        delta_days = delta.total_seconds()/86400
        
        for i in prop:
            rate = getattr(self,i)
            if rate is None:
                continue
            
            vol = rate * uptime * delta_days
            setattr(obj,i, vol)
        setattr(obj,'format','volume')
            
        return obj
    
    def to_calendar(self, which=None):
        obj = self.copy()
        list_props = ['oil','water','gas','water_inj','gas_inj']
        if which is None:
            prop = list_props.copy()
        elif isinstance(which,str):
            prop = [which]
        if any([i not in list_props for i in prop]):
            raise ValueError(f'any of next values: {which} is not in {list_props}')


        start_time = self.period.start_time
        end_time = self.period.end_time
        delta = end_time - start_time
        delta_days = delta.total_seconds()/86400
        
        if self.format == 'volume':
            uptime = 1
        elif self.format == 'effective':
            uptime = self.uptime * delta_days
        else:
            return obj
        
        for i in prop:
            val = getattr(self,i)
            if val is None:
                continue
            
            cal = val * uptime * (1/delta_days)
            setattr(obj,i, cal)
        setattr(obj,'format','calendar')
            
        return obj

    def to_effective(self, which=None):
        obj = self.copy()
        list_props = ['oil','water','gas','water_inj','gas_inj']
        if which is None:
            prop = list_props.copy()
        elif isinstance(which,str):
            prop = [which]

        if any([i not in list_props for i in prop]):
            raise ValueError(f'any of next values: {which} is not in {list_props}')


        start_time = self.period.start_time
        end_time = self.period.end_time
        delta = end_time - start_time
        delta_days = delta.total_seconds()/86400
        
        if self.format == 'calendar':
            uptime = delta_days / self.uptime
        elif self.format == 'volume':
            uptime = 1/self.uptime
        else:
            return obj
        
        for i in prop:
            val = getattr(self,i)
            if val is None:
                continue
            
            cal = val * uptime * (1/delta_days)
            setattr(obj,i, cal)
        setattr(obj,'format','effectiveß')
            
        return obj
        
        
class Production(BaseModel):
    records: List[Record]
    
    class Config:
        extra = 'ignore'
        validate_assigment = True
        arbitrary_types_allowed = True
        json_encoders = {
            pd.Period: lambda x: x.strftime('%Y-%m-%d')
        }
    
    @validator('records')
    def check_same_scenario_freq(cls,v):
        assert unique([i.scenario for i in v]).shape[0] == 1
        assert unique([i.freq for i in v]).shape[0] == 1
        return v
    
    @classmethod
    def from_df(
        cls,
        df:pd.DataFrame,
        freq:FreqEnum=FreqEnum.M,
        fields:List[str] = None,
        parse_date:bool=False,
        fmt:str = None,
        scenario_name='prod',
        recovery: RecoveryEnum = RecoveryEnum.total,
        type: TypeDataEnum = TypeDataEnum.measured,
        level: LevelEnum = LevelEnum.well,
        format:FormatEnum = FormatEnum.calendar,
        **kwargs
    ):
        _df = df.copy()

        #To change columns name to match Object
        if bool(kwargs):
            kwargs = {v: k for k, v in kwargs.items()}
            _df = _df.rename(columns=kwargs)
            
        if parse_date:
            _df['period'] = pd.to_datetime(_df['period'],format=fmt).dt.to_period(freq=freq)
        
        for s,v in zip(['scenario','recovery','type','level','format'],[scenario_name,recovery,type,level,format]):
            if s not in _df.columns:
                _df[s] = v
        
        if fields is not None:
            fields_dict = _df[fields].to_dict(orient='records')
            _df = _df.drop(columns=fields)
            
            pr_dict = _df.to_dict(orient='records')
            
            for i,pr in enumerate(pr_dict):
                pr.update({'fields':fields_dict[i]})
        else:
            pr_dict = _df.to_dict(orient='records')
        return cls(
            records=parse_obj_as(
                List[Record],
                pr_dict
            )
        )
        
    
    def to_calendar(self):
        obj = self.copy()
        
        list_r = [i.to_calendar() for i in obj.records]
        obj.records = list_r
        return obj

    def to_effective(self):
        obj = self.copy()
        
        list_r = [i.to_effective() for i in obj.records]
        obj.records = list_r
        return obj
    
    def to_volume(self):
        obj = self.copy()
        
        list_r = [i.to_volume() for i in obj.records]
        obj.records = list_r
        return obj
        
    def df(self):
        list_series = [r.to_series() for r in self.records]
        prod_df =  pd.concat(list_series, axis=1).T
        #prod_df['period'] = prod_df[['date','freq']].apply(lambda x: pd.Period(x['date'], freq=x['freq']), axis=1)
        return prod_df