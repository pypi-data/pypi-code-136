from .annot import CellAnnotation
from ..brain_region import brain


class AIBSTENXCellAnnotation(CellAnnotation):
    __slots__ = ()

    def __init__(self, annot_path, metadata, add_l4_from_l3=True):
        super().__init__(annot_path)

        # add AIBS specific attributes
        if 'sample' not in self.data_vars:
            self['sample'] = self.get_index('cell').map(lambda i: i.split('-')[0])

        self['DissectionRegion'] = self['sample'].to_pandas().map(metadata['Structure'])

        metadata['MajorRegion'] = metadata['Structure'].map(
            brain.map_dissection_region_to_major_region())
        self['MajorRegion'] = self['sample'].to_pandas().map(metadata['MajorRegion'])

        metadata['SubRegion'] = metadata['Structure'].map(
            brain.map_dissection_region_to_sub_region())
        self['SubRegion'] = self['sample'].to_pandas().map(metadata['SubRegion'])

        if add_l4_from_l3:
            if 'L4' not in self.data_vars and 'L3' in self.data_vars:
                self['L4'] = self['L3'].copy()
        return


class AIBSSMARTCellAnnotation(CellAnnotation):
    __slots__ = ()

    def __init__(self, annot_path, metadata, add_l4_from_l3=True):
        super().__init__(annot_path)

        self['DissectionRegion'] = metadata['Substructure']

        self['MajorRegion'] = metadata['Substructure'].map(
            brain.map_dissection_region_to_major_region())

        self['SubRegion'] = metadata['Substructure'].map(
            brain.map_dissection_region_to_sub_region())

        if add_l4_from_l3:
            if 'L4' in self.data_vars and 'L3' in self.data_vars:
                self['L4'] = self['L3'].copy()
        return
