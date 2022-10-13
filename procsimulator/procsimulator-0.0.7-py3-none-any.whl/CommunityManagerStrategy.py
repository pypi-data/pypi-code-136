from CommunityManager import CommunityManager
from ConsumptionGenerator import ConsumptionGenerator
from Knapsack import Knapsack
import pandas as pd
import os
import math
import shutil
import errno
import datetime


class CommunityManagerStrategy(CommunityManager):

  def __init__(self, cg, path_steps_minutes, path_steps_after_first, path_steps_after_second):
    """
    This class is a load balancing strategy implemented using Multiple Knapsack (which is a combinatorial optimization problem).
    Taking in consideration the objective functions and constraints, it shifts the consumption of the activities.

    Args:
      cg: Consumption Generator instance (to allow to use its functions)
      path_steps_minutes: path of the resampled consumption profiles (at 1/60Hz)
      path_steps_after_first: path of the consumption profiles after the 1st step of the optimization
      path_steps_after_second: path of the consumption profiles after the 2nd step of the optimization
    """
    self.cg = cg
    self.path_steps_minutes = path_steps_minutes
    self.path_steps_after_first = path_steps_after_first
    self.path_steps_after_second = path_steps_after_second


  def calculate_bin_used_capacity(self, bins_capacities, placed_timeslots, production_baseload, n_bins_per_hour):
    """
    Updates the bin capacity for the second part of the optimization (increases the production_baseload to the bin capacity of the first part, and subtracts the energy of the placed timeslots in the first step.

    Args:
      bins_capacities: bin capacities of the bins in the 1st step of the optimization
      placed_timeslots: placed timeslots in the 1st step (in order to subtract the energy of them to the bin capacity) - if they are placed, the bin capacity decreases
      production_baseload: value to increment in the bin capacities, which corresponds to the value of energy that can be acquired from the grid in the 2nd step
      n_bins_per_hour: number of bins per hour (parameter of the strategy) to know the quantity of bins in a day (e.g. if bins of 30 minutes, n_bins_per_hour = 2)

    Returns:
      array with x positions in a day (where the number of positions is 24*n_bins_per_hour) with the bin capacity of each bin
    """

    binUsedCapacity = [0] * 24 * n_bins_per_hour

    for bin in range(len(bins_capacities)):
      binUsedCapacity[bin] = bins_capacities[bin]
      binUsedCapacity[bin] += production_baseload

    for timeslot in placed_timeslots:
      tm = timeslot.split("-")
      weight = float(tm[2])
      bin = int(tm[3]) - 1  # bin 1 is 0 position (00:00-00:59)
      binUsedCapacity[bin] -= weight

    return binUsedCapacity


  def get_production_max_after_first_optimization(self, netload_second_optim, fd, production_baseload, n_bins_per_hour, fact):
    """
    Calculates the maximum production peak for each bin of the second step (calculates the maximum in the netload dataframe after updating the profiles of 1st step, and have to increase the production_baseload and decrease the energy of the placed timeslots of the 1st step)

    Args:
      netload_second_optim: dataframe which contains the netload after updating the profiles of the 1st step (to calculate the maximum peak in the 2nd step)
      fd: consumption profile date (to
      production_baseload: value to increment in the bin capacities, which corresponds to the value of energy that can be acquired from the grid in the 2nd step
      n_bins_per_hour: number of bins per hour (parameter of the strategy) to know the quantity of bins in a day (e.g. if bins of 30 minutes, n_bins_per_hour = 2)
      fact: minutes of each bin (e.g. if bins of 30 minutes, fact = 30)

    Returns:
      array with x positions in a day (where the number of positions is 24*n_bins_per_hour) with the bin maximum production peak of each bin
    """

    bins_maximum_second_optimization = []
    for z in range(0, 24):

      startMin = 0
      endMin = fact - 1
      for w in range(0, n_bins_per_hour):
        max = netload_second_optim[
          (netload_second_optim['Date'] >= str(fd) + ' ' + str(z).zfill(2) + ':' + str(startMin).zfill(2) + ':00') & (
              netload_second_optim['Date'] <= str(fd) + ' ' + str(z).zfill(2) + ':' + str(endMin).zfill(2) + ':00')][
          'Production'].max()
        # demand when the production is max
        binUsage = netload_second_optim.loc[netload_second_optim[
          (netload_second_optim['Date'] >= str(fd) + ' ' + str(z).zfill(2) + ':' + str(startMin).zfill(2) + ':00') & (
              netload_second_optim['Date'] <= str(fd) + ' ' + str(z).zfill(2) + ':' + str(endMin).zfill(2) + ':00')][
          'Production'].idxmax()]["Demand"]
        bins_maximum_second_optimization.append(max + production_baseload - binUsage)

        startMin = startMin + fact
        endMin = endMin + fact

    return bins_maximum_second_optimization


  def remove_flexible_consumption(self):
    """
    Removes the flexible consumption of the consumption profile, in order to have the baseload consumption (that consumption that can not be shifted.
    In order to do this, the consumption of the flexible appliances are subtracted from the netload and community dataframes (notice that each flexible has it own consumption profile for each house)

    Returns:
      netload dataframe with the non-flexible consumption
    """

    flexible_timeslots = self.cg.get_timeslots(self.cg.get_community(), True)

    df_community = pd.read_csv(self.path_steps_after_first + '/community.csv', sep=';')  # Header=None to indicate that the first row is data and not colummn names
    df_community.columns = ['Date', 'Power']

    df_netload = pd.read_csv(self.path_steps_after_first + '/netload.csv', sep=';')  # Header=None to indicate that the first row is data and not colummn names
    df_netload.columns = ['Date', 'Demand', 'PV_Production', 'Wind_Production', 'Production', 'Netload']


    for timeslot in flexible_timeslots:

      df_appliance = pd.read_csv(self.path_steps_after_first + '/house' + str(timeslot["House"]) + '/' + timeslot["Appliance"] + ".csv", sep=';')  # Header=None to indicate that the first row is data and not colummn names
      df_appliance.columns = ['Date', 'Power']

      df_total = pd.read_csv(self.path_steps_after_first + '/house' + str(timeslot["House"]) + '/total.csv', sep=';')  # Header=None to indicate that the first row is data and not colummn names
      df_total.columns = ['Date', 'Power']

      start_obj = datetime.datetime.strptime(timeslot["Start"], '%Y-%m-%d %H:%M:%S')  # Convert string to datetime object
      end_obj = datetime.datetime.strptime(timeslot["End"], '%Y-%m-%d %H:%M:%S')  # Convert string to datetime object
      obj = start_obj

      while (obj != end_obj + datetime.timedelta(minutes=1)):

        # Update house total consumption
        indexTotal = df_total[df_total.Date == str(obj)].index  # Get index of the row

        df_total.loc[indexTotal, 'Power'] = float(df_total[df_total.Date == str(obj)]["Power"]) - float(df_appliance[df_appliance.Date == str(obj)]["Power"])

        # Update community consumption
        indexCommunity = df_community[df_community.Date == str(obj)].index  # Get index of the row
        df_community.loc[indexCommunity, 'Power'] = float(df_community[df_community.Date == str(obj)]["Power"]) - float(df_appliance[df_appliance.Date == str(obj)]["Power"])


        # Update community netload
        indexNetload = df_netload[df_netload.Date == str(obj)].index  # Get index of the row
        df_netload.loc[indexNetload, 'Demand'] = float(df_netload[df_netload.Date == str(obj)]["Demand"]) - float(df_appliance[df_appliance.Date == str(obj)]["Power"])

        # Update appliance consumption - has to be the last update since the others dataframes use this dataframe
        indexAppliance = df_appliance[df_appliance.Date == str(obj)].index  # Get index of the row
        df_appliance.loc[indexAppliance, 'Power'] = 0

        obj = obj + datetime.timedelta(minutes=1)  # Next minute


      # After all minutes of the appliance updated
      output_directory = os.path.join('', self.path_steps_after_first + '/house' + str(timeslot["House"]))

      outname = os.path.join(output_directory, str(timeslot["Appliance"]) + '.csv')
      df_appliance.to_csv(outname, columns=['Date', 'Power'], sep=";", index=False)

      outname = os.path.join(output_directory, 'total.csv')
      df_total.to_csv(outname, columns=['Date', 'Power'], sep=";", index=False)

    output_directory = os.path.join('', self.path_steps_after_first)
    outname = os.path.join(output_directory, 'community.csv')
    df_community.to_csv(outname, columns=['Date', 'Power'], sep=";", index=False)

    outname = os.path.join(output_directory, 'netload.csv')
    df_netload.to_csv(outname, columns=['Date', 'Demand', 'PV_Production', 'Wind_Production', 'Production', 'Netload'], sep=";", index=False)

    return df_netload



  def create_profiles_after_strategy(self, placed_timeslots, all_timeslots_objects, initial_path, final_path, short_initial_path, short_final_path, remove_flex_cons, n_bins_per_hour, fact):
    """
    Implementing the abstract function (from the parent) which updates the profiles after applying the strategy.

    Args:
      placed_timeslots: array of the placed timeslots
      all_timeslots_objects: array of all timeslots with all the information (Start, End, Appliance, Power, House, etc)
      initial_path: path of the minutes (1/60Hz) dataframe (e.g. "(...)/output/minute")
      final_path: path of the dataframe after the strategy (e.g. "(...)/output/afteroptimization")
      short_initial_path: folder of the minutes (1/60Hz) dataframe (e.g. "minutes")
      short_final_path: folder of the dataframe after the strategy e.g. "afteroptimization")
      remove_flex_cons: if True, the flexible consumption will be removed, otherwise the flexible consumption will not be removed (in 1st step, it was True to remove the flexible consumption and in the 2nd step it was False because the flexible consumption has already been removed)
      n_bins_per_hour: number of bins per hour (parameter of the strategy) to know the quantity of bins in a day (e.g. if bins of 30 minutes, n_bins_per_hour = 2)
      fact: minutes of each bin (e.g. if bins of 30 minutes, fact = 30)

    Returns:
      output of update_consumption_profiles_based_on_optimization function
    """
    return self.update_consumption_profiles_based_on_optimization(placed_timeslots, all_timeslots_objects, initial_path, final_path, short_initial_path, short_final_path, remove_flex_cons, n_bins_per_hour, fact)


  def update_consumption_profiles_based_on_optimization(self, placed_timeslots, all_timeslots_objects, initial_path, final_path, short_initial_path, short_final_path, remove_flex_cons, n_bins_per_hour, fact):
    """
    Implementing the function which updates the profiles after applying the strategy.

    Args:
      placed_timeslots: array of the placed timeslots
      all_timeslots_objects: array of all timeslots with all the information (Start, End, Appliance, Power, House, etc)
      initial_path: path of the minutes (1/60Hz) dataframe (e.g. "(...)/output/minute")
      final_path: path of the dataframe after the strategy (e.g. "(...)/output/afteroptimization")
      short_initial_path: folder of the minutes (1/60Hz) dataframe (e.g. "minutes")
      short_final_path: folder of the dataframe after the strategy e.g. "afteroptimization")
      remove_flex_cons: if True, the flexible consumption will be removed, otherwise the flexible consumption will not be removed (in 1st step, it was True to remove the flexible consumption and in the 2nd step it was False because the flexible consumption has already been removed)
      n_bins_per_hour: number of bins per hour (parameter of the strategy) to know the quantity of bins in a day (e.g. if bins of 30 minutes, n_bins_per_hour = 2)
      fact: minutes of each bin (e.g. if bins of 30 minutes, fact = 30)

    Returns:
      array with 2 positions: array of the placed timeslots [0] and flexible dataframe [1]
    """
    # Remove all files of the folder and the folder (before copying the consumption profiles)
    if os.path.exists(final_path):
      shutil.rmtree(final_path)

    # Create the folder
    if not os.path.exists(final_path):
      os.mkdir(final_path)


    # Copy the consumption profiles to after optimization folder in order to change it consumption after the optimization of the timeslots
    try:
      src_files = os.listdir(initial_path)
      for file_name in src_files:
        full_file_name = os.path.join(initial_path, file_name)
        if os.path.isfile(full_file_name):
          shutil.copy(full_file_name, final_path)
        elif os.path.isdir(full_file_name):
          shutil.copytree(full_file_name, full_file_name.replace(short_initial_path, short_final_path))
    except OSError as e:
      if e.errno != errno.EEXIST:
        raise

    # community profile
    # communityBefore = pd.read_csv('output/minute/community.csv', sep=';')  # Header=None to indicate that the first row is data and not colummn names
    # communityBefore.columns = ['Date', 'Power']


    df_flexible = ""
    if (remove_flex_cons):
      df_flexible = self.remove_flexible_consumption()
      #showNetloadGraph(finalPath + '/netload.csv')


    community_after = pd.read_csv(final_path + '/community.csv', sep=';')  # Header=None to indicate that the first row is data and not colummn names
    community_after.columns = ['Date', 'Power']

    netload_after = pd.read_csv(final_path + '/netload.csv', sep=';')  # Header=None to indicate that the first row is data and not colummn names
    netload_after.columns = ['Date', 'Demand', 'PV_Production', 'Wind_Production', 'Production', 'Netload']


    # Reset community consumption
    #community_after['Power'] = 0
    #netload_after['Demand'] = 0


    placed_appliances = []
    placed_houses = []
    placed_timeslots_array = []


    for timeslot in placed_timeslots:

      timeslot = timeslot.split("-")
      first_item_date = str(int(timeslot[5])-1)
      timeslot_number = int(timeslot[0])
      timeslot_sub_item_number = int(timeslot[1])
      timeslot_power = float(timeslot[2])
      timeslot_first_bin = str(int(timeslot[3]) - 1) # bin 1 corresponds to midnight, bin 2 corresponds to 1 am, etc
      timeslot_number_of_bins = timeslot[4]
      timeslot_last_bin = str(int(first_item_date) + (int(timeslot_number_of_bins) - 1))
      timeslot_bin_before_opt = str(int(timeslot[7]) - 1)


      # Gets all the fields of the timeslot (Start, End, Appliance, House, etc)
      timeslot_obj = all_timeslots_objects[timeslot_number]  # If a timeslot is placed, all the subitemms are placed

      # each house consumption profile
      # total_before = pd.read_csv('output/minute/house' + str(timeslotObj["House"]) + '/total.csv', sep=';')
      # total_before.columns = ['Date', 'Power']

      total_after = pd.read_csv(final_path + '/house' + str(timeslot_obj["House"]) + '/total.csv', sep=';')
      total_after.columns = ['Date', 'Power']

      # Reset all houses consumption
      #if (str(timeslot_obj["House"]) not in placed_houses):
        #total_after['Power'] = 0
        #placed_houses.append(str(timeslot_obj["House"]))

      # each appliance consumption profile (of a specific house)
      df_before = pd.read_csv(self.path_steps_minutes + '/house' + str(timeslot_obj["House"]) + '/' + timeslot_obj["Appliance"] + ".csv", sep=';')  # Header=None to indicate that the first row is data and not colummn names
      df_before.columns = ['Date', 'Power']

      df_after = pd.read_csv(final_path + '/house' + str(timeslot_obj["House"]) + '/' + timeslot_obj["Appliance"] + ".csv", sep=';')  # Header=None to indicate that the first row is data and not colummn names
      df_after.columns = ['Date', 'Power']

      # Reset all appliance consumption
      #if ((str(timeslot_obj["House"]) + "-" + str(timeslot_obj["Appliance"])) not in placed_appliances):
        #dfAfter['Power'] = 0
        #placed_appliances.append(str(timeslot_obj["House"]) + "-" + str(timeslot_obj["Appliance"]))

      # when there's more than one item of a timeslot:
      # 1) if its the first hour - starts at the first minutes of the timeslot and ends at 59 miutes
      # 2) if its a middle hour (not the first and not the last) - starts at 00 minutes and ends at 59 minutes
      # 3) if its the last hour - starts at 00 and ends at the last minutes of the timeslot
      # e.g. timeslot from 8.53 to 10.15:
      # hour 8 (bin 9) -> 08:53 (original) - 08:59 (first)
      # hour 9 (bin 10) -> 09:00 - 09:59 (middle)
      # hour 10 (bin 11) -> 10:00 - 10:15 (original) (last)

      tim_new_hour = int(math.floor(int(timeslot_first_bin)/n_bins_per_hour))
      tim_new_min = int((int(timeslot_first_bin)%n_bins_per_hour)*fact)
      tim_old_hour = int(math.floor(int(timeslot_bin_before_opt)/n_bins_per_hour))
      tim_old_min = int((int(timeslot_bin_before_opt) % n_bins_per_hour) * fact)


      if (int(timeslot_number_of_bins) > 1):
        if (int(first_item_date) == int(timeslot_first_bin)):

          timeslot_start_date = str(timeslot_obj["Start"])
          timeslot_end_date = str(timeslot_obj["Start"])[0:11] + str(tim_old_hour).zfill(2) + ":" + str(tim_old_min + (fact - 1)).zfill(2) + ":00"
          new_optimization_start_date = str(timeslot_obj["Start"])[0:11] + str(tim_new_hour).zfill(2) + ":" + str(int(tim_new_min+(fact-1)) - (int(tim_old_min+(fact-1))-int(timeslot_obj["Start"][14:16]))).zfill(2) + ":00"
          new_optimization_end_date = str(timeslot_obj["Start"])[0:11] + str(tim_new_hour).zfill(2) + ":" + str(tim_new_min + (fact - 1)).zfill(2) + ":00"

        elif (int(timeslot_first_bin) == int(timeslot_last_bin)):

          timeslot_start_date = str(timeslot_obj["Start"])[0:11] + str(tim_old_hour).zfill(2) + ":" + str(tim_old_min).zfill(2) + ":00"
          timeslot_end_date = str(timeslot_obj["End"])
          new_optimization_start_date = str(timeslot_obj["Start"])[0:11] + str(tim_new_hour).zfill(2) + ":" + str(tim_new_min).zfill(2) + ":00"
          new_optimization_end_date = str(timeslot_obj["Start"])[0:11] + str(tim_new_hour).zfill(2) + ":" + str(int(tim_new_min) + (int(timeslot_obj["End"][14:16])-int(tim_old_min))).zfill(2) + ":00"

        else:

          timeslot_start_date = str(timeslot_obj["Start"])[0:11] + str(tim_old_hour).zfill(2) + ":" + str(tim_old_min).zfill(2) + ":00"
          timeslot_end_date = str(timeslot_obj["Start"])[0:11] + str(tim_old_hour).zfill(2) + ":" + str(tim_old_min + (fact - 1)).zfill(2) + ":00"
          new_optimization_start_date = str(timeslot_obj["Start"])[0:11] + str(tim_new_hour).zfill(2) + ":" + str(tim_new_min).zfill(2) + ":00"
          new_optimization_end_date = str(timeslot_obj["Start"])[0:11] + str(tim_new_hour).zfill(2) + ":" + str(tim_new_min + (fact - 1)).zfill(2) + ":00"

      else:

        timeslot_start_date = str(timeslot_obj["Start"])
        timeslot_end_date = str(timeslot_obj["End"])
        new_optimization_start_date = str(timeslot_obj["Start"])[0:11] + str(tim_new_hour).zfill(2) + ":" + str(int(tim_new_min + (fact - 1)) - (int(tim_old_min + (fact - 1)) - int(timeslot_obj["Start"][14:16]))).zfill(2) + ":00"
        new_optimization_end_date = str(timeslot_obj["Start"])[0:11] + str(tim_new_hour).zfill(2) + ":" + str(int(tim_new_min) + (int(timeslot_obj["End"][14:16]) - int(tim_old_min))).zfill(2) + ":00"


      # list of placed timeslots
      placed_timeslots_array.append(str(timeslot_obj["House"]) + "*" + str(timeslot_obj["Appliance"]) + "*" + str(timeslot_number) + "*" + str(new_optimization_start_date) + "*" + str(new_optimization_end_date))


      # before optimization (original)
      start_obj_before = datetime.datetime.strptime(timeslot_start_date, '%Y-%m-%d %H:%M:%S')  # Convert string to datetime object
      end_obj_before = datetime.datetime.strptime(timeslot_end_date, '%Y-%m-%d %H:%M:%S')  # Convert string to datetime object
      obj_before = start_obj_before

      # after optimization
      start_obj_after = datetime.datetime.strptime(new_optimization_start_date, '%Y-%m-%d %H:%M:%S')  # Convert string to datetime object
      end_obj_after = datetime.datetime.strptime(new_optimization_end_date, '%Y-%m-%d %H:%M:%S')  # Convert string to datetime object
      obj_after = start_obj_after


      while (obj_after != end_obj_after + datetime.timedelta(minutes=1)):


        index_netload_after = netload_after[netload_after.Date == str(obj_after)].index  # Get index of the row
        index_after = community_after[community_after.Date == str(obj_after)].index  # Get index of the row
        index_total_after = total_after[total_after.Date == str(obj_after)].index  # sGet index of the row
        index_app_after = df_after[df_after.Date == str(obj_after)].index  # Get index of the row


        netload_after.loc[index_netload_after, 'Demand'] = float(netload_after[netload_after.Date == str(obj_after)]["Demand"]) + float(df_before[df_before.Date == str(obj_before)]["Power"])  # Subtract the energy of that timeslot from the community energy
        netload_after.loc[netload_after['Production'] < 0, 'Production'] = 0


        community_after.loc[index_after, 'Power'] = float(community_after[community_after.Date == str(obj_after)]["Power"]) + float(df_before[df_before.Date == str(obj_before)]["Power"])  # Subtract the energy of that timeslot from the community energy

        total_after.loc[index_total_after, 'Power'] = float(total_after[total_after.Date == str(obj_after)]["Power"]) + float(df_before[df_before.Date == str(obj_before)]["Power"])  # Subtract the energy of that timeslot from the total energy of that house (the house which corresponds the timeslot)
        df_after.loc[index_app_after, 'Power'] = float(df_after[df_after.Date == str(obj_after)]["Power"]) + float(df_before[df_before.Date == str(obj_before)]["Power"])  # Subtract the energy of that timeslot from the total energy of that house (the house which corresponds the timeslot)

        obj_before = obj_before + datetime.timedelta(minutes=1)  # Next minute
        obj_after = obj_after + datetime.timedelta(minutes=1)  # Next minute


      # After while - when the consumption profile is updated for each minute of the timeslot
      output_directory = os.path.join('', final_path + '/house' + str(timeslot_obj["House"]))
      outname = os.path.join(output_directory, str(timeslot_obj["Appliance"]) + '.csv')
      df_after.to_csv(outname, columns=['Date', 'Power'], sep=";", index=False)

      # After all timeslots updated - update the total of each house
      output_directory = os.path.join('', final_path + '/house' + str(timeslot_obj["House"]))
      outname = os.path.join(output_directory, 'total.csv')
      df_after.to_csv(outname, columns=['Date', 'Power'], sep=";", index=False)

    netload_after["Netload"] = netload_after["Demand"] - netload_after["Production"]

    # After all timeslots updated - update the community profile
    output_directory = os.path.join('', final_path)
    outname = os.path.join(output_directory, 'community.csv')
    community_after.to_csv(outname, columns=['Date', 'Power'], sep=";", index=False)

    # After all timeslots updated - update the community profile
    outname = os.path.join(output_directory, 'netload.csv')
    netload_after.to_csv(outname, columns=['Date', 'Demand', 'PV_Production', 'Wind_Production', 'Production', 'Netload'], sep=";", index=False)


    return [placed_timeslots_array, df_flexible]


  def execute(self):
    """
    Executes the optimization process (implemented strategy using Multiple Knapsack):
    1) First step
    - Prepares the input (arrays) for the process (bin_capacities, bin_maximums, timeslots_number, flexibitilies, items_max, etc)
    - Calls the Knapsack class with the input processed (execute_knapsack function)
    - Updates the consumption profiles based on the output of the knapsack
    2) Second Step
    - Prepares the input (arrays) for the process (bin_capacities, bin_maximums, timeslots_number, flexibitilies, items_max, etc)
    - Calls the Knapsack class with the input processed (execute_knapsack function)
    - Updates the consumption profiles based on the output of the knapsack
    """

    print("Optimization the community using the implemented strategy")

    netload = pd.read_csv(self.path_steps_minutes + '/netload.csv',
                          sep=';')  # Header=None to indicate that the first row is data and not colummn names
    netload.columns = ['Date', 'Demand', 'PV_Production', 'Wind_Production', 'Production', 'Netload']

    # Plotd
    # netload.plot(x="Date", y=["Demand", "Production", "Netload"], kind="line", figsize=(10, 10))
    # plt.show()

    fd = str(netload.iloc[0]["Date"])[0:10]
    bins_capacities = []
    bins_maximum = []
    fact = 60
    n_bins_per_hour = int(60 / fact)

    for z in range(0, 24):
      startMin = 0
      endMin = fact - 1
      for w in range(0, n_bins_per_hour):
        avg = netload[
          (netload['Date'] >= str(fd) + ' ' + str(z).zfill(2) + ':' + str(startMin).zfill(2) + ':00') & (
                  netload['Date'] <= str(fd) + ' ' + str(z).zfill(2) + ':' + str(endMin).zfill(2) + ':00')][
          'Production'].mean()
        max = netload[
          (netload['Date'] >= str(fd) + ' ' + str(z).zfill(2) + ':' + str(startMin).zfill(2) + ':00') & (
                  netload['Date'] <= str(fd) + ' ' + str(z).zfill(2) + ':' + str(endMin).zfill(2) + ':00')][
          'Production'].max()
        bins_capacities.append(avg)
        bins_maximum.append(max)

        startMin = startMin + fact
        endMin = endMin + fact

    self.timeslots = self.cg.get_timeslots(self.cg.get_community(), True)

    community = self.cg.get_community()
    appliances_flexibility = {"DISHWASHER": 12, "VACUUMCLEANER": 8, "WASHINGMACHINE": 10, "DRYER": 5, "IRON": 5,
                             "COOKINGSTOVE": 1}
    # appliances_flexibility = {"DISHWASHER": 12, "VACUUMCLEANER": 12, "WASHINGMACHINE": 12, "DRYER": 12, "IRON": 12, "COOKINGSTOVE": 12}
    flexibilities_array = self.cg.get_community_flexibility(community)
    contracted_power = self.cg.calculate_contracted_power(community)

    dates = []
    items = []
    items_max = []
    timeslot_numbers = []
    count = 0
    flexibilities = []

    print("Timeslots List")
    for timeslot in self.timeslots:

      print(timeslot)

      # Fill timeslots (with subitems) array
      df = pd.read_csv(self.path_steps_minutes + '/house' + str(timeslot['House']) + '/' + timeslot['Appliance'] + ".csv",
                       sep=';')  # Header=None to indicate that the first row is data and not colummn names
      df.columns = ['Date', 'Power']
      df = df[:24 * 60 * 60]  # Only the first day is important (24 hours * 60 minutes * 60 seconds)
      # df = df.fillna(0) # fills nan with 0

      # Fill dates array
      start_hour = int(str(timeslot['Start'])[11:13])
      end_hour = int(str(timeslot['End'])[11:13])
      start_date = str(timeslot['Start'])[0:10]
      start_minute = int(str(timeslot['Start'])[14:16])
      end_minute = int(str(timeslot['End'])[14:16])

      hour = start_hour
      temp_date = []
      temp_tim = []
      temp_num = []
      temp_max = []
      temp_flex = []

      while (hour <= end_hour):

        for w in range(0, n_bins_per_hour):

          if (n_bins_per_hour > 1):
            # for example, if we have bins of 30 minutes and the startMinute is 30 or higher, then we just have the second bin of that hour
            if (w != n_bins_per_hour - 1 and hour == start_hour and start_minute >= fact * (w + 1)):
              continue

            if (hour == end_hour and end_minute < fact * w):
              continue

          if (hour == start_hour and start_minute < fact * (w + 1) and start_minute >= fact * w):
            start = start_minute
          else:
            start = w * fact

          if (hour == end_hour and fact * (w + 1) >= end_minute):
            end = end_minute
          elif (hour == start_hour and w == 0):
            end = fact - 1
          else:
            end = (w + 1) * fact - 1

          duration_in_minutes = end - start + 1
          # print(str(startDate) + ' ' + str(hour).zfill(2)+ ':' + str(start).zfill(2) + ':00')
          # print(str(startDate) + ' ' + str(hour).zfill(2) + ':' + str(end).zfill(2) + ':00')
          tim = (df[(df['Date'] >= str(start_date) + ' ' + str(hour).zfill(2) + ':' + str(start).zfill(2) + ':00') & (
                  df['Date'] <= str(start_date) + ' ' + str(hour).zfill(2) + ':' + str(end).zfill(2) + ':00')][
                   'Power'].mean()) * (duration_in_minutes / 60)
          max = df[(df['Date'] >= str(start_date) + ' ' + str(hour).zfill(2) + ':' + str(start).zfill(2) + ':00') & (
                  df['Date'] <= str(start_date) + ' ' + str(hour).zfill(2) + ':' + str(end).zfill(2) + ':00')][
            'Power'].max()

          temp_date.append((hour * n_bins_per_hour) + w + 1)  # 10 am corresponds to bin 11
          temp_tim.append(tim)
          temp_max.append(max)
          temp_num.append(count)
          temp_flex.append(flexibilities_array[int(timeslot['House'])] * appliances_flexibility[timeslot['Appliance']])
          # tempHour.append([]

        hour = hour + 1

      dates.append(temp_date)
      items.append(temp_tim)
      items_max.append(temp_max)
      timeslot_numbers.append(temp_num)
      flexibilities.append(temp_flex)
      count = count + 1

    # showNetloadGraph('output/aftersecoptimization')
    # showNetloadGraphDouble('output/aftersecoptimization')

    # print(dates)
    print("Community Flexibilities:")
    print(flexibilities)
    print("Bin Capacities:")
    print(bins_capacities)
    print("Bin Maximum:")
    print(bins_maximum)
    print("Dates:")
    print(dates)
    print("Timeslots:")
    print(items)
    print("Timeslots Maximum:")
    print(items_max)
    print("Numbers:")
    print(timeslot_numbers)

    self.production_baseload = 0.85 * float(contracted_power)

    exec = Knapsack(dates, items, bins_capacities, timeslot_numbers, bins_maximum, items_max, self.production_baseload, fact, n_bins_per_hour, flexibilities)
    otimization = exec.execute_knapsack(1)

    # Remove all the consumption (all timeslots - placed and not placed ones)
    # Add the consumption of the placed timeslots (just the ones that were placed by the optimization process)
    self.placed_timeslots = otimization[1]
    self.not_placed_timeslots = otimization[2]

    # showNetloadGraph('output/minute/netload.csv')

    updt = self.create_profiles_after_strategy(self.placed_timeslots, self.timeslots, self.path_steps_minutes, self.path_steps_after_first, self.path_steps_minutes.split("/")[-1], self.path_steps_after_first.split("/")[-1], True, n_bins_per_hour, fact)
    placed_timeslots_array = updt[0]
    df_flexible = updt[1]

    # prepare dates and timemslots for the second optimization (the ones that were not placed in the first optimization)
    tmp_index = -1
    dates_second_optim = []
    items_second_optim = []
    numbers_second_optim = []
    items_max_second_optim = []
    flexibilities_second_optim = []
    count = 0
    for tim in self.not_placed_timeslots:

      if (tmp_index != int(tim.split("-")[0])):
        tmp_dates = []
        tmp_weights = []
        tmp_nums = []
        tmp_max = []
        tmp_flexibility = []

      tmp_dates.append(int(tim.split("-")[3]))
      tmp_weights.append(float(tim.split("-")[2]))
      tmp_nums.append(int(tim.split("-")[0]))
      tmp_max.append(float(tim.split("-")[6]))
      tmp_flexibility.append(tim.split("-")[8])

      if (count == int(tim.split("-")[4]) - 1):
        dates_second_optim.append(tmp_dates)
        items_second_optim.append(tmp_weights)
        numbers_second_optim.append(tmp_nums)
        items_max_second_optim.append(tmp_max)
        flexibilities_second_optim.append(tmp_flexibility)
        count = 0
      else:
        count = count + 1
      tmp_index = int(tim.split("-")[0])

    netload_second_optim = pd.read_csv(self.path_steps_after_first + '/netload.csv', sep=';')
    netload_second_optim.columns = ['Date', 'Demand', 'PV_Production', 'Wind_Production', 'Production', 'Netload']

    # Update Production after first optimization (in order to update bin capacities)
    # Remove flexible consumption from netload (update production after optimization by removing placed timeslots consumption
    bins_capacities_second_optimization = self.calculate_bin_used_capacity(bins_capacities, self.placed_timeslots, self.production_baseload, n_bins_per_hour)
    bins_maximum_second_optimization = self.get_production_max_after_first_optimization(netload_second_optim, fd, self.production_baseload, n_bins_per_hour, fact)

    print("Community Flexibilities (2nd):")
    print(flexibilities_second_optim)
    print("Bin Capacities (2nd):")
    print(bins_capacities_second_optimization)
    print("Bin Maximum (2nd):")
    print(bins_maximum_second_optimization)
    print("Dates (2nd):")
    print(dates_second_optim)
    print("Timeslots (2nd):")
    print(items_second_optim)
    print("Timeslots Maximum (2nd):")
    print(items_max_second_optim)
    print("Numbers (2nd):")
    print(numbers_second_optim)

    # showNetloadGraph('output/afteroptimization/netload.csv')

    if (len(items_second_optim) > 0 and len(dates_second_optim) > 0):
      # Second Optimization
      second_exec = Knapsack(dates_second_optim, items_second_optim, bins_capacities_second_optimization, numbers_second_optim,
                            bins_maximum_second_optimization, items_max_second_optim, self.production_baseload, fact,
                            n_bins_per_hour, flexibilities_second_optim)
      second_optim = second_exec.execute_knapsack(2)

      self.second_placed_timeslots = second_optim[1]
      self.second_not_placed_timeslots = second_optim[2]

      print("Not Placed 2nd:")
      print(self.second_not_placed_timeslots)

      self.create_profiles_after_strategy(self.second_placed_timeslots, self.timeslots,
                                                   self.path_steps_after_first, self.path_steps_after_second,
                                                   self.path_steps_after_first.split("/")[-1], self.path_steps_after_second.split("/")[-1], False, n_bins_per_hour,
                                                   fact)

      # showNetloadGraph('output/aftersecoptimization/netload.csv')

    # print(timeslots)

    # community = ConsumptionGenerator.get_community()
    # ConsumptionGenerator.show_community_graph(community, 'output/minute/house')
    # ConsumptionGenerator.show_community_graph(community, 'output/afterknapsack/house')
    # ConsumptionGenerator.show_community_graph(community, 'output/afteroptimization/house')
    # ConsumptionGenerator.show_community_graph(community, 'output/afterexchanges/house')
