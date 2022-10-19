from pydantic import BaseModel, Field, validate_arguments, validator, parse_obj_as
import pandas as pd
import numpy as np
import geopandas as gpd
from typing import Dict, List, Optional, Union
from enum import Enum
from datetime import date
#local imports
from .survey import Survey, InterpolatorsEnum, DepthRefsEnum
from .depthmodel import DepthModel

# Perforations
class StatusEnum(str,Enum):
    unknown = 'unknown'
    open = 'open'
    closed = 'closed'
    isolated = 'isolated'
    squeezed = 'squeezed'
    abandoned = 'abandoned'
    
class PerforationStatus(BaseModel):
    start_date: date = Field(...)
    end_date: date = Field(None)
    status: StatusEnum = Field(...)
    description: str = Field(None)

    class Config:
        validate_assignment = True
        extra = 'ignore'
    
        
    def df(self, name = None):
        s = pd.Series(self.dict())
        s['status'] = s['status'].value
        
        if name:
            s.name = name
        return s
    
    def get_date_array(self, freq:str='M', as_int=True):
        date_array = pd.date_range(
            start=self.start_date,
            end=self.end_date,
            freq=freq
        )
        if as_int:
            value = int(1) if self.status == StatusEnum.open else int(0)
        else:
            value = self.status.value
        return pd.Series([value]*len(date_array), index=date_array)
    
    def get_period_array(self, freq:str='M', as_int=True):
        period_array = pd.period_range(
            start=self.start_date,
            end=self.end_date,
            freq=freq
        )
        if as_int:
            value = int(1) if self.status == StatusEnum.open else int(0)
        else:
            value = self.status.value
        return pd.Series([value]*len(period_array), index=period_array)
    
        
class PerforationsStatus(BaseModel):
    status: Dict[str, PerforationStatus] = Field(None)
    class Config:
        validate_assignment = True
        
    def __repr__(self) -> str:
        return (f'Status:\n'
            f'Number of items: {len(self.status)}')

    def __str__(self) -> str:
        return (f'Formations:\n'
            f'Number of items: {len(self.status)}')
    def __len__(self):
        return len(self.status)
    
    def __getitem__(self, key):
        if isinstance(key, str):
            return self.status[key]
        elif isinstance(key, (int,slice)):
            return list(self.status.values())[key]
        else:
            raise KeyError(key)
    
    def __iter__(self):
        return (self.status[f] for f in self.status)

    def status_df(self):
        if self.status:
            df = pd.concat([self.status[s].df(name=s) for s in self.status], axis=1).T
            return df
        return None
    
    def period_array(self, freq:str='M', as_int=True):
        if self.status:
            sr =  pd.concat([self.status[s].get_period_array(freq=freq, as_int=as_int) for s in self.status], axis=0).sort_index()
            sr.name = 'status'
            return sr[~sr.index.duplicated(keep='first')]
        return None
    
    
class Perforation(DepthModel):
    status: PerforationsStatus = Field(None)
    
    def status_df(self):
        if self.status:
            df = self.status.status_df()
            df['name'] = self.name
            df['md_top'] = self.md_top
            df['md_bottom'] = self.md_bottom
            return df
        return None
    
    @validate_arguments(config=dict(arbitrary_types_allowed=True))
    def status_from_df(self,df:pd.DataFrame, name:str=None, **kwargs):
        df = df.copy()
        #Name must be the index to merge with the current perforations
        #To change columns name to match Object
        if bool(kwargs):
            kwargs = {v: k for k, v in kwargs.items()}
            df = df.rename(columns=kwargs)
            
        df[name]=df[name].astype(str)
        ps_dict = df.reset_index(drop=True).to_dict(orient='index')
        perf_status_obj = parse_obj_as(Dict[str,PerforationStatus],ps_dict)
        self.status = PerforationsStatus(status=perf_status_obj)
        
        return None
    
    def period_array(self, freq:str='M', as_int=True,fields=None):
        if self.status:
            df = self.status.period_array(freq=freq, as_int=as_int).to_frame()
            df['perforation'] = self.name
            df['md_tick'] = self.md_tick
            df['tvd_tick'] = self.tvd_tick
            df['md_midpoint'] = self.md_midpoint
            df['tvd_midpoint'] = self.tvd_midpoint
            df['tvdss_midpoint'] = self.tvdss_midpoint
            if fields is not None:
                for k,v in self.fields.items():
                    df[k] = v
            return df
        return None
    

                                  
class Perforations(BaseModel):
    perforations: Dict[str,Perforation] = Field(None)

    class Config:
        validate_assignment = True
        
    def __repr__(self) -> str:
        return (f'Formations:\n'
            f'Number of items: {len(self.perforations)}')

    def __str__(self) -> str:
        return (f'Formations:\n'
            f'Number of items: {len(self.perforations)}')
    
    def __len__(self):
        return len(self.perforations)
    
    def __getitem__(self, key):
        if isinstance(key, str):
            return self.perforations[key]
        elif isinstance(key, (int,slice)):
            return list(self.perforations.values())[key]
        else:
            raise KeyError(key)
    
    def __iter__(self):
        return (self.perforations[f] for f in self.perforations)

    @validate_arguments
    def df(self, perforations: Union[str,List[str]] = None):
        gdf_list = []
        for f in self.perforations:
            gdf_list.append(self.perforations[f].df())
        
        gdf = gpd.GeoDataFrame(pd.concat(gdf_list, axis=0))
        gdf.crs = gdf_list[0].crs
            
        gdf.index.name='perforation'
        if perforations:
            if isinstance(perforations,str):
                perforations = [perforations]
            gdf = gdf.loc[perforations]
            
        return gdf
    
    def period_array(self, perforations=None, freq:str='M', as_int=True, fields=None):
        if self.perforations:
            if perforations is None:
                perforations = list(self.perforations.keys())
            list_df = []
            for f in self.perforations:
                if f in perforations:
                    df_i = self.perforations[f].period_array(freq=freq, as_int=as_int,fields=fields)
                    list_df.append(df_i)
                else:
                    continue 
            return pd.concat(list_df, axis=0)
        return None
    
    def period_array_open(self, freq:str='M', fields=None, perforations=None, depth_ref=['md']):
        groupers = ['index'] if fields is None else ['index'] + fields
        period_array = self.period_array(freq=freq,perforations=perforations, as_int=True,fields=fields)
        if period_array is None:
            return None
        period_array.reset_index(inplace=True)
        
        vars = []
        for d in depth_ref:
            var = f'{d}_open'
            period_array[var] = period_array['status'] * period_array[f'{d}_tick']
            vars.append(var)
        return period_array.groupby(groupers)[vars].sum()
    
    def period_array_midpoint(self, perforations=None, freq:str='M', fields=None, weights=None,depth_ref = ['tvd']):
        groupers = ['index'] if fields is None else ['index'] + fields
        vars = ['index','perforation'] if fields is None else ['index','perforation'] + fields
        period_array = self.period_array(freq=freq, perforations=perforations, as_int=True,fields=fields)
        if period_array is None:
            return None
        period_array.reset_index(inplace=True)
        period_array = period_array.loc[period_array['status']==1,vars]
        
        def midpoint_func(x):
            list_perfs = x['perforation'].unique().tolist()
            ind = x['index'].iloc[0]
            midpoint = self.average_midpoint(
                perforations=list_perfs,
                weights=weights,
                depth_ref=depth_ref,
                name = f'{ind}'
            )
            
            return pd.Series(midpoint)
        
        period_array = period_array.groupby(groupers).apply(midpoint_func)
        for d in depth_ref:
            period_array[f'{d}_midpoint'] = period_array[[f'{d}_top',f'{d}_bottom']].mean(axis=1)
        period_array.drop(columns=['name'],inplace=True)
        return period_array
 
    @validate_arguments
    def average_midpoint(
        self, 
        perforations: Optional[Union[str,List[str]]] = None, 
        weights:Optional[str] = None, 
        depth_ref:Union[DepthRefsEnum,List[DepthRefsEnum]]=['md'],
        name:str = 'avg_mid_point'
    ):
        
        df = self.df(
            perforations=perforations
        )
        
        midpoint_dict = {'name':name}
        for d in depth_ref:
            top_column = f'{d}_top'
            bottom_column = f'{d}_bottom'
            if weights is not None:
                if weights not in df.columns:
                    raise ValueError(f'{weights} is not a column in the dataframe')
            value_top = df[top_column].dropna()
            value_bottom = df[bottom_column].dropna()
            
            if value_top.shape[0] > 0:
                top = np.average(value_top, weights=df[weights] if weights is not None else None)
                midpoint_dict[f'{d}_top'] = top
            if value_bottom.shape[0] > 0:
                bottom = np.average(value_bottom, weights=df[weights] if weights is not None else None)
                midpoint_dict[f'{d}_bottom'] = bottom
            
        return midpoint_dict
    
    @validate_arguments
    def estimate_average_midpoint(
        self, 
        perforations: Optional[Union[str,List[str]]] = None, 
        weights:Optional[str] = None, 
        depth_ref:Union[DepthRefsEnum,List[DepthRefsEnum]]=['md'],
        name:str = 'avg_mid_point'
    ):        
        midpoint_dict = self.average_midpoint(
            perforations=perforations,
            weights=weights,
            depth_ref=depth_ref,
            name = name
        )
        if len(midpoint_dict) > 0:
            
            new_perf = Perforation(**midpoint_dict)
            self.add_perforations(new_perf)
            
        #? It is good practice return self? 
        return None
            
    def status_df(self):
        return pd.concat([self.perforations[f].status_df() for f in self.perforations], axis=0)
    
    
    @classmethod
    def from_df(
        cls,
        df:pd.DataFrame,
        name:str=None,
        fields:List[str] = None,
        **kwargs
    ):
        df = df.copy()
        if name:
            df['name'] = df[name].copy()
            df.index = df['name']
        else:
            df['name'] = df.index
            
        #To change columns name to match Object
        if bool(kwargs):
            kwargs = {v: k for k, v in kwargs.items()}
            df = df.rename(columns=kwargs)
        
        if fields is not None:
            fields_dict = df[fields].to_dict(orient='index')
            df.drop(fields,axis=1,inplace=True)
            
            fm_dict = df.to_dict(orient='index')
            
            for fm in fm_dict:
                fm_dict[fm].update({'fields':fields_dict[fm]})
        else:
            fm_dict = df.to_dict(orient='index')
        
        return cls(
            perforations=parse_obj_as(
                Dict[str,Perforation],
                fm_dict
            )
        )
    
    @validate_arguments(config=dict(arbitrary_types_allowed=True))
    def status_from_df(self,df:pd.DataFrame, name:str=None, **kwargs):
        df = df.copy()
        #Name must be the index to merge with the current perforations
        #To change columns name to match Object
        if bool(kwargs):
            kwargs = {v: k for k, v in kwargs.items()}
            df = df.rename(columns=kwargs)
            
        list_perforations = list(self.perforations.keys())
        df[name]=df[name].astype(str)
        for i in df[name].unique():
            if i not in list_perforations:
                print(f'{i} is not in current perforations  {list_perforations}')
                continue

            ps_dict = df.loc[df[name]==i].reset_index(drop=True).to_dict(orient='index')
            perf_status_obj = parse_obj_as(Dict[str,PerforationStatus],ps_dict)
            self.perforations[i].status = PerforationsStatus(status=perf_status_obj)
        
        return None
    
    @validate_arguments
    def add_perforations(self, perforations: Union[List[Perforation],Dict[str,Perforation],Perforation]):
        perf_dict = {}
        if isinstance(perforations,Perforation):
            perf_dict.update({perforations.name:perforations})
        elif isinstance(perforations,list):
            perf_dict.update({p.name:p for p in perforations})
        elif isinstance(perforations,dict):
            perf_dict = perforations
        
        if self.perforations:
            self.perforations.update(perf_dict)
        else:
            self.perforations = perf_dict
            
        return None
    
    @validate_arguments
    def estimate_ticks(self,perforations = None,depth_ref:Union[DepthRefsEnum,List[DepthRefsEnum]]=['md','tvd']):
        if perforations is None:
            perforations = self.perforations.keys()
            
        for f in perforations:
            self.perforations[f].estimate_ticks(depth_ref)
            
        return None
       
    @validate_arguments
    def estimate_midpoints(self,perforations = None,depth_ref:Union[DepthRefsEnum,List[DepthRefsEnum]]=['md','tvd','tvdss']):
        if perforations is None:
            perforations = self.perforations.keys()
            
        for f in perforations:
            self.perforations[f].estimate_midpoint(depth_ref)
            
        return None
    
    @validate_arguments
    def estimate_coordinate(self,survey: Survey,perforations=None, depth_ref:DepthRefsEnum='md'):
        if perforations is None:
            perforations = self.perforations.keys()
            
        for f in perforations:
            self.perforations[f].estimate_coordinate(survey,depth_ref=depth_ref)
            
        return None
    
    @validate_arguments
    def get_reference_depth(
        self,
        survey: Survey, 
        perforations=None,
        depth_ref:Union[InterpolatorsEnum,List[InterpolatorsEnum]] = [InterpolatorsEnum.md_to_tvd,InterpolatorsEnum.md_to_tvdss]
    ):
        
        if perforations is None:
            perforations = self.perforations.keys()
            
        for f in perforations:
            self.perforations[f].get_reference_depth(survey,depth_ref=depth_ref)  
            
        return None