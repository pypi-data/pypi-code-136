from dataclasses import field
from textwrap import indent
from fieldspy.wells.projection import projection_1d
from pydantic import BaseModel, Field, validate_arguments, validator, parse_obj_as
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
from typing import Tuple, Dict, List, Optional, Union
from shapely.geometry import Point
from lasio import LASFile
from wellschematicspy import WellSchema
import folium
from folium.plugins import MeasureControl, MousePosition
from scipy.spatial import distance_matrix, Delaunay
import seaborn as sns
import pyvista as pv
from sqlalchemy.engine.base import Engine
from plotly import graph_objects as go
from datetime import date
import os
#local imports
from .survey import Survey
from .perforations import Perforations, Perforation
from .correlation import Correlations
from .formations import  Formations, Formation
from .units import Units, Unit
from .tools import Tool, Tools
from .log import Las
from .geo_utils import create_voronoi, create_voronoi_grid
from .production import FormatEnum, Production, FormatEnum
from .pressures import Pressures
# Folium Colors available
folium_color_list = ['red', 'blue', 'green', 'purple', 'orange', 'darkred',
    'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue', 'darkpurple', 
    'white', 'pink', 'lightblue', 'lightgreen', 'gray', 'black', 'lightgray']


class Well(BaseModel):
    name: str = Field(...)
    uwi: str = Field(None)
    symbol: str = Field(None)
    #surface_coordinate: Union[Tuple[float,float],Point, Dict[str,float]] = Field(None)
    surface_x: float = Field(None)
    surface_y: float = Field(None)
    crs: int = Field(None)
    rte: float = Field(0.0)
    gle: float = Field(None)
    td_md: float = Field(None)
    td_tvd: float = Field(None)
    spud_date: date = Field(None)
    completion_date:date = Field(None)
    abandon_date: date = Field(None)
    survey: Survey = Field(None)
    logs: Dict[str,Las] = Field(None)
    diagram: Dict[str,WellSchema] = Field(None)
    formations: Formations = Field(None)
    units: Units = Field(None)
    tools: Tools = Field(None)
    perforations: Perforations = Field(None)
    production: Production = Field(None)
    pressures: Pressures = Field(None)
    fields: Dict[str,Union[float,int,str,date]] = Field(None)
    
    class Config:
        extra = 'ignore'
        validate_assignment = True
        underscore_attrs_are_private = True
        arbitrary_types_allowed = True
        json_encoders = {  
            LASFile: lambda x: x.to_json(),
            np.ndarray: lambda x: x.tolist(),
            pd.Period: lambda x: x.strftime('%Y-%m-%d')
            
        }

    def __str__(self):
        return self.well_head().T.dropna().astype(str).reset_index().to_string()

    def __repr__(self) -> str:
        return self.__str__()
    
   
    # @validator('surface_coordinate',always=True)
    # def get_surf_coord(cls, v):
    #     if isinstance(v,tuple):
    #         return Point(v[0],v[1])
    #     elif isinstance(v,dict):
    #         return Point(v['x'],v['y'])
    #     return v

    @validate_arguments
    def get_wellid(self, lenght:int=10, character: str = '0', first:str = 'W'):
        well_str = self.name.upper().rjust(lenght,character)
        well_str = well_str.replace(character, first,1)
        return well_str


    @validate_arguments(config=dict(arbitrary_types_allowed=True))
    def survey_from_deviation(self,df:pd.DataFrame, md:str=None,inc:str=None,azi:str=None):
        surv = Survey.from_deviation(
            df=df,
            md=md,
            inc=inc, 
            azi=azi,
            surface_northing=self.surface_y,
            surface_easting=self.surface_x,
            crs=self.crs,
            rte = self.rte
        )
        self.survey = surv
    
    @validate_arguments(config=dict(arbitrary_types_allowed=True))
    def add_logs(self, logs: Dict[str,Las]):
        if self.logs:
            self.logs.update(logs)
        self.logs = logs

    @validate_arguments
    def add_diagram(self, diagrams: Dict[str,WellSchema]):
        if self.diagram:
            self.diagram.update(diagrams)
        else:
            self.diagram = diagrams
    
    @validate_arguments
    def add_formations(self, formations: Union[Formation,List[Formation],Dict[str,Formation]]):
        if self.formations:
            self.formations.add_formations(formations)
        else:
            fm = Formations().add_formations(formations)
            self.formations = fm
        
    @validate_arguments
    def add_units(self, units: Union[Unit,List[Unit],Dict[str,Unit]]):
        if self.units:
            self.units.add_units(units)
        else:
            un = Units().add_units(units)
            self.units = un
        
    @validate_arguments
    def add_tools(self, tools: Union[Tool,List[Tool],Dict[str,Tool]]):
        if self.tools:
            self.tools.add_tools(tools)
        else:
            toolss = Tools().add_tools(tools)
            self.tools = tools
        
    @validate_arguments
    def add_perforations(self, perforations: Union[Perforation,List[Perforation],Dict[str,Perforation]]):
        if self.perforations:
            self.perforations.add_perforations(perforations)
        else:
            perf = Perforations().add_perforations(perforations)
            self.perforations = perf
    
    @validate_arguments
    def well_map(self,zoom:int=10, map_style:str = 'OpenStreetMap', to_crs:int=4326, tooltip:bool=False,popup:bool=True, ax=None):
        """
        Make a Foluim map with the selected well

        Input:
            zoom -> (int, float) Initial zoom for folium map
            map_stule -> (str) Type of map folium
        Return:
            w_map -> (folium.Map) Folium map object
        """
        _coord = gpd.GeoDataFrame()

        x_coord = self.surface_x
        y_coord = self.surface_y
        geometry = Point(x_coord,y_coord)
        crs = self.crs
        _w = gpd.GeoDataFrame({'x':[x_coord],'y':[y_coord],'geometry':[geometry]}, index=[self.name])
        _w.crs = crs
        _w = _w.to_crs(to_crs)
        _w['lon'] = _w['geometry'].x
        _w['lat'] = _w['geometry'].y
        _coord = _coord.append(_w)
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
            folium.Marker(
                [r['lat'],r['lon']],
                tooltip=f"{i}" if tooltip else None,
                popup = folium.Popup(html=f"{i}",show=True) if popup else None,
                icon=folium.Icon(icon='tint', color='green')
                ).add_to(map_folium)

        folium.LayerControl().add_to(map_folium)
        #LocateControl().add_to(map_folium)
        MeasureControl().add_to(map_folium)
        MousePosition().add_to(map_folium)

        return map_folium
    
    def describe(self):
        dict_attr = {
            #'surface_coordinate': True if self.surface_coordinate else False,
            'surface_x': True if self.surface_x else False,
            'surface_y': True if self.surface_y else False,
            'crs': True if self.crs else False,
            'rte': True if self.rte else False,
            'survey': True if self.survey else False,
            'logs': True if self.logs else False,
            'diagram': True if self.diagram else False,
            'formations': True if self.formations else False,
            'units': True if self.units else False,
            'tools': True if self.tools else False,
            'perforations': True if self.perforations else False,
            'pressures':True if self.pressures else False,
            'td_md': True if self.td_md else False,
            'td_tvd': True if self.td_tvd else False         
        }
        
        if self.fields is not None:
            for f in self.fields:
                dict_attr[f] = True
        
        
        return pd.Series(dict_attr, name=self.name)
    
    def well_head(self,to_crs:int=None,c:float=0.3028):
        if to_crs is None:
            to_crs = self.crs
        _w = gpd.GeoDataFrame({
            'z':[self.rte * c],
            'rte':[self.rte],
            'geometry':[Point(self.surface_x,self.surface_y)],
            'td_md':[self.td_md],
            'td_tvd':[self.td_tvd]            
        }, index=[self.name])
        cols_fields = []
        if self.fields is not None:
            for f in self.fields:
                _w[f] = [self.fields[f]]
                cols_fields.append(f)
                
        _w.crs = self.crs
        
        _w = _w.to_crs(to_crs)

        _w['x'] = _w['geometry'].x
        _w['y'] = _w['geometry'].y
        _w['crs'] = to_crs
        
        #converto to wsg
        _wsg = _w.to_crs(4326)
        _w['lon'] = _wsg['geometry'].x
        _w['lat'] = _wsg['geometry'].y
        
        cols = ['x','y','z','rte','crs','geometry','lon','lat','td_md','td_tvd']
        _w.index.name='well'
        #_w = _w.round(1)
        return _w[cols + cols_fields]

    
class Wells(BaseModel):
    name: Optional[str] = Field(None)
    wells: Dict[str,Well] = Field(...)
    
    class Config:
        extra = 'ignore'
        validate_assignment = True
        underscore_attrs_are_private = True
        arbitrary_types_allowed = True
        json_encoders = {
            Point: lambda x: {'x': x.x, 'y': x.y},   
            LASFile: lambda x: x.to_json(),
            np.ndarray: lambda x: x.tolist(),
            pd.Period: lambda x: x.strftime('%Y-%m-%d')
        }
    
    def __str__(self):
        return f'Wells Name: {self.name if self.name is not None else "Name not set"}\nWells: {len(self.wells) if self.wells is not None else "Empty"}'
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __getitem__(self, key):
        if isinstance(key, str):
            return self.wells[key]
        elif isinstance(key, (int,slice)):
            return list(self.wells.values())[key]
        else:
            raise KeyError(key)
    
    def __len__(self):
        return 0 if self.wells is None else len(self.wells)
    
    def __iter__(self):
        return (self.wells[w] for w in self.wells)
    
    def wells_list(self):
        return list(self.wells.keys())
    
    @validate_arguments(config=dict(arbitrary_types_allowed=True))
    def wells_filter(
        self,
        wells: Optional[Union[str,List[str]]] = None,
        field: Optional[Dict] = None
    ):
        
        list_wells = []
        if isinstance(wells,str):
            list_wells.append(wells)
        elif isinstance(wells,list):
            list_wells.extend(wells)
        else:
            list_wells.extend(list(self.wells.keys()))
            
        if field is None:
            return list_wells
        
        list_wells_filtered_full = []
        #for loop fields filter
        for f in field:
            # for loop wells allowed
            list_wells_filtered = []
            for w in list_wells:
                #if field in filter not in well object continue
                if f not in self.wells[w].fields:
                    continue
                # if field filter is a list check if well object field is in list
                if isinstance(field[f],list):
                    if self.wells[w].fields[f] not in field[f]:
                        continue
                # if field filter is a dict apply operators lt, le, gt, ge, eq, ne
                elif isinstance(field[f],dict):
                    if 'lt' in field[f]:
                        if self.wells[w].fields[f] < field[f]['lt']:
                            pass
                        else:
                            continue
                    if 'le' in field[f]:
                        if self.wells[w].fields[f] <= field[f]['le']:
                            pass
                        else:
                            continue
                    if 'gt' in field[f]:
                        if self.wells[w].fields[f] > field[f]['gt']:
                            pass
                        else:
                            continue
                    if 'ge' in field[f]:
                        if self.wells[w].fields[f] >= field[f]['ge']:
                            pass
                        else:
                            continue
                    if 'eq' in field[f]:
                        if self.wells[w].fields[f] == field[f]['eq']:
                            pass
                        else:
                            continue
                    if 'ne' in field[f]:
                        if self.wells[w].fields[f] != field[f]['ne']:
                            pass
                        else:
                            continue
                else:
                    if self.wells[w].fields[f] != field[f]:
                        continue
                    
                list_wells_filtered.append(w)
            list_wells_filtered_full.append(list_wells_filtered)
        
        return list(set.intersection(*map(set, list_wells_filtered_full)))         

    def sample_wells(self, n:int, seed:Optional[int] = None):
        rng = np.random.default_rng(seed)
        return rng.choice(list(self.wells.keys()), n, replace=False).tolist()
    
    def add_wells(self, wells: Dict[str,Well]):
        if self.logs:
            self.logs.update(wells)
        self.logs = wells
        
    def describe(self):
        list_series = []
        for well in self.wells:
            list_series.append(self.wells[well].describe())
        descr_df = pd.concat(list_series, axis=1).T.fillna(False)
        return descr_df
    
    @classmethod
    def from_well_heads(
        cls,
        df:pd.DataFrame,
        name:str=None,
        fields=None,
        **kwargs
    ):
        df = df.copy()
               
        if name:
            df['name'] = df[name].copy()
            df = df.set_index(name)
        else:
            df['name'] = df.index
            
        #To change columns name to match Object
        if bool(kwargs):
            kwargs = {v: k for k, v in kwargs.items()}
            df = df.rename(columns=kwargs)
            
        if fields is not None:
            fields_dict = df[fields].to_dict(orient='index')
            df.drop(fields,axis=1,inplace=True)
            
            wells_dict = df.to_dict(orient='index')
            
            for well in fields_dict:
                wells_dict[well].update({'fields':fields_dict[well]})
        else:
            wells_dict = df.to_dict(orient='index')
        
        return cls(name=name, wells=parse_obj_as(Dict[str,Well],wells_dict))
    
    def formations_list(
        self,
        wells:Optional[Union[str,List[str]]]=None
    ):
    
        list_wells = []
        if isinstance(wells,str):
            list_wells.append(wells)
        elif isinstance(wells,list):
            list_wells.extend(wells)
        else:
            list_wells.extend(list(self.wells.keys()))

        gdf_formations_list = []
        for well in list_wells:
            if self.wells[well].formations is None:
                continue
            gf = self.wells[well].formations
            
            gdf_formations_list.extend(gf.formations_list())
        
        return np.unique(gdf_formations_list).tolist()
            
        
    
    @validate_arguments
    def formations(
        self, 
        wells:Optional[Union[str,List[str]]]=None,
        formations:Optional[Union[str,List[str]]]=None,
        projection:Optional[bool]=False,
        azi: Optional[float]=90,
        center: Optional[Tuple[float,float]] = None,
        estimate_midpoint:bool=False,
        midpoint_weights_column:Optional[str]='md_tick',
        midpoint_name:str='midpoint',
        record_midpoint:bool=False
    ):
        list_wells = []
        if isinstance(wells,str):
            list_wells.append(wells)
        elif isinstance(wells,list):
            list_wells.extend(wells)
        else:
            list_wells.extend(list(self.wells.keys()))
           
        gdf_formations_list = []
        for well in list_wells:
            if self.wells[well].formations is None:
                continue
            gf = self.wells[well].formations

            #! TODO: Verify if the calculation were already made
            if self.wells[well].survey:
                gf.get_reference_depth(self.wells[well].survey)
                gf.estimate_ticks()
                gf.estimate_coordinate(self.wells[well].survey)
            
            if record_midpoint:
                gf.estimate_midpoints(formations=formations)

            #Estimate Mid point
            if estimate_midpoint:
                try:
                    gf.estimate_average_midpoint(
                        formations=formations,
                        weights=midpoint_weights_column,
                        name = midpoint_name
                    )
                except:
                    pass            


            gdf = gf.df()
            gdf['well'] = self.wells[well].name
            gdf_formations_list.append(gdf)
        
        if len(gdf_formations_list) == 0:
            raise ValueError('No formations found')
        gdf_formations = gpd.GeoDataFrame(
            pd.concat(gdf_formations_list),
            crs=gdf_formations_list[0].crs
        )

        if formations:
            gdf_formations = gdf_formations.loc[formations]
        
        _pr = None
        if projection:
            _pr,c = projection_1d(
                gdf_formations[['easting','northing']].values, 
                azi, 
                center=center
            )
            gdf_formations['projection'] = _pr
        
        gdf_formations.set_index('well',append=True,inplace=True)        
        return gdf_formations
    
    @validate_arguments
    def formations_voronoi(
        self, 
        wells:Optional[Union[str,List[str]]]=None,
        formations:Optional[Union[str,List[str]]]=None,
        projection:Optional[bool]=False,
        azi: Optional[float]=90,
        center: Optional[Tuple[float,float]] = None,
        estimate_midpoint:bool=False,
        midpoint_weights_column:Optional[str]='md_tick',
        midpoint_name:str='midpoint',
        xscale: float = 1.1,
        yscale: float = 1.1,
    ):
        
        gdf = self.formations(
            wells = wells,
            formations = formations,
            projection = projection,
            azi = azi,
            center = center,
            estimate_midpoint = estimate_midpoint,
            midpoint_weights_column=midpoint_weights_column,
            midpoint_name=midpoint_name
        ).reset_index()
        
        gdf_list = []
        for fm in gdf['formation'].unique():
            gfm = gdf.loc[gdf['formation'] == fm]
            
            vor_gdf = create_voronoi(geom = gfm, xscale=xscale, yscale=yscale)
            gdf_list.append(vor_gdf)
        
        return gpd.GeoDataFrame(pd.concat(gdf_list,axis=0), crs=gdf.crs)

    @validate_arguments
    def formations_voronoi_grid(
        self, 
        wells:Optional[Union[str,List[str]]]=None,
        formations:Optional[Union[str,List[str]]]=None,
        projection:Optional[bool]=False,
        azi: Optional[float]=90,
        center: Optional[Tuple[float,float]] = None,
        estimate_midpoint:bool=False,
        midpoint_weights_column:Optional[str]='md_tick',
        midpoint_name:str='midpoint',
        xscale: float = 1.1,
        yscale: float = 1.1,
        dsol:float=1000
    ):
        
        gdf = self.formations(
            wells = wells,
            formations = formations,
            projection = projection,
            azi = azi,
            center = center,
            estimate_midpoint = estimate_midpoint,
            midpoint_weights_column=midpoint_weights_column,
            midpoint_name=midpoint_name
        ).reset_index()
        
        gdf_list = []
        for fm in gdf['formation'].unique():
            gfm = gdf.loc[gdf['formation'] == fm]
        
            polys = create_voronoi_grid(
                gfm,
                xscale=xscale,
                yscale=yscale,
                dsol=dsol
            )
        
            polys_merge = polys.sjoin(
                gfm,
                how='left',
                predicate = 'contains'
            )
            gdf_list.append(polys_merge)
        
        return gpd.GeoDataFrame(pd.concat(gdf_list,axis=0), crs=gdf.crs)
        
        
    def units_list(
        self,
        wells:Optional[Union[str,List[str]]]=None
    ):
    
        list_wells = []
        if isinstance(wells,str):
            list_wells.append(wells)
        elif isinstance(wells,list):
            list_wells.extend(wells)
        else:
            list_wells.extend(list(self.wells.keys()))

        gdf_units_list = []
        for well in list_wells:
            if self.wells[well].units is None:
                continue
            gf = self.wells[well].units
            
            gdf_units_list.extend(gf.units_list())
        
        return np.unique(gdf_units_list).tolist()
    
    @validate_arguments
    def units(
        self, 
        wells:Optional[Union[str,List[str]]]=None,
        units:Optional[Union[str,List[str]]]=None,
        projection:Optional[bool]=False,
        azi: Optional[float]=90,
        center: Optional[Tuple[float,float]] = None,
        estimate_midpoint:bool=False,
        midpoint_weights_column:Optional[str]='md_tick',
        midpoint_name:str='midpoint'
    ):
        list_wells = []
        if isinstance(wells,str):
            list_wells.append(wells)
        elif isinstance(wells,list):
            list_wells.extend(wells)
        else:
            list_wells.extend(list(self.wells.keys()))
           
        gdf_units_list = []
        for well in list_wells:
            if self.wells[well].units is None:
                continue
            gf = self.wells[well].units
            
            #Estimate Mid point
            if estimate_midpoint:
                try:
                    gf.estimate_average_midpoint(
                        units=units,
                        weights=midpoint_weights_column,
                        name = midpoint_name
                    )
                except:
                    pass
            if self.wells[well].survey:
                gf.get_reference_depth(self.wells[well].survey)
                gf.estimate_ticks()
                gf.estimate_coordinate(self.wells[well].survey)
            gdf = gf.df()
            gdf['well'] = self.wells[well].name
            gdf_units_list.append(gdf)

        if len(gdf_units_list) == 0:
            raise ValueError('No units found')
        gdf_units = gpd.GeoDataFrame(
            pd.concat(gdf_units_list),
            crs=gdf_units_list[0].crs
        )

        if units:
            gdf_units = gdf_units.loc[units]
        
        _pr = None
        if projection:
            _pr,c = projection_1d(
                gdf_units[['easting','northing']].values, 
                azi, 
                center=center
            )
            gdf_units['projection'] = _pr
            
        gdf_units.set_index('well',append=True,inplace=True) 
        return gdf_units
    
    @validate_arguments
    def units_voronoi(
        self, 
        wells:Optional[Union[str,List[str]]]=None,
        units:Optional[Union[str,List[str]]]=None,
        projection:Optional[bool]=False,
        azi: Optional[float]=90,
        center: Optional[Tuple[float,float]] = None,
        estimate_midpoint:bool=False,
        midpoint_weights_column:Optional[str]='md_tick',
        midpoint_name:str='midpoint',
        xscale: float = 1.1,
        yscale: float = 1.1,
    ):
        
        gdf = self.units(
            wells = wells,
            units = units,
            projection = projection,
            azi = azi,
            center = center,
            estimate_midpoint = estimate_midpoint,
            midpoint_weights_column=midpoint_weights_column,
            midpoint_name=midpoint_name
        ).reset_index()
        
        gdf_list = []
        for fm in gdf['unit'].unique():
            gfm = gdf.loc[gdf['unit'] == fm]
            
            vor_gdf = create_voronoi(geom = gfm, xscale=xscale, yscale=yscale)
            gdf_list.append(vor_gdf)
        
        return gpd.GeoDataFrame(pd.concat(gdf_list,axis=0), crs=gdf.crs)
    
    @validate_arguments
    def tools(
        self, 
        wells:Optional[Union[str,List[str]]]=None,
        tools:Optional[Union[str,List[str]]]=None,
        projection:Optional[bool]=False,
        azi: Optional[float]=90,
        center: Optional[Tuple[float,float]] = None,
        estimate_midpoint:bool=False,
        midpoint_weights_column:Optional[str]='md_tick',
        midpoint_name:str='midpoint'
    ):
        list_wells = []
        if isinstance(wells,str):
            list_wells.append(wells)
        elif isinstance(wells,list):
            list_wells.extend(wells)
        else:
            list_wells.extend(list(self.wells.keys()))
           
        gdf_tools = gpd.GeoDataFrame()
        for well in list_wells:
            if self.wells[well].tools is None:
                continue
            gf = self.wells[well].tools
            
            #Estimate Mid point
            if estimate_midpoint:
                try:
                    gf.estimate_average_midpoint(
                        tools=tools,
                        weights=midpoint_weights_column,
                        name = midpoint_name
                    )
                except:
                    pass
                
            if self.wells[well].survey:
                gf.get_reference_depth(self.wells[well].survey)
                gf.estimate_ticks()
                gf.estimate_coordinate(self.wells[well].survey)
            gdf = gf.df()
            gdf['well'] = self.wells[well].name
            gdf_tools = gdf_tools.append(gdf)

        if tools:
            gdf_tools = gdf_tools.loc[tools]
        
        _pr = None
        if projection:
            _pr,c = projection_1d(
                gdf_tools[['easting','northing']].values, 
                azi, 
                center=center
            )
            gdf_tools['projection'] = _pr
        
        gdf_tools.set_index('well',append=True,inplace=True)
        return gdf_tools
    
    @validate_arguments
    def tools_voronoi(
        self, 
        wells:Optional[Union[str,List[str]]]=None,
        tools:Optional[Union[str,List[str]]]=None,
        projection:Optional[bool]=False,
        azi: Optional[float]=90,
        center: Optional[Tuple[float,float]] = None,
        estimate_midpoint:bool=False,
        midpoint_weights_column:Optional[str]='md_tick',
        midpoint_name:str='midpoint',
        xscale: float = 1.1,
        yscale: float = 1.1,
    ):
        
        gdf = self.tools(
            wells = wells,
            tools = tools,
            projection = projection,
            azi = azi,
            center = center,
            estimate_midpoint = estimate_midpoint,
            midpoint_weights_column=midpoint_weights_column,
            midpoint_name=midpoint_name
        ).reset_index()
        
        gdf_list = []
        for fm in gdf['tool'].unique():
            gfm = gdf.loc[gdf['tool'] == fm]
            
            vor_gdf = create_voronoi(geom = gfm, xscale=xscale, yscale=yscale)
            gdf_list.append(vor_gdf)
        
        return gpd.GeoDataFrame(pd.concat(gdf_list,axis=0), crs=gdf.crs)
    
    @validate_arguments
    def formations_projection(
        self, 
        wells:Optional[Union[str,List[str]]]=None,
        formations:Optional[Union[str,List[str]]]=None,
        azi: Optional[float]=90,
        center: Optional[Tuple[float,float]] = None
    ):
        list_wells = []
        if isinstance(wells,str):
            list_wells.append(wells)
        elif isinstance(wells,list):
            list_wells.extend(wells)
        else:
            list_wells.extend(list(self.wells.keys()))
           
        gdf_formations = gpd.GeoDataFrame()
        for well in list_wells:
            if self.wells[well].formations is None:
                continue            
            gf = self.wells[well].formations
            if self.wells[well].survey:
                gf.get_reference_depth(self.wells[well].survey)
                gf.estimate_ticks()
                gf.estimate_coordinate(self.wells[well].survey)
            gdf = gf.df()
            gdf['well'] = self.wells[well].name
            gdf_formations = gdf_formations.append(gdf)

        if formations:
            gdf_formations = gdf_formations.loc[formations]
            
        _pr,c = projection_1d(
            gdf_formations[['easting','northing']].values, 
            azi, 
            center=center
        )
        gdf_formations['projection'] = _pr
                
        return gdf_formations, c
    
    @validate_arguments
    def units_projection(
        self, 
        wells:Optional[Union[str,List[str]]]=None,
        units:Optional[Union[str,List[str]]]=None,
        azi: Optional[float]=90,
        center: Optional[Tuple[float,float]] = None
    ):
        list_wells = []
        if isinstance(wells,str):
            list_wells.append(wells)
        elif isinstance(wells,list):
            list_wells.extend(wells)
        else:
            list_wells.extend(list(self.wells.keys()))
           
        gdf_units = gpd.GeoDataFrame()
        for well in list_wells:
            if self.wells[well].units is None:
                continue            
            gf = self.wells[well].units
            if self.wells[well].survey:
                gf.get_reference_depth(self.wells[well].survey)
                gf.estimate_ticks()
                gf.estimate_coordinate(self.wells[well].survey)
            gdf = gf.df()
            gdf['well'] = self.wells[well].name
            gdf_units = gdf_units.append(gdf)

        if units:
            gdf_units = gdf_units.loc[units]
            
        _pr,c = projection_1d(
            gdf_units[['easting','northing']].values, 
            azi, 
            center=center
        )
        gdf_units['projection'] = _pr
                
        return gdf_units, c
    
    @validate_arguments
    def perforations_projection(
        self, 
        wells:Optional[Union[str,List[str]]]=None,
        perforations:Optional[Union[str,List[str]]]=None,
        azi: Optional[float]=90,
        center: Optional[Tuple[float,float]] = None
    ):
        list_wells = []
        if isinstance(wells,str):
            list_wells.append(wells)
        elif isinstance(wells,list):
            list_wells.extend(wells)
        else:
            list_wells.extend(list(self.wells.keys()))
           
        gdf_perforations = gpd.GeoDataFrame()
        for well in list_wells:
            if self.wells[well].perforations is None:
                continue            
            gf = self.wells[well].perforations
            if self.wells[well].survey:
                gf.get_reference_depth(self.wells[well].survey)
                gf.estimate_ticks()
                gf.estimate_coordinate(self.wells[well].survey)
            gdf = gf.df()
            gdf['well'] = self.wells[well].name
            gdf_perforations = gdf_perforations.append(gdf)

        if perforations:
            gdf_perforations = gdf_perforations.loc[perforations]
            
        _pr,c = projection_1d(
            gdf_perforations[['easting','northing']].values, 
            azi, 
            center=center
        )
        gdf_perforations['projection'] = _pr
                
        return gdf_perforations, c
    
    @validate_arguments
    def tools_projection(
        self, 
        wells:Optional[Union[str,List[str]]]=None,
        tools:Optional[Union[str,List[str]]]=None,
        azi: Optional[float]=90,
        center: Optional[Tuple[float,float]] = None
    ):
        list_wells = []
        if isinstance(wells,str):
            list_wells.append(wells)
        elif isinstance(wells,list):
            list_wells.extend(wells)
        else:
            list_wells.extend(list(self.wells.keys()))
           
        gdf_tools = gpd.GeoDataFrame()
        for well in list_wells:
            if self.wells[well].tools is None:
                continue            
            gf = self.wells[well].tools
            if self.wells[well].survey:
                gf.get_reference_depth(self.wells[well].survey)
                gf.estimate_ticks()
                gf.estimate_coordinate(self.wells[well].survey)
            gdf = gf.df()
            gdf['well'] = self.wells[well].name
            gdf_tools = gdf_tools.append(gdf)

        if tools:
            gdf_tools = gdf_tools.loc[tools]
            
        _pr,c = projection_1d(
            gdf_tools[['easting','northing']].values, 
            azi, 
            center=center
        )
        gdf_tools['projection'] = _pr
                
        return gdf_tools, c
    
    @validate_arguments
    def surveys(
        self, 
        wells:Optional[Union[str,List[str]]]=None,
        projection:Optional[bool]=False,
        azi: Optional[float]=90,
        center: Optional[Tuple[float,float]] = None,
        to_crs:int=None
    ):
        list_wells = []
        if isinstance(wells,str):
            list_wells.append(wells)
        elif isinstance(wells,list):
            list_wells.extend(wells)
        else:
            list_wells.extend(list(self.wells.keys()))
        
        surveys_gdf = gpd.GeoDataFrame()
        gdf_surveys_list = []
        for well in list_wells:
            if self.wells[well].survey is None:
                continue
            
            surv_gdf = self.wells[well].survey.df()
            if to_crs:
                surv_gdf = surv_gdf.to_crs(to_crs)
            surv_gdf['well'] = self.wells[well].name
            gdf_surveys_list.append(surv_gdf)

        surveys_gdf = gpd.GeoDataFrame(
            pd.concat(gdf_surveys_list),
            crs=gdf_surveys_list[0].crs
        )
            
        if projection == True:
            _pr,c = projection_1d(surveys_gdf[['easting','northing']].values, azi, center=center)
            surveys_gdf['projection'] = _pr
            
        return surveys_gdf

    @validate_arguments
    def surveys_ascii(
        self, 
        wells:Union[str,List[str]]=None, 
        factor=None, 
        cols:List[str]=['easting','northing','tvdss','md'],
        float_format='{:.2f}'.format
    ):
               
        wells_surveys_df = self.surveys(wells=wells)
             
        string = ""

        if factor is None:
            factor = np.ones(len(cols))
        else:
            factor = np.atleast_1d(factor)
            assert (factor.ndim==1) & (factor.shape[0]==len(cols))
        
        for w in wells_surveys_df['well'].unique():

            _df = wells_surveys_df.loc[wells_surveys_df['well']==w,cols] * factor
            string += f"WELLNAME: {w}\n"
            string += _df.to_string(header=False,index=False,float_format=float_format) + '\n'
        return string
    
    @validate_arguments
    def perforations(
        self, 
        wells:Optional[Union[str,List[str]]]=None,
        perforations:Optional[Union[str,List[str]]]=None,
        projection:Optional[bool]=False,
        azi: Optional[float]=90,
        center: Optional[Tuple[float,float]] = None,
        estimate_midpoint:bool=False,
        midpoint_weights_column:Optional[str]='md_tick',
        midpoint_name:str='midpoint'
    ):

        list_wells = []
        if isinstance(wells,str):
            list_wells.append(wells)
        elif isinstance(wells,list):
            list_wells.extend(wells)
        else:
            list_wells.extend(list(self.wells.keys()))
           
        gdf_perforations_list = []
        for well in list_wells:
            if self.wells[well].perforations is None:
                continue
            gf = self.wells[well].perforations
            
            #Estimate Mid point
            if estimate_midpoint:
                try:
                    gf.estimate_average_midpoint(
                        perforations=perforations,
                        weights=midpoint_weights_column,
                        name = midpoint_name
                    )
                except Exception as e:
                    print(e)
            
            if self.wells[well].survey:
                gf.get_reference_depth(self.wells[well].survey)
                gf.estimate_ticks()
                gf.estimate_midpoints()
                gf.estimate_coordinate(self.wells[well].survey)
            gdf = gf.df()
            gdf['well'] = self.wells[well].name
            gdf_perforations_list.append(gdf)

        if len(gdf_perforations_list) == 0:
            raise ValueError('No perforations found')
        gdf_perforations = gpd.GeoDataFrame(
            pd.concat(gdf_perforations_list),
            crs=gdf_perforations_list[0].crs
        )

        if perforations:
            gdf_perforations = gdf_perforations.loc[perforations]
        
        if projection:
            _pr,c = projection_1d(
                gdf_perforations[['easting','northing']].values, 
                azi, 
                center=center
            )
            gdf_perforations['projection'] = _pr
                
        return gdf_perforations
    
    def completion_length_timeline(
        self,
        wells:Optional[Union[str,List[str]]]=None,
        freq:str = 'M',
        fields:List = None,
        depth_ref = ['md']
    ):
        
        list_wells = []
        if isinstance(wells,str):
            list_wells.append(wells)
        elif isinstance(wells,list):
            list_wells.extend(wells)
        else:
            list_wells.extend(list(self.wells.keys()))
            
        df_list = []
        
        for w in list_wells:
            if self.wells[w].perforations is None:
                continue
            cl_df = self.wells[w].perforations.period_array_open(
                freq=freq,
                fields=fields,
                depth_ref=depth_ref
            )
            if cl_df is None:
                continue
            cl_df['well'] = w
            
            df_list.append(cl_df)
        
        if len(df_list) == 0:
            return None
        return pd.concat(df_list, axis=0)
            
    def open_midpoint_timeline(
        self,
        wells:Optional[Union[str,List[str]]]=None,
        freq:str = 'M',
        weights:str = None,
        fields:List = None,
        depth_ref = ['md']
    ):

        list_wells = []
        if isinstance(wells,str):
            list_wells.append(wells)
        elif isinstance(wells,list):
            list_wells.extend(wells)
        else:
            list_wells.extend(list(self.wells.keys()))
            
        df_list = []
        
        for w in list_wells:
            if self.wells[w].perforations is None:
                continue
            mp_df = self.wells[w].perforations.period_array_midpoint(
                freq = freq,
                weights=weights,
                depth_ref=depth_ref,
                fields = fields
            )
            if mp_df is None:
                continue
            mp_df['well'] = w
            df_list.append(mp_df)

        if len(df_list) == 0:
            return None
        return pd.concat(df_list, axis=0).reset_index().set_index(['index','well'])
        
    
    @validate_arguments
    def perforations_ascii(self,
        wells:Optional[List[str]]=None, 
        perforations:Optional[List[str]]=None,
        factor:Optional[float]=None, 
        cols:List[str]=['md_top','md_bottom'],
        float_format='{:.2f}'.format
    ):
        
        wells_perforations_df = self.perforations(
            wells=wells, 
            perforations=perforations
        ).reset_index()
             
        string = ""

        if factor is None:
            factor = np.ones(len(cols))
        else:
            factor = np.atleast_1d(factor)
            assert (factor.ndim==1) & (factor.shape[0]==len(cols))
            
        wells_perforations_df['completion'] = 'perforation'
        
        if 'date' not in wells_perforations_df.columns:
            wells_perforations_df['date'] = '"SOH"'
        else:
            wells_perforations_df['date'] = wells_perforations_df['date'].apply(lambda x: x.strftime('%Y-%m-%d').upper())
        
        if 'skin' not in wells_perforations_df.columns:
            wells_perforations_df['skin'] = 0

        if 'OH' not in wells_perforations_df.columns:
            wells_perforations_df['oh'] = 0.354           
        
        for w in wells_perforations_df['well'].unique():
            #_df = wells_perforations_df.loc[wells_perforations_df['well']==w,:]
            wells_perforations_df.loc[wells_perforations_df['well']==w,cols] = wells_perforations_df.loc[wells_perforations_df['well']==w,cols] * factor        
            
            string += f"WELLNAME {w}\n"
            cols_order = ['date','completion','md_top','md_bottom','oh','skin']
            string += wells_perforations_df.loc[wells_perforations_df['well']==w,cols_order].to_string(header=False,index=False,float_format=float_format) + '\n'
        return string
    
    @validate_arguments
    def well_heads(
        self, 
        wells:Optional[List[str]]=None, 
        to_crs:Optional[int]=None,
        c:float=0.3028
    ):
        
        list_wells = []
        if isinstance(wells,str):
            list_wells.append(wells)
        elif isinstance(wells,list):
            list_wells.extend(wells)
        else:
            list_wells.extend(list(self.wells.keys()))

        #Create coordinates dataframe
        _coord = []
        
        for well in list_wells:
            _w = self.wells[well].well_head(to_crs=to_crs,c=c)
            _coord.append(_w)
        
        df = gpd.GeoDataFrame(
            pd.concat(_coord, axis=0),
            crs = _coord[0].crs
        )
        
        return df
        
    @validate_arguments
    def wells_coordinates(
        self, 
        wells:Optional[List[str]]=None, 
        to_crs:Optional[int]=4326,
        c:float=0.3028
    ):


        list_wells = []
        if isinstance(wells,str):
            list_wells.append(wells)
        elif isinstance(wells,list):
            list_wells.extend(wells)
        else:
            list_wells.extend(list(self.wells.keys()))

        #Create coordinates dataframe
        _coord = gpd.GeoDataFrame()

        for well in list_wells:
            x_coord = self.wells[well].surface_x
            y_coord = self.wells[well].surface_y
            z_coord = self.wells[well].rte * c
            shape = Point(self.wells[well].surface_x,self.wells[well].surface_y)
            crs = self.wells[well].crs
            _w = gpd.GeoDataFrame({'x':[x_coord],'y':[y_coord],'z':[z_coord],'geometry':[shape]}, index=[well])
            _w.crs = crs
            _w = _w.to_crs(to_crs)
            _w['lon'] = _w['geometry'].x
            _w['lat'] = _w['geometry'].y
            _coord = _coord.append(_w)

        return _coord
    
    @validate_arguments
    def wells_distance(
        self,
        wells:Optional[List[str]]=None,
        dims: List[str] = ['x','y','z'],
        to_crs:int=None,
        stack:bool=False,     
        lt:Optional[float]=None,
        gt:Optional[float]=0.,
        le:Optional[float]=None,
        ge:Optional[float]=None,
        eq:Optional[float]=None,
        ne:Optional[float]=None,
        between:Optional[Tuple[float,float]]=None
    ):
        
        coords = self.well_heads(wells=wells,to_crs=to_crs)

        dist_array = distance_matrix(coords[dims].values,coords[dims].values)
        dist_matrix = pd.DataFrame(dist_array,index=coords.index.values, columns=coords.index.values)
        dist_matrix.index.name = 'well_row'
        dist_matrix.columns.name = 'well_column'
        
        locs = locals()
        if any([locs[i] is not None for i in ['lt','gt','le','ge','eq','ne','between']]):
            dist_matrix_s = dist_matrix.stack().reset_index()
            dist_matrix_s.columns = ['well_row','well_column','distance']
            
            filter_list = []
            for f in ['lt','gt','le','ge','eq','ne','between']:
                if locs[f] is None:
                    continue
                if f == 'between':
                    filter = eval(f"dist_matrix_s['distance'].{f}(*{locs[f]})")
                else:
                    filter = eval(f"dist_matrix_s['distance'].{f}({locs[f]})")
                filter_list.append(filter)
                
            fil_df = pd.concat(filter_list, axis=1).product(axis=1).astype(bool)
            dist_matrix_sf = dist_matrix_s.loc[fil_df,:]
            
            if stack:
                return dist_matrix_sf
            else:
                return dist_matrix_sf.pivot(index='well_row',columns='well_column',values='distance')
            
        if stack:
            dist_matrix = dist_matrix.stack().reset_index()
            dist_matrix.columns = ['well_row','well_column','distance']
            return dist_matrix
        return dist_matrix
    

    
    @validate_arguments
    def formation_distance(
        self,
        formation:str,
        wells:Optional[List[str]]=None,
        dims:list=['x','y','z'],
        stack:bool=False,
        lt:Optional[float]=None,
        gt:Optional[float]=0.,
        le:Optional[float]=None,
        ge:Optional[float]=None,
        eq:Optional[float]=None,
        ne:Optional[float]=None,
        between:Optional[Tuple[float,float]]=None
    ):
        coords = self.formations(wells=wells,formations=formation).reset_index()
        coords[['x','y']] = coords[['easting','northing']]
        coords['z'] = coords['tvdss_top']*0.3028

        dist_array = distance_matrix(coords[dims].values,coords[dims].values)
        dist_matrix = pd.DataFrame(dist_array,index=coords['well'], columns=coords['well'])
        dist_matrix.index.name = 'well_row'
        dist_matrix.columns.name = 'well_column'

        locs = locals()
        if any([locs[i] is not None for i in ['lt','gt','le','ge','eq','ne','between']]):
            dist_matrix_s = dist_matrix.stack().reset_index()
            dist_matrix_s.columns = ['well_row','well_column','distance']
            
            filter_list = []
            for f in ['lt','gt','le','ge','eq','ne','between']:
                if locs[f] is None:
                    continue
                if f == 'between':
                    filter = eval(f"dist_matrix_s['distance'].{f}(*{locs[f]})")
                else:
                    filter = eval(f"dist_matrix_s['distance'].{f}({locs[f]})")
                filter_list.append(filter)
                
            fil_df = pd.concat(filter_list, axis=1).product(axis=1).astype(bool)
            dist_matrix_sf = dist_matrix_s.loc[fil_df,:]
            
            if stack:
                return dist_matrix_sf
            else:
                return dist_matrix_sf.pivot(index='well_row',columns='well_column',values='distance')
            
        if stack:
            dist_matrix = dist_matrix.stack().reset_index()
            dist_matrix.columns = ['well_row','well_column','distance']
            return dist_matrix
        return dist_matrix
        
    
    @validate_arguments
    def wells_map(
      self,
      wells:Optional[List[str]]=None,
      zoom:int =10,
      map_style:str = 'OpenStreetMap',
      tooltip=True,
      popup=False,
      ax=None,
      crs:int = 4326,
      color:Union[str,Dict[str,str]] = 'green',
      hue:str = None,
      seed:int=21,
    ):
        
        coords = self.well_heads(wells=wells,to_crs = crs)
        center = coords[['lat','lon']].mean(axis=0)

        if ax is None:
            map_folium = folium.Map(
                location=(center['lat'],center['lon']),
                zoom_start=zoom,
                tiles = map_style)
        else:
            map_folium = ax
            
        if hue is None:
            coords['color'] = color
        else:
            if not isinstance(color,dict):
                unique_type = coords[hue].unique().tolist()
                rs = np.random.RandomState(seed)
                colors_type = rs.choice(folium_color_list,size=len(unique_type),replace=False)
                color = dict(zip(unique_type,colors_type))
            coords['color'] = coords[hue].map(color)
                

        for i, r in coords.iterrows():
            folium.CircleMarker(
                [r['lat'],r['lon']],
                tooltip=f"{i} {r[hue] if hue is not None else ''}" if tooltip else None,
                popup = folium.Popup(html=f"{i} {r[hue] if hue is not None else ''}",show=True,max_width='50%') if popup else None,
                fill = True,
                radius=5,
                color = r['color']
                #icon=folium.Icon(icon='tint', color=r['color'])
                ).add_to(map_folium)

        folium.LayerControl().add_to(map_folium)
        #LocateControl().add_to(map_folium)
        MeasureControl().add_to(map_folium)
        MousePosition().add_to(map_folium)

        return map_folium
    
    @validate_arguments
    def formations_map(
        self,
        wells:Optional[List[str]]=None,
        formations:Optional[List[str]]=None,
        zoom:int =10,
        map_style:str = 'OpenStreetMap',
        tooltip=True,
        popup=False,
        ax=None,
        crs:int = 4326, 
    ):
        
        coords = self.formations(wells=wells, formations=formations).reset_index()
        coords = coords.to_crs(crs)
        coords['lon'] = coords['geometry'].x
        coords['lat'] = coords['geometry'].y
        center = coords[['lat','lon']].mean(axis=0)
        
        if ax is None:
            map_folium = folium.Map(
                location=(center['lat'],center['lon']),
                zoom_start=zoom,
                tiles = map_style)
        else:
            map_folium = ax
            
        for i, r in coords.iterrows():
            folium.Marker(
                [r['lat'],r['lon']],
                tooltip=f"{r['well']} {r['formation']}" if tooltip else None,
                popup = folium.Popup(html=f"{r['well']} {r['formation']}",show=True,max_width='50%') if popup else None,
                icon=folium.Icon(icon='tint', color='green')
                ).add_to(map_folium)

        folium.LayerControl().add_to(map_folium)
        #LocateControl().add_to(map_folium)
        MeasureControl().add_to(map_folium)
        MousePosition().add_to(map_folium)

        return map_folium
    
    @validate_arguments
    def units_map(
        self,
        wells:Optional[List[str]]=None,
        units:Optional[List[str]]=None,
        zoom:int =10,
        map_style:str = 'OpenStreetMap',
        tooltip=True,
        popup=False,
        ax=None,
        crs:int = 4326, 
    ):
        
        coords = self.units(wells=wells, units=units).reset_index()
        coords = coords.to_crs(crs)
        coords['lon'] = coords['geometry'].x
        coords['lat'] = coords['geometry'].y
        center = coords[['lat','lon']].mean(axis=0)
        
        if ax is None:
            map_folium = folium.Map(
                location=(center['lat'],center['lon']),
                zoom_start=zoom,
                tiles = map_style)
        else:
            map_folium = ax
            
        for i, r in coords.iterrows():
            folium.Marker(
                [r['lat'],r['lon']],
                tooltip=f"{r['well']} {r['unit']}" if tooltip else None,
                popup = folium.Popup(html=f"{r['well']} {r['unit']}",show=True,max_width='50%') if popup else None,
                icon=folium.Icon(icon='tint', color='green')
                ).add_to(map_folium)

        folium.LayerControl().add_to(map_folium)
        #LocateControl().add_to(map_folium)
        MeasureControl().add_to(map_folium)
        MousePosition().add_to(map_folium)

        return map_folium
    
    @validate_arguments
    def surveys_map(
        self,
        wells:Optional[List[str]]=None,
        zoom:int =10,
        map_style:str = 'OpenStreetMap',
        tooltip=True,
        popup=False,
        ax=None,
        crs:int = 4326, 
        radius:int = 10,
    ):
        
        coords = self.surveys(wells=wells)
        coords = coords.to_crs(crs)
        coords['lon'] = coords['geometry'].x
        coords['lat'] = coords['geometry'].y
        center = coords[['lat','lon']].mean(axis=0)
        
        if ax is None:
            map_folium = folium.Map(
                location=(center['lat'],center['lon']),
                zoom_start=zoom,
                tiles = map_style)
        else:
            map_folium = ax
            
        for i, r in coords.iterrows():
            folium.Circle(
                [r['lat'],r['lon']],
                tooltip=f"{r['well']} <br>md:{r['md']} <br>tvd:{r['tvd']} <br>tvdss:{r['tvdss']} <br>inc:{r['inc']} " if tooltip else None,
                popup = folium.Popup(html=f"{r['well']} <br>md:{r['md']} <br>tvd:{r['tvd']} <br>tvdss:{r['tvdss']} <br>inc:{r['inc']} ",show=True,max_width='50%') if popup else None,
                #icon=folium.Icon(icon='circle',prefix='fa', color='green'),
                radius=radius
                ).add_to(map_folium)

        folium.LayerControl().add_to(map_folium)
        #LocateControl().add_to(map_folium)
        MeasureControl().add_to(map_folium)
        MousePosition().add_to(map_folium)

        return map_folium
    
    @validate_arguments
    def structural_view3d(
        self,
        wells:Optional[List[str]]=None,
        by:Optional[str] = None,
        formations:Optional[List[str]]=None,
        units:Optional[List[str]]=None,
        perforations:Optional[List[str]]=None,
        tools:Optional[List[str]]=None,
        show_surveys:bool=False,
        show_formations:bool=False,
        show_units:bool=False,
        show_perforations:bool=False,
        show_tools:bool=False,
        formations_scatter:bool=True,
        units_scatter:bool=True,
        perforations_scatter:bool=True,
        tools_scatter:bool=True,
        surveys_mode:str='lines',
        width:int=800,
        height:int=800,
        perforations_triangulate:bool=False,
        formations_triangulate:bool=False,
        units_triangulate:bool=False,
        tools_triangulate:bool=False,
        area_unit:str='m',
        depth_unit:str='ft',
        layout_kw:Dict={}
    ): 
        list_traces = []
        if by is not None:
            list_of_list_of_wells = []
            wh_df =  self.well_heads(wells=wells)
            for j in wh_df[by].unique():
                list_of_list_of_wells.append(wh_df.loc[wh_df[by]==j].index.tolist())
            
            for list_of_wells in list_of_list_of_wells:
                if show_formations:
                    fm_traces = self.formations3d_traces(
                        wells=list_of_wells,
                        formations=formations,
                        scatter=formations_scatter,
                        triangulate=formations_triangulate,
                        area_unit=area_unit,
                        depth_unit=depth_unit
                    )
                    list_traces.extend(fm_traces)
                    
                if show_units:
                    un_traces = self.units3d_traces(
                        wells=list_of_wells,
                        units=units,
                        scatter=units_scatter,
                        triangulate=units_triangulate,
                        area_unit=area_unit,
                        depth_unit=depth_unit
                    )
                    list_traces.extend(un_traces)
                
                if show_perforations:
                    perf_traces = self.perforations3d_traces(
                        wells=list_of_wells,
                        perforations=perforations,
                        scatter=perforations_scatter,
                        triangulate = perforations_triangulate,
                        area_unit=area_unit,
                        depth_unit=depth_unit
                    )
                    list_traces.extend(perf_traces)
                    
                if show_tools:
                    perf_traces = self.tools3d_traces(
                        wells=list_of_wells,
                        tools=tools,
                        scatter=tools_scatter,
                        triangulate = tools_triangulate,
                        area_unit=area_unit,
                        depth_unit=depth_unit
                    )
                    list_traces.extend(perf_traces)   
        else:
            if show_formations:
                fm_traces = self.formations3d_traces(
                    wells=wells,
                    formations=formations,
                    scatter=formations_scatter,
                    triangulate=formations_triangulate,
                    area_unit=area_unit,
                    depth_unit=depth_unit
                )
                list_traces.extend(fm_traces)
                
            if show_units:
                un_traces = self.units3d_traces(
                    wells=wells,
                    units=units,
                    scatter=units_scatter,
                    triangulate=units_triangulate,
                    area_unit=area_unit,
                    depth_unit=depth_unit
                )
                list_traces.extend(un_traces)
            
            if show_perforations:
                perf_traces = self.perforations3d_traces(
                    wells=wells,
                    perforations=perforations,
                    scatter=perforations_scatter,
                    triangulate = perforations_triangulate,
                    area_unit=area_unit,
                    depth_unit=depth_unit
                )
                list_traces.extend(perf_traces)
                
            if show_tools:
                perf_traces = self.tools3d_traces(
                    wells=wells,
                    tools=tools,
                    scatter=tools_scatter,
                    triangulate = tools_triangulate,
                    area_unit=area_unit,
                    depth_unit=depth_unit
                )
                list_traces.extend(perf_traces)
        
        if show_surveys:
            surv_traces = self.surveys3d_traces(
                wells=wells,
                mode=surveys_mode,
                area_unit=area_unit,
                depth_unit=depth_unit
            )
            list_traces.extend(surv_traces)
            
        layout = go.Layout(
            title = 'Surveys',
            scene = {
                'xaxis': {'title': 'Easting'},
                'yaxis': {'title': 'Northing'},
                'zaxis': {'title': 'TVDss'}
            },
            width = width,
            height = height,
            **layout_kw
        )
        return go.Figure(
            data=list_traces,
            layout=layout
        )
            
    @validate_arguments
    def structural_view(
        self,
        wells:Optional[List[str]]=None,
        formations:Optional[List[str]]=None,
        units:Optional[List[str]]=None,
        perforations:Optional[List[str]]=None,
        tools:Optional[List[str]]=None,
        show_surveys:bool=True,
        show_formations:bool=False,
        show_units:bool=False,
        show_perforations:bool=False,
        show_tools:bool=False,
        azi:float = 0,
        center:Optional[Tuple[float,float]]=None,
        margin:float=500,
        ax=None,
        fm_color:str='Set1',
        well_color:str='Set2',
        unit_color:str='magma',
        perforation_color:str='viridis',
        tools_color:str='crest',
        legend:Union[bool,str]='brief',
        formation_kind:str='line',
        unit_kind:str='line',
        perforation_kind:str='scatter',
        well_kind:str='line',
        tool_kind:str='scatter',
        ann_formations:bool=False,
        ann_units:bool=False,
        ann_perforations:bool=False,
        ann_tools:bool=False,
        ann_fontsize:float=11,
        ylims:Optional[Tuple[float,float]]=None,
        **kwargs
    ):
        stax= ax or plt.gca()
               
        if show_formations:
            tops, center = self.formations_projection(
                wells = wells,
                formations=formations,
                azi=azi,
                center=center
            )
            tops.reset_index(inplace=True)
            
            if formation_kind == 'line':
                sns.lineplot(
                    x='projection',
                    y='tvdss_top', 
                    data=tops, 
                    hue='formation',
                    markers=True, 
                    ax=stax, 
                    palette=fm_color, 
                    legend=legend
                )
            else:
                sns.scatterplot(
                    x='projection',
                    y='tvdss_top', 
                    data=tops, 
                    hue='formation',
                    markers=True, 
                    ax=stax, 
                    palette=fm_color, 
                    legend=legend)
                
            if ann_formations:
                for i,v in tops.iterrows():
                    stax.annotate(
                        f"{v['well']} - {v['formation']}",
                        xy=(v['projection'],v['tvdss_top']),
                        xycoords='data',
                        horizontalalignment='right', 
                        fontsize=ann_fontsize,
                        bbox={'boxstyle':'round', 'fc':'0.8'},
                        xytext=(0, 0),
                        textcoords='offset points'
                    )

        if show_tools:
            tools_tops, center = self.tools_projection(
                wells = wells,
                tools=tools,
                azi=azi,
                center=center
            )
            tools_tops.reset_index(inplace=True)
            
            if tool_kind == 'line':
                sns.lineplot(
                    x='projection',
                    y='tvdss_top', 
                    data=tools_tops, 
                    hue='tool',
                    markers=True, 
                    ax=stax, 
                    palette=tools_color, 
                    legend=legend
                )
            else:
                sns.scatterplot(
                    x='projection',
                    y='tvdss_top', 
                    data=tools_tops, 
                    hue='tool',
                    markers=True, 
                    ax=stax, 
                    palette=tools_color, 
                    legend=legend)
                
            if ann_tools:
                for i,v in tops.iterrows():
                    stax.annotate(
                        f"{v['well']} - {v['tool']}",
                        xy=(v['projection'],v['tvdss_top']),
                        xycoords='data',
                        horizontalalignment='right', 
                        fontsize=ann_fontsize,
                        bbox={'boxstyle':'round', 'fc':'0.8'},
                        xytext=(0, 20),
                        textcoords='offset points'
                    )
                
        if show_units:
            units_top, center = self.units_projection(
                wells = wells,
                units=units,
                azi=azi,
                center=center
            )
            units_top.reset_index(inplace=True)
            
            if unit_kind == 'line':
                sns.lineplot(
                    x='projection',
                    y='tvdss_top', 
                    data=units_top, 
                    hue='unit',
                    markers=True, 
                    ax=stax, 
                    palette=unit_color, 
                    legend=legend
                )
            else:
                sns.scatterplot(
                    x='projection',
                    y='tvdss_top', 
                    data=units_top, 
                    hue='unit',
                    markers=True, 
                    ax=stax, 
                    palette=unit_color, 
                    legend=legend
                )

            if ann_units:
                for i,v in units_top.iterrows():
                    stax.annotate(
                       f"{v['well']} - {v['unit']}",
                        xy=(v['projection'],v['tvdss_top']),
                        xycoords='data',
                        horizontalalignment='right', 
                        fontsize=ann_fontsize,
                        bbox={'boxstyle':'round', 'fc':'0.8'},
                        xytext=(0, 20),
                        textcoords='offset points'
                    )

        if show_perforations:
            perfs_top, center = self.perforations_projection(
                wells = wells,
                perforations=perforations,
                azi=azi,
                center=center
            )
            perfs_top.reset_index(inplace=True)
            
            if perforation_kind == 'line':
                sns.lineplot(
                    x='projection',
                    y='tvdss_top', 
                    data=perfs_top, 
                    hue='perforation',
                    markers=True, 
                    ax=stax, 
                    palette=perforation_color, 
                    legend=legend
                )
            else:
                sns.scatterplot(
                    x='projection',
                    y='tvdss_top', 
                    data=perfs_top, 
                    hue='perforation',
                    markers=True, 
                    ax=stax, 
                    palette=unit_color, 
                    legend=legend
                )
                
            if ann_perforations:
                for i,v in perfs_top.iterrows():
                    stax.annotate(
                        f"{v['well']} - {v['perforation']}",
                        xy=(v['projection'],v['tvdss_top']),
                        xycoords='data',
                        horizontalalignment='right', 
                        fontsize=ann_fontsize,
                        bbox={'boxstyle':'round', 'fc':'0.8'},
                        xytext=(0, 20),
                        textcoords='offset points'
                    )

                
        if show_surveys:
            surv= self.surveys(
                wells=wells,
                projection=True, 
                azi=azi, 
                center=center
            ).reset_index(drop=True)
            
            if well_kind=='line':
                sns.lineplot(
                    x='projection',
                    y='tvdss', 
                    data=surv, 
                    hue='well', 
                    ax=stax, 
                    palette=well_color, 
                    legend=legend
                )
            else:
                sns.scatterplot(
                    x='projection',
                    y='tvdss', 
                    data=surv, 
                    hue='well', 
                    ax=stax, 
                    palette=well_color, 
                    legend=legend
                )

        if ylims==None: #Depth Limits
            if show_surveys and show_formations:
                ylims=[surv['tvdss'].max()-margin,surv['tvdss'].min()+margin]
            elif show_surveys:
                ylims=[surv['tvdss'].max()-margin,surv['tvdss'].min()+margin]
            elif show_formations:
                ylims=[tops['tvdss_top'].max()-margin,tops['tvdss_top'].min()+margin]
            elif show_perforations:
                ylims=[perfs_top['tvdss_top'].max()-margin,perfs_top['tvdss_top'].min()+margin]

        stax.set_ylim([ylims[1],ylims[0]])

        xlims = kwargs.pop('xlims',None)
        if xlims:
            stax.set_xlim([xlims[0],xlims[1]])
            
        return stax
    
    @validate_arguments
    def surveys_vtk(
        self,
        wells: Optional[List[str]] = None,
        to_crs:int = None,
        add_wellhead:bool = False
    ):
        list_wells = []
        if isinstance(wells,str):
            list_wells.append(wells)
        elif isinstance(wells,list):
            list_wells.extend(wells)
        else:
            list_wells.extend(list(self.wells.keys()))
            
        survey_blocks = pv.MultiBlock()
        for well in list_wells:
            survey_block = self.wells[well].survey.get_vtk(to_crs=to_crs)
            if add_wellhead:
                wh = self.wells[well].well_head(to_crs=to_crs)
                for i in wh.columns:
                    if wh[i].iloc[0] is not None and i != 'geometry':
                        survey_block.add_field_data([wh[i].iloc[0]],i)
            survey_blocks[well] = survey_block
        
        return survey_blocks
    
    @validate_arguments
    def surveys3d_traces(
        self,
        wells: Optional[List[str]] = None,
        area_unit:str='m', 
        depth_unit:str='ft',
        mode:str = 'lines',
        trace_kw:Dict = {}
    ):
        
        list_wells = []
        if isinstance(wells,str):
            list_wells.append(wells)
        elif isinstance(wells,list):
            list_wells.extend(wells)
        else:
            list_wells.extend(list(self.wells.keys()))
            
        traces = []
        for well in list_wells:
            if self.wells[well].survey is None:
                continue
            trace = self.wells[well].survey.trace3d(name=well, area_unit=area_unit, depth_unit=depth_unit, mode = mode, **trace_kw)
            traces.append(trace)        
        
        return traces

    @validate_arguments
    def surveys3d(
        self,
        wells: Optional[List[str]] = None,
        area_unit:str='m', 
        depth_unit:str='ft',
        mode:str = 'lines',
        width:float = 700,
        height:float = 700,
        trace_kw:Dict = {},
        layout_kw:Dict = {},
    ):
        
        traces = self.surveys3d_traces(
            wells=wells,
            area_unit=area_unit,
            depth_unit=depth_unit,
            mode=mode,
            trace_kw=trace_kw
        )
        
        layout = go.Layout(
            title = 'Surveys',
            scene = {
                'xaxis': {'title': 'Easting'},
                'yaxis': {'title': 'Northing'},
                'zaxis': {'title': 'TVDss'}
            },
            width = width,
            height = height,
            **layout_kw
        )
        return go.Figure(data=traces,layout=layout)
        
    
    @validate_arguments
    def formations_vtk(
        self,
        wells: Optional[List[str]] = None,
        formations: Optional[List[str]] = None,
        to_crs:int = None,
        triangulate:bool = False
    ):
        coords = self.formations(wells = wells, formations = formations).reset_index()
        
        if to_crs:
            coords = coords.to_crs(to_crs)
        
        coords['x'] = coords['geometry'].x
        coords['y'] = coords['geometry'].y
        
        data = {}
        for fm in coords['formation'].unique():
            _df = coords.loc[coords['formation']==fm,['x','y','tvdss_top']].values
            _surv = pv.PolyData(_df)
            if triangulate:
                _surv = _surv.delaunay_2d()
            data[fm] = _surv
        
        fm_blocks = pv.MultiBlock(data)
        return fm_blocks
    
    @validate_arguments
    def units_vtk(
        self,
        wells: Optional[List[str]] = None,
        units: Optional[List[str]] = None,
        to_crs:int = None,
        triangulate:bool = False
    ):
        coords = self.units(wells = wells, units = units).reset_index()
        
        if to_crs:
            coords = coords.to_crs(to_crs)
        
        coords['x'] = coords['geometry'].x
        coords['y'] = coords['geometry'].y
        
        data = {}
        for fm in coords['unit'].unique():
            _df = coords.loc[coords['unit']==fm,['x','y','tvdss_top']].values
            _surv = pv.PolyData(_df)
            if triangulate:
                _surv = _surv.delaunay_2d()
            data[fm] = _surv
        
        fm_blocks = pv.MultiBlock(data)
        return fm_blocks
    
    @validate_arguments
    def formations3d_traces(
        self,
        wells: Optional[List[str]] = None,
        formations: Optional[List[str]] = None,
        to_crs:int = None,
        scatter: bool = False,
        triangulate:bool = True,
        area_unit='m',
        depth_unit='ft',
        **kwargs
    ):
        coords = self.formations(wells = wells, formations = formations).reset_index()
        
        if to_crs:
            coords = coords.to_crs(to_crs)
        
        coords['x'] = coords['geometry'].x
        coords['y'] = coords['geometry'].y
        
        coef_area = 1 if area_unit == 'm' else 3.28084
        coef_depth = 1 if depth_unit == 'ft' else 0.3048
        
        traces = []
        for fm in coords['formation'].unique():
            _df = coords.loc[coords['formation']==fm,['x','y','tvdss_top']]
            
            if triangulate:
                tri = Delaunay(_df[['x','y']].values*coef_area)
                
                trace = go.Mesh3d(
                    x = _df['x'].values * coef_area,
                    y = _df['y'].values * coef_area,
                    z = _df['tvdss_top'].values * coef_depth,
                    i = tri.simplices[:,0],
                    j = tri.simplices[:,1],
                    k = tri.simplices[:,2],
                    name = fm,
                    **kwargs
                )
                traces.append(trace)

            if scatter:
                scatter_trace = go.Scatter3d(
                    x = _df['x'].values* coef_area,
                    y = _df['y'].values* coef_area,
                    z = _df['tvdss_top'].values*coef_depth,
                    mode = 'markers',
                    name = fm,
                )
                traces.append(scatter_trace)

        return traces
    
    @validate_arguments
    def units3d_traces(
        self,
        wells: Optional[List[str]] = None,
        units: Optional[List[str]] = None,
        to_crs:int = None,
        scatter:bool = False,
        triangulate:bool = False,
        area_unit:str='m',
        depth_unit:str='ft',
        **kwargs
    ):
        coords = self.units(wells = wells, units = units).reset_index()
        
        if to_crs:
            coords = coords.to_crs(to_crs)
        
        coords['x'] = coords['geometry'].x
        coords['y'] = coords['geometry'].y

        coef_area = 1 if area_unit == 'm' else 3.28084
        coef_depth = 1 if depth_unit == 'ft' else 0.3048
        
        traces = []
        for fm in coords['unit'].unique():
            _df = coords.loc[coords['unit']==fm,['x','y','tvdss_top']]
            
            if triangulate:
                tri = Delaunay(_df[['x','y']].values*coef_area)
                
                
                trace = go.Mesh3d(
                    x = _df['x'].values * coef_area,
                    y = _df['y'].values * coef_area,
                    z = _df['tvdss_top'].values * coef_depth,
                    i = tri.simplices[:,0],
                    j = tri.simplices[:,1],
                    k = tri.simplices[:,2],
                    name = fm,
                    **kwargs
                )
                traces.append(trace)
            
            if scatter:
                scatter_trace = go.Scatter3d(
                    x = _df['x'].values * coef_area,
                    y = _df['y'].values * coef_area,
                    z = _df['tvdss_top'].values * coef_depth,
                    mode = 'markers',
                    name = fm
                )
                traces.append(scatter_trace)
                
        return traces
    
    @validate_arguments
    def perforations3d_traces(
        self,
        wells: Optional[List[str]] = None,
        perforations: Optional[List[str]] = None,
        to_crs:int = None,
        scatter:bool = False,
        triangulate:bool = False,
        area_unit:str='m',
        depth_unit:str='ft',
        **kwargs
    ):
        coords = self.perforations(wells = wells, perforations = perforations).reset_index()
        
        if to_crs:
            coords = coords.to_crs(to_crs)
        
        coords['x'] = coords['geometry'].x
        coords['y'] = coords['geometry'].y
        
        coef_area = 1 if area_unit == 'm' else 3.28084
        coef_depth = 1 if depth_unit == 'ft' else 0.3048
        
        traces = []
        for fm in coords['perforation'].unique():
            _df = coords.loc[coords['perforation']==fm,['x','y','tvdss_top']]
            
            if triangulate:
                tri = Delaunay(_df[['x','y']].values*coef_area)
                
                
                trace = go.Mesh3d(
                    x = _df['x'].values * coef_area,
                    y = _df['y'].values * coef_area,
                    z = _df['tvdss_top'].values * coef_depth,
                    i = tri.simplices[:,0],
                    j = tri.simplices[:,1],
                    k = tri.simplices[:,2],
                    name = fm,
                    **kwargs
                )
                traces.append(trace)
            
            if scatter:
                scatter_trace = go.Scatter3d(
                    x = _df['x'].values * coef_area,
                    y = _df['y'].values * coef_area,
                    z = _df['tvdss_top'].values * coef_depth,
                    mode = 'markers',
                    name = fm
                )
                traces.append(scatter_trace)
                
        return traces
    
    @validate_arguments
    def tools3d_traces(
        self,
        wells: Optional[List[str]] = None,
        tools: Optional[List[str]] = None,
        to_crs:int = None,
        scatter:bool = False,
        triangulate:bool = False,
        area_unit:str='m',
        depth_unit:str='ft',
        **kwargs
    ):
        coords = self.tools(wells = wells, tools = tools).reset_index()
        
        if to_crs:
            coords = coords.to_crs(to_crs)
        
        coords['x'] = coords['geometry'].x
        coords['y'] = coords['geometry'].y

        coef_area = 1 if area_unit == 'm' else 3.28084
        coef_depth = 1 if depth_unit == 'ft' else 0.3048
        
        traces = []
        for fm in coords['tool'].unique():
            _df = coords.loc[coords['tool']==fm,['x','y','tvdss_top']]
            
            if triangulate:
                tri = Delaunay(_df[['x','y']].values*coef_area)
                
                
                trace = go.Mesh3d(
                    x = _df['x'].values * coef_area,
                    y = _df['y'].values * coef_area,
                    z = _df['tvdss_top'].values* coef_depth,
                    i = tri.simplices[:,0],
                    j = tri.simplices[:,1],
                    k = tri.simplices[:,2],
                    name = fm,
                    **kwargs
                )
                traces.append(trace)
            
            if scatter:
                scatter_trace = go.Scatter3d(
                    x = _df['x'].values * coef_area,
                    y = _df['y'].values * coef_area,
                    z = _df['tvdss_top'].values * coef_depth,
                    mode = 'markers',
                    name = fm
                )
                traces.append(scatter_trace)
                
        return traces

    @validate_arguments
    def formations3d(
        self,
        wells: Optional[List[str]] = None,
        formations: Optional[List[str]] = None,
        to_crs:int = None,
        title:str = 'Formations',
        width:float = 700,
        height:float = 700,
        scatter:bool = False,
        area_unit:str='m',
        depth_unit:str='ft',
        **kwargs
    ):
        
        traces = self.formations3d_traces(
            wells = wells, 
            formations = formations, 
            to_crs = to_crs, 
            scatter=scatter,
            area_unit=area_unit,
            depth_unit=depth_unit,
            **kwargs
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
        
        return go.Figure(data=traces,layout=layout)
    
    @validate_arguments
    def units3d(
        self,
        wells: Optional[List[str]] = None,
        units: Optional[List[str]] = None,
        to_crs:int = None,
        title:str = 'units',
        width:float = 700,
        height:float = 700,
        scatter:bool = False,
        area_unit:str='m',
        depth_unit:str='ft',
        **kwargs
    ):
        
        traces = self.units3d_traces(
            wells = wells, 
            units = units, 
            to_crs = to_crs, 
            scatter = scatter,
            area_unit=area_unit,
            depth_unit=depth_unit,
            **kwargs
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
        
        return go.Figure(data=traces,layout=layout)

    @validate_arguments
    def perforations3d(
        self,
        wells: Optional[List[str]] = None,
        perforations: Optional[List[str]] = None,
        to_crs:int = None,
        title:str = 'perforations',
        width:float = 700,
        height:float = 700,
        scatter:bool = False,
        area_unit:str='m',
        depth_unit:str='ft',
        **kwargs
    ):
        
        traces = self.perforations3d_traces(
            wells = wells, 
            perforations = perforations, 
            to_crs = to_crs, 
            scatter = scatter,
            area_unit=area_unit,
            depth_unit=depth_unit,
            **kwargs
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
        
        return go.Figure(data=traces,layout=layout)   

    @validate_arguments
    def tools3d(
        self,
        wells: Optional[List[str]] = None,
        tools: Optional[List[str]] = None,
        to_crs:int = None,
        title:str = 'tools',
        width:float = 700,
        height:float = 700,
        scatter:bool = False,
        area_unit:str='m',
        depth_unit:str='ft',
        **kwargs
    ):
        
        traces = self.tools3d_traces(
            wells = wells, 
            tools = tools, 
            to_crs = to_crs, 
            scatter = scatter,
            area_unit=area_unit,
            depth_unit=depth_unit,
            **kwargs
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
        
        return go.Figure(data=traces,layout=layout)     
            
    
    @validate_arguments
    def structural_view_vtk(
        self,
        wells: Union[None,List[str]] = None,
        formations: Union[None,List[str]] = None,
        units: Union[None,List[str]] = None,
        export_wells:bool = True,
        export_formations:bool=True,
        export_units:bool=True,
        to_crs:int = None,
        triangulate_formations:bool = False,
        triangulate_units:bool = False
    ):
        
        blocks = pv.MultiBlock()
        
        if export_wells:
            surv = self.surveys_vtk(wells = wells, to_crs = to_crs)
            for s in surv.keys():
                blocks[s]=surv[s]
        
        if export_formations:
            form = self.formations_vtk(wells = wells, formations = formations, to_crs = to_crs, triangulate=triangulate_formations)
            for t in form.keys():
                blocks[t]=form[t]
        
        if export_units:
            unit = self.units_vtk(wells = wells, units = units, to_crs = to_crs, triangulate=triangulate_units)
  
            for u in unit.keys():
                blocks[u]=unit[u]

        return blocks
    
    @validate_arguments
    def production(
        self, 
        wells:Optional[Union[str,List[str]]]=None,
        mode:Optional[FormatEnum]=None,
        by:str = None
    ):
        list_wells = []
        if isinstance(wells,str):
            list_wells.append(wells)
        elif isinstance(wells,list):
            list_wells.extend(wells)
        else:
            list_wells.extend(list(self.wells.keys()))

        df_list = []
        for w in list_wells:
            if self.wells[w].production is None:
                continue
            
            if mode is not None:
                if mode == FormatEnum.calendar:
                    p_obj = self.wells[w].production.to_calendar()
                elif mode == FormatEnum.effective:
                    p_obj = self.wells[w].production.to_effective()
                elif mode == FormatEnum.volume:
                    p_obj = self.wells[w].production.to_volume()
                
                p_df = p_obj.df()
            else:
                p_df = self.wells[w].production.df()
            
            p_df['well'] = w
            df_list.append(p_df)
            
        df = pd.concat(df_list,axis=0)
        df[['freq','recovery','type','level','format']] = df[['freq','recovery','type','level','format']].applymap(lambda x: x if isinstance(x,str) else x.value)
        if by is not None:
            grouper = ['period']
            sums = ['oil','water','gas','water_inj','gas_inj']
            if by == 'field':
                pass
            elif isinstance(by,list):
                grouper.extend(by)
            elif isinstance(by,str):
                grouper.append(by)
            df = df.groupby(grouper)[sums].sum().reset_index()
        
        df['date'] = df['period'].dt.to_timestamp()
        return df

    @validate_arguments
    def pressures(
        self, 
        wells:Optional[Union[str,List[str]]]=None,
        pressures:Optional[Union[str,List[str]]]=None,
        estimate_midpoint:bool=False,
        midpoint_weights_column:Optional[str]='md_tick',
        midpoint_name:str='midpoint',
        record_midpoint:bool=False
    ):
        list_wells = []
        if isinstance(wells,str):
            list_wells.append(wells)
        elif isinstance(wells,list):
            list_wells.extend(wells)
        else:
            list_wells.extend(list(self.wells.keys()))

        df_list = []
        for w in list_wells:
            if self.wells[w].pressures is None:
                continue
            
            gdf = self.wells[w].pressures
            #! TODO: Verify if the calculation were already made
            if self.wells[w].survey:
                gdf.get_reference_depth(self.wells[w].survey)
                gdf.estimate_ticks()
                gdf.estimate_coordinate(self.wells[w].survey)
            
            if record_midpoint:
                gdf.estimate_midpoints(pressures=pressures)

            #Estimate Mid point
            if estimate_midpoint:
                try:
                    gdf.estimate_average_midpoint(
                        pressures=pressures,
                        weights=midpoint_weights_column,
                        name = midpoint_name
                    )
                except:
                    pass   
            p_df = gdf.df()            
            p_df['well'] = w
            df_list.append(p_df)
            
        df = pd.concat(df_list,axis=0)    
        df[['type','welltype']] = df[['type','welltype']].applymap(lambda x: x.value)    
        return df
    
            
    def save_json(self, filename:str=None):
        """
        Export the survey to a json file.
        """
        if filename is None:
            if self.name is None:
                filename = 'wells.json'
            else:
                filename = f'{self.name}.json'
        if not filename.endswith('.json'):
            filename += '.json'
        # Writing to sample.json
        with open(f"{filename}", "w") as outfile:
            outfile.write(self.json(exclude_none=True, indent=2))
    
    @classmethod
    def from_omegadb(
        cls,
        engine:Engine,
        wells:List[str]=None, 
        fields:List[str]=None,
        blocks:List[str]=None,
        basins:List[str]=None,
        name:str=None
    ):
        """
        Add wells information from the Postgres Database scuervo91/oilbase
        It uses the structure and the sintaxis implemented specifically in that database
        """
        
        well_heads_query = """
            select
                w.well as well,
                w.rte as rte,
                w.surface_x as easting,
                w.surface_y as northing,
                w.epsg as epsg,
                f.field as field,
                bk.block as block,
                bs.basin as basin
            from
                list.wells w
            join
                list.fields f on w.field_id = f.id
            join
                list.blocks bk on f.block_id = bk.id
            join
                list.basins bs on bk.basin_id = bs.id
        """
        
        well_surveys_query= """
            SELECT 
                w.well as well,
                s.md as md,
                s.inc as inc,
                s.azi as azi
            FROM
                list.surveys s
            JOIN
                list.wells w ON s.well_id = w.id
            JOIN
                list.fields f ON w.field_id = f.id
            join
                list.blocks bk on f.block_id = bk.id
            join
                list.basins bs on bk.basin_id = bs.id
        """

        well_perforations_query= """
            SELECT 
                w.well as well,
                p.id as id,
                p.md_top as md_top,
                p.md_bottom as md_bottom
            FROM
                list.perforations p
            JOIN
                list.wells w ON p.well_id = w.id
            JOIN
                list.fields f ON w.field_id = f.id
            join
                list.blocks bk on f.block_id = bk.id
            join
                list.basins bs on bk.basin_id = bs.id
        """
        
        well_formations_tops_query= """
            SELECT 
                w.well as well,
                fm.formation as formation,
                ft.md_top as md_top,
                ft.md_bottom as md_bottom
            FROM
                list.formations_tops ft
            JOIN
                list.formations fm ON ft.formation_id = fm.id
            JOIN
                list.wells w ON ft.well_id = w.id
            JOIN
                list.fields f ON w.field_id = f.id        
            join
                list.blocks bk on f.block_id = bk.id
            join
                list.basins bs on bk.basin_id = bs.id
        """
        
        well_units_tops_query= """
            SELECT 
                w.well as well,
                un.unit as formation,
                ut.md_top as md_top,
                ut.md_bottom as md_bottom
            FROM
                list.units_tops ut
            JOIN
                list.units un ON ut.unit_id = un.id
            JOIN
                list.wells w ON ut.well_id = w.id
            JOIN
                list.fields f ON w.field_id = f.id        
            join
                list.blocks bk on f.block_id = bk.id
            join
                list.basins bs on bk.basin_id = bs.id
        """
        
        well_perf_status_query= """
            select 
                w.well, 
                p.id, 
                p.md_top, 
                p.md_bottom, 
                pf.start_date, 
                pf.end_date, 
                pf.status 
            from 
                events.perforations_status pf 
            join 
                list.perforations p on pf.perforation_id = p.id 
            join 
                list.wells w on p.well_id = w.id
            join 
                list.fields f on w.field_id = f.id
            join
                list.blocks bk on f.block_id = bk.id
            join
                list.basins bs on bk.basin_id = bs.id
        """


        #Custom the query
        query_list = {
            'well_heads':well_heads_query,
            'well_surveys': well_surveys_query,
            'well_perforations':well_perforations_query,
            'well_formations_tops':well_formations_tops_query,
            'well_units_tops':well_units_tops_query,
            'well_perf_status':well_perf_status_query
        }

        wells_where_bool = False
        if wells is not None:
            assert isinstance(wells,(str,list))

            for i in query_list:
                query_list[i] = query_list[i] + f" {'and' if wells_where_bool else 'where'} w.well in {tuple(wells)}".replace(',)',')')
                
            wells_where_bool = True

        if fields is not None:
            assert isinstance(fields,(str,list))
            
            for i in query_list:
                query_list[i] = query_list[i] + f" {'and' if wells_where_bool else 'where'} f.field in {tuple(fields)}".replace(',)',')')
            wells_where_bool = True
            
        if blocks is not None:
            assert isinstance(blocks,(str,list))
            
            for i in query_list:
                query_list[i] = query_list[i] + f" {'and' if wells_where_bool else 'where'} bk.block in {tuple(blocks)}".replace(',)',')')
            wells_where_bool = True
            
        if basins is not None:
            assert isinstance(basins,(str,list))
            
            for i in query_list:
                query_list[i] = query_list[i] + f" {'and' if wells_where_bool else 'where'} f.basin in {tuple(basins)}".replace(',)',')')
            wells_where_bool = True



        # query from oilbase
        df_dict = {}
        for i in query_list:
            try:
                _df = pd.read_sql(query_list[i], con=engine)     
                df_dict[i] = _df
            except:
                print(f'no entered {i}')
                df_dict[i] = None
               
        wells_dict = {}

        for i, r in df_dict['well_heads'].iterrows():
            
            try:
                s = Survey.from_deviation(
                    df_dict['well_surveys'].loc[df_dict['well_surveys']['well']==r['well'],['md','azi','inc']], 
                    surface_easting=r['easting'],
                    surface_northing=r['northing'],
                    rte=r['rte'],
                    crs=r['epsg']
                )
            except Exception as e:
                print(f'survey {e}')
                s = None
            
            formations = Formations()
            try:
                tops_fm_df = df_dict['well_formations_tops'].loc[df_dict['well_formations_tops']['well']==r['well'],['formation','md_top','md_bottom']]
                tops = Formations.from_df(tops_fm_df,name='formation')
                formations.add_formations(tops.formations)
            except Exception as e:
                print(f'Excfm {e}')
                
            units = Units()
            try:
                tops_un_df = df_dict['well_units_tops'].loc[df_dict['well_units_tops']['well']==r['well'],['formation','md_top','md_bottom']]
                tops_un = Units.from_df(tops_un_df,name='formation')
                units.add_units(tops_un.units)
            except Exception as e:
                print(f'units {e}')


            perforations = Perforations()
            try:
                perfw = Perforations.from_df(df_dict['well_perforations'].loc[df_dict['well_perforations']['well']==r['well'],:],name='id')
                perforations.add_perforations(perfw.perforations)
            except Exception as e:
                print(f'perf {e}')
            
            #try:
            perforations.status_from_df(df_dict['well_perf_status'].loc[df_dict['well_perf_status']['well']==r['well'],:],name='id')
            #except Exception as e:
            #    print(f'perf status{e}')
            w = Well(
                name = r['well'],
                surface_x = r['easting'],
                surface_y = r['northing'],
                #surface_coordinate = Point(r['easting'], r['northing']),
                rte=r['rte'],
                crs = int(r['epsg']),
                survey = s,
                formations = formations,
                units = units,
                perforations = perforations,  
                fields = {
                    'field':r['field'],
                    'block':r['block'],
                    'basin':r['basin']
                }                  
            )
            
            wells_dict[w.name] = w

        return cls(name=name,wells=wells_dict)
    
    @classmethod
    def from_dataonboarding(
        cls,
        wellheads:str,
        deviations:str = None,
        formations:str = None,
        units:str = None,
        perforations:str = None,
        tools:str = None,
        correlations:str = None,
        root:str = None,
        name:str = None,
        crs = None,
        vertical_depth:float = 6000,
        well_heads_kwargs:dict = None,
        survey_kwargs:dict = None,
        formations_kwargs:dict = None,
        units_kwargs:dict = None,
        perforations_kwargs:dict = None,
        tools_kwargs:dict = None,
        correlations_kwargs:dict = None
    ):
        if root is not None:
            root_path = os.path.abspath(root)
            wellheads_path = os.path.join(root_path,wellheads)
        else:
            wellheads_path = wellheads 
            
        wells_dict = {}
        
        wellheads_df = pd.read_csv(
            wellheads_path,
            dtype = well_heads_kwargs.get('import_dtype',None)
        )
        wh_map = well_heads_kwargs.get('mapping',None)
        if wh_map is not None:
            wh_map = {v: k for k, v in wh_map.items()}
            wellheads_df.rename(columns=wh_map,inplace=True)
        
        wh_dates_cols = well_heads_kwargs.get('dates',None)
        if wh_dates_cols is not None:
            for c in wh_dates_cols['cols']:
                wellheads_df[c] = pd.to_datetime(wellheads_df[c],format=wh_dates_cols['format'], exact=False)
        
        
        if deviations is not None:
            if root is not None:
                root_path = os.path.abspath(root)
                dev_path = os.path.join(root_path,deviations)
            else:
                dev_path = deviations
            deviations_df = pd.read_csv(
                dev_path,
                dtype = survey_kwargs.get('import_dtype',None)
            )
            surv_map = survey_kwargs.get('mapping',None)
            if surv_map is not None:
                surv_map = {v: k for k, v in surv_map.items()}
                deviations_df.rename(columns=surv_map,inplace=True)
            
            
        if formations is not None:
            if root is not None:
                root_path = os.path.abspath(root)
                lay_path = os.path.join(root_path,formations)
            else:
                lay_path = formations 
                
            formations_df = pd.read_csv(
                lay_path,
                dtype = formations_kwargs.get('import_dtype',None)
            ) 
            
            fm_map = formations_kwargs.get('mapping',None)
            if fm_map is not None:
                fm_map = {v: k for k, v in fm_map.items()}
                formations_df.rename(columns=fm_map,inplace=True)
            
            fm_dates_cols = formations_kwargs.get('dates',None)
            if fm_dates_cols is not None:
                for c in fm_dates_cols['cols']:
                    formations_df[c] = pd.to_datetime(formations_df[c],format=fm_dates_cols['format'],exact=False)

        if units is not None:
            if root is not None:
                root_path = os.path.abspath(root)
                lay_path = os.path.join(root_path,units)
            else:
                lay_path = units 
                
            units_df = pd.read_csv(
                lay_path,
                dtype = units_kwargs.get('import_dtype',None)
            ) 
            
            un_map = units_kwargs.get('mapping',None)
            if un_map is not None:
                un_map = {v: k for k, v in un_map.items()}
                units_df.rename(columns=un_map,inplace=True)
            
            un_dates_cols = units_kwargs.get('dates',None)
            if un_dates_cols is not None:
                for c in un_dates_cols['cols']:
                    units_df[c] = pd.to_datetime(units_df[c],format=un_dates_cols['format'],exact=False)
                    
        if perforations is not None:
            if root is not None:
                root_path = os.path.abspath(root)
                lay_path = os.path.join(root_path,perforations)
            else:
                lay_path = perforations 
                
            perforations_df = pd.read_csv(
                lay_path,
                dtype = perforations_kwargs.get('import_dtype',None)
            ) 
            
            perf_map = perforations_kwargs.get('mapping',None)
            if perf_map is not None:
                perf_map = {v: k for k, v in perf_map.items()}
                perforations_df.rename(columns=perf_map,inplace=True)
            
            perf_dates_cols = perforations_kwargs.get('dates',None)
            if perf_dates_cols is not None:
                for c in perf_dates_cols['cols']:
                    perforations_df[c] = pd.to_datetime(perforations_df[c],format=perf_dates_cols['format'],exact=False)
                    
        if tools is not None:
            if root is not None:
                root_path = os.path.abspath(root)
                lay_path = os.path.join(root_path,tools)
            else:
                lay_path = tools 
                
            tools_df = pd.read_csv(
                lay_path,
                dtype = tools_kwargs.get('import_dtype',None)
            ) 
            
            to_map = tools_kwargs.get('mapping',None)
            if to_map is not None:
                to_map = {v: k for k, v in to_map.items()}
                tools_df.rename(columns=to_map,inplace=True)
            
            to_dates_cols = tools_kwargs.get('dates',None)
            if to_dates_cols is not None:
                for c in to_dates_cols['cols']:
                    tools_df[c] = pd.to_datetime(tools_df[c],format=to_dates_cols['format'],exact=False)
                    
        if correlations is not None:
            if root is not None:
                root_path = os.path.abspath(root)
                lay_path = os.path.join(root_path,correlations)
            else:
                lay_path = correlations 
                
            correlations_df = pd.read_csv(
                lay_path,
                dtype = correlations_kwargs.get('import_dtype',None)
            ) 
            
            cor_map = correlations_kwargs.get('mapping',None)
            if cor_map is not None:
                cor_map = {v: k for k, v in cor_map.items()}
                correlations_df.rename(columns=cor_map,inplace=True)
            
            cor_dates_cols = correlations_kwargs.get('dates',None)
            if cor_dates_cols is not None:
                for c in cor_dates_cols['cols']:
                    correlations_df[c] = pd.to_datetime(correlations_df[c],format=cor_dates_cols['format'],exact=False)

        coef_conv = well_heads_kwargs['mapping'].get('coef_conversion',1.0)
        for i, r in wellheads_df.iterrows():
            well_id = r['name']
            
            #Deviation
            if deviations is not None:
                dev_i = deviations_df.loc[deviations_df['name']==well_id,:]
                
                if dev_i.empty:
                    s = Survey.make_vertical(
                        td = vertical_depth,
                        n = 2,
                        surface_easting=r['easting']*coef_conv,
                        surface_northing=r['northing']*coef_conv,
                        rte = r['rte'],
                        crs = crs
                    )
                
                #Check if any of the md, azi and ic columns have null values
                elif all([~dev_i[i].isnull().any() for i in ['md','inc','azi']]):

                    s = Survey.from_deviation(
                        dev_i,
                        md = 'md',
                        inc = 'inc',
                        azi = 'azi',
                        surface_easting=r['easting'] * coef_conv,
                        surface_northing=r['northing']* coef_conv,
                        rte=r['rte'],
                        crs=crs
                    )
                
                else:
                    s = Survey.from_position(
                        dev_i,
                        md = 'md',
                        tvd = 'tvd',
                        easting = 'easting',
                        northing= 'northing',
                        surface_easting=r['easting'] * coef_conv,
                        surface_northing=r['northing']* coef_conv,
                        crs= crs,
                        rte = r['rte']
                    )
            else:
                s = None
                
            if formations is not None:
                lay_i = formations_df.loc[formations_df['well_id']==well_id,:]

                if lay_i.empty:
                    fm = None 
                else:
                    fm = Formations.from_df(
                        lay_i,
                        name='name',
                        md_top = 'md_top',
                        md_bottom = 'md_bottom',
                        fields = formations_kwargs.get('fields',None),
                    )
            else:
                fm = None
                
            if units is not None:
                lay_i = units_df.loc[units_df['well_id']==well_id,:]

                if lay_i.empty:
                    un = None 
                else:
                    un = Units.from_df(
                        lay_i,
                        name='name',
                        md_top = 'md_top',
                        md_bottom = 'md_bottom',
                        fields = units_kwargs.get('fields',None),
                    )
            else:
                un = None
                
            if perforations is not None:
                lay_i = perforations_df.loc[perforations_df['well_id']==well_id,:]

                if lay_i.empty:
                    perf = None 
                else:
                    perf = Perforations.from_df(
                        lay_i,
                        name='name',
                        md_top = 'md_top',
                        md_bottom = 'md_bottom',
                        fields = perforations_kwargs.get('fields',None),
                    )
            else:
                perf = None

            if tools is not None:
                lay_i = tools_df.loc[tools_df['well_id']==well_id,:]

                if lay_i.empty:
                    tool = None 
                else:
                    tool = Tools.from_df(
                        lay_i,
                        name='name',
                        md_top = 'md_top',
                        md_bottom = 'md_bottom',
                        fields = tools_kwargs.get('fields',None),
                    )
            else:
                tool = None
                
            if correlations is not None:
                lay_i = correlations_df.loc[correlations_df['well_id']==well_id,:]

                if lay_i.empty:
                    corr = None 
                else:
                    corr = Correlations.from_df(
                        lay_i,
                        name='name',
                        md_top = 'md_top',
                        md_bottom = 'md_bottom',
                        fields = correlations_kwargs.get('fields',None),
                    )
            else:
                corr = None
                
            wh_fields = well_heads_kwargs.get('fields',None)
            w = Well(
                name = r['name'],
                surface_x=r['easting']*coef_conv,
                surface_y = r['northing']*coef_conv,
                # surface_coordinate = Point(
                #     r['easting']*coef_conv, 
                #     r['northing']*coef_conv
                # ),
                rte=r['rte'],
                crs = crs,
                survey = s,
                formations = fm, 
                units = un,
                perforations = perf,
                tools = tool,
                corralations = corr,
                fields = {i:r[i] for i in wh_fields} if wh_fields is not None else None,               
            )
            
            wells_dict[w.name] = w
            
        return cls(name=name,wells=wells_dict) 