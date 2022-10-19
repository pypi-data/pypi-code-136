# -*- coding: utf-8 -*-

from datetime import (
    datetime,
    timedelta
)
import logging
import logging.config
from numbers import Number
from operator import index
import numpy as np
import os
import pandas as pd
from pandas import DataFrame
from pandas.io.sql import SQLTable
import s3fs
import scipy.stats as sct
import shutil
import sys
from typing import Union
import xlsxwriter

from dashboard.data_processing import Bluesky_weather_fucntions_v01 as blu
from dashboard.data_processing import BV_pp_deg as batt
from dashboard.data_processing import Correct_POI_data_v01 as poi
from dashboard.data_processing import Correct_Meter_data_v08_smartercheck as meter_correct
from dashboard.data_processing import Performance_Guarantees_v01 as perf
from dashboard.data_processing import Plant_Availability_v16_bbsc as plant_ava
from dashboard.data_processing import Rate_Structure_Python_with_DST_v07 as rates
from dashboard.data_processing import snow_loss_functions_v3 as snow
from dashboard.data_processing import Table_by_Rate_Schedule_v01 as rate_table
from dashboard.data_processing import weather_adjusted_functions_v03 as weather

from dashboard.utils.dashboard_utils import func_timer
from dashboard.utils import df_tools as df_tools
from dashboard.utils import project_neighbors as neighbs

# Python 2 compatibility
if sys.version_info.major == 3:
    unicode = str

# suppress warnings about "A value is trying to be set on a copy of a slice from a DataFrame."
pd.options.mode.chained_assignment = None

# Create logger
logger = logging.getLogger(__name__)


