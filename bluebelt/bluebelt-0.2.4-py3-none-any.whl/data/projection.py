import numpy as np
import pandas as pd

import bluebelt.helpers.date

import datetime

def project(_obj, year=None, adjust_holidays=True):
    """
        Project an object with DatetimeIndex to another year. If the object
        contains more than one iso year the data will be projected from the
        provided year up.
        Data is projected by iso week and weekday; e.g. the data at Monday
        of isoweek 1 in the original year data is projected to Monday of
        iso week 1 in the projection year.
    
        Parameters
        ----------
        year: int, default None
            the year to project to
        adjust_holidays: boolean, default True
            adjust the values for holidays; take the values for each holiday
            and swap them with the new holiday dates

        Returns
        -------
        The projected pandas object

    """
    _obj = _obj.copy()

    # create result object
    if isinstance(_obj, pd.Series):
        result = pd.Series(dtype=_obj.dtype)
    else:
        result = pd.DataFrame(dtype=_obj.dtype)

    # check if _obj has only one iso year
    for this_year in _obj.index.isocalendar().year.unique():

        year_obj = _obj[_obj.index.isocalendar().year == this_year]

        _year = year + this_year - _obj.index.isocalendar().year.min()

        # check for week 53
        if (
            year_obj.index.isocalendar().week.max()
            > bluebelt.helpers.date.last_iso_week_in_year(_year)
        ):
            # drop week 53
            year_obj = year_obj[year_obj.index.isocalendar().week < 53]
        elif (
            year_obj.index.isocalendar().week.max()
            < bluebelt.helpers.date.last_iso_week_in_year(_year)
        ):
            # TO DO OPTIONAL create week 53
            pass

        # create a isoformat MultiIndex
        index = pd.MultiIndex.from_frame(year_obj.index.isocalendar())
        # set the year to the requested year
        index = index.set_levels([_year], level=0)
        # build a new DatetimeIndex from the isoformat MultiIndex
        index = pd.DatetimeIndex(
            np.apply_along_axis(
                lambda x: datetime.datetime.fromisocalendar(x[0], x[1], x[2]),
                1,
                np.array([*index.values]),
            )
        )
        # create the new year_obj
        if isinstance(year_obj, pd.Series):
            result = pd.concat([result, pd.Series(index=index, data=year_obj.values, name=year_obj.name)])
        else:
            result = pd.concat([result, pd.DataFrame(index=index, data=year_obj.values, columns=year_obj.columns)])

        if adjust_holidays:

            # get original holidays
            _obj_holidays = bluebelt.helpers.holidays.get_holidays_dict(
                year_obj.index.year.unique()
            )
            # find the new dates for the original holidays
            _obj_holidays = {
                datetime.datetime.fromisocalendar(
                    _year, key.isocalendar()[1], key.isocalendar()[2]
                ): value
                for key, value in _obj_holidays.items()
                if key in year_obj.index
            }

            # get new holidays
            result_holidays = bluebelt.helpers.holidays.get_holidays_dict(
                result.index.year.unique()
            )
            result_holidays = {
                value: key for key, value in result_holidays.items() if key in result.index
            }

            # create a swap dictionairy
            holidays = {
                key: result_holidays.get(value) for key, value in _obj_holidays.items()
            }

            for key, value in holidays.items():

                # catch none existing holidays like liberation day in some years
                if key and value:
                    result.loc[[key, value]] = result.loc[[value, key]].values

    return result
