from .annot import CellAnnotation

from ..brain_region import brain


class BROADTENXCellAnnotation(CellAnnotation):
    __slots__ = ()

    def __init__(self, annot_path, metadata, add_l4_from_l3=True):
        super().__init__(annot_path)

        # add BROAD specific attributes
        self['sample'] = self.get_index('cell').map(lambda i: i[:-18])

        self['DissectionRegion'] = self['sample'].to_pandas().map(metadata['DissectionRegion'])

        metadata['MajorRegion'] = metadata['DissectionRegion'].map(
            brain.map_dissection_region_to_major_region())
        self['MajorRegion'] = self['sample'].to_pandas().map(metadata['MajorRegion'])

        metadata['SubRegion'] = metadata['DissectionRegion'].map(
            brain.map_dissection_region_to_sub_region())
        self['SubRegion'] = self['sample'].to_pandas().map(metadata['SubRegion'])

        if add_l4_from_l3:
            if 'L4' in self.data_vars and 'L3' in self.data_vars:
                self['L4'] = self['L3'].copy()
        return

