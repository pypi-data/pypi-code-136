import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import procsimulator
import antgen

from procsimulator.CommunityGenerator import CommunityGenerator
from procsimulator.CommunityManagerStrategy import CommunityManagerStrategy
from procsimulator.CommunitySpecificator import CommunitySpecificator
from procsimulator.ConsumptionGenerator import ConsumptionGenerator
from procsimulator.DataFromSmile import DataFromSmile
from procsimulator.DataFromTomorrow import DataFromTomorrow
from procsimulator.Evaluation import Evaluation
from procsimulator.RenewableEnergyGenerator import RenewableEnergyGenerator

# Using 6 subplots (2 rows and 3 columns) sharing the y and x axis
'''
def show_flexibility_evolution_graph():

  path = [["/Users/nunovelosa/Desktop/flex_subplots/before/aftersecoptimization", "/Users/nunovelosa/Desktop/flex_subplots/flex25/aftersecoptimization", "/Users/nunovelosa/Desktop/flex_subplots/flex50/aftersecoptimization"], ["/Users/nunovelosa/Desktop/flex_subplots/flex75/aftersecoptimization", "/Users/nunovelosa/Desktop/flex_subplots/flex100/aftersecoptimization", "/Users/nunovelosa/Desktop/flex_subplots/flex100/aftersecoptimization"]]

  # fig, ax1 = plt.subplots()
  fig, axes = plt.subplots(nrows=2, ncols=3, constrained_layout=True, sharey=True, sharex=True)

  for p in range(2):
    for j in range(3):

      abc = pd.read_csv(path[p][j] + '/netload.csv', sep=';')
      abc.columns = ['Date', 'Demand', 'Production', 'Netload']
      abc.drop('Netload', inplace=True, axis=1)
      abc.drop('Demand', inplace=True, axis=1)
      # abc.drop('Production', inplace=True, axis=1)

      abc.set_index('Date')

      tim2 = pd.read_csv(path[p][j] + '/house0/WASHINGMACHINE.csv', sep=';')
      # tim2['Power'] = tim2['Power'] + 62.1 * 30;
      tim2 = tim2.rename(columns={"Power": "Timeslot 2 - Washing Machine - House 1"})
      tim2.set_index('Date')

      tim25 = pd.read_csv(path[p][j] + '/house5/DISHWASHER.csv', sep=';')
      # tim10['Power'] = tim10['Power'] + 62.1 * 30
      tim25 = tim25.rename(columns={"Power": "Timeslot 25 - Dishwasher - House 6"})
      tim25.set_index('Date')

      tim33 = pd.read_csv(path[p][j] + '/house6/WASHINGMACHINE.csv', sep=';')
      # tim33['Power'] = tim33['Power'] + 62.1 * 30
      tim33 = tim33.rename(columns={"Power": "Timeslot 33 - Washing Machine - House 7"})
      tim33.set_index('Date')

      df = pd.merge(pd.merge(pd.merge(abc, tim2, on='Date', how='left'), tim25, on='Date', how='left'), tim33,
                    on='Date',
                    how='left')
      df.set_index('Date')

      df['Time'] = df['Date'].map(lambda x: datetime.datetime.strptime(str(x), "%Y-%m-%d %H:%M:%S").strftime("%H:%M"))


      axes[p,j].set_xlabel('Time')
      axes[p,j].set_ylabel('Power (W)', color='red')
      plt1 = axes[p,j].plot(df['Time'], df["Timeslot 2 - Washing Machine - House 1"], color='red',
                             label='Timeslot 2 - Washing Machine - House 1')
      plt2 = axes[p,j].plot(df['Time'], df["Timeslot 25 - Dishwasher - House 6"], color='green',
                             label='Timeslot 25 - Dishwasher - House 6')
      plt3 = axes[p,j].plot(df['Time'], df["Timeslot 33 - Washing Machine - House 7"], color='orange',
                             label='Timeslot 33 - Washing Machine - House 7')
      axes[p,j].axis(ymin=-280, ymax=7500)
      # ax1.set_xticks(df['Time'])
      # ax1.tick_params(axis='y', labelcolor='red')

      # Adding Twin Axes

      if (p == 1 and j == 2):
        print("")
      else:
        ax2 = axes[p,j].twinx()

        ax2.set_ylabel('Production (W)', color='blue')
        plt4 = ax2.plot(df['Time'], df["Production"], color='blue', label='Production')

      #ax1.get_shared_y_axes().join(ax1, ax3)

      # adds space between x values because there are a lot of different values for the x-axis and not all of them can be displayed
      # ref. https://stackoverflow.com/questions/48251417/matplotlib-plots-multiple-dark-lines-on-x-axis
      spacing = 500
      visible = axes[p,j].xaxis.get_ticklabels()[::spacing]
      for label in axes[p,j].xaxis.get_ticklabels():
        if label not in visible:
          label.set_visible(False)
      visible = axes[p,j].xaxis.get_ticklines()[::spacing]
      for label in axes[p,j].xaxis.get_ticklines():
        if label not in visible:
          label.set_visible(False)

      # join labels of both axis (ax1 and ax2)
      plts = plt1 + plt2 + plt3 + plt4
      labs = [l.get_label() for l in plts]
      axes[p, j].legend(plts, labs, loc=0, prop={'size': 6})

    # ax.get_xaxis().set_visible(False)
    # Show plot


  axes[1][2].set_visible(False)


  plt.show()
  '''


