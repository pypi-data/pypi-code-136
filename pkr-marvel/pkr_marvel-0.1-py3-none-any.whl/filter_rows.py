def input_filter(result_df):
    print(''' The list of available columns are-
    character_name,
    character_id, 
    number_of_event_appearances, 
    number_of_series_appearances, 
    number_of_stories_appearances, 
    number_of_comics_appearances

    Enter combination of conditions in the below format
    For Ex,
    "number_of_event_appearances>=x & number_of_event_appearances<=y"
    ''')
    print('\nPlease Enter the conditions')
    condn= str(input())

    def filter_df(result_df, condn):
        filtered_df= result_df.eval(condn)
        return(result_df[filtered_df])
    
    final_df=filter_df(result_df, condn)
    return final_df 