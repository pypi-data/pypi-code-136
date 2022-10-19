import pickle
import xgboost as xgb
import pandas as pd
import platform
from pathlib import Path


def video_to_cuts(df, shots_data):
    df = df.astype(float)

    df['Frame:'] += 1

    data = []
    cuts = pd.DataFrame()
    for i in shots_data:
        frame = i['frames_range'].replace(" ", "").split(",")
        data.append(df.iloc[int(frame[0]):int(frame[1]),:].mean())

    cuts = pd.DataFrame(data)
    cuts = cuts[['Blockiness:', 'SA:', 'Blockloss:', 'Blur:', 'TA:',
                    'Exposure(bri):', 'Contrast:', 'Noise:', 'Slice:', 'Flickering:']]
    cuts.columns = ['Blockiness:', 'SA:', 'Blockloss:', 'Blur:', 'TA:',
                    'Exposure(bri):', 'Contrast:', 'Noise:', 'Slice:', 'Flickering:']
    return cuts, shots_data


def ugc(df, shots_data):
#  input path to files where shots data are in pickle format
#  returns updated shots_data
    cuts, shots_data = video_to_cuts(df, shots_data)

    # 9k_all_set.json
    # 12k_all_set.json
    model_path = Path('/'.join(__file__.split('/')[:-1]) if platform.system() != 'Windows' else '\\'.join(__file__.split('\\')[:-1]), '12k_all_set.json')

    xgb_cl = pickle.load(open(str(model_path), 'rb'))  # exception thrown
    for count, value in enumerate(shots_data):
        preds = xgb_cl.predict((cuts[count:count+1]))
        value['ugc'] = 0 if int(preds[0]) == 1 else 1
    return shots_data  # 0 => not UGC, 1 => UGC

#print(ugc_dummy("/content/metricsResultsCSV.csv","/content/data.pkl"))


