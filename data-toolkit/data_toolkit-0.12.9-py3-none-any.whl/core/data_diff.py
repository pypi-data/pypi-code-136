import numpy as np
import pandas as pd



def highlight_diff(df1, df2, color='yellow'):
    '''
    write a function to highlight the differences between two dataframes (df1 and df2)
    goes throug each row of the two dataframes, compares them and if any of the values are different, highlight the different value
    if there are additional rows, highlight the entire row
    '''
    df1 = df1.reset_index(drop=True)
    df2 = df2.reset_index(drop=True)
    # get the shape of the larger df and fill it with 0s
    # shape = df1.shape if df1.shape > df2.shape else df2.shape
    # mask = np.zeros(shape)
    # mask[:df1.shape[0],:df1.shape[1]] = np.where(df1 != df2, 1, 0)
    
    # df1 = df1.reindex(range(shape[0]))
    # compare the two dataframes and highlight the differences
    # return pd.concat([df1.style.applymap(lambda x: 'background-color: %s' % color if x != df2.iloc[df1.index, df1.columns.get_loc(x.name)] else '', subset=df1.columns),
    #                   df2.style.applymap(lambda x: 'background-color: %s' % color if x != df1.iloc[df2.index, df2.columns.get_loc(x.name)] else '', subset=df2.columns)])
    
    # make sure the two dataframes have the same dimensions
    # assert df1.shape == df2.shape, 'Dataframes do not have the same shape'
    # # create a new dataframe with the same dimensions as the two dataframes
    df = df1.copy()
    # iterate through each row of the two dataframes
    for i in range(df1.shape[0]):
        # iterate through each column of the two dataframes
        for j in range(df1.shape[1]):
            # if the values in the two dataframes are not the same, then highlight the value in the new dataframe
            if df1.iloc[i,j] != df2.iloc[i,j]:
                df.iloc[i,j] = f'-> {df.iloc[i,j]}'
            
                

    def color_fill(val):
        styling = ''
        if isinstance(val, str):
            if "->" in val:
                styling = 'background-color: red; color:black'
        return styling 

    df.style.applymap(color_fill)
    
    return df