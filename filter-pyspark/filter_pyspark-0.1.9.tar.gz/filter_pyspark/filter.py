
class filter_data:
    def __int__(self,df,columns,val):
        self.self=self
        self.df=df
        self.columns=columns
        self.val=val
    ''' In multiple filter function you can filter upto ten data 10 
    only you have to pass yor value as list(respect to multiple filter)'''
    def pysprk_filter(self,df,columns,val):
        '''
        df="Data Frame"
        Column="target column"
        val -> "string/List"
        '''
        #column=input('Enter your target ciolumn name :')
        typ=input("kindly enter \n which filter do you want to perorm\n 0 -> 'Equal'\n 1 -> 'not-Equal' \n 2 -> 'isnull' \n kindly pass your value as 1 or 2 or 3 \n")
        if typ=="0":
            if type(val)==list and len(val)<=10:
                if len(val)==2:
                    df=df.filter((col(column)==val[0])|(col(column)==val[1]))
                elif len(val)==3:
                    df=df.filter((col(column)==val[0])|(col(column)==val[1])|(col(column)==val[2]))
                elif len(val)==4:
                    df=df.filter((col(column)==val[0])|(col(column)==val[1])|(col(column)==val[2])|(col(column)==val[3]))
                elif len(val)==5:
                    df=df.filter((col(column)==val[0])|(col(column)==val[1])|(col(column)==val[2])|(col(column)==val[3])|
                                 (col(column)==val[4]))
                elif len(val)==6:
                    df=df.filter((col(column)==val[0])|(col(column)==val[1])|(col(column)==val[2])|(col(column)==val[3])|
                                 (col(column)==val[4])|(col(column)==val[5]))
                elif len(val)==7:
                    df=df.filter((col(column)==val[0])|(col(column)==val[1])|(col(column)==val[2])|(col(column)==val[3])|
                                 (col(column)==val[4])|(col(column)==val[5])|(col(column)==val[6]))
                elif len(val)==8:
                    df=df.filter((col(column)==val[0])|(col(column)==val[1])|(col(column)==val[2])|(col(column)==val[3])|
                                 (col(column)==val[4])|(col(column)==val[5])|(col(column)==val[6])|(col(column)==val[7]))
                elif len(val)==9:
                    df=df.filter((col(column)==val[0])|(col(column)==val[1])|(col(column)==val[2])|(col(column)==val[3])|
                                 (col(column)==val[4])|(col(column)==val[5])|(col(column)==val[6])|
                                 (col(column)==val[7])|(col(column)==val[8]))
                elif len(val)==10:
                    df=df.filter((col(column)==val[0])|(col(column)==val[1])|(col(column)==val[2])|(col(column)==val[3])|
                                 (col(column)==val[4])|(col(column)==val[5])|(col(column)==val[6])|
                                 (col(column)==val[7])|(col(column)==val[8])|(col(column)==val[9]))
            elif type(val)!=list:
                df=df.filter(col(column)==val)
            else:
                pass
        elif typ=="1":
            if type(val)==list and len(val)<=10:
                if len(val)==2:
                    df=df.filter((col(column)!=val[0])|(col(column)!=val[1]))
                elif len(val)==3:
                    df=df.filter((col(column)!=val[0])|(col(column)!=val[1])|(col(column)!=val[2]))
                elif len(val)==4:
                    df=df.filter((col(column)!=val[0])|(col(column)!=val[1])|(col(column)!=val[2])|(col(column)!=val[3]))
                elif len(val)==5:
                    df=df.filter((col(column)!=val[0])|(col(column)!=val[1])|(col(column)!=val[2])|(col(column)!=val[3])|
                                 (col(column)!=val[4]))
                elif len(val)==6:
                    df=df.filter((col(column)!=val[0])|(col(column)!=val[1])|(col(column)!=val[2])|(col(column)!=val[3])|
                                 (col(column)!=val[4])|(col(column)!=val[5]))
                elif len(val)==7:
                    df=df.filter((col(column)!=val[0])|(col(column)!=val[1])|(col(column)!=val[2])|(col(column)!=val[3])|
                                 (col(column)!=val[4])|(col(column)!=val[5])|(col(column)!=val[6]))
                elif len(val)==8:
                    df=df.filter((col(column)!=val[0])|(col(column)!=val[1])|(col(column)!=val[2])|(col(column)!=val[3])|
                                 (col(column)!=val[4])|(col(column)!=val[5])|(col(column)!=val[6])|(col(column)!=val[7]))
                elif len(val)==9:
                    df=df.filter((col(column)!=val[0])|(col(column)!=val[1])|(col(column)!=val[2])|(col(column)!=val[3])|
                                 (col(column)!=val[4])|(col(column)!=val[5])|(col(column)!=val[6])|
                                 (col(column)!=val[7])|(col(column)!=val[8]))
                elif len(val)==10:
                    df=df.filter((col(column)!=val[0])|(col(column)!=val[1])|(col(column)!=val[2])|(col(column)!=val[3])|
                                 (col(column)!=val[4])|(col(column)!=val[5])|(col(column)!=val[6])|
                                 (col(column)!=val[7])|(col(column)!=val[8])|(col(column)!=val[9]))
            elif type(val)!=list:
                df=df.filter(col(column)!=val)
            else:
                pass
        elif typ=="2":
            df=df.filter(col(column).isNull())
        else:
            pass
        return df