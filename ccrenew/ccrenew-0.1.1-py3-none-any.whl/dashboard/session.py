# -*- coding: utf-8 -*-

from logging_conf import get_logging_config
from datetime import datetime
import logging
import logging.config
from matplotlib.pyplot import waitforbuttonpress
from numbers import Number
import numpy as np
import os
import pandas as pd
from pandas import DataFrame
from pandas.io.sql import SQLTable
import scipy.stats as sct
import shutil
import sys
from typing import Union

from dashboard.data_processing.CCR import (
    all_df_keys,
    file_project,
)
from dashboard.plotting.plots import Plotter
from dashboard.project import Project
import dashboard.utils.dashboard_utils as dbutils
import dashboard.utils.project_neighbors as neighbs
from dashboard.utils.dashboard_utils import func_timer
from dashboard.utils.df_tools import df_update_join

    
# Python 2 compatibility
if sys.version_info.major == 3:
    unicode = str

# suppress warnings about "A value is trying to be set on a copy of a slice from a DataFrame."
pd.options.mode.chained_assignment = None

# Initialize logger
# Get logging configuration from the logging.conf file in the same directory as this file
username = os.getenv('username')
dashboard_folder = file_project
log_filename = '{}_dashboard-{}.log'.format(datetime.now().strftime('%Y-%m-%d_%H-%M-%S'), username)
log_config = os.path.join(dashboard_folder, 'Python_Functions', 'logging.conf')
log_file = os.path.join(dashboard_folder, 'Python_Functions', '_old', 'logs', log_filename)
LOGGING_CONFIG = get_logging_config(log_file)
logging.config.dictConfig(LOGGING_CONFIG)

# Create logger
logger = logging.getLogger(__name__)
logger.info('Beginning Dashboard Session')

def _execute_insert(self, conn, keys, data_iter):
    #print "Using monkey-patched _execute_insert"
    data = [dict((k, v) for k, v in zip(keys, row)) for row in data_iter]
    conn.execute(self.insert_statement().values(data))


