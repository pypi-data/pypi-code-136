#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 21:07:11 2022

@author: mike
"""
#############################################
### h5py
import hdf5tools
import hdf5plugin
import h5py
import os
import numpy as np
import xarray as xr
from time import time
import pandas as pd
from datetime import datetime
import cftime
import dateutil.parser as dparser
import numcodecs
import io
try:
    import hdf5plugin
    # compressor = hdf5plugin.Blosc()
    compressor = hdf5plugin.Zstd(1)
    # compressor = hdf5plugin.LZ4()
except:
    compressor = {'compression': 'lzf'}
h5py.enable_ipython_completer()

base_path = '/home/mike/cache/temp'

er_nc = '2m_temperature_2014-2020_reanalysis-era5-land.nc'

er0 = xr.open_dataset(os.path.join(base_path, er_nc)).t2m

er1 = er0[:30000]
er2 = er0[30000:]

shape = er1.shape
dtype = er1.dtype

start = time()
f = h5py.File(os.path.join(base_path, 'test.h5'), 'w', libver='latest')

time_ds = f.create_dataset('time', shape[0], dtype=int, maxshape=(None, ), chunks=(30000, ), **hdf5plugin.Zstd(1))
time_ds[:] = er1.time.values.astype('M8[s]').astype(int)
time_ds.make_scale('time')

lat_ds = f.create_dataset('lat', shape[1], dtype=er1.latitude.dtype, **hdf5plugin.Zstd(1))
lat_ds[:] = er1.latitude.values
lat_ds.make_scale('lat')

lon_ds = f.create_dataset('lon', shape[2], dtype=er1.longitude.dtype, **hdf5plugin.Zstd(1))
lon_ds[:] = er1.longitude.values
lon_ds.make_scale('lon')

ds = f.create_dataset('test1', shape, maxshape=(None, shape[1], shape[2]), chunks=(30000, 1, shape[2]), dtype=dtype, **hdf5plugin.Zstd(1))

dims = ds.dims
dims[0].attach_scale(time_ds)
dims[0].label = 'time'
dims[1].attach_scale(lat_ds)
dims[1].label = 'lat'
dims[2].attach_scale(lon_ds)
dims[2].label = 'lon'

for lat in range(len(er1.latitude.values)):
    print('-- lat ' + str(lat))
    temp = er1[:, lat, :].copy().load().values
    ds[:, lat, :] = temp
    del temp

f.close()


f = h5py.File(os.path.join(base_path, 'test.h5'), 'a', libver='latest')
ds = f['test1']
ds.resize((er0.shape[0], shape[1], shape[2]))

time_ds = f['time']
time_ds.resize((er0.shape[0], ))
time_ds[30000:] = er2.time.values.astype('M8[s]').astype(int)


for lat in range(len(er2.latitude.values)):
    print('-- lat ' + str(lat))
    temp = er2[:, lat, :].copy().load().values
    ds[30000:, lat, :] = temp
    del temp

f.close()

end = time()

print(end - start)


f = h5py.File(os.path.join(base_path, 'test.h5'), 'a', libver='latest')
dset = f['test1']

arr1 = dset[:, :3, :]
arr1[:] = 1

dset[:, :3, :] = arr1

f.close()



start = time()
old = h5py.File(os.path.join(base_path, 'test.h5'), 'r')

old_time = old['time']
old_lat = old['lat']
old_lon = old['lon']
old_ds = old['test1']

f = h5py.File(os.path.join(base_path, 'test2.h5'), 'w', libver='latest')

time_ds = f.create_dataset('time', old_time.shape, dtype=int, maxshape=(None, ), chunks=(30000, ))
time_ds[:] = old_time[:]
time_ds.make_scale('time')

lat_ds = f.create_dataset('lat', old_lat.shape, dtype=old_lat.dtype)
lat_ds[:] = old_lat[:]
lat_ds.make_scale('lat')

lon_ds = f.create_dataset('lon', old_lon.shape, dtype=old_lon.dtype)
lon_ds[:] = old_lon[:]
lon_ds.make_scale('lon')

ds = f.create_dataset('test2', old_ds.shape, maxshape=old_ds.shape, chunks=(30000, 1, old_lon.shape[0]), dtype=dtype)

dims = ds.dims
dims[0].attach_scale(time_ds)
dims[0].label = 'time'
dims[1].attach_scale(lat_ds)
dims[1].label = 'lat'
dims[2].attach_scale(lon_ds)
dims[2].label = 'lon'

for lat in range(old_lat.shape[0]):
    print('-- lat ' + str(lat))
    ds[:, lat, :] = old_ds[:, lat, :]

f.close()

old.close()

end = time()

print(end - start)



start = time()
old = h5py.File(os.path.join(base_path, 'test2.h5'), 'r')

old_time = old['time']
old_lat = old['lat']
old_lon = old['lon']
old_ds = old['test2']

f = h5py.File(os.path.join(base_path, 'test3.h5'), 'w', libver='latest')

time_ds = f.create_dataset('time', old_time.shape, dtype=int, maxshape=(None, ), chunks=(30000, ), **hdf5plugin.Zstd(1))
time_ds[:] = old_time[:]
time_ds.make_scale('time')

lat_ds = f.create_dataset('lat', old_lat.shape, dtype=old_lat.dtype, **hdf5plugin.Zstd(1))
lat_ds[:] = old_lat[:]
lat_ds.make_scale('lat')

lon_ds = f.create_dataset('lon', old_lon.shape, dtype=old_lon.dtype, **hdf5plugin.Zstd(1))
lon_ds[:] = old_lon[:]
lon_ds.make_scale('lon')

ds = f.create_dataset('test2', old_ds.shape, maxshape=old_ds.shape, chunks=(30000, 1, old_lon.shape[0]), dtype=dtype, **hdf5plugin.Zstd(1))

dims = ds.dims
dims[0].attach_scale(time_ds)
dims[0].label = 'time'
dims[1].attach_scale(lat_ds)
dims[1].label = 'lat'
dims[2].attach_scale(lon_ds)
dims[2].label = 'lon'

for lat in range(old_lat.shape[0]):
    print('-- lat ' + str(lat))
    ds[:, lat, :] = old_ds[:, lat, :]

f.close()

old.close()

end = time()

print(end - start)


start = time()
old = h5py.File(os.path.join(base_path, 'test3.h5'), 'r')

old_time = old['time']
old_lat = old['lat']
old_lon = old['lon']
old_ds = old['test2']

f = h5py.File(os.path.join(base_path, 'test4.h5'), 'w', libver='latest')

time_ds = f.create_dataset('time', old_time.shape, dtype=int, maxshape=(None, ), chunks=(30000, ), **hdf5plugin.Zstd(1))
time_ds[:] = old_time[:]
time_ds.make_scale('time')

lat_ds = f.create_dataset('lat', old_lat.shape, dtype=old_lat.dtype, **hdf5plugin.Zstd(1))
lat_ds[:] = old_lat[:]
lat_ds.make_scale('lat')

lon_ds = f.create_dataset('lon', old_lon.shape, dtype=old_lon.dtype, **hdf5plugin.Zstd(1))
lon_ds[:] = old_lon[:]
lon_ds.make_scale('lon')

ds = f.create_dataset('test2', old_ds.shape, maxshape=old_ds.shape, chunks=(30000, 1, old_lon.shape[0]), dtype=dtype, **hdf5plugin.Zstd(1))

dims = ds.dims
dims[0].attach_scale(time_ds)
dims[0].label = 'time'
dims[1].attach_scale(lat_ds)
dims[1].label = 'lat'
dims[2].attach_scale(lon_ds)
dims[2].label = 'lon'

for lat in range(old_lat.shape[0]):
    print('-- lat ' + str(lat))
    ds[:, lat, :] = old_ds[:, lat, :]

f.close()

old.close()

end = time()

print(end - start)



start = time()
old = h5py.File(os.path.join(base_path, 'test3.h5'), 'r')

old_time = old['time']
old_lat = old['lat']
old_lon = old['lon']
old_ds = old['test2']

f = h5py.File(os.path.join(base_path, 'test5.h5'), 'w', libver='latest')

time_ds = f.create_dataset('time', old_time.shape, dtype=int, maxshape=(None, ), chunks=(30000, ), **hdf5plugin.Zstd(1))
time_ds[:] = old_time[:]
time_ds.make_scale('time')

lat_ds = f.create_dataset('lat', old_lat.shape, dtype=old_lat.dtype, **hdf5plugin.Zstd(1))
lat_ds[:] = old_lat[:]
lat_ds.make_scale('lat')

lon_ds = f.create_dataset('lon', old_lon.shape, dtype=old_lon.dtype, **hdf5plugin.Zstd(1))
lon_ds[:] = old_lon[:]
lon_ds.make_scale('lon')

ds = f.create_dataset('test2', old_ds.shape, maxshape=old_ds.shape, chunks=(30000, 1, old_lon.shape[0]), dtype=dtype, **hdf5plugin.Blosc())

dims = ds.dims
dims[0].attach_scale(time_ds)
dims[0].label = 'time'
dims[1].attach_scale(lat_ds)
dims[1].label = 'lat'
dims[2].attach_scale(lon_ds)
dims[2].label = 'lon'

for lat in range(old_lat.shape[0]):
    print('-- lat ' + str(lat))
    ds[:, lat, :] = old_ds[:, lat, :]

f.close()

old.close()

end = time()

print(end - start)


start = time()
old = h5py.File(os.path.join(base_path, 'test5.h5'), 'r')

old_time = old['time']
old_lat = old['lat']
old_lon = old['lon']
old_ds = old['test2']

f = h5py.File(os.path.join(base_path, 'test6.h5'), 'w', libver='latest')

time_ds = f.create_dataset('time', old_time.shape, dtype=int, maxshape=(None, ), chunks=(30000, ), **hdf5plugin.Zstd(1))
time_ds[:] = old_time[:]
time_ds.make_scale('time')

lat_ds = f.create_dataset('lat', old_lat.shape, dtype=old_lat.dtype, **hdf5plugin.Zstd(1))
lat_ds[:] = old_lat[:]
lat_ds.make_scale('lat')

lon_ds = f.create_dataset('lon', old_lon.shape, dtype=old_lon.dtype, **hdf5plugin.Zstd(1))
lon_ds[:] = old_lon[:]
lon_ds.make_scale('lon')

ds = f.create_dataset('test2', old_ds.shape, maxshape=old_ds.shape, chunks=(30000, 1, old_lon.shape[0]), dtype='int16', **hdf5plugin.Blosc())

dims = ds.dims
dims[0].attach_scale(time_ds)
dims[0].label = 'time'
dims[1].attach_scale(lat_ds)
dims[1].label = 'lat'
dims[2].attach_scale(lon_ds)
dims[2].label = 'lon'

for lat in range(old_lat.shape[0]):
    print('-- lat ' + str(lat))
    data = old_ds[:, lat, :]
    na_bool = np.isnan(data)
    data[na_bool] = -99
    ds[:, lat, :] = (data * 100).astype('int16')
    del data
    del na_bool

f.close()

old.close()

end = time()

print(end - start)


start = time()
old = h5py.File(os.path.join(base_path, 'test6.h5'), 'r')

old_time = old['time']
old_lat = old['lat']
old_lon = old['lon']
old_ds = old['test2']

f = h5py.File(os.path.join(base_path, 'test7.h5'), 'w', libver='latest')

time_ds = f.create_dataset('time', old_time.shape, dtype=int, maxshape=(None, ), chunks=(30000, ), **hdf5plugin.Zstd(1))
time_ds[:] = old_time[:]
time_ds.make_scale('time')

lat_ds = f.create_dataset('lat', old_lat.shape, dtype=old_lat.dtype, **hdf5plugin.Zstd(1))
lat_ds[:] = old_lat[:]
lat_ds.make_scale('lat')

lon_ds = f.create_dataset('lon', old_lon.shape, dtype=old_lon.dtype, **hdf5plugin.Zstd(1))
lon_ds[:] = old_lon[:]
lon_ds.make_scale('lon')

ds = f.create_dataset('test2', old_ds.shape, maxshape=old_ds.shape, chunks=(30000, 1, old_lon.shape[0]), dtype='int16', **hdf5plugin.Blosc())

dims = ds.dims
dims[0].attach_scale(time_ds)
dims[0].label = 'time'
dims[1].attach_scale(lat_ds)
dims[1].label = 'lat'
dims[2].attach_scale(lon_ds)
dims[2].label = 'lon'

for lat in range(old_lat.shape[0]):
    print('-- lat ' + str(lat))
    ds[:, lat, :] = old_ds[:, lat, :]

f.close()

old.close()

end = time()

print(end - start)


old = h5py.File(os.path.join(base_path, 'test.nc'), 'r')

old_ds = old['netcdf']['t2m']

ds = old.create_dataset('/netcdf/test', old_ds.shape, maxshape=old_ds.shape, dtype='i2', **hdf5plugin.Blosc())

ds[:] = old_ds[:]
ds.attrs.update(dict(old_ds.attrs))

old.close()

dataset = xr.open_dataset(os.path.join(base_path, 'test.nc'), engine='h5netcdf', group='netcdf')

dataset.close()



time_str_conversion = {'days': 'datetime64[D]',
                       'hours': 'datetime64[h]',
                       'minutes': 'datetime64[m]',
                       'seconds': 'datetime64[s]',
                       'milliseconds': 'datetime64[ms]'}


def encode_datetime(data, units=None, calendar='gregorian'):
    """

    """
    if units is None:
        output = data.astype('datetime64[s]').astype(int)
    else:
        if '1970-01-01' in units:
            time_unit = units.split()[0]
            output = data.astype(time_str_conversion[time_unit]).astype(int)
        else:
            output = cftime.date2num(data.astype('datetime64[s]').tolist(), units, calendar)

    return output


def decode_datetime(data, units=None, calendar='gregorian'):
    """

    """
    if units is None:
        output = data.astype('datetime64[s]')
    else:
        if '1970-01-01' in units:
            time_unit = units.split()[0]
            output = data.astype(time_str_conversion[time_unit])
        else:
            output = cftime.num2pydate(data, units, calendar).astype('datetime64[s]')

    return output


def encode_data(data, dtype, missing_value=None, add_offset=0, scale_factor=1, units=None, calendar=None, **kwargs):
    """

    """
    if 'datetime64' in data.dtype.name:
        if (calendar is None):
            raise TypeError('data is datetime, so calendar must be assigned.')
        output = encode_datetime(data, units, calendar)
    else:
        output = (data - add_offset)/scale_factor

        if isinstance(missing_value, (int, np.number)):
            output[np.isnan(output)] = missing_value

        output = output.astype(dtype)

    return output


def decode_data(data, dtype=None, missing_value=None, add_offset=0, scale_factor=1, units=None, calendar=None, **kwargs):
    """

    """
    if isinstance(calendar, str):
        output = decode_datetime(data, units, calendar)
    else:
        output = data.astype(dtype)

        if isinstance(missing_value, (int, np.number)):
            output[output == missing_value] = np.nan

        output = (output * scale_factor) + add_offset

    return output


def is_scale(dataset):
    """

    """
    check = h5py.h5ds.is_scale(dataset._id)

    return check


def extend_coords(paths, group=None):
    """

    """
    coords_dict = {}

    for path in paths:
        f = h5py.File(path, 'r')

        if isinstance(group, str):
            f1 = f[group]
        else:
            f1 = f

        ds_list = list(f1.keys())

        for ds_name in ds_list:
            if is_scale(f1[ds_name]):
                ds = f1[ds_name]

                if ds_name in coords_dict:
                    coords_dict[ds_name] = np.union1d(coords_dict[ds_name], ds[:])
                else:
                    coords_dict[ds_name] = ds[:]

        f.close()

    return coords_dict


def extend_variables(paths, coords_dict, group=None):
    """

    """
    vars_dict = {}

    for path in paths:
        f = h5py.File(path, 'r')

        if isinstance(group, str):
            f1 = f[group]
        else:
            f1 = f

        ds_list = list(f1.keys())

        for ds_name in ds_list:
            if not is_scale(f1[ds_name]):
                ds = f1[ds_name]

                dims = []
                slice_index = []

                for dim in ds.dims:
                    dim_name = dim[0].name.split('/')[-1]
                    dims.append(dim_name)
                    arr_index = np.where(np.isin(coords_dict[dim_name], dim[0][:]))[0]
                    slice1 = slice(arr_index.min(), arr_index.max() + 1)
                    slice_index.append(slice1)

                if ds_name in vars_dict:
                    if not np.in1d(vars_dict[ds_name]['dims'], dims).all():
                        raise ValueError('dims are not consistant between the same named datasets.')
                    if vars_dict[ds_name]['dtype'] != ds.dtype:
                        raise ValueError('dtypes are not consistant between the same named datasets.')

                    vars_dict[ds_name]['data'][path] = {'dims_order': tuple(dims), 'slice_index': tuple(slice_index)}
                else:
                    shape = tuple([coords_dict[dim_name].shape[0] for dim_name in dims])
                    vars_dict[ds_name] = {'data': {path: {'dims_order': tuple(dims), 'slice_index': tuple(slice_index)}}, 'dims': tuple(dims), 'shape': shape, 'dtype': ds.dtype, 'fillvalue': ds.fillvalue}

        f.close()

    return vars_dict


def create_nc_dataset(hdf, xr_dataset, var_name, chunks, compressor, unlimited_dims):
    """

    """
    shape = xr_dataset[var_name].shape
    dims = xr_dataset[var_name].dims
    maxshape = tuple([s if dims[i] not in unlimited_dims else None for i, s in enumerate(shape)])

    encoding = xr_dataset[var_name].encoding.copy()
    if 'dtype' not in encoding:
        encoding['dtype'] = xr_dataset[var_name].dtype
    attrs = xr_dataset[var_name].attrs.copy()

    enc = {k: v for k, v in encoding.items() if k in encode_data.__code__.co_varnames}
    enc['dtype'] = enc['dtype'].name

    if 'calendar' in enc:
        enc['units'] = 'seconds since 1970-01-01 00:00:00'

    if 'missing_value' in enc:
        enc['_FillValue'] = enc['missing_value']
        fillvalue = enc['missing_value']
    else:
        fillvalue = None

    chunks1 = guess_chunk(shape, maxshape, encoding['dtype'])
    # chunks1 = None

    if isinstance(chunks, dict):
        if var_name in chunks:
            chunks1 = chunks[var_name]

    ds = hdf.create_dataset(var_name, shape, chunks=chunks1, maxshape=maxshape, dtype=encoding['dtype'], fillvalue=fillvalue, **compressor)

    # if (chunks1 is None):
    #     old_chunks = ds.chunks
    #     _ = hdf.pop(var_name)
    #     new_chunks = tuple([int(c*dim_chunk_mupliplier) if int(c*dim_chunk_mupliplier) <= shape[i] else shape[i] for i, c in enumerate(old_chunks)])
    #     ds = hdf.create_dataset(var_name, shape, chunks=new_chunks, maxshape=maxshape, dtype=encoding['dtype'], **compressor)

    if ('scale_factor' in enc) or ('add_offset' in enc) or ('calendar' in enc):
        if ds.chunks == shape:
            ds[:] = encode_data(xr_dataset[var_name].copy().load().values, **enc)
        else:
            new_slices, source_slices = copy_chunks(shape, chunks1)

            for new_slice, source_slice in zip(new_slices, source_slices):
                # print(new_slice, source_slice)
                ds[new_slice] = encode_data(xr_dataset[var_name][source_slice].copy().load().values, **enc)

            # for chunk in ds.iter_chunks():
                # print(chunk)

                # data = xr_dataset[var_name][chunk].copy().load().values
                # data_bool = ~np.isnan(data)

                # if np.any(data_bool):
                #     slice_arrays = [(s.min(), s.max() + 1) for s in np.where(data_bool)]
                #     slices = tuple([slice(chunk[i].start + s[0], chunk[i].start + s[1]) for i, s in enumerate(slice_arrays)])
                #     source_slices = tuple([slice(s[0], s[1]) for s in slice_arrays])
                #     ds[slices] = encode_data(data[source_slices], **enc)

                # ds[chunk] = encode_data(xr_dataset[var_name][chunk].copy().load().values, **enc)
    else:
        if ds.chunks == shape:
            ds[:] = xr_dataset[var_name].copy().load().values
        else:
            new_slices, source_slices = copy_chunks(shape, chunks1)

            for new_slice, source_slice in zip(new_slices, source_slices):
                # print(new_slice, source_slice)
                ds[new_slice] = xr_dataset[var_name][source_slice].copy().load().values

            # for chunk in ds.iter_chunks():
                # print(chunk)
                # data = xr_dataset[var_name][chunk].copy().load().values
                # data_bool = ~np.isnan(data)
                # if np.any(data_bool):
                #     slice_arrays = [(s.min(), s.max() + 1) for s in np.where(data_bool)]
                #     slices = tuple([slice(chunk[i].start + s[0], chunk[i].start + s[1]) for i, s in enumerate(slice_arrays)])
                #     source_slices = tuple([slice(s[0], s[1]) for s in slice_arrays])
                #     ds[slices] = encode_data(data[source_slices], **enc)
                # ds[chunk] = xr_dataset[var_name][chunk].copy().load().values

    # elif 'float' in enc['dtype']:
    #     enc['_FillValue'] = np.array([np.nan], dtype='float32')

    _ = enc.pop('dtype')
    # print(enc)
    attrs.update(enc)

    ds.attrs.update(attrs)

    if var_name in xr_dataset.dims:
        # p = list(xr_dataset.dims).index(var_name)
        # ds_attrs = {'_Netcdf4Coordinates': np.array([p], dtype='int16'), '_Netcdf4Dimid': p}
        # ds_attrs = {'_Netcdf4Dimid': p}

        # ds.attrs.update(ds_attrs)

        ds.make_scale(var_name)
    # else:
    #     ds_dims = list(xr_dataset.dims)

    #     ds_attrs = {'_Netcdf4Coordinates': np.array([ds_dims.index(dim) for dim in dims], dtype='int16'), '_Netcdf4Dimid': 2}

    #     ds.attrs.update(ds_attrs)

    ds_dims = ds.dims
    for i, dim in enumerate(dims):
        if dim != var_name:
            ds_dims[i].attach_scale(hdf[dim])
            ds_dims[i].label = dim

    return ds


def xr_save_netcdf4(xr_dataset, path, group=None, chunks=None, unlimited_dims=None):
    """
    
    Parameters
    ----------
    xr_dataset : xr.Dataset
    path : str or pathlib
        Output path.
    chunks : dict of tuple or None
        The chunking for the variables. All variables without a chunking defined will be automatically chunked.
    group : str
        The group to put the netcdf datasets.
    unlimited_dims : list or str
        The dimensions that should be marked as unlimited.

    """
    if isinstance(unlimited_dims, str):
        unlimited_dims = [unlimited_dims]
    else:
        unlimited_dims = []

    xr_dims_list = list(xr_dataset.dims)

    with h5py.File(path, 'w', libver='latest', rdcc_nbytes=3*1024*1024) as f:

        if isinstance(group, str):
            g = f.create_group(group)
        else:
            g = f
    
        ## Create coords
        for coord in xr_dims_list:
            _ = create_nc_dataset(g, xr_dataset, coord, chunks, compressor, unlimited_dims)
    
        ## Create data vars
        for var in list(dataset.data_vars):
            _ = create_nc_dataset(g, xr_dataset, var, chunks, compressor, unlimited_dims)
    
        ## Dataset attrs
        # attrs = {'_NCProperties': b'version=2,h5netcdf=1.0.2,hdf5=1.12.2,h5py=3.7.0'}
        attrs = {}
        attrs.update(dataset.attrs)
        g.attrs.update(attrs)


def combine_netcdf4(paths, new_path, group=None, chunks=None, unlimited_dims=None):
    """

    """
    if isinstance(unlimited_dims, str):
        unlimited_dims = [unlimited_dims]
    else:
        unlimited_dims = []

    ## Create new file
    with h5py.File(new_path, 'w', libver='latest', rdcc_nbytes=3*1024*1024) as nf:

        if isinstance(group, str):
            nf1 = nf.create_group(group)
        else:
            nf1 = nf
    
        ## Get the extended coords
        coords_dict = extend_coords(paths, group)
    
        ## Add the coords as datasets
        for coord, arr in coords_dict.items():
            shape = arr.shape

            maxshape = tuple([s if s not in unlimited_dims else None for s in shape])

            chunks1 = guess_chunk(shape, maxshape, arr.dtype)
    
            if isinstance(chunks, dict):
                if coord in chunks:
                    chunks1 = chunks[coord]

            ds = nf1.create_dataset(coord, shape, chunks=chunks1, maxshape=maxshape, dtype=arr.dtype, **compressor)
    
            # old_chunks = ds.chunks
    
            # if (old_chunks != shape) and (chunks1 is None):
            #     _ = nf1.pop(coord)
            #     new_chunks = tuple([int(c*dim_chunk_mupliplier) if int(c*dim_chunk_mupliplier) <= shape[i] else shape[i] for i, c in enumerate(old_chunks)])
            #     ds = nf1.create_dataset(coord, shape, chunks=new_chunks, maxshape=maxshape, dtype=arr.dtype, **compressor)
    
            ds[:] = arr
    
            ds.make_scale(coord)
    
            # p = list(ds.dims).index(coord)
            # ds_attrs = {'_Netcdf4Coordinates': np.array([p], dtype='int16'), '_Netcdf4Dimid': p}
            # ds.attrs.update(ds_attrs)
    
        ## Add the variables as datasets
        vars_dict = extend_variables(paths, coords_dict, group)
    
        for dim_name in vars_dict:
            shape = vars_dict[dim_name]['shape']
            dims = vars_dict[dim_name]['dims']
            maxshape = tuple([s if dims[i] not in unlimited_dims else None for i, s in enumerate(shape)])
    
            chunks1 = guess_chunk(shape, maxshape, vars_dict[dim_name]['dtype'])
    
            if isinstance(chunks, dict):
                if dim_name in chunks:
                    chunks1 = chunks[dim_name]
    
            ds = nf1.create_dataset(dim_name, shape, chunks=chunks1, maxshape=maxshape, dtype=vars_dict[dim_name]['dtype'], fillvalue=vars_dict[dim_name]['fillvalue'], **compressor)
    
            # old_chunks = ds.chunks
    
            # if (old_chunks != shape) and (chunks1 is None):
            #     _ = nf1.pop(dim_name)
            #     new_chunks = tuple([int(c*dim_chunk_mupliplier) if int(c*dim_chunk_mupliplier) <= shape[i] else shape[i] for i, c in enumerate(old_chunks)])
            #     ds = nf1.create_dataset(dim_name, shape, chunks=new_chunks, maxshape=maxshape, dtype=vars_dict[dim_name]['dtype'], **compressor)
    
            ds_dims = ds.dims
            for i, dim in enumerate(dims):
                ds_dims[i].attach_scale(nf1[dim])
                ds_dims[i].label = dim
    
            # ds_dims = list(ds.dims)
    
            # ds_attrs = {'_Netcdf4Coordinates': np.array([ds_dims.index(dim) for dim in dims], dtype='int16')}
    
            # ds.attrs.update(ds_attrs)
    
            # Load the data by chunk
            for path in vars_dict[dim_name]['data']:
                f = h5py.File(path, 'r')
    
                if isinstance(group, str):
                    f1 = f[group]
                else:
                    f1 = f
    
                ds_old = f1[dim_name]
    
                source_slice_index = vars_dict[dim_name]['data'][path]['slice_index']
                dims_order = vars_dict[dim_name]['data'][path]['dims_order']
    
                source_dim_index = [dims_order.index(dim) for dim in dims]

                new_slices, source_slices = copy_chunks(shape, chunks1, source_slice_index, source_dim_index)

                for new_slice, source_slice in zip(new_slices, source_slices):
                    # print(new_slice, source_slice)
                    ds[new_slice] = ds_old[source_slice]

                # for chunk in ds.iter_chunks(slice_index):
                #     # print(chunk)
                #     source_chunk = tuple([slice(chunk[i].start - slice_index[i].start, chunk[i].stop - slice_index[i].start) for i in dims_index])
                #     ds[chunk] = ds_old[source_chunk]
    
                f.close()
    
        ## Assign attrs
        for path in paths:
            f = h5py.File(path, 'r')
    
            if isinstance(group, str):
                f1 = f[group]
            else:
                f1 = f
    
            ds_list = list(f1.keys())
    
            for ds_name in ds_list:
                attrs = {k: v for k, v in f1[ds_name].attrs.items() if k not in ['DIMENSION_LABELS', 'DIMENSION_LIST', 'CLASS', 'NAME', '_Netcdf4Coordinates', '_Netcdf4Dimid', 'REFERENCE_LIST']}
                # print(attrs)
                nf1[ds_name].attrs.update(attrs)


def index_coords(hdf_path: str, selection: dict, group: str = None):
    """

    """
    # with h5py.File(hdf_path, 'r') as f:
    f = h5py.File(hdf_path, 'r')

    if isinstance(group, str):
        f1 = f[group]
    else:
        f1 = f

    coords_list = [ds_name for ds_name in f1 if is_scale(f1[ds_name])]

    index_coords_dict = {}

    for coord, sel in selection.items():
        if coord not in coords_list:
            raise ValueError(coord + ' is not in the coordiantes of the hdf5 file.')

        attrs = dict(f1[coord].attrs)
        enc = {k: v for k, v in attrs.items() if k in decode_data.__code__.co_varnames}

        arr = decode_data(f1[coord][:], **enc)

        if isinstance(sel, slice):
            if 'datetime64' in arr.dtype.name:
                start = np.datetime64(sel.start, 's')
                end = np.datetime64(sel.stop, 's')
                bool_index = (start <= arr) & (arr < end)
            else:
                bool_index = (sel.start <= arr) & (arr < sel.stop)

        else:
            if isinstance(sel, (int, float)):
                sel = [sel]

            try:
                sel1 = np.array(sel)
            except:
                raise TypeError('selection input could not be coerced to an ndarray.')

            if sel1.dtype.name == 'bool':
                if sel1.shape[0] != arr.shape[0]:
                    raise ValueError('The boolean array does not have the same length as the coord array.')
                bool_index = sel1
            else:
                bool_index = np.in1d(arr, sel1)

        int_index = np.where(bool_index)[0]
        slice_index = slice(int_index.min(), int_index.max())

        index_coords_dict[coord] = {'bool_index': bool_index, 'int_index': int_index, 'slice_index': slice_index}

    return index_coords_dict
























test_nc = '/home/mike/cache/temp/test.nc'
path0 = '/home/mike/cache/temp/test11.h5'
path1 = '/home/mike/cache/temp/test12a.h5'
path2 = '/home/mike/cache/temp/test12b.h5'
path3 = '/home/mike/cache/temp/test12c.h5'

new_path = '/home/mike/cache/temp/test14.h5'
hdf_path = new_path
path4 = '/home/mike/cache/temp/test15.h5'
path5 = '/home/mike/cache/temp/test16.h5'

paths = [path1, path2, path3]

dataset = xr.open_dataset(os.path.join(base_path, '2m_temperature_2014-2020_reanalysis-era5-land.nc'))

dataset.t2m[:2000].to_dataset().to_netcdf(test_nc, engine='h5netcdf')

dataset = xr.open_dataset(path0, engine='h5netcdf')
dataset = xr.open_dataset(new_path, engine='h5netcdf')

ds1 = dataset.t2m[:20000].to_dataset()
ds2 = dataset.t2m[20000:40000].to_dataset()
ds3 = dataset.t2m[40000:].to_dataset()

ds1 = dataset.sel(longitude=slice(168, 169.9), latitude=slice(-44, -45.9)).isel(time=slice(0, 2500))


dataset.t2m.encoding.update({'dtype': np.dtype('int32')})
xr_save_netcdf4(ds1, path0, unlimited_dims=['time'])
xr_save_netcdf4(dataset, path4, unlimited_dims=['time'])

xr_save_netcdf4(dataset, path1, chunks={'t2m': (30000, 1, 124)}, unlimited_dims=['time'])

xr_save_netcdf4(ds1, path1, unlimited_dims=['time'])
xr_save_netcdf4(ds2, path2, unlimited_dims=['time'])
xr_save_netcdf4(ds3, path3, unlimited_dims=['time'])



f1 = h5py.File(path1, 'r')

f1 = h5py.File(test_nc, 'r')
f1 = h5py.File(new_path, 'r')
f1 = h5py.File(path0, 'r')


start = time()
hdf5tools.combine_hdf5(paths, new_path, unlimited_dims=['time'])
end = time()

print(end - start)

start = time()
hdf5tools.combine_hdf5([new_path], path4, unlimited_dims=['time'])
end = time()

print(end - start)



start = time()
xr_save_netcdf4(dataset, path4, unlimited_dims=['time'])
end = time()

print(end - start)


combine_netcdf4([path0], path4, unlimited_dims=['time'])


combine_netcdf4([path4], path5, unlimited_dims=['time'])

hdf5tools.xr_to_hdf5(ds1, path0, chunks={'t2m': (2500, 19, 20)}, unlimited_dims=['time'])


selection = {'time': slice('2014-01-01', '2015-01-01')}


f1 = h5py.File(new_path, 'a')
f2 = h5py.File(new_path, 'r')

out1 = f1['t2m'][:100, :, :]

out2 = f2['t2m'][200:300, :, :]



f1 = h5py.File(path4, 'w')

arr = np.array([np.datetime64('2019-09-22T17:38:30')])
arr = decode_datetime(f1['time'][:], f1['time'].attrs['units'])

dtype = h5py.opaque_dtype(arr.dtype)

ds = f1.create_dataset('time', arr.shape, dtype=h5py.opaque_dtype(arr.dtype), data=arr.astype(dtype))
ds.make_scale('time')

f1['t2m'].dims[0].attach_scale(ds)



h1 = io.BytesIO()

with open(path0, 'rb') as b:
    h1 = io.BytesIO(b.read())


f1 = h5py.File(h3, 'r')
f2 = h5py.File(h1, 'w')
f1 = h5py.File(chunks1[0], 'r')








out1 = ds[:]

ds = f2['t2m']
enc = dict(ds.attrs)

missing_value = -32767
scale_factor = 0.0008487733722746316
dtype = 'int16'
add_offset = 280.70142650442716
asdtype = 'float32'


def decode1(ds, dtype, missing_value, scale_factor, add_offset):
    """

    """
    out1 = np.empty(ds.shape, dtype=asdtype)

    ds.read_direct(out1)

    if isinstance(missing_value, (int, np.number)):
        out1[out1 == missing_value] = np.nan

    out1 = (out1 * scale_factor) + add_offset



output = data.astype(dtype)


codec = numcodecs.FixedScaleOffset(add_offset, scale_factor, dtype, asdtype)

out1 = codec.decode(out1)




CHUNK_BASE = 32*1024    # Multiplier by which chunks are adjusted
CHUNK_MIN = 32*1024      # Soft lower limit (32k)
CHUNK_MAX = 3*1024*1024   # Hard upper limit (4M)




def _get_default_chunksizes(dimsizes, dtype):
    # This is a modified version of h5py's default chunking heuristic
    # https://github.com/h5py/h5py/blob/aa31f03bef99e5807d1d6381e36233325d944279/h5py/_hl/filters.py#L334-L389
    # (published under BSD-3-Clause, included at licenses/H5PY_LICENSE.txt)
    # See also https://github.com/h5py/h5py/issues/2029 for context.

    type_size = np.dtype(dtype).itemsize

    is_unlimited = np.array([x is None for x in dimsizes])

    # For unlimited dimensions start with a guess of 1024
    chunks = np.array([x if x is not None else 1024 for x in dimsizes], dtype="=f8")

    ndims = len(dimsizes)
    if ndims == 0:
        raise ValueError("Chunks not allowed for scalar datasets.")

    if not np.all(np.isfinite(chunks)):
        raise ValueError("Illegal value in chunk tuple")

    # Determine the optimal chunk size in bytes using a PyTables expression.
    # This is kept as a float.
    dset_size = np.product(chunks[~is_unlimited]) * type_size
    target_size = CHUNK_BASE * (2 ** np.log10(dset_size / (1024 * 1024)))
    target_size = CHUNK_MAX

    if target_size > CHUNK_MAX:
        target_size = CHUNK_MAX
    elif target_size < CHUNK_MIN:
        target_size = CHUNK_MIN

    i = 0
    while True:
        # Repeatedly loop over the axes, dividing them by 2.
        # Start by reducing unlimited axes first.
        # Stop when:
        # 1a. We're smaller than the target chunk size, OR
        # 1b. We're within 50% of the target chunk size, AND
        #  2. The chunk is smaller than the maximum chunk size

        idx = i % ndims

        chunk_bytes = np.product(chunks) * type_size

        done = (
            chunk_bytes < target_size
            or abs(chunk_bytes - target_size) / target_size < 0.5
        ) and chunk_bytes < CHUNK_MAX

        if done:
            break

        if np.product(chunks) == 1:
            break  # Element size larger than CHUNK_MAX

        nelem_unlim = np.product(chunks[is_unlimited])

        if nelem_unlim == 1 or is_unlimited[idx]:
            chunks[idx] = np.ceil(chunks[idx] / 2.0)

        i += 1

    return tuple(int(x) for x in chunks)



CHUNK_BASE = 32*1024    # Multiplier by which chunks are adjusted
CHUNK_MIN = 32*1024      # Soft lower limit (32k)
CHUNK_MAX = 3*1024*1024   # Hard upper limit (4M)


def guess_chunk(shape, maxshape, dtype):
    """ Guess an appropriate chunk layout for a dataset, given its shape and
    the size of each element in bytes.  Will allocate chunks only as large
    as MAX_SIZE.  Chunks are generally close to some power-of-2 fraction of
    each axis, slightly favoring bigger values for the last index.
    Undocumented and subject to change without warning.
    """
    # pylint: disable=unused-argument

    # For unlimited dimensions we have to guess 1024
    shape1 = []
    for i, x in enumerate(maxshape):
        if x is None:
            if shape[i] > 1024:
                shape1.append(shape[i])
            else:
                shape1.append(1024)
        else:
            shape1.append(x)

    shape = tuple(shape1)

    ndims = len(shape)
    if ndims == 0:
        raise ValueError("Chunks not allowed for scalar datasets.")

    chunks = np.array(shape, dtype='=f8')
    if not np.all(np.isfinite(chunks)):
        raise ValueError("Illegal value in chunk tuple")

    # Determine the optimal chunk size in bytes using a PyTables expression.
    # This is kept as a float.
    typesize = dtype.itemsize
    # dset_size = np.product(chunks)*typesize
    # target_size = CHUNK_BASE * (2**np.log10(dset_size/(1024.*1024)))

    # if target_size > CHUNK_MAX:
    #     target_size = CHUNK_MAX
    # elif target_size < CHUNK_MIN:
    #     target_size = CHUNK_MIN

    target_size = CHUNK_MAX

    idx = 0
    while True:
        # Repeatedly loop over the axes, dividing them by 2.  Stop when:
        # 1a. We're smaller than the target chunk size, OR
        # 1b. We're within 50% of the target chunk size, AND
        #  2. The chunk is smaller than the maximum chunk size

        chunk_bytes = np.product(chunks)*typesize

        if (chunk_bytes < target_size or \
         abs(chunk_bytes-target_size)/target_size < 0.5) and \
         chunk_bytes < CHUNK_MAX:
            break

        if np.product(chunks) == 1:
            break  # Element size larger than CHUNK_MAX

        chunks[idx%ndims] = np.ceil(chunks[idx%ndims] / 2.0)
        idx += 1

    return tuple(int(x) for x in chunks)


def copy_chunks(shape, chunks, source_slice_index=None, source_dim_index=None, factor=3):
    """

    """
    n_shapes = []

    if isinstance(source_slice_index, (list, tuple)) and isinstance(source_dim_index, (list, tuple)):
        copy_shape = tuple([s*factor if s*factor <= (source_slice_index[i].stop - source_slice_index[i].start) else (source_slice_index[i].stop - source_slice_index[i].start) for i, s in enumerate(chunks)])

        for i, s in enumerate(copy_shape):
            shapes = np.arange(source_slice_index[i].start, source_slice_index[i].stop, s)
            n_shapes.append(shapes)

        cart = cartesian(n_shapes)

        slices = []
        append = slices.append
        for arr in cart:
            slices1 = tuple([slice(s, s + copy_shape[i]) if s + copy_shape[i] <= source_slice_index[i].stop else slice(s, source_slice_index[i].stop) for i, s in enumerate(arr)])
            append(slices1)

        source_slices = []
        append = source_slices.append
        for s in slices:
            source_chunk = tuple([slice(s[i].start - source_slice_index[i].start, s[i].stop - source_slice_index[i].start) for i in source_dim_index])
            append(source_chunk)

    else:
        copy_shape = tuple([s*factor if s*factor <= shape[i] else shape[i] for i, s in enumerate(chunks)])
        for i, s in enumerate(copy_shape):
            shapes = np.arange(0, shape[i], s)
            n_shapes.append(shapes)

        cart = cartesian(n_shapes)

        slices = []
        append = slices.append
        for arr in cart:
            slices1 = tuple([slice(s, s + copy_shape[i]) if s + copy_shape[i] <= shape[i] else slice(s, shape[i]) for i, s in enumerate(arr)])
            append(slices1)
    
        source_slices = slices

    return slices, source_slices










def cartesian(arrays, out=None):
    """
    Generate a cartesian product of input arrays.

    Parameters
    ----------
    arrays : list of array-like
        1-D arrays to form the cartesian product of.
    out : ndarray
        Array to place the cartesian product in.

    Returns
    -------
    out : ndarray
        2-D array of shape (M, len(arrays)) containing cartesian products
        formed of input arrays.

    Examples
    --------
    >>> cartesian(([1, 2, 3], [4, 5], [6, 7]))
    array([[1, 4, 6],
           [1, 4, 7],
           [1, 5, 6],
           [1, 5, 7],
           [2, 4, 6],
           [2, 4, 7],
           [2, 5, 6],
           [2, 5, 7],
           [3, 4, 6],
           [3, 4, 7],
           [3, 5, 6],
           [3, 5, 7]])

    """

    arrays = [np.asarray(x) for x in arrays]
    dtype = arrays[0].dtype

    n = np.prod([x.size for x in arrays])
    if out is None:
        out = np.zeros([n, len(arrays)], dtype=dtype)

    m = int(n / arrays[0].size)
    out[:,0] = np.repeat(arrays[0], m)
    if arrays[1:]:
        cartesian(arrays[1:], out=out[0:m, 1:])
        for j in range(1, arrays[0].size):
            out[j*m:(j+1)*m, 1:] = out[0:m, 1:]

    return out



















