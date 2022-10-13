# Function which returns a df of all the characters starting 
# with the passed string in nameStartsWith arguement
import requests
import pandas as pd

def df_characters(nameStartsWith, *args):
    ''' Ideally takes 3 arguemnts: nameStartsWith, api_key, hash in the same order 
        and returns a dataframe starting with the passed string  '''
    api_key = None
    hash = None

    if len(args) != 2 :
        raise Exception("Either api_key or hash is missing!")
        
    else:
        api_key = args[0]
        hash = args[1]
        parameters = {'ts':1,'apikey':api_key,'hash':hash, 'limit': 100 , 'nameStartsWith':nameStartsWith}
        response = requests.get('http://gateway.marvel.com/v1/public/characters',params = parameters)
        output = response.json()
        df = pd.json_normalize(output['data']['results'])
        df = df[['id','name','comics.available','events.available','stories.available','series.available']]
        return df


# Filter Function
def filter(data_frame, column_name, filter_condition, filter_values):
    '''Takes in data frame of characters and returns a filtered dataframe based on the filter conditions and values
        available filter conditions for column_name = name:
            - starts_with: takes a string in filter_values (case sensitive)
            - is_in: takes a list of strings (names)
        filter conditions for other int columns:
            - is_equal_to, less_than, less_than_or_equal_to,  greater_than, greater_than_or_equal_to: pass an integer
            - is_in: pass a list of integers or a range(a,b)   '''
    if column_name == "name":
        if filter_condition == "starts_with":
            length = len(filter_values)
            return data_frame[data_frame[column_name].str[:length] == filter_values]
        elif filter_condition == "is_in":
            return data_frame[data_frame[column_name].isin(filter_values)]

    elif column_name != "name":
        if filter_condition == "is_equal_to":
            return data_frame[data_frame[column_name] == int(filter_values)]
        elif filter_condition == "less_than":
            return data_frame[data_frame[column_name] < int(filter_values)]
        elif filter_condition == "less_than_or_equal_to":
            return data_frame[data_frame[column_name] <= int(filter_values)]
        elif filter_condition == "greater_than":
            return data_frame[data_frame[column_name] > int(filter_values)]
        elif filter_condition == "greater_than_or_equal_to":
            return data_frame[data_frame[column_name] >= int(filter_values)]
        elif filter_condition == "is_in":
            return data_frame[data_frame[column_name].isin(filter_values)]
    
    else:
        return ("Invalid filter condition. Please check the documentation")