import pandas as pd
from bru_analysis.sttm_groups import sttm
from bru_analysis.common.nlp_utils import CleanText

FOLDER_DATA = '/home/oscar/Labs'

df_e = pd.read_csv(f'{FOLDER_DATA}/bru_analysis/bru_analysis/ft_test/data/Facebook/facebook_lib_facebook_comments.csv')
df_e = df_e.sample(n=1000)

df_e['clean_text'] = df_e['message'].apply(lambda x: CleanText(x).process_text())

emotion = sttm(df_p=df_e, batch=50).sttm_groups()

print(emotion[['_id', 'clean_text', 'sttm_group']])
