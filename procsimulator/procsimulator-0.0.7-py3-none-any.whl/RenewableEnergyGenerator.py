import pandas as pd
from pvlib.location import Location
import os

#from pvlib.forecast import GFS, NAM, NDFD, HRRR, RAP

from pvlib.pvsystem import PVSystem, retrieve_sam
from pvlib.temperature import TEMPERATURE_MODEL_PARAMETERS
from pvlib.tracking import SingleAxisTracker
from pvlib.modelchain import ModelChain


from windpowerlib import ModelChain as ModelChainWind, WindTurbine


class RenewableEnergyGenerator:


  def __init__(self, cg, pv_dat, wind_dat, path_steps_minutes):
    """
    This class generates the production from PV and turbines for the community. It used the DataAcquistion class to get weather data, and, based on that, calculates the quantity of production from the PVs using PVLib, and the production from turbines using windpowerlib.

    Args:
      cg: Consumption Generator instance in order to use some of its functions
      pvdat: Data Acquisiton instance in order to get solar data from PVs
      wind_dat: Data Acquisiton instance in order to get wind data from turbines
      path_steps_minutes: path of the resampled consumption profiles (at 1/60Hz)
    """
    self.cg = cg
    self.pv_dat = pv_dat
    self.wind_dat = wind_dat
    self.path_steps_minutes = path_steps_minutes


  def show_production_plot(self, power_results, start, end):
    """
    Shows a production plot based on power_results dataframe, and also based on stat and end dates.

    Args:
      power_results: the production dataframe to be plotted (has to have the column "ac")
      start: start period to be plotted
      end: end period to be plotted
    """
    # create a data frame with just AC results

    ac = pd.DataFrame(power_results, columns=["ac"], index=pd.to_datetime(power_results.index))
    ac = ac.loc[start:end]

    # add a scaled column
    ac["ac_s"] = ac["ac"] / 220

    # add a column as if the installation has the possibility to produce a maximum of 5000 Watts

    ac["ac_5k"] = ac["ac_s"] * 9000
    ac["ac_5k"].plot(figsize=(14, 6), marker='.')



  def get_first_and_last_date_of_community(self):
    """
    Gets the first and last date of the community based on the dataset (first and last rows).
    It is used to get the production for the same days as the consumption profiles.

    Returns:
      array with 2 positions: first_date [0] and last_date [1]
    """
    # Get community needs
    community = pd.read_csv(self.path_steps_minutes + '/community.csv',
                            sep=';')  # Header=None to indicate that the first row is data and not colummn names
    community.columns = ['Date', 'Power']

    # Get first and last dates of comunity needs (to get the PV Power forecast of that days)
    first_date = str(community.head(1)["Date"].values[0])
    last_date = str(community.tail(1)["Date"].values[0])

    return [first_date, last_date]




  def remove_duplicated_items(self, array):
    """
    Removes duplicated items from an array (for instance, timeslots or activities array)

    Args:
      array: timeslots/activities array

    Returns:
      array without duplicated items
    """

    tmp_number_list = []
    tmp_timeslots_list = []

    for timeslot in array:

      if (timeslot.split("-")[0] not in tmp_number_list):
        tmp_timeslots_list.append(timeslot)
        tmp_number_list.append(timeslot.split("-")[0])

    return tmp_timeslots_list



  def calculate_timeslots_list_energy(self, timeslots_list):
    """
    Calculates the total energy from the timeslots/activities of the list.
    Each position of the list/array have to have the following format XX-YY-energy-... (the energy have to be the third parameter separated by "-")

    Args:
      timeslots_list: list/array of timeslots/activities to calculate the energy

    Returns:
      total energy of the timeslots/activities of the list
    """
    total_energy = 0
    for timeslot in timeslots_list:
      total_energy += float(timeslot.split("-")[2])
    return total_energy



  def get_wind_power(self, wind_data, factor):

    enercon_e126 = {
      'turbine_type': 'E-126/4200',  # turbine type as in oedb turbine library
      'hub_height': 135  # in m
    }

    # Initialize WindTurbine object
    e126 = WindTurbine(**enercon_e126)

    # Own specifications for ModelChain setup
    modelchain_data = {
      'wind_speed_model': 'logarithmic',  # 'logarithmic' (default),
      # 'hellman' or
      # 'interpolation_extrapolation'
      'density_model': 'ideal_gas',  # 'barometric' (default), 'ideal_gas'
      #  or 'interpolation_extrapolation'
      'temperature_model': 'linear_gradient',  # 'linear_gradient' (def.) or
      # 'interpolation_extrapolation'
      'power_output_model':
        'power_coefficient_curve',  # 'power_curve' (default) or
      # 'power_coefficient_curve'
      'density_correction': True,  # False (default) or True
      'obstacle_height': 0,  # default: 0
      'hellman_exp': None}  # None (default) or None

    # Initialize ModelChain with own specifications and use run_model method to calculate power output
    mc_e126 = ModelChainWind(e126, **modelchain_data).run_model(wind_data)

    # Write power output time series to WindTurbine object
    e126.power_output = mc_e126.power_output

    # Get first 24 hours
    wind_power = e126.power_output
    wind_power = wind_power[:25]

    # Normalize wind production
    wind_power_norm = wind_power / wind_power.max() * factor
    wind_power_norm.plot(legend=True, label='Wind Production')

    return wind_power_norm





  def get_pv_power(self, data, modules_per_string, strings_per_inverter, latitude, longitude):
    """
    Calculates the PV power based on the solar data as well as some coordinates.

    Args:
      data: weather data (dataframe)
      modules_per_string: modules per string for the PV system
      strings_per_inverter: strins per inverter for the PV system
      latitude: latitude of the PVs
      longitude: longitude of the PVs

    Returns:
      dataframe with the power data
    """

    sandia_modules = retrieve_sam('sandiamod')
    cec_inverters = retrieve_sam('cecinverter')
    module = sandia_modules['Canadian_Solar_CS5P_220M___2009_']
    inverter = cec_inverters['ABB__MICRO_0_25_I_OUTD_US_208__208V_']
    # inverter = cec_inverters['SMA_America__SC630CP_US__with_ABB_EcoDry_Ultra_transformer_']
    temperature_model_parameters = TEMPERATURE_MODEL_PARAMETERS['sapm']['open_rack_glass_glass']

    # system = SingleAxisTracker(module_parameters=module, inverter_parameters=inverter, temperature_model_parameters=temperature_model_parameters, modules_per_string=modulesPerString, strings_per_inverter=stringsPerInverter)


    system = PVSystem(surface_tilt=20, surface_azimuth=200, module_parameters=module, inverter_parameters=inverter,
                      temperature_model_parameters=temperature_model_parameters)

    location = Location(latitude=latitude, longitude=longitude)
    mc = ModelChain(system, location)
    mc.run_model(data);

    power_results = mc.results.ac

    #show_production_plot(powerResults, "2022-02-25", "2022-02-25")

    power_dataframe = pd.DataFrame({'Date': power_results.index, 'Power': power_results.values})
    return power_dataframe



  def normalize_power_dataframe(self, power_dataframe, max_power, factor):
    """
    Normalizes the power dataframe (divides by the max power) and multiplies by a factor

    Args:
      power_dataframe: the power dataframe to be normalized
      max_power: max power value (all the values of the dataframe will be divided by this value)
      factor: value to be multiplied (all the values of the dataframe will be multiplied by this value)

    Returns:
      normalized power dataframe
    """

    power_dataframe_normalized = power_dataframe
    power_dataframe_normalized["Power"] = (power_dataframe_normalized["Power"] / max_power) * factor

    power_dataframe_normalized.loc[power_dataframe_normalized.Power < 0.0, 'Power'] = 0

    return power_dataframe_normalized




  def execute(self):
    """
    Executes a set of functions in order to calculate the production and save in a netload.csv file (with the consumption as well as a production column).
    This is just an example of how the functions can be used to obtain the expected result.
    """


    print("Renewable Energy Generator")

    # Get weather data from models (from different ways)
    # data = DataAcquisition.get_weather_data_from_model(GFS())
    # data = DataAcquisition.get_weather_data_from_csv()
    data = self.pv_dat.get_weather_data()
    # data = DataAcquisition.get_weather_data_from_api()

    # Resample data to 1 minute
    resampled_data = self.pv_dat.resample_data(data, "1min")

    # Get PV Power Forecast based on weather models
    power = self.get_pv_power(resampled_data, 2, 1000, 32.756, -17.179)


    # Get community needs
    community = pd.read_csv(self.path_steps_minutes + '/community.csv', sep=';')  # Header=None to indicate that the first row is data and not colummn names
    community.columns = ['Date', 'Power']

    # Get first and last dates of comunity needs (to get the PV Power forecast of that days)
    first_date = self.get_first_and_last_date_of_community()[0]
    last_date = self.get_first_and_last_date_of_community()[1]

    # Filter PV Power Forecast to get power for the same days as the community needs
    filtered_data = self.pv_dat.filter_data(power, first_date, last_date)

    # Update energy csv file
    output_directory = os.path.join('', self.path_steps_minutes)
    outname = os.path.join(output_directory, 'energy.csv')
    filtered_data.to_csv(outname, columns=['Date', 'Power'], sep=";", index=False)


    # Set Index of Community Needs
    community = community.set_index('Date')
    community.index = pd.to_datetime(community.index)


    # Set Index of PV Power Forecast
    filtered_data = filtered_data.set_index('Date')
    filtered_data['Power'] = filtered_data['Power'].fillna(0)
    filtered_data.index = pd.to_datetime(filtered_data.index)


    energy_contracted_power = self.cg.calculate_contracted_power(self.cg.get_community())*0.5
    print("energy contracted: " + str(energy_contracted_power))
    filtered_data = self.normalize_power_dataframe(filtered_data, 220, energy_contracted_power) # Normalize dataframe and multiply by 220
    filtered_data.loc[filtered_data['Power'] < 0, 'Power'] = 0 # Remove negative power (convert it to zero)


    # Merges the community demand with the PV production
    production = pd.merge(community, filtered_data, on='Date')
    production = production.reset_index()

    # Calculates wind power based on weather data
    wind_power_df = self.get_wind_power(self.wind_dat.get_weather_data(), energy_contracted_power*0.2)
    # Upsample to steps of 1 minute
    wind_power_df.index = pd.to_datetime(wind_power_df.index) # In order to resample, the index have to be converted in datetime index
    wind_power_df = wind_power_df.resample('1T').interpolate(method='polynomial',order=3)[:25*60][:-1]

    wind_power_df = wind_power_df.reset_index() # Remove index in order to change the column name
    wind_power_df = wind_power_df.rename({'index': 'Date'}, axis=1) # Change column names

    wind_power_df["Date"] = production["Date"] # Update the wind production dates to the same as the netload dataframe

    wind_power_df = wind_power_df.set_index('Date')
    wind_power_df.index = pd.to_datetime(wind_power_df.index)


    # Reindex columns and renames
    production = production.reindex(columns=['Date', 'Power_y', 'Power_x'])
    production = production.rename({'Power_y': 'PV_Production', 'Power_x': 'Demand'}, axis=1) # Change column names

    # Sets index in order to allow to merge with winder_power_df dataframe
    production = production.set_index('Date')
    production.index = pd.to_datetime(production.index)


    # Merge wind production with the production (demand + pv production)
    production = pd.merge(production, wind_power_df, on='Date')
    production = production.rename({'feedin_power_plant': 'Wind_Production'}, axis=1) # Change column names
    production = production.reset_index()


    # Calculates total of production (PV + Wind)
    production["Production"] = production["PV_Production"] + production["Wind_Production"]

    print(production)


    # Create netload csv file to store the production
    output_directory = os.path.join('', self.path_steps_minutes)
    outname = os.path.join(output_directory, 'netload.csv')
    production.to_csv(outname, columns=['Date', 'Demand', 'PV_Production', 'Wind_Production', 'Production'], sep=";", index=False)


    #filtered_data.plot(figsize=(14, 6), marker='.')
    #showNetloadGraph('output/minute')



