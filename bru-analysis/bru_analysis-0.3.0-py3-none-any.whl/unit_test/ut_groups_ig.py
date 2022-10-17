import unittest
import pandas as pd
from copy import deepcopy
from bru_analysis.common.groups import Groups
from bru_analysis.common.nlp_utils import CleanText

FOLDER_DATA = '/home/oscar/Labs'
SOCIAL_NET = 'ig'

posts = f'{FOLDER_DATA}/bru_analysis/bru_analysis/ft_test/data/Instagram/instagram_lib_posts.csv'
comments = f'{FOLDER_DATA}/bru_analysis/bru_analysis/ft_test/data/Instagram/instagram_lib_comment.csv'
pages = f'{FOLDER_DATA}/bru_analysis/bru_analysis/ft_test/data/Instagram/instagram_lib_profile.csv'
page_id = 'userid'
page_id_column_com = 'post_owner_id'
page_id_column_pos = 'owner_id'
text_column = 'text'
list_words = ['rappi', 'ifood', 'fdgsdgsf', 'repartidor']


class TestGroups(unittest.TestCase):
    """
    This unit test groups accounts and words analytics
    """

    def setUp(self):
        """
        This function prepare data to analysis and test
        """
        print('Setup')

        # data test
        self.df_groups_com = pd.read_csv(comments)
        self.df_post_com = pd.read_csv(posts)
        self.df_pages = pd.read_csv(pages)

        # list accounts to analytics
        self.list_id = list(self.df_pages[page_id].unique())
        self.list_id = self.list_id[0:2]
        self.list_id = [str(element) for element in self.list_id]

        print('Ok')
        print(''.center(60, '-'))

    def test_accounts(self):
        """
        This test is data ok result equal to accounts to analyse
        """
        print('Test accounts')

        df_groups_com_out = Groups(df_no_groups=self.df_groups_com,
                                   net=SOCIAL_NET,
                                   type_data='comments').accounts(list_accounts=self.list_id)

        df_groups_pos_out = Groups(df_no_groups=self.df_post_com,
                                   net=SOCIAL_NET,
                                   type_data='post').accounts(list_accounts=self.list_id)

        self.assertEqual(len(self.list_id), len(df_groups_com_out[page_id_column_com].unique()))
        self.assertEqual(len(self.list_id), len(df_groups_pos_out[page_id_column_pos].unique()))

        print('Ok')
        print(''.center(60, '-'))

    def test_words(self):
        """
        This test find a list words in column test
        """
        print('Test find words')

        df_filter_w = deepcopy(self.df_groups_com)
        df_filter_w['clean_text'] = df_filter_w[text_column].apply(lambda x: CleanText(x).process_text(rts=True,
                                                                                                       mentions=True,
                                                                                                       hashtags=True,
                                                                                                       links=True,
                                                                                                       spec_chars=True,
                                                                                                       stop_words=True))
        Groups(df_no_groups=df_filter_w,
               net=SOCIAL_NET,
               type_data='comments').words(list_words=list_words,
                                           column_text='clean_text')

        self.assertEqual(len(list_words) + len(self.df_groups_com.columns) + 1,
                         len(df_filter_w.columns))

        print('Ok')
        print(''.center(60, '-'))

    def test_empty_df(self):
        """
        This test in case of exception return empty dataframe with a original dataframe columns
        """
        print('Test Exception')

        df_com_empty = pd.DataFrame(columns=self.df_groups_com.columns)
        df_pos_empty = pd.DataFrame(columns=self.df_post_com.columns)

        df_com_empty = Groups(df_no_groups=df_com_empty,
                              net=SOCIAL_NET,
                              type_data='comments').accounts(list_accounts=self.list_id)

        df_pos_empty = Groups(df_no_groups=df_pos_empty,
                              net=SOCIAL_NET,
                              type_data='post').accounts(list_accounts=self.list_id)

        self.assertEqual(len(df_com_empty), 0)
        self.assertEqual(len(df_pos_empty), 0)

        print('Ok')
        print(''.center(60, '-'))


if __name__ == "__main__":
    unittest.main()
