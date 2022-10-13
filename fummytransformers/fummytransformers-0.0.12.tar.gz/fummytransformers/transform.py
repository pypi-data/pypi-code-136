import pandas as pd


def dict_to_csv(dic_obj, fn_csv):
    df = pd.DataFrame.from_dict(dic_obj, orient="index")
    df.to_csv(fn_csv, header=False)