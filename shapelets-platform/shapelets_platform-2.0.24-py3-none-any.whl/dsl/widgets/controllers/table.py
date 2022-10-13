# Copyright (c) 2021 Grumpy Cat Software S.L.
#
# This Source Code is licensed under the MIT 2.0 license.
# the terms can be found in LICENSE.md at the root of
# this project, or at http://mozilla.org/MPL/2.0/.
from __future__ import annotations

from typing import Union, Optional, Tuple
from dataclasses import dataclass

from shapelets.dsl.widgets import AttributeNames, Widget, StateControl
import pandas as pd
import numpy as np


@dataclass
class Table(StateControl):
    data: Optional[pd.DataFrame] = None
    cols: Optional[Union[np.ndarray, list]] = None
    rows_per_page: Optional[int] = None
    
    @staticmethod
    def from_dataframe(self, data: pd.DataFrame) -> Table:
        self.data = data
        return self

    def to_dataframe(self) -> pd.DataFrame:
        dataframe = self.data
        return dataframe

    @staticmethod
    def from_list(self, lista: list) -> Table:
        self.data = lista
        return self

    def to_list(self) -> list:
        lista = self.data.values.tolist() if self.data is not None else []
        return lista


class TableWidget(Table, Widget):

    def __init__(self, data: Optional[pd.DataFrame] = None, rows: Optional[Union[np.ndarray, list]] = None,
                 cols: Optional[Union[np.ndarray, list]] = None,
                 rows_per_page: Optional[int] = None,
                 **additional):
        Widget.__init__(self, Table.__name__, **additional)
        Table.__init__(self, data, cols, rows_per_page)
        self._parent_class = Table.__name__
        self._compatibility: Tuple = (pd.DataFrame.__name__, np.ndarray.__name__, list.__name__, Table.__name__)

    def to_dict_widget(self):
        table_dict = Widget.to_dict_widget(self)

        if (self.data is not None):
            if isinstance(self.data, pd.DataFrame):
                
                table_dict[AttributeNames.PROPERTIES.value].update({
                    AttributeNames.COLS.value: list(self.data.columns)
                })
                df_json = self.data.to_json(orient = 'records')
                table_dict[AttributeNames.PROPERTIES.value].update({
                    AttributeNames.DATA.value: df_json,
                })

        if (self.rows_per_page is not None):
            if isinstance(self.rows_per_page, int):
                table_dict[AttributeNames.PROPERTIES.value].update({
                    AttributeNames.ROWS_PER_PAGE.value: self.rows_per_page
                })

        return table_dict
