import pandas as pd
import datetime
from DataAcquisition import DataAcquisition
import requests


class DataFromAPI(DataAcquisition):

  def __init__(self, url, params):
    """
    This class gets weather data from an API.

    Args:
      url: url of the dataframe
      params: params to send to url (if necessary) e.g. {"a": 1, "b": 2}
    """
    self.url = url
    self.params = params


  def get_weather_data(self):
    """
    Gets weather data from an API (url)

    Returns:
      dataframe with weather data
    """

    response = requests.get(self.url, params=self.params)

    data = pd.DataFrame(response.json()["estimated_actuals"])

    # Rename the columns
    api_df = data.rename(columns={"Dhi": "dhi", "Ghi": "ghi", "Dni": "dni"})

    solc = [api_df["period_end"], api_df["dhi"], api_df["ghi"], api_df["dni"]]
    headers = ["Start", "dhi", "ghi", "dni"]

    # print(datetime.datetime.strptime("2021-08-07T23:00:00Z", "%Y-%m-%dT%H:%M:%SZ").strftime('%Y-%m-%d %H:%M:%S'))
    dataframe = pd.concat(solc, axis=1, keys=headers)

    # Convert values to float
    dataframe['ghi'] = dataframe['ghi'].apply(lambda x: float(x))
    dataframe['dni'] = dataframe['dni'].apply(lambda x: float(x))
    dataframe['dhi'] = dataframe['dhi'].apply(lambda x: float(x))

    # Change date format (to remove T and Z)
    dataframe["Start"] = dataframe.Start.apply(
      (lambda x: datetime.datetime.strptime(x, "%Y-%m-%dT%H:%M:%S.%f0Z").strftime('%Y-%m-%d %H:%M:%S')))


    # Convert index to DatetimeIndex (to allow interpolation)
    dataframe.Start = pd.to_datetime(dataframe.Start)

    # Add Start column to be the index (instead of sequential number)
    dataframe.set_index('Start', inplace=True)

    return dataframe
