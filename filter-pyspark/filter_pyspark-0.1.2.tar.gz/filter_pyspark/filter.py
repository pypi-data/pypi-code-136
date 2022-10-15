
class filter_data:
    def __init__(self):
        self.self=self
        ''' In multiple filter function you can filter upto ten data 10 
        only you have to pass yor value as list(respect to multiple filter)
        '''
    def pysprk_filter(self,df,column,val,typ):
        '''
        df="Data Frame"
        Column="target column"
        val -> "string/List"
        Type:
            0 -> "Equal"
            1 -> "not-Equal"
            2 -> isnull()'''
        if typ=="Equal":
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
        elif typ=="not-Equal":
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
        elif typ=="isnull()":
            df=df.filter(col(column).isNull())
        else:
            pass
        return df