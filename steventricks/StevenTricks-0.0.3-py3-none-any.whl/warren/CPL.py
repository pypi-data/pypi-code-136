import pandas as pd
from StevenTricks.tracker import logmaker
from StevenTricks.dbsqlite import tosql_df
from warren.conf.twse import warehouse, collection
from os.path import dirname, abspath, basename, join
from datetime import datetime
from os import makedirs, mkdir
# from sys import path
cwp = dirname(abspath(__file__))
cwd = basename(cwp)


def warehousedircheck(whsename):
    makedirs(join(whsename, warehouse['source']), exist_ok=True)
    makedirs(join(whsename, warehouse['product']), exist_ok=True)
    print('Making sub item directory of collection dictionary ...')
    msg = list(map(lambda x: None if mkdir(join(whsename, warehouse['source'], x)) is None else x + 'Failed to make directory',
                  collection.keys()))
    msg = pd.Series({'ErrorMSG': ','.join([_ for _ in msg if _ is not None])}, dtype='object')
    log = logmaker(datetime.now(), datetime.now(), msg, None, whsename)
    tosql_df(log, whsename)


if __name__ == '__main__':
    pass