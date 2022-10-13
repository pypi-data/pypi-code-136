import pandas as pd
import datetime
from DataAcquisition import DataAcquisition

#from pvlib.forecast import GFS, NAM, NDFD, HRRR, RAP



class DataFromModel(DataAcquisition):

  def __init__(self, model):
    """
    This class gets weather data from a PVLib model.

    Args:
      url: model from PVLib
    """
    self.model = model


  def get_weather_data(self):
    """
    Gets weather data from a specified model

    Returns:
      weather data
    """

    # specify location (Tucson, AZ)
    # latitude, longitude, tz = 32.6598087, -16.9256102, 'Atlantic/Madeira'
    latitude, longitude, tz = 32.2, -110.9, 'US/Arizona'

    # specify time range.
    start = pd.Timestamp(datetime.date.today(), tz=tz)
    end = start + pd.Timedelta(days=1)

    data = self.model.get_processed_data(latitude, longitude, start, end)

    return data