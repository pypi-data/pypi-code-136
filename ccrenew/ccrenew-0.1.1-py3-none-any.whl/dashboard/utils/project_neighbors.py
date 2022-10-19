import logging
from numbers import Number
import numpy as np
from pandas import DataFrame, Series

from CCR import all_df_keys as df_keys

logger = logging.getLogger(__name__)


def find_nearby_projects(project_name, dist=10, print_data=True, include_retired=False, df=None):
    """Creates a list of sites within a certain distance of the reference site.

    Args:
        project_name (str): Reference site.
        dist (int, optional): Number of miles to search around the reference site.
            Defaults to 10.
        include_retired (bool, optional): Whether to return sites that have been retired.
            Defaults to False, i.e. does not return retired sites.
        df (Dataframe, optional): Dataframe containing sitenames & lat/longs.
            Defaults to `df_keys` if no `df` supplied.

    Returns:
        DataFrame: Contains information about all sites within the specified\
        distance from the reference site.
    """
    # Set `df` to `df_keys` if not supplied
    if not isinstance(df, DataFrame):
        df = df_keys

        # Exclude retired projects if desired
        if not include_retired:
            df = df.query("Retired != True")

    # Rename 'Tilt/GCR' column to a valid python identifier
    df.rename(columns={'Tilt/GCR':'Tilt_GCR'}, inplace=True)
    
    # Get a dictionary of site information, then the required parameters for the query
    site_info = df.loc[[project_name]].to_dict('index')[project_name]
    lat = site_info['GPS_Lat']
    lon = site_info['GPS_Long']
    df.loc[:, 'dist'] = haversine(lon, lat, df['GPS_Long'], df['GPS_Lat'])
    nearby_sites = df.query("dist <= @dist") \
                     .reindex(columns=['Racking', 'OEM_Racking', 'Tilt_GCR', 'Max_angle', 'dist']) \
                     .sort_values('dist')

    if print_data:
        print('\n')
        print('Sites within {} miles of {}'.format(dist, project_name))
        print(nearby_sites)
        print('\n')
    return nearby_sites

def find_similar_projects(project_name, include_retired=False, df=None):
    """Creates a list of sites that share similar racking properties to the reference project.

    Args:
        project_name (str): Reference project.
        include_retired (bool, optional): Whether to return sites that have been retired.
            Defaults to False, i.e. does not return retired sites.
        df (Dataframe, optional): Dataframe containing sitenames & lat/longs.
            Defaults to `df_keys` if no `df` supplied.
    Returns:
        DataFrame: Contains information about all sites with similar racking\
        properties to the reference site.
    """
    # Set `df` to `df_keys` if not supplied
    if not isinstance(df, DataFrame):
        df = df_keys

        # Exclude retired projects if desired
        if not include_retired:
            df = df.query("Retired != True")

    # Rename 'Tilt/GCR' column to a valid python identifier
    df.rename(columns={'Tilt/GCR':'Tilt_GCR'}, inplace=True)
    
    # Get a dictionary of site information, then the required parameters for the query
    site_info = df.loc[[project_name]].to_dict('index')[project_name]
    racking = site_info['Racking']
    oem_racking = site_info['OEM_Racking']
    tilt = site_info['Tilt_GCR']
    max_angle = site_info['Max_angle']
    
    if racking == 'Fixed':
        query = """Racking == @racking \
                 & OEM_Racking == @oem_racking \
                 & Tilt_GCR == @tilt
                """

    elif racking == 'Tracker':
        # Correct for cases when GCR is entered as a percentage rather than a fraction
        if tilt > 1:
            tilt /= 100.0
        query = """Racking == @racking \
                 & OEM_Racking == @oem_racking \
                 & Tilt_GCR >= @tilt - 0.05 \
                 & Tilt_GCR <= @tilt + 0.05 \
                 & Max_angle == @max_angle
                """
    
    else:
        raise ValueError("""Racking type not found. Double check df_keys to
                         ensure racking is either 'Fixed' or 'Tracker'""")

    # Get all sites that have matching info to the reference site
    similar_sites = df.query(query)

    return similar_sites

def find_nearby_similar_projects(project_name, dist=10, print_data=True, include_retired=False, df=None):
    """Creates a list of sites within a certain distance of the reference site
    that share similar racking properties. 

    Args:
        project_name (str): Reference site.
        dist (int, optional): Number of miles to search around the reference site.
            Defaults to 10.
        include_retired (bool, optional): Whether to return sites that have been retired.
            Defaults to False, i.e. does not return retired sites.
        df (Dataframe, optional): Dataframe containing sitenames & lat/longs.
            Defaults to `df_keys` if no `df` supplied.
    Returns:
        DataFrame: Contains information about all sites within a certain distance\
        of the reference site that share similar racking properties.
    """
    nearby_sites = find_nearby_projects(project_name, dist, include_retired, df)
    nearby_similar_sites = find_similar_projects(project_name, df=nearby_sites)
    
    if print_data:
        print('\n')
        print('Similar sites within {} miles of {}'.format(dist, project_name))
        print(nearby_similar_sites)
        print('\n')
    return nearby_similar_sites

def haversine(lon1, lat1, lon2, lat2):
    """Calculate the great circle distance between two points
    on the earth (specified in decimal degrees).

    Args:
        lon1 (Number, np.ndarray, or Series): Longitude of point 1.
        lon1 (Number, np.ndarray, or Series): Latitude of point 1.
        lon1 (Number, np.ndarray, or Series): Longitude of point 2.
        lon1 (Number, np.ndarray, or Series): Latitude of point 2.

    Returns:
        np.number, np.ndarray, or Series: Distance between points in miles.
    """
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = np.sin(dlat/2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2.0)**2

    c = 2 * np.arcsin(np.sqrt(a))
    dist_miles = 3798 * c
    return dist_miles