def show_flexibility_evolution_graph(path):

    # fig, ax1 = plt.subplots()
    fig, axes = plt.subplots(nrows=2, ncols=2, constrained_layout=True, )

    for p in range(2):
        for j in range(2):

            abc = pd.read_csv(path[p][j] + '/netload.csv', sep=';')
            abc.columns = ['Date', 'Demand', 'Production', 'Netload']
            abc.drop('Netload', inplace=True, axis=1)
            abc.drop('Demand', inplace=True, axis=1)
            # abc.drop('Production', inplace=True, axis=1)

            abc.set_index('Date')

            tim2 = pd.read_csv(path[p][j] + '/house0/WASHINGMACHINE.csv', sep=';')
            # tim2['Power'] = tim2['Power'] + 62.1 * 30;
            tim2 = tim2.rename(columns={"Power": "Timeslot 2 - Washing Machine - House 1"})
            tim2.set_index('Date')

            tim25 = pd.read_csv(path[p][j] + '/house3/DISHWASHER.csv', sep=';')
            # tim10['Power'] = tim10['Power'] + 62.1 * 30
            tim25 = tim25.rename(columns={"Power": "Timeslot 25 - Dishwasher - House 6"})
            tim25.set_index('Date')

            tim33 = pd.read_csv(path[p][j] + '/house4/WASHINGMACHINE.csv', sep=';')
            # tim33['Power'] = tim33['Power'] + 62.1 * 30
            tim33 = tim33.rename(columns={"Power": "Timeslot 33 - Washing Machine - House 7"})
            tim33.set_index('Date')

            df = pd.merge(pd.merge(pd.merge(abc, tim2, on='Date', how='left'), tim25, on='Date', how='left'), tim33,
                          on='Date',
                          how='left')
            df.set_index('Date')

            df['Time'] = df['Date'].map(
                lambda x: datetime.datetime.strptime(str(x), "%Y-%m-%d %H:%M:%S").strftime("%H:%M"))

            axes[p, j].set_xlabel('Time')
            axes[p, j].set_ylabel('Power (W)', color='red')
            plt1 = axes[p, j].plot(df['Time'], df["Timeslot 2 - Washing Machine - House 1"], color='red',
                                   label='Timeslot 2 - Washing Machine - House 1')
            plt2 = axes[p, j].plot(df['Time'], df["Timeslot 25 - Dishwasher - House 6"], color='green',
                                   label='Timeslot 25 - Dishwasher - House 6')
            plt3 = axes[p, j].plot(df['Time'], df["Timeslot 33 - Washing Machine - House 7"], color='orange',
                                   label='Timeslot 33 - Washing Machine - House 7')
            axes[p, j].axis(ymin=-280, ymax=7500)
            # ax1.set_xticks(df['Time'])
            # ax1.tick_params(axis='y', labelcolor='red')

            # Adding Twin Axes

            ax2 = axes[p, j].twinx()

            ax2.set_ylabel('Production (W)', color='blue')
            plt4 = ax2.plot(df['Time'], df["Production"], color='blue', label='Production')

            # ax1.get_shared_y_axes().join(ax1, ax3)

            # adds space between x values because there are a lot of different values for the x-axis and not all of them can be displayed
            # ref. https://stackoverflow.com/questions/48251417/matplotlib-plots-multiple-dark-lines-on-x-axis
            spacing = 500
            visible = axes[p, j].xaxis.get_ticklabels()[::spacing]
            for label in axes[p, j].xaxis.get_ticklabels():
                if label not in visible:
                    label.set_visible(False)
            visible = axes[p, j].xaxis.get_ticklines()[::spacing]
            for label in axes[p, j].xaxis.get_ticklines():
                if label not in visible:
                    label.set_visible(False)

            # join labels of both axis (ax1 and ax2)
            plts = plt1 + plt2 + plt3 + plt4
            labs = [l.get_label() for l in plts]
            axes[p, j].legend(plts, labs, loc=2, prop={'size': 6})

        # ax.get_xaxis().set_visible(False)
        # Show plot

    axes[0, 0].set_title("A) Flexibility of 25%")
    axes[0, 1].set_title("B) Flexibility of 50%")
    axes[1, 0].set_title("C) Flexibility of 75%")
    axes[1, 1].set_title("D) Flexibility of 100%")

    plt.show()