class Project(object):
    """An object representing a solar site (project). This should never be initialized\
        outside of a `DashboardSession` instance, which coordinates the processing of `proj_init_dict`.

    Args:
        proj_init_dict (dict): A dictionary of metadata to pass to the project for initialization.
    """
    
    # Initialize class variables
    Gstc = 1000
    """W/m2 for POA irradiance ratio"""

    @func_timer
    def __init__(self, proj_init_dict):

        # Processed flag that we'll turn to true once we process the data
        self.processed = False
        """Flag to denote if the project has been processed."""

        # List to note neighbor sensors once we've added them
        self.neighbor_sensors = set()
        """A list of neighbor sensors that are available to the project. These are set with the `Get_Sensor` keyword on the `data` tab of the config file"""
        # self.neighbor_sensors_needed = set()
        
        # Project properties passed from DashboardSession
        self.project_name = proj_init_dict['project_name']
        """The string representation of the `Project` name. This should match the 'Project' field in `df_keys`."""
        self.df_proj_keys = proj_init_dict['df_proj_keys']
        """The subset of `df_keys` corresponding to the `Project` instance."""
        self.dashboard_dir = proj_init_dict['dashboard_dir']
        self.data_cutoff_date = proj_init_dict['data_cutoff_date']
        self.data_source = proj_init_dict['data_source']
        self.Battery_AC_site = proj_init_dict['Battery_AC_site']
        """Flag denoting a project with AC battery storage"""
        self.Battery_DC_site = proj_init_dict['Battery_DC_site']
        """Flag denoting a project with DC battery storage"""
        self.Tracker_site = proj_init_dict['Tracker_site']
        """Flag denoting a project with tracker-type racking"""
        self.raw_snow_df = proj_init_dict['raw_snow_df']
        self.neighbor_list = proj_init_dict['neighbor_list']
        """List of neighbors that meet the criteria for data substitution.  
            <h2>Default Criteria:</h2>
            * Distance <= 10 miles  
            * Fixed projects:
                * Same module tilt  
                * Same racking OEM
            * Tracker projects:
                * GCR &plusmn;0.05
        """

        # Get information for the project from DF keys
        # `self.df_proj_keys` is the appropriate row from `df_keys` as a dictionary
        self.project_directory = self.df_proj_keys['Folder']
        """Folder in the Dashboard file structure where the project data lives"""
        self.lat = self.df_proj_keys['GPS_Lat']
        """Project latitude"""
        self.lon = self.df_proj_keys['GPS_Long']
        """Project longitude"""
        self.MWAC = self.df_proj_keys['MWAC']
        """Nameplate AC rating of the project"""

        # Build filename for config file
        config_filename = self.project_name + r'_Plant_Config_MACRO.xlsm'
        self.config_filepath = os.path.join(self.dashboard_dir,
                                        self.project_directory,
                                        self.project_name,
                                       'Plant_Config_File',
                                        config_filename)
        """Filepath for the `Project`'s config file"""

        if not os.path.isfile(self.config_filepath):
            raise RuntimeError("*** No config file found for {}, skipping project. Check that filepath exists: {}".format(self.project_name, self.config_filepath))        

        # Get last update time for config file - we will use this to check if config file has been updated
        self.last_update_config = 0.0
        """Timestamp of the last update to the config file. This is used to check if it needs to be re-loaded from the filesystem"""

        # Find Powertrack file
        self.data_AE_dir = os.path.join(self.dashboard_dir,
                                        self.project_directory,
                                        self.project_name,
                                        'Powertrack_data')
        self.data_AE_all_files = [f for f in os.listdir(self.data_AE_dir) if os.path.isfile(os.path.join(self.data_AE_dir, f))]
        data_AE = [s for s in self.data_AE_all_files if self.data_source in s]

        # TODO: check on error handling here if we can't find the Powertrack file
        if len(data_AE) == 0:
            raise RuntimeError("*** No Powertrack file found for {}, skipping project".format(self.project_name))

        # Build filename for Powertrack file
        self.powertrack_filepath = os.path.join(self.dashboard_dir, self.project_directory, self.project_name, 'Powertrack_data', data_AE[0])
        """Filepath for the `Project`'s Powertrack file"""

        # Initialize powertrack update time, will use it the same as config
        self.last_update_powertrack = 0.0
        """Timestamp of the last update to the powertrack file. This is used to check if it needs to be re-loaded from the filesystem."""
        
        # Initialize other instance variables
        self.config_sheets = None
        """Dictionary of `DataFrame`s for each sheet in the config file"""
        self.colnames_ccr = None
        """CCR standard column names for data fields"""
        self.colnames_das = None
        """Original column names from the DAS"""
        self.df = None
        """Main source of hourly data"""
        self.df_Pvsyst = None
        """Projected hourly values for the year, aka '8760'"""
        self.df_sensor_ON = None
        """Boolean table to specify if a meter or sensor should be used or ignored"""

        # Finish initializing project
        # FIXME: update error handling when can't find config file
        self._parse_config_file()
        self._find_neighbor_sensors()
        self.__get_project_parameters()
        self.__read_degradation_profile()
       

    @func_timer
    def _parse_config_file(self):
        """Reads data from config file & parses each sheet into a dataframe
        """
        # Read variables from Plant Configuration File
        # `self.config_sheets` will store all the sheets from the config file as a dictionary
        if self.last_update_config == os.path.getmtime(self.config_filepath):
            return
        try:
            print("Loading config file for {}".format(self.project_name))
            self.config_sheets = pd.read_excel(self.config_filepath, sheet_name=None)
        except IOError:
            error_msg = "Can't find config file for {}. Please check that the following path exists: {}".format(self.project_name, self.config_filepath)
            print(error_msg)
            logger.error(error_msg)

            raise Exception()
        
        # Set all sheets of the config file to instance variables

        ################ `data` tab ###############
        self.df_config = self.config_sheets['data'].fillna(0)

        # Create dictionary of config parameters
        df_config_dict = self.df_config.to_dict('list')
        self.config_dict = dict(zip(df_config_dict['Name'], df_config_dict['Value']))

        ############# `Column_ID` tab #############
        # `colnames_ccr` is a list of the CCR column names
        # `colnames_das` is a list of the original column names from the project's DAS
        col_id_sheet = self.config_sheets['Column_ID']

        # Python 2 compatibility - old versions of Pandas would read the first column as the index, with new versions we have to set it explicitly
        if col_id_sheet.index.inferred_type == 'integer':
            col_id_sheet.set_index(col_id_sheet.columns[0], inplace=True)

        column_ref = col_id_sheet.iloc[2,:]
        self.colnames_ccr = column_ref.index.tolist()
        self.colnames_das = column_ref.values.tolist()
        self.non_error_cols = [col for col in self.colnames_ccr if 'ERROR' not in col]

        ########## `Sensor_Offline` tab ###########
        self.sensor_OFF = self.config_sheets['Sensor_Offline'].reset_index()

        ############## `Unit_Tab` tab #############
        self.Convert_Units = self.config_sheets['Unit_Tab']

        ################ `8760` tab ###############
        self.df_Pvsyst = self.config_sheets['8760'].fillna(0)
        self.df_Pvsyst.loc[self.df_Pvsyst['Year 0 Actual Production (kWh)'] < 0, 'Year 0 Actual Production (kWh)'] = 0

        # Create date index from date column
        try:
            self.df_Pvsyst.loc[:, 'date'] = pd.to_datetime(self.df_Pvsyst.loc[:, 'date'])
            self.df_Pvsyst.set_index('date', inplace=True)
        except KeyError:
            pass

        # Get capacity & neighbor sensor params
        self.OFF_PEAK = self.config_dict['OFF_PEAK']
        self.CAPACITY_ON_PEAK_SUMMER = self.config_dict['CAPACITY_ON_PEAK_SUMMER']
        self.CAPACITY_ON_PEAK_NON_SUMMER = self.config_dict['CAPACITY_ON_PEAK_NON_SUMMER']
        self.Get_Sensor = self.df_config.loc[(self.df_config['Name'].str.lower() == 'get_sensor'), :]
        
        # Update last config update timestamp
        self.last_update_config = os.path.getmtime(self.config_filepath)

    
    @func_timer
    def _find_neighbor_sensors(self):
        # TODO: check here if project already exists in DashboardSession & load it if not
        # Loop through all neighbor sensors listed in the config file
        for neighbor_name in self.Get_Sensor['Source'].unique().tolist():
            self.neighbor_sensors.add(neighbor_name)
            
            
    @func_timer
    def __get_project_parameters(self):
        # Check if these base parameters are present in df_keys
        # If not we'll log the project & pull the parameters from the config file
        params = [self.df_proj_keys['MWDC'], 
                  self.df_proj_keys['Delta_Tcnd'],
                  self.df_proj_keys['Temp_Coeff_Pmax'],
                  self.df_proj_keys['a_module'],
                  self.df_proj_keys['b_module']
                  ]
        # Check if any parameters are not present
        if not np.isnan(params).any():
            self.Pstc_KW, self.Delta_Tcnd, self.Temp_Coeff_Pmax, self.a_module, self.b_module = params
            self.Pstc_KW = self.Pstc_KW * 1000  # MW to kW
            self.Temp_Coeff_Pmax = self.Temp_Coeff_Pmax / 100.0  # % to decimal
        # Pull parameters from config file if any are not present
        else:
            print("*** df_keys INFO NOT COMPLETE for {} ***".format(self.project_name))
            logging.warn("df_keys INFO NOT COMPLETE for {} ***".format(self.project_name))
            self.Pstc_KW = self.config_dict['Pstc_KW']
            self.Delta_Tcnd = self.config_dict['Delta_Tcnd']
            self.Temp_Coeff_Pmax = self.config_dict['Temp_Coeff_Pmax']
            self.a_module = self.config_dict['a_module']
            self.b_module = self.config_dict['b_module']
        
        # Check if Placed In Service date exits
        if self.df_proj_keys['PIS'] == self.df_proj_keys['PIS']:
            self.PIS_date = self.df_proj_keys['PIS']
        else:
            self.PIS_date = datetime(2050, 1, 1)  # fake date
            # NOTE: warn on this - it's needed for degradation profile
            print('*** PIS Date Load failed for {} ***'.format(self.project_name))
            logging.warn('*** PIS Date Load failed for {} ***'.format(self.project_name))

        # Check if Final Completion date exists
        if self.df_proj_keys['FC'] == self.df_proj_keys['FC']:
            self.SC_Date = self.df_proj_keys['FC']
        else:
            self.SC_Date = datetime(2050, 1, 1)  # fake date
            # QUESTION: is FC Date important? Do we need to fill it out? Do we need to warn about it?
            # NOTE: Don't need to log this - comment out for now in case CCR starts to develop projects
            print('*** FC Date Load failed for {} ***'.format(self.project_name))
            logging.warn('*** FC Date Load failed for {} ***'.format(self.project_name))
        
        # Get `clipping_KW` based on max value on the 8760
        self.clipping_KW = self.df_Pvsyst['Year 0 Actual Production (kWh)'].max()

        # Calculate ASTM linear regression coef to calculate Weather adjusted values
        self.var_astm = ['Year 0 Actual Production (kWh)', 'POA (W/m2)', 'Wind Velocity (m/s)', 'Ambient Temperature']
        self.df_coef, self.df_coef_RC = weather.generate_linear_coeff_table_v3(self.df_Pvsyst, self.var_astm, self.clipping_KW)

        # Find empty months
        if not self.df_coef.loc[:, self.df_coef.sum() == 0].empty:
            aux = self.df_coef.loc[:, self.df_coef.sum() == 0]
            # Find typical values to replace bad ones
            avg = self.df_coef.loc[:, self.df_coef.sum() != 0].mean(axis=1)

            # Edit months that failed
            for col in aux.columns:
                self.df_coef.loc[:, col] = avg
            print ("Edited ASTM test - no data for months: " + ",".join(aux.columns))
            logging.warn("Edited ASTM test - no data for months: " + ",".join(aux.columns))


    @func_timer
    def __read_degradation_profile(self):
        # Create empty dataframe to store profile
        self.Deg = pd.DataFrame(index=range(41))

        # Initialize `Capacity` column to zero & set year 1 to 100%
        self.Deg['Capacity'] = 0.0
        self.Deg['Capacity'][0] = 1.0

        # Find degradation rows
        Deg_Read = [s for s in self.df_config['Name'] if "-ENG- -DEG- AC Energy De-Rate Year" in s]
        
        # Extract year from string
        year_str = [x[35:37] for x in Deg_Read]
        year_ = [int(y) for y in year_str]

        # Add degradation for the corresponding year
        for i in range(len(Deg_Read)):
            self.Deg['Capacity'][year_[i]] = self.df_config[self.df_config['Name'] == Deg_Read[i]]['Value'].values[0]

        # find if any elements are 0. Any matches trigger else condition
        # QUESTION: Do we want to exit the run if the degradation profile fails??
        # NOTE: warn but still run
        if np.any(self.Deg['Capacity'] == 0):
            # Set all degradation values to 100%
            self.Deg['Capacity'] = 1
            print('*** Degradation profile failed for {} ***'.format(self.project_name))

        # Fix year index to properly to 0.0, 0.5, 1.5 index steps per Jeff Webber spreadsheet
        self.Deg.set_index(np.append([0], np.arange(0.5, 40.5, 1)), inplace=True)


    @func_timer
    def load_production_data(self):
        """Loads production data from the `Project`'s Powertrack file.  
        If file has already been loaded, it will check `last_update_powertrack` against the
        last updated timestamp for the file on the file system to determine if it needs
        to re-load the data from the file system or use the previously loaded data in the `Project` object."""

        # Read Powertrack data
        # If the powertrack file has been updated since we last loaded production
        # we'll read the data from Excel & store a copy in df_powertrack
        # If it hasn't been updated we'll just use the powertrack copy we loaded previously
        def load_from_source(filepath):
            print('Loading Powertrack data for {}'.format(self.project_name))
            self.df = pd.read_excel(filepath, sheet_name='Sheet1', skiprows=0, index_col=0)
            self.last_update_powertrack = os.path.getmtime(self.powertrack_filepath)
            self.df_powertrack = self.df.copy()
        
        last_update_powertrack_file = os.path.getmtime(self.powertrack_filepath)
        
        if self.last_update_powertrack != last_update_powertrack_file:
            load_from_source(self.powertrack_filepath)
        else:
            # If we try to load from `df_powertrack` and it doesn't exist we'll need to load from source
            try:
                self.df = self.df_powertrack.copy()
                print('Using previously loaded Powertrack file for {}'.format(self.project_name))
            except AttributeError:
                load_from_source(self.powertrack_filepath)
            
        # Curtail date to max of `data_cutoff_date`
        self.df = self.df.loc[self.df.index < self.data_cutoff_date, :]

        # Apply CCR column names to df
        if len(self.df.columns) < len(self.colnames_ccr):
            list1 = self.df.columns.tolist()
            list2 = self.colnames_das
            list1_upper = [x.upper() for x in list1]
            list2_upper = [x.upper() for x in list2]
            ind_list_position = [i for i, item in enumerate(list2_upper) if item in list1_upper]
            self.colnames_ccr = [self.colnames_ccr[i] for i in ind_list_position]
            self.df.columns = self.colnames_ccr
        else:
            self.df.columns = self.colnames_ccr

        # Remove error columns
        self.df = self.df[self.non_error_cols]

        # Find native sensors, used to find DAS_ON instead of all sensors.
        # Avoids using Get_Sensor data from another site
        val = ['Meter_kw_', 'POA', 'GHI', 'Wind_speed', 'Inv_kw_', 'Inv_kwnet', 'Tmod', 'Tamb']
        self.pos_Native = [s for s in self.df.columns if any([x in s for x in val])]

        # Copy columns if necessary - most commonly used to map inverters to meters
        # at sites where we don't have standalone meters & use the inverters as a proxy
        Copy_Sensor = self.df_config.loc[(self.df_config['Name'].str.lower() == 'copy_sensor'), :]
        Copy_from = Copy_Sensor['Value'].values.tolist()
        Copy_to = Copy_Sensor['Source'].values.tolist()
        for _from, _to in zip(Copy_from, Copy_to):
            self.df[_to] = self.df[_from]
            self.colnames_ccr = self.colnames_ccr + [_to]

        # Get production year
        self.year = int(self.df.index.year[0])

        # Convert production data to hourly values
        self.df = self.df.resample('h').mean()

        # Initialize & populate sensor_ON dataframe
        self.df_sensor_ON = pd.DataFrame(columns=self.df.columns.tolist(), index=self.df.index).fillna(True).astype(object)


    def get_columns(project):
        """Prints out CCR column names with their location in the `Project`'s Powertrack file and a map to its DAS column name.

        Args:
            project (Project): The `Project` where the columns are pulled from.
        """
        intake = project.pos_Meter + project.pos_Meter_Cum + project.pos_Inv + project.pos_Inv_cum
        columns_df=DataFrame(data={'Column':[],'Position':[],'OG Name':[]})
        for x in intake: #lists out the column names and index for the lists. 
            column=x
            position=xlsxwriter.utility.xl_col_to_name(project.colnames_ccr.index(x)+1)
            og=project.colnames_das[project.colnames_ccr.index(x)]
            temp=DataFrame(data={'Column':[column],'Position':[position],'OG Name':[og]})
            columns_df=columns_df.append(temp)
        print('\n')
        print('Column locations for {}:'.format(project.project_name))
        print(columns_df[['Column','Position','OG Name']])
        print('\n')


    def find_nearby_projects(self, dist=10, print_data=True, include_retired=False, df=None):
        """Creates a list of sites within a certain distance of the reference site.

        Args:
            dist (int, optional): Number of miles to search around the reference site.
                Defaults to 10.
            df (Dataframe, optional): Dataframe containing sitenames & lat/longs.
                Defaults to `df_keys` if no `df` supplied.

        Returns:
            DataFrame: Contains information about all sites within the specified\
            distance from the reference site.
        """
        ns = neighbs.find_nearby_projects(self.project_name, dist, print_data, include_retired, df)
        return ns
    

    def find_nearby_similar_projects(self, dist=10, print_data=True, include_retired=False, df=None):
        """Creates a list of sites within a certain distance of the reference site
        that share similar racking properties. 
    
        Args:
            dist (int, optional): Number of miles to search around the reference site.
                Defaults to 10.
            df (Dataframe, optional): Dataframe containing sitenames & lat/longs.
                Defaults to `df_keys` if no `df` supplied.
        Returns:
            DataFrame: Contains information about all sites within a certain distance\
            of the reference site that share similar racking properties.
        """
        nss = neighbs.find_nearby_similar_projects(self.project_name, dist, print_data, include_retired, df=None)
        return nss
        
    
    def get_sensors(project):
        """Prints out the location of POA & weather sensors in a `Project`'s Powertrack file and a map to its DAS column name.

        Args:
            project (Project): The `Project` where the columns are pulled from.
        """
        columns_df=DataFrame(data={'Column':[],'Position':[],'OG Name':[]})
        for x in project.pos_POA: #lists out the column names and index for the lists.
            if len(x) < 7:
                column=x
                position=xlsxwriter.utility.xl_col_to_name(project.colnames_ccr.index(x)+1)
                og=project.colnames_das[project.colnames_ccr.index(x)]
                temp=DataFrame(data={'Column':[column],'Position':[position],'OG Name':[og]})
                columns_df=columns_df.append(temp)
        for x in project.pos_Temperature: #lists out the column names and index for the lists.
            if len(x) < 7:
                column=x
                position=xlsxwriter.utility.xl_col_to_name(project.colnames_ccr.index(x)+1)
                og=project.colnames_das[project.colnames_ccr.index(x)]
                temp=DataFrame(data={'Column':[column],'Position':[position],'OG Name':[og]})
                columns_df=columns_df.append(temp)
        for x in project.pos_Wind: #lists out the column names and index for the lists.
            if len(x) < 13:
                column=x
                position=xlsxwriter.utility.xl_col_to_name(project.colnames_ccr.index(x)+1)
                og=project.colnames_das[project.colnames_ccr.index(x)]
                temp=DataFrame(data={'Column':[column],'Position':[position],'OG Name':[og]})
                columns_df=columns_df.append(temp)
        columns_df = columns_df.set_index('Column')
        print('\n')
        print('Sensor locations for {}:'.format(project.project_name))
        print(columns_df[['Position','OG Name']])
        print('\n')

    def run_bluesky(project, start=None, end=None):
        """Pulls irradiance & weather data from Solcast for the project & date range.

        Args:
            project (Project): The `Project` object to use for the Solcast script.
            start (str, datetime, or date, optional): The start date for Solcast data. Defaults to first day of the current month.
            end (str, datetime, or date, optional): The end date for Solcast data. Defaults to the day before the script is run.

        Returns:
            DataFrame: The Solcast irradiance & weather data.
        """
        project_name = project.project_name
        tz='US/'+str(project.df_proj_keys['Timezone'])

        # Get default dates if not provided.
        if not start:
            today = datetime.today()
            start = datetime(today.year, today.month, 1)
        if not end:
            today = datetime.today()
            end = today - timedelta(days=1)

        df_cats,df_units=blu.solcats_to_dash(project_name,start,end,resample=True)

        try:
            df_poa=blu.site_s3_to_poa(project_name, start, end)
            df_cats.loc[:, 'sites_ghi_poa']=df_poa
            df_cats.loc[:, 'site'] = project_name
            df_cats[['poa','ghi', 'sites_ghi_poa']].tz_localize(None).plot()
            df_cats['sites_ghi_poa'].tz_localize(None).plot()
        except IndexError:
            print('No GHI to transpose! Solcast POA only')

        df_cats.to_clipboard()
        print('\n')
        print('Solcast data successfully returned for {}'.format(project.project_name))
        print('\n')
        return df_cats

    def generate_power_from_invoice(project, start, stop, total_energy):
        """Generates power based upon `P_exp`. Need to ensure that all weather and irradiance data
        are filled in before running this script.

        Args:
            project (Project): The `Project` object to analyze.
            start (str or datetime): Start date for calculations.
            stop (str or datetime): End date for calculations.
            total_energy (Number): Total energy from the invoice to fill in over the date range.

        Returns:
            DataFrame: The calculated power data for the interval provided.
        """
        #use expected power (or POA though expected power is probs better)
        #power_proportions will have a sum of 1, it represents what portion of power is contained in that hour
        power_proportions=project.df['P_exp'][start:stop]/(project.df['P_exp'][start:stop].sum())
        power_proportions=project.df['POA_avg'][start:stop]/(project.df['POA_avg'][start:stop].sum())


        #get difference between curated power and actual invoiced to aim for 0
        remainder=total_energy
        #initiate a power_iterative term, its really the power when you remove points over clipping
        power_i= power_proportions*0
        
        #iteratively spread production over the month based on expected until remainder is near 0
        i = 0
        while remainder >(total_energy/(10*10**8)): #while loop instead of for because i am seeking a goal, not an amount of iterations
            power_data=(power_proportions*remainder)+power_i
            power_i=power_data.clip(upper=project.clipping_KW) #gets rid of points over clipping
            remainder=(power_data-power_i).sum()
            i+=1
            if i > 10000:
                break
            
        print('\n')
        print('Power data successfully generated for {}'.format(project.project_name))
        print('\n')
        return power_data

    @func_timer
    def _process_data(self, reprocess=None):
        # TODO: update for reprocessing only to run the methods that update the required data

        print('Processing data for {}'.format(self.project_name))

        # Find columns
        self.__locate_column_positions()

        # Turn off sensors disabled in the config file
        self.__disable_faulty_sensors()

        # Perform any necessary unit conversions
        self.__convert_sensor_units()

        # Configure PVSyst
        self.__pvsyst_adjustments()

        # Calculate monthly
        self.__calculate_monthly()

        # Fix columns before data gets used anywhere
        self.__column_fix()

        # Find sensor anomalies
        self.__find_sensor_anomalies()

        # Fill NAs
        self.df = self.df.fillna(0)

        # Correct POI data
        if self.Battery_AC_site:
            self.__correct_poi()

        # Correct meter data
        self.__correct_meter_data()

        # Calculate averages for the sensors on the site
        self.__calculate_sensor_averages()
        
        # QUESTION: do we need another fillna here?
        self.df = self.df.fillna(0)

        self.__calculate_availability()

        # QUESTION: Snow data - we probably only need to push to S3 on initial run
        self.snow_data = snow.timeseries(self.raw_snow_df,
                               self.df.index,
                               self.lat,
                               self.lon)

        self.snow_coverage = \
            snow.coverage_v3(self.df,
                        self.snow_data,
                        self.df['Tmod_avg'] - \
                            self.df['POA_avg'] * np.exp(self.a_module + self.b_module * self.df['Wind_speed']),
                        self.data_source,
                        self.project_name)
        self.snow_times = self.snow_coverage[self.snow_coverage > 0].index
        """
        # ADD IN SNOW DATA STORAGE TO FIX YEAR ROLLOVER PROBLEM 1.12.2022
        # establish s3 storage area
        import boto3
        import StringIO
        bucket = 'perfdatadev.ccrenew.com'
        bucket_prefix_snow = "snow_projects/"
        s3_snow = boto3.client('s3')
        #pull in functions

        def bucket_push(df, s3_key):
            fileobj = StringIO.StringIO()
            df.to_csv(fileobj)
            fileobj.seek(0)

            s3_snow.upload_fileobj(fileobj, bucket, s3_key)

        # actually send the data up. one folder per project, 2 files per project per year

        fname_data = "{}snow_data_project.csv".format(self.data_source)
        key_data = bucket_prefix_snow+self.project_name+"/"+fname_data
        bucket_push(snow_data, key_data)

        fname_coverage = "{}snow_coverage_project.csv".format(self.data_source)
        key_coverage = bucket_prefix_snow+self.project_name+"/"+fname_coverage
        bucket_push(snow_coverage, key_coverage)
        #############################################################################
        """

        # Calculate PR
        self.__calculate_PR()

        # Calculate losses
        self.__calculate_losses()

        # Calculate revenue
        self.__calculate_revenue('initial')

        # Calculate weather adjustments
        self.__calculate_weather_adjustments()

        # Calculate weather adjusted monthly revenue
        self.__calculate_revenue('weather_adjusted')

        # Calculate percentages for dashboard
        self.__calculate_dashboard_percentages()

        # Verify Performance Guarantees
        self.__verify_performance()

        # Calculate metrics
        self.__calculate_project_metrics()


        # import necessary libraries for connecting to s3

        bucket = 'perfdatadev.ccrenew.com'

        # helper function to get data from s3
        def retrieve_df(key):
            path = "s3://{b}/{k}".format(b=bucket, k=key)
            try:
                df = pd.read_csv(path, index_col=0, parse_dates=True)
                df = df.loc[~df.index.duplicated(), :]
            except IOError:
                return pd.DataFrame()
            return df

        def get_tracker_ava(project):
            year = int(self.df.index[0].year)
            # create an empty df to avoid issues with sites w/o data
            start = '1/1/'+str(year)
            end = '12/31/'+str(year)
            index = pd.date_range(start, end)
            columns = [u'Ava', u'Ava NaN', u'Ava No Interp',
                    u'Ava Variance', u'Date', u'Site', u'Type']
            df_hist = pd.DataFrame(index=index, columns=columns)

            # get sites that actually have data
            tracker_prefix = 'Tracker_data_pf/Ava_History/'
            key = tracker_prefix+project+'.csv'
            df_hist2 = retrieve_df(key)
            if len(df_hist2) > 0:
                df_hist2.index = pd.to_datetime(df_hist2['Date'])
                df_hist2 = df_hist2[df_hist2.index.year == year]
                # combine together and resample
                df_hist = df_hist.combine_first(df_hist2)

                df_hist = df_hist.resample('M').mean()
            else:
                df_hist = df_hist.resample('M').asfreq()

            df_hist = df_hist[['Ava', 'Ava NaN', 'Ava No Interp', 'Ava Variance']]
            df_hist.columns = ['tracker_ava', 'tracker_ava_nan',
                            'tracker_ava_interpremoved', 'tracker_variance_ava']
            df_hist.loc[df_hist.index < '7/1/2020'] = np.nan
            return df_hist

        df_tracker_ava = get_tracker_ava(self.project_name)


    @func_timer
    def excel_output(self):

        template_filename = 'Dashboard_v07.xlsx'
        self.metadata = pd.DataFrame([], index=[1])
        self.metadata['date'] = str(datetime.now())
        self.metadata['username'] = os.getenv('username')
        self.metadata['version'] = sys.version
        try:
            self.metadata['filename'] = __file__
        except:
            self.metadata['filename'] = 'console'
        self.metadata['weather_adjusted_functions'] = weather.generate_Tcell.__module__
        self.metadata['Table_by_Rate_Schedule'] = rate_table.generate_table_variable_by_rev_schedule_v02.__module__
        self.metadata['Plant_Availability'] = plant_ava.calculate_inverter_availability_and_loss.__module__
        self.metadata['Correct_Meter_data'] = meter_correct.Correct_Meter_with_Inv_data_v01.__module__
        self.metadata['Rate_Structure_Python_with_DST'] = rates.generate_Rate_column.__module__
        self.metadata['Performance_Guarantees'] = perf.USB1_performance_guarantee.__module__
        self.metadata['snow_loss_functions'] = snow.timeseries.__module__
        # FIXME: update snow file
        self.metadata['Snow data file'] = "UPDATE SNOW FILE REFERENCE"
        self.metadata['df.index[0]'] = self.df.index[0]
        self.metadata['df.index[-1]'] = self.df.index[-1]
        self.metadata['pandas'] = pd.__version__
        self.metadata['dashboard template'] = template_filename
        self.metadata = self.metadata.T

        df_dict = {'PVsyst': self.df_Pvsyst_2_month,
                   'OM_Summary': self.OM_data,
                   'data_month': self.df_month_3,
                   'Table_gen': self.table_gen,
                   'Table_rev': self.table_rev,
                   'data_day': self.df_d2,
                   'Guarantee': self.df_perf,
                   'Metadata': self.metadata}
        # sheet_name_save = ['PVsyst', 'OM_Summary', 'data_month', 'Table_gen',
        #                    'Table_rev', 'data_day', 'Guarantee', 'Metadata']

        # Build filename for Excel output
        if self.project_name == 'Old Pageland Monroe Road Solar Farm':
            project_name = 'Old Pageland'
        else:
            project_name = self.project_name
        ts = datetime.now().strftime("%Y-%m-%d-T%H%M%m")
        output_filename = project_name + '_' + ts +'.xlsx'

        #  Create a copy of template and rename it in project folder to save analysis
        template_filepath = os.path.join(self.dashboard_dir, 'Python_Functions', 'Dashboard_Template', template_filename)
        output_dir = os.path.join(self.dashboard_dir, self.project_directory, self.project_name)
        shutil.copy(template_filepath, output_dir)
        output_template = os.path.join(output_dir, template_filename)
        output_filepath = os.path.join(output_dir, output_filename)
        os.rename(output_template, output_filepath)

        df_tools.dfs_to_excel(output_filepath, df_dict)

    
    def export_summary(self):
        export_summary = None 
        if export_summary:

            try:
                engine
            except:
                engine = get_sql_engine_cgd()

            df_toSQL = pd.concat(
                [self.df_Pvsyst_2_month[[u'KWh_adj_by_days', 'NREL_Weather_Adj_%']],
                 self.df_month_2[['Plant_Perf_%', 'Snow_Adj_%', 'Grid_Ava_%', 'Inv_Ava_%', 'Meter_Corrected_2', 'PR_Plant']],
                 self.df_Pvsyst_2_month['PR_IE_P50_PR'],
                 self.df_month_2[['diff_PR_%', 'Project_IPR_%', 'Project_OPR_%', 'Project_OPR_Temp_%']],
                 self.df_Pvsyst_2_month['Revenue_IE_P50_days_adj'],
                 self.df_month_2[['diff_weather_$', 'diff_Plant_Perf_$', 'diff_snow_$', 'diff_Grid_ava_$', 'diff_Inv_ava_$', 'Meter_Corrected_2_rev', 'diff_all_$', 'AC_Capacity_%', 'DC_Capacity_%', 'Monthly Probability of Exceedence']],
                 self.df_Pvsyst_2_month['POA (W/m2)'],
                 self.df_month_2[['POA_avg', 'Perf_Test_Pass']],
                 self.df_Pvsyst_2_month[['POA_%', 'GHI_%', 'Model_Irradiance_Index', 'Post SC Date', 'Pvsyst_POA_weighted_Tcell']],
                 self.df_month_2[['OPR_notemp', 'POA_weighted_Tcell', 'PR_notemp']],
                 self.df_Pvsyst_2_month[['Pvsyst_PR_notemp', 'IE_AC_batt_eff_%', 'IE_AC_batt_rev_gain', 'Revenue_IE_POI']],
                 self.df_month_2[['AC_batt_eff_%', 'AC_batt_eff_index_%', 'AC_batt_rev_gain', 'AC_batt_rev_index_%', 'diff_AC_batt_$', 'POI_Corrected_2', 'POI_rev', 'ac_battery_flag', 'Modeled_AC_batt_rev_gain', 'Modeled_AC_batt_rev_index_%', 'Modeled_AC_rev_target', 'OM_uptime']],
                 self.df_Pvsyst_2_month[['POI Output (kWh)', 'Weather_prorate', 'days_month_5', 'Nominal_Noclip_Weather_Adj', 'Nominal_NoclipNoTemp_Weather_Adj', 'ie_clipping_dcimpact', 'ie_clipping_astmimpact']],
                 self.df_month_2[['measured_clipping_dcimpact', 'measured_clipping_astmimpact', 'night_flag', 'POA_regress_flag', 'borrowed_data', 'inv_cum_check', 'poi_limit_flag', 'snowfall', 'snow_coverage_5', 'snow_coverage_energy']],
                 OM_data2,
                 df_tracker_ava],
                axis=1)

            df_toSQL['meter_check'] = (df_toSQL['Meter_Corrected_2'] / self.df_month_3['AE_Meter']) - 1
            df_toSQL[['KWh_adj_by_days', 'Meter_Corrected_2', 'POA (W/m2)', 'POA_avg', 'POI_Corrected_2']] = \
                df_toSQL[['KWh_adj_by_days', 'Meter_Corrected_2', 'POA (W/m2)', 'POA_avg', 'POI_Corrected_2']]/1000

            # filter by months with no data, then filter for FC
            df_toSQL.loc[df_toSQL[u'KWh_adj_by_days'] == 0, :] = 0
            df_toSQL_FC = df_toSQL.copy()
            df_toSQL_FC.loc[self.df_Pvsyst_2_month['Post SC Date'] == 0, :] = 0

            # correct index
            df_toSQL.index = df_toSQL.index.strftime('%b')
            df_toSQL_FC.index = df_toSQL.index

            # create Total row. Combination of sums and sumproducts
            df_toSQL_total = pd.DataFrame([], columns=df_toSQL.columns.tolist(), index=['Total'])
            df_toSQL_total_FC = df_toSQL_total.copy()

            sum_var = [
                'KWh_adj_by_days', 'Meter_Corrected_2', 'Revenue_IE_P50_days_adj',
                'diff_weather_$', 'diff_Plant_Perf_$', 'diff_snow_$', 'diff_Grid_ava_$',
                'diff_Inv_ava_$', 'Meter_Corrected_2_rev', 'diff_all_$', u'POA (W/m2)',
                'POA_avg', 'Revenue_IE_POI', 'diff_AC_batt_$', 'POI_Corrected_2', 'POI_rev',
                'POI Output (kWh)', 'weather_ad_exp_prod_kwh', 'estimated_loss', 'weather_losses_kwh',
                'grid_ava_kwh', 'inv_ava_kwh', 'snow_loss_kwh', 'plant_perf_kwh']
            df_toSQL_total[sum_var] = df_toSQL[sum_var].sum().values
            df_toSQL_total_FC[sum_var] = df_toSQL_FC[sum_var].sum().values

            dot_var = [
                'NREL_Weather_Adj_%', 'Plant_Perf_%', 'Snow_Adj_%', 'Grid_Ava_%',
                'Inv_Ava_%', 'PR_Plant', 'PR_IE_P50_PR', 'diff_PR_%', 'Project_IPR_%',
                'Project_OPR_%', 'Project_OPR_Temp_%', 'AC_Capacity_%', 'DC_Capacity_%',
                'POA_%', 'GHI_%', 'Model_Irradiance_Index', 'Post SC Date', 'PR_notemp',
                'OPR_notemp', 'POA_weighted_Tcell', 'Pvsyst_PR_notemp', 'Pvsyst_POA_weighted_Tcell',
                'meter_check', 'IE_AC_batt_eff_%', 'IE_AC_batt_rev_gain', 'AC_batt_eff_%',
                'AC_batt_eff_index_%', 'AC_batt_rev_gain', 'AC_batt_rev_index_%',
                'ac_battery_flag', 'Modeled_AC_batt_rev_gain', 'Modeled_AC_batt_rev_index_%',
                'Modeled_AC_rev_target', 'OM_uptime', 'Weather_prorate', 'days_month_5',
                'Nominal_Noclip_Weather_Adj', 'Nominal_NoclipNoTemp_Weather_Adj',
                'ie_clipping_dcimpact', 'ie_clipping_astmimpact', 'measured_clipping_dcimpact',
                'measured_clipping_astmimpact', 'night_flag', 'POA_regress_flag', 'inv_cum_check',
                'poi_limit_flag', 'ovp_insolation', 'ovp_production']

            for var in dot_var:
                df_toSQL_total[var] = ((df_toSQL[var] * df_toSQL['KWh_adj_by_days']) / df_toSQL['KWh_adj_by_days'].sum()).sum()
                df_toSQL_total_FC[var] = ((df_toSQL_FC[var] * df_toSQL_FC['KWh_adj_by_days']) / df_toSQL_FC['KWh_adj_by_days'].sum()).sum()

            # TODO: fix probability of excedence total
            df_toSQL_total['Post SC Date'] = 0
            df_toSQL_total_FC['Post SC Date'] = 1

            # append
            df_toSQL = df_toSQL.append(df_toSQL_total)[df_toSQL.columns.tolist()].fillna(0)

            #df_toSQL_FC = df_toSQL_FC.append(df_toSQL_total_FC)[df_toSQL.columns.tolist()].fillna(0)
            df_toSQL = df_toSQL.append(df_toSQL_total_FC)[df_toSQL.columns.tolist()].fillna(0)

            # add cols
            df_toSQL['Year'] = [year] * len(df_toSQL)
            df_toSQL['Site_name'] = [self.project_name] * len(df_toSQL)
            #df_toSQL_FC['Year'] = [year]* len(df_toSQL_FC)
            #df_toSQL_FC['Site_name'] =  [self.project_name] * len(df_toSQL_FC)
            df_toSQL['month'] = df_toSQL.index

            column_map = {'AC_Capacity_%': 'ac_capacity_5',
                        'DC_Capacity_%': 'dc_capacity_5',
                        'Grid_Ava_%': 'grid_ava_5',
                        'Inv_Ava_%': 'inv_ava_5',
                        'Monthly Probability of Exceedence': 'monthly_probability_of_exceedence',
                        'NREL_Weather_Adj_%': 'nrel_weather_adj_5',
                        'POA (W/m2)': 'poa_wm2',
                        'Plant_Perf_%': 'plant_perf_5',
                        'Post SC Date': 'post_fc',
                        'Project_IPR_%': 'project_ipr_5',
                        'Project_OPR_%': 'project_opr_5',
                        'Project_OPR_Temp_%': 'project_opr_temp_5',
                        'Snow_Adj_%': 'snow_adj_5',
                        'diff_PR_%': 'diff_pr_5',
                        'POA_%': 'poa_5',
                        'GHI_%': 'ghi_5',
                        'Model_Irradiance_Index': 'model_irradiance_index',
                        'POA_weighted_Tcell': 'poa_weighted_tcell',
                        'OPR_notemp': 'opr_notemp',
                        'Pvsyst_POA_weighted_Tcell': 'pvsyst_poa_weighted_tcell',
                        'PR_notemp': 'pr_notemp',
                        'Pvsyst_PR_notemp': 'pvsyst_pr_notemp',
                        'IE_AC_batt_eff_%': 'ie_ac_batt_eff_5',
                        'AC_batt_eff_%': 'ac_batt_eff_5',
                        'AC_batt_eff_index_%': 'ac_batt_eff_index_5',
                        'AC_batt_rev_index_%': 'ac_batt_rev_index_5',
                        'Modeled_AC_batt_rev_index_%': 'modeled_ac_batt_rev_index_5',
                        'POI Output (kWh)': 'om_unadjusted_p50_kwh',
                        'WAP_5': 'WAP_5'}

            df_toSQL['ccr_id'] = self.df_keys.loc[self.df_keys['Project']
                                            == self.project_name, 'CCR_ID'].item()
            df_toSQL['WAP_5'] = df_toSQL['Project_IPR_%'] / \
                df_toSQL['NREL_Weather_Adj_%']/df_toSQL['Snow_Adj_%']
            df_toSQL = df_toSQL.rename(columns=column_map)
            df_toSQL = df_toSQL.rename(columns=lambda s: s.lower())

            engine.execute("DELETE FROM dev_analytic.am_summary_data WHERE site_name = %(site_name)s AND year = %(year)s;",
                        site_name=self.project_name, year=year)
            #engine.execute("DELETE FROM dev_analytic.am_forecast_data WHERE site_name = %(site_name)s AND year = %(year)s;", site_name = self.project_name, year = year)
            # use the two lines below to add a column to sql database
            #query="ALTER TABLE dev_analytic.am_summary_data ADD COLUMN wap_5 Float"
            # engine.execute(query)

            df_toSQL.to_sql(name='am_summary_data',
                            con=engine,
                            schema='dev_analytic',
                            if_exists='append',
                            index=False,
                            chunksize=None,
                            dtype=None)
        
        
    @func_timer
    def __column_fix(self):
        '''
        this function, added 12/10/2020 (and some time after, sorry I'm slow),
        intends to provide an option to alter the AE file from the config file.
        Options here include allowing for setting 1 column equal to the sum of others,
        doing a dif on the cumulative meter or building a cumulative from a power column.
        To do "trip" this function put "column fix" in the Var_ID column on sensor offline page
        '''

        for i, row in self.sensor_OFF.iterrows():
            option = row['Var_ID']
            e = row['end date']
            e = self.df.index[-1] if e == -1 else e
            func_choice = row['#']
            func_outcome = row['description']
            s = row['start date']

            if option.lower() != 'column fix':
                continue
            if self.df.index[0].year in set(pd.date_range(s, e, freq='d').year):
                if s.year != self.df.index[0].year:
                    print ('changing start for column fix')
                    # set s to start of current year if before current year
                    s = self.df.index[0]

                print(func_outcome)
                if func_choice.lower() == 'eval':
                    # do simple eval functions
                    print('eval eval eval')
                    # this(needing df_temporary on all these) is hacky and I hate it,
                    # but it wasn't working doing an inplace=True on a loc version of df. so this works

                    # .eval using basic arithmetic functions, because of that when there is a NaN value,
                    # it fails to do the eval. need to fillna(0) during the temporary
                    df_temp2 = self.df.copy()
                    columns =  [func_outcome.split('=')[0].strip()] + [col.strip() for col in func_outcome.split('=')[1].split('+')]
                    for column in columns:
                        try:
                            df_temp2[column] = df_temp2[column].fillna(0)
                        except:
                            continue

                    # do the eval
                    df_temporary = df_temp2.eval(func_outcome)
                    # change only the desired column so the rest is not changed from NaN
                    self.df.loc[s:e, func_outcome.split('=')[0].strip()] = df_temporary[func_outcome.split('=')[0].strip()].loc[s:e]

                elif func_choice.lower() == 'dif_cum':
                    # Will do this by creating a net_meter.shift(1) column.
                    # Dif in cumulative is then net_meter-net_meter_shift.
                    # Delete net_meter_shift afterwards
                    # FOR SOME REASON "s" IS READ AS error.225 INSTEAD OF THE DATE. IT WORKS WHEN RUN LINE BY LINE SO IDK WHAT IS HAPPENING
                    df_temporary = self.df.copy()
                    fix_column_split = func_outcome.split(',')

                    # Cum column
                    fix_column = fix_column_split[1]
                    # Power column
                    func_outcome = fix_column_split[0]

                    # Shift column
                    shift_column = fix_column + '_shifted'
                    df_temporary[shift_column] = df_temporary[fix_column].shift(1)
                    df_temporary[func_outcome] = \
                        df_temporary[fix_column] - df_temporary[shift_column]

                    # Set to NAN if the cumulative or the shift cumulative column is missing
                    df_temporary.loc[df_temporary[fix_column].isnull(), func_outcome] = df_temporary[fix_column]
                    df_temporary.loc[df_temporary[shift_column].isnull(), func_outcome] = df_temporary[shift_column]
                    df_temporary = df_temporary.drop(columns=shift_column)
                    self.df.loc[(self.df.index >= s) & (self.df.index <= e)] = \
                        df_temporary.loc[(df_temporary.index >= s) & (df_temporary.index <= e)]

                elif func_choice.lower() == 'build_cum':
                    print('build cum')
                    fix_column_split = func_outcome.split(',')
                    fix_column = fix_column_split[1]
                    func_outcome = fix_column_split[0]

                    if pd.isna(self.df[fix_column].loc[s]):
                        print('''-------------
                        SELECTED START DATE {} FOR BUILDING CUMULATIVE METER IS NAN. 
                        CHOOSE NEW DATE IN CONFIG
                        --------------'''.format(s))
                        self.df[fix_column].loc[s:].fillna(0)
                    df_temporary = self.df[fix_column].fillna(
                        0).loc[s] + self.df[func_outcome].loc[s:].fillna(0).cumsum()

                    self.df.loc[s:e, fix_column] = df_temporary.loc[s:e]

            else:
                continue  # this continues if s and e both occur in a previous year


    @func_timer
    def __disable_faulty_sensors(self):
        """
        This function manipulates df_sensor_ON to change when a field should be used in future calculations
        Args:
            sensor_OFF: df of the sensor offline sheet of the config file
            df_sensor_ON: df of all the possible fields in the data. True, False or, Negative POA, or Not updating    
        """
        for i, row in self.sensor_OFF.iterrows():
            sensor = row['Var_ID']
            s = row['start date']
            e = row['end date']

            # Check for change in losses type and move to the next row. This fxn only for turning sensors off
            if sensor.lower() in ["grid", "curtailment", "site ava", "column fix"]:
                continue

            # Set dates with -1 to last date in df
            if (e == -1) | (e == pd.to_datetime('1899-12-30')):
                e = self.df.index[-1]

            self.df_sensor_ON.loc[(self.df_sensor_ON.index >= s) & (self.df_sensor_ON.index <= e), sensor] = False


    @func_timer
    def __convert_sensor_units(self):
        """

        """
        # Perform unit conversions that are found in the configuration file
        if np.any(['Convert_Multiply' in s for s in list(self.Convert_Units.columns)]):
            Convert_custom = self.Convert_Units.loc[~self.Convert_Units['Convert_Multiply'].isnull(), ['Var_ID', 'Convert_Multiply']]
            for index, row in Convert_custom.iterrows():
                self.df[row['Var_ID']] = self.df[row['Var_ID']] * row['Convert_Multiply']

        # Convert sensor units
        Convert_Temperature = self.Convert_Units.loc[self.Convert_Units['Convert_Farenheit_to_Celcius'] == True, 'Var_ID'].values.tolist()
        for t_sensor in Convert_Temperature:
            self.df[t_sensor] = (self.df[t_sensor] - 32.0) * 5.0 / 9.0

        Convert_wind = self.Convert_Units.loc[self.Convert_Units['Convert_mph_to_mps'] == True, 'Var_ID'].values.tolist()
        for wind in Convert_wind:
            self.df[wind] = self.df[wind] * 0.44704


    @func_timer
    def __pvsyst_adjustments(self):

        # Add Tcell column. The function is in the weather adjusted function that are imported at the top of the script.
        self.df_Pvsyst['Tcell'] = weather.generate_Tcell(self.df_Pvsyst['POA (W/m2)'],
                                                 self.df_Pvsyst['Ambient Temperature'],
                                                 self.df_Pvsyst['Wind Velocity (m/s)'],
                                                 self.a_module,
                                                 self.b_module,
                                                 self.Delta_Tcnd)

        # Calculate average cell temperature for the year
        # (See NREL paper here: https://www.nrel.gov/docs/fy13osti/57991.pdf)
        Gpoa_x_Tcell = self.df_Pvsyst['POA (W/m2)'].values * self.df_Pvsyst['Tcell'].values
        self.Tcell_typ_avg = np.sum(Gpoa_x_Tcell) / self.df_Pvsyst['POA (W/m2)'].sum()

        # For PVsyst we need to shift the columns to adjust for DST.
        # It also deletes the last value. It is from the following year
        self.df_Pvsyst_2, self.normal_rate_flag = rates.generate_Rate_column(
                                                            self.config_filepath,
                                                            shift_DST=True,
                                                            year=self.year)
        self.df_Pvsyst_2 = self.df_Pvsyst_2.iloc[:-1, :]

        # Also need to remove Feb 29, to match PVsyst file.
        self.df_Pvsyst_2 = self.df_Pvsyst_2[~((self.df_Pvsyst_2.index.month == 2) & (self.df_Pvsyst_2.index.day == 29))]

        # Adjust df_Pvsyst index to match the year that we're running
        # (the year in the config file may be in the past, when the 8760 was generated)
        self.df_Pvsyst.index = self.df_Pvsyst_2.index

        # Insert Pvsyst degradation before calculating rates and PR. Not needed before weather corrected function
        # Set pvsyst datastart to January first regardless of AE dataset start
        PVsyst_start = datetime(int(self.df.index.year[0]), 1, 1)
        Deg_months = (PVsyst_start.year - self.PIS_date.year) * 12 + PVsyst_start.month - self.PIS_date.month

        if Deg_months > 0:  # site turned on last year
            Deg_array = np.arange(0, 40*12, 1/12.0)[Deg_months:Deg_months+12]
        else:  # site turned on this calandar year or in the future
            if Deg_months < -12:
                Deg_array = np.zeros(12)
            else:
                Deg_months = Deg_months*-1
                Deg_array = np.arange(0, 1, 1/12.0)[:(12-Deg_months)]
                Deg_array = list(Deg_array)
                Deg_array = list(np.arange(Deg_months)*0) + Deg_array

        # Create montly degradation profile based on linear interporlation of yearly deg factors
        Deg_Pvsyst = np.interp(Deg_array, self.Deg.index, self.Deg['Capacity'].values)

        # Create column for non-derated values
        self.df_Pvsyst['kWh_ORIGINAL'] = self.df_Pvsyst['Year 0 Actual Production (kWh)']

        # Initialize derate column
        self.df_Pvsyst['Degradation_Derate'] = 1

        # Set monthly degredation factor from linear interp above
        for i in range(1, 13):
            self.df_Pvsyst.loc[self.df_Pvsyst.index.month == i, 'Degradation_Derate'] = Deg_Pvsyst[i-1]
        self.df_Pvsyst['Year 0 Actual Production (kWh)'] = \
            self.df_Pvsyst['Year 0 Actual Production (kWh)'].multiply(self.df_Pvsyst['Degradation_Derate'])

        # Calculate temperature corrected DC energy based on NREL paper
        self.df_Pvsyst = weather.calculate_DC_Corrected_PVsyst(
                                                       self.df_Pvsyst,
                                                       self.Pstc_KW,
                                                       self.Gstc,
                                                       self.Temp_Coeff_Pmax,
                                                       self.Tcell_typ_avg,
                                                       self.clipping_KW)

        # also apply degradation to gen_no_clipping
        self.df_Pvsyst['Gen_NO_Clipping_PVsyst'] = \
            self.df_Pvsyst['Gen_NO_Clipping_PVsyst'].multiply(self.df_Pvsyst['Degradation_Derate'])

        col_pvsyst = [i for i in self.df_Pvsyst.columns if i.lower() not in ('month', 'day', 'hour')]

        self.df_Pvsyst_2 = pd.concat([self.df_Pvsyst_2, self.df_Pvsyst[col_pvsyst]], axis=1)
        self.df_Pvsyst_2['POA_weighted_Tcell'] = self.df_Pvsyst['Tcell'] * self.df_Pvsyst_2['POA (W/m2)']

        if self.Battery_AC_site:
            PVsyst_degradation_hours = (datetime(self.year, 1, 1) - self.PIS_date).total_seconds() / 3600
            # TODO: swapped out `rates_PVsyst['Rates']` for `df_Pvsyst_2['Rates']` because I don't think the rates_PVsyst df is necessary
            df_battery = batt.Run_AC_Batt(self.df_Pvsyst_2['Year 0 Actual Production (kWh)'], self.df_Pvsyst_2['Rates'], PVsyst_degradation_hours)

            df_battery_pp = batt.AC_Batt_PP(self.df_Pvsyst_2, df_battery)

            self.df_Pvsyst_2['POI Output (kWh)'] = df_battery_pp['POI_no_night']
            self.df_Pvsyst_2['POI_ORIGINAL'] = self.df_Pvsyst_2['POI Output (kWh)']
        else:
            self.df_Pvsyst_2['POI_ORIGINAL'] = self.df_Pvsyst_2['kWh_ORIGINAL']
            self.df_Pvsyst_2['POI Output (kWh)'] = self.df_Pvsyst_2['Year 0 Actual Production (kWh)']

        # Calculate flat payments/fees
        self.df_Pvsyst_2['Revenue_IE_P50'] = \
            self.df_Pvsyst_2['Year 0 Actual Production (kWh)'].multiply(self.df_Pvsyst_2['Rates'], axis="index") + self.df_Pvsyst_2['Flat']
        self.df_Pvsyst_2['Revenue_IE_POI'] = \
            self.df_Pvsyst_2['POI Output (kWh)'].multiply(self.df_Pvsyst_2['Rates'], axis="index") + self.df_Pvsyst_2['Flat']


    @func_timer
    def __calculate_monthly(self):
        # Calculate monthly DF
        self.df_Pvsyst_2_month = self.df_Pvsyst_2.resample('M').sum()
        self.df_Pvsyst_2_month['POA_weighted_Tcell'] /= self.df_Pvsyst_2_month['POA (W/m2)']
        self.df_Pvsyst_2_month['Blended_Rate'] = self.df_Pvsyst_2_month[['Revenue_IE_P50']].div(self.df_Pvsyst_2_month['Year 0 Actual Production (kWh)'].replace(0, np.nan), axis="index")
        self.df_Pvsyst_2_month['Blended_POI_rate'] = self.df_Pvsyst_2_month[['Revenue_IE_POI']].div(self.df_Pvsyst_2_month['Year 0 Actual Production (kWh)'].replace(0, np.nan), axis="index")
        self.df_Pvsyst_2_month['PR_IE_P50'] = self.df_Pvsyst_2_month[['Year 0 Actual Production (kWh)']].div(self.df_Pvsyst_2_month['DC_corrected_PVsyst'].replace(0, np.nan), axis="index")
        self.df_Pvsyst_2_month['PR_IE_P50_PR'] = self.df_Pvsyst_2_month[['Gen_NO_Clipping_PVsyst']].div(self.df_Pvsyst_2_month['DC_corrected_PVsyst_PR'].replace(0, np.nan), axis="index")
        
    
    @func_timer
    def __locate_column_positions(self):
        # Find Meters
        self.pos_Meter = [s for s in self.df.columns if 'Meter_kw_' in s]
        # Find CUM Meters
        self.pos_Meter_Cum = [s for s in self.df.columns if 'Meter_kwhnet_' in s]
        # search for POA sensors and generate avg.
        self.pos_POA = [s for s in self.df.columns if 'POA' in s]
        # search for GHI sensors and generate avg
        self.pos_GHI = [s for s in self.df.columns if 'GHI' in s]
        #   Wind speed in m/s.  Also Energy gives wind speed in Km/h
        self.pos_Wind = [s for s in self.df.columns if 'Wind_speed' in s]
        #   Find Inverters
        self.pos_Inv = [s for s in self.df.columns if 'Inv_kw_' in s]
        self.pos_Inv_cum = [s for s in self.df.columns if 'Inv_kwnet_' in s]

        #  Convert all Temperature sensor in Celcius if needed
        self.pos_Tmod = [s for s in self.df.columns if 'Tmod' in s]
        self.pos_Tamb = [s for s in self.df.columns if 'Tamb' in s]
        self.pos_Temperature = self.pos_Tamb + self.pos_Tmod

        #  Main meter site cols - battery sites only
        self.pos_POI_Meter = [s for s in self.df.columns if 'POI_kw_' in s]
        self.pos_POI_Meter_Cum = [s for s in self.df.columns if 'POI_kwhnet_' in s]

        #  Battery site cols
        self.pos_BatteryAC = [s for s in self.df.columns if 'BatteryAC_kw_' in s]
        self.pos_BatteryAC_del = [s for s in self.df.columns if 'BatteryAC_kwhdel_' in s]
        self.pos_BatteryAC_rec = [s for s in self.df.columns if 'BatteryAC_kwhrec_' in s]

        # Find all tracker position sensors
        self.pos_Tracker = [s for s in self.df.columns if 'Tracker_position' in s]
        self.Tracker_site = not (self.pos_Tracker == [])
        
    
    @func_timer
    def __find_sensor_anomalies(self):
        #   Add function to find sensors with anomalies
        for s in self.pos_Temperature:
            self.df_sensor_ON.loc[self.df[s].isnull(), [s]] = "Missing data NAN"
            # 0 deg is clear sign sensor is broken for deg F
            self.df_sensor_ON.loc[self.df[s] <= -30, [s]] = "Negative Temp"
            # set unreasonabley high temp. Usual max is 150 deg F
            self.df_sensor_ON.loc[self.df[s] > 120, [s]] = "Too high Temp"
            # added by Saurabh on 4/11/18
            self.df_sensor_ON.loc[((self.df[s].diff(1) == 0) & (self.df[s].diff(-1) == 0)), [s]] = 'Not Updating'
            # create flag column that allows for easier numerical 1/0 indexing
            aux = self.df_sensor_ON[[s]] == 'Not Updating'
            rolling_indices = aux[s].rolling(
                window=3, center=True, min_periods=1).sum() > 0
            self.df_sensor_ON.loc[rolling_indices, [s]] = 'Not Updating'

        for s in self.pos_Wind:
            self.df_sensor_ON.loc[self.df[s].isnull(), [s]] = "Missing data NAN"
            # less than 0 not possible for wind sensor
            self.df_sensor_ON.loc[self.df[s] < 0, [s]] = "Negative Wind"
            # set unreasonable ceiling for m/s
            self.df_sensor_ON.loc[self.df[s] > 67, [s]] = "Too High above 67 m/s"

        for s in self.pos_POA:
            self.df_sensor_ON.loc[self.df[s].isnull(), [s]] = "Missing data NAN"
            # less than 0 not possible for POA
            self.df_sensor_ON.loc[self.df[s] < 0, [s]] = "Negative POA"
            # set unreasonable ceiling for W/m2
            self.df_sensor_ON.loc[self.df[s] > 1800, [s]] = "Too high - above 1800"
            # added by Saurabh on 4/11/18
            self.df_sensor_ON.loc[((self.df[s].diff(1) == 0) & (self.df[s].diff(-1) == 0)), [s]] = 'Not Updating'
            # create flag column that allows for easier numerical 1/0 indexing
            aux = self.df_sensor_ON[[s]] == 'Not Updating'
            rolling_indices = aux[s].rolling(window=3, center=True, min_periods=1).sum() > 0
            self.df_sensor_ON.loc[rolling_indices, [s]] = 'Not Updating'

        for s in self.pos_GHI:
            self.df_sensor_ON.loc[self.df[s].isnull(), [s]] = "Missing data NAN"
            # less than 0 not possible for POA
            self.df_sensor_ON.loc[self.df[s] < 0, [s]] = "Negative GHI"
            # set unreasonable ceiling for W/m2
            self.df_sensor_ON.loc[self.df[s] > 1800, [s]] = "Too high - above 1800"

        for s in self.pos_Meter:  # Need to do the meter fix function before any of this checking
            self.df_sensor_ON.loc[self.df[s] > self.clipping_KW * 1.2, [s]] = "Over nameplate threshold"
            self.df_sensor_ON.loc[self.df[s] < self.clipping_KW * - 0.02, [s]] = "Below negative 2% threshold"
            self.df_sensor_ON.loc[self.df[s].isnull(), [s]] = "Missing data NAN"

        for s in self.pos_POI_Meter:
            self.df_sensor_ON.loc[self.df[s] > self.clipping_KW * 2.1, [s]] = "Way over nameplate threshold"
            self.df_sensor_ON.loc[self.df[s] < self.clipping_KW * - 0.02, [s]] = "Below negative 2% threshold"
            self.df_sensor_ON.loc[self.df[s].isnull(), [s]] = "Missing data NAN"

        for s in self.pos_Meter_Cum + self.pos_POI_Meter_Cum:
            self.df_sensor_ON.loc[self.df[s].isnull(), [s]] = "Missing data NAN"

        for s in self.pos_Inv:
            self.df.loc[self.df[s] < 0, [s]] = 0  # inverters should not display below 0
            
    
    @func_timer
    def __correct_poi(self):
        # TODO: update this error log deal to use logging module
        df_POI_ok, draker_flags, error_log = \
            poi.Correct_POI_data_v01(self.df,
                                 self.pos_POI_Meter,
                                 self.pos_POI_Meter_Cum,
                                 self.df_Pvsyst_2,
                                 self.clipping_KW,
                                 self.df_sensor_ON)
        df_POI_ok = df_POI_ok.clip(lower=0)
        self.df_POI_ORIGINAL = self.df[self.pos_POI_Meter + self.pos_POI_Meter_Cum]
        self.df_POI_ORIGINAL.rename(columns=lambda x: x+'_ORIGINAL', inplace=True)
        df_POI_ok.rename(columns=lambda x: x[:-3], inplace=True)
        self.df = self.df.drop(self.pos_POI_Meter, 1)

        #  add Original POI and Corrected one
        self.df = pd.concat([self.df, self.df_POI_ORIGINAL, df_POI_ok], axis=1, join='inner')
        self.df['POI_Corrected_2'] = self.df[self.pos_POI_Meter].sum(axis=1)
        

    @func_timer
    def __correct_meter_data(self):
        if self.project_name in ['Innovative Solar 6, LLC', 'Colchester', 'Franklin', 'Morgan Solar 2']:
            import Correct_Meter_data_v08_IS6 as meter_alt
            df_Meter_OK, self.draker_flags, error_log = \
                meter_alt.Correct_Meter_with_Inv_data_v01(self.df, self.pos_Meter, self.pos_Meter_Cum, self.clipping_KW, self.df_sensor_ON)
        else:
            df_Meter_OK, self.draker_flags, error_log = \
                meter_correct.Correct_Meter_with_Inv_data_v01(self.df, self.pos_Meter, self.pos_Meter_Cum, self.clipping_KW, self.df_sensor_ON)

        # TODO: update this error log deal to use logging module
        # error_log.loc[:, [u'Site_name', u'year']] = [self.project_name, self.year]
        # error_master = error_master.append(error_log)

        # Create new columns in main df to delineate original vs corrected meter values
        self.df_Meter_ORIGINAL = self.df[self.pos_Meter + self.pos_Meter_Cum]
        self.df_Meter_ORIGINAL.rename(columns=lambda x: x+'_ORIGINAL', inplace=True)
        self.pos_Meter_ORIGINAL = [s for s in self.df_Meter_ORIGINAL.columns if 'Meter_kw_' in s]
        self.pos_Meter_Cum_ORIGINAL = [s for s in self.df_Meter_ORIGINAL.columns if 'Meter_kwhnet_' in s]

        df_Meter_OK.rename(columns=lambda x: x[:-3], inplace=True)
        self.df = self.df.drop(self.pos_Meter, 1)
        #  add Original Meter and Corrected one
        self.df = pd.concat([self.df, self.df_Meter_ORIGINAL, df_Meter_OK], axis=1, join='inner')
        #  remove changed values from PR calculation
        self.Meter_delta = np.subtract(self.df[self.pos_Meter], self.df_Meter_ORIGINAL[self.pos_Meter_ORIGINAL]).sum(axis=1)

        # remove off hours after meter delta
        for s in self.pos_Meter:
            self.df.loc[self.df[s] < 0, s] = 0

        # Sum Meters
        # QUESTION: Is there a reason we aren't using `df_sensor_ON` here like for the cum meters?
        # NOTE: leave as is
        aux = self.df[self.pos_Meter].sum(axis=1)
        self.df['Meter'] = aux.values

        # Sum Cum Meters
        aux = self.df[self.pos_Meter_Cum][self.df_sensor_ON[self.pos_Meter_Cum] == True].sum(axis=1)
        self.df['Meter_cum'] = aux.values

        # check if the cum meter is calculated with 2 or more sensors.
        # identify when one sensor is bad and corrects accordingly.
        # Actually this is wrong & only sets the cum meter sum to a single meter & is overwritten anyways
        # if len(self.pos_Meter_Cum) > 1:
            # self.__correct_multiple_cum_meters()

        # For single inverter sites set meter = inverter if meter is zero & vice-versa
        if len(self.pos_Inv) == 1:
            self.df.loc[(self.df[self.pos_Inv[0]] == 0) & (self.df[self.pos_Meter[0]] > 0), self.pos_Inv[0]] = self.df[self.pos_Meter[0]]
            self.df.loc[(self.df[self.pos_Meter[0]] == 0) & (self.df[self.pos_Inv[0]] > 0), self.pos_Meter[0]] = self.df[self.pos_Inv[0]]


    @func_timer
    def __correct_multiple_cum_meters(self):
        #  find rows with at least 1 value = Missing Data in Meter cum
        count_Missing_CUM = self.df_sensor_ON[self.df_sensor_ON[self.pos_Meter_Cum] == "Missing data NAN"].count(axis=1)
        count_Missing_CUM_3 = count_Missing_CUM
        # QUESTION - why does this exclude when all meters are blank? Comment above says to find rows with at least 1 value missing but this line below excludes rows when all values are missing
        # NOTE: if all meters are off then it's likely a site outage
        count_Missing_CUM_3[count_Missing_CUM_3 == len(self.pos_Meter_Cum)] = 0
        count_Missing_CUM_3[count_Missing_CUM_3 > 0] = 1
        aux = self.df['Meter'].multiply(count_Missing_CUM_3)
        meter_cum_corrected = [0]
        for i in range(1, len(self.df['Meter'])):
            if count_Missing_CUM_3[i] == 1:
                meter_cum_corrected.append(self.df['Meter_cum'][i-1] + aux[i])
            else:
                meter_cum_corrected.append(self.df['Meter_cum'][i])
        #
        aux2 = pd.DataFrame()
        aux2['Meter_cum'] = aux
        aux2['Meter_cum_2'] = meter_cum_corrected
        aux2['Meter_cum_max'] = aux2.max(axis=1)
        self.df['Meter_cum'] = aux2['Meter_cum_max']

        ''' ***************          CHANGE 2         *********************'''
        #
        #  Correct the cum meter to avoid going down when one of the sensors is not reporting
        #  See Boseman Solar Center ( August)
        aux3 = pd.DataFrame()
        aux3['Meter_cum'] = self.df['Meter_cum']
        aux3['count_Missing_CUM_3'] = count_Missing_CUM_3
        aux3[self.pos_Meter_Cum] = self.df[self.pos_Meter_Cum].cumsum() - self.df[self.pos_Meter_Cum].cumsum().shift(1)
        #
        self.df['Meter_cum'] = aux3[self.pos_Meter_Cum].multiply(1 - aux3['count_Missing_CUM_3'], axis=0)
            

    @func_timer
    def __calculate_sensor_averages(self):
        # Average POA sensors
        aux = self.df[self.pos_POA][self.df_sensor_ON[self.pos_POA] == True].mean(axis=1)
        self.df['POA_avg'] = aux.values

        # Average GHI sensors
        aux = self.df[self.pos_GHI][self.df_sensor_ON[self.pos_GHI] == True].mean(axis=1)
        self.df['GHI_avg'] = aux.values

        # Average wind speed sensors in m/s. (Also Energy gives wind speed in Km/h)
        aux = self.df[self.pos_Wind][self.df_sensor_ON[self.pos_Wind] == True].mean(axis=1)
        self.df['Wind_speed'] = aux.values

        # Average Tamb sensors
        aux = self.df[self.pos_Tmod][self.df_sensor_ON[self.pos_Tmod] == True].mean(axis=1)
        self.df['Tmod_avg'] = aux.values

        # Average Tamb sensors
        aux = self.df[self.pos_Tamb][self.df_sensor_ON[self.pos_Tamb] == True].mean(axis=1)
        self.df['Tamb_avg'] = aux.values

        # Calculate Tcell from ambient temperature & Tcell from module temperature
        self.df['POA_avg'] = self.df['POA_avg'].fillna(0)
        self.df['Tcell_AMB'] = weather.generate_Tcell(self.df['POA_avg'],
                                              self.df['Tamb_avg'],
                                              self.df['Wind_speed'],
                                              self.a_module,
                                              self.b_module,
                                              self.Delta_Tcnd)
        self.df['Tcell_MOD'] = weather.generate_Tcell_from_Tmod(self.df['POA_avg'],
                                                        self.df['Tmod_avg'],
                                                        self.Delta_Tcnd)

        # Fill Tcell using module temp first
        self.df['Tcell'] = self.df['Tcell_MOD']
        # Use Tcell from ambient temp when possible
        self.df.loc[(self.df['Tamb_avg'] > 0) & (self.df['Wind_speed'] > 0), ['Tcell']] = self.df['Tcell_AMB']


    @func_timer
    def __calculate_availability(self):
        # System Availability
        self.df['Meter_cum'] = self.df['Meter_cum'].values + self.df['Meter'].values
        pos_Zoneamps = [s for s in self.df.columns if 'Zoneamps' in s]
        meter_cum_corrected = [0]

        # QUESTION: is this the same procedure as calculating the meter corrected for multiple meters? (line 1088 in original file)
        for i in range(1, len(self.df['Meter_cum'])):
            if self.df['Meter_cum'][i] == 0:
                meter_cum_corrected.append(meter_cum_corrected[i-1] + self.df['Meter'][i])
            else:
                meter_cum_corrected.append(self.df['Meter_cum'][i])

        #
        aux2 = pd.DataFrame()
        aux2['Meter_cum_OLD'] = self.df['Meter_cum']
        aux2['Meter_cum_FIXED'] = meter_cum_corrected
        #
        coef_Zoneamps = pd.DataFrame(self.df[pos_Zoneamps].values, columns=pos_Zoneamps)
        coef_Zoneamps_sum = coef_Zoneamps.sum(axis=1)
        #
        coef_AVA = pd.DataFrame()
        coef_AVA = self.df[['Meter', 'Meter_cum']]
        coef_AVA['coef_AVA'] = 0
        coef_AVA.loc[(coef_AVA['Meter'] == 0) & (coef_AVA['Meter_cum'] == 1) & (coef_Zoneamps_sum == 0), 'coef_AVA'] = 1
        #
        aux2['Meter_cum_FIXED_Corrected'] = aux2['Meter_cum_FIXED'].multiply(coef_AVA['coef_AVA'])
        #
        self.df['Meter_cum'] = aux2['Meter_cum_FIXED_Corrected']

        # calculate DAS_ON for ava function using native sensors
        self.df['DAS_ON'] = self.df[self.pos_Native].sum(axis=1)
        self.df.loc[self.df['DAS_ON'] != 0, 'DAS_ON'] = 1

        # ASTM
        # Calculate ASTM linear regression coef to calculate Weather adjusted values
        self.var_astm = ['Year 0 Actual Production (kWh)', 'POA (W/m2)', 'Wind Velocity (m/s)', 'Ambient Temperature']
        self.df_coef, self.df_coef_RC = weather.generate_linear_coeff_table_v3(self.df_Pvsyst, self.var_astm, self.clipping_KW)

        # Find empty months
        if not self.df_coef.loc[:, self.df_coef.sum() == 0].empty:
            aux = self.df_coef.loc[:, self.df_coef.sum() == 0]
            # Find typical values to replace bad ones
            avg = self.df_coef.loc[:, self.df_coef.sum() != 0].mean(axis=1)

            # Edit months that failed
            for col in aux.columns:
                self.df_coef.loc[:, col] = avg
            print ("Edited ASTM test - no data for months: " + ",".join(aux.columns))
            logging.warn("Edited ASTM test - no data for months: " + ",".join(aux.columns))
            
        self.P_exp = weather.create_ASTM_column(self.df, self.df_coef)

        #  Remove Clipping from the data
        self.P_exp[self.P_exp > self.clipping_KW] = self.clipping_KW
        self.df['P_exp'] = self.P_exp
        self.ava = plant_ava.calculate_inverter_availability_and_loss(self.df, self.df_Pvsyst, self.P_exp)

        ava_col = ['AVA_Energy_loss', 'Meter_&_ava', 'Grid_loss', 'Meter_cum_corrected_2', 'Meter_Corrected_2']
        self.df[ava_col] = self.ava[ava_col]

        cum_meter_offset = self.df_Meter_ORIGINAL.drop(self.pos_Meter_ORIGINAL, 1).sum(axis=1).subtract(self.df['Meter_cum_corrected_2']).median()

        # Add offset value to match meter
        self.df['Meter_cum_corrected_2'] = self.df['Meter_cum_corrected_2'].add(cum_meter_offset)

        if not self.Battery_AC_site:
            self.df['POI_Corrected_2'] = self.df['Meter_Corrected_2']
            self.df['POI_modeled'] = self.df['POI_Corrected_2']
        else:
            degradation_hours = (self.df.index[0] - self.PIS_date).total_seconds() / 3600

            df_battery_meas = batt.Run_AC_Batt(self.df['Meter_Corrected_2'],
                                          self.df_Pvsyst_2.loc[self.df.index, 'Rates'],
                                          degradation_hours)
            df_battery_pp_meas = batt.AC_Batt_PP(self.df, df_battery_meas)
            self.df['POI_modeled'] = df_battery_pp_meas['POI_no_night']

        #  Calculate DC-corrected for ratio of Weather increased
        clipping_Point_DC_corrected_PVsyst = \
            self.df_Pvsyst.loc[self.df_Pvsyst['DC_corrected_PVsyst_PR'] == 0.0, 'DC_corrected_PVsyst_WA'].max()
        self.df = weather.calculate_DC_Corrected(self.df,
                                         'Meter_Corrected_2',
                                         self.Pstc_KW,
                                         self.Gstc,
                                         self.Temp_Coeff_Pmax,
                                         self.Tcell_typ_avg,
                                         clipping_Point_DC_corrected_PVsyst)

        # Calculate Meter including what is lost due to Availability
        self.df['Meter_&_ava'] = self.ava['Meter_&_ava']
        self.df['Meter_&_ava_&_grid'] = self.df['Meter_&_ava'] + self.df['Grid_loss']

        # Manually fix times of grid caused outages
        self.curtailment_flags = []
        for i, row in self.sensor_OFF.loc[self.sensor_OFF['Var_ID'].str.lower() == "curtailment", :].iterrows():
            # date_list = pd.date_range(start = row['start date'], end = row['end date'], freq = 'h')
            date_list = self.df.loc[row['start date']: row['end date'], :].index
            self.df.loc[date_list, 'Meter_&_ava'] = self.df['Meter_Corrected_2']
            # fix grid_loss and ava_energy_loss
            self.df.loc[date_list, 'Grid_loss'] = self.df['AVA_Energy_loss']
            self.curtailment_flags = self.curtailment_flags + list(date_list)

        # Manually fix times where site is down and it's NOT grid outage
        self.loss_swap_flags = []
        for i, row in self.sensor_OFF.loc[self.sensor_OFF['Var_ID'].str.lower() == "site ava", :].iterrows():
            date_list = self.df.loc[row['start date']: row['end date'], :].index
            # turn grid loss to inv ava
            self.df.loc[date_list, 'Meter_&_ava'] = self.df['Meter_&_ava_&_grid']
            self.df.loc[date_list, 'AVA_Energy_loss'] = self.df['Grid_loss']
            self.loss_swap_flags = self.loss_swap_flags + list(date_list)

        self.df['Grid_loss'] = (self.df['Meter_&_ava_&_grid'] - self.df['Meter_&_ava']).clip(lower=0)
        self.df['AVA_Energy_loss'] = ( self.df['Meter_&_ava'] - self.df['Meter_Corrected_2']).clip(lower=0)
        

    @func_timer
    def __calculate_PR(self):
        # create expected PR value based on monthly average
        # Resample to start of month
        df_IE = self.df_Pvsyst_2_month['PR_IE_P50'].resample('MS').mean()
        df_IE = df_IE.loc[df_IE.index < self.df.index[-1]]
        df_temporary = pd.Series(df_IE[-1], index=[self.df.index[-1]])
        df_IE = df_IE.append(df_temporary).resample('h').pad()

        # estimate AC kwh based on this ratio
        self.df['P_exp_NREL'] = self.df['DC_corrected'] * df_IE
        self.df.loc[self.df['P_exp_NREL'] > self.clipping_KW, 'P_exp_NREL'] = self.clipping_KW

        # kill ava == 0 spikes on snow days
        self.df.loc[(self.ava['AVA'] == 0) &
            (self.df_sensor_ON[self.pos_Inv] == True).any(axis=1) &
            self.df.index.isin(self.snow_times) &
            (~self.df.index.isin(self.loss_swap_flags)) &
            (self.df['Meter_&_ava'] > self.df['Meter_Corrected_2']), 'Meter_&_ava'] = self.df['Meter_Corrected_2']
        self.df['Meter_&_ava_&_grid'] = self.df['Meter_&_ava'] + self.df['Grid_loss']

        # remove meter adjustments from PR calculation 10/18/16
        # Keep times where meter == inverter sum
        self.Meter_delta[(self.Meter_delta != 0) & (self.df['Meter_Corrected_2'] == self.ava['Inv_sum'])] = 0

        # remove individual meter corrections
        self.df.loc[(self.Meter_delta != 0), ['DC_corrected_PR', 'Gen_NO_Clipping']] = 0

        # remove draker correction
        self.df.loc[self.draker_flags, ['DC_corrected_PR', 'Gen_NO_Clipping']] = 0

        # remove times designated as curtailment in config file
        self.df.loc[self.curtailment_flags, ['DC_corrected_PR', 'Gen_NO_Clipping']] = 0
        
        # Remove when temperature data is invalid
        self.df.loc[(self.df_sensor_ON[self.pos_Temperature] != True).all(axis=1), ['DC_corrected_PR', 'Gen_NO_Clipping']] = 0


    @func_timer
    def __calculate_losses(self):
        self.df['Meter_losses&snow'] = self.df['Meter_&_ava_&_grid']
        self.df.loc[self.snow_times, 'Meter_losses&snow'] = self.P_exp
        self.df.loc[self.df['Meter_losses&snow'] < self.df['Meter_&_ava_&_grid'], 'Meter_losses&snow'] = self.df['Meter_&_ava_&_grid']
        self.df['snow_losses'] = self.df['Meter_losses&snow'] - self.df['Meter_&_ava_&_grid']
        self.df['Meter_losses&snow'] = self.df['Meter_losses&snow'].astype(float)

        # Calculate losses df
        self.losses = self.df[['Meter_Corrected_2']].copy()
        self.losses.loc[:, 'Inv_losses'] = self.df.loc[:, 'Meter_&_ava'] - self.df.loc[:, 'Meter_Corrected_2']
        self.losses.loc[:, 'Grid_losses'] = self.df.loc[:, 'Meter_&_ava_&_grid'] - self.df.loc[:, 'Meter_&_ava']
        self.losses.loc[:, 'Snow_losses'] = self.df.loc[:, 'Meter_losses&snow'] - self.df.loc[:, 'Meter_&_ava_&_grid']


    @func_timer
    def __calculate_revenue(self, method):
        def initial_hourly():
            self.rates_year_i = self.df_Pvsyst_2['Rates'][self.df.index[0]:self.df.index[-1]]
            flat_year_i = self.df_Pvsyst_2['Flat'][self.df.index[0]:self.df.index[-1]]
            self.df['Rates'] = self.rates_year_i
            self.df['Energy_Peak'] = self.df_Pvsyst_2['Energy_Peak']
            self.df['Capacity_Peak'] = self.df_Pvsyst_2['Capacity_Peak']
            self.df['Meter_Corrected_2_rev'] = (self.rates_year_i * self.df['Meter_Corrected_2']) + flat_year_i
            self.df['Meter_&_ava_rev'] = (self.rates_year_i * self.df['Meter_&_ava']) + flat_year_i
            self.df['Meter_&_ava_&_grid_rev'] = (self.rates_year_i * self.df['Meter_&_ava_&_grid']) + flat_year_i
            self.df['Meter_losses&snow_rev'] = (self.rates_year_i * self.df['Meter_losses&snow']) + flat_year_i
            self.df['POI_Corrected_2_rev'] = (self.rates_year_i * self.df['POI_Corrected_2']) + flat_year_i
            self.df['POI_modeled_rev'] = (self.rates_year_i * self.df['POI_modeled']) + flat_year_i

        def weather_adjusted_monthly():
            #  Calculate Revenue.
            #  With the NREL method, Revenue due to Weather is calculated with monthly %
            #
            self.df_Pvsyst_2_month['Revenue_IE_P50_days_adj'] = \
                self.df_Pvsyst_2_month['Revenue_IE_POI'].multiply(self.df_Pvsyst_2_month['%_days_month'], axis="index")

            #  Adjust Weather Revenue
            self.df_Pvsyst_2_month['Revenue_IE_P50_days_adj_&_Weather'] = \
                self.df_Pvsyst_2_month['Revenue_IE_P50_days_adj'].multiply(self.df_Pvsyst_2_month['NREL_Weather_Adj_%'], axis="index")

            # make solar version as well
            self.df_Pvsyst_2_month['Revenue_IE_meterOnly_days_adj'] = \
                self.df_Pvsyst_2_month['Revenue_IE_P50'].multiply(
                    self.df_Pvsyst_2_month['%_days_month'], axis="index").multiply(
                        self.df_Pvsyst_2_month['NREL_Weather_Adj_%'], axis="index")
                    
        if method == 'initial':
            initial_hourly()
        if method == 'weather_adjusted':
            weather_adjusted_monthly()

        # TODO: battery POI/meter swap
        if self.Battery_AC_site:
            self.df['POI_kWH'] = self.df['POI_Corrected_2']
            self.df['POI_rev'] = self.df['POI_Corrected_2_rev']

        else:
            self.df['POI_kWH'] = self.df['Meter_Corrected_2']
            self.df['POI_rev'] = self.df['Meter_Corrected_2_rev']
            

    @func_timer
    def __calculate_weather_adjustments(self):
        #  Count Days per month showing in Power Track
        day_points_full_year = self.df_Pvsyst['POA (W/m2)'].resample('M').count() / 24.0

        # find the % of the month measured in df, based on POA data per hour
        # Calculate average POA for each month
        aux_pivot = pd.pivot_table(self.df_Pvsyst,
                                    values='POA (W/m2)',
                                    index='Hour',
                                    columns='Month',
                                    aggfunc=np.mean)
        # Calculate total POA for each month
        aux_pivot_sum = pd.pivot_table(self.df_Pvsyst,
                                        values='POA (W/m2)',
                                        index='Month',
                                        aggfunc=np.sum)
        aux_percent = aux_pivot.copy()

        aux_percent = aux_pivot.div(pd.Series(aux_pivot_sum.T.values[0], index=aux_pivot.columns).replace(0, np.nan), axis=1)
        
        # Unpivot dataframe
        stack = aux_percent.T.stack().reset_index().rename(columns={'level_0': 'Month', 0: 'percent_month'})

        # create frame to merge with. Has correct index column which is important
        df_input_index = self.df.index
        df_aux = pd.DataFrame({'Month': df_input_index.month,
                               'Hour': df_input_index.hour},
                                index=df_input_index)
        df_aux['timestamp'] = df_aux.index

        df_merged = pd.merge(df_aux, stack, on=['Month', 'Hour'])
        df_merged.set_index('timestamp', drop=True, inplace=True)

        self.df['percent_month'] = df_merged['percent_month']
        aux_temp = pd.concat([self.df['percent_month'], self.df_Pvsyst], axis=1).fillna(0)

        self.df_Pvsyst_2_month['%_days_month'] = aux_temp['percent_month'].resample('m').sum()

        self.df_Pvsyst_2_month['KWh_adj_by_days'] = \
            self.df_Pvsyst_2_month['Year 0 Actual Production (kWh)'].multiply(self.df_Pvsyst_2_month['%_days_month'])

        # -->  NREL  Weather adjusted needs DC_Corrected once the Meter is corrected in Ava functions.
        #
        #  There is a problem when all values are  = 0 and the Meter corrected is corrected with PVsyst values.
        #  the Weather adjusted function does not capture this effect, and therefore the Plant Performance is
        # higher than it should be.  We corrected reducing the number of days in the month.
        #
        # 09/16/2016  added >15 to fix Happy Solar issue.  Meter is positive at night.
        #
        aux_correction = \
            self.df[(self.df['DC_corrected_WA'] == 0) & (self.df['Meter_Corrected_2'] > 15) & (self.df['Grid_loss'] == 0)]['Meter_Corrected_2']
        aux_correction_2 = aux_correction.resample('M').count() / 12.0  # Sunny days are considered 12 h
        aux_correction_2_percentage = \
            pd.concat([day_points_full_year, aux_correction_2], axis=1)
        aux_correction_2_percentage = \
            aux_correction_2_percentage['Meter_Corrected_2'].div(aux_correction_2_percentage['POA (W/m2)'].replace(0, np.nan)).fillna(0)

        #  To correct Weather adjusted values.  There is an issue when the Grid loss gets corrected
        #   PVsyst % values need to increase to move up weather % and lower Plant Performance
        #  See Kenansville 2 Solar Farm,  Month = April
        aux_correction_11 = self.df[(self.df['DC_corrected_WA'] == 0) & (self.df['Grid_loss'] > 0)]['Meter_Corrected_2']
        aux_correction_22 = aux_correction_11.resample('M').count() / 12  # Sunny days are considered 12 h
        aux_correction_22_percentage = pd.concat([day_points_full_year, aux_correction_22], axis=1)
        aux_correction_22_percentage = \
            aux_correction_22_percentage['Meter_Corrected_2'].div(aux_correction_22_percentage['POA (W/m2)'].replace(0, np.nan)).fillna(0)

        filtered_flags = [x for x in self.loss_swap_flags if self.df.loc[x, 'DC_corrected_WA'] == 0]
        ls = list(aux_correction.index) + list(aux_correction_11.index) + filtered_flags

        new_correction = \
            1 - (self.df.loc[ls, 'Meter_losses&snow'].resample('m').sum().fillna(0) / self.df['Meter_losses&snow'].resample('m').sum())
        aux_weather_k = \
            pd.concat([self.df_Pvsyst_2_month[u'POA (W/m2)'], new_correction], axis=1).fillna(1).iloc[:, 1]
        self.aux_new_k = aux_weather_k * self.df_Pvsyst_2_month['%_days_month']
        #  By doing this, all the Revenue gets changed.  NOt correct!

        aux_WA_PVsyst = pd.DataFrame()
        aux_WA_PVsyst['DC_corrected_PVsyst_WA'] = \
            self.df_Pvsyst_2_month['DC_corrected_PVsyst_WA'].multiply(self.aux_new_k)
        #
        aux_WA_measured = self.df['DC_corrected_WA'].resample('M').sum()
        aux_WA = pd.concat([aux_WA_PVsyst, aux_WA_measured], axis=1).fillna(0)
        self.df_Pvsyst_2_month['NREL_Weather_Adj_%'] = \
            aux_WA['DC_corrected_WA'].div(aux_WA['DC_corrected_PVsyst_WA'].replace(0, np.nan)).fillna(0)

        # ASTM
        P_exp_month = self.P_exp.resample('M').sum()
        #
        self.df_Pvsyst_2_month['ASTM_Weather_Adj_%'] = P_exp_month.div(self.df_Pvsyst_2_month['KWh_adj_by_days'].replace(0, np.nan)).fillna(0)
        # POA Ratios
        self.df_Pvsyst_2_month['POA_adj_by_days'] = self.df_Pvsyst_2_month['POA (W/m2)'].multiply(self.aux_new_k)
        self.df_Pvsyst_2_month['GHI_adj_by_days'] = self.df_Pvsyst_2_month['GHI (W/m2)'].multiply(self.aux_new_k)
        #
        self.POA_month = self.df['POA_avg'].resample('M').sum()
        #
        self.df_Pvsyst_2_month['POA_%'] = self.POA_month.div(self.df_Pvsyst_2_month['POA_adj_by_days'].replace(0, np.nan)).fillna(0)
        self.df_Pvsyst_2_month['GHI_%'] = self.df['GHI_avg'].resample('M').sum().div(self.df_Pvsyst_2_month['GHI_adj_by_days'].replace(0, np.nan)).fillna(0)


    @func_timer
    def __calculate_dashboard_percentages(self):
        # Create Monthly Dataframes
        df = self.df.astype(float)
        self.df_month = df.resample('M').sum()

        #  Calculate Plant PR
        self.df_month['PR_Plant'] = self.df_month['Gen_NO_Clipping'].div(self.df_month['DC_corrected_PR'].replace(0, np.nan), axis="index")

        self.df_month_2 = pd.DataFrame(index=self.df_Pvsyst_2_month.index)
        self.df_month_2 = pd.concat([self.df_month_2, self.df_month], axis=1).fillna(0)
        pvsyst_var = ['KWh_adj_by_days', 'NREL_Weather_Adj_%',
                    'Revenue_IE_P50_days_adj', 'Revenue_IE_P50_days_adj_&_Weather']
        self.df_month_2[pvsyst_var] = self.df_Pvsyst_2_month[pvsyst_var]
        self.df_month_2['Weather_KWh'] = self.df_month_2['KWh_adj_by_days'].multiply(self.df_month_2['NREL_Weather_Adj_%'])

        #  Calculate Percentages
        self.df_month_2['Inv_Ava_%'] = self.df_month_2['Meter_Corrected_2'].div(self.df_month_2['Meter_&_ava'].replace(0, np.nan)).fillna(1)
        self.df_month_2['Grid_Ava_%'] = self.df_month_2['Meter_&_ava'].div(self.df_month_2['Meter_&_ava_&_grid'].replace(0, np.nan)).fillna(1)
        self.df_month_2['Snow_Adj_%'] = self.df_month_2['Meter_&_ava_&_grid'].div(self.df_month_2['Meter_losses&snow'].replace(0, np.nan)).fillna(1)
        self.df_month_2['Plant_Perf_%'] = self.df_month_2['Meter_losses&snow'].div(self.df_month_2['Weather_KWh'].replace(0, np.nan)).fillna(0).replace(np.inf, 1).replace(-np.inf, 1)
        self.df_month_2['diff_PR_%'] = self.df_month_2['PR_Plant'] - self.df_Pvsyst_2_month['PR_IE_P50_PR']
        self.df_month_2['Project_IPR_%'] = self.df_month_2['POI_kWH'].div(self.df_Pvsyst_2_month['KWh_adj_by_days'].replace(0, np.nan)).fillna(0)

        #  modified on 2016/09/22 to eliminate the effect of Grid Ava on OPR.  OPR should not include Gri
        self.df_month_2['Project_OPR_%'] = self.df_month_2['Project_IPR_%'].div((self.df_Pvsyst_2_month['POA_%'] * self.df_month_2['Grid_Ava_%']).replace(0, np.nan)).fillna(0).replace(np.inf, 0).replace(-np.inf, 0)
        self.df_month_2['Project_OPR_Temp_%'] = self.df_month_2['PR_Plant'].div(self.df_Pvsyst_2_month['PR_IE_P50_PR']).fillna(0)

        self.df_month_2['AC_batt_eff_%'] = self.df_month_2['POI_kWH'].div(self.df_month_2['Meter_Corrected_2'].replace(0, np.nan))
        self.df_Pvsyst_2_month['IE_AC_batt_eff_%'] = self.df_Pvsyst_2_month['POI Output (kWh)'].div(self.df_Pvsyst_2_month['Year 0 Actual Production (kWh)'].replace(0, np.nan))
        self.df_month_2['AC_batt_eff_index_%'] = self.df_month_2['AC_batt_eff_%'].div(self.df_Pvsyst_2_month['IE_AC_batt_eff_%'].replace(0, np.nan))

        self.df_month_2['AC_batt_rev_gain'] = self.df_month_2['POI_rev'].div(self.df_month_2['Meter_Corrected_2_rev'].replace(0, np.nan)).fillna(1)
        self.df_Pvsyst_2_month['IE_AC_batt_rev_gain'] = self.df_Pvsyst_2_month['Revenue_IE_P50_days_adj_&_Weather'].div(self.df_Pvsyst_2_month['Revenue_IE_meterOnly_days_adj'].replace(0, np.nan)).fillna(1)
        self.df_month_2['AC_batt_rev_index_%'] = self.df_month_2['AC_batt_rev_gain'].div(self.df_Pvsyst_2_month['IE_AC_batt_rev_gain'].replace(0, np.nan)).fillna(1)

        self.df_month_2['Modeled_AC_batt_rev_gain'] = self.df_month_2['POI_modeled_rev'].div(self.df_month_2['Meter_Corrected_2_rev'].replace(0, np.nan)).fillna(1)
        self.df_month_2['Modeled_AC_batt_rev_index_%'] = self.df_month_2['Modeled_AC_batt_rev_gain'].div(self.df_Pvsyst_2_month['IE_AC_batt_rev_gain']).replace(0, np.nan).fillna(1)

        self.df_month_2['Modeled_AC_rev_target'] = self.df_month_2['POI_rev'].div(self.df_month_2['POI_modeled_rev'].replace(0, np.nan))

        #  Calculate Revenue Differences
        self.df_month_2['diff_weather_$'] = \
            self.df_Pvsyst_2_month['Revenue_IE_P50_days_adj_&_Weather'] - self.df_Pvsyst_2_month['Revenue_IE_P50_days_adj']

        self.df_month_2['diff_Inv_ava_$'] = \
            (self.df_month_2['Meter_Corrected_2_rev'] - self.df_month_2['Meter_&_ava_rev']).multiply(self.df_Pvsyst_2_month['IE_AC_batt_rev_gain'])
        self.df_month_2['diff_Grid_ava_$'] = \
            (self.df_month_2['Meter_&_ava_rev'] - self.df_month_2['Meter_&_ava_&_grid_rev']).multiply(self.df_Pvsyst_2_month['IE_AC_batt_rev_gain'])

        self.df_month_2['diff_snow_$'] = \
            (self.df_month_2['Meter_&_ava_&_grid_rev'] - self.df_month_2['Meter_losses&snow_rev']).multiply(self.df_Pvsyst_2_month['IE_AC_batt_rev_gain'])
        self.df_month_2['diff_AC_batt_$'] = \
            (self.df_month_2['POI_rev'] - self.df_month_2['Meter_Corrected_2_rev']) - \
                (self.df_Pvsyst_2_month['Revenue_IE_P50_days_adj_&_Weather'] - self.df_Pvsyst_2_month['Revenue_IE_meterOnly_days_adj'])

        self.df_month_2['diff_Plant_Perf_$'] = \
            (self.df_month_2['POI_rev'] - self.df_month_2[
                ['diff_snow_$', 'diff_Grid_ava_$', 'diff_Inv_ava_$', 'diff_AC_batt_$']
                    ].sum(axis=1)) - self.df_Pvsyst_2_month['Revenue_IE_P50_days_adj_&_Weather']

        self.df_month_2['diff_all_$'] = self.df_month_2['POI_rev'] -  self.df_Pvsyst_2_month['Revenue_IE_P50_days_adj']

        old_cum = self.df_Meter_ORIGINAL.iloc[:, np.arange(len(self.pos_Meter),
                                                           len(self.pos_Meter) + len(self.pos_Meter_Cum))
                                              ].sum(axis=1)
        old_cum = old_cum[old_cum != 0]
        self.df_month_2['AE_Meter'] = old_cum.resample('M').last() - old_cum.resample('M').first()

        day_points = self.df['POA_avg'].resample('M').count() / 24.0
        self.df_month_2 = pd.concat([self.df_month_2, day_points.rename('Days_counted')], axis=1).fillna(0)
        self.df_month_2['AC_Capacity_%'] = self.df_month_2['POI_kWH'] / (self.clipping_KW * 24 * self.df_month_2['Days_counted'])
        self.df_month_2['DC_Capacity_%'] = self.df_month_2['POI_kWH'] / (self.Pstc_KW * 24 * self.df_month_2['Days_counted'])

        # Calculate probability as a normal distribution
        # x=measured; loc=mean; scale = standard deviation
        self.df_month_2['Monthly Probability of Exceedence'] = \
            sct.norm.sf(x=self.df_Pvsyst_2_month['GHI_%'] * self.df_Pvsyst_2_month['GHI_adj_by_days'],
                        loc=self.df_Pvsyst_2_month['GHI_adj_by_days'],
                        scale=self.df_Pvsyst_2_month['GHI_adj_by_days'] * .10)

        # comparing poa-weighted tcell against 8760 equivalent
        # and calculating non-temperature-adjusted PRs
        df['DC_corrected_PR_notemp'] = 0
        # exclude times when DC_corrected_PR has been filtered (ie, equals zero)
        df.loc[df['DC_corrected_PR'] != 0, 'DC_corrected_PR_notemp'] = self.Pstc_KW * (df['POA_avg'] / self.Gstc)

        self.df_month_2['PR_notemp'] = np.nan
        self.df_month_2.loc[df['POA_avg'].resample('m').count().index, 'PR_notemp'] = \
            df['Gen_NO_Clipping'].resample('m').sum() / df['DC_corrected_PR_notemp'].resample('m').sum()

        aux = df['POA_avg'] * df['Tcell']
        self.df_month_2['POA_weighted_Tcell'] = aux.resample('m').sum() / df['POA_avg'].resample('m').sum()
        self.df_Pvsyst['DC_corrected_PVsyst_PR_notemp'] = 0

        # exclude times when DC_corrected_PVsyst_PR has been filtered (ie, equals zero)
        self.df_Pvsyst.loc[self.df_Pvsyst['DC_corrected_PVsyst_PR'] != 0,
                    'DC_corrected_PVsyst_PR_notemp'] = self.Pstc_KW * (self.df_Pvsyst['POA (W/m2)'] / self.Gstc)

        self.df_Pvsyst_2_month['Pvsyst_PR_notemp'] = \
            self.df_Pvsyst['Gen_NO_Clipping_PVsyst'].resample('m').sum() / self.df_Pvsyst['DC_corrected_PVsyst_PR_notemp'].resample('m').sum()

        aux = self.df_Pvsyst['POA (W/m2)'] * self.df_Pvsyst['Tcell']
        self.df_Pvsyst_2_month['Pvsyst_POA_weighted_Tcell'] = \
            aux.resample('m').sum() / self.df_Pvsyst['POA (W/m2)'].resample('m').sum()

        self.df_month_2['OPR_notemp'] = self.df_month_2['PR_notemp'] / self.df_Pvsyst_2_month['Pvsyst_PR_notemp']

        self.df_month_2['ac_battery_flag'] = self.Battery_AC_site * 1

        # Calculate capacity test
        var_meas = ['Meter_Corrected_2', 'POA_avg', 'Wind_speed', 'Tamb_avg']
        df_meas, df_meas_RC = weather.generate_linear_coeff_table_v2(self.df[var_meas], var_meas, self.clipping_KW)
        if not df_meas.empty:
            # prep columns
            self.df_coef.columns = [int(x) for x in self.df_coef.columns]
            df_meas.columns = [int(x) for x in df_meas.columns]
            df_meas_RC.columns = [int(x) for x in df_meas_RC.columns]
            # prep for dataframe math
            self.df_coef = self.df_coef[df_meas.columns.tolist()].T
            df_meas = df_meas.T
            df_meas_RC = df_meas_RC.T
            # find scores
            aux_meas = df_meas_RC['POA']*(df_meas['E']+df_meas['E2']*df_meas_RC['POA'] +
                                        df_meas['ET']*df_meas_RC['T']+df_meas['Ev']*df_meas_RC['Wind'])
            aux_ie = df_meas_RC['POA']*(self.df_coef['E']+self.df_coef['E2']*df_meas_RC['POA'] +
                                        self.df_coef['ET']*df_meas_RC['T']+self.df_coef['Ev']*df_meas_RC['Wind'])
            capacity_scores = pd.DataFrame((aux_meas / aux_ie).values, index=self.df_month.index, columns=['Capacity_result'])
        else:
            capacity_scores = pd.DataFrame([], index=self.df_month.index, columns=['Capacity_result'])
        self.df_month_2['Capacity_result'] = capacity_scores

    
    @func_timer
    def __verify_performance(self):
        self.df_month_2['Perf_Test_Pass'] = 1
        guarantee_id = self.df_proj_keys['Guarantee_ID']
        self.df_perf = \
            pd.DataFrame([], columns=['Guar_freq', 'Gaur_range', 'USB1', 'kwh_guar',
                                      'kwh_pro', 'usb_years', 'kwh_pro_deg', 'kwh_meas',
                                      'kwh_meas_poa', 'kwh_meas_ghi', 'USB1_target',
                                      'USB_result', 'REGIONS', 'reg_IPR', 'reg_OPR',
                                      'reg_target', 'reg_result', 'SOL', 'sol_IPR_weather',
                                      'sol_target', 'sol_result', 'IDP', 'IDP_mechanical_ava',
                                      'IDP_target_ava', 'IDP_pass', 'SCEG', 'SCEG_kwh_guar',
                                      'SCEG_kwh_guar_grid_85_proration', 'SCEG_kwh_measured',
                                      'SCEG_kwh_proration_factor', 'SCEG_perf_guar_result'])

        if str(guarantee_id) != "nan":
            if guarantee_id == "USB1":
                guarantee_input = float(self.df_proj_keys['Guarantee_input'])
                self.df_perf, guarantee_result = perf.USB1_performance_guarantee(self.df,
                                                                       len(self.df_month),
                                                                       self.df_Pvsyst,
                                                                       self.PIS_date,
                                                                       guarantee_input,
                                                                       self.df_perf)
            elif guarantee_id == 'SCEG':
                self.df_perf, guarantee_result = perf.SCEG_performance_guarantee(self.project_name,
                                                                       self.df,
                                                                       self.df_Pvsyst,
                                                                       self.PIS_date,
                                                                       self.df_perf)
            elif guarantee_id == "Regions_OPR":
                guarantee_input = pd.to_datetime(self.df_proj_keys['Guarantee_input'])
                self.df_perf, guarantee_result = perf.Regions_performance_guarantee(self.df,
                                                                          self.df_month_2,
                                                                          self.df_Pvsyst,
                                                                          self.df_Pvsyst_2_month,
                                                                          guarantee_input,
                                                                          self.df_perf)
            elif guarantee_id == "Sol_OPR":
                self.df_perf, guarantee_result = perf.Sol_performance_guarantee(self.df_month_2,
                                                                      self.df_Pvsyst_2_month,
                                                                      self.df_perf)
            elif guarantee_id == "IDP_MAG":
                self.df_perf, guarantee_result = perf.IDP_performance_guarantee(self.ava, self.df_perf)
            else:
                raise RuntimeError("Unknown Guarantee ID for " + self.project_name + ": " + guarantee_id)
            self.df_month_2['Perf_Test_Pass'] = guarantee_result
        self.df_perf = self.df_perf.fillna('')

        # curtailed sites will have their PP unfairly decreased, so we move the losses to grid availability
        for i, row in self.sensor_OFF.query('Var_ID == "grid"').iterrows():
            s = row['start date']
            e = row['end date']
            print(e)
            if e == -1:
                e = self.df_month_2.index[-1]
            e = e.to_period('M').to_timestamp('M')

            # generate all months between start and end -- dates look like '2017-01-31' (end of month) to match self.df_month_2.index
            curtailment_dates = pd.date_range(start=s, end=e, freq='M')
            for date in self.df_month_2.index:
                if date in curtailment_dates:
                    print("using curtailment for the month of", date)
                    self.df_month_2.loc[date, 'Grid_Ava_%'] = \
                        self.df_month_2.loc[date, 'Grid_Ava_%'] + (self.df_month_2.loc[date, 'Plant_Perf_%'] - 1)
                    self.df_month_2.loc[date, 'Plant_Perf_%'] = 1
                    self.df_month_2.loc[date, 'diff_Grid_ava_$'] = \
                        self.df_month_2.loc[date, 'diff_Grid_ava_$'] + self.df_month_2.loc[date, 'diff_Plant_Perf_$']
                    self.df_month_2.loc[date, 'diff_Plant_Perf_$'] = 0

    
    @func_timer
    def __calculate_project_metrics(self):
        var_col = ['Wind_speed', 'Meter', 'Meter_cum', 'POA_avg', 'Tmod_avg', 'Tamb_avg',
                   'Tcell_AMB', 'Tcell_MOD', 'Tcell', 'DC_corrected', 'DC_corrected_PR',
                   'DC_corrected_WA', 'Gen_NO_Clipping', 'AVA_Energy_loss', 'Grid_loss',
                   'Meter_cum_corrected_2', 'Meter_Corrected_2', 'Meter_&_ava',
                   'Meter_&_ava_&_grid', 'Rates', 'Meter_Corrected_2_rev', 'Meter_&_ava_rev',
                   'Meter_&_ava_&_grid_rev', 'PR_Plant', 'KWh_adj_by_days', 'NREL_Weather_Adj_%',
                   'Revenue_IE_P50_days_adj', 'Revenue_IE_P50_days_adj_&_Weather', 'Weather_KWh',
                   'Inv_Ava_%', 'Grid_Ava_%', 'Plant_Perf_%', 'diff_PR_%', 'Project_IPR_%',
                   'Project_OPR_%', 'Project_OPR_Temp_%', 'diff_Inv_ava_$', 'diff_Grid_ava_$',
                   'diff_weather_$', 'diff_Plant_Perf_$', 'diff_all_$', 'AE_Meter',
                   'AC_Capacity_%', 'DC_Capacity_%', 'Monthly Probability of Exceedence',
                   'Perf_Test_Pass', 'Capacity_result', 'Snow_Adj_%', 'diff_snow_$',
                   'POA_weighted_Tcell', 'AC_batt_eff_%', 'AC_batt_eff_index_%',
                   'AC_batt_rev_gain', 'AC_batt_rev_index_%', 'diff_AC_batt_$',
                   'POI_Corrected_2', 'POI_rev', 'ac_battery_flag', 'Modeled_AC_batt_rev_gain',
                   'Modeled_AC_batt_rev_index_%', 'Modeled_AC_rev_target', 'OM_uptime']

        # Calculate OM uptime
        # Create average POA data in case of grid outage
        # Replaced ava.AVA with ava.OM_Uptime
        aux = pd.concat([self.df[['Meter_Corrected_2',
                                  'Meter_&_ava',
                                  'Meter_&_ava_&_grid',
                                  'Meter_losses&snow',
                                  'POA_avg',
                                  'percent_month']],
                         self.ava['OM_Uptime']], axis=1)
        aux['month'] = aux.index.month
        aux['ind'] = aux.index

        multiply = self.df_Pvsyst_2_month[['POA (W/m2)']]
        multiply['month'] = multiply.index.month

        aux2 = pd.merge(aux, multiply, on='month').set_index('ind', drop=True)

        aux2.index.name = None
        aux2['estimated_POA'] = aux2['POA (W/m2)'] * aux2['percent_month']

        # when POA data is not available, use estimate data
        aux2.loc[~(self.df_sensor_ON[self.pos_POA] == True).any(axis=1), 'POA_avg'] = aux2['estimated_POA']

        # filter and calculate uptime
        aux3 = aux2.copy()

        # Filter out config grid outage
        aux3 = aux3.loc[~aux3.index.isin(self.curtailment_flags), :]

        # filtered out grid outage
        aux3 = aux3.loc[aux3['Meter_&_ava_&_grid'] == aux3['Meter_&_ava'], :]
        aux3 = aux3.loc[aux3['POA_avg'] > 100, :]  # poa filter
        aux3 = aux3.loc[~((aux3['OM_Uptime'] == 0) & (aux3['Meter_&_ava'] == aux3['Meter_Corrected_2'])), :]
        self.df_month_2['OM_uptime'] = aux3['OM_Uptime'].resample('m').mean()
        self.df_month_2['OM_uptime'] = self.df_month_2['OM_uptime'].fillna(1)

        self.df_month_3 = self.df_month_2[var_col].fillna(0)

        #  Calculate Energy generated based on rate
        #  Use NREL Weather adj % to create PVsyst Revenue
        self.df_Pvsyst_2['NREL_Weather_Adj_coef'] = 0
        self.df_Pvsyst_2['NREL_Weather_Adj_days_%'] = 0

        for mh in range(1, 13):
            self.df_Pvsyst_2.loc[self.df_Pvsyst.index.month == mh,
                            'NREL_Weather_Adj_coef'] = self.df_Pvsyst_2_month['NREL_Weather_Adj_%'].values[mh-1]
            self.df_Pvsyst_2.loc[self.df_Pvsyst.index.month == mh,
                            'NREL_Weather_Adj_days_%'] = self.df_Pvsyst_2_month['%_days_month'].values[mh-1]

        self.df_Pvsyst_2['NREL_Weather_Adj_Kwh'] = self.df_Pvsyst_2['NREL_Weather_Adj_days_%'].multiply(
            self.df_Pvsyst_2['Year 0 Actual Production (kWh)'])

        # Added flat payments/fees
        self.df_Pvsyst_2['NREL_Weather_Adj_Kwh_$'] = \
            self.df_Pvsyst_2['NREL_Weather_Adj_Kwh'].multiply(self.df_Pvsyst_2['Rates'], axis="index") + self.df_Pvsyst_2['Flat']

        if self.normal_rate_flag:  # are you using normal 3 price rate, or custom 8760 rate?
            self.table_gen = \
                rate_table.generate_table_variable_by_rev_schedule_v02(self.rates_year_i,
                                                            self.df,
                                                            'POI_kWH',
                                                            self.df_Pvsyst_2,
                                                            'NREL_Weather_Adj_Kwh',
                                                            self.df_config,
                                                            self.df_month_2,
                                                            self.df_Pvsyst_2_month)
            self.table_rev = \
                rate_table.generate_table_variable_by_rev_schedule_v02(self.rates_year_i,
                                                            self.df,
                                                            'POI_rev',
                                                            self.df_Pvsyst_2,
                                                            'NREL_Weather_Adj_Kwh_$',
                                                            self.df_config,
                                                            self.df_month_2,
                                                            self.df_Pvsyst_2_month)
        else:
            self.table_gen = pd.DataFrame(np.zeros([12, 6]), index=self.df_Pvsyst_2_month.index)
            self.table_rev = self.table_gen

        # Post SC Date correction
        # 10/26/16 create an 1 or 0 if after the SC date. Used for reporting
        self.df_Pvsyst_2_month['Post SC Date'] = 0
        self.df_Pvsyst_2_month.loc[(self.df_Pvsyst_2_month.index > self.SC_Date + pd.offsets.MonthEnd(0)), 'Post SC Date'] = 1
        self.df_Pvsyst_2_month['Model_Irradiance_Index'] = \
            (self.df_Pvsyst_2_month['POA_%'] / self.df_Pvsyst_2_month['GHI_%']).replace(np.inf, 0).fillna(0)

        # correct the column ordering
        col_reorder = ['Holiday', 'month', 'DST', 'weekday', 'Peak_day', 'ON_Peak', 'Summer', 'Energy_Peak',
                    'Capacity_Peak', 'Rates', 'Flat', u'POA (W/m2)', u'GHI (W/m2)', 'kWh_ORIGINAL',
                    u'Year 0 Actual Production (kWh)', 'DC_corrected_PVsyst', 'DC_corrected_PVsyst_PR',
                    'DC_corrected_PVsyst_WA', 'Gen_NO_Clipping_PVsyst', 'Revenue_IE_P50', 'Blended_Rate',
                    'PR_IE_P50', 'PR_IE_P50_PR', '%_days_month', 'KWh_adj_by_days', 'NREL_Weather_Adj_%',
                    'ASTM_Weather_Adj_%', 'POA_adj_by_days', 'GHI_adj_by_days', 'POA_%', 'GHI_%',
                    'Revenue_IE_P50_days_adj', 'Revenue_IE_P50_days_adj_&_Weather', 'Post SC Date',
                    'Model_Irradiance_Index', 'POA_weighted_Tcell', 'Pvsyst_PR_notemp', 'Pvsyst_POA_weighted_Tcell',
                    'IE_AC_batt_eff_%', 'IE_AC_batt_rev_gain', 'Revenue_IE_POI', 'POI_ORIGINAL', 'POI Output (kWh)']

        self.df_Pvsyst_2_month = self.df_Pvsyst_2_month[col_reorder]

        #    SEND TO EXCEL

        # ---------------
        #  Send day values
        df_d = self.df.resample('D').sum()
        var_col = ['POA_avg', 'POI_kWH', 'Meter_cum_corrected_2']
        #
        Prod_adj = self.P_exp
        Prod_adj_day = Prod_adj.resample('D').sum()

        # measured NREL PR
        NREL_OPR_day = pd.DataFrame(self.df[['Gen_NO_Clipping', 'DC_corrected_PR']]).resample('d').sum()
        NREL_OPR_day['Meas_PR'] = NREL_OPR_day['Gen_NO_Clipping'].div(NREL_OPR_day['DC_corrected_PR'].replace(0, np.nan)).fillna(0)
        # expected NREL PR
        PR_day = pd.DataFrame(self.df_Pvsyst_2_month['PR_IE_P50']).resample('MS').mean()
        aux = pd.DataFrame([PR_day['PR_IE_P50'][-1]], index=[PR_day.index.max() +
                        pd.offsets.MonthEnd()], columns=PR_day.columns)
        PR_day = PR_day.append(aux)
        PR_day = PR_day['PR_IE_P50'].resample('d').pad()

        # Changed due to pandas deprecating `join_axes`
        # NREL_OPR_day = pd.concat([NREL_OPR_day, PR_day], axis=1, join_axes=[df_d.index])
        NREL_OPR_day = pd.concat([NREL_OPR_day, PR_day], axis=1).reindex(df_d.index)

        # Changed due to pandas deprecating `join_axes`
        # self.df_d2 = pd.concat([df_d[var_col], Prod_adj_day, NREL_OPR_day], axis=1, join_axes=[df_d.index])
        self.df_d2 = pd.concat([df_d[var_col], Prod_adj_day, NREL_OPR_day], axis=1).reindex(df_d.index)


        # Diagnostic Metrics
        # NOTE: diagnostic metrics - weather bool ~ weather_prorate; day bool ~ days_month_5
        self.df_Pvsyst_2_month['Weather_prorate'] = self.aux_new_k
        self.df_Pvsyst_2_month['days_month_5'] = self.df_Pvsyst_2_month['%_days_month']
        self.df_Pvsyst_2_month['Nominal_Noclip_Weather_Adj'] = \
            self.df['DC_corrected'].resample('M').sum().div((self.df_Pvsyst_2_month['DC_corrected_PVsyst'].multiply(self.aux_new_k)).replace(0, np.nan)).fillna(0)

        self.df['DC_nominal'] = self.Pstc_KW * self.df['POA_avg']/self.Gstc
        self.df_Pvsyst['DC_nominal_PVsyst'] = self.Pstc_KW * self.df_Pvsyst['POA (W/m2)']/self.Gstc
        self.df_Pvsyst_2_month['Nominal_NoclipNoTemp_Weather_Adj'] = \
            self.df['DC_nominal'].resample('M').sum().div((self.df_Pvsyst['DC_nominal_PVsyst'].resample('M').sum().multiply(self.aux_new_k)).replace(0, np.nan)).fillna(0)

        # clipping effect for measured
        self.df_month_2['measured_clipping_dcimpact'] = \
            self.df['DC_corrected_WA'].resample('M').sum().div(self.df['DC_corrected'].resample('M').sum().replace(0, np.nan)).fillna(1)

        # clipping effect for IE
        self.df_Pvsyst_2_month['ie_clipping_dcimpact'] = \
            self.df_Pvsyst_2_month['DC_corrected_PVsyst_WA'].div(self.df_Pvsyst['DC_corrected_PVsyst'].resample('M').sum().replace(0, np.nan)).fillna(1)

        # ASTM clipping effect for measured
        IE_coef, IE_coef_RC = weather.generate_linear_coeff_table_v3(self.df_Pvsyst, self.var_astm, self.clipping_KW)

        # find empty months
        if not IE_coef.loc[:, IE_coef.sum() == 0].empty:
            aux = IE_coef.loc[:, IE_coef.sum() == 0]
            # find typical values to replace bad ones
            avg = IE_coef.loc[:, IE_coef.sum() != 0].mean(axis=1)

            # edit months that failed
            for col in aux.columns:
                IE_coef.loc[:, col] = avg

        P_astm = weather.create_ASTM_column(self.df, IE_coef)
        self.df_month_2['measured_clipping_astmimpact'] = \
            P_astm.clip(upper=self.clipping_KW).resample('M').sum().div(P_astm.resample('M').sum().replace(0, np.nan)).fillna(1)
        # ASTM measured effect for IE
        TIE_coef = IE_coef.T
        self.df_Pvsyst_2['month'] = self.df_Pvsyst_2.index.month
        aux_pvsyst = pd.merge(self.df_Pvsyst_2, TIE_coef,left_on='month', right_index=True)
        aux_pvsyst['astm'] = aux_pvsyst['POA (W/m2)'] * \
            (aux_pvsyst['E'] + aux_pvsyst['E2']*aux_pvsyst['POA (W/m2)'] +
             aux_pvsyst['ET']*aux_pvsyst['Ambient Temperature'] +
             aux_pvsyst['Ev']*aux_pvsyst['Wind Velocity (m/s)'])
        self.df_Pvsyst_2_month['ie_clipping_astmimpact'] = \
            aux_pvsyst['astm'].clip(upper=self.clipping_KW).resample('M').sum().div(aux_pvsyst['astm'].resample('M').sum().replace(0, np.nan))

        # SPA Night flag, interp at night
        self.df_filt = self.df[['Meter_Corrected_2', 'POA_avg']].copy()
        self.df_filt['interp_check'] = 0

        # choosing conditional value of 10 in arbitrary sense
        # Meter correct 2 interp issues
        self.df_filt.loc[(self.df_filt['Meter_Corrected_2'] > 10) &
                    ((self.df_filt.index.hour < 6) | (self.df_filt.index.hour > 20)), 'interp_check'] = 1
        
        # POA interp issues
        self.df_filt.loc[(self.df_filt['POA_avg'] > 5) & 
                    ((self.df_filt.index.hour < 6) | (self.df_filt.index.hour > 20)), 'interp_check'] = 1
        self.df_filt['Hour Index Copy'] = self.df_filt.index.hour
        self.df_month_2['night_flag'] = self.df_filt['interp_check'].resample('m').sum()+1

        # POI limit/PPA limit flag
        self.df_month_2['poi_limit_flag'] = \
            (self.df['Meter_Corrected_2'] > self.MWAC*1000 * 1.01).astype(float).resample('m').sum()

        # Sensor Diagnostic Test
        # create poa list with only POAs on the site, not imported ones
        pos_POA_native = [x for x in self.pos_Native if 'POA' in x]

        # Keep only real values
        scatter = self.df[pos_POA_native][self.df_sensor_ON[pos_POA_native] == True]

        def slope_check(scatter):
            slope_list = []

            # Column to compare against
            ind = scatter.columns.tolist()[0]
            for poa_native in scatter.columns.tolist():
                if poa_native == 'month':
                    continue

                # remove nans in either col, messes up regression
                aux = scatter.loc[~scatter[[ind, poa_native]].isnull().any(axis=1)]
                if aux.empty:
                    slope_list.append((1, 1))
                else:
                    slope, intercept, r_value, p_value, std_err = sct.linregress(aux[ind], aux[poa_native])
                    slope_list.append((slope, r_value))

            df_slope_values = pd.DataFrame(slope_list, columns=['slope', 'r2'])
            df_slope_values['error'] = df_slope_values['slope'].fillna(1)
            df_slope_values['diff'] = (1-(df_slope_values['error'] - 1).abs()) * df_slope_values['r2']**2

            # using .min() doesn't capture bad values above 1
            return df_slope_values.loc[df_slope_values['diff'].idxmin(), 'error']

        self.df_month_2['POA_regress_flag'] = scatter.resample('M').apply(slope_check)

        # neighbor data
        non_native = [x for x in self.pos_POA + self.pos_Temperature + self.pos_Wind if x not in self.pos_Native]

        # True implies not filtered. If borrowed sensors have any value above 0, then it was used and flags need to be raised
        df_borrowed_sensors = \
            self.df[non_native][self.df_sensor_ON[non_native] == True].fillna(0).resample('M').sum() > 0

        if non_native == []:
            self.df_month_2['borrowed_data'] = ''
            self.df_month_2['nearby_sensor_flag'] = 1

        else:
            df_borrowed_sensors['nearby_sensor_flag'] = 1
            df_borrowed_sensors.loc[df_borrowed_sensors[non_native].any(axis=1), 'nearby_sensor_flag'] = 2
            self.df_month_2['nearby_sensor_flag'] = df_borrowed_sensors['nearby_sensor_flag']

            active = df_borrowed_sensors[non_native]
            df_borrowed_sensors['flag'] = active.apply(lambda row: ";".join(active.columns[row]), axis=1)
            self.df_month_2['borrowed_data'] = df_borrowed_sensors['flag']
            self.df_month_2['borrowed_data'] = self.df_month_2['borrowed_data'].fillna('')

        # inverter cum meter checks
        self.df['inv_cum'] = self.df[self.pos_Inv_cum].sum(axis=1)
        aux = self.df.loc[self.df['inv_cum'] != 0, ['inv_cum', 'Meter_cum_corrected_2']]

        self.df_month_2['inv_cum_check'] = \
            (aux['Meter_cum_corrected_2'].resample('M').last() - 
             aux['Meter_cum_corrected_2'].resample('M').first()
             ).div(aux['inv_cum'].resample('M').last() - aux['inv_cum'].resample('M').first())
        self.df_month_2['inv_cum_check'] = \
        self.df_month_2['inv_cum_check'].replace([np.nan, np.inf, -np.inf], 0) - 1

        # snow paper data
        self.df_month_2['snowfall'] = self.snow_data.resample('m').sum()

        # Remove night & non-data points
        self.df_month_2['snow_coverage_5'] = self.snow_coverage.loc[self.df['POA_avg'] > 5].resample('m').mean()
        self.df_month_2['snow_coverage_energy'] = self.snow_coverage.multiply(self.df.P_exp).resample('m').sum().divide(self.df_month_2['Meter_losses&snow'].replace(0, np.nan))

        # Create OM Summary DF
        OM_POI = self.df_month_2['POI_Corrected_2']
        OM_P50 = self.df_Pvsyst_2_month['POI Output (kWh)']
        OM_Weather_adj = self.df_month_2['NREL_Weather_Adj_%'] * OM_P50
        OM_Production_Diff = (OM_POI-OM_P50)/OM_P50
        OM_Losses = OM_POI*np.nan

        OM_POA = self.POA_month/1000
        OM_POA_P50 = self.df_Pvsyst_2_month['POA (W/m2)']/1000
        OM_POA_Diff = (OM_POA-OM_POA_P50)/OM_POA_P50

        OM_Inv_Ava = self.df_month_2['Inv_Ava_%']
        OM_Ava = self.df_month_2['OM_uptime']
        OM_OPR = self.df_month_2['Project_OPR_Temp_%']
        OM_Batt = self.df_month_2['Modeled_AC_rev_target']

        # added for the waterfall numbers
        OM_IE_P50 = OM_P50
        OM_Weather_adj_kwh = (self.df_month_2['NREL_Weather_Adj_%']-1) * OM_P50
        OM_INV_ava_kwh = self.df_month_2['Meter_Corrected_2'] - self.df_month_2['Meter_&_ava']
        OM_Grid_ava_kwh = self.df_month_2['Meter_&_ava'] - self.df_month_2['Meter_&_ava_&_grid']
        OM_snow_losses_kwh = self.df_month_2['Meter_&_ava_&_grid'] - self.df_month_2['Meter_losses&snow']
        OM_plant_perf_kwh = self.df_month_2['Meter_losses&snow'] - OM_Weather_adj
        OM_Meter_production_kwh = OM_POI
        OM_Losses = OM_Grid_ava_kwh+OM_INV_ava_kwh+OM_snow_losses_kwh
        OM_gap = OM_POI * np.nan

        # added 6.29.2020
        OM_WAP = OM_POI / OM_P50 / self.df_month_2['NREL_Weather_Adj_%']/self.df_month_2['Snow_Adj_%']
        OM_WAP = self.df_month_2['Project_IPR_%'] / self.df_month_2['NREL_Weather_Adj_%']/self.df_month_2['Snow_Adj_%']

        self.OM_data = pd.concat([
            OM_POI, OM_P50, OM_Weather_adj, OM_Production_Diff, OM_Losses, OM_POA,
            OM_POA_P50, OM_POA_Diff, OM_Inv_Ava, OM_Ava, OM_OPR, OM_WAP, OM_Batt,
            OM_gap, OM_IE_P50, OM_Weather_adj_kwh, OM_Grid_ava_kwh, OM_INV_ava_kwh,
            OM_snow_losses_kwh, OM_plant_perf_kwh, OM_Meter_production_kwh], axis=1)
        self.OM_data = self.OM_data.fillna('')

        #ADDED 3/11/2020##################################################################
        self.OM_data.columns = [
            'POI_Corrected_2', 'POI Output (kWh)', 'weather_ad_exp_prod_kwh',
            'ovp_production', 'estimated_loss', 'POA_avg', 'POA (W/m2)',
            'ovp_insolation', 'Inv_Ava_%', 'OM_uptime', 'Project_OPR_Temp_%',
            'Weather_Adjusted_performance', 'Modeled_AC_rev_target', 'POI_Corrected_2',
            'POI Output (kWh)', 'weather_losses_kwh', 'grid_ava_kwh', 'inv_ava_kwh',
            'snow_loss_kwh', 'plant_perf_kwh', 'POI_Corrected_2']

        # get just the necessary columns that aren't already given to O&M
        self.OM_data2 = self.OM_data[[
            'weather_ad_exp_prod_kwh', 'ovp_production', 'estimated_loss',
            'ovp_insolation', 'weather_losses_kwh', 'grid_ava_kwh', 'inv_ava_kwh',
            'snow_loss_kwh', 'plant_perf_kwh']]

    
Project.__annotations__ = {'Gstc': Number,
                           'Battery_AC_site': bool,
                           'Battery_DC_site': bool,
                           'MWAC': Number,
                           'Tracker_site': bool,
                           'colnames_ccr': list,
                           'colnames_das': list,
                           'config_filepath': Union[str, bytes],
                           'config_sheets': dict,
                           'df': DataFrame,
                           'df_Pvsyst': DataFrame,
                           'df_proj_keys': dict,
                           'df_sensor_ON': DataFrame,
                           'last_update_config': float,
                           'last_update_powertrack': float,
                           'lat': Number,
                           'lon': Number,
                           'neighbor_list': list,
                           'neighbor_sensors': set,
                           'processed': bool,
                           'project_directory': Union[str, bytes],
                           'project_name': str}
 