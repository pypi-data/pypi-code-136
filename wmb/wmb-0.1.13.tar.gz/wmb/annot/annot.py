import pandas as pd
import xarray as xr


class CellAnnotation(xr.Dataset):
    __slots__ = ()

    def __init__(self, annot_path):
        annot = xr.open_zarr(annot_path)
        super().__init__(data_vars=annot.data_vars, coords=annot.coords, attrs=annot.attrs)
        self.attrs['annot_path'] = annot_path

        # determine cluster hierarchy list
        cluster_data_var = []
        for var_name in self.attrs['cluster_hierarchy']:
            cluster_data_var += var_name
        self.attrs['cluster_data_var'] = cluster_data_var

        # fill cluster cat if the annotation exists
        for var_name in cluster_data_var:
            if f'{var_name}_cat' in self.attrs:
                self[var_name] = self[var_name].to_pandas().map(
                    {i: c for i, c in enumerate(self.attrs[f'{var_name}_cat'])})
        self._concat_hierarchy_label()

        # add cell annot if the cat annot exists
        for var_name in self.data_vars.keys():
            if var_name.endswith('_cat_annot'):
                cluster_name = var_name.split('_cat_annot')[0]
                self._map_cluster_cat(cluster_name)

        self.attrs['__cache__'] = {}
        return

    def _concat_hierarchy_label(self):
        """Concatenate hierarchy labels to make lower level labels unique"""
        for hierarchy_list in self.attrs['cluster_hierarchy']:
            for i, var_name in enumerate(hierarchy_list):
                if i > 0:
                    self[var_name] = self[hierarchy_list[i - 1]].to_pandas().astype(str) + \
                                     '_' + self[var_name].to_pandas().astype(str)
        return

    def get_cell_annot(self, cluster_name):
        cell_annot_name = f'{cluster_name}_annot'
        try:
            return self[cell_annot_name]
        except KeyError:
            # if cell annot does not exist, try to map cluster cat annot to cell annot
            self._map_cluster_cat(cluster_name)
            return self[cell_annot_name]

    def _map_cluster_cat(self, cluster_name):
        self[f'{cluster_name}_annot'] = self[cluster_name].to_pandas().map(
            self[f'{cluster_name}_cat_annot'].to_pandas())

    def save_annot(self, cat_map, cluster_name, missing_name='unknown'):
        """Save annotation to zarr file"""
        # delete cache
        if "__cache__" in self.attrs:
            del self.attrs['__cache__']

        annot = pd.Series(cat_map)
        cat_name = f'{cluster_name}_cat'
        annot.index.name = cat_name
        if cat_name not in self.dims:
            # if annot is not full, add missing categories
            all_cats = self[cluster_name].to_pandas().unique()
            for cat in all_cats:
                if cat not in annot.index:
                    annot[cat] = missing_name
            # all categories are in index
            self.coords[cat_name] = annot.index

        # save annotation in data_vars
        self[f'{cluster_name}_cat_annot'] = annot

        # save annotation in zarr
        self[[f'{cluster_name}_cat_annot']].to_zarr(self.attrs['annot_path'], mode='a')

        # add cell level annotation, but not save to zarr
        self._map_cluster_cat(cluster_name)
        return

    def get_cluster_centroids_df(self, coords, groupby):
        if isinstance(coords, str):
            coords = [coords]
        records = []
        for coord in coords:
            cell_coords = self[f'{coord}_coord'].to_pandas()
            cluster_df = cell_coords.groupby(self[groupby].to_pandas()).median()
            records.append(cluster_df)
        all_coords = pd.concat(records, axis=1)
        all_coords['cell_counts'] = self[groupby].to_pandas().value_counts()
        return all_coords

    def add_palette(self, palette, da_name, missing_color='#D3D3D3'):
        if da_name not in self:
            print(f'{da_name} does not exist in data_vars or coords, palette not added.')
            return

        if 'palettes' not in self.attrs:
            self.attrs['palettes'] = {}
        # fill missing cat with missing_color
        unique_cats = self[da_name].to_pandas().unique()
        self.attrs['palettes'][da_name] = {cat: palette[cat] if cat in palette else missing_color
                                           for cat in unique_cats}
        return

    def get_palette(self, da_name):
        try:
            return self.attrs['palettes'][da_name]
        except KeyError:
            return None