def show_timeslots_placement_graph(path):
    abc = pd.read_csv(path + '/netload.csv', sep=';')
    abc.columns = ['Date', 'Demand', 'Production', 'Netload']
    abc.drop('Netload', inplace=True, axis=1)
    abc.drop('Demand', inplace=True, axis=1)
    # abc.drop('Production', inplace=True, axis=1)

    abc.set_index('Date')

    tim2 = pd.read_csv(path + '/house0/WASHINGMACHINE.csv', sep=';')
    # tim2['Power'] = tim2['Power'] + 62.1 * 30;
    tim2 = tim2.rename(columns={"Power": "Timeslot 2 - Washing Machine - House 1"})
    tim2.set_index('Date')

    tim25 = pd.read_csv(path + '/house3/DISHWASHER.csv', sep=';')
    # tim10['Power'] = tim10['Power'] + 62.1 * 30
    tim25 = tim25.rename(columns={"Power": "Timeslot 25 - Dishwasher - House 6"})
    tim25.set_index('Date')

    tim33 = pd.read_csv(path + '/house4/WASHINGMACHINE.csv', sep=';')
    # tim33['Power'] = tim33['Power'] + 62.1 * 30
    tim33 = tim33.rename(columns={"Power": "Timeslot 33 - Washing Machine - House 7"})
    tim33.set_index('Date')

    df = pd.merge(pd.merge(pd.merge(abc, tim2, on='Date', how='left'), tim25, on='Date', how='left'), tim33, on='Date',
                  how='left')
    df.set_index('Date')

    df['Time'] = df['Date'].map(lambda x: datetime.datetime.strptime(str(x), "%Y-%m-%d %H:%M:%S").strftime("%H:%M"))

    df.plot(x="Time", y=["Production", "Timeslot 2 - Washing Machine - House 1", "Timeslot 25 - Dishwasher - House 6",
                         "Timeslot 33 - Washing Machine - House 7"], kind="line", figsize=(10, 10))

    # plt.xlim(0, 60*24)
    # plt.ylim(0, 4500)
    plt.ylabel('Power')
    plt.xlabel('Time')

    # abc.plot(x="Date", y=["Netload"], kind="line", figsize=(10, 10))
    plt.show()


