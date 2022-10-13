import json
import pandas as pd
import os


class CommunityGenerator:

  def __init__(self, path_steps_minutes):
    """
    This class calculates the community netload

    Args:
      path_steps_minutes: path of the resampled consumption profiles (at 1/60Hz)
    """
    self.path_steps_minutes = path_steps_minutes


  def calculate_netload(self, netload_df):
    """
    Calculates the netload (Demand-Production) of the community and saves in the netload.csv file.
    This file contains 4 columns: Date, Demand, Production and Netload.

    Args:
      netload_df: dataframe containing at least 3 columns (Date, Demand and Production)

    Returns:
      netload dataframe with an extra column "Netload"
    """
    df = netload_df

    df.columns = ['Date', 'Demand', 'PV_Production', 'Wind_Production', 'Production']
    df["Netload"] = df["Demand"] - df["Production"]

    # Update netload csv file
    output_directory = os.path.join('', self.path_steps_minutes)
    outname = os.path.join(output_directory, 'netload.csv')
    df.to_csv(outname, columns=['Date', 'Demand', 'PV_Production', 'Wind_Production', 'Production', 'Netload'], sep=";", index=False)

    return df


  def execute(self):
    """
    Calculates the netload of a netload dataframe.
    """

    print("Calculating netload of the community")

    # Calculate community netload
    netload_df = pd.read_csv(self.path_steps_minutes + '/netload.csv', sep=';')
    self.calculate_netload(netload_df)


    # Plotd
    # netload.plot(x="Date", y=["Demand", "Production", "Netload"], kind="line", figsize=(10, 10))
    # plt.show()
