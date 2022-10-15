import xarray as xr
import pandas as pd
from collections import OrderedDict


def _concat_non_nan_groups(ll):
    nl = []
    for g in ll:
        if g != 'nan':
            nl.append(g)
        else:
            break
    return '_'.join(nl)


class IntegrationResultZarr(xr.Dataset):
    __slots__ = ()

    def __init__(self, zarr_path):
        annot = xr.open_zarr(zarr_path)
        super().__init__(data_vars=annot.data_vars,
                         coords=annot.coords,
                         attrs=annot.attrs)
        self.attrs['zarr_path'] = zarr_path

        # aggregate integration groups
        self._get_final_inte_group('ref')
        self._get_final_inte_group('query')
        return

    def _get_final_inte_group(self, dataset):
        if dataset == 'ref':
            dataset = self.ref_name
        elif dataset == 'query':
            dataset = self.query_name
        else:
            pass

        groups = OrderedDict()
        for i, level in enumerate(self.levels):
            cur_group = self._get_categorical_vector(dataset, level,
                                                     'InteGroup')
            cur_group = cur_group.replace('-1', 'nan')
            groups[i] = cur_group
        final_group = pd.DataFrame(groups).apply(_concat_non_nan_groups,
                                                 axis=1)

        # print stats
        print(f'For the {dataset} cells:')
        cells = (final_group == '').sum()
        print(f'{cells: 8d} cells do not belong to any integration group.')
        level_counts = final_group[final_group != ''].str.count('_').value_counts().sort_index()
        for level, cells in level_counts.items():
            print(
                f'{cells: 8d} cells belong to {self.levels[level]} integration group.'
            )

        key = f'{dataset}_Final_InteGroup'
        if key not in self.data_vars:
            self[key] = final_group
        return final_group

    def _get_categorical_vector(self, dataset, level, data_type):
        if isinstance(level, int):
            level = self.levels[level]

        key = f'{dataset}_{level}_{data_type}'
        self[key].load()
        value = self[key].to_pandas()
        return value

    @property
    def query_name(self):
        return self.attrs['query_name']

    @property
    def ref_name(self):
        return self.attrs['ref_name']

    @property
    def levels(self):
        return self.attrs['integration_levels']

    @property
    def ref_group(self):
        return self[f'{self.ref_name}_Final_InteGroup'].to_pandas()

    @property
    def query_group(self):
        return self[f'{self.query_name}_Final_InteGroup'].to_pandas()

    @property
    def ref_cluster(self):
        return self[f'{self.ref_name}_Cluster'].to_pandas()

    @property
    def query_cluster(self):
        return self[f'{self.query_name}_Cluster'].to_pandas()

    def get_ref_co_cluster(self, level):
        dataset = self.ref_name
        return self._get_categorical_vector(dataset, level, 'CoCluster')

    def get_query_co_cluster(self, level):
        dataset = self.query_name
        return self._get_categorical_vector(dataset, level, 'CoCluster')

    def get_ref_inte_group(self, level):
        dataset = self.ref_name
        return self._get_categorical_vector(dataset, level, 'InteGroup')

    def get_query_inte_group(self, level):
        dataset = self.query_name
        return self._get_categorical_vector(dataset, level, 'InteGroup')

    def inte_group_overlap_score(self, group):
        """Calculate the overlap score of a group."""
        from ALLCools.integration.confusion import calculate_overlap_score

        ref_group = self.ref_group
        query_group = self.query_group

        ref_cells = ref_group[ref_group.str.startswith(group)].index
        query_cells = query_group[query_group.str.startswith(group)].index

        level = self.levels[group.count('_')]
        ref_df = pd.DataFrame({'Cluster': self.ref_cluster[ref_cells]})
        ref_df['CoCluster'] = self.get_ref_co_cluster(level)

        query_df = pd.DataFrame({'Cluster': self.query_cluster[query_cells]})
        query_df['CoCluster'] = self.get_query_co_cluster(level)

        score_df = calculate_overlap_score(ref_df, query_df)
        score_df.index.name = self.ref_name + '_Cluster'
        score_df.columns.name = self.query_name + '_Cluster'
        return score_df

    def get_group_data(self, group, coord='tsne'):
        if group == 'nan' or group == '-1' or group == '':
            return None, None

        group_level = len(group.split('_'))
        level = self.levels[group_level]

        ref_cells = self.ref_group[self.ref_group.str.startswith(group)].index
        query_cells = self.query_group[self.query_group.str.startswith(group)].index

        ref_df = self[f'{self.ref_name}_{level}_{coord}_coord'].sel(
            {f'{self.ref_name}_cell': ref_cells}).to_pandas()
        ref_df['CoCluster'] = self.get_ref_co_cluster(level)
        ref_df['Cluster'] = self.ref_cluster[ref_cells]

        query_df = self[f'{self.query_name}_{level}_{coord}_coord'].sel(
            {f'{self.query_name}_cell': query_cells}).to_pandas()
        query_df['CoCluster'] = self.get_query_co_cluster(level)
        query_df['Cluster'] = self.query_cluster[query_cells]
        return ref_df, query_df
