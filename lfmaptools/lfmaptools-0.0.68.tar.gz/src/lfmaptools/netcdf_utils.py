from typing import Dict, Hashable, List, Optional, Tuple

import netCDF4 as nc
import numpy as np
import xarray as xr
from numpy.lib.recfunctions import rename_fields as np_rename_fields


def nc2np(filename, var=None):

    with nc.Dataset(filename, "r") as rgrp:

        attrs = rgrp.__dict__

        tiles = list(rgrp.groups)
        nc_variables = list(rgrp[tiles[0]].variables)

        if var is not None:
            if isinstance(var, list):
                for v in var:
                    if v not in nc_variables:
                        raise ValueError(
                            "variable {} not in netcdf file {}".format(v, filename)
                        )
            else:
                if var not in nc_variables:
                    raise ValueError(
                        "variable {} not in netcdf file {}".format(var, filename)
                    )

        nX = attrs["nXpertile"]
        nY = attrs["nYpertile"]
        nXY = nX * nY
        nrows = len(tiles) * nXY

        if var is None:
            variables = nc_variables.copy()
        else:
            variables = []
            if "x_distance" in nc_variables:
                variables.append("x_distance")
            if "x" in nc_variables:
                variables.append("x")
            if "y_distance" in nc_variables:
                variables.append("y_distance")
            if "y" in nc_variables:
                variables.append("y")
            if "lat" in nc_variables:
                variables.append("lat")
            if "latitude" in nc_variables:
                variables.append("latitude")
            if "lon" in nc_variables:
                variables.append("lon")
            if "longitude" in nc_variables:
                variables.append("longitude")
            if isinstance(var, list):
                for v in var:
                    variables.append(v)
            else:
                variables.append(var)

        dt = [("tile", int)]
        for v in variables:
            dt.append((v, rgrp[tiles[0]][v].dtype))

        data = np.full((nrows,), np.nan, dtype=dt)

        data = np_rename_fields(data, {"x": "x_distance", "y": "y_distance"})

        # data[:] = np.nan

        if "x" in variables:
            variables.remove("x")
        if "y" in variables:
            variables.remove("y")

        if "x_distance" in variables:
            variables.remove("x_distance")
        if "y_distance" in variables:
            variables.remove("y_distance")

        for i, t in enumerate(tiles):
            grp = rgrp[t]
            if "x" in nc_variables:
                x = grp["x"][:]
            elif "x_distance" in nc_variables:
                x = grp["x_distance"][:]
            if "y" in nc_variables:
                y = grp["y"][:]
            elif "y_distance" in nc_variables:
                y = grp["y_distance"][:]
            Y, X = np.meshgrid(y, x)
            data["tile"][i * nXY : (i + 1) * nXY] = int(t)
            data["x_distance"][i * nXY : (i + 1) * nXY] = X.flatten()
            data["y_distance"][i * nXY : (i + 1) * nXY] = Y.flatten()
            for v in variables:
                data[v][i * nXY : (i + 1) * nXY] = grp[v][:].flatten()

    return data


# def nc_max(filename: str, var: Optional[str] = None) -> Dict[Hashable, np.float_]:

#     max_vals: Dict[Hashable, np.float_]

#     da = xr.open_dataset(filename, engine="h5netcdf")

#     tiles = da.tiles

#     da.close()

#     da = xr.open_dataset(filename, engine="h5netcdf", group=str(tiles[0]))
#     if var is None:
#         vars = list(da.variables)
#         vars.remove("x")
#         vars.remove("y")
#         max_vals = dict.fromkeys(vars, np.array([-np.inf]))
#     else:
#         max_vals = dict.fromkeys(var, np.array([-np.inf]))
#     variables = max_vals.keys()
#     tile_max = da.max()
#     for v in variables:
#         max_vals[v] = np.maximum(max_vals[v], tile_max[v].values)
#     da.close()

#     for t in tiles[1:]:
#         da = xr.open_dataset(filename, engine="h5netcdf", group=str(t))
#         tile_max = da.max()
#         for v in variables:
#             max_vals[v] = np.maximum(max_vals[v], tile_max[v].values)

#         da.close()

#     return max_vals


def nc_max(filename, var=None):

    with nc.Dataset(filename, "r") as rgrp:

        tiles = list(rgrp.groups)

        nc_variables = list(rgrp[tiles[0]].variables)

        if var is None:
            variables = nc_variables.copy()
        else:
            if isinstance(var, list):
                variables = [v for v in var if v in nc_variables]
            else:
                if var in nc_variables:
                    variables = [var]
                else:
                    raise ValueError(
                        "variable {} not in netcdf file {}".format(var, filename)
                    )
        max_vals = dict.fromkeys(variables, -np.inf)

        for t in tiles:
            grp = rgrp[t]
            for v in variables:
                max_vals[v] = max(max_vals[v], np.amax(grp[v][:]))

    return max_vals


