import pandas as pd
import os
from rats.core.RATS_CONFIG import packagepath, dfpath


class RatsDataTracker:
    """This class is instantiated in rats.core.app"""

    data_files: pd.DataFrame = None
    topo_files: pd.DataFrame = None

    def __init__(self, data_directory):
        self.data_directory = data_directory

    def scan_for_files(self):
        """Checks for .txt files in the specified data directory, then adds the files to the data_files dataframe"""
        file_list = [str(filename) for filename in os.listdir(self.data_directory)
                     if '.parquet' in filename]
        file_sizes = [os.path.getsize(str(packagepath / dfpath / filename)) / 1e6 for filename in
                      os.listdir(self.data_directory)
                      if '.parquet' in filename]

        temp_file_frame = pd.DataFrame(dict(file=file_list, file_size=file_sizes))

        if self.data_files is None:
            self.data_files = temp_file_frame
        else:
            # filter the temp file dataframe to exclude already present files, then append to the data_files frame
            temp_file_frame = temp_file_frame[~temp_file_frame['file'].isin(self.data_files['file'].values)]

            self.data_files = self.data_files.append(temp_file_frame, ignore_index=True)

    def delete_data(self, files_to_delete: [str] = [''], all_files=False):
        if self.data_files is None:
            pass
        elif self.data_files.empty:
            pass
        else:
            try:
                if all_files:
                    files_to_delete = [file for file in os.listdir(str(packagepath / dfpath)) if 'parquet' in file]
                for file in files_to_delete:
                    if os.path.isfile(str(packagepath / dfpath / file)) or os.path.islink(
                            str(packagepath / dfpath / file)):
                        os.unlink(str(packagepath / dfpath / file))
                        print(f'{file} deleted')

                self.data_files = self.data_files[~self.data_files['file'].isin(files_to_delete)]

            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file, e))
