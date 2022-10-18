import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_selection import mutual_info_regression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler, MinMaxScaler

class Ranker:
    '''Rank your features in order of importance to your target variable
    '''
    def __init__(self, dataframe, target, scaler='MinMax', imp_ranker='Correlation'):

        '''
        Args: 
            dataframe 
            target (str)
            scaler (str)
            imp_ranker (str)

        Attributes:
            dataframe : pandas dataframe
            target (str): variable to be predicted
            scaler (str): scaler type to be used, "Standard" or "MinMax". 
            default scaler is "MinMax"
            imp_ranker (float): algorithm for ranking, default is "Correlation"
            Others are "Mutual_info" and "Random_forest"
        '''

        self.dataframe=dataframe
        self.target=target
        self.scaler=scaler
        self.imp_ranker=imp_ranker
        self.color='blue'
        
    def scaler(self):
        X=df.drop(self.target,axis=1)
        y=df[self.target]
        cols=X.columns
        if self.scaler == "Standard":
            sc=StandardScaler()
        else:
            sc=MinMaxScaler()

        X=sc.fit_transform(X)
        df1=pd.DataFrame(scaler(X,'MinMax'),columns=cols)
        df1[self.target]=y 
        self.dataframe=df1
        return self.dataframe
        

    

    def build_table(self):
        """Show a table ranking the importance of the features in descending order
        """
        if self.imp_ranker == "Correlation":
            corr = self.dataframe.corr()[self.target].apply(lambda x:abs(x)).sort_values(ascending=False)
            corr=corr[1:]
            corr=pd.DataFrame(corr)
            corr.columns=['Score']
            
            self.table=corr
            return self.table
        elif self.imp_ranker == "Random_forest":
            X=df.drop(target,axis=1)
            y=df[target]
            rf=RandomForestRegressor()
            rf.fit(X, y)
            predictors = X.columns
            coef = pd.Series(rf.feature_importances_, predictors).sort_values(ascending=False)
            coef=pd.DataFrame(coef,columns=["Score"])
            self.table=coef
            return self.table
        else:
            self.imp_ranker == "Mutual_info"
            X=df.drop(target,axis=1)
            y=df[target]
            mutual_info_regression(X,y)
            tab=pd.DataFrame(mutual_info_regression(X,y),index=X.columns)
            tab.columns=['Importance']
            tab=tab.sort_values(by='Importance',ascending=False)
            self.table=tab
            return self.table

    def build_chart(self, color): 
        """Show a table ranking the importance of the features in descending order
        """
        self.color=color
        if self.imp_ranker == "Correlation":
            corr = self.dataframe.corr()[self.target].apply(lambda x:abs(x)).sort_values(ascending=False)
            corr=corr[1:]
            corr=pd.DataFrame(corr)
            corr.columns=['Score']
            
            self.table=corr
        elif self.imp_ranker == "Random_forest":
            X=df.drop(target,axis=1)
            y=df[target]
            rf=RandomForestRegressor()
            rf.fit(X, y)
            predictors = X.columns
            coef = pd.Series(rf.feature_importances_, predictors).sort_values(ascending=False)
            coef=pd.DataFrame(coef,columns=["Score"])
            self.table=coef
        else:
            self.imp_ranker == "Mutual_info"
            X=df.drop(target,axis=1)
            y=df[target]
            mutual_info_regression(X,y)
            tab=pd.DataFrame(mutual_info_regression(X,y),index=X.columns)
            tab.columns=['Importance']
            tab=tab.sort_values(by='Importance',ascending=False)
            self.table=tab
        plt.figure(figsize=(14,6))
        self.table.plot.bar(label='Importance',color=self.color)
        plt.show()


        
