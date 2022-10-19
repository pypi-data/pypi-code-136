import pandas as pd

from qpandas import MyPandas, load_births

births = load_births()
assert type(births) == pd.DataFrame
URL = "mysql://root:root@localhost/"
QUERY = """
SELECT b1.date d1
    , b1.births b1
    , b2.date d2
    , b2.births b2
FROM births b1, births b2
"""
df = MyPandas(URL)(QUERY, locals())
assert type(df) == pd.DataFrame
print(df)
