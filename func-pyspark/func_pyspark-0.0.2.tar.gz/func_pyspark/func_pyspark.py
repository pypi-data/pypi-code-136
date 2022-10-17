from functools import reduce
def multiple_equal(df,column,val):
    if type(val)==list and len(val)<=10:
        if len(val)==2:
            df=df.filter((df[column]==val[0])|(df[column]==val[1]))
        elif len(val)==3:
            df=df.filter((df[column]==val[0])|(df[column]==val[1])|(df[column]==val[2]))
        elif len(val)==4:
            df=df.filter((df[column]==val[0])|(df[column]==val[1])|(df[column]==val[2])|(df[column]==val[3]))
        elif len(val)==5:
            df=df.filter((df[column]==val[0])|(df[column]==val[1])|(df[column]==val[2])|(df[column]==val[3])|
            (df[column]==val[4]))
        elif len(val)==6:
            df=df.filter((df[column]==val[0])|(df[column]==val[1])|(df[column]==val[2])|(df[column]==val[3])|
            (df[column]==val[4])|(df[column]==val[5]))
        elif len(val)==7:
            df=df.filter((df[column]==val[0])|(df[column]==val[1])|(df[column]==val[2])|(df[column]==val[3])|
            (df[column]==val[4])|(df[column]==val[5])|(df[column]==val[6]))
        elif len(val)==8:
            df=df.filter((df[column]==val[0])|(df[column]==val[1])|(df[column]==val[2])|(df[column]==val[3])|
            (df[column]==val[4])|(df[column]==val[5])|(df[column]==val[6])|(df[column]==val[7]))
        elif len(val)==9:
            df=df.filter((df[column]==val[0])|(df[column]==val[1])|(df[column]==val[2])|(df[column]==val[3])|
            (df[column]==val[4])|(df[column]==val[5])|(df[column]==val[6])|
            (df[column]==val[7])|(df[column]==val[8]))
        elif len(val)==10:
            df=df.filter((df[column]==val[0])|(df[column]==val[1])|(df[column]==val[2])|(df[column]==val[3])|
            (df[column]==val[4])|(df[column]==val[5])|(df[column]==val[6])|
            (df[column]==val[7])|(df[column]==val[8])|(df[column]==val[9]))
    return df



####equal #####

def equal(df,column,val):
    df=df.filter(df[column]==val)
    return df

##multiple not equal
def multiple_not_equal(df,column,val):
    if type(val)==list and len(val)<=10:
        if len(val)==2:
            df=df.filter((df[column]!=val[0])|(df[column]!=val[1]))
        elif len(val)==3:
            df=df.filter((df[column]!=val[0])|(df[column]!=val[1])|(df[column]!=val[2]))
        elif len(val)==4:
            df=df.filter((df[column]!=val[0])|(df[column]!=val[1])|(df[column]!=val[2])|(df[column]!=val[3]))
        elif len(val)==5:
            df=df.filter((df[column]!=val[0])|(df[column]!=val[1])|(df[column]!=val[2])|(df[column]!=val[3])|
            (df[column]!=val[4]))
        elif len(val)==6:
            df=df.filter((df[column]!=val[0])|(df[column]!=val[1])|(df[column]!=val[2])|(df[column]!=val[3])|
            (df[column]!=val[4])|(df[column]!=val[5]))
        elif len(val)==7:
            df=df.filter((df[column]!=val[0])|(df[column]!=val[1])|(df[column]!=val[2])|(df[column]!=val[3])|
            (df[column]!=val[4])|(df[column]!=val[5])|(df[column]!=val[6]))
        elif len(val)==8:
            df=df.filter((df[column]!=val[0])|(df[column]!=val[1])|(df[column]!=val[2])|(df[column]!=val[3])|
            (df[column]!=val[4])|(df[column]!=val[5])|(df[column]!=val[6])|(df[column]!=val[7]))
        elif len(val)==9:
            df=df.filter((df[column]!=val[0])|(df[column]!=val[1])|(df[column]!=val[2])|(df[column]!=val[3])|
            (df[column]!=val[4])|(df[column]!=val[5])|(df[column]!=val[6])|
            (df[column]!=val[7])|(df[column]!=val[8]))
        elif len(val)==10:
            df=df.filter((df[column]!=val[0])|(df[column]!=val[1])|(df[column]!=val[2])|(df[column]!=val[3])|
            (df[column]!=val[4])|(df[column]!=val[5])|(df[column]!=val[6])|
            (df[column]!=val[7])|(df[column]!=val[8])|(df[column]!=val[9]))
    return df


#### not equal
def not_equal(df,column,val):
    df=df.filter(df[column]!=val)
    return df

###is  null
def is_null(df,column,val):
    df=df.filter(df[column].isNull())
    return df

###not null
def not_null(df,column,val):
    df=df.filter(df[column].isNotNull())
    return df


#union###
def unionAll(*dfs):
    return reduce(DataFrame.unionAll, dfs)


