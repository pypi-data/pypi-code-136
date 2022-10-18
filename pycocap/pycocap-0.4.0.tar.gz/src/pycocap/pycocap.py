# -*- coding: utf-8 -*-

import warnings
from functools import reduce
from datetime import date
import requests
import numpy as np
import pandas as pd


API_URL = 'https://webapp.ufz.de/cocap/'


def cut_at_dates(
    df: pd.DataFrame,
    start_date: date = None,
    end_date: date = None,
) -> pd.DataFrame:
    """Cut a DataFrame at given dates."""
    if (start_date is not None or end_date is not None) and start_date == end_date:
        raise ValueError('start_date and end_date cannot be equal')
    mask = None
    if start_date is not None:
        start_date = pd.to_datetime(start_date)
        mask = df['date'] >= start_date
    if end_date is not None:
        end_date = pd.to_datetime(end_date)
        if start_date is not None:
            mask &= df['date'] < end_date
        else:
            mask = df['date'] < end_date
    if mask is not None:
        df = df[mask]
    return df

def regularize_timeseries(
    df: pd.DataFrame,
    fill_value: float = None,
    start_date: date = None,
    end_date: date = None,
) -> pd.DataFrame:
    """Fill missing data with NaNs, or fill_value to get a regular timeseries"""
    # TODO can all this be done cleaner?!
    sd = start_date if start_date is not None else df['date'].iloc[0]
    ed = end_date if end_date is not None else df['date'].iloc[-1]
    idx = pd.date_range(sd, ed, freq='D', inclusive='left')
    df = df.set_index('date')
    df = df.reindex(idx)
    df['date'] = df.index
    df = df.reset_index(drop=True)
    # put 'date' at position 0 again
    cols = df.columns.tolist()
    cols.insert(0, cols.pop())
    df = df[cols]
    if fill_value is not None:
        if fill_value == 'interpolate':
            # interpolate does not like dates...
            df.loc[:, df.columns!='date'] = (
                df.loc[:, df.columns!='date'].interpolate()
            )
        else:
            df = df.fillna(fill_value)
    return df

def _convert_json_to_df(
    json,
    rename_cols: dict = None,
    start_date: date = None,
    end_date: date = None,
) -> pd.DataFrame:
    df = pd.DataFrame(json)
    if rename_cols is not None:
        df = df.rename(columns=rename_cols)
    df['date'] = pd.to_datetime(df['date'])
    df = cut_at_dates(df, start_date, end_date)
    return df


def reports(
    country: str,
    report_type: str,
    start_date: date = None,
    end_date: date = None,
    params: dict = None,
    fill_value=np.nan,
    return_population: bool = False,
):
    """Get cases or deaths timeseries as a DataFrame from the db.

    Parameters
    ----------
    country
        The country name for which to get the reports

    report_type
        Can either be "cases" or "death"

    start_date : optional
        The date at which the timeseries will start

    end_date : optional
        The date at which the timeseries will end

    fill_value : optional
        decide what to do with missing values, can be

            - np.nan: fill with NaNs, to optain regular timeseries
            - a number: fill with constant value, e.g. 0
            - 'drop': drop missing values
            - 'interpolate' : linear interpolation over gaps

    return_population : bool, optional
        Convenience flag: return tuple of (DataFrame, N)

    Returns
    -------
    df
        A DataFrame consisting of the columns "date" and `report_type`
    N, optional
        The population of `country`
    """
    response = requests.get(API_URL + f'{country}/{report_type}', params=params)
    if response.status_code == 200:
        r_json = response.json()
        if len(r_json['report']) == 0:
            warnings.warn('Empty response')
            return None
        N = int(r_json['population'])
        df = _convert_json_to_df(
            r_json['report'],
            {'count': report_type},
            start_date,
            end_date,
        )
        if fill_value != 'drop':
            df = regularize_timeseries(
                df,
                fill_value,
                start_date,
                end_date,
            )
    else:
        print(f'Response code: {response.status_code}')
        df = None
        N = None
    r = df
    if return_population:
        r = (df, N)
    return r

def cases(
    country: str,
    start_date: date = None,
    end_date: date = None,
    params: dict = None,
    fill_value=np.nan,
    return_population: bool = False,
):
    """Get cases timeseries as a DataFrame from the db.

    Parameters
    ----------
    country
        The country name for which to get the reports

    start_date : optional
        The date at which the timeseries will start

    end_date : optional
        The date at which the timeseries will end

    fill_value : optional
        decide what to do with missing values, can be

            - np.nan: fill with NaNs, to optain regular timeseries
            - a number: fill with constant value, e.g. 0
            - 'drop': drop missing values
            - 'interpolate' : linear interpolation over gaps

    return_population : bool, optional
        Convenience flag: return tuple of (DataFrame, N)

    Returns
    -------
    df
        A DataFrame consisting of the columns "date" and "cases"
    N, optional
        The population of `country`
    """
    return reports(
        country,
        'cases',
        start_date,
        end_date,
        params,
        fill_value,
        return_population,
    )

