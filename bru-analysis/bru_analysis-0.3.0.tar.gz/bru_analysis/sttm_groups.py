import os
import traceback
import pandas as pd
from sys import exc_info
from bru_analysis.common.nlp_utils import sendData
pd.options.mode.chained_assignment = None

BRU_MODELS_URL = os.environ["BRU_MODELS_URL"]
RETRIES = int(os.environ["RETRIES"])
ERR_SYS = "System error: "


class sttm:

    def __init__(self, df_p, batch=500):

        method_name = 'sttm __init__'

        try:
            self.cols_f = ['_id', 'clean_text']
            self.cols_except = df_p.columns
            self.batch = batch
            self.df_org = df_p
            self.df_p = df_p[self.cols_f]
            self.df_p = self.df_p.rename(columns={'_id': 'id'})

        except KeyError as e_1:
            print(''.center(60, '='))
            print(e_1)
            print(''.center(60, '='))
            error_1 = exc_info()[0]
            print(ERR_SYS + str(error_1))
            print(f'\nMethod: {method_name}')
            print(''.center(60, '='))
            traceback.print_exc()
            self.df_p = pd.DataFrame(columns=self.cols_f)

    def sttm_groups(self):

        method_name = 'sttm.sttm_groups()'
        df_p = self.df_p
        batch = self.batch

        url_features = f'{BRU_MODELS_URL}/sttm_groups'

        try:
            df_send = sendData(df=df_p, url=url_features).batch2all(batch=batch, delay_req=0.05)

            # pydantic ignore '_' character
            df_out = df_send.rename(columns={'id': '_id'})

            # df_out = pd.merge(df_send, self.df_org, how='outer', on='_id')

        except Exception as e_1:
            print(''.center(60, '='))
            print(e_1)
            print(''.center(60, '='))
            error_1 = exc_info()[0]
            print(ERR_SYS + str(error_1))
            print(f'\nMethod: {method_name}')
            print(''.center(60, '='))
            traceback.print_exc()
            df_out = pd.DataFrame(columns=list(self.cols_except) + ['sttm_group'])

        return df_out