def show_timeslots_placement_graph_double(path):
    abc = pd.read_csv(path + '/netload.csv', sep=';')
    abc.columns = ['Date', 'Demand', 'Production', 'Netload']
    abc.drop('Netload', inplace=True, axis=1)
    abc.drop('Demand', inplace=True, axis=1)
    # abc.drop('Production', inplace=True, axis=1)

    abc.set_index('Date')

    tim2 = pd.read_csv(path + '/house0/WASHINGMACHINE.csv', sep=';')
    # tim2['Power'] = tim2['Power'] + 62.1 * 30;
    tim2 = tim2.rename(columns={"Power": "Timeslot 2 - Washing Machine - House 1"})
    tim2.set_index('Date')

    tim25 = pd.read_csv(path + '/house3/DISHWASHER.csv', sep=';')
    # tim10['Power'] = tim10['Power'] + 62.1 * 30
    tim25 = tim25.rename(columns={"Power": "Timeslot 25 - Dishwasher - House 6"})
    tim25.set_index('Date')

    tim33 = pd.read_csv(path + '/house4/WASHINGMACHINE.csv', sep=';')
    # tim33['Power'] = tim33['Power'] + 62.1 * 30
    tim33 = tim33.rename(columns={"Power": "Timeslot 33 - Washing Machine - House 7"})
    tim33.set_index('Date')

    df = pd.merge(pd.merge(pd.merge(abc, tim2, on='Date', how='left'), tim25, on='Date', how='left'), tim33, on='Date',
                  how='left')
    df.set_index('Date')

    df['Time'] = df['Date'].map(lambda x: datetime.datetime.strptime(str(x), "%Y-%m-%d %H:%M:%S").strftime("%H:%M"))

    fig, ax1 = plt.subplots()

    ax1.set_xlabel('Time')
    ax1.set_ylabel('Power (W)', color='red')
    plt1 = ax1.plot(df['Time'], df["Timeslot 2 - Washing Machine - House 1"], color='red',
                    label='Timeslot 2 - Washing Machine - House 1')
    plt2 = ax1.plot(df['Time'], df["Timeslot 25 - Dishwasher - House 6"], color='green',
                    label='Timeslot 25 - Dishwasher - House 6')
    plt3 = ax1.plot(df['Time'], df["Timeslot 33 - Washing Machine - House 7"], color='orange',
                    label='Timeslot 33 - Washing Machine - House 7')
    ax1.axis(ymin=-280, ymax=6000)
    # ax1.set_xticks(df['Time'])
    # ax1.tick_params(axis='y', labelcolor='red')

    # Adding Twin Axes

    ax2 = ax1.twinx()

    ax2.set_ylabel('Production (W)', color='blue')
    plt4 = ax2.plot(df['Time'], df["Production"], color='blue', label='Production')

    # adds space between x values because there are a lot of different values for the x-axis and not all of them can be displayed
    # ref. https://stackoverflow.com/questions/48251417/matplotlib-plots-multiple-dark-lines-on-x-axis
    spacing = 200
    visible = ax1.xaxis.get_ticklabels()[::spacing]
    for label in ax1.xaxis.get_ticklabels():
        if label not in visible:
            label.set_visible(False)
    visible = ax1.xaxis.get_ticklines()[::spacing]
    for label in ax1.xaxis.get_ticklines():
        if label not in visible:
            label.set_visible(False)

    # ax.get_xaxis().set_visible(False)
    # Show plot

    # join labels of both axis (ax1 and ax2)
    plts = plt1 + plt2 + plt3 + plt4
    labs = [l.get_label() for l in plts]
    ax1.legend(plts, labs, loc=0)

    plt.show()


def create_table_figure(df):
    # make this example reproducible
    np.random.seed(0)

    # define figure and axes
    fig, ax = plt.subplots()

    # hide the axes
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')

    # create data

    # create table
    table = ax.table(cellText=df.values, colLabels=df.columns, loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)

    # display table
    fig.tight_layout()
    plt.show()



def show_evolution_graph(df_flexible, path_steps_minutes, path_steps_after_first, path_steps_after_second):
  before_opt = pd.read_csv(path_steps_minutes + '/netload.csv', sep=';')
  before_opt.columns = ['Date', 'Demand', 'Production', 'Netload']
  before_opt.drop('Netload', inplace=True, axis=1)
  before_opt.set_index('Date')

  first_opt = pd.read_csv(path_steps_after_first + '/netload.csv', sep=';')
  first_opt.columns = ['Date', 'Demand', 'Production', 'Netload']
  first_opt.drop('Netload', inplace=True, axis=1)
  first_opt.set_index('Date')

  second_opt = pd.read_csv(path_steps_after_second + '/netload.csv', sep=';')
  second_opt.columns = ['Date', 'Demand', 'Production', 'Netload']
  second_opt.drop('Netload', inplace=True, axis=1)
  second_opt.set_index('Date')

  df_flexible.drop('Netload', inplace=True, axis=1)

  fig, axes = plt.subplots(nrows=2, ncols=2)

  before_opt.plot(ax=axes[0, 0])
  df_flexible.plot(ax=axes[0, 1])
  first_opt.plot(ax=axes[1, 0])
  second_opt.plot(ax=axes[1, 1])

  axes[0, 0].set_title("A) Without optimization")
  axes[0, 1].set_title("B) Not Flexible (Without opt)")
  axes[1, 0].set_title("C) First Optimization")
  axes[1, 1].set_title("D) Second Optimization")
  plt.show()



