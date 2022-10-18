from typing import Optional

import pandas as pd
from seeq import spy
from seeq.spy import _common
from seeq.spy._errors import *


class ItemMap:
    """
    Represents a map of item identifiers from a source (usually a saved set of workbooks) to the destination on the
    Seeq Server. This class is used extensively by spy.workbooks.push() operations.
    """

    _lookup_df: pd.DataFrame

    def __init__(self, item_map=None, lookup_df=None):
        self._item_map = item_map if item_map is not None else dict()

        if lookup_df is None:
            self._lookup_df = pd.DataFrame()
        else:
            self._lookup_df = lookup_df

    def __contains__(self, key):
        key = _common.ensure_upper_case_id('ID', key)
        return self._item_map.__contains__(key)

    def __getitem__(self, key):
        key = _common.ensure_upper_case_id('ID', key)
        return self._item_map.__getitem__(key)

    def __setitem__(self, key, val):
        key = _common.ensure_upper_case_id('ID', key)
        val = _common.ensure_upper_case_id('ID', val)
        self._item_map.__setitem__(key, val)

    def __delitem__(self, key):
        key = _common.ensure_upper_case_id('ID', key)
        self._item_map.__delitem__(key)

    def keys(self):
        return self._item_map.keys()

    def look_up_id(self, value):
        row = _common.look_up_in_df(value, self._lookup_df)
        return row['ID'] if row is not None else None


class OverrideItemMap(ItemMap):
    """
    Takes an existing ItemMap and overrides various keys. This is used extensively in the templating system to
    temporarily (for the extent of a particular frame in a callstack) override the inner ItemMap using
    template_parameters or an override_map.
    """

    _override: dict
    _parameters: Optional[dict]

    def __init__(self, item_map: ItemMap, *, template_parameters: dict = None, override_map: dict = None):
        super().__init__(item_map)

        self._override = dict() if override_map is None else override_map
        self._parameters = None
        if template_parameters:
            self._parameters = template_parameters
            self._override_from_template_parameters(template_parameters)

    def __contains__(self, key):
        key = _common.ensure_upper_case_id('ID', key)
        return self._override.__contains__(key) or self._item_map.__contains__(key)

    def __getitem__(self, key):
        key = _common.ensure_upper_case_id('ID', key)
        if self._override.__contains__(key):
            return self._override.__getitem__(key)
        else:
            return super().__getitem__(key)

    def __delitem__(self, key):
        key = _common.ensure_upper_case_id('ID', key)
        if self._override.__contains__(key):
            self._override.__delitem__(key)
        else:
            self._item_map.__delitem__(key)

    def look_up_id(self, value):
        return self._item_map.look_up_id(value)

    def keys(self):
        keys = set(self._item_map.keys())
        keys.update(self._override.keys())
        return keys

    def override(self, key, value):
        self._override[key] = value

    @property
    def parameters(self):
        if self._parameters is not None:
            return self._parameters

        if isinstance(self._item_map, OverrideItemMap):
            return self._item_map.parameters

        return None

    def _override_from_template_parameters(self, template_parameters: dict):

        for key, value in template_parameters.items():
            if value is None:
                continue

            _id, _type, _fqn = spy.workbooks.ItemTemplate.code_key_tuple(key)

            if _id is None:
                # This is the case of a Mustachioed annotation with {{variable}} tokens in it
                continue

            if isinstance(value, pd.DataFrame):
                if len(value) > 1:
                    raise SPyValueError(f'Multiple rows in template_parameters dict for "{key}":\n{value}')
                value = value.iloc[0].to_dict()
            elif isinstance(value, str):
                value = {'Name': value}
            elif isinstance(value, spy.workbooks.ItemTemplate):
                continue

            if _common.present(value, 'ID') and not _common.get(value, 'Reference', default=False):
                self._override[_id] = _common.get(value, 'ID')
            else:
                self._override[_id] = self.look_up_id(value)
