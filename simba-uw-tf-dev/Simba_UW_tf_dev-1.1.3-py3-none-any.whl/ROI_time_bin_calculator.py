from datetime import datetime
from simba.read_config_unit_tests import read_config_entry, read_config_file
import os
import pandas as pd
from simba.ROI_analyzer import ROIAnalyzer
from simba.misc_tools import get_fn_ext
import itertools

class ROITimebinCalculator(object):
    def __init__(self,
                 config_path: str,
                 bin_length: int):

        self.config_path, self.bin_length = config_path, bin_length
        self.date_time = datetime.now().strftime('%Y%m%d%H%M%S')
        self.config = read_config_file(config_path)
        self.file_type = read_config_entry(self.config, 'General settings', 'workflow_file_type', 'str', 'csv')
        self.project_path = read_config_entry(self.config, 'General settings', 'project_path', data_type='folder_path')
        self.roi_animal_cnt = read_config_entry(config=self.config, section='ROI settings', option='no_of_animals', data_type='int')
        self.probability_threshold = read_config_entry(config=self.config, section='ROI settings', option='probability_threshold', data_type='float',default_value=0.00)
        self.logs_path = os.path.join(self.project_path, 'logs')
        self.roi_analyzer = ROIAnalyzer(ini_path=self.config_path, data_path='outlier_corrected_movement_location', calculate_distances=False)
        self.roi_analyzer.read_roi_dfs()
        self.roi_analyzer.analyze_ROIs()
        self.shape_names = self.roi_analyzer.shape_names
        self.animal_names = list(self.roi_analyzer.bp_dict.keys())
        self.entries_exits_df = pd.concat(self.roi_analyzer.entry_exit_df_lst, axis=0)

    def analyze_time_bins(self):
        self.files_found = self.roi_analyzer.files_found
        for file_cnt, file_path in enumerate(self.files_found):
            _, self.video_name, _ = get_fn_ext(filepath=file_path)
            self.video_data = self.entries_exits_df[self.entries_exits_df['Video'] == self.video_name]
            for animal_name, shape_name in list(itertools.product(self.animal_names, self.shape_names)):
                data_df = self.video_data.loc[(self.video_data['Shape'] == shape_name) & (self.video_data['Animal'] == animal_name)]
                inside_shape_frms = [list(range(x, y)) for x, y in zip(list(data_df['Entry_times']), list(data_df['Exit_times'] + 1))]
                inside_shape_frms = [i for s in inside_shape_frms for i in s]





test = ROITimebinCalculator(config_path='/Users/simon/Desktop/troubleshooting/train_model_project/project_folder/project_config.ini',bin_length=5)
test.analyze_time_bins()