import pandas as pd
import requests


def load_dataset(url) -> pd.DataFrame:
    local_filename = "test.csv"  # url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return pd.read_csv(local_filename)
