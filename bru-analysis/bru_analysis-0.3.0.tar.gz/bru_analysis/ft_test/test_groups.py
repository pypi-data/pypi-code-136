import pandas as pd
from bru_analysis.common.groups import Groups
from bru_analysis.common.extract_account_ids_fb import extractId
from bru_analysis.common.nlp_utils import CleanText

FOLDER_DATA = '/home/oscar/Labs'
SOCIAL_NET = 'tw'

if SOCIAL_NET == 'fb':
    posts = f'{FOLDER_DATA}/bru_analysis/bru_analysis/ft_test/data/Facebook/facebook_lib_facebook_posts.csv'
    comments = f'{FOLDER_DATA}/bru_analysis/bru_analysis/ft_test/data/Facebook/facebook_lib_facebook_comments.csv'
    pages = f'{FOLDER_DATA}/bru_analysis/bru_analysis/ft_test/data/Facebook/facebook_lib_facebook_pages.csv'
    page_id = 'page_id'
    page_id_column_com = 'page_id'
    page_id_column_pos = 'page_id'
    text_column = 'message'

elif SOCIAL_NET == 'ig':
    posts = f'{FOLDER_DATA}/bru_analysis/bru_analysis/ft_test/data/Instagram/instagram_lib_posts.csv'
    comments = f'{FOLDER_DATA}/bru_analysis/bru_analysis/ft_test/data/Instagram/instagram_lib_comment.csv'
    pages = f'{FOLDER_DATA}/bru_analysis/bru_analysis/ft_test/data/Instagram/instagram_lib_profile.csv'
    page_id = 'userid'
    page_id_column_com = 'post_owner_id'
    page_id_column_pos = 'owner_id'
    text_column = 'text'

elif SOCIAL_NET == 'tw':
    posts = f'{FOLDER_DATA}/bru_analysis/bru_analysis/ft_test/data/Twitter/twitter_lib_tweet.csv'
    comments = f'{FOLDER_DATA}/bru_analysis/bru_analysis/ft_test/data/Twitter/twitter_lib_tweetreply.csv'
    pages = f'{FOLDER_DATA}/bru_analysis/bru_analysis/ft_test/data/Twitter/twitter_lib_twitteraccount.csv'
    page_id = 'twitter_id'
    page_id_column_com = 'replying_to_id'
    page_id_column_pos = 'twitter_id'
    text_column = 'text'

else:
    print(f'{SOCIAL_NET} there is no such network')


df_groups_com = pd.read_csv(comments)
df_post_com = pd.read_csv(posts)
df_pages = pd.read_csv(pages)

# -----Filter-List-ID----- #

list_id = list(df_pages[page_id].unique())
list_id = list_id[0:2]
list_id = [str(element) for element in list_id]


if SOCIAL_NET == 'fb':
    df_groups_com = extractId(df_no_name=df_groups_com).extract_id()

df_groups_com_out = Groups(df_no_groups=df_groups_com,
                           net=SOCIAL_NET,
                           type_data='comments').accounts(list_accounts=list_id)

df_groups_pos_out = Groups(df_no_groups=df_post_com,
                           net=SOCIAL_NET,
                           type_data='post').accounts(list_accounts=list_id)

print(df_groups_com_out[page_id_column_com].unique())
print(df_groups_pos_out[page_id_column_pos].unique())

# -----Filter-List-ID----- #
df_filter_words = df_groups_com
df_filter_words['clean_text'] = df_filter_words[text_column].apply(lambda x: CleanText(x).process_text(rts=True,
                                                                                                       mentions=True,
                                                                                                       hashtags=True,
                                                                                                       links=True,
                                                                                                       spec_chars=True,
                                                                                                       stop_words=True))

print(df_filter_words[text_column].iloc[0])
print(df_filter_words['clean_text'].iloc[0])

list_words = ['rappi', 'ifood', 'fdgsdgsf', 'repartidor']

Groups(df_no_groups=df_filter_words,
       net=SOCIAL_NET,
       type_data='comments').words(list_words=list_words,
                                   column_text='clean_text')
print(f'{df_filter_words[-3:]}')
