from bru_analysis.common.extract_account_ids_fb import extractId
import pandas as pd

FILE_P = 'data/Facebook/facebook_lib_facebook_posts.csv'
FILE_C = 'data/Facebook/facebook_lib_facebook_comments.csv'

df_post = pd.read_csv(FILE_P)
df_com = pd.read_csv(FILE_C)

df_name = extractId(df_no_name=df_post).extract_name()
df_id = extractId(df_no_name=df_com).extract_id()

print(df_id.columns)