# def nc_min(filename: str, var: Optional[str] = None) -> Dict[Hashable, np.float_]:

#     min_vals: Dict[Hashable, np.float_]

#     da = xr.open_dataset(filename, engine="h5netcdf")

#     tiles = da.tiles

#     da.close()

#     da = xr.open_dataset(filename, engine="h5netcdf", group=str(tiles[0]))
#     if var is None:
#         vars = list(da.variables)
#         vars.remove("x")
#         vars.remove("y")
#         min_vals = dict.fromkeys(vars, np.array([np.inf]))
#     else:
#         min_vals = dict.fromkeys(var, np.array([np.inf]))
#     variables = min_vals.keys()
#     tile_min = da.min()
#     for v in variables:
#         min_vals[v] = np.minimum(min_vals[v], tile_min[v].values)
#     da.close()

#     for t in tiles[1:]:
#         da = xr.open_dataset(filename, engine="h5netcdf", group=str(t))
#         tile_min = da.min()
#         for v in variables:
#             min_vals[v] = np.minimum(min_vals[v], tile_min[v].values)

#         da.close()

#     return min_vals


def nc_min(filename, var=None):

    with nc.Dataset(filename, "r") as rgrp:

        tiles = list(rgrp.groups)

        nc_variables = list(rgrp[tiles[0]].variables)

        if var is None:
            variables = nc_variables.copy()
        else:
            if isinstance(var, list):
                variables = [v for v in var if v in nc_variables]
            else:
                if var in nc_variables:
                    variables = [var]
                else:
                    raise ValueError(
                        "variable {} not in netcdf file {}".format(var, filename)
                    )
        min_vals = dict.fromkeys(variables, np.inf)

        for t in tiles:
            grp = rgrp[t]
            for v in variables:
                min_vals[v] = min(min_vals[v], np.amin(grp[v][:]))

    return min_vals


# def nc_min_max(
#     filename: str, var: Optional[str] = None
# ) -> Tuple[Dict[Hashable, np.float_], Dict[Hashable, np.float_]]:

#     min_vals: Dict[Hashable, np.float_]
#     max_vals: Dict[Hashable, np.float_]

#     da = xr.open_dataset(filename, engine="h5netcdf")

#     tiles = da.tiles

#     da.close()

#     da = xr.open_dataset(filename, engine="h5netcdf", group=str(tiles[0]))
#     if var is None:
#         vars = list(da.variables)
#         vars.remove("x")
#         vars.remove("y")
#         min_vals = dict.fromkeys(vars, np.array([np.inf]))
#         max_vals = dict.fromkeys(vars, np.array([-np.inf]))
#     else:
#         min_vals = dict.fromkeys(var, np.inf)
#         max_vals = dict.fromkeys(var, -np.inf)
#     variables = max_vals.keys()
#     tile_min = da.min()
#     tile_max = da.max()
#     for v in variables:
#         min_vals[v] = np.minimum(min_vals[v], tile_min[v].values)
#         max_vals[v] = np.maximum(max_vals[v], tile_max[v].values)
#     da.close()

#     for t in tiles[1:]:
#         da = xr.open_dataset(filename, engine="h5netcdf", group=str(t))
#         tile_min = da.min()
#         tile_max = da.max()
#         for v in variables:
#             min_vals[v] = np.minimum(min_vals[v], tile_min[v].values)
#             max_vals[v] = np.maximum(max_vals[v], tile_max[v].values)

#         da.close()

#     return min_vals, max_vals


def nc_min_max(filename, var=None):

    with nc.Dataset(filename, "r") as rgrp:

        tiles = list(rgrp.groups)

        nc_variables = list(rgrp[tiles[0]].variables)

        if var is None:
            variables = nc_variables.copy()
        else:
            if isinstance(var, list):
                variables = [v for v in var if v in nc_variables]
            else:
                if var in nc_variables:
                    variables = [var]
                else:
                    raise ValueError(
                        "variable {} not in netcdf file {}".format(var, filename)
                    )
        min_vals = dict.fromkeys(variables, np.inf)
        max_vals = dict.fromkeys(variables, -np.inf)

        for t in tiles:
            grp = rgrp[t]
            for v in variables:
                min_vals[v] = min(min_vals[v], np.amin(grp[v][:]))
                max_vals[v] = max(max_vals[v], np.amax(grp[v][:]))

    return min_vals, max_vals
