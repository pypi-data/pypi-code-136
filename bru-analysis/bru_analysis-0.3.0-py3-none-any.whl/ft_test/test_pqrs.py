import pandas as pd
from bru_analysis.common.nlp_utils import CleanText
from bru_analysis.pqrs import pqrs

FOLDER_DATA = '/home/oscar/Labs'

df_e = pd.read_csv(f'{FOLDER_DATA}/bru_analysis/bru_analysis/ft_test/data/Facebook/facebook_lib_facebook_comments.csv')
df_e = df_e.sample(n=20)

df_e['clean_text'] = df_e['message'].apply(lambda x: CleanText(x).process_text())


pqrs = pqrs(df_p=df_e, batch=5).pqrs_df()

print(pqrs[['_id', 'clean_text', 'is_pqrs']])
