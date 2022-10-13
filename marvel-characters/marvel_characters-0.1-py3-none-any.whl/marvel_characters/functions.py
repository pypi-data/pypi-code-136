import pandas as pd
import requests

# function to create characters dataframe by making API call
def create_character_df (input_apikey, input_hash, nameStartWith):
    ''' 
    inputs = public api key, hash, and starting character of name
    outputs = pandas dataframe containing details of characters starting with the specified character.
    '''
    ts = 1
    address = 'http://gateway.marvel.com/v1/public/characters'
    df = pd.DataFrame()

    #looping to get all characters starting with certain character, when there are more than 100 suitable characters - using offset
    for i in range(0,3):
        parameters = {
            'apikey':input_apikey,
            'ts':ts,
            'hash':input_hash,
            'limit':100,
            'nameStartsWith':nameStartWith,
            'offset':100*i
        }
        response = requests.get(address, params=parameters)
        results = response.json()                             
        response.raise_for_status() # raise exception if http error
        df_new = pd.json_normalize(results['data']['results'])
        df = pd.concat([df, df_new], ignore_index=True)
    character_df = df[['id','name','events.available','series.available','stories.available','comics.available']]
    return(character_df)


# function to filter the characters dataframe
def filter_characters(df, column_name, filter_condition, filter_value):
    '''
    inputs = characters dataframe, name of column that will be used for filtering,
        filtering condition (for string value columns, filtering condition defaults to STARTS_WITH
                            for integer value columns, filtering condition can be EQUAL_TO, GREATER_THAN, and LESS_THAN)
        value of filter (value that the filter condition will be checked with)

    outputs = filtered dataframe of characters
    '''
    if column_name == 'name':
        filter_condition = 'starts_with'
        length =len(filter_value)
        return(df[df.name.str[:length] == filter_value])
    else:
        if filter_condition == 'equal_to':
            return(df[df[column_name] == int(filter_value)])
        elif filter_condition == 'less_than':
            return(df[df[column_name] < int(filter_value)])
        elif filter_condition == 'greater_than':
            return(df[df[column_name] > int(filter_value)])
        else:
            return('ERROR - Invalid filter condition')