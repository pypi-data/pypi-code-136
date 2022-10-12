import pathlib
import re
import pandas as pd

def load_ms_weights(path: pathlib.Path, data: dict, format="csv") -> None:
        """
        Loads weights output by the millenium simulation into a dataframe.
        Here, we just load everything into a single dataframe.

        Params:

        folder: location of the MS weights.

        """
        #Find all the CSV files in the folder
        files = list(path.glob("*.csv"))
        ms_files = {}
        dfs = []

        for f in files: #Loop through the files
            #Figure out which field it corresponds to
            field = re.search(r"[0-9]_[0-9]", f.name)
            field = field.group()
            if format == "csv":
                #read in the file 
                f_path = path / f
                df = pd.read_csv(f_path)
                df['field'] = field
                if 'Unnamed: 0' in df.columns:
                    df.drop(columns=['Unnamed: 0'], inplace=True)
                dfs.append(df)
                ms_files.update({field: f})
        
        #Put all the files together into one dataframe
        dfs = pd.concat(dfs, ignore_index=True)
        data.update({'ms_weights': dfs, 'ms_files': ms_files})

weight_path = pathlib.Path('/Users/patrick/Documents/Documents/Work/Research/LensEnv/ms/weighting2')
data = {}
load_ms_weights(weight_path, data)

print(data['ms_weights'])