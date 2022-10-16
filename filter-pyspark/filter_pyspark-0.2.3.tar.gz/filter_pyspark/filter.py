def pysprk_filter(df,column,val):
    '''df="Data Frame"
    Column="target column"
    val -> "string/List"
    Type:
        0 -> "Equal"
        1 -> "not-Equal"
        2 -> isnull()'''
    typ=input("kindly enter wich kind of Filter you want perform :")
    if typ=="0":
        if type(val)==list and len(val)<=10:
            if len(val)==2:
                df=df.filter((df[column]==lval[0])|(df[column]==lval[1]))
            elif len(val)==3:
                df=df.filter((df[column]==lval[0])|(df[column]==lval[1])|(df[column]==lval[2]))
            elif len(val)==4:
                df=df.filter((df[column]==lval[0])|(df[column]==lval[1])|(df[column]==lval[2])|(df[column]==lval[3]))
            elif len(val)==5:
                df=df.filter((df[column]==lval[0])|(df[column]==lval[1])|(df[column]==lval[2])|(df[column]==lval[3])|
                (df[column]==lval[4]))
            elif len(val)==6:
                df=df.filter((df[column]==lval[0])|(df[column]==lval[1])|(df[column]==lval[2])|(df[column]==lval[3])|
                (df[column]==lval[4])|(df[column]==lval[5]))
            elif len(val)==7:
                df=df.filter((df[column]==lval[0])|(df[column]==lval[1])|(df[column]==lval[2])|(df[column]==lval[3])|
                (df[column]==lval[4])|(df[column]==lval[5])|(df[column]==lval[6]))
            elif len(val)==8:
                df=df.filter((df[column]==lval[0])|(df[column]==lval[1])|(df[column]==lval[2])|(df[column]==lval[3])|
                (df[column]==lval[4])|(df[column]==lval[5])|(df[column]==lval[6])|(df[column]==lval[7]))
            elif len(val)==9:
                df=df.filter((df[column]==lval[0])|(df[column]==lval[1])|(df[column]==lval[2])|(df[column]==lval[3])|
                (df[column]==lval[4])|(df[column]==lval[5])|(df[column]==lval[6])|
                (df[column]==lval[7])|(df[column]==lval[8]))
            elif len(val)==10:
                df=df.filter((df[column]==lval[0])|(df[column]==lval[1])|(df[column]==lval[2])|(df[column]==lval[3])|
                (df[column]==lval[4])|(df[column]==lval[5])|(df[column]==lval[6])|
                (df[column]==lval[7])|(df[column]==lval[8])|(df[column]==lval[9]))
        elif type(val)!=list:
            df=df.filter(df[column]==lval)
        else:
            pass
    elif typ=="1":
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
        elif type(val)!=list:
            df=df.filter(df[column]!=val)
        else:
            pass
    elif typ=="2":
        df=df.filter(df[column].isNull())
    else:
        pass
    return df