def calculate_phase_metrics(phase, ev, placed_timeslots, not_placed_timeslots, all_timeslots):

  print(phase)
  print("Average Power used from Grid: " + str(ev.get_average_power_used_from_grid()))
  print("Average Power not used from PV: " + str(ev.get_average_power_not_used_from_pv()))
  print("Average Power used from PV: " + str(ev.get_average_power_used_from_pv()))
  print("Energy used from Grid: " + str(ev.get_energy_used_from_grid()))
  print("Energy not used from PV: " + str(ev.get_energy_not_used_from_pv()))
  print("Energy used from PV: " + str(ev.get_energy_used_from_pv()))
  print("Maximum Grid Peak: " + str(ev.get_maximum_grid_peak()))
  print("Minimum Grid Peak: " + str(ev.get_minimum_grid_peak()))
  print("Maximum Magnitude Peak: " + str(ev.get_maximum_magnitude_peak()))
  print("Minimum Magnitude Peak: " + str(ev.get_minimum_magnitude_peak()))
  print("Number of Peaks: " + str(ev.get_peaks_number()))
  print("Self Sufficiency (%): " + str(ev.get_self_sufficiency()))
  print("Self Consumption (%): " + str(ev.get_self_consumption()))

  if (phase == "Before Optimization"):
    print("Placed (flexible) Timeslots: " + str(len(all_timeslots)))
    print("Not Placed (flexible) Timeslots: 0")
    print("kWh of placed (flexible) timeslots: " + str(
      float(ev.get_energy_of_timeslots_list(placed_timeslots)) + float(ev.get_energy_of_timeslots_list(not_placed_timeslots))))
    print("kWh of not placed (flexible) timeslots: 0")
  else:
    print("Placed (flexible) Timeslots: " + str(ev.get_timeslots_list_number(placed_timeslots)))
    print("Not Placed (flexible) Timeslots: " + str(ev.get_timeslots_list_number(not_placed_timeslots)))
    print("Energy of placed (flexible) timeslots: " + str(ev.get_energy_of_timeslots_list(placed_timeslots)))
    print("Energy of not placed (flexible) timeslots: " + str(ev.get_energy_of_timeslots_list(not_placed_timeslots)))


