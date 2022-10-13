import pandas as pd
import os
import datetime
from DataAcquisition import DataAcquisition
import requests
import logging


class DataFromTomorrow(DataAcquisition):

  def __init__(self, url):
    """
    This class gets weather data from Tomorrow.io API.

    Args:
      url: url of the tomorrow.io API
    """
    self.url = url


  # Get weather data (from wind)
  def get_weather_data_from_file(self, filename="weather.csv", **kwargs):
    r"""
    Imports weather data from a file.

    The data include wind speed at two different heights in m/s, air
    temperature in two different heights in K, surface roughness length in m
    and air pressure in Pa. The height in m for which the data applies is
    specified in the second row.
    In case no weather data file exists, an example weather data file is
    automatically downloaded and stored in the same directory as this example.

    Args:
      filename : Filename of the weather data file. Default: 'weather.csv'.
      datapath : Path where the weather data file is stored. Default is the same directory this example is stored in.

    Returns:
      DataFrame with time series for wind speed `wind_speed` in m/s,
      temperature `temperature` in K, roughness length `roughness_length`
      in m, and pressure `pressure` in Pa.
      The columns of the DataFrame are a MultiIndex where the first level
      contains the variable name as string (e.g. 'wind_speed') and the
      second level contains the height as integer at which it applies
      (e.g. 10, if it was measured at a height of 10 m). The index is a
      DateTimeIndex.

    """

    if 'datapath' not in kwargs:
      kwargs['datapath'] = os.path.dirname(__file__)

    file = os.path.join(kwargs['datapath'], filename)

    # download example weather data file in case it does not yet exist
    if not os.path.isfile(file):
      logging.debug("Download weather data for example.")
      req = requests.get("https://osf.io/59bqn/download")
      with open(file, "wb") as fout:
        fout.write(req.content)

    # read csv file
    weather_df = pd.read_csv(
      file,
      index_col=0,
      header=[0, 1],
      date_parser=lambda idx: pd.to_datetime(idx))

    # change time zone
    #weather_df.index = weather_df.index.tz_convert('Europe/Berlin')

    return weather_df





  def get_weather_data(self):
    """
    Gets weather data from Tomorrow.io API

    Returns:
      dataframe with wind data
    """

    wind_data_from_file = self.get_weather_data_from_file(filename='../weather.csv', datapath='')


    # Using Tomorrow.io API to get wind data
    wind_data = requests.get(self.url)
    intervals = wind_data.json()["data"]["timelines"][0]["intervals"][1:]


    for i in intervals:
      i["wind_speed"] = i["values"]["windSpeed"]
      i["temperature"] = i["values"]["temperature"]
      i["pressure"] = i["values"]["pressureSurfaceLevel"]
      del i['values']


    wind_data_df = pd.DataFrame.from_dict(intervals[:25])
    wind_data_df['startTime'] = pd.to_datetime(wind_data_df['startTime'])
    wind_data_df = wind_data_df.set_index('startTime')



    # print(weather[['wind_speed', 'temperature', 'pressure']][:25]["wind_speed"][10])
    n_row = 0
    wind_data_from_file = wind_data_from_file.reset_index()
    wind_data_df = wind_data_df.reset_index()

    for index, i in wind_data_from_file[['index', 'wind_speed', 'temperature', 'pressure']][:25].iterrows():
      wind_data_from_file.loc[index, "wind_speed"] = wind_data_df.iloc[n_row]["wind_speed"]
      wind_data_from_file.loc[index, "temperature"] = wind_data_df.iloc[n_row]["temperature"]
      wind_data_from_file.loc[index, "pressure"] = wind_data_df.iloc[n_row]["pressure"]
      wind_data_from_file.loc[index, "index"] = wind_data_df.iloc[n_row]["startTime"]
      # print(weather.loc[index, "startTime"])
      n_row += 1

    wind_data_from_file.set_index('index', inplace=True)
    wind_data_df = wind_data_from_file

    #print(wind_data_from_file[["index", "wind_speed", "temperature", "pressure"]][:25])


    return wind_data_from_file
