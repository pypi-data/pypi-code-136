#__init__.py 파일

import datetime
import os

import geopandas as gpd
import pandas as pd
from dateutil.parser import parse as str2datm

from .mapper import STATION_LIST_HEADER_MAPPER

BASE_URL = 'https://raw.githubusercontent.com/yanghjep/rdawos/master/'


def read(sub_url, cache_dir):
    if cache_dir:
        cache_path = f'{cache_dir}/{sub_url}'
    else:
        cache_path = None

    if cache_path and os.path.exists(cache_path):
        df = pd.read_csv(cache_path)
    else:
        data_url = f'{BASE_URL}/{sub_url}'
        df = pd.read_csv(data_url)
        if cache_path:
            os.makedirs(os.path.dirname(cache_path), exist_ok=True)
            df.to_csv(cache_path, index=False)
    col_set = set(df.columns)
    if len({'lon', 'lat'} - col_set) == 0:
        geometry = gpd.points_from_xy(x=df.lon, y=df.lat)
    elif len({'경도', '위도'} - col_set) == 0:
        geometry = gpd.points_from_xy(x=df['경도'], y=df['위도'])
    elif len({'x', 'y'} - col_set) == 0:
        geometry = gpd.points_from_xy(x=df.x, y=df.y)
    elif len({'st_x', 'st_y'} - col_set) == 0:
        geometry = gpd.points_from_xy(x=df.st_x, y=df.st_y)
    else:
        geometry = None
    if geometry:
        df = gpd.GeoDataFrame(df, crs='epsg:4326', geometry=geometry)
    return df


def read_stations(cache_dir='./.rdawos', *, kor_header=False):
    df = read(f'/stations/rda.stations.csv', cache_dir)
    if not kor_header:
        df = df.rename(columns=STATION_LIST_HEADER_MAPPER)
    return df


def read_single_point(code, begin, until, *, cache_dir='./.rdawos'):
    if isinstance(begin, (datetime.date,)):
        begin_year = begin.year
    elif isinstance(begin, (str,)):
        begin = str2datm(begin).date()
        begin_year = begin.year
    else:
        begin_year = int(begin)

    if isinstance(until, (datetime.date,)):
        until_year = until.year
    elif isinstance(until, (str,)):
        until = str2datm(until).date()
        until_year = until.year
    else:
        until_year = int(until)

    df_ary = []
    for year in range(begin_year, until_year + 1):
        df = read(f'/pointly/{code}/{year}/{code}.{year}.csv', cache_dir)
        df_ary.append(df)
    df = pd.concat(df_ary)

    if isinstance(begin, (datetime.date,)):
        df = df[df['tm'] >= begin.strftime('%Y-%m-%d')]
    if isinstance(until, (datetime.date,)):
        df = df[df['tm'] <= until.strftime('%Y-%m-%d')]

    return df.reset_index()


def read_multi_point(date, *, cache_dir='./.rdawos'):
    if isinstance(date, (str,)):
        date = str2datm(date)

    df = read(date.strftime(f'/daily/%Y/%m/%d/rdadaily.%Y-%m-%d.csv'), cache_dir)

    return df
