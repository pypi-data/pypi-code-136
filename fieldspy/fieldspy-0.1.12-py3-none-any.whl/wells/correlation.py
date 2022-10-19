from pydantic import BaseModel, Field, validate_arguments, validator, parse_obj_as
import pandas as pd
import geopandas as gpd
from typing import Dict, List, Union
#local imports
from .survey import Survey, InterpolatorsEnum, DepthRefsEnum
from .depthmodel import DepthModel


# Correlations

class Correlation(DepthModel):
    pass
        
class Correlations(BaseModel):
    correlations: Dict[str,Correlation] = Field(None)

    class Config:
        validate_assignment = True
        
    def __repr__(self) -> str:
        return (f'Formations:\n'
            f'Number of items: {len(self.correlations)}')

    def __str__(self) -> str:
        return (f'Formations:\n'
            f'Number of items: {len(self.correlations)}')
    
    def __len__(self):
        return 0 if self.correlations is None else len(self.correlations)
    
    def __getitem__(self, key):
        if isinstance(key, str):
            return self.correlations[key]
        elif isinstance(key, (int,slice)):
            return list(self.correlations.values())[key]
        else:
            raise KeyError(key)
    
    def __iter__(self):
        return (self.correlations[f] for f in self.correlations)
    
    @validate_arguments
    def df(self, correlations:Union[str,List[str]]=None):
        gdf = gpd.GeoDataFrame()
        for f in self.correlations:
            gdf = gdf.append(self.correlations[f].df())
        gdf.index.name='correlation'
        if correlations:
            if isinstance(correlations,str):
                correlations = [correlations]
            gdf = gdf.loc[correlations]
        return gdf
    
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
            correlations=parse_obj_as(
                Dict[str,Correlation],
                fm_dict
            )
        )

    
    @validate_arguments
    def add_correlations(self, correlations: Union[Correlation,List[Correlation],Dict[str,Correlation]]):
        form_dict = {}
        if isinstance(correlations,Correlation):
            form_dict.update({correlations.name:correlations})
        elif isinstance(correlations,list):
            form_dict.update({p.name:p for p in correlations})
        elif isinstance(correlations,dict):
            form_dict = correlations
        
        if self.correlations:
            self.correlations.update(form_dict)
        else:
            self.correlations = form_dict
        
        return None
    
    @validate_arguments
    def estimate_ticks(self,correlations = None,depth_ref:Union[DepthRefsEnum,List[DepthRefsEnum]]=['md','tvd']):
        if correlations is None:
            correlations = self.correlations.keys()
            
        for f in correlations:
            self.correlations[f].estimate_ticks(depth_ref)
            
        return None
    
    @validate_arguments
    def estimate_midpoints(self,correlations = None,depth_ref:Union[DepthRefsEnum,List[DepthRefsEnum]]=['md','tvd']):
        if correlations is None:
            correlations = self.correlations.keys()
            
        for f in correlations:
            self.correlations[f].estimate_midpoint(depth_ref)

        return None
    
    @validate_arguments
    def estimate_coordinate(self,survey: Survey,correlations=None, depth_ref:DepthRefsEnum='md'):
        if correlations is None:
            correlations = self.correlations.keys()
            
        for f in correlations:
            self.correlations[f].estimate_coordinate(survey,depth_ref=depth_ref)
            
        return None
    
    @validate_arguments
    def get_reference_depth(
        self,
        survey: Survey, 
        correlations=None,
        depth_ref:Union[InterpolatorsEnum,List[InterpolatorsEnum]] = [InterpolatorsEnum.md_to_tvd,InterpolatorsEnum.md_to_tvdss]
    ):
        
        if correlations is None:
            correlations = self.correlations.keys()
            
        for f in correlations:
            self.correlations[f].get_reference_depth(survey,depth_ref=depth_ref)   
            
        return None 
            
