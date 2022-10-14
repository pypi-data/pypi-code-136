import pandas as pd
import os
from rats.core.RATS_CONFIG import Packet, splitchar, packagepath, dfpath


class SessionDataTracker:
    """This class is instantiated in rats.core.app"""
    data_files: pd.DataFrame = pd.DataFrame(columns=['File', 'Intra_file_analysis', 'Inter_file_analysis'])
    topo_files: pd.DataFrame = None

    def __init__(self, data_directory, parser, parser_test_directory=False):
        self.data_directory = data_directory + splitchar
        self.parser = parser
        if parser_test_directory:
            self.parser_test_directory = parser_test_directory
        else:
            self.parser_test_directory = packagepath / dfpath

    def scan_for_files(self, file_list: list = []):
        """Checks for .txt files in the specified data directory, then adds the files to the data_files dataframe"""
        if not file_list:
            # facilitate loading of files from datamanagement app
            file_list = [str(filename) for filename in os.listdir(self.data_directory)
                         if '.txt' in filename]

        temp_file_frame = pd.DataFrame(dict(File=[file.split('.')[0] for file in file_list],
                                            Intra_file_analysis=['not processed'] * len(file_list),
                                            Inter_file_analysis=['No deviations detected'] * len(file_list)))

        # this means that the data tracker is not satisfying the need to send a .txt file extension to the parser

        temp_file_frame = temp_file_frame[~temp_file_frame['File'].isin(self.data_files['File'].values)]
        self.data_files = self.data_files.append(temp_file_frame, ignore_index=True)

    def parse_data_files(self):
        """Use the parser passed to this class to parse the files"""
        if self.data_files.empty:
            pass
        # dumb... basically this now does nothing...
        else:
            for name in self.data_files.File.values:
                parser_class = self.parser(filepath = self.data_directory + name, data_directory=self.parser_test_directory)
                parser_class.parse()
                if parser_class.metadata['errors']:
                    self.data_files.loc[
                        self.data_files['File'] == name, 'Intra_file_analysis'] = 'Errors recorded during a scan'
                elif not parser_class.metadata['errors']:
                    self.data_files.loc[
                        self.data_files['File'] == name, 'Intra_file_analysis'] = 'No errors recorded during a scan'

                name = name + '.txt'
                if os.path.isfile(self.data_directory + name) or os.path.islink(self.data_directory + name):
                    os.unlink(self.data_directory + name)
                    print(f'{name} parsed and deleted from cache')

    def compare_data_files(self):
        if not self.data_files.empty:
            for name in self.data_files.File.values:
                parser_1 = self.parser(filepath = self.data_directory + name, data_directory=self.parser_test_directory)
                parser_1.parse()
                parser_1.dataframe = parser_1.dataframe[['LLC_COUNT', 'FUNCTION']]
                parser_1.dataframe.drop_duplicates(inplace=True)

                for second_name in self.data_files.File.values:
                    if second_name != name:
                        parser_2 = self.parser(filepath = self.data_directory + second_name, data_directory=self.parser_test_directory)
                        parser_2.parse()
                        parser_2.dataframe = parser_2.dataframe[
                            ['LLC_COUNT', 'FUNCTION']]
                        parser_2.dataframe.drop_duplicates(inplace=True)

                        if not parser_1.dataframe['FUNCTION'].equals \
                                    (parser_2.dataframe['FUNCTION']):
                            parser_1.different_to_n_dataframes += 1

                if parser_1.different_to_n_dataframes == 1 and len(self.data_files.File.values) < 3:
                    # There are only two files, so
                    status_message = f'LLC_COUNT vs FUNCTION ' \
                                     f'differs from the other file.'
                elif parser_1.different_to_n_dataframes > 1:
                    status_message = f'LLC_COUNT vs FUNCTION ' \
                                     f'differs from more than one other file.'
                else:
                    status_message = 'No deviations detected'

                self.data_files.loc[self.data_files['File'] == name, 'Inter_file_analysis'] = status_message

    def save_session_data(self):
        if self.data_files is None:
            pass
        elif self.data_files.empty:
            pass
        else:
            self.data_files.to_feather(self.data_directory + 'sessionfilenames')

    def load_session_data(self):
        self.data_files = pd.read_feather(self.data_directory + 'sessionfilenames')
