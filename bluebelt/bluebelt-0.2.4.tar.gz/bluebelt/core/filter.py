import numpy as np
import copy

import bluebelt

import bluebelt.helpers.check as check


def _filter(cls):
    def weekend(
        self, drop=None, fill_value=np.nan, inplace=None, weekend_days=[5, 6]
    ):
        """
        Fill all non-weekend data with the fill_value. If fill_value=None the
        Series or DataFrame will contain only the weekend days.

        The Series or DataFrame must have a DatetimeIndex

        Parameters
        ----------
        self : Series or DataFrame
        fill_value: object or None, default numpy.nan
        drop: boolean, default None
            if True the filtered values will be dropped
            if drop is None global settings will be applied, default True
        inplace: boolean, default None
            if True the function will be on the object itself
            if False the function will return a new object
            if inplace is None global settings will be applied, default True
        weekend_days: list of int, default [5, 6]

        Returns
        -------
        Series or DataFrame
        """
        # settings
        drop = drop if drop is not None else bluebelt.config("drop")
        inplace = inplace if inplace is not None else bluebelt.config("inplace")
        
        # checks
        check.has_datetimeindex(self._obj)
        series = copy.deepcopy(self._obj) if not inplace else self._obj

        
        if fill_value is not None and not drop:
            series.loc[~series.index.weekday.isin(weekend_days)] = fill_value
        else:
            series = series[series.index.weekday.isin(weekend_days)]

        # only if Workload Class is used directly modify _obj
        # if self.__class__.__name__ == "Workload":
        #     self._obj = series
        
        return series


    setattr(cls, "weekend", weekend)

    return cls