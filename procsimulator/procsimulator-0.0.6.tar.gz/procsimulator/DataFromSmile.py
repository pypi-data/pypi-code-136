import pandas as pd
import datetime
from DataAcquisition import DataAcquisition
import requests


class DataFromSmile(DataAcquisition):

  def __init__(self, url):
    """
    This class gets weather data from Smile API.

    Args:
      url: url of the Smile API
    """
    self.url = url


  def change_date_format(self, date):
    """
    Changes date format to remove 'T' and 'Z' (used in smile dataframe)

    Args:
      date: date to be formatted

    Returns:
      date with the new format
    """
    try:
      return datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f0Z").strftime('%Y-%m-%d %H:%M:%S')
    except:
      return datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")

    try:
      return datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ").strftime('%Y-%m-%d %H:%M:%S')
    except:
      return datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f0Z")



  def get_weather_data(self):
    """
    Gets weather data from the Smile dataset

    Returns:
      dataframe with weather data
    """

    #response = requests.get('https://smile.prsma.com/public/solcast-radiation-forecast/Fazendinha_solcast-radiation-forecast_2022_30min_all.csv')
    response = requests.get(self.url)

    line = response.text.split("\n")

    mat = [n.split(',') for n in line]

    data = pd.DataFrame(mat)
    data.columns = data.iloc[0] # The columns will be the first row of the dataset
    data = data.reindex(data.index.drop(0)) # Drop the first row after setting as columns

    # Rename the columns
    smile_df = data.rename(columns={"Dhi": "dhi", "Ghi": "ghi", "Dni": "dni"})

    # Create subset of the dataset with just 4 columns (Start, dhi, ghi and dni)
    smile = [smile_df["period_end"], smile_df["dhi"], smile_df["ghi"], smile_df["dni"]]
    headers = ["Start", "dhi", "ghi", "dni"]

    # print(datetime.datetime.strptime("2021-08-07T23:00:00Z", "%Y-%m-%dT%H:%M:%SZ").strftime('%Y-%m-%d %H:%M:%S'))
    # Create dataframe with headers and smile data
    dataframe = pd.concat(smile, axis=1, keys=headers)

    # Remove null values
    dataframe = dataframe[dataframe.Start.notnull()]
    dataframe = dataframe[dataframe.dni.notnull()]
    dataframe = dataframe[dataframe.dhi.notnull()]
    dataframe = dataframe[dataframe.ghi.notnull()]

    # Convert values to float
    dataframe['ghi'] = dataframe['ghi'].apply(lambda x: float(x))
    dataframe['dni'] = dataframe['dni'].apply(lambda x: float(x))
    dataframe['dhi'] = dataframe['dhi'].apply(lambda x: float(x))

    # Change date format (to remove T and Z)
    dataframe["Start"] = dataframe.Start.apply((lambda x: self.change_date_format(x)))


    # Convert index to DatetimeIndex (to allow interpolation)
    dataframe.Start = pd.to_datetime(dataframe.Start)

    # Add Start column to be the index (instead of sequential number)
    dataframe.set_index('Start', inplace=True) # inplace = True updates the dataframe without doing datafame = dataframe.set_index

    return dataframe
