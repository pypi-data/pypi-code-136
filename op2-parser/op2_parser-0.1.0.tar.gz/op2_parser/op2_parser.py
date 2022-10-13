# -*- coding: utf-8 -*-

"""Main module."""
import logging
from collections import namedtuple
from pprint import pprint as pp

import pandas as pd
from numtools.pandas_tk import signed_absmax, subset
from pyNastran.op2.op2 import read_op2
from pyNastran.utils import object_attributes, object_methods

from op2_parser.utils import get_close_matches


class Parser:
    """Simple Wrapper to pyNastra OP2 class
    https://pynastran-git.readthedocs.io/en/latest/quick_start/features.html?highlight=ctria3_force#id1
    """

    def __init__(self, fpath, mode="nx"):
        self.op2 = read_op2(fpath, build_dataframe=False, debug=False, mode=mode)
        self._op2_attributes = object_attributes(self.op2)

    def log_attr_error(self, bad_attribute):
        """when searching an OP2 parameter that does not exists,
        search for closest match in available parameters
        """
        closest_matches = get_close_matches(bad_attribute, self._op2_attributes)
        msg = (
            f"attribute `{bad_attribute}` not found. Do you mean '{closest_matches[0]}'? "
            f"Other founds found are: {closest_matches[1:]}"
        )
        logging.error(msg)

    def available_results(self):
        return self.op2.result_names

    def get(self, attribute, raw=False, **levels):
        """shortcut to self.`get_vector`"""
        return self.get_vector(attribute=attribute, raw=raw, **levels)

    def absmax(self, attribute, raw=False, axis=0, origin=False, **levels):
        df = self.get_vector(attribute=attribute, raw=raw, **levels)
        return signed_absmax(df, axis=axis, origin=origin)

    def get_vector(self, attribute, raw=False, **levels):
        """if `raw` is True, return pyNastran aggregated outputs without columns modifications."""
        lcids = {}
        try:
            attr = getattr(self.op2, attribute)
        except AttributeError:
            self.log_attr_error(attribute)
            return
        for lcid, data in attr.items():
            data.build_dataframe()
            df = data.data_frame
            lcids[lcid] = data.data_frame
        if not lcids:
            return
        df = pd.concat(lcids, names=["SubcaseID"]).reset_index()
        if not raw:
            index = ["SubcaseID", "ElementID", "NodeID"]
            index = [ix for ix in index if ix in df]
            df.set_index(index, inplace=True)
            discard = [c for c in df if c.startswith("level_")]
            if "Type" in df:
                discard.append("Type")
            df = df.drop(columns=discard)
            df.columns.names = [None]
        return subset(df, **levels)

    # =========================================================================
    # syntaxic sugars or shortcuts to common aggregations
    # =========================================================================

    def get_loads(self, **levels):
        df = self.get_vector("loads", **levels)
        # drop rows where everithing is 0
        df = df[df.abs() > 0].dropna(how="all").fillna(0)
        return df

    def get_displacements(self, **levels):
        return self.get_vector("displacements", **levels)

    def get_reactions(self, **levels):
        df = self.get_vector("reactions", **levels)
        # drop rows where everithing is 0
        df = df[df.abs() > 0].dropna(how="all").fillna(0)
        return df

    def get_forces(self, axis, **levels):
        """extract element forces. This is trickier than others since we need to interrogate
        several tables depending on axis request.

        * In global axis request, we will interrogate gridpoint forces
        * In local axis, we will interrogate bar and bush forces
        """
        if axis == "global":
            return self.get_global_forces(**levels)
        else:
            df_bars = self.get_vector("cbar_force")
            df_bars.columns = pd.MultiIndex.from_tuples(
                [c.split("_") for c in df_bars.columns]
            )
            df_bars_A = df_bars["ga"]
            df_bars_B = df_bars["gb"]
            df_bushes_A = self.get_vector("cbush_force")
            df_bushes_B = -df_bushes_A
            raise NotImplementedError(
                f"OP2 recovering of forces in {axis} axis is not implemented"
            )
        pass

    def get_gpf(self, **levels):
        df = self.get_vector("gpf")
        df.etype = df.etype.str.strip()
        df.set_index("etype", append=True, inplace=True)
        return subset(df, **levels).sort_index()

    def get_global_forces(self, **levels):
        """recover grid point forces filtered by elements BAR & BUSH"""
        df = self.get_gpf(etype=["BAR", "BUSH"])
        df.reset_index(level=-1, drop=True, inplace=True)  # drop etype
        return subset(df, **levels) * -1


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)
