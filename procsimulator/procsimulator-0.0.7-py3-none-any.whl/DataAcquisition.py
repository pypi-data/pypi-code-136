from abc import ABC, abstractmethod

class DataAcquisition(ABC):


  @abstractmethod
  def get_weather_data(self, *args):
    """
    This function should be implemented in a class which inherits from this one.
    The goal is to define how the weather data will be acquired (API, dataset, etc). Different sources can be developed.

    Args:
      args: can have as many arguments as you want
    """
    pass


  def filter_data(self, data, start_date, end_date):
    """
    Filters dataframe according to the start and end dates

    Args:
      data: dataframe to be filtered
      start_date: start date (to be filtered)
      end_date: end date (to be filtered)
    """

    #in_range_df = data[data["Date"].isin(pd.date_range("2021-09-11 00:00:00", "2021-09-13 00:00:00"))]
    mask = (data['Date'] >= start_date) & (data['Date'] < end_date)
    df = data.loc[mask]

    return df


  def resample_data(self, data, resolution = "1min"):
    """
    Resamples dataframe according go the resolution given.

    Args:
      data: dataframe to be resampled
      resolution: resolution to resample (if not provided, 1min will be used) (e.g. 5min)

    Returns:
      resampled dataframe
    """

    # Remove duplicated indexs
    data = data[~data.index.duplicated(keep='last')]

    # Resample data
    resampled_data = data.resample(resolution).interpolate()

    return resampled_data
