import ast


class extractId:

    def __init__(self, df_no_name):
        """
        this function extracts the name of the post_from column
        :param df_no_name: dataframe with the column post_from
        """

        self.df_n = df_no_name

    def extract_name(self):
        """
        this function extract the name of account in Facebook
        :return: dataframe with a name account
        """

        df_n = self.df_n

        df_name = df_n.post_from.apply(lambda x: ast.literal_eval(x))
        df_clean = []
        for i in range(len(df_n)):
            temp_1 = df_name.iloc[i]["name"]
            df_clean.append(temp_1)
        df_n["name_id"] = df_clean

        return df_n

    def extract_id(self):
        """
        This function extract page_id from comments
        :return: df_with 'page_id' collumn
        """

        df_n = self.df_n
        df_n['page_id'] = df_n['post_id'].apply(lambda x: str(x.split('_')[0]))

        return df_n

