import pandas as pd
from sys import exc_info
from bru_analysis.common.find_text import findText

ERR_SYS = "System error: "


class Groups:

    def __init__(self, df_no_groups, net, type_data='comments'):
        """
        This function group by accounts and group by words in the text
        :param df_no_groups: dataframe to group
        :param net: social network
        :param type_data: if comments or post
        """

        self.df_g = df_no_groups

        if type_data == 'comments':
            self.columns_df = self.df_g.columns
            if net == 'fb':
                self.id_column = 'page_id'
            elif net == 'ig':
                self.id_column = 'post_owner_id'
            elif net == 'tw':
                self.id_column = 'replying_to_id'
                self.df_g[self.id_column] = self.df_g[self.id_column].apply(lambda x: str(x)[0:10])
            else:
                print(f'The {net} is undefined')

        elif type_data == 'post':
            self.columns_df = self.df_g.columns
            if net == 'fb':
                self.id_column = 'page_id'
            elif net == 'ig':
                self.id_column = 'owner_id'
            elif net == 'tw':
                self.id_column = 'twitter_id'
            else:
                print(f'The {net} is undefined')

    def accounts(self, list_accounts):
        """
        This function filter by a list of counts id
        :param list_accounts: lista de cadenas con id de cuentas
        :return: dataframe : same filter dataframe with equal number of new columns that words
        """
        method_name = 'Groups.accounts'

        try:
            df_groups_account = self.df_g
            id_column = self.id_column
            df_groups_account[id_column] = df_groups_account[id_column].apply(lambda x: str(x))
            df_groups_account = df_groups_account[df_groups_account[id_column].isin(list_accounts)]

        except Exception as e_1:
            print(e_1)
            error_1 = exc_info()[0]
            print(ERR_SYS + str(error_1))
            print(f"Class: {self.__str__()}\nMethod: {method_name}")
            df_groups_account = pd.DataFrame(columns=self.columns_df)

        return df_groups_account

    def words(self, list_words, column_text='clean_text'):
        """
        This function returns a column for each words to find, to original dataframe
        :param list_words: list, words to find
        :param column_text: string: name column to find text
        :return: dataframe: with a column for each words to find
        """
        method_name = 'Groups.words'

        df_find_words = self.df_g

        try:

            for word in list_words:
                temp_word_list = []
                for col in range(len(df_find_words)):
                    temp1 = findText(text=df_find_words[column_text].iloc[col],
                                     word_find=word).find()
                    temp_word_list.append(temp1)

                df_find_words[f'word_{word}'] = temp_word_list

        except Exception as e_1:
            print(e_1)
            error_1 = exc_info()[0]
            print(ERR_SYS + str(error_1))
            print(f"Class: {self.__str__()}\nMethod: {method_name}")
            df_find_words[f'word_{word}'] = None