def create_dataframe(before, first, second, placed_timeslots, not_placed_timeslots, second_placed_timeslots, second_not_placed_timeslots, all_timeslots):

  data = [['Average Power used from Grid',
           str(before.get_average_power_used_from_grid()) + " kW",
           str(first.get_average_power_used_from_grid()) + " kW",
           str(second.get_average_power_used_from_grid()) + " kW"],
          ['Average Power not used from PV',
           str(before.get_average_power_not_used_from_pv()) + " kW",
           str(first.get_average_power_not_used_from_pv()) + " kW",
           str(second.get_average_power_not_used_from_pv()) + " kW"],
          ['Average Power used from PV',
           str(before.get_average_power_used_from_pv()) + " kW",
           str(first.get_average_power_used_from_pv()) + " kW",
           str(second.get_average_power_used_from_pv()) + " kW"],
          ['Energy used from Grid',
           str(before.get_energy_used_from_grid()) + " kWh",
           str(first.get_energy_used_from_grid()) + " kWh",
           str(second.get_energy_used_from_grid()) + " kWh"],
          ['Energy not used from PV',
           str(before.get_energy_not_used_from_pv()) + " kWh",
           str(first.get_energy_not_used_from_pv()) + " kWh",
           str(second.get_energy_not_used_from_pv()) + " kWh"],
          ['Energy used from PV',
           str(before.get_energy_used_from_pv()) + " kWh",
           str(first.get_energy_used_from_pv()) + " kWh",
           str(second.get_energy_used_from_pv()) + " kWh"],
          ['Maximum Grid Peak',
           str(before.get_maximum_grid_peak()) + " kW",
           str(first.get_maximum_grid_peak()) + " kW",
           str(second.get_maximum_grid_peak()) + " kW"],
          ['Minimum Grid Peak',
           str(before.get_minimum_grid_peak()) + " kW",
           str(first.get_minimum_grid_peak()) + " kW",
           str(second.get_minimum_grid_peak()) + " kW"],
          ['Maximum Magnitude Peak',
           str(before.get_maximum_magnitude_peak()) + " kW",
           str(first.get_maximum_magnitude_peak()) + " kW",
           str(second.get_maximum_magnitude_peak()) + " kW"],
          ['Minimum Magnitude Peak',
           str(before.get_minimum_magnitude_peak()) + " kW",
           str(first.get_minimum_magnitude_peak()) + " kW",
           str(second.get_minimum_magnitude_peak()) + " kW"],
          ['Number of Peaks',
           before.get_peaks_number(),
           first.get_peaks_number(),
           second.get_peaks_number()],
          ['Self Sufficiency',
           before.get_self_sufficiency(),
           first.get_self_sufficiency(),
           second.get_self_sufficiency()],
          ['Self Consumption',
           before.get_self_consumption(),
           first.get_self_consumption(),
           second.get_self_consumption()],
          ['Placed (flexible) Timeslots',
           len(all_timeslots),
           first.get_timeslots_list_number(placed_timeslots),
           second.get_timeslots_list_number(second_placed_timeslots)],
          ['Unplaced (flexible) Timeslots',
           '0',
           first.get_timeslots_list_number(not_placed_timeslots),
           second.get_timeslots_list_number(second_not_placed_timeslots)],
          ['Energy of placed (flexible) timeslots',
           str(float(before.get_energy_of_timeslots_list(placed_timeslots)) + float(
             before.get_energy_of_timeslots_list(not_placed_timeslots))) + " kWh",
           str(first.get_energy_of_timeslots_list(placed_timeslots)) + " kWh",
           str(second.get_energy_of_timeslots_list(second_placed_timeslots)) + " kWh"],
          ['Energy of unplaced (flexible) timeslots',
           '0 kWh',
           str(first.get_energy_of_timeslots_list(not_placed_timeslots)) + " kWh",
           str(second.get_energy_of_timeslots_list(second_not_placed_timeslots)) + " kWh"]]

  # Create the pandas DataFrame
  df = pd.DataFrame(data, columns=['', 'Before Optimization', 'After 1st Optimization', 'After 2nd Optimization'])

  create_table_figure(df)



def calculate_metrics(before, first, second, placed_timeslots, not_placed_timeslots, second_placed_timeslots, second_not_placed_timeslots, timeslots):

  print("Metrics")
  calculate_phase_metrics("Before Optimization", before, placed_timeslots, not_placed_timeslots, timeslots)
  calculate_phase_metrics("After 1st Optimization", first, placed_timeslots, not_placed_timeslots, timeslots)
  calculate_phase_metrics("After 2nd Optimization", second, second_placed_timeslots, second_not_placed_timeslots, timeslots)
  create_dataframe(before, first, second, placed_timeslots, not_placed_timeslots, second_placed_timeslots, second_not_placed_timeslots, timeslots)




