class filter_data:
    def __init__(self,df,column):
        self.self=self
        self.df=df
        self.column=column
        
          '''In multiple filter function you can filter upto ten data 10 
        only you have to pass yor value as list(respect to multiple filter)'''
    def filter_equalto_multiple(self,df,column,val):#val as list
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
            else:
                pass
            
                print("Your List length is more than 10 ➡ currently",len(val))
        return df
    def filter_equalto(self,df,column,val):
        df=df.filter(df[column]==val)
        print("New Shape of the data frame",(df.count(),len(df.coulumns)))
        return df
    def filter_not_equalto_multiple(self,df,column,val):#val as list
        if type(val)==list and len(val)<=10:
            print('start')
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
            else:
                pass
            
                print("Your List length is more than 10 ➡ currently",len(val))
        return df
        
    def filter_not_equalto(self,df,column,val):
        df=df.filter(df[column]!=val)
        print('New shape of the Dat set',(df.count(), len(df.dfumns)))
        return df
    def filter_null(self,df,column):
        df=df.filter(df[column].isNull())
        print('New shape of the Dat set',(df.count(), len(df.dfumns)))
        return df
        
