from dataclasses import dataclass
from pydantic import BaseModel, Field, validator, PrivateAttr, validate_arguments
from typing import List, Dict, Union, Optional, Tuple
import numpy as np
import pandas as pd
import geopandas as gpd
from scipy.interpolate import interp1d
from enum import Enum
import folium
from folium.plugins import MarkerCluster, MeasureControl,MousePosition
import matplotlib.pyplot as plt
from plotly import graph_objects as go
from shapely.geometry import LineString
#Local imports
from .mincurve import min_curve_method, vtk_survey
from .interpolate import interpolate_deviation, interpolate_position
from .projection import projection_1d

class InterpolatorsEnum(str,Enum):
    md_to_tvd = 'md_to_tvd'
    md_to_tvdss = 'md_to_tvdss'
    tvd_to_md = 'tvd_to_md'
    tvd_to_tvdss = 'tvd_to_tvdss'
    tvdss_to_md = 'tvdss_to_md'
    tvdss_to_tvd = 'tvdss_to_tvd'

class DepthRefsEnum(str,Enum):
    md = 'md'
    tvd = 'tvd'
    tvdss = 'tvdss'
    
    
class Survey(BaseModel):
    md: Union[List[float], np.ndarray] = Field(...)
    inc: Union[List[float], np.ndarray] = Field(...)
    azi: Union[List[float], np.ndarray] = Field(...)
    tvd: Union[List[float], np.ndarray] = Field(...)
    tvdss: Union[List[float], np.ndarray] = Field(...)
    north_offset: Union[List[float], np.ndarray] = Field(...)
    east_offset: Union[List[float], np.ndarray] = Field(...)
    northing: Union[List[float], np.ndarray] = Field(...)
    easting: Union[List[float], np.ndarray] = Field(...)
    dleg: Union[List[float], np.ndarray] = Field(...)
    fields: Optional[Dict[str,List[Union[float,str]]]] = Field(None)
    crs: Optional[int] = Field(None, gt=0) 
    _interpolators: Dict[InterpolatorsEnum,interp1d] = PrivateAttr({})
    
    def __repr__(self) -> str:
        return (f'Survey:\n'
            f'Number of Points: {len(self.md)}\n'
            f'Max Depth: {np.max(self.md)}\n'
            f'Max TVD: {np.max(self.tvd)}\n'
            f'Max Inclination: {np.max(self.inc)}\n'
            f'Crs Code: {self.crs}\n')
        
    
    
    @validator('md')
    def check_array_pressures_order(cls, v):
        v_array = np.array(v)
        diff = np.diff(v_array)
        if not np.all(diff>0):
            raise ValueError('Md must be increasing order')
        if not np.all(v_array>=0):
            raise ValueError('Md must be postive')
        return v
    
    class Config:
        extra = 'forbid'
        validate_assignment = True
        underscore_attrs_are_private = True
        arbitrary_types_allowed = True
        json_encoders = {np.ndarray: lambda x: x.tolist()}
        
    def df(
        self,
        projection:bool=False,
        azi: Optional[float]=90,
        center: Optional[Tuple[float,float]] = None,
        to_crs:int=None,
        horizontal_distance:bool=False
    ):
        surv_dict = self.dict()
        fields = surv_dict.pop('fields',None)
        
        if fields is not None:
            surv_dict.update(fields)
            
        _gdf = gpd.GeoDataFrame(
            surv_dict, 
            geometry=gpd.points_from_xy(surv_dict['easting'],surv_dict['northing'])
        )
        _gdf.crs = self.crs
        
        if to_crs:
            _gdf = _gdf.to_crs(to_crs)

        if projection == True:
            _pr,c = projection_1d(_gdf[['easting','northing']].values, azi, center=center)
            _gdf['projection'] = _pr
            
        if horizontal_distance == True:
            shifted_geo = _gdf[['geometry']].shift(periods=1)
            _gdf['h_distance'] = _gdf['geometry'].distance(shifted_geo).fillna(0)
            _gdf['h_distance_cum'] = _gdf['h_distance'].cumsum()
        return _gdf
    
    def td_md(self):
        return np.array(self.md).max()
    
    def td_tvd(self):
        return np.array(self.tvd).max()
    
    def plot_projection(
        self,
        azi: Optional[float]=90,
        center: Optional[Tuple[float,float]] = None,
        to_crs:int=None,
        ax=None
    ):
        df = self.df(projection=True,azi=azi,center=center,to_crs=to_crs)
        sax = ax or plt.gca()
        sax.plot(df['projection'],df['tvdss'])
        return sax
        
    @classmethod
    def make_vertical(
        cls,
        td,
        surface_northing=0,
        surface_easting=0, 
        rte = 0,
        n=2,
        crs=None
    ):
        dict_params = {}
        dict_params['md'] = np.linspace(0,td,n)
        dict_params['inc'] = np.zeros(n)
        dict_params['azi'] = np.zeros(n)
        dict_params['tvd'] = np.linspace(0,td,n)
        dict_params['tvdss'] = (dict_params['tvd'] - rte)*-1
        dict_params['north_offset'] = np.zeros(n)
        dict_params['east_offset'] = np.zeros(n)
        dict_params['northing'] = np.full(n,surface_northing)
        dict_params['easting'] =  np.full(n,surface_easting)
        dict_params['dleg'] = np.zeros(n)
        dict_params['crs'] = crs
        
        return cls(**dict_params)
        
        
    @classmethod
    def from_deviation(
        cls,
        df:pd.DataFrame=None, 
        md:Union[str,list,np.ndarray, pd.Series]='md',
        azi:Union[str,list,np.ndarray, pd.Series]='azi',
        inc:Union[str,list,np.ndarray, pd.Series]='inc',
        surface_northing:float=0,
        surface_easting:float=0, 
        rte:float=0, 
        crs=None
    ):
        
        dev_dict = {}
        for i,name in zip([md,azi,inc],['md','azi','inc']):
            if isinstance(i,str):
                _var = df[i].values
            else:
                _var = np.atleast_1d(i)
            dev_dict[name] = _var
            
        gdf = min_curve_method(
            dev_dict['md'],
            dev_dict['inc'],
            dev_dict['azi'],
            surface_northing=surface_northing,
            surface_easting=surface_easting,
            rte=rte,
            crs = crs
        )
        
        use_cols = ['md','inc','azi','tvd','tvdss','north_offset','east_offset','northing','easting','dleg']
        dict_params = gdf[use_cols].to_dict('list')
        dict_params['crs'] = crs
        return cls(**dict_params)
    
    def horizontal_length(self):
        return LineString(self.df()['geometry'].tolist()).length
    
    @classmethod
    def from_position(
        cls,
        df:pd.DataFrame=None, 
        md:Union[str,list,np.ndarray, pd.Series]='md',
        tvd:Union[str,list,np.ndarray, pd.Series]='tvd',
        northing:Union[str,list,np.ndarray, pd.Series]='northing',
        easting: Union[str,list,np.ndarray, pd.Series]='easting',
        surface_northing:float=0,
        surface_easting:float=0,
        rte:float=0, 
        crs=None
    ):
        
        pos_dict = {}
        for i,name in zip([md,tvd,northing,easting],['md','tvd','northing','easting']):
            if isinstance(i,str):
                _var = df[i].values
            else:
                _var = np.atleast_1d(i)
            pos_dict[name] = _var
            
        pos_df = pd.DataFrame(pos_dict)
        cols_dif = ['md','tvd','northing','easting']
        new_cols_dif = ['diff_'+i for i in cols_dif]
        pos_df[new_cols_dif] = pos_df[cols_dif].diff()

        pos_df['inc'] = np.degrees(np.arccos(pos_df['diff_tvd']/pos_df['diff_md']))
        pos_df['angle'] = np.degrees(np.arctan2(pos_df['diff_northing'],pos_df['diff_easting']))
        pos_df['azi'] = np.where(pos_df['angle']>90,450 - pos_df['angle'],90-pos_df['angle'])
        pos_df.fillna(0,inplace=True)
        gdf = min_curve_method(
            pos_df['md'],
            pos_df['inc'],
            pos_df['azi'],
            surface_northing=surface_northing,
            surface_easting=surface_easting,
            rte=rte,
            crs = crs
        )
        
        use_cols = ['md','inc','azi','tvd','tvdss','north_offset','east_offset','northing','easting','dleg']
        dict_params = gdf[use_cols].to_dict('list')
        dict_params['crs'] = crs
        return cls(**dict_params)

    
    @validate_arguments(config=dict(arbitrary_types_allowed=True))
    def sample_deviation(
        self,
        step:Optional[float]=100, 
        min_depth:Optional[float]=None, 
        max_depth:Optional[float]=None,
        depth_ref:str='md',
        depth_array:Optional[np.ndarray]=None
    )->pd.DataFrame:

        _survey = self.df()
        
        if min_depth is not None:
            _survey = _survey.loc[_survey[depth_ref]>=min_depth]

        if max_depth is not None:
            _survey = _survey.loc[_survey[depth_ref]<=max_depth] 
                
        return interpolate_deviation(
            _survey['md'].values, 
            _survey['inc'].values, 
            _survey['azi'].values, 
            md_step=step,
            md_array=depth_array
        )           

    @validate_arguments(config=dict(arbitrary_types_allowed=True))
    def sample_survey(
        self,          
        step:Optional[float]=100, 
        min_depth:Optional[float]=None, 
        max_depth:Optional[float]=None,
        depth_ref:str='md',
        depth_array:Optional[np.ndarray]=None
    ):
        
        new_dev = self.sample_deviation(
            step = step,
            min_depth = min_depth,
            max_depth = max_depth,
            depth_ref = depth_ref,
            depth_array=depth_array
        )
        
        if min_depth is not None:
            coord = self.coord_interpolate(
                values=new_dev['new_md'].iloc[0],
                depth_ref='md'
            )
            
            easting = coord['geometry'].iloc[0].x
            northing = coord['geometry'].iloc[0].y
        else:
            easting = self.easting[0]
            northing = self.northing[0]
        
        return Survey.from_deviation(
            new_dev,
            md = 'new_md',
            inc = 'new_inc',
            azi = 'new_azi',
            surface_easting=easting,
            surface_northing=northing,
            crs=self.crs
        )
        
    
    @validate_arguments
    def sample_depth(
        self,          
        step:float=100, 
        min_depth:Optional[float]=None, 
        max_depth:Optional[float]=None,
        depth_ref:str='md'
    ):
        
        _survey = self.df()
        
        if min_depth is not None:
            _survey = _survey.loc[_survey[depth_ref]>=min_depth]

        if max_depth is not None:
            _survey = _survey.loc[_survey[depth_ref]<=max_depth]
            
        new_pos = interpolate_position(
            _survey['tvd'], 
            _survey['easting'], 
            _survey['northing'], 
            tvd_step=step
        )
        
        new_pos['new_md'] = self.depth_interpolate(
            values=new_pos['new_tvd'].values,
            mode = 'tvd_to_md'    
        )
        
        
        
        return gpd.GeoDataFrame(
            new_pos,
            geometry=gpd.points_from_xy(new_pos.new_easting,new_pos.new_northing),
            crs=self.crs
        )
    
    @validate_arguments
    def sample_position(
        self,
        step:float = 100,
        
    ):
        surv = self.df(
            horizontal_distance=True
        )
        
        sample = np.arange(
            surv['h_distance_cum'].min(),
            surv['h_distance_cum'].max()+step,
            step
        )
        sample[-1] = surv['h_distance_cum'].max()
        
        inter = interp1d(
            surv['h_distance_cum'],
            surv['md'],
            fill_value='extrapolate'
        )(sample)
        
        return self.sample_survey(
            step=None,
            depth_array=inter
        )
        
        
        
    
    @validate_arguments(config=dict(arbitrary_types_allowed=True))
    def depth_interpolate(
        self,
        values:Union[float,List[float],np.ndarray]=None,
        mode:InterpolatorsEnum=InterpolatorsEnum.md_to_tvd
    ):
        if self._interpolators is None or mode.value not in self._interpolators:
            str_split = mode.value.split('_')
            _survey=self.df()
            self._interpolators[mode.value] = interp1d(_survey[str_split[0]],_survey[str_split[2]],fill_value='extrapolate')

        if values is None:
            return self._interpolators[mode.value](self.df()['md'])
        else:
            return self._interpolators[mode.value](np.atleast_1d(values))     
    
    @validate_arguments
    def coord_interpolate(
        self,
        values:Union[float,List[float]]=None,
        depth_ref:DepthRefsEnum=DepthRefsEnum.md,
    ):

        if depth_ref != DepthRefsEnum.tvd:
            values_tvd = self.depth_interpolate(values = values, mode = f'{depth_ref.value}_to_tvd')
        else:
           
            values_tvd = np.atleast_1d(values)

        if any([self._interpolators is None,'tvd_easting' not in self._interpolators]):
            _survey=self.df()
            self._interpolators['tvd_easting'] = interp1d(_survey['tvd'],_survey['easting'],fill_value='extrapolate')
            self._interpolators['tvd_northing'] = interp1d(_survey['tvd'],_survey['northing'],fill_value='extrapolate')

        if values is None:
            easting = self._interpolators['tvd_easting'](self.df()['tvd'])
            northing = self._interpolators['tvd_northing'](self.df()['tvd'])
        else:

            easting = self._interpolators['tvd_easting'](values_tvd)
            northing = self._interpolators['tvd_northing'](values_tvd)
        
                
        return gpd.GeoDataFrame(
            geometry=gpd.points_from_xy(easting,northing),
            crs = self.crs
        )
        
    def get_vtk(self, to_crs = None):
    
        _survey = self.df()
        
        if to_crs:
            _survey = _survey.to_crs(to_crs)
            
        _survey['x'] = _survey['geometry'].x
        _survey['y'] = _survey['geometry'].y
            
        surv_vtk = vtk_survey(_survey[['x','y','tvdss']].values)
        
        for col in _survey.iteritems():
            surv_vtk.point_data[col[0]] = col[1].values

        return surv_vtk
    
    def survey_map(
        self,
        zoom:int=10,
        map_style:str = 'OpenStreetMap',
        tooltip:bool=True,
        popup:bool=False,
        ax=None,
        radius=10
    ):

        _coord = self.df()
        _coord = _coord.to_crs('EPSG:4326')
        _coord['lon'] = _coord['geometry'].x
        _coord['lat'] = _coord['geometry'].y
        center = _coord[['lat','lon']].mean(axis=0)
        
        #make the map
        if ax is None:
            map_folium = folium.Map(
                location=(center['lat'],center['lon']),
                zoom_start=zoom,
                tiles = map_style)
        else:
            assert isinstance(ax,folium.folium.Map)
            map_folium = ax
            
        for i, r in _coord.iterrows():
            folium.Circle(
                [r['lat'],r['lon']],
                tooltip=f"md:{r['md']} <br>tvd:{r['tvd']} <br>tvdss:{r['tvdss']} <br>inc:{r['inc']} " if tooltip else None,
                popup = folium.Popup(html=f"<br>md:{r['md']} <br>tvd:{r['tvd']} <br>tvdss:{r['tvdss']} <br>inc:{r['inc']} ",show=True,max_width='50%') if popup else None,
                #icon=folium.Icon(icon='circle',prefix='fa', color='green'),
                radius=radius
                ).add_to(map_folium)

        folium.LayerControl().add_to(map_folium)
        #LocateControl().add_to(map_folium)
        MeasureControl().add_to(map_folium)
        MousePosition().add_to(map_folium)

        return map_folium
    
    def trace3d(
        self, 
        area_unit='m', 
        depth_unit='ft',
        name='survey',
        mode = 'lines',
        **kwargs
    ):
        
        df = self.df()
        
        coef_area = 1 if area_unit == 'm' else 3.28084
        coef_depth = 1 if depth_unit == 'ft' else 0.3048
        
        trace = go.Scatter3d(
            x = df['easting'] * coef_area,
            y = df['northing'] * coef_area,
            z = df['tvdss'] * coef_depth,
            hoverinfo = 'all',
            mode = mode,
            name = name,
            **kwargs
        )
        
        return trace
    
    def plot3d(
        self, 
        area_unit='m', 
        depth_unit='ft',
        name='survey',
        mode = 'lines',
        title = 'Survey',
        trace_kw = {},
        width = 800,
        height = 600,
        **kwargs
    ):
        
        traces = self.trace3d(
            area_unit=area_unit,
            depth_unit=depth_unit,
            name = name,
            mode = mode,
            **trace_kw
        )
        
        layout = go.Layout(
            title = title,
            scene = {
                'xaxis': {'title': 'Easting'},
                'yaxis': {'title': 'Northing'},
                'zaxis': {'title': 'TVDss'}
            },
            width = width,
            height = height,
            **kwargs
        )
        
        return go.Figure(data=[traces],layout=layout)
            

