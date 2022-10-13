def filter_character_data_via_name(df, column, value):
    ''' This function is taking the sting value as parameter 
        and filters the data which has that string in the name'''

    filtered_data_df = df[df[column].str.contains(value, case=False, na=False)]
    return filtered_data_df