SQLTable._execute_insert = _execute_insert

    
class DashboardSession(object):
    """Main orchestrator for processing, plotting, and exporting data for projects (i.e. sites).

    Args:
        project_list (str or list, optional): List of project(s) to initialize. Defaults to None.
        data_cutoff_date (str or datetime, optional): The last date you want to analyze. Defaults to the current date the dashboard is being run.
        data_source (str, optional): The data source to run the dashboard on. Defaults to "AE_data_".

    """

    # Instantiate globals as class variables
    dashboard_dir = file_project
    """Directory for the dashboard project"""
    df_keys = all_df_keys
    """Metadata for all projects"""

    # Site lists
    tracker_sites = ['5840 Buffalo Road', 'Alexis', 'ATOOD II', 'Bar D', 'Barnhill Road Solar', 'Bay Branch',
                     'Bonanza', 'Bovine Solar', 'Bronson', 'Cascade', 'Chisum', 'Copperfield', 'Curie',
                     'Eddy II', 'Gaston II', 'Griffin', 'Grove Solar (NC)', 'Grove', 'Hardison Farm',
                     'Hopewell Friends', 'Hyline', 'IS - 46 Tracker', 'IS 67', 'Lampwick', 'Leggett Solar',
                     'Mars', 'Neff', 'Nimitz', 'Open Range', 'Palmetto Plains', 'Prince George 1',
                     'Prince George 2', 'Railroad', 'Shoe Creek', 'Siler', 'Simba', 'Springfield', 'Sterling',
                     'Thunderegg', 'Vale', 'Wagyu', 'Warren', 'Wendell', 'West Moore II', 'Yellow Jacket']
    """Projects with tracker-type racking"""
    battery_ac_funds = ['LGE']
    """Funds that have projects with AC batteries"""
    battery_ac_sites = df_keys.query("Fund in @battery_ac_funds").index
    """Projects with AC batteries"""
    battery_dc_sites = ['Salt Point', 'Dubois']
    """Projects with DC batteries"""

    def __init__(self,
                 project_list=None,
                 data_cutoff_date=None,
                 data_source='AE_data_',
                 **kwargs):
        self.project_list = project_list
        """List of `Project` objects that have been initialized & added to the `DashboardSession` instance"""
        if not data_cutoff_date:
            self.data_cutoff_date = datetime.today()
        else:
            self.data_cutoff_date = data_cutoff_date
        self.data_source = data_source
        
            
        # Snow dataframe from Smartsheets
        self.raw_snow_df = dbutils.get_snow_df(dashboard_folder, data_source)
        """Snow data pulled from Smartsheets"""

        # Initialize a dict to store projects - key = project name; value = project object
        self.project_list = {}

        # Add projects to the session if provided
        if project_list:
            if isinstance(project_list, (str, unicode, list)):
                self.add_projects(project_list)
            else:
                print('`project_list` must be a string or list. The projects provided were not added to the DashboardSession. Please try again in the initialized DashboardSession.')
        
        # Create list for projects that have errored out
        self.errored_projects = {}

        # Active plotter instance for drawing plots
        self.active_plotter = None

        # List of plotter objects if you want to have multiple going in your session
        self.plotters = {}


    @func_timer
    def add_project(self, project_name, get_neighbors=True):
        """Adds & initializes a project to a `DashboardSession` instance.

        Args:
            project_name (str or Project): The name of the project (i.e. solar site) to add to the `DashboardSession` instance.
            get_neighbors (bool, optional): Flag to add & initialize neighbor projects. Defaults to True.
        """
        # Type validation
        if not isinstance(project_name, (str, unicode, list)):
            raise TypeError("`project_name` must be a string or Python list! Please reformat input and try again.")

        # Determine behavior based on what was passed to method
        if isinstance(project_name, list):
            self.add_projects(project_name)
        elif project_name in self.project_list:
            return
        else:
            try:
                project = self.__initialize_project(project_name, get_neighbors)
                self.project_list[project.project_name] = project
            except RuntimeError as e:
                print(e)
                logger.warn(e)
    

    def add_projects(self, project_list, get_neighbors=True):
        """Calls `add_project` for each project in a list.

        Args:
            project_list (list, str): list of project names to add & initialize to the `DashboardSession` instance.
            get_neighbors (bool, optional): Flag to add & initialize neighbor sites. Defaults to True.
        """
        if isinstance(project_list, (str, unicode)):
            self.add_project(project_list, get_neighbors)

        elif isinstance(project_list, list):
            for project_name in project_list:
                self.add_project(project_name, get_neighbors)
        
        else:
            raise TypeError("`project_list` must be a string or Python list! Please reformat input and try again.")
                

    @func_timer
    def process_project(self, project_name, reprocess=False):
        """Processes data for the given project.

        Args:
            project_name (str, Project, or list): The name of the project to process.
            reprocess (bool, optional): Whether to reprocess the data. This option will likely\
            be uncommon as any changes to a project's config file or powertrack file will\
            automatically reprocess that data. This could be used if any changes are made\
            outside of the config/powertrack file or a change is made to a neighbor. Defaults to False.
        """
        if isinstance(project_name, list):
            self.process_projects(project_name, reprocess)
        elif isinstance(project_name, (str, unicode, Project)):
            # Get project object
            project = self.__get_project(project_name)

            # Pull the last updated dates from the filesystem for the config & Powertrack files
            last_update_config_file = os.path.getmtime(project.config_filepath)
            last_update_powertrack_file = os.path.getmtime(project.powertrack_filepath)

            # Check if the config file or the Powertrack file has been updated.
            # If not we don't need to process.
            if (
                project.last_update_config != last_update_config_file or
                project.last_update_powertrack != last_update_powertrack_file
                ):
                # Pull config and/or Powertrack data
                self.__prepare_source_data(project)
            else:
                if project.processed and not reprocess:
                    print('{} already processed'.format(project.project_name))
                    return True

            # Process data - update neighbor sensors first then process the project
            self.__get_neighbor_sensor_data(project)
            project._process_data(reprocess)
            project.processed = True
            print('{} successfully processed'.format(project.project_name))
        else:
            raise TypeError("`project_name` must be a string or Project object! Please reformat input and try again.")
    
    
    def process_projects(self, project_list, reprocess=False):
        """Calls `process_project` for each project in a list

        Args:
            project_list (list, str, or Project): List of project names of `Project` objects to process.
            reprocess (bool, optional): See `process_project`. Defaults to False.
        """
        if isinstance(project_list, (str, unicode, Project)):
            self.process_project(project_name, reprocess)
        elif isinstance(project_list, list):
            for project_name in project_list:
                self.process_project(project_name, reprocess)
        else:
            raise TypeError("`project_list` must be a string or Python list! Please reformat input and try again.")
    

    def process_all_projects(self):
        """Processes all projects in the `project_list` for the `DashboardSession` instance
        """
        # FIXME: add data cutoff date in here in case you want to change that in the middle of a session
        # FIXME: Same with process project object below
        project_list = self.project_list.keys()
        self.process_projects(project_list)

    
    def __get_project(self, project_name, get_neighbors=True):
        """Returns a project object given a project name.

        Args:
            project_name (str or Project): Project name to add to the `DashboardSession` instance.
            get_neighbors (bool, optional): Flag to add & initialize neighbor projects. Defaults to True.

        Returns:
            Project: the initialized `Project` given the project name.
        """
        if isinstance(project_name, Project):
            return project_name
        try:
            project = self.project_list[project_name]
        except KeyError:
            self.add_project(project_name, get_neighbors)
            project = self.project_list[project_name]
        
        return project


    def __prepare_source_data(self, project):

        # Update config file
        # If the config file hasn't been updated it will use the data that's already been pulled
        # If the config file has been updated it will read the file & update the data
        self.__update_project_config(project)

        # Load powertrack data
        # If the powertrack file hasn't been updated it will use the data that's already been pulled
        # If the powertrack file has been updated it will read the file & update the data
        project.load_production_data()
    

    def __update_project_config(self, project):
        
        # Store the list of sensors before pulling the config file
        sensors = project.Get_Sensor
        project._parse_config_file()

        # Check if new neighbor sensors have been added to the config & pull them if so
        if not sensors.equals(project.Get_Sensor):
            project._find_neighbor_sensors(self)
            self.__get_neighbor_sensor_data(project)
            
            
    def __get_neighbor_sensor_data(self, project):
        for neighbor_name in project.neighbor_sensors:
            # Update production data from neighbor
            try:
                neighbor = self.__get_project(neighbor_name, get_neighbors=False)
            except KeyError:
                print('Neighbor for {} not found: {}. Sensor data for the neighbor will be blank. Check logs to determine why neighbor was not added to DashboardSession'.format(project.project_name, neighbor_name))

            # Find the columns needed from the neighbor
            sensor_cols = project.Get_Sensor.loc[project.Get_Sensor['Source'] == neighbor_name, 'Value'].tolist()

            # Get the columns from the neighbor
            try:
                neighbor_df = neighbor.df.loc[project.df.index, sensor_cols]
            # If the production data hasn't been loaded for the project
            except AttributeError:
                neighbor.load_production_data()
                neighbor_df = neighbor.df.loc[project.df.index, sensor_cols]
            # If the neighbor errored out during initialization we'll just create a blank df for the neighbor
            except NameError:
                neighbor_cols = [col + '_' + neighbor_name for col in sensor_cols]
                project.df = project.df.reindex(columns = project.df.columns.tolist() + neighbor_cols)
                project.df_sensor_ON = project.df_sensor_ON.reindex(columns = project.df_sensor_ON.columns.tolist() + neighbor_cols)
                return

            neighbor_df.rename(columns=lambda x: np.str(x) + '_' + neighbor_name, inplace=True)
            neighbor_sensor_ON = neighbor.df_sensor_ON.loc[project.df_sensor_ON.index, sensor_cols]
            neighbor_sensor_ON.columns = neighbor_df.columns.tolist()

            df_cols = project.df.columns.tolist()
            project.df = df_update_join(project.df, neighbor_df)
            project.df = project.df[df_cols + neighbor_df.columns.tolist()]

            project.df_sensor_ON = df_update_join(project.df_sensor_ON, neighbor_sensor_ON)
            project.df_sensor_ON = project.df_sensor_ON[project.df.columns.tolist()]

    
    def draw_plots(self, project_name, plot_order=None, *args, **kwargs):
        """Draws plots for the given project

        Args:
            project_name (str, Project, or list): A project to draw plots on for analysis.
            plot_order (list or str, optional): A list of plots to draw. This can be
                any number of plots from one to all plots. Defaults to all plots in the below order.
            <h2>Acceptable Options & Default Order:</h2>
            * `xplot_met_poa`: Crossplot of meter & POA data.
            * `xplot_temp`: Crossplot of meter & POA, colored by Tamb.
            * `temps`: Tcell temperature comparison.
            * `inv`: Inverters.
            * `pr`: Hourly PR plot.
            * `8760`: Measured vs 8760 comparison.
            * `weather`: Weather sensors.
            * `met_corr`: Meter corrections.
            * `met_corr_dif`: Meter correction dif.
            * `poas`: POA sensors.
            * `met_poa`: Meter & POA avg.
            * `ghi`: GHI sensors.
            * `irrad`: POA & GHI sensors.
            * `tz`: Timezone check.
            * `losses`: Losses by type.
            * `poa_corr`: POA correlation check.
        """
        if isinstance(project_name, (str, unicode, Project)):
            project = self.__get_project(project_name, get_neighbors=False)
            redraw = kwargs.get('redraw', False)
            already_processed = self.process_project(project_name)
            if already_processed and not redraw:
                try:
                    # Check if the plotter object has the same project
                    plotter_project_name = self.active_plotter.project.project_name
                    if plotter_project_name == project_name:
                        # We don't need to re-draw plots if it's already been processed & plots are showing
                        return
                    else:
                        self.__draw_plots(project, plot_order, *args, **kwargs)
                except (NameError, AttributeError):
                    self.__draw_plots(project, plot_order, *args, **kwargs)
            else:
                self.__draw_plots(project, plot_order, *args, **kwargs)
        elif isinstance(project_name, list):
            project_list = project_name
            for i, project_name in enumerate(project_list):
                project = self.__get_project(project_name, get_neighbors=False)
                self.draw_plots(project.project_name, *args, **kwargs)
                try:
                    print('Press any key in the last plot window to show plots for {}'.format(project_list[i+1]))
                except IndexError:
                    print('Last plot in the list. Press any key in the last plot window to exit loop. Plots will remain showing until you close them.')
                while True:
                    if waitforbuttonpress():
                        break

    
    def __draw_plots(self, project, plot_order, *args, **kwargs):
        """Private method to orchestrate drawing of plots

        Args:
            project (Project): A project to use to draw plots for analysis
        """
        project_name = project.project_name
        close_plots = kwargs.get('close_plots', True)
        self.active_plotter = Plotter(project, *args, **kwargs)
        plotter_init_time = datetime.now().strftime('%m/%d/%Y %H:%M:%S')
        if close_plots:
            self.plotters = {project_name: [(plotter_init_time, self.active_plotter)]}
        else:
            try:
                self.plotters[project_name].append((plotter_init_time, self.active_plotter))
            except KeyError:
                self.plotters[project_name] = [(plotter_init_time, self.active_plotter)]
                
        self.active_plotter.draw_dashboard_plots(plot_order, *args, **kwargs)

    
    def __initialize_project(self, project_name, get_neighbors=True):
        """Initializes a project object with metadata

        Args:
            project_name (str): Name of a project to initialize.
            get_neighbors (bool, optional): Flag to add & initialize neighbor projects. Defaults to True.

        Returns:
            Project: An initialized Project object
        """

        try:
            df_proj_keys = self.df_keys.query("Project == @project_name").to_dict('records')[0]
        except IndexError:
            # Log that project was not found
            warn_msg = '"{}" not found in df keys. Please verify the project is present in df keys & the spelling is correct and try again'.format(project_name)
            print(warn_msg)
            logger.warn(warn_msg)

            # Remove project from project_list since we won't be able to initialize it
            del self.project_list[project_name]
            return

        if get_neighbors:
            # Find all neighbors that satisfy the distance and equipment requirements
            neighbor_list = neighbs.find_nearby_similar_projects(project_name, print_data=False).index.tolist()
            
            # Then remove the search project from the list
            # (Sometimes it will return an empty list if there is some data missing in `df_keys`) so we need to check if it returned a non-empty list first
            try:
                neighbor_list.remove(project_name)
            except ValueError:
                pass

            # If the project has neighbors, we'll add them to the DashboardSession instance
            # Set get_neighbors to False so we don't get neighbors of neighbors of neighbors etc.
            if neighbor_list:
                self.add_projects(neighbor_list, get_neighbors=False)
        else:
            neighbor_list = None

        Battery_AC_site = project_name in self.battery_ac_sites
        Battery_DC_site = project_name in self.battery_dc_sites
        Tracker_site = project_name in self.tracker_sites
        
        proj_init_dict = {}
        proj_init_dict['project_name'] = project_name
        proj_init_dict['df_proj_keys'] = df_proj_keys
        proj_init_dict['dashboard_dir'] = self.dashboard_dir
        proj_init_dict['data_cutoff_date'] = self.data_cutoff_date
        proj_init_dict['data_source'] = self.data_source
        proj_init_dict['Battery_AC_site'] = Battery_AC_site
        proj_init_dict['Battery_DC_site'] = Battery_DC_site
        proj_init_dict['Tracker_site'] = Tracker_site
        proj_init_dict['raw_snow_df'] = self.raw_snow_df
        proj_init_dict['neighbor_list'] = neighbor_list

        project = Project(proj_init_dict)
        return project
        

DashboardSession.__annotations__ = {'battery_ac_funds':list,
                                    'battery_ac_sites':list,
                                    'battery_dc_sites':list,
                                    'tracker_sites': list,
                                    'dashboard_dir': Union[str, bytes],
                                    'df_keys': DataFrame,
                                    'raw_snow_df': DataFrame,
                                    'project_list': list}
