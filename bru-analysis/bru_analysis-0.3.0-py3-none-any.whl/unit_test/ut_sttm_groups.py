import unittest
import pandas as pd
from sttm_groups import SttmGroups

FOLDER = ""#D:/whale_jaguar/bru/bru_analysis/bru_analysis/


class Test(unittest.TestCase):

    def setUp(self):
        '''
        Variables to use in tests

        Returns
        -------
        None.

        '''
        self.s_net = 'tw'
        self.df = pd.read_csv("../twitter_lib_tweetreply.csv", index_col=0, low_memory=False)
        self.columns_df = list(self.df.columns)
        self.df_empty = pd.DataFrame(columns=self.columns_df)

    def test_data_normal(self):
        """
        This test with data ok

        Returns
        -------
        None.

        """
        print("TEST_DATA_NORMAL...")

        sttm_g = SttmGroups(dataframe=self.df,
                            s_net=self.s_net)

        df_sttm_groups = sttm_g.get_sttm_groups(min_texts=100)

        self.assertGreater(len(df_sttm_groups), 0)

        print(''.center(60, '='))

    def test_data_empty(self):
        '''
        This test with data empty

        Returns
        -------
        None.

        '''
        print("TEST_DATA_EMPTY...")

        sttm_g = SttmGroups(dataframe=self.df_empty,
                            s_net=self.s_net)

        df_sttm_groups = sttm_g.get_sttm_groups(min_texts=100)

        self.assertEqual(len(df_sttm_groups), 0)

        print(''.center(60, '='))

    def test_list_remove(self):
        '''
        This test remove two words

        Returns
        -------
        None.

        '''
        print("TEST_LIST_REMOVE...")

        list_remove = ['angelicalozanoc', 'delacallehum']

        sttm_g = SttmGroups(dataframe=self.df,
                            s_net=self.s_net)

        df_sttm_groups = sttm_g.get_sttm_groups(list_remove=list_remove,
                                                min_texts= 100)

        self.assertGreater(len(df_sttm_groups), 0)

        print(''.center(60, '='))


if __name__ == "__main__":
    unittest.main()