if __name__ == '__main__':

    # Defining the dataset paths
    path_steps_seconds = "C:/Users/Nuno.Velosa.CORP/OneDrive - Unipartner IT Services, S.A/Desktop/procsim"
    path_steps_minutes = "output/minute"
    path_steps_after_first = "output/afteroptimization"
    path_steps_after_second = "output/aftersecoptimization"

    # Defining the simulator classes that will be used
    cs = CommunitySpecificator("data.json")
    cg = ConsumptionGenerator("data.json", path_steps_seconds, path_steps_minutes)
    pv_dat = DataFromSmile("https://ems.prsma.com/solcast/public/Fazendinha_solcast-radiation-historical_30min.csv")
    wind_dat = DataFromTomorrow(
        "https://api.tomorrow.io/v4/timelines?location=-73.98529171943665,40.75872069597532&fields=pressureSurfaceLevel,pressureSeaLevel,precipitationIntensity,precipitationType,windSpeed,windGust,windDirection,temperature,temperatureApparent,cloudCover,cloudBase,cloudCeiling,weatherCode&timesteps=1h&units=metric&apikey=Yckmp3vREbJqyprWGGiTOC1pVaAYO0ZT")
    reg = RenewableEnergyGenerator(cg, pv_dat, wind_dat, cg.path_steps_minutes)
    cmg = CommunityGenerator(cg.path_steps_minutes)
    cm = CommunityManagerStrategy(cg, cg.path_steps_minutes, path_steps_after_first, path_steps_after_second)

    # Creating the house and user files as well as the consumption and production profiles
    #cs.execute()
    #cg.execute("1", "houses", "C:/Users/Nuno.Velosa.CORP/OneDrive - Unipartner IT Services, S.A/Desktop/antgen/antgen", True, False)
    cg.execute("1", "houses", True, False)
    reg.execute()
    cmg.execute()

    # Getting the community contracted power
    community = cg.get_community()
    print("Contracted Power: " + str(cg.calculate_contracted_power(community)))
    cm.execute()


    # Getting the consumption profiles before the optimization
    before_opt = pd.read_csv(path_steps_minutes + '/netload.csv', sep=';')
    before_opt.columns = ['Date', 'Demand', 'PV_Production', 'Wind_Production', 'Production', 'Netload']
    before_opt['Date'] = pd.to_datetime(before_opt['Date'])
    before_opt.set_index('Date')

    # Getting the consumption profiles after the 1st step of the optimization
    first_opt = pd.read_csv(path_steps_after_first + '/netload.csv', sep=';')
    first_opt.columns = ['Date', 'Demand', 'PV_Production', 'Wind_Production', 'Production', 'Netload']
    first_opt['Date'] = pd.to_datetime(first_opt['Date'])
    first_opt.set_index('Date')

    # Getting the consumption profiles after the 2nd step of the optimization
    second_opt = pd.read_csv(path_steps_after_second + '/netload.csv', sep=';')
    second_opt.columns = ['Date', 'Demand', 'PV_Production', 'Wind_Production', 'Production', 'Netload']
    second_opt['Date'] = pd.to_datetime(second_opt['Date'])
    second_opt.set_index('Date')


    # Defining evaluation for the three different phases (dataframes): before the optimization, after the 1st step and after the 2nd step
    ev_before = Evaluation(reg, before_opt, cm.production_baseload)
    ev_first = Evaluation(reg, first_opt, cm.production_baseload)
    ev_second = Evaluation(reg, second_opt, cm.production_baseload)

    # Graphically show some timeslots placement using different flexibilities with just 1 y-axis
    show_timeslots_placement_graph(path_steps_minutes)
    show_timeslots_placement_graph(path_steps_after_second)

    # Graphically show some timeslots placement using different flexibilities with 2 y-axis
    show_timeslots_placement_graph_double(path_steps_minutes)
    show_timeslots_placement_graph_double(path_steps_after_second)

    # Graphically show flexibility evolution graph (the impact of the optimization when considering 4 flexibility cases: 25%, 50%, 75% and 100%
    # path = [[ "/Users/nunovelosa/Desktop/flex_subplots/flex25/aftersecoptimization", "/Users/nunovelosa/Desktop/flex_subplots/flex50/aftersecoptimization"], ["/Users/nunovelosa/Desktop/flex_subplots/flex75/aftersecoptimization", "/Users/nunovelosa/Desktop/flex_subplots/flex100/aftersecoptimization"]]
    path = [[path_steps_minutes, path_steps_after_first],[path_steps_after_second,path_steps_after_second]]
    show_flexibility_evolution_graph(path)

    # Calculate the metrics for the three phases (dataframes)
    calculate_metrics(ev_before, ev_first, ev_second, cm.placed_timeslots, cm.not_placed_timeslots, cm.second_placed_timeslots, cm.second_not_placed_timeslots, cm.timeslots)
