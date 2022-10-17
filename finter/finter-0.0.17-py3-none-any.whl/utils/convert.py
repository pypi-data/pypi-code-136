import pandas as pd

def to_dataframe(json_response):
    return pd.read_json(json_response, orient='index')