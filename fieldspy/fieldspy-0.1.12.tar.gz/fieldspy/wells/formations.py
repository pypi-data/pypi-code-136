from pydantic import BaseModel, Field, validate_arguments, validator, parse_obj_as
import pandas as pd
import numpy as np
import geopandas as gpd
from typing import Dict, List, Union, Optional
from enum import Enum
#local imports
from .survey import Survey, InterpolatorsEnum, DepthRefsEnum
from .depthmodel import DepthModel


# Formations

class GeologicPeriodEnum(str,Enum):
    neogene = 'neogene'
    paleogene = 'paleogene'
    cretaceous = 'cretaceous'
    jurassic = 'jurassic'
    triassic = 'triassic'
    permian = 'permian'

class Formation(DepthModel):
    period: GeologicPeriodEnum = Field(None)
        
class Formations(BaseModel):
    formations: Dict[str,Formation] = Field(None)

    class Config:
        validate_assignment = True

    def __repr__(self) -> str:
        return (f'Formations:\n'
            f'Number of items: {len(self.formations)}')

    def __str__(self) -> str:
        return (f'Formations:\n'
            f'Number of items: {len(self.formations)}')
    
    def __len__(self):
        return len(self.formations)
    
    def __getitem__(self, key):
        if isinstance(key, str):
            return self.formations[key]
        elif isinstance(key, (int,slice)):
            return list(self.formations.values())[key]
        else:
            raise KeyError(key)
    
    def __iter__(self):
        return (self.formations[f] for f in self.formations)

    def formations_list(self):
        return list(self.formations.keys())
    
    @validate_arguments
    def df(self, formations:Union[str,List[str]]=None):
        gdf_list = []
        for f in self.formations:
            gdf_list.append(self.formations[f].df())
        
        gdf = gpd.GeoDataFrame(pd.concat(gdf_list, axis=0))
        gdf.crs = gdf_list[0].crs
        gdf.index.name='formation'
        if formations:
            if isinstance(formations,str):
                formations = [formations]
            gdf = gdf.loc[formations]
        return gdf
    
    @validate_arguments
    def estimate_average_midpoint(
        self, 
        formations: Optional[Union[str,List[str]]] = None, 
        weights:Optional[str] = None, 
        depth_ref:Union[DepthRefsEnum,List[DepthRefsEnum]]=['md'],
        name:str = 'avg_mid_point'
    ):
        df = self.df(
            formations=formations
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
            
        if len(midpoint_dict) > 0:
            
            new_form = Formation(**midpoint_dict)
            self.add_formations(new_form)
            
        #? It is good practice return self? 
        return None
    
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
            formations=parse_obj_as(
                Dict[str,Formation],
                fm_dict
            )
        )
    
    @validate_arguments
    def add_formations(self, formations: Union[List[Formation],Dict[str,Formation],Formation]):
        form_dict = {}
        if isinstance(formations,Formation):
            form_dict.update({formations.name:formations})
        elif isinstance(formations,list):
            form_dict.update({p.name:p for p in formations})
        elif isinstance(formations,dict):
            form_dict = formations
        
        if self.formations:
            self.formations.update(form_dict)
        else:
            #print(form_dict)
            self.formations = form_dict

        return None
    
    @validate_arguments
    def estimate_ticks(self,formations = None,depth_ref:Union[DepthRefsEnum,List[DepthRefsEnum]]=['md','tvd']):
        if formations is None:
            formations = self.formations.keys()
            
        for f in formations:
            self.formations[f].estimate_ticks(depth_ref)

        return None
    
    @validate_arguments
    def estimate_midpoints(self,formations = None,depth_ref:Union[DepthRefsEnum,List[DepthRefsEnum]]=['md','tvd','tvdss']):
        if formations is None:
            formations = self.formations.keys()

        list_fm = self.formations_list()    
    
        for f in formations:
            if f not in list_fm:
                continue
            self.formations[f].estimate_midpoint(depth_ref)


        return None
    
    @validate_arguments
    def estimate_coordinate(self,survey: Survey,formations=None, depth_ref:DepthRefsEnum='md'):
        if formations is None:
            formations = self.formations.keys()
            
        for f in formations:
            self.formations[f].estimate_coordinate(survey,depth_ref=depth_ref)
            
        return None
    
    @validate_arguments
    def get_reference_depth(
        self,
        survey: Survey, 
        formations=None,
        depth_ref:Union[InterpolatorsEnum,List[InterpolatorsEnum]] = [InterpolatorsEnum.md_to_tvd,InterpolatorsEnum.md_to_tvdss]
    ):
        
        if formations is None:
            formations = self.formations.keys()
            
        for f in formations:
            self.formations[f].get_reference_depth(survey,depth_ref=depth_ref)    
        
        return None
            
    @validate_arguments
    def bottom_from_next_top(self, depth_ref:DepthRefsEnum='md',end_depth:float=None,plus_depth:float=100):
        df = self.df().sort_values(by=[f'{depth_ref}_top'])
        
        for i,(idx,row) in enumerate(df.iterrows()):
            if i+1 == len(df):
                if end_depth is not None:
                    setattr(self.formations[idx],f'{depth_ref}_bottom',end_depth)
                if plus_depth is not None:
                    setattr(self.formations[idx],f'{depth_ref}_bottom',row[f'{depth_ref}_top']+plus_depth)
            else:
                setattr(self.formations[idx],f'{depth_ref}_bottom',df[f'{depth_ref}_top'].iloc[i+1])
        
        return None
            
