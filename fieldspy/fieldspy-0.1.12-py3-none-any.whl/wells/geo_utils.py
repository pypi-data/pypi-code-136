from shapely.ops import voronoi_diagram, triangulate
from shapely.geometry import Point
from shapely.affinity import scale
import geopandas as gpd
import pandas as pd
import numpy as np


def create_convex_hull(
    geom:gpd.GeoDataFrame, 
    xscale=1.1,
    yscale=1.1,
):
    gdf = geom.copy()
    # Create a single geometry with Muilti points object
    multipoints = gdf.unary_union
    
    # Create a convex hull from the multipoints and scale it
    # with the purpose of creating a bounding box
    convex_hull = scale(
        multipoints.convex_hull,
        xfact = xscale,
        yfact = yscale,
    )
    
    return convex_hull

def create_voronoi(
    geom:gpd.GeoDataFrame, 
    xscale=1.1,
    yscale=1.1,
):
    gdf = geom.copy()
    # Create a single geometry with Muilti points object
    multipoints = gdf.unary_union
    
    # Create a convex hull from the multipoints and scale it
    # with the purpose of creating a bounding box
    
    convex_hull = scale(
        multipoints.convex_hull,
        xfact = xscale,
        yfact = yscale,
    )
    
    # Create a voronoi diagram from the multipoints 
    polys = gpd.GeoSeries([i for i in voronoi_diagram(multipoints)])
    cliped = polys.clip(convex_hull)
    
    d = {}
    
    for i, r in gdf.iterrows():
        for p in cliped:
            if p.contains(r['geometry']):
                d[i] = p
                break
        
    geopoly  =  gpd.GeoSeries(d)
    gdf['geometry'] = geopoly
    
    return gdf

def create_voronoi_grid(
    geom:gpd.GeoDataFrame, 
    xscale=1.1,
    yscale=1.1,
    dsol = 1000,
    fac = 1
):
    gdf = geom.copy()
    gdf['type'] = 'original_points'
    vor = create_voronoi(gdf,xscale=xscale,yscale=yscale)
    vor_union = vor.unary_union
    vor_union_gdf = gpd.GeoSeries([vor_union])
    
    minx, miny, maxx, maxy = vor_union.bounds
    x = np.arange(minx,maxx,dsol)
    y = np.arange(miny,maxy,dsol)
    
    xx, yy = np.meshgrid(x,y)
    
    points = np.column_stack((xx.flatten(),yy.flatten()))
    mp = gpd.GeoDataFrame({'geometry':[Point(c[0],c[1]) for c in points]})
    mp['within'] = mp.within(vor_union)
    mp_gdf_inside = mp.loc[mp['within']==True]
    distance = mp_gdf_inside.geometry.apply(lambda g: gdf.distance(g))
    bool_distance = distance < dsol*fac
    mp_gdf_inside['ndist'] = bool_distance.sum(axis=1)
    add_points = mp_gdf_inside.loc[mp_gdf_inside['ndist']==0]
    add_points['type'] = 'new_points'
    all_p = gpd.GeoDataFrame(pd.concat([gdf[['geometry']],add_points[['geometry']]]))
    polys = gpd.GeoSeries([i for i in voronoi_diagram(all_p.unary_union)])
    cliped = polys.clip(all_p.unary_union.convex_hull)
    return gpd.GeoDataFrame(geometry=cliped)

def create_triangulation(
    geom:gpd.GeoDataFrame
):
    gdf = geom.copy()
    # Create a single geometry with Muilti points object
    multipoints = gdf.unary_union
    
    polys = gpd.GeoSeries([i for i in triangulate(multipoints)])
      
    return polys