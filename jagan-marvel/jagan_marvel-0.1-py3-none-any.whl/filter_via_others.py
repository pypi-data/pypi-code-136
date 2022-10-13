def filter_character_data(df, column, condition, value):
    ''' This function is taking the column, condition and value as parameter 
        and filters the data which satisfies the given condition'''

    if condition == 1:
        filtered_data_df = df[df[column] > value]
    elif condition == 2:
        filtered_data_df = df[df[column] < value]
    elif condition == 3:
        filtered_data_df = df[df[column] == value]
    else:
        print('Wrong choice')

    return filtered_data_df
