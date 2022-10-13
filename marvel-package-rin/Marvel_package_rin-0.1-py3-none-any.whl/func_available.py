def fetch_available(results, dataframe_col, col_name, df_col):
    for i in results['data']['results']:
        if(df_col == 'character_id' or df_col == 'character_name'):
            dataframe_col[df_col].append(i[col_name])
        else:
             dataframe_col[df_col].append(i[col_name]['available'])