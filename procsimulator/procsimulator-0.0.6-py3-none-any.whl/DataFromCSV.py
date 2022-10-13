import pandas as pd
import datetime
from DataAcquisition import DataAcquisition


class DataFromCSV(DataAcquisition):

  def __init__(self, file_path):
    """
    This class gets weather data from a CSV file (dataframe).

    Args:
      file_path: path of the CSV file with weather data
    """
    self.file_path = file_path


  def get_weather_data(self):
    """
    Gets weather data from the CSV file (dataframe)

    Returns:
      dataframe with weather data
    """

    solcastDf = pd.read_csv(self.file_path, sep=',')  # Header=None to indicate that the first row is data and not colummn names
    solcastDf = solcastDf.rename(columns={"Dhi": "dhi", "Ghi": "ghi", "Dni": "dni"})

    solc = [solcastDf["PeriodStart"], solcastDf["dhi"], solcastDf["ghi"], solcastDf["dni"]]
    headers = ["Start", "dhi", "ghi", "dni"]

    # print(datetime.datetime.strptime("2021-08-07T23:00:00Z", "%Y-%m-%dT%H:%M:%SZ").strftime('%Y-%m-%d %H:%M:%S'))
    dataframe = pd.concat(solc, axis=1, keys=headers)

    # Change date format (to remove T and Z)
    dataframe["Start"] = dataframe.Start.apply(
      (lambda x: datetime.datetime.strptime(x, "%Y-%m-%dT%H:%M:%SZ").strftime('%Y-%m-%d %H:%M:%S')))

    # Convert index to DatetimeIndex (to allow interpolation)
    dataframe.Start = pd.to_datetime(dataframe.Start)

    # Add Start column to be the index (instead of sequential number)
    dataframe.set_index('Start', inplace=True)

    return dataframe