def deaths(
    country: str,
    start_date: date = None,
    end_date: date = None,
    params: dict = None,
    fill_value=np.nan,
    return_population: bool = False,
):
    """Get death timeseries as a DataFrame from the db.

    Parameters
    ----------
    country
        The country name for which to get the reports

    start_date : optional
        The date at which the timeseries will start

    end_date : optional
        The date at which the timeseries will end

    params : optional
        optional query parameters

            - "source_name"

    fill_value : optional
        decide what to do with missing values, can be

            - np.nan: fill with NaNs, to optain regular timeseries
            - a number: fill with constant value, e.g. 0
            - 'drop': drop missing values
            - 'interpolate' : linear interpolation over gaps

    return_population : bool, optional
        Convenience flag: return tuple of (DataFrame, N)

    Returns
    -------
    df
        A DataFrame consisting of the columns "date" and "death"
    N, optional
        The population of `country`
    """
    return reports(
        country,
        'death',
        start_date,
        end_date,
        params,
        fill_value,
        return_population,
    )

def npi(
    country: str,
    npi_type: str,
    start_date: date = None,
    end_date: date = None,
    params: dict = None,
    fill_value=np.nan,
) -> pd.DataFrame:
    """Get NPI timeseries as a DataFrame from the db.

    Parameters
    ----------
    country
        The country name for which to get the reports

    npi_type
        choose the npi type from

            - "stringency"
            - "school closing"
            - "workplace closing"
            - "cancel public events"
            - "restrictions on gatherings"
            - "close public transport"
            - "stay at home requirements"
            - "restrictions on internal movement"
            - "international travel controls"
            - "income support"
            - "debt relief"
            - "public information campaigns"
            - "testing policy"
            - "contact tracing"
            - "facial coverings"
            - "vaccination policy"
            - "protection of elderly people"

    start_date : optional
        The date at which the timeseries will start

    end_date : optional
        The date at which the timeseries will end

    params : optional
        optional query parameters

            - "source_name"
    fill_value : optional
        decide what to do with missing values, can be

            - np.nan: fill with NaNs, to optain regular timeseries
            - a number: fill with constant value, e.g. 0
            - 'drop': drop missing values
            - 'interpolate' : linear interpolation over gaps

    Returns
    -------
    df
        A DataFrame consisting of the columns "date" and `npi_type`
    """
    response = requests.get(API_URL + f'{country}/npi/{npi_type}', params=params)
    if response.status_code == 200:
        r_json = response.json()
        if len(r_json['policies']) == 0:
            warnings.warn('Empty response')
            return None
        df = _convert_json_to_df(
            r_json['policies'],
            {'value': npi_type, 'flag': npi_type+'_flag'},
            start_date,
            end_date,
        )
        if fill_value != 'drop':
            df = regularize_timeseries(
                df,
                fill_value,
                start_date,
                end_date,
            )
    else:
        print(f'Response code: {response.status_code}')
        df = None
    return df

def npis(
    country: str,
    npi_types: list | str,
    start_date: date = None,
    end_date: date = None,
    params: dict = None,
    fill_value=np.nan,
) -> pd.DataFrame:
    """Get multiple NPI timeseries as a DataFrame from the db.

    Parameters
    ----------
    country
        The country name for which to get the reports

    npi_types
        can either be "all" to get all NPIs or a list of following

            - "stringency"
            - "school closing"
            - "workplace closing"
            - "cancel public events"
            - "restrictions on gatherings"
            - "close public transport"
            - "stay at home requirements"
            - "restrictions on internal movement"
            - "international travel controls"
            - "income support"
            - "debt relief"
            - "public information campaigns"
            - "testing policy"
            - "contact tracing"
            - "facial coverings"
            - "vaccination policy"
            - "protection of elderly people"

    start_date : optional
        The date at which the timeseries will start

    end_date : optional
        The date at which the timeseries will end

    params : optional
        optional query parameters

            - "source_name"

    fill_value : optional
        decide what to do with missing values, can be

            - np.nan: fill with NaNs, to optain regular timeseries
            - a number: fill with constant value, e.g. 0
            - 'drop': drop missing values
            - 'interpolate' : linear interpolation over gaps

    Returns
    -------
    df
        A DataFrame consisting of the columns "date" and `npi_type`
    """
    _npi_types = npi_types
    if npi_types == 'all':
        _npi_types = [
            'stringency',
            'school closing',
            'workplace closing',
            'cancel public events',
            'restrictions on gatherings',
            'close public transport',
            'stay at home requirements',
            'restrictions on internal movement',
            'international travel controls',
            'income support',
            'debt relief',
            'public information campaigns',
            'testing policy',
            'contact tracing',
            'facial coverings',
            'vaccination policy',
            'protection of elderly people',
        ]

    dfs = [
        npi(
            country,
            npi_type,
            start_date,
            end_date,
            params,
            fill_value,
        ) for npi_type in _npi_types
    ]
    dfs = reduce(lambda df1, df2: pd.merge(df1, df2, on='date'), dfs)
    return dfs
