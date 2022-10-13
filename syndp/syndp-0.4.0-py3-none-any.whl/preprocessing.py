
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def dummify(data : pd.DataFrame, columns= None, prefix_separator = "-"):
    '''
    dummifing function
    data : original data with categorical and continuous variables
    prefix_sep  mostly uses '_' as prefix separator. Can be modified
    columns : list of columns that are categorical
    '''
    excluded_variables = [continuous for continuous in data.columns if continuous not in columns]
    data1 = data[excluded_variables].copy() # we will concat this data with the dummified data
    
    list_of_series = [data[cols] for cols in columns]
    dummified = list(map(lambda x, y : pd.get_dummies(data=y, prefix=x, prefix_sep=prefix_separator), columns, list_of_series))
    
    dummified = pd.concat([data1, *dummified], axis=1)
    
    return dummified


def undummify(data :pd.DataFrame, columns :list, prefix_separator="-"):
    '''
    This function changes tabular data's categorical variable's one-hot dummy encoding to the original form
    data : original tabular data
    columns : a list of names of categorical values
    prefix_sep : prefix separator. Mostly is "-"
    '''
    # cols2collapse = {
    #     item.split(prefix_separator)[0]: (prefix_separator in item) for item in data.columns
    # }
    
    continuous_list = [cont for cont in data.columns if cont.split(prefix_separator)[0] not in columns]
    data1 = data[continuous_list].copy() # data to concat later

    undummified_list  = []
    for col in columns:
        undummified = data.filter(like=col).idxmax(axis=1).apply(lambda x : x.split(prefix_separator, maxsplit=1)[1]).rename(col)
        undummified_list.append(undummified) 
    
    recovered_data = pd.concat([data1, *undummified_list], axis=1)
    return recovered_data



def do_scaling(data : pd.DataFrame, columns : list):
    '''
    scaling function for continous variable. 
    This function returns the scaled data and the scaler itself for future use.
    data : the data you want to change
    columns : continuous columns
    '''
    scaler = MinMaxScaler(feature_range=(-1,1))
    not_scaling_columns = [cols for cols in data.columns if cols not in columns ]
    data1 = data[not_scaling_columns].copy()
    
    scaler.fit(data[columns].copy())
    scaled = scaler.transform(data[columns].copy())
    scaled= pd.DataFrame(scaled, columns=columns)
    
    scaled_data = pd.concat([scaled,data1], axis=1)
    return scaled_data, scaler


def reverse_scaling(data : pd.DataFrame, columns : list, scaler : MinMaxScaler):
    '''
    reverse the scaled data to original form
    data : scaled data
    columns : continuous columns - should be the same as the original scaling process
    scaler : Minmax scaler from do_scaling function
    '''
    excluded_cols = [col for col in data.columns if col not in columns]
    
    data1 = data[excluded_cols].copy()
    inversed = scaler.inverse_transform(data[columns])
    inversed = pd.DataFrame(inversed, columns=columns)
    
    reversed_data = pd.concat([data1, inversed], axis=1)
    return reversed_data
