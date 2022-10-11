print("""
import sys
import warnings
import itertools as itr

import numpy as np
import pandas as pd
from pandas import   read_csv, Grouper, DataFrame, concat
from pandas import datetime
import seaborn as sns
from matplotlib import pyplot as plt
%matplotlib inline
pd.options.display.float_format = '{:.6f}'.format

from math import sqrt
from   datetime                        import  datetime, timedelta
import statsmodels.tools.eval_measures as      em

import statsmodels.api as sm
import statsmodels.tsa.api as smt
import statsmodels.formula.api as smf

from statsmodels.tsa.api               import ExponentialSmoothing, SimpleExpSmoothing, Holt
from statsmodels.tsa.stattools         import  adfuller
from statsmodels.tsa.stattools         import  pacf
from statsmodels.tsa.stattools         import  acf
from statsmodels.graphics.tsaplots     import  plot_pacf
from statsmodels.graphics.tsaplots     import  plot_acf
from statsmodels.graphics.gofplots     import qqplot
from statsmodels.tsa.seasonal          import seasonal_decompose
from statsmodels.tsa.arima_model       import  ARMA, ARIMA
from statsmodels.tsa.statespace.sarimax   import  SARIMAX
from statsmodels.tsa.arima_process     import  ArmaProcess
from statsmodels.tsa.statespace.varmax import VARMAX
from statsmodels.tsa.seasonal     import seasonal_decompose, STL

from   sklearn.metrics                 import  mean_squared_error
from   IPython.display                 import display
from   pylab                           import rcParams

from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import silhouette_score, silhouette_samples, mean_absolute_percentage_error
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.impute import KNNImputer
import warnings
warnings.filterwarnings('ignore')

from   sklearn.metrics                 import  mean_squared_error
from math import sqrt
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline

# -------------------------------------------------------------------------------------------------------------
### oildata.ipynb
Reading time series data
df = pd.read_csv('oil.csv',parse_dates=['date'],dayfirst=True)
df.head()
df.tail()
df=df.set_index('date')
Plotting time series
rcParams['figure.figsize'] = 25,8
df.plot(grid=True);
Spliting time series data
Most recent observations will be used to test the model while remaining series will be used to train the model
if time series has seasonality, then test data must include atleast one seasonal period.
train_end=datetime(2017,1,1)
test_end=datetime(2017,8,1)
train             = df[:train_end] 
test              = df[train_end + timedelta(days=1):test_end]
print('Train')
display(train)
print('Test')
display(test)
Simple Exponential Smoothing
model_SES = SimpleExpSmoothing(train,initialization_method='estimated')
lets train the model for different 𝛼 values
model_SES_fit1 = model_SES.fit(optimized=True)
Predicting forecast using trained models
SES_predict1 = model_SES_fit1.forecast(steps=len(test))
Plotting time searies and forecasts
plt.plot(train, label='Train')
plt.plot(test, label='Test')
​
plt.plot(SES_predict1,label='forecast')
​
plt.legend(loc='best')
plt.grid()
Root Mean Square Error for simple forecasting model
mean_squared_error(test.values,SES_predict1.values,squared=False)
Defining Mean Absolute Percentage error
def MAPE(y_true, y_pred):
    return np.mean((np.abs(y_true-y_pred))/(y_true))*100
Mean Absolute Percentage Error for simple forecasting model
MAPE(test.values,SES_predict1.values)
END


# -------------------------------------------------------------------------------------------------------------
### MA_processes.ipynb

MA(1) process
from pylab import rcParams
rcParams['figure.figsize'] = 20, 10
​
ar = np.array([1])
ma = np.array([1,0.7])
object1 = ArmaProcess(ar, ma)
simulated_data_1 = object1.generate_sample(nsample=150)
df1=pd.Series(simulated_data_1)
df1.plot()
plot_acf(df1);
plot_pacf(df1);
## MA(2) process
from pylab import rcParams
rcParams['figure.figsize'] = 20, 10
​
ar = np.array([1])
ma = np.array([1,0.7,0.2])
object1 = ArmaProcess(ar, ma)
simulated_data_1 = object1.generate_sample(nsample=600)
df2=pd.Series(simulated_data_1)
df2.plot()
plot_acf(df2);
plot_pacf(df2);

# -------------------------------------------------------------------------------------------------------------
### Intro_to_TSF.ipynb

Reading time series
Example 1
 df1 = pd.read_csv('AirPassenger.csv')
checking datatypes

df1.dtypes
Pandas unable to identify Year-Month column as a date object

Using 'parse_dates' input, pandas will be able to identify that the data is time series.

df1 = pd.read_csv('AirPassenger.csv', parse_dates = ['Year-Month'])
df1.dtypes
Now the time series reference is approprately identified.

It is recommended that we make our time series reference as the index

df1 = pd.read_csv('AirPassenger.csv', parse_dates = ['Year-Month'], index_col = 'Year-Month')
df1.head()
Using time series reference as index, We can conveniently do slicing i.e. obtain data for a specific time period.

df1['1951-04-01':'1952-01-01']
We can check values corresponding to a specific time point aswell

df1.loc['1960-05-01']
Example 2
df2 = pd.read_csv('Gas.csv')
df2.head()
Lets drop unwanted columns and add time-stamp to series

df2.drop('Unnamed: 0',axis=1,inplace=True)
df2.head()
date = pd.date_range(start='1/1/1956', end='1/1/1996', freq='M')
date
df2['Time_Stamp'] = pd.DataFrame(date)
df2.head()
df2=df2.set_index('Time_Stamp')
df2.head()
Example 3
df3= pd.read_csv('RetailTurnover.csv')
df3.head()
df3.tail()
data is recorder for the period of 1982 through 1992 on quarterly basis

converting above data into time series

quarters= pd.date_range(start='9/30/1982', end='3/31/1992', freq='Q')
quarters
df3['Time_Stamp']=pd.DataFrame(quarters)
df3.head()
dropping unwanted columns and making time-stamp as index for the series

df3.drop(['Year','Quarter'],axis=1,inplace=True)
df3=df3.set_index('Time_Stamp')
df3.head()
Multivariate Time Series
df4= pd.read_csv('Daily_electricity_consumption.csv',)
df4.head()
date = pd.date_range(start='1/1/2009', end='11/26/2010', freq='D')
date
df4['Time_Stamp'] = pd.DataFrame(date)
df4=df4.set_index('Time_Stamp')
df4=df4.drop('date_time',axis=1)
df4.head()
Plotting time series
Plotting Air Passanger time series data
df1.plot()
plt.show()
We can increase the size of the plot

df1.plot(figsize=(12,8))
we can include gridlines to the plot

df1.plot(figsize=(12,8),grid=True)
for multivariate time series
df4.plot(figsize=(15,12))
Handling missing values
No missing data is allowed in time series as data is ordered. It is simply not possible to shift the series to fill in the gaps.

df4=pd.read_csv('Shoe Sales.csv',parse_dates = ['Month'], index_col = 'Month')
df4.head()
Let us replace the number of pairs for 2012-May which is 932 as np.NaN.

df4.replace(932, np.NaN, inplace = True)
df4.isnull().sum()
Time series has one misiing value
NA value can be replaced using resampling.
## imputing using rolling mean
daily = df4.fillna(df4.rolling(6,min_periods=1).mean())
​
​
## imputing using interpolation
df4_imputed= df4.interpolate(method = 'linear')
df4_imputed.loc['2012-05-01']
number of pairs for 2012-May which was 932 is now replaced by value 976.5

daily.loc['2012-05-01']
df4_imputed.isnull().sum()
daily.isnull().sum()
Modifying time series range
Let's change the monthly series to quarterly.
df1_q = df1.resample('Q').sum()
df1_q.head()
df1_q.plot()
Decomposition of time series
Air Passanger data
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October','November', 'December']
yearly_sales_across_years = pd.pivot_table(df1, values = 'Pax', columns = df1.index.year,index = df1.index.month_name())
yearly_sales_across_years = yearly_sales_across_years.reindex(index = months)
yearly_sales_across_years.plot()
plt.grid()
plt.legend(loc='best');
decomposition = seasonal_decompose(df1,model='additive')
decomposition.plot();
decomposition = seasonal_decompose(df1,model='multiplicative')
decomposition.plot();
Decomposition by Loess
decomposition = STL(df1).fit()
decomposition.plot();
decomposition = STL(np.log10(df1)).fit()
decomposition.plot();
Moving Average
df5=pd.read_csv('Stock.csv', parse_dates = ['TimeStamp'], index_col = 'TimeStamp',dayfirst=True)
df5
df5.plot()
plt.figure(figsize=(12,8))
plt.plot(df5, label='closing price')
plt.plot(df5.rolling(5).mean(), label='Moving Average')
plt.legend(loc='best')
plt.show()
plt.figure(figsize=(12,8))
plt.plot(df5, label='closing price')
plt.plot(df5.rolling(30).mean(), label='Moving Average')
plt.legend(loc='best')
plt.show()

# -------------------------------------------------------------------------------------------------------------
### Intro Forecasting.ipynb

Read the data as a monthly Time Series from the '.csv' file.
df = pd.read_csv("daily-total-female-births.csv")
​
## Here we will create a separate date range and then add it to the data instead of parsing the dates
df.head()
date = pd.date_range(start='1/1/1959', periods=len(df), freq='D')
date
df['Time_Stamp'] = pd.DataFrame(date,columns=['Month'])
df.head()
df.set_index('Time_Stamp',inplace=True,drop='Time_Stamp')
df.drop(labels='Date', axis=1, inplace=True)
df.head()
Now, we have our data ready for the Time Series Analysis.

Plot the Time Series to understand the behaviour of the data
from pylab import rcParams
rcParams['figure.figsize'] = 15,8
df.plot(grid=True);
Check the basic measures of descriptive statistics of the Time Series
round(df.describe(),3)
Remember, the above measure is independent of the Time Series aspect. As in, it does not take into account the Time Stamped data.

Split the data into train and test and plot the training and test data. [30% of the most recent data should be in the test set]
train    =   df[0:int(len(df)*0.7)] 
test     =   df[int(len(df)*0.7):]
print(train.shape)
print(test.shape)
from IPython.display import display
print('First few rows of Training Data')
display(train.head())
print('Last few rows of Training Data')
display(train.tail())
print('First few rows of Test Data')
display(test.head())
print('Last few rows of Test Data')
display(test.tail())
train['Births'].plot(fontsize=14)
test['Births'].plot(fontsize=14)
plt.grid()
plt.legend(['Training Data','Test Data'])
plt.show()
Note: It is difficult to predict the future observations if such an instance has not happened in the past. From our train-test split we are predicting likewise behaviour as compared to the past years.
Building different models and comparing the accuracy metrics.
Model 1: Linear Regression
For this particular linear regression, we are going to regress the 'Births' variable against the order of the occurrence. For this we need to modify our training data before fitting it into a linear regression.
train_time = [i+1 for i in range(len(train))]
test_time = [i+256 for i in range(len(test))]
print('Training Time instance','\n',train_time)
print('Test Time instance','\n',test_time)
We see that we have successfully the generated the numerical time instance order for both the training and test set. Now we will add these values in the training and test set.

LinearRegression_train = train.copy()
LinearRegression_test = test.copy()
LinearRegression_train['time'] = train_time
LinearRegression_test['time'] = test_time
​
print('First few rows of Training Data')
display(LinearRegression_train.head())
print('Last few rows of Training Data')
display(LinearRegression_train.tail())
print('First few rows of Test Data')
display(LinearRegression_test.head())
print('Last few rows of Test Data')
display(LinearRegression_test.tail())
Now that our training and test data has been modified, let us go ahead use 𝐿𝑖𝑛𝑒𝑎𝑟𝑅𝑒𝑔𝑟𝑒𝑠𝑠𝑖𝑜𝑛⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯ to build the model on the training data and test the model on the test data.

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(LinearRegression_train[['time']],LinearRegression_train['Births'])
train_predictions_model1         = lr.predict(LinearRegression_train[['time']])
LinearRegression_train['RegOnTime'] = train_predictions_model1
​
test_predictions_model1         = lr.predict(LinearRegression_test[['time']])
LinearRegression_test['RegOnTime'] = test_predictions_model1
​
plt.plot( train['Births'], label='Train')
plt.plot(test['Births'], label='Test')
plt.plot(LinearRegression_test['RegOnTime'], label='Regression On Time_Test Data')
​
plt.legend(loc='best')
plt.grid();
Defining the functions for calculating the accuracy metrics.
from sklearn import metrics
Model Evaluation
rmse_model1_test = metrics.mean_squared_error(test['Births'],test_predictions_model1,squared=False)
print("For RegressionOnTime forecast on the Test Data,  RMSE is %3.3f " %(rmse_model1_test))
resultsDf = pd.DataFrame({'Test RMSE': [rmse_model1_test]},index=['RegressionOnTime'])
resultsDf
Model 2: Naive Approach: 𝑦̂ 𝑡+1=𝑦𝑡
For this particular naive model, we say that the prediction for tomorrow is the same as today and the prediction for day after tomorrow is tomorrow and since the prediction of tomorrow is same as today,therefore the prediction for day after tomorrow is also today.
NaiveModel_train = train.copy()
NaiveModel_test = test.copy()
train.tail()
NaiveModel_test['naive'] = np.asarray(train['Births'])[len(np.asarray(train['Births']))-1]
NaiveModel_test['naive'].head()
plt.plot(NaiveModel_train['Births'], label='Train')
plt.plot(test['Births'], label='Test')
​
plt.plot(NaiveModel_test['naive'], label='Naive Forecast on Test Data')
​
plt.legend(loc='best')
plt.title("Naive Forecast")
plt.grid();
Model Evaluation
rmse_model2_test = metrics.mean_squared_error(test['Births'],NaiveModel_test['naive'],squared=False)
print("For RegressionOnTime forecast on the Test Data,  RMSE is %3.3f" %(rmse_model2_test))
resultsDf_2 = pd.DataFrame({'Test RMSE': [rmse_model2_test]},index=['NaiveModel'])
​
resultsDf = pd.concat([resultsDf, resultsDf_2])
resultsDf
Method 3: Simple Average
For this particular simple average method, we will forecast by using the average of the training values.
SimpleAverage_train = train.copy()
SimpleAverage_test = test.copy()
SimpleAverage_test['mean_forecast'] = train['Births'].mean()
SimpleAverage_test.head()
plt.plot(SimpleAverage_train['Births'], label='Train')
plt.plot(SimpleAverage_test['Births'], label='Test')
​
plt.plot(SimpleAverage_test['mean_forecast'], label='Simple Average on Test Data')
​
plt.legend(loc='best')
plt.title("Simple Average Forecast")
plt.grid();
Model Evaluation
rmse_model3_test = metrics.mean_squared_error(test['Births'],SimpleAverage_test['mean_forecast'],squared=False)
print("For Simple Average forecast on the Test Data,  RMSE is %3.3f" %(rmse_model3_test))
resultsDf_3 = pd.DataFrame({'Test RMSE': [rmse_model3_test]}
                           ,index=['SimpleAverageModel'])
​
resultsDf = pd.concat([resultsDf, resultsDf_3])
resultsDf
Method 4: Moving Average(MA)
For the moving average model, we are going to calculate rolling means (or moving averages) for different intervals. The best interval can be determined by the maximum accuracy (or the minimum error) over here.
For Moving Average, we are going to average over the entire data.
MovingAverage = df.copy()
MovingAverage.head()
Trailing moving averages
​
MovingAverage['Trailing_2'] = MovingAverage['Births'].rolling(2).mean()
MovingAverage['Trailing_4'] = MovingAverage['Births'].rolling(4).mean()
MovingAverage['Trailing_6'] = MovingAverage['Births'].rolling(6).mean()
MovingAverage['Trailing_9'] = MovingAverage['Births'].rolling(9).mean()
​
MovingAverage.head()
## Plotting on the whole data
​
plt.plot(MovingAverage['Births'], label='Train')
plt.plot(MovingAverage['Trailing_2'], label='2 Point Moving Average')
plt.plot(MovingAverage['Trailing_4'], label='4 Point Moving Average')
plt.plot(MovingAverage['Trailing_6'],label = '6 Point Moving Average')
plt.plot(MovingAverage['Trailing_9'],label = '9 Point Moving Average')
​
plt.legend(loc = 'best')
plt.grid();
Let us split the data into train and test and plot this Time Series. The window of the moving average is need to be carefully selected as too big a window will result in not having any test set as the whole series might get averaged over.

#Creating train and test set 
trailing_MovingAverage_train=MovingAverage[0:int(len(MovingAverage)*0.7)] 
trailing_MovingAverage_test=MovingAverage[int(len(MovingAverage)*0.7):]
## Plotting on both the Training and Test data
​
plt.figure(figsize=(16,8))
plt.plot(trailing_MovingAverage_train['Births'], label='Train')
plt.plot(trailing_MovingAverage_test['Births'], label='Test')
​
​
plt.plot(trailing_MovingAverage_test['Trailing_2'], label='2 Point Trailing Moving Average on Test Set')
plt.plot(trailing_MovingAverage_test['Trailing_4'], label='4 Point Trailing Moving Average on Test Set')
plt.plot(trailing_MovingAverage_test['Trailing_6'],label = '6 Point Trailing Moving Average on Test Set')
plt.plot(trailing_MovingAverage_test['Trailing_9'],label = '9 Point Trailing Moving Average on Test Set')
​
plt.legend(loc = 'best')
plt.grid();
Model Evaluation
Done only on the test data.
## Test Data - RMSE  --> 2 point Trailing MA
​
rmse_model4_test_2 = metrics.mean_squared_error(test['Births'],trailing_MovingAverage_test['Trailing_2'],squared=False)
print("For 2 point Moving Average Model forecast on the Training Data,  RMSE is %3.3f" %(rmse_model4_test_2))
​
## Test Data - RMSE --> 4 point Trailing MA
​
rmse_model4_test_4 = metrics.mean_squared_error(test['Births'],trailing_MovingAverage_test['Trailing_4'],squared=False)
print("For 4 point Moving Average Model forecast on the Training Data,  RMSE is %3.3f" %(rmse_model4_test_4))
​
## Test Data - RMSE --> 6 point Trailing MA
​
rmse_model4_test_6 = metrics.mean_squared_error(test['Births'],trailing_MovingAverage_test['Trailing_6'],squared=False)
print("For 6 point Moving Average Model forecast on the Training Data,  RMSE is %3.3f" %(rmse_model4_test_6))
​
## Test Data - RMSE --> 9 point Trailing MA
​
rmse_model4_test_9 = metrics.mean_squared_error(test['Births'],trailing_MovingAverage_test['Trailing_9'],squared=False)
print("For 9 point Moving Average Model forecast on the Training Data,  RMSE is %3.3f" %(rmse_model4_test_9))
resultsDf_4 = pd.DataFrame({'Test RMSE': [rmse_model4_test_2,rmse_model4_test_4
                                          ,rmse_model4_test_6,rmse_model4_test_9]}
                           ,index=['2pointTrailingMovingAverage','4pointTrailingMovingAverage'
                                   ,'6pointTrailingMovingAverage','9pointTrailingMovingAverage'])
​
resultsDf = pd.concat([resultsDf, resultsDf_4])
resultsDf
## Plotting on both Training and Test data
​
plt.plot(train['Births'], label='Train')
plt.plot(test['Births'], label='Test')
​
plt.plot(LinearRegression_test['RegOnTime'], label='Regression On Time_Training Data')
​
plt.plot(NaiveModel_test['naive'], label='Naive Forecast on Test Data')
​
plt.plot(SimpleAverage_test['mean_forecast'], label='Simple Average on Test Data')
​
plt.plot(trailing_MovingAverage_test['Trailing_2'], label='2 Point Trailing Moving Average on Training Set')
​
​
plt.legend(loc='best')
plt.title("Model Comparison Plots")
plt.grid();
END

# -------------------------------------------------------------------------------------------------------------
### GDPUS.ipynb

Reading time series data
df= pd.read_csv('GDPUS.csv')
df.head()
date = pd.date_range(start='01/01/1929', end='12/31/1991', freq='Y')
df['Year']=date
df=df.set_index('Year')
df.head()
rcParams['figure.figsize'] = 25,8
df.plot(grid=True);
Spliting time series data
Most recent observations will be used to test the model while remaining series will be used to train the model
if time series has seasonality, then test data must include atleast one seasonal period.
train             = df[:55] 
test              = df[55:]
print('Train')
display(train)
print('Test')
display(test)
Simple Exponential Smoothing
model_SES = SimpleExpSmoothing(train,initialization_method='estimated')
model_SES_fit1 = model_SES.fit(optimized=True)
Predicting forecast using trained models
SES_predict1 = model_SES_fit1.forecast(steps=len(test))
Plotting time searies and forecasts
plt.plot(train, label='Train')
plt.plot(test, label='Test')
plt.plot(SES_predict1,label='forecast')
​
plt.legend(loc='best')
plt.grid()
Double Exponential Smoothing / Holt's linear Method
model_DES = Holt(train,exponential=True, initialization_method='estimated')
training the double exponential model
model_DES_fit1 = model_DES.fit(optimized=True)
model_DES_fit1.summary()
Predicting forecast
DES_predict1 = model_DES_fit1.forecast(steps=len(test))
Lets plot the forecast
plt.plot(train, label='Train')
plt.plot(test, label='Test')
​
plt.plot(DES_predict1, label='DES forecast')
plt.legend(loc='best')
plt.grid()
mean_squared_error(test.values,DES_predict1.values,squared=False)
Defining Mean Absolute Percentage error
def MAPE(y_true, y_pred):
    return np.mean((np.abs(y_true-y_pred))/(y_true))*100
Mean Absolute Percentage Error for simple forecasting model
MAPE(test['GDP'],DES_predict1)
END

# -------------------------------------------------------------------------------------------------------------
### Exponential Smoothing Methods.ipynb

Exponential Smoothing methods
Exponential smoothing methods consist of flattening time series data.
Exponential smoothing averages or exponentially weighted moving averages consist of forecast based on previous periods data with exponentially declining influence on the older observations.
Exponential smoothing methods consist of special case exponential moving with notation ETS (Error, Trend, Seasonality) where each can be none(N), additive (N), additive damped (Ad), Multiplicative (M) or multiplicative damped (Md).
One or more parameters control how fast the weights decay.
These parameters have values between 0 and 1
# Importing the necessary packages

import pandas                          as      pd
import numpy                           as      np
import matplotlib.pyplot               as      plt
import statsmodels.tools.eval_measures as      em
from   sklearn.metrics                 import  mean_squared_error
from   statsmodels.tsa.api             import ExponentialSmoothing, SimpleExpSmoothing, Holt
from   IPython.display                 import display
from   pylab                           import rcParams
# Importing the necessary packages
​
import pandas                          as      pd
import numpy                           as      np
import matplotlib.pyplot               as      plt
import statsmodels.tools.eval_measures as      em
from   sklearn.metrics                 import  mean_squared_error
from   statsmodels.tsa.api             import ExponentialSmoothing, SimpleExpSmoothing, Holt
from   IPython.display                 import display
from   pylab                           import rcParams
Read the data.
df = pd.read_csv('AirPassenger.csv',parse_dates=True,index_col='Year-Month')
df.head()
rcParams['figure.figsize'] = 15,8
df.plot(grid=True);
Split the data into training and test. The data from 1957 should be training data.
train             = df[df.index<'1957'] 
test              = df[df.index>'1957']
# Printing the AirPassengers Data
print('Training Data')
display(train)
print('Test Data')
display(test)
SES - ETS(A, N, N) - Simple Exponential Smoothing with additive errors
The simplest of the exponentially smoothing methods is naturally called simple exponential smoothing (SES).
This method is suitable for forecasting data with no clear trend or seasonal pattern.
In Single ES, the forecast at time (t + 1) is given by Winters,1960

𝐹𝑡+1=𝛼𝑌𝑡+(1−𝛼)𝐹𝑡
Parameter 𝛼 is called the smoothing constant and its value lies between 0 and 1. Since the model uses only one smoothing constant, it is called Single Exponential Smoothing.

Note: Here, there is both trend and seasonality in the data. So, we should have directly gone for the Triple Exponential Smoothing but Simple Exponential Smoothing and the Double Exponential Smoothing models are built over here to get an idea of how the three types of models compare in this case.
SimpleExpSmoothing class must be instantiated and passed the training data.

The fit() function is then called providing the fit configuration, the alpha value, smoothing_level. If this is omitted or set to None, the model will automatically optimize the value.

# create class
model_SES = SimpleExpSmoothing(train,initialization_method='estimated')
# Fitting the Simple Exponential Smoothing model and asking python to choose the optimal parameters
model_SES_autofit = model_SES.fit(optimized=True)
## Let us check the parameters
​
model_SES_autofit.params
Here, Python has optimized the smoothing level to be almost 1.

# Using the fitted model on the training set to forecast on the test set
SES_predict = model_SES_autofit.forecast(steps=len(test))
SES_predict
## Plotting the Training data, Test data and the forecasted values
​
plt.plot(train, label='Train')
plt.plot(test, label='Test')
​
plt.plot(SES_predict, label='Alpha =0.99 Simple Exponential Smoothing predictions on Test Set')
​
plt.legend(loc='best')
plt.grid()
plt.title('Alpha = 0.99 Predictions');
## Mean Absolute Percentage Error (MAPE) - Function Definition
​
def MAPE(y_true, y_pred):
    return np.mean((np.abs(y_true-y_pred))/(y_true))*100
print('SES RMSE:',mean_squared_error(test.values,SES_predict.values,squared=False))
#different way to calculate RMSE
print('SES RMSE (calculated using statsmodels):',em.rmse(test.values,SES_predict.values)[0])
resultsDf = pd.DataFrame({'Test RMSE': [em.rmse(test.values,SES_predict.values)[0]]},index=['Alpha=0.99,SES'])
resultsDf
Holt - ETS(A, A, N) - Holt's linear method with additive errors
Double Exponential Smoothing
One of the drawbacks of the simple exponential smoothing is that the model does not do well in the presence of the trend.
This model is an extension of SES known as Double Exponential model which estimates two smoothing parameters.
Applicable when data has Trend but no seasonality.
Two separate components are considered: Level and Trend.
Level is the local mean.
One smoothing parameter α corresponds to the level series
A second smoothing parameter β corresponds to the trend series.
Double Exponential Smoothing uses two equations to forecast future values of the time series, one for forecating the short term avarage value or level and the other for capturing the trend.

Intercept or Level equation, 𝐿𝑡 is given by: 𝐿𝑡=𝛼𝑌𝑡+(1−𝛼)𝐹𝑡

Trend equation is given by 𝑇𝑡=𝛽(𝐿𝑡−𝐿𝑡−1)+(1−𝛽)𝑇𝑡−1

Here, 𝛼 and 𝛽 are the smoothing constants for level and trend, respectively,

0 <𝛼 < 1 and 0 < 𝛽 < 1.
The forecast at time t + 1 is given by

𝐹𝑡+1=𝐿𝑡+𝑇𝑡
𝐹𝑡+𝑛=𝐿𝑡+𝑛𝑇𝑡
# Initializing the Double Exponential Smoothing Model
model_DES = Holt(train,initialization_method='estimated')
# Fitting the model
model_DES = model_DES.fit()
​
print('')
print('==Holt model Exponential Smoothing Estimated Parameters ==')
print('')
print(model_DES.params)
# Forecasting using this model for the duration of the test set
DES_predict =  model_DES.forecast(len(test))
DES_predict
## Plotting the Training data, Test data and the forecasted values
​
plt.plot(train, label='Train')
plt.plot(test, label='Test')
​
plt.plot(SES_predict, label='Alpha=0.99:Simple Exponential Smoothing predictions on Test Set')
plt.plot(DES_predict, label='Alpha=0.099,Beta=0.0001:Double Exponential Smoothing predictions on Test Set')
​
plt.legend(loc='best')
plt.grid()
plt.title('Simple and Double Exponential Smoothing Predictions');
We see that the double exponential smoothing is picking up the trend component along with the level component as well.

print('DES RMSE:',mean_squared_error(test.values,DES_predict.values,squared=False))
resultsDf_temp = pd.DataFrame({'Test RMSE': [mean_squared_error(test.values,DES_predict.values,squared=False)]}
                           ,index=['Alpha=1,Beta=0.0189:DES'])
​
resultsDf = pd.concat([resultsDf, resultsDf_temp])
resultsDf
Inference
Here, we see that the Double Exponential Smoothing has actually done well when compared to the Simple Exponential Smoothing. This is because of the fact that the Double Exponential Smoothing model has picked up the trend component as well.

The Holt's model in Python has certain other options of exponential trends or whether the smoothing parameters should be damped. You can try these out later to check whether you get a better forecast.

Holt-Winters - ETS(A, A, A) - Holt Winter's linear method with additive errors
# Initializing the Double Exponential Smoothing Model
model_TES = ExponentialSmoothing(train,trend='additive',seasonal='additive',initialization_method='estimated')
# Fitting the model
model_TES = model_TES.fit()
​
print('')
print('==Holt Winters model Exponential Smoothing Estimated Parameters ==')
print('')
print(model_TES.params)
# Forecasting using this model for the duration of the test set
TES_predict =  model_TES.forecast(len(test))
TES_predict
## Plotting the Training data, Test data and the forecasted values
​
plt.plot(train, label='Train')
plt.plot(test, label='Test')
​
plt.plot(SES_predict, label='Alpha=1:Simple Exponential Smoothing predictions on Test Set')
plt.plot(DES_predict, label='Alpha=0.99,Beta=0.001:Double Exponential Smoothing predictions on Test Set')
plt.plot(TES_predict, label='Alpha=0.25,Beta=0.0,Gamma=0.74:Triple Exponential Smoothing predictions on Test Set')
​
plt.legend(loc='best')
plt.grid()
plt.title('Simple,Double and Triple Exponential Smoothing Predictions');
We see that the Triple Exponential Smoothing is picking up the seasonal component as well.

print('TES RMSE:',mean_squared_error(test.values,TES_predict.values,squared=False))
resultsDf_temp = pd.DataFrame({'Test RMSE': [mean_squared_error(test.values,TES_predict.values,squared=False)]}
                           ,index=['Alpha=0.25,Beta=0.0,Gamma=0.74:TES'])
​
resultsDf = pd.concat([resultsDf, resultsDf_temp])
resultsDf
Inference
Triple Exponential Smoothing has performed the best on the test as expected since the data had both trend and seasonality.

But we see that our triple exponential smoothing is under forecasting. Let us try to tweak some of the parameters in order to get a better forecast on the test set.

Holt-Winters - ETS(A, A, M) - Holt Winter's linear method
ETS(A, A, M) model

# Initializing the Double Exponential Smoothing Model
model_TES_am = ExponentialSmoothing(train,trend='add',seasonal='multiplicative',initialization_method='estimated')
# Fitting the model
model_TES_am = model_TES_am.fit()
​
print('')
print('==Holt Winters model Exponential Smoothing Estimated Parameters ==')
print('')
print(model_TES_am.params)
# Forecasting using this model for the duration of the test set
TES_predict_am =  model_TES_am.forecast(len(test))
TES_predict_am
## Plotting the Training data, Test data and the forecasted values
​
plt.plot(train, label='Train')
plt.plot(test, label='Test')
​
plt.plot(SES_predict, label='Alpha=1:Simple Exponential Smoothing predictions on Test Set')
plt.plot(DES_predict, label='Alpha=0.99,Beta=0.001:Double Exponential Smoothing predictions on Test Set')
plt.plot(TES_predict, label='Alpha=0.25,Beta=0.0,Gamma=0.74:Triple Exponential Smoothing predictions on Test Set')
plt.plot(TES_predict_am, label='Alpha=0.74,Beta=2.73e-06,Gamma=5.2e-07:Triple Exponential Smoothing predictions on Test Set')
​
plt.legend(loc='best')
plt.grid()
plt.title('Simple,Double and Triple Exponential Smoothing Predictions');
Report model accuracy
print('TES_am RMSE:',mean_squared_error(test.values,TES_predict_am.values,squared=False))
resultsDf_temp = pd.DataFrame({'Test RMSE': [mean_squared_error(test.values,TES_predict_am.values,squared=False)]}
                           ,index=['Alpha=0.74,Beta=2.73e-06,Gamma=5.2e-07,Gamma=0:TES'])
​
resultsDf = pd.concat([resultsDf, resultsDf_temp])
resultsDf
We see that the multiplicative seasonality model has not done that well when compared to the additive seasonality Triple Exponential Smoothing model.

There are various other parameters in the models. Please do feel free to play around with those in the hope of getting a better forecast on the test set.

END


# -------------------------------------------------------------------------------------------------------------
### champagne.ipynb

Reading time series data
df = pd.read_csv('champagne.csv')
df.head()
df.tail()
date = pd.date_range(start='01/01/1964', end='09/30/1972', freq='M')
df['Month']=date
df=df.set_index('Month')
Plotting time series
rcParams['figure.figsize'] = 25,8
df.plot(grid=True);
Spliting time series data
Most recent observations will be used to test the model while remaining series will be used to train the model
if time series has seasonality, then test data must include atleast one seasonal period.
train_end=datetime(1971,9,30)
test_end=datetime(1972,9,30)
train             = df[:train_end] 
test              = df[train_end + timedelta(days=1):test_end]
print('Train')
display(train)
print('Test')
display(test)
Double Exponential Smoothing / Holt's linear Method
model_DES = Holt(train,exponential=True, initialization_method='estimated')
training the double exponential model
model_DES_fit1 = model_DES.fit(optimized=True)
model_DES_fit1.summary()
Predicting forecast
DES_predict1 = model_DES_fit1.forecast(steps=len(test))
Lets plot the forecast
plt.plot(train, label='Train')
plt.plot(test, label='Test')
​
plt.plot(DES_predict1, label='DES forecats')
plt.legend(loc='best')
plt.grid()
Triple Exponential Smoothing / Holt-Winters Method
lets build model using 'additive' seasonality
model_TES_add = ExponentialSmoothing(train,trend='additive',seasonal='additive',initialization_method='estimated')
training the model
model_TES_add = model_TES_add.fit(optimized=True)
model_TES_add.summary()
predicting forecast
TES_add_predict =  model_TES_add.forecast(len(test))
lets plot foecast results
plt.plot(train, label='Train')
plt.plot(test, label='Test')
plt.plot(TES_add_predict, label='forecast')
plt.legend(loc='best')
plt.grid()
Root Mean Square Error for simple forecasting model
mean_squared_error(test.values,TES_add_predict.values,squared=False)
Defining Mean Absolute Percentage error
def MAPE(y_true, y_pred):
    return np.mean((np.abs(y_true-y_pred))/(y_true))*100
Mean Absolute Percentage Error for simple forecasting model
MAPE(test['Sales'],TES_add_predict)
END

# -------------------------------------------------------------------------------------------------------------
### ARMA_process.ipynb

#s

df=pd.read_csv('inflation.csv')
df.head()
df.tail()
date = pd.date_range(start='01/01/1980', end='12/31/2004', freq='M')
date
adding business dates to time series as a new column
df['Month']=date
df=df.set_index('Month')
df.head()
plotting time series
rcParams['figure.figsize'] = 25,8
df.plot(grid=True);
df.isna().value_counts()
Decomposing time series
df_decompose = seasonal_decompose(df, model = 'additive')
from pylab import rcParams
rcParams['figure.figsize'] = 14, 7
df_decompose.plot()
plt.show()
applying Adfuller test to check the stationarity
observations= df.values
test_result = adfuller(observations)
print('ADF Statistic: %f' % test_result[0])
print('p-value: %f' % test_result[1])
print('Critical Values:')
for key, value in test_result[4].items():
    print('\t%s: %.5f' % (key, value))
test results confirms that the series is stationary
Building ARMA model
To find p and q values of AR() and MA() processes, lets plot ACF and PACF
plot_acf(df);
plot_pacf(df);
Can select AR(2) and MA(2) process to build ARMA model
splittng time series into training and testing sets
train_end=datetime(2002,12,31)
test_end=datetime(2004,12,31)
train             = df[:train_end] 
test              = df[train_end + timedelta(days=1):test_end]
train.shape
building ARMA model
model=ARMA(train,(2,2))
model_fit=model.fit()
print(model_fit.summary())
predicting forecasts using the model
pred_start=test.index[0]
pred_end=test.index[-1]
pred_end
predictions=model_fit.predict(start=pred_start, end=pred_end)
predictions1=model_fit.forecast(12)
predictions1
lets plot actual series and forecast
plt.plot(train,label='Training Data')
plt.plot(test,label='Test Data')
plt.plot(test.index,predictions,label='Predicted Data - ARMA(1,0)')
plt.legend(loc='best')
plt.grid();
finding residuals
residuals = test.growth - predictions
plt.plot(residuals)
plt.show()
accuracy matrix
from sklearn.metrics import mean_squared_error
mean_squared_error(test.values,predictions.values,squared=False)
residual q-q plot for to check model performance
qqplot(residuals,line="s");
End


# -------------------------------------------------------------------------------------------------------------
### AR_processes

AR(1) process
from pylab import rcParams
rcParams['figure.figsize'] = 20, 10
​
ar = np.array([1,-0.33])
ma = np.array([1])
object1 = ArmaProcess(ar, ma)
simulated_data_1 = object1.generate_sample(nsample=150)
df1=pd.Series(simulated_data_1)
df1.plot()
plot_acf(df1);
plot_pacf(df1);
AR(2 process)
from pylab import rcParams
rcParams['figure.figsize'] = 20, 10
​
ar = np.array([1,-0.33,-0.5])
ma = np.array([1])
object1 = ArmaProcess(ar, ma)
simulated_data_1 = object1.generate_sample(nsample=150)
df2=pd.Series(simulated_data_1)
df2.plot()
plot_acf(df2);
plot_pacf(df2);
End


# -------------------------------------------------------------------------------------------------------------
### Additive and Multiplicative Model - Decomposition.ipynb

Time Series 1
import pandas as pd
df = pd.read_csv('D:/Gas.csv')
df.head()
df.drop('Unnamed: 0',axis=1,inplace=True)
df.head()
date = pd.date_range(start='1/1/1956', end='1/1/1996', freq='M')
date
df['Time_Stamp'] = pd.DataFrame(date)
df.head()
df.info()
df.set_index(keys='Time_Stamp',drop=True,inplace=True)
df.head()
df.plot(figsize=(15,8),grid=True);
Moving Average Decomposition
from    statsmodels.tsa.seasonal import   seasonal_decompose
from pylab import rcParams
rcParams['figure.figsize'] = 14, 7
​
decomposition = seasonal_decompose(df,model='additive')
decomposition.plot();
Time Series 2
import pandas as pd
df = pd.read_csv('D:/Sales_Souvenir.csv')
df.head()
df.shape
date = pd.date_range(start='1/1/1987', end='1/1/1994', freq='M')
date
df['Time_Stamp'] = pd.DataFrame(date)
df.head()
df.info()
df.set_index(keys='Time_Stamp',drop=True,inplace=True)
df.head()
df.plot(figsize=(15,8),grid=True);
Moving Average Decomposition
from pylab import rcParams
rcParams['figure.figsize'] = 14, 7
​
decomposition = seasonal_decompose(df,model='additive')
decomposition.plot();
from pylab import rcParams
rcParams['figure.figsize'] = 14, 7
​
decomposition = seasonal_decompose(df,model='multiplicative')
decomposition.plot();
END

# -------------------------------------------------------------------------------------------------------------
### ACF_PACF_Handson-updated.ipynb

Lag Plot
df = pd.read_excel('StockPrice.xlsx')
df.head()
df.tail()
date=pd.date_range(start="01/01/1981",end="31/12/1993",freq='M')
date
df['Month']=date
df=df.drop('Year',axis=1)
df=df.set_index('Month')
rcParams['figure.figsize'] = 25,8
df.plot()
pd.plotting.lag_plot(df, lag=1)
pd.plotting.lag_plot(df, lag=2)
pd.plotting.lag_plot(df, lag=3)
ACF anf PACF
ACF-PACF plot for random process with mean 0 and Std Dev 1
array = np.random.normal(0,1,150) 
array=pd.Series(array)
array.plot()
acf(array)
pacf(array)
plot_acf(array,lags=5);
plot_pacf(array,lags=5);
ACF-PACF plot for series with trend
df1= pd.read_csv('GDPUS.csv')
df1.head()
df1=df1.set_index('Year')
df1.plot()
acf(df1,nlags=20)
pacf(df1,nlags=20)
plot_acf(df1,lags=10);
plot_pacf(df1,lags=10);
ACF and PACF for seasonal data
df2= pd.read_csv('AirTemp.csv')
df2.head()
df2.tail()
date=pd.date_range(start='01/01/1920',end='31/12/1939',freq='M')
df2['Month']=date
df2=df2.drop('Year',axis=1)
df2=df2.set_index('Month')
df2.plot()
acf(df2)
pacf(df2)
plot_acf(df2,lags=15);
plot_pacf(df2,lags=15);
ACF and PACF for series with trend and seasonality
df3=pd.read_csv('champagne.csv')
df3.head()
df3.tail()
date=pd.date_range(start='01/01/1964',end='30/9/1972',freq='M')
df3['Month']=date
df3=df3.set_index('Month')
df3.plot()
plot_acf(df3,lags=15);
plot_pacf(df3,lags=15);
ACF and PACF for series with trend and multiplicative seasonality
df4 = pd.read_csv('AirPassenger.csv',parse_dates=True,index_col = 'Year-Month')
df4.head()
df4.plot()
plot_acf(df4,lags=15);
plot_pacf(df4,lags=15);
Differencing
1st order Differencing
df_1=df.diff().dropna()
df_1.plot(title='1st oder differencing')
Seasonal differencing
df2.plot()
df2_12=df2.diff(periods=12).dropna()
df2_12.plot()
df4_1=df4.diff(periods=1).dropna()
df4_1.plot()
df4_12=df4_1.diff(periods=12).dropna()
df4_12.plot()
​


# -------------------------------------------------------------------------------------------------------------
### Whatsapp_Inclass_assignment3.ipynb

read AirTemp data and convert it to time series
import pandas                             as      pd
import numpy                              as      np
import matplotlib.pyplot                  as      plt
import seaborn                            as      sns
from   IPython.display                    import  display
from   pylab                              import  rcParams 
from   datetime                           import  datetime, timedelta
from statsmodels.tsa.stattools            import  adfuller
from statsmodels.tsa.stattools            import  pacf
from statsmodels.tsa.stattools            import  acf
from statsmodels.graphics.tsaplots        import  plot_pacf
from statsmodels.graphics.tsaplots        import  plot_acf
from statsmodels.graphics.gofplots        import  qqplot
from statsmodels.tsa.seasonal             import  seasonal_decompose
from statsmodels.tsa.arima_model          import  ARIMA
from statsmodels.tsa.statespace.sarimax   import  SARIMAX
from statsmodels.tsa.api                  import  ExponentialSmoothing
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline
​
from pylab import rcParams
rcParams['figure.figsize'] = 15, 8
df = pd.read_csv('AirTemp.csv')
df.tail()
df['TimeSeries'] = pd.date_range(start='1/1/1920',end='12/31/1939',freq='M')
df.tail()
df.set_index(keys='TimeSeries',inplace=True,drop=True)
df.head()
df.drop(['Year','Month'],inplace=True,axis=1)
df.head()
plot the time series
df.plot(grid=True)
Check the stationarity of series using ADF test
testResult = adfuller(df.values)
print('ADF Statistic: %f' % testResult[0])
print('p-value: %f' % testResult[1])
print('Critical Values:')
for key, value in testResult[4].items():
    print('\t%s: %.5f' % (key, value))
0.0169 < 0.05
#p-value = 0.0169 < 0.05, so it failed the null hypothesis. Therefore, The data is stationary.
If series is stationary, using ACF and PACF plot find the values of p and q
plot_acf(df)
plotting PACF
plot_pacf(df)
Split the data into training and testing set
train_end = datetime(1938,12,31)
test_end = datetime(1939,12,31)
train = df[:train_end] 
test = df[train_end + timedelta(days=1):test_end]
​
Build ARMA model for selected p and q
import itertools
p = q = range(0, 4)
d = range(0,1)
pdq = list(itertools.product(p, d, q))
print('parameter combinations for the Model')
for i in range(1,len(pdq)):
    print('Model: {}'.format(pdq[i]))
dfObj1 = pd.DataFrame(columns=['param', 'AIC'])
for param in pdq:
            try:
                mod = ARIMA(train, order=param)
                results_Arima = mod.fit()
                print('ARIMA{} - AIC:{}'.format(param, results_Arima.aic))
                dfObj1 = dfObj1.append({'param':param, 'AIC': results_Arima.aic}, ignore_index=True)
​
            except:
                continue
dfObj1.sort_values(by=['AIC'])
model = ARIMA(train, order=(2,0,2))
​
results_Arima = model.fit()
​
print(results_Arima.summary())
Find predictions of model for the range of test data
ARIMA_predictions=results_Arima.predict(start=test.index[0], end=test.index[-1])
ARIMA_predictions
plt.plot(train,label='Training Data')
plt.plot(test,label='Test Data')
plt.plot(test.index,ARIMA_predictions,label='Predicted Data - ARIMA')
plt.legend(loc='best')
plt.grid()
Find residuals for the model and plot using Q-Q- plot
predict = pd.DataFrame(data=ARIMA_predictions,columns=test.columns,index=test.index)
predict.head()
residuals = test['AvgTemp'] - predict['AvgTemp']
qqplot(residuals,line="s")
​


# -------------------------------------------------------------------------------------------------------------
### Whatsapp_in_class_assign2.ipynb

Read retail turnover data
df_retail = pd.read_csv('RetailTurnover.csv')
df_retail.head()
df_retail['Time_Index'] = pd.date_range(start='9/1/1982', end='3/31/1992', freq='Q')
df_retail.head()
df_retail.set_index(keys='Time_Index',drop=True,inplace=True)
df_retail.head()
df_retail = df_retail.drop(['Year','Quarter'],axis=1)
df_retail.head()
df_retail.plot(figsize=(15,6),grid=True)
plt.show()
Decompose the series to identify trends and seasonality
decomp_add = seasonal_decompose(df_retail,model='add')
decomp_add.plot()
plt.show()
decomp_mul = seasonal_decompose(df_retail,model='mul')
decomp_mul.plot()
plt.show()
Split the time series data into training and testing sets
train_end = datetime(1991,3,31)
test_end = datetime(1992,3,31)
train   = df_retail[:train_end] 
test    = df_retail[train_end + timedelta(days=1):test_end]
train.tail()
test.head()
Based on the trend and seasonality apply the Smoothing technique
#Triple Exponential Smoothing
model_TES = ExponentialSmoothing(train, trend='add', seasonal='mul', initialization_method='estimated')
model_TES = model_TES.fit()
​
print('Exponential Smoothing Parameters:')
print(model_TES.params)
TES_predict =  model_TES.forecast(len(test))
TES_predict
plt.plot(train, label='Train')
plt.plot(test, label='Test')
plt.plot(TES_predict, label='Triple Exponential Smoothing predictions on Test Set')
​
plt.legend(loc='best')
plt.grid()
plt.title('Exponential Smoothing Predictions');
Find MAPE for your Model
print('TES MAPE:', metrics.mean_absolute_percentage_error(test.values, TES_predict.values))
​

# -------------------------------------------------------------------------------------------------------------
### TimeSeries_CaseStudy-Covid-19.ipynb

importing data
df=pd.read_csv('us_covid19_daily.csv',parse_dates=True)
df.head()
df.tail()
Data is collecetd for the period of 17th March 2020 to 06th December 2020. Data is collected on daily basis for Positive cases, Hospitalized and Death count
converting data into time series
date = pd.date_range(start='3/17/2020', end='12/6/2020', freq='D')
date
df['Time_Stamp'] = pd.DataFrame(date)
df=df.set_index('Time_Stamp')
df.head()
df.tail()
For this case study, we will build time series model to forecast the Hospitalized count
plotting variable Hospitalized
rcParams['figure.figsize'] = 15,8
df['Hospitalized'].plot()
df_final=df.drop(['Date','Positive','Death'],axis=1)
df_final.tail()
Checking for Null values
df_final.isnull().sum()
data does not have any missing values
Exploratory Data Analysis
rcParams['figure.figsize'] = 10,6
df_final.plot()
plotting box-plot for distribution of data
sns.boxplot(x = df_final.index.year,y = df_final['Hospitalized'])
plt.grid();
data does not show any skewness
plotting monthwise distribution
sns.boxplot(x = df_final.index.month,y = df_final['Hospitalized'])
plt.grid();
High variation in data can be observed in the month of November. Few outliers are present in the month of April
Decomposing time series
decomposition = seasonal_decompose(df_final, model = 'additive',period=7)
decomposition.plot()
plt.show()
decomposition = seasonal_decompose(df_final, model = 'multiplicative')
decomposition.plot()
plt.show()
Time series is showing trend as well as seasonality. Residual curve confirms that series is Multiplicative
Looking for stationarity
plotting monthly mean
monthly_mean = df_final.resample('M').mean()
monthly_mean.plot.bar()
Variation in monthly mean plot is indicating that series is non-stationary
lets plot rolling mean and std deviation
rolmean = df_final.rolling(window=15).mean()
rolstd = df_final.rolling(window=15).std()
orig = plt.plot(df_final, color='blue',label='Original')
mean = plt.plot(rolmean, color='red', label='Rolling Mean')
std = plt.plot(rolstd, color='black', label = 'Rolling Std')
plt.legend(loc='best')
plt.title('Rolling Mean & Standard Deviation')
plt.show()
both rolling mean and std deviation are changing over the period of time
statistical test to confirm the stationarity
observations= df_final.values
test_result = adfuller(observations)
print('ADF Statistic: %f' % test_result[0])
print('p-value: %f' % test_result[1])
print('Critical Values:')
for key, value in test_result[4].items():
    print('\t%s: %.5f' % (key, value))
Test result confirms that series is non-stationary
ACF and PACF plots for the series
plot_acf(df_final);
plot_pacf(df_final);
ACF plot is showing gradual decay whereas PACF plot cut-offs after forst two lags.
It seems that time series may have AR signature
Splitting series into training and testing sets
df_final.head()
df_final.tail()
train_end=datetime(2020,11,6)
test_end=datetime(2020,12,6)
train             = df_final[:train_end] 
test              = df_final[train_end + timedelta(days=1):test_end]
train.shape
test.shape
Model Selection
As the given time series is non-stationary, we will the forecasting model using ARIMA, SARIMA and SARIMAX model. We will also build the H-W forecasting model.
Let's start by building ARIMA model -- Although the data set has some seasonality and hence ARIMA is not the right option for making the model.
we will find the model parameters based on AIC criteria. Parameters will be generated using combination for the given range.
import itertools
p = q = range(0, 2)
d= range(0,2)
pdq = list(itertools.product(p, d, q))
​
model_pdq = [(x[0], x[1], x[2],7) for x in list(itertools.product(p, d, q))]
print('Examples of parameter combinations for Model...')
print('Model: {}{}'.format(pdq[1], model_pdq[1]))
print('Model: {}{}'.format(pdq[1], model_pdq[2]))
print('Model: {}{}'.format(pdq[2], model_pdq[3]))
print('Model: {}{}'.format(pdq[2], model_pdq[4]))
Creating an empty Dataframe with column names only where the model and AIC scores will be saved
dfObj1 = pd.DataFrame(columns=['param', 'AIC'])
dfObj1
model parameter selection using hypertuning
for param in pdq:
            try:
                mod = ARIMA(train, order=param)
                results_Arima = mod.fit()
                print('ARIMA{} - AIC:{}'.format(param, results_Arima.aic))
                dfObj1 = dfObj1.append({'param':param, 'AIC': results_Arima.aic}, ignore_index=True)
​
            except:
                continue
dfObj1.sort_values(by=['AIC'])
model = ARIMA(train, order=(1,1,1))
​
model_Arima = model.fit()
​
print(model_Arima.summary())
predicting results
pred_start=test.index[0]
pred_end=test.index[-1]
ARIMA_predictions=model_Arima.predict(start=pred_start, end=pred_end)
invert transformation
ARIMA_pred=ARIMA_predictions.cumsum()
ARIMA_pred=pd.DataFrame(ARIMA_pred,columns=train.columns)
df_fc = ARIMA_pred.copy()
columns = train.columns
for col in columns:        
        df_fc[str(col)+'_forecast'] = train[col].iloc[-1] + df_fc[str(col)]
df_fc.head()
plt.plot(train,label='Training Data')
plt.plot(test,label='Test Data')
plt.plot(test.index,df_fc['Hospitalized_forecast'],label='Predicted Data - ARIMA(1,1,1)')
plt.legend(loc='best')
plt.grid();
finding model residuals
residuals = test.Hospitalized - df_fc['Hospitalized_forecast']
qqplot(residuals,line="s");
sns.displot(residuals,bins=20)
distribution of residual plot confirms that model does not fit well with the seasonality series
Calculating RSME and MAPE
from math import sqrt
from sklearn.metrics import  mean_squared_error
rmse = sqrt(mean_squared_error(test.Hospitalized,df_fc['Hospitalized_forecast']))
print(rmse)
def MAPE(y_true, y_pred):
    return np.mean((np.abs(y_true-y_pred))/(y_true))*100
mape = MAPE(test.Hospitalized,df_fc['Hospitalized_forecast'])
print(mape)
creating new dataframe for storing the results
resultsDf = pd.DataFrame({'Test RMSE': rmse,'Test MAPE':mape}
                           ,index=['ARIMA(1,1,1)'])
​
resultsDf
Now to include seasonality, we will use SARIMA model
we will find the model parameters based on AIC criteria. Parameters will be generated using combination for the given range.
import itertools
p = q = range(0, 2)
d= range(0,2)
pdq = list(itertools.product(p, d, q))
​
model_pdq = [(x[0], x[1], x[2], 7) for x in list(itertools.product(p, d, q))]
print('Examples of parameter combinations for Model...')
print('Model: {}{}'.format(pdq[1], model_pdq[1]))
print('Model: {}{}'.format(pdq[1], model_pdq[2]))
print('Model: {}{}'.format(pdq[2], model_pdq[3]))
print('Model: {}{}'.format(pdq[2], model_pdq[4]))
Creating an empty Dataframe with column names only where the model and AIC scores will be saved
dfObj2 = pd.DataFrame(columns=['param','seasonal', 'AIC'])
dfObj2
model parameter selection using hypertuning
import statsmodels.api as sm
for param in pdq:
    for param_seasonal in model_pdq:
        mod = sm.tsa.statespace.SARIMAX(train,
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)
            
        results_SARIMA = mod.fit()
        print('SARIMA{}x{}7 - AIC:{}'.format(param, param_seasonal, results_SARIMA.aic))
        dfObj2 = dfObj2.append({'param':param,'seasonal':param_seasonal ,'AIC': results_SARIMA.aic}, ignore_index=True)
sorting parameters for best AIC score
dfObj2.sort_values(by=['AIC'])
SARIMA model parameters are selected as (1,1,1)(0,1,1,7)
model = sm.tsa.statespace.SARIMAX(train,
                                order=(1,1,1),
                                seasonal_order=(0,1,1,7),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
model_Sarima = model.fit()
print(model_Sarima.summary())
SARIMA_predictions=model_Sarima.predict(start=pred_start, end=pred_end)
plotting model predictions
plt.plot(train,label='Training Data')
plt.plot(test,label='Test Data')
plt.plot(test.index,df_fc['Hospitalized_forecast'],label='Predicted Data - ARIMA')
plt.plot(test.index,SARIMA_predictions,label='Predicted Data - SARIMA')
plt.legend(loc='best')
plt.grid();
It can be observed that SARIMA model is showing good seasonal considerations
finding RSMA and MAPE
rmse = sqrt(mean_squared_error(test.Hospitalized,SARIMA_predictions))
print(rmse)
mape = MAPE(test.Hospitalized,SARIMA_predictions)
print(mape)
resultsDfsarima = pd.DataFrame({'Test RMSE': rmse, 'Test MAPE':mape}
                           ,index=['SARIMA(1, 1, 1)(0, 1, 1)7'])
​
resultsDf = pd.concat([resultsDf, resultsDfsarima])
resultsDf
model residual analysis
model_Sarima.plot_diagnostics(figsize=(16, 8))
plt.show()
It can be observed that Model residuals are normally distributed and ACF plot also confirms that residuals are random
We will build SARIMAX model for forecasting Hospitalized count. For SARIMAX model,we will use Positive count as exog variable
ex=df[['Positive']]
ex
splitting exog variable into training and testing set
ex_train             = ex[:train_end]
ex_test              = ex[train_end + timedelta(days=1):test_end]
Creating an empty Dataframe with column names only where the model and AIC scores will be saved
dfObj3 = pd.DataFrame(columns=['param','seasonal', 'AIC'])
dfObj3
model parameter selection using hypertuning
import statsmodels.api as sm
for param in pdq:
    for param_seasonal in model_pdq:
        mod = sm.tsa.statespace.SARIMAX(train,exog=ex_train,
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)
            
        results_SARIMAX = mod.fit()
        print('SARIMA{}{} - AIC:{}'.format(param, param_seasonal, results_SARIMAX.aic))
        dfObj3 = dfObj3.append({'param':param,'seasonal':param_seasonal ,'AIC': results_SARIMAX.aic}, ignore_index=True)
sorting parameters for AIC score
dfObj3.sort_values(by=['AIC'])
We will build SARIMAX model of order (1,1,1)(0,1,1,7)
model = sm.tsa.statespace.SARIMAX(train,exog=ex_train,
                                order=(1,1,1),
                                seasonal_order=(0,1,1,7),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
model_sarimax = model.fit()
print(model_sarimax.summary())
model predictions
SARIMAX_predictions=model_sarimax.predict(start=pred_start, end=pred_end,exog=ex_test)
plt.plot(train,label='Training Data')
plt.plot(test,label='Test Data')
plt.plot(test.index,df_fc['Hospitalized_forecast'],label='Predicted Data - ARIMA')
plt.plot(test.index,SARIMA_predictions,label='Predicted Data - SARIMA')
plt.plot(test.index,SARIMAX_predictions,label='Predicted Data - SARIMAX')
plt.legend(loc='best')
plt.grid();
SARIMAX model is predicting results quite close to actual data
Residual analysis
model_sarimax.plot_diagnostics(figsize=(16, 8))
plt.show()
It can be observed that Model residuals are normally distributed and ACF plot also confirms that residuals are random
Finding RSMA and MAPE
rmse = sqrt(mean_squared_error(test.Hospitalized,SARIMAX_predictions))
print(rmse)
mape = MAPE(test.Hospitalized,SARIMAX_predictions)
print(mape)
resultsDf_temp = pd.DataFrame({'Test RMSE': rmse,'Test MAPE': mape}
                           ,index=['SARIMAX(1, 1, 1)(0, 1, 1)7'])
​
resultsDf = pd.concat([resultsDf, resultsDf_temp])
resultsDf
As series has seasonality and trend, lets try H-W model for forecasting Hospitalized count
model_TES_mul = ExponentialSmoothing(train,trend='additive',seasonal='multiplicative',initialization_method='estimated')
model_TES_mul = model_TES_mul.fit(smoothing_level=0.2, smoothing_trend=0.2, smoothing_seasonal=0.2 ,optimized=True)
TES_predictions =  model_TES_mul.forecast(len(test))
plt.plot(train,label='Training Data')
plt.plot(test,label='Test Data')
plt.plot(test.index,df_fc['Hospitalized_forecast'],label='Predicted Data - ARIMA')
plt.plot(test.index,SARIMA_predictions,label='Predicted Data - SARIMA')
plt.plot(test.index,SARIMAX_predictions,label='Predicted Data - SARIMAX')
plt.plot(test.index,TES_predictions,label='Predicted Data - TES')
plt.legend(loc='best')
plt.grid();
finding RSME and MAPE
rmse = sqrt(mean_squared_error(test.Hospitalized,TES_predictions))
print(rmse)
mape = MAPE(test.Hospitalized,TES_predictions)
print(mape)
resultsDf_temp = pd.DataFrame({'Test RMSE': rmse,'Test MAPE': mape}
                           ,index=['TES'])
​
resultsDf = pd.concat([resultsDf, resultsDf_temp])
resultsDf
Calculating and plotting residual
residuals = test.Hospitalized - TES_predictions
qqplot(residuals,line="s");
plot_acf(residuals);
Residual ACF plot confirms that residuals are not normally distribute and randomized
END

# -------------------------------------------------------------------------------------------------------------
### Time Series Forecasting_SARIMAX Case Study

Store id Day of Week Date Customers: the number of customers on a given day.(Target Variable) Open: an indicator for whether the store was open: 0 = closed, 1 = open. Promo: indicates whether a store is running a promo on that day. StateHoliday: indicates a state holiday. Normally all stores, with few exceptions, are closed on state holidays. This has value as "0", "a", "b", "c" SchoolHoliday: indicates if the (Store, Date) was affected by the closure of public schools.

# importing data
import os
os.chdir('D:/Academic Operations/DSBA - Python/Online/Time Series Forecasting/ARIMAX Case Study/Final')
​
Store50 = pd.read_excel("Store_50.xlsx", parse_dates = True, index_col = 'Date')
Store50.head()
print("The number of rows: ",Store50.shape[0], "\n""The number of columns: ",Store50.shape[1])
Store50_1044 = Store50[Store50.Store == 1044]['Customers']. sort_index(ascending=True)
Store50_1044.head()
plt.figure(figsize=(12,8))
plot_acf(Store50_1044,lags=50,  ax=plt.gca())
plt.show()
plt.figure(figsize=(12,8))
plot_pacf(Store50_1044, lags=50, ax=plt.gca())
plt.show()
## Seasonality after certain lags is visible. Every 7th day
### Data is being read again for model. This time no index is created while loading the data. First time when the data, index was used
## so that specific Explortory Data Analysis can be done.
Store50 = pd.read_excel("Store_50.xlsx",parse_dates=True)
# Extract customers only for store 1044 and the model would be built for this customer 
Store50_1044 = Store50[Store50.Store == 1044]
# reverse to the order: from 2013 to 2015
Store50_1044 = Store50_1044.sort_index(ascending = False)
​
​
Store50_1044.head()
Store50_1044.rename(columns = {"Day Of Week": "DayOfWeek", "State Holiday":"StateHoliday","School Holiday":"SchoolHoliday"}, 
                      inplace = True) 
Store50_1044['Date'] = pd.to_datetime(Store50_1044['Date'])
​
Store50_1044['year']= Store50_1044['Date'].dt.year
Store50_1044.head()
train=Store50_1044[Store50_1044['year'] !=2016]
test=Store50_1044[Store50_1044['year'] ==2016]
train_mod=train[['Date','Customers']]
test_mod=train[['Date','Customers']]
print(train.shape)
print(test.shape)
## Test for stationarity of the series - Dicky Fuller test
​
from statsmodels.tsa.stattools import adfuller
def test_stationarity(timeseries):
    
    #Determing rolling statistics
    rolmean = timeseries.rolling(window=7).mean()
    rolstd = timeseries.rolling(window=7).std()
​
    #Plot rolling statistics:
    orig = plt.plot(timeseries, color='blue',label='Original')
    mean = plt.plot(rolmean, color='red', label='Rolling Mean')
    std = plt.plot(rolstd, color='black', label = 'Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show(block=False)
    
    #Perform Dickey-Fuller test:
    print ('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    print (dfoutput,'\n')
test_stationarity(train['Customers'])
## Series is stationary and hence no need for differentiation
import itertools
p = q = range(0, 3)
d= range(0,1)
pdq = list(itertools.product(p, d, q))
model_pdq = [(x[0], x[1], x[2], 7) for x in list(itertools.product(p, d, q))]
print('Examples of parameter combinations for Model...')
print('Model: {}{}'.format(pdq[1], model_pdq[1]))
print('Model: {}{}'.format(pdq[1], model_pdq[2]))
print('Model: {}{}'.format(pdq[2], model_pdq[3]))
print('Model: {}{}'.format(pdq[2], model_pdq[4]))
# Creating an empty Dataframe with column names only
ARIMA_AIC = pd.DataFrame(columns=['param', 'AIC'])
print(ARIMA_AIC)
​
train['Customers']
from statsmodels.tsa.arima_model import ARIMA
​
for param in pdq:
    ARIMA_model = ARIMA(train['Customers'],order=param).fit()
    print('ARIMA{} - AIC:{}'.format(param,ARIMA_model.aic))
    ARIMA_AIC = ARIMA_AIC.append({'param':param, 'AIC': ARIMA_model.aic}, ignore_index=True)
ARIMA_AIC.sort_values(by='AIC',ascending=True)
## ARIMA(2,0,2) has the lowest AIC
mod = ARIMA(train['Customers'], order=(2,0,2))
​
results_Arima = mod.fit()
​
print(results_Arima.summary())
test.Customers= test.Customers.astype(float)
final_hat_avg =test.copy()
pred = results_Arima.forecast(steps=152)
from sklearn.metrics import  mean_squared_error
rmse = mean_squared_error(test.Customers,pred[0],squared=False)
print(rmse)
resultsDf = pd.DataFrame({'RMSE': [rmse]}
                           ,index=['ARIMA(2,0,2)'])
​
resultsDf
### As the dataset has seasonality.. Let's build the model with SARIMA
SARIMA_AIC = pd.DataFrame(columns=['param','seasonal', 'AIC'])
print(SARIMA_AIC)
SARIMA_AIC
import statsmodels.api as sm
​
for param in pdq:
    for param_seasonal in model_pdq:
        SARIMA_model = sm.tsa.statespace.SARIMAX(train['Customers'],
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)
            
        results_SARIMA = SARIMA_model.fit()
        print('SARIMA{}x{}7 - AIC:{}'.format(param, param_seasonal, results_SARIMA.aic))
        SARIMA_AIC = SARIMA_AIC.append({'param':param,'seasonal':param_seasonal ,'AIC': results_SARIMA.aic}, ignore_index=True)
        
SARIMA_AIC.sort_values(by=['AIC']).head()
import statsmodels.api as sm
​
## SARIMA(0, 0, 1)(2, 0, 2, 7)
mod = sm.tsa.statespace.SARIMAX(train['Customers'],
                                order=(0,0,1),
                                seasonal_order=(2, 0, 2, 7),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results_SARIMA = mod.fit()
print(results_SARIMA.summary())
results_SARIMA.plot_diagnostics(figsize=(16, 8))
plt.show()
test.head()
test.Customers= test.Customers.astype(float)
final_hat_avg =test.copy()
pred = results_SARIMA.get_forecast(steps=152)
pred.predicted_mean
pred.summary_frame()
from math import sqrt
from sklearn.metrics import mean_squared_error
rmse = sqrt(mean_squared_error(test.Customers ,pred.predicted_mean))
print(rmse)
temp_resultsDf = pd.DataFrame({'RMSE': [rmse]}
                           ,index=['SARIMA(0,0,1)(2,0,2)7'])
​
resultsDf = pd.concat([resultsDf, temp_resultsDf])
resultsDf
## To get the real forecast for 7 days, we will rerun the model on the complete dataset
​
mod = sm.tsa.statespace.SARIMAX(Store50_1044['Customers'],
                                order=(0,0,1),
                                seasonal_order=(2, 0, 2, 7),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results = mod.fit()
print(results.summary())
pred = results.get_forecast(steps=7)
pred.predicted_mean
pred.summary_frame()
SARIMAX Models
## This data set has exogeneous variables and hence the same should be considered while creating the model
## so to start with let's create a subset which only has exogeneous variables
​
ex_train=train[['Open','Promotion','StateHoliday','SchoolHoliday']]
ex_test=test[['Open','Promotion','StateHoliday','SchoolHoliday']]
## State variable has numeric character which has to be convered
ex_train["StateHoliday"].loc[ex_train["StateHoliday"] == "0"] = 0
ex_train["StateHoliday"].loc[ex_train["StateHoliday"] == "a"] = 1
ex_train["StateHoliday"].loc[ex_train["StateHoliday"] == "b"] = 2
ex_train["StateHoliday"].loc[ex_train["StateHoliday"] == "c"] = 3
ex_train.head()
ex_train.info()
ex_train['StateHoliday'] = ex_train['StateHoliday'].astype('int64')
ex_train.info()
## State variable has numeric character which has to be convered
ex_test["StateHoliday"].loc[ex_test["StateHoliday"] == "0"] = 0
ex_test["StateHoliday"].loc[ex_test["StateHoliday"] == "a"] = 1
ex_test["StateHoliday"].loc[ex_test["StateHoliday"] == "b"] = 2
ex_test["StateHoliday"].loc[ex_test["StateHoliday"] == "c"] = 3
ex_test.head()
ex_test.info()
ex_test['StateHoliday'] = ex_test['StateHoliday'].astype('int64')
ex_test.info()
SARIMAX_AIC = pd.DataFrame(columns=['param','seasonal', 'AIC'])
print(SARIMAX_AIC)
## Let's first use SARIMAX with exogenous variable 
​
for param in pdq:
    for param_seasonal in model_pdq:
        mod = sm.tsa.statespace.SARIMAX(train['Customers'],exog=ex_train,
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)
            
        results_SARIMAX = mod.fit()
        print('SARIMA{}{} - AIC:{}'.format(param, param_seasonal, results_SARIMAX.aic))
        SARIMAX_AIC = SARIMAX_AIC.append({'param':param,'seasonal':param_seasonal ,'AIC': results_SARIMAX.aic}, ignore_index=True)
​
SARIMAX_AIC.sort_values(by=['AIC']).head()
## SARIMA(1, 0, 2)(2, 0, 2, 7)
mod = sm.tsa.statespace.SARIMAX(train['Customers'],exog=ex_train,
                                order=(1,0,2),
                                seasonal_order=(2, 0, 2, 7),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results = mod.fit()
print(results.summary())
pred = results.get_forecast(steps=152,exog=ex_test)
pred.predicted_mean
rmse_SARIMAX = sqrt(mean_squared_error(test.Customers ,pred.predicted_mean))
print(rmse_SARIMAX)
temp_resultsDf = pd.DataFrame({'RMSE': [rmse_SARIMAX]}
                           ,index=['SARIMAX(1,0,2)(2,0,2)7'])
​
resultsDf = pd.concat([resultsDf, temp_resultsDf])
resultsDf
## Let's use SARIMAX with exogenous variable whose coefficients are allowed to vary over time 
## Time Varying Linear Model[TVLM] SARIMA(1, 0, 2)(2, 0, 2, 7)
mod = sm.tsa.statespace.SARIMAX(train['Customers'],exog=ex_train,time_varying_regression=True,mle_regression=False,
                                order=(1,0,2),
                                seasonal_order=(2, 0, 2, 7),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results = mod.fit()
print(results.summary())
pred = results.get_forecast(steps=152,exog=ex_test)
pred.predicted_mean
rmse_SARIMAX_timevarying = sqrt(mean_squared_error(test.Customers ,pred.predicted_mean))
print(rmse_SARIMAX_timevarying)
temp_resultsDf = pd.DataFrame({'RMSE': [rmse_SARIMAX_timevarying]}
                           ,index=['SARIMAX_tvlm(1,0,2)(2,0,2)7'])
​
resultsDf = pd.concat([resultsDf, temp_resultsDf])
resultsDf
ex_1044=Store50_1044[['Open','Promotion','StateHoliday','SchoolHoliday']]
## State variable has numeric character which has to be convered
ex_1044["StateHoliday"].loc[ex_1044["StateHoliday"] == "0"] = 0
ex_1044["StateHoliday"].loc[ex_1044["StateHoliday"] == "a"] = 1
ex_1044["StateHoliday"].loc[ex_1044["StateHoliday"] == "b"] = 2
ex_1044["StateHoliday"].loc[ex_1044["StateHoliday"] == "c"] = 3
ex_1044.head()
ex_1044.info()
ex_1044['StateHoliday'] = ex_1044['StateHoliday'].astype('int64')
ex_1044.info()
## To get the real forecast for 7 days, we will rerun the model on the complete dataset
​
mod = sm.tsa.statespace.SARIMAX(Store50_1044['Customers'],exog=ex_1044,
                                order=(1,0,2),
                                seasonal_order=(2, 0, 2, 7),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results = mod.fit()
print(results.summary())
Role of Exogenous variables is not to reduce errors but to ensure to consider the additional variables in a practical way.

Now let's verify if the order as we got it using ACF and PACF gives you a better model in terms of performance. So we will build two models with order=(0,0,0),seasonal_order=(1, 1,1, 7) and order=(0,0,1),seasonal_order=(1, 1,1, 7) for both SARIMAX with and without exogeneous variables seasonality value for P and Q is assumed to be one because as per ACF and PACF plot seasonality was visible for every 7th period. In our SARIMAX loop in the earlier part of code we have assumed d to be 0. With this we will verify if first order differentiation makes a difference in terms of value of p and q both for the order and seasonal order.

## SARIMA(0, 0, 0)(1,1,1, 7) 
mod = sm.tsa.statespace.SARIMAX(train['Customers'],
                                order=(0,0,0),
                                seasonal_order=(1, 1, 1, 7),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results = mod.fit()
print(results.summary())
test.Customers= test.Customers.astype(float)
final_hat_avg =test.copy()
pred = results.get_forecast(steps=152)
pred.predicted_mean
from math import sqrt
from sklearn.metrics import mean_squared_error
rms = sqrt(mean_squared_error(test.Customers ,pred.predicted_mean))
print(rms)
temp_resultsDf = pd.DataFrame({'RMSE': [rms]}
                           ,index=['SARIMA(0,0,0)(1,1,1)7'])
​
resultsDf = pd.concat([resultsDf, temp_resultsDf])
resultsDf
## SARIMA(0, 0, 1)(1,1,1, 7) 
mod = sm.tsa.statespace.SARIMAX(train['Customers'],
                                order=(0,0,1),
                                seasonal_order=(1, 1, 1, 7),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results = mod.fit()
print(results.summary())
test.Customers= test.Customers.astype(float)
final_hat_avg =test.copy()
pred = results.get_forecast(steps=152)
pred.predicted_mean
rms = sqrt(mean_squared_error(test.Customers ,pred.predicted_mean))
print(rms)
temp_resultsDf = pd.DataFrame({'RMSE': [rms]}
                           ,index=['SARIMA(0,0,1)(1,1,1)7'])
​
resultsDf = pd.concat([resultsDf, temp_resultsDf])
resultsDf
## Exogeneous with order = (0,0,0) and seasonal order (1,1,1,7)
mod = sm.tsa.statespace.SARIMAX(train['Customers'],exog=ex_train,
                                order=(0,0,0),
                                seasonal_order=(1, 1, 1, 7),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results = mod.fit()
print(results.summary())
pred = results.get_forecast(steps=152,exog=ex_test)
pred.predicted_mean
rms = sqrt(mean_squared_error(test.Customers ,pred.predicted_mean))
print(rms)
temp_resultsDf = pd.DataFrame({'RMSE': [rms]}
                           ,index=['SARIMAX(0,0,0)(1,1,1)7'])
​
resultsDf = pd.concat([resultsDf, temp_resultsDf])
resultsDf
## Exogeneous with order = (0,0,1) and seasonal order (1,1,1,7)
mod = sm.tsa.statespace.SARIMAX(train['Customers'],exog=ex_train,
                                order=(0,0,1),
                                seasonal_order=(1, 1, 1, 7),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results = mod.fit()
print(results.summary())
pred = results.get_forecast(steps=152,exog=ex_test)
pred.predicted_mean
rms = sqrt(mean_squared_error(test.Customers ,pred.predicted_mean))
print(rms)
temp_resultsDf = pd.DataFrame({'RMSE': [rms]}
                           ,index=['SARIMAX(0,0,1)(1,1,1)7'])
​
resultsDf = pd.concat([resultsDf, temp_resultsDf])
resultsDf
## Exogeneous with order = (0,0,1) and seasonal order (1,1,1,7) - TVLM
mod = sm.tsa.statespace.SARIMAX(train['Customers'],exog=ex_train,time_varying_regression=True,mle_regression=False,
                                order=(0,0,1),
                                seasonal_order=(1, 1, 1, 7),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
results = mod.fit()
print(results.summary())
pred = results.get_forecast(steps=152,exog=ex_test)
pred.predicted_mean
rms = sqrt(mean_squared_error(test.Customers ,pred.predicted_mean))
print(rms)
temp_resultsDf = pd.DataFrame({'RMSE': [rms]}
                           ,index=['SARIMAX_tvlm(0,0,1)(1,1,1)7'])
​
resultsDf = pd.concat([resultsDf, temp_resultsDf])
resultsDf
END


# -------------------------------------------------------------------------------------------------------------
### TSF.ipynb

Example 1
#Read the data 
df1 = pd.read_csv('AirPassenger.csv')
#Check data types
df1.dtypes
Year-Month column is not seen as a date object

#We are providing inputs to tell pandas that we are trying to work with time series.
df1 = pd.read_csv('AirPassenger.csv', parse_dates = ['Year-Month'])
df1.dtypes
Now the time series reference is approprately identified.

#It is recommended that we make our time series reference as the index
df1 = pd.read_csv('AirPassenger.csv', parse_dates = ['Year-Month'], index_col = 'Year-Month')
df1.head()
#We can conveniently do slicing i.e. obtain data for a specific time period.
df1['1951-04-01':'1952-03-01']
#We can check values corresponding to a specific time point
df1.loc['1960-05-01']
#Plot the time series
df1.plot()
plt.show()
#Increase the figure size
from pylab import rcParams
rcParams['figure.figsize'] = 12, 8
df1.plot()
plt.show()
We see an increasing trend and seasonality which is not constant in nature.

#Decompose the time series additively
df1_add_decompose = seasonal_decompose(df1, model = 'additive', period = 12)
df1_add_decompose.plot()
plt.show()
##Decompose the time series multiplicatively
df1_mul_decompose = seasonal_decompose(df1, model = "multiplicative")
df1_mul_decompose.plot()
plt.show()
#Let's try to do log transformation
df1_log = df1.copy()
df1_log['Pax'] = np.log(df1)
df1_log.Pax
#Visualize the log transformed series
df1_log.plot()
plt.show()
#Compare with the original series
plt.subplot(2,1,1)
plt.title('Original Time Series')
plt.plot(df1)
​
plt.subplot(2,1,2)
plt.title('Log Transformed Time Series')
plt.plot(df1_log)
plt.tight_layout()
Example 2
#Read the data
df2 = pd.read_csv('daily-total-female-births.csv', parse_dates = ['Date'], index_col = 'Date')
df2.head()
#Visualise the time series
df2.plot()
plt.show()
Doesn't show very clear trend and seasonality.

#Additive decomposition
df2_add_decompose = seasonal_decompose(df2, model = 'additive')
df2_add_decompose.plot()
plt.show()
#Let's inspect each component 
df2_add_decompose.trend
df2_add_decompose.seasonal
df2_add_decompose.resid
#Since this is an additive model:
#Observed = Trend + Seasonal + Irregular should hold true
35.142857 -3.077608 -1.065249
df2.head()
df2_add_decompose.resid.plot()
plt.show()
#Multiplicative decomposition
df2_mul_decompose = seasonal_decompose(df2, model = 'multiplicative')
df2_mul_decompose.plot()
plt.show()
df2_mul_decompose.resid.plot()
plt.show()
#Let's inspect each component
df2_mul_decompose.trend
df2_mul_decompose.seasonal
df2_mul_decompose.resid
#Since this is a multiplicative model:
#Observed = Trend*Seasonality*Irregular
35.14*.93*.952
Downsampling
#Let's change the monthly series to quarterly. This would require aggregation.
df1_q = df1.resample('Q').mean()
df1_q.plot()
Upsampling
#Let's change the monthly series to daily. 
df1_d = df1.resample('D').ffill()
df1_d['1949-02']
df1_d.plot()
#Let's change the monthly series to hourly. 
df1_h = df1.resample('H').interpolate()
df1_h
df1_h.plot()

# -------------------------------------------------------------------------------------------------------------
### Video+-+ARIMA+Models+-+Hands+on+Python+-+Code

Auto ARIMA
In an ARIMA model there are 3 parameters, namely p, q and d that help model major aspects of a time series: seasonality, trend and noise.

If our model has a seasonal component, we use Seasonal ARIMA with parameters, P, Q and D related to seasonal components of the model.

https://medium.com/@josemarcialportilla/using-python-and-auto-arima-to-forecast-seasonal-time-series-90877adff03c

auto.arima
The module auto.arima fits the best ARIMA model to univariate time series according to either AIC, AICc or BIC value. This function conducts a search over possible model within the order constraints provided.

AIC
The Akaike information criterion (AIC) is an estimator of the relative quality of statistical models for a given set of data. Given a collection of models for the data, AIC estimates the quality of each model, relative to each of the other models. Thus, AIC provides a means for model selection.

AICc is AIC with a correction for small sample sizes.
BIC
Bayesian information criterion (BIC) or Schwarz information criterion (also SIC, SBC, SBIC) is a criterion for model selection among a finite set of models; the model with the lowest BIC is preferred. It is based, in part, on the likelihood function and it is closely related to the Akaike information criterion (AIC).

https://en.wikipedia.org/wiki/Akaike_information_criterion#Comparison_with_BIC

https://en.wikipedia.org/wiki/Bayesian_information_criterion

Example 3
We use tractor sales data to replicate auto.arima in python.

import sys
import warnings
import itertools
warnings.filterwarnings("ignore")
​
import pandas as pd
import numpy as np
​
import statsmodels.api as sm
import statsmodels.tsa.api as smt
import statsmodels.formula.api as smf
​
import matplotlib.pyplot as plt
%matplotlib inline
data = pd.read_csv("TractorSales-1.csv")
data.head(5)
dates = pd.date_range(start='2003-01-01', freq='MS', periods=len(data))
#This particular 'calendar' library lets us play around with the Time Stamp and lets us extract various 
#features from the time stamp
import calendar
data['Month'] = dates.month
data['Month'] = data['Month'].apply(lambda x: calendar.month_abbr[x])
data['Year'] = dates.year
data.drop(['Month-Year'], axis=1, inplace=True)
data.rename(columns={'Number of Tractor Sold':'Tractor-Sales'}, inplace=True)
data = data[['Month', 'Year', 'Tractor-Sales']]
data.set_index(dates, inplace=True)
data
# extract out the time-series
sales_ts = data['Tractor-Sales']
sales_ts.head()
plt.figure(figsize=(8, 4))
plt.plot(sales_ts)
plt.xlabel('Years')
plt.ylabel('Tractor Sales')
plt.show()
Inference
We observe both trend and multiplicative seasonaliy from the plot shown above.

We try moving averages of various window widths such as 4, 6,8 and 12.

fig, axes = plt.subplots(2, 2, sharey=False, sharex=False)
fig.set_figwidth(14)
fig.set_figheight(8)
​
axes[0][0].plot(sales_ts.index, sales_ts, label='Original')
axes[0][0].plot(sales_ts.index, sales_ts.rolling(window=4).mean(), label='4-Months Rolling Mean')
axes[0][0].set_xlabel("Years")
axes[0][0].set_ylabel("Number of Tractor's Sold")
axes[0][0].set_title("4-Months Moving Average")
axes[0][0].legend(loc='best')
​
axes[0][1].plot(sales_ts.index, sales_ts, label='Original')
axes[0][1].plot(sales_ts.index, sales_ts.rolling(window=6).mean(), label='6-Months Rolling Mean')
axes[0][1].set_xlabel("Years")
axes[0][1].set_ylabel("Number of Tractor's Sold")
axes[0][1].set_title("6-Months Moving Average")
axes[0][1].legend(loc='best')
​
axes[1][0].plot(sales_ts.index, sales_ts, label='Original')
axes[1][0].plot(sales_ts.index, sales_ts.rolling(window=8).mean(), label='8-Months Rolling Mean')
axes[1][0].set_xlabel("Years")
axes[1][0].set_ylabel("Number of Tractor's Sold")
axes[1][0].set_title("8-Months Moving Average")
axes[1][0].legend(loc='best')
​
axes[1][1].plot(sales_ts.index, sales_ts, label='Original')
axes[1][1].plot(sales_ts.index, sales_ts.rolling(window=12).mean(), label='12-Months Rolling Mean')
axes[1][1].set_xlabel("Years")
axes[1][1].set_ylabel("Number of Tractor's Sold")
axes[1][1].set_title("12-Months Moving Average")
axes[1][1].legend(loc='best')
​
plt.tight_layout()
plt.show()
#Determing rolling statistics
​
rolmean = sales_ts.rolling(window = 4).mean()
rolstd = sales_ts.rolling(window = 4).std()
#Plot rolling statistics:
orig = plt.plot(sales_ts, label='Original')
mean = plt.plot(rolmean, label='Rolling Mean')
std = plt.plot(rolstd, label = 'Rolling Std')
plt.legend(loc='best')
plt.title('Rolling Mean & Standard Deviation')
plt.show()
Augmented Dickey-Fuller Test - Let's run the Augmented Dicky Fuller Test on the timeseries and verify the null hypothesis that the TS is non-stationary.

from statsmodels.tsa.stattools import adfuller
dftest = adfuller(sales_ts)
dftest
print('DF test statistic is %3.3f' %dftest[0])
print('DF test p-value is %1.4f' %dftest[1])
Though the variation in standard deviation is small, rolling mean is clearly increasing with time and this is not a stationary series. Also, the test statistic is way more than the critical values.

As we observed while plotting the moving average over months that there is a monthly pattern. Let us try to decipher the seasonal component.

Seasonality – Time Series Decomposition
Observe how number of tractors sold vary on a month on month basis. We will plot a stacked annual plot to observe seasonality in our data.

monthly_sales_data = pd.pivot_table(data, values = "Tractor-Sales", columns = "Year", index = "Month")
monthly_sales_data
#Second method to create the same pivot table
​
monthly_sales_data = monthly_sales_data.reindex(index = ['Jan','Feb','Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
monthly_sales_data
monthly_sales_data.plot();
yearly_sales_data = pd.pivot_table(data, values = "Tractor-Sales", columns = "Month", index = "Year")
yearly_sales_data = yearly_sales_data[['Jan','Feb','Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']]
yearly_sales_data
yearly_sales_data.plot();
yearly_sales_data.boxplot();
Inferences
The tractor sales have been increasing without fail every year. July and August are the peak months for tractor sales and the variance and the mean value in July and August are also much higher than any of the other months. We can see a seasonal cycle of 12 months where the mean value of each month starts with a increasing trend in the beginning of the year and drops down towards the end of the year. We can see a seasonal effect with a cycle of 12 months.

Time Series Decomposition
decomposition = sm.tsa.seasonal_decompose(sales_ts, model='multiplicative')
fig = decomposition.plot()
fig.set_figwidth(8)
fig.set_figheight(6)
fig.suptitle('Decomposition of multiplicative time series')
plt.show()
Some of our key observations from this analysis:
1) Trend: 12-months moving average looks quite similar to a straight line hence we could have easily used linear regression to estimate the trend in this data.

2) Seasonality: Seasonal plot displays a fairly consistent month-on-month pattern. The monthly seasonal components are average values for a month after removal of trend. Trend is removed from the time series using the following formula:

Seasonality_t × Remainder_t = Y_t/Trend_t

3) Irregular Remainder (random): is the residual left in the series after removal of trend and seasonal components. Remainder is calculated using the following formula:

Remainder_t = Y_t / (Trend_t × Seasonality_t)

plt.figure(figsize=(8, 4))
plt.plot(sales_ts.diff(periods=1))
plt.xlabel('Years')
plt.ylabel('Tractor Sales');
We observe seasonality even after differencing.

plt.figure(figsize=(8, 4))
plt.plot(np.log10(sales_ts))
plt.xlabel('Years')
plt.ylabel('Log (Tractor Sales)');
We observe trend and seasonality even after taking log of the observations.

plt.figure(figsize=(10, 5))
plt.plot(np.log10(sales_ts).diff(periods=1))
plt.xlabel('Years')
plt.ylabel('Differenced Log (Tractor Sales)');
sales_ts_log = np.log10(sales_ts)
sales_ts_log.dropna(inplace=True)
​
sales_ts_log_diff = sales_ts_log.diff(periods=1) # same as ts_log_diff = ts_log - ts_log.shift(periods=1)
sales_ts_log_diff.dropna(inplace=True)
fig, axes = plt.subplots(1, 2)
fig.set_figwidth(12)
fig.set_figheight(4)
smt.graphics.plot_acf(sales_ts_log, lags=30, ax=axes[0])
smt.graphics.plot_pacf(sales_ts_log, lags=30, ax=axes[1])
plt.tight_layout()
Nonstationary series have an ACF that remains significant for half a dozen or more lags, rather than quickly declining to zero. You must difference such a series until it is stationary before you can identify the process

The above ACF is “decaying”, or decreasing, very slowly, and remains well above the significance range (blue band) for at least a dozen lags. This is indicative of a non-stationary series.

fig, axes = plt.subplots(1, 2)
fig.set_figwidth(12)
fig.set_figheight(4)
plt.xticks(range(0,30,1), rotation = 90)
smt.graphics.plot_acf(sales_ts_log_diff, lags=30, ax=axes[0])
smt.graphics.plot_pacf(sales_ts_log_diff, lags=30, ax=axes[1])
plt.tight_layout()
Inference
The above ACF has “decayed” fast and remains within the significance range (blue band) except for a few (5) lags. This is indicative of a stationary series.

# Define the p, d and q parameters to take any value between 0 and 2
p = d = q = range(0, 2)
​
# Generate all different combinations of p, d and q triplets
pdq = list(itertools.product(p, d, q))
​
# Generate all different combinations of seasonal p, q and q triplets
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
pdq
seasonal_pdq
#Separate data into train and test
data['date'] = data.index
train = data[data.index < '2013-01-01']
test = data[data.index >= '2013-01-01']
train_sales_ts_log = np.log10(train['Tractor-Sales'])
best_aic = np.inf
best_pdq = None
best_seasonal_pdq = None
temp_model = None
for param in pdq:#looping through the (p,d,q) values for ARIMA
    for param_seasonal in seasonal_pdq:#looping through the (P,D,Q,freq) values for SARIMA
        
        try:
            temp_model = sm.tsa.statespace.SARIMAX(train_sales_ts_log,#defining the SARIMA model after taking
                                                   # the logarithm of the training data
                                             order = param,#setting the (p,d,q) values
                                             seasonal_order = param_seasonal,#setting the (P,D,Q,freq) values
                                             enforce_stationarity=True)
            results = temp_model.fit()#fitting the above built SARIMA model
​
            
            if results.aic < best_aic:#defining a conditional statement about whether the AIC of the model
                #just built is less than the best_aic
                best_aic = results.aic#defining the new value of AIC from the SARIMA model as the best_aic
                best_pdq = param#storing the (p,d,q) values in the variable best_pdq
                best_seasonal_pdq = param_seasonal#storing the (P,D,Q,freq) values in the variable 
                #best_seasonal_pdq
        except:
            #print("Unexpected error:", sys.exc_info()[0])
            continue
print("Best SARIMAX{}x{}12 model - AIC:{}".format(best_pdq, best_seasonal_pdq, best_aic))
Inference
The best fit model is selected based on Akaike Information Criterion (AIC) , and Bayesian Information Criterion (BIC) values. The idea is to choose a model with minimum AIC and BIC values.
For ARIMA(p, d, q) × (P, D, Q)S, we got SARIMAX(0, 1, 1)x(1, 0, 1, 12)12 model with the least AIC:-600.0908420381976

Here,

p = non-seasonal AR order = 0,
d = non-seasonal differencing = 1,
q = non-seasonal MA order = 1,
P = seasonal AR order = 1,
D = seasonal differencing = 0,
Q = seasonal MA order = 1,
S = time span of repeating seasonal pattern = 12
Predict sales on in-sample date using the best fit ARIMA model
best_model = sm.tsa.statespace.SARIMAX(train_sales_ts_log,
                                      order=(0, 1, 1),
                                      seasonal_order=(1, 0, 1, 12),
                                      enforce_stationarity=True)
best_results = best_model.fit()
print(best_results.summary().tables[0])
print(best_results.summary().tables[1])
pred_dynamic = best_results.get_prediction(start=pd.to_datetime('2012-01-01'), dynamic=True, full_results=True)
pred_dynamic_ci = pred_dynamic.conf_int()
pred99 = best_results.get_forecast(steps=24, alpha=0.1)
# Extract the predicted and true values of our time series
sales_ts_forecasted = pred_dynamic.predicted_mean
testCopy = test.copy()
#we need to change the scale of the logarithmic scale to the original scale by raising the predicted values
#to the power of 10
testCopy['sales_ts_forecasted'] = np.power(10, pred99.predicted_mean)
testCopy
# Compute the root mean square error
mse = ((testCopy['Tractor-Sales'] - testCopy['sales_ts_forecasted']) ** 2).mean()
rmse = np.sqrt(mse)
print('The Root Mean Squared Error of our forecasts is {}'.format(round(rmse, 3)))
axis = train['Tractor-Sales'].plot(label='Train Sales', figsize=(10, 6))
testCopy['Tractor-Sales'].plot(ax=axis, label='Test Sales', alpha=0.7)
testCopy['sales_ts_forecasted'].plot(ax=axis, label='Forecasted Sales', alpha=0.7)
axis.set_xlabel('Years')
axis.set_ylabel('Tractor Sales')
plt.legend(loc='best')
plt.show()
plt.close()
Forecast sales using the best fit ARIMA model
# Get forecast 36 steps (3 years) ahead in future
n_steps = 36
pred_uc_99 = best_results.get_forecast(steps=36, alpha=0.01) # alpha=0.01 signifies 99% confidence interval
pred_uc_95 = best_results.get_forecast(steps=36, alpha=0.05) # alpha=0.05 signifies 95% confidence interval
​
# Get confidence intervals 95% & 99% of the forecasts
pred_ci_99 = pred_uc_99.conf_int()
pred_ci_95 = pred_uc_95.conf_int()
n_steps = 36
​
idx = pd.date_range(data.index[-1], periods=n_steps, freq='MS')#defining the date range for 3 years
#into the future
​
fc_95 = pd.DataFrame(np.column_stack([np.power(10, pred_uc_95.predicted_mean), np.power(10, pred_ci_95)]), 
                     index=idx, columns=['forecast', 'lower_ci_95', 'upper_ci_95'])#creating a data frame
#by raising the results to the appropriate power for suitable predicted values - For 95% confidence interval
​
fc_99 = pd.DataFrame(np.column_stack([np.power(10, pred_ci_99)]), 
                     index=idx, columns=['lower_ci_99', 'upper_ci_99'])#creating a data frame
#by raising the results to the appropriate power for suitable predicted values - For 99% confidence interval
​
fc_all = fc_95.combine_first(fc_99)
​
fc_all = fc_all[['forecast', 'lower_ci_95', 'upper_ci_95', 'lower_ci_99', 'upper_ci_99']]# just reordering 
#columns
​
fc_all.head()
# plot the forecast along with the confidence band
​
axis = sales_ts.plot(label='Observed', figsize=(8, 4))
fc_all['forecast'].plot(ax=axis, label='Forecast', alpha=0.7)
axis.fill_between(fc_all.index, fc_all['lower_ci_95'], fc_all['upper_ci_95'], color='k', alpha=.15)
axis.set_xlabel('Years')
axis.set_ylabel('Tractor Sales')
plt.legend(loc='best')
plt.show()
Plot ACF and PACF for residuals of ARIMA model to ensure no more information is left for extraction
best_results.plot_diagnostics(lags=30, figsize=(16,12))
plt.show()
Inference
We need to ensure that the residuals of our model are uncorrelated and normally distributed with zero-mean. If it is not that it signifies that the model can be further improved and we repeat the process with the residuals.

In this case, our model diagnostics suggests that the model residuals are normally distributed based on the following:

The KDE plot of the residuals on the top right is almost similar with the normal distribution.
The qq-plot on the bottom left shows that the ordered distribution of residuals (blue dots) follows the linear trend of the samples taken from a standard normal distribution with N(0, 1). Again, this is a strong indication that the residuals are normally distributed.
The residuals over time (top left plot) don't display any obvious seasonality and appear to be white noise. This is confirmed by the autocorrelation (i.e. correlogram) plot on the bottom right, which shows that the time series residuals have low correlation with lagged versions of itself.
Those observations coupled with the fact that there are no spikes outside the insignificant zone for both ACF and PACF plots lead us to conclude that that residuals are random with no information or juice in them and our model produces a satisfactory fit that could help us understand our time series data and forecast future values. It sems that our ARIMA model is working fine.

END

# -------------------------------------------------------------------------------------------------------------
### Video - Time Series Analysis_EDA_Hands-on - Code

Store id Day of Week Date Customers: the number of customers on a given day.(Target Variable) Open: an indicator for whether the store was open: 0 = closed, 1 = open. Promo: indicates whether a store is running a promo on that day. StateHoliday: indicates a state holiday. Normally all stores, with few exceptions, are closed on state holidays. This has value as "0", "a", "b", "c" SchoolHoliday: indicates if the (Store, Date) was affected by the closure of public schools.

# importing data
Store50 = pd.read_excel("D:/Store_50.xlsx", parse_dates = True, index_col = 'Date')
Store50.head()
# Check if date has been defined as an index
Store50.index
print("The number of rows: ",Store50.shape[0], "\n""The number of columns: ",Store50.shape[1])
#Let us extract some additional features
#Creating separate columns for 'Year','Month','Day' and 'WeekofYear'
Store50['Year'] = Store50.index.year
Store50['Month'] = Store50.index.month
Store50['Day'] = Store50.index.day
Store50['WeekOfYear'] = Store50.index.weekofyear
Store50.head()
## Plot ECDF: Empirical Cumulative Distribution Function
#ECDF - Adds up the number of observations that are there for a certain value.
sns.set(style = "ticks")# to format into seaborn 
c = '#386B7F' # basic color for plots
plt.figure(figsize = (12, 6))
​
  
plt.subplot(312)
cdf = ECDF(Store50['Customers'])
plt.plot(cdf.x, cdf.y, label = "statmodels", color = c)
plt.xlabel('Customers');
About 20-25% of the values are zero for customers.. May be the store was closed on that day

## Let us check if we have records where the store was open and customer count/foot-fall was zero
​
Store50[(Store50.Open == 1) & (Store50.Customers == 0)]
​
As such records are less and we do not know the specific reason why there was no customer even if store was open, we are not deleting such records.

Store50.isnull().sum()
No Missing Values are present in the data.

## Rename Columns to remove space
​
Store50.rename(columns = {"Day Of Week": "DayOfWeek", "State Holiday":"StateHoliday","School Holiday":"SchoolHoliday"}, 
                      inplace = True) 
Store50.head()
Store50.info()
# Customer trends based on day of week and promotion
sns.catplot(data = Store50, x = 'Month', y = "Customers", 
               col = 'DayOfWeek', # Day of Week
               palette = 'plasma',
               row = 'Promotion', # per promotion in the store in rows
               kind = 'box', 
               color = c) 
​
plt.show()
Impact of the promotion is clearly visible even across month.. Day1 , Month 1, Promotion=1, customer count is high.. However for December, no impact of promotion.

## Let us check if we have stores which are open on Sundays
​
Store50[(Store50.Open == 1) & (Store50.DayOfWeek == 7)]['Store'].unique()
fig, (axis1) = plt.subplots(1,1,figsize=(15,4))
sns.countplot(x='Open',hue='DayOfWeek', data=Store50,palette="husl", ax=axis1);
Even when the store was closed we see that the footfall count is high on Sunday Even for other days when store was not open, the count of customers is not zero.

# group by date and get average Customers, and precent change
average_customers    = Store50.groupby('Date')["Customers"].mean()
pct_change_customers = Store50.groupby('Date')["Customers"].sum().pct_change()
​
fig, (axis1,axis2) = plt.subplots(2,1,sharex=True,figsize=(15,8))
​
# plot average Customers over time(year-month)
ax1 = average_customers.plot(legend=True,ax=axis1,marker='o',title="Average Customers")
ax1.set_xticks(range(len(average_customers)))
ax1.set_xticklabels(average_customers.index.tolist(), rotation=90)
# plot precent change for Customers over time(year-month)
ax2 = pct_change_customers.plot(legend=True,ax=axis2,marker='o',rot=90,colormap="summer",title="Customer Percent Change")
​
Much of the variation is visible across specific days of the week and specific months in a year.

## Plot average customers for every year
fig, (axis1) = plt.subplots(1,figsize=(15,4))
​
sns.barplot(x='Year', y='Customers', data=Store50, ax=axis1);
There is not much variation for the customer footfall per year.

# Plot average customers with and without promo
fig, (axis1) = plt.subplots(1,figsize=(15,4))
​
sns.barplot(x='Promotion', y='Customers', data=Store50, ax=axis1);
​
Having a Promotion does have an impact on the customer count.

# StateHoliday
​
# StateHoliday column has values 0 & "0", So, we need to merge values with 0 to "0"
Store50["StateHoliday"].loc[Store50["StateHoliday"] == 0] = "0"
​
#Plotting the count of different types of State Holidays
sns.countplot(x='StateHoliday', data=Store50);
​
fig, (axis1,axis2) = plt.subplots(1,2,figsize=(15,4))
​
#Plotting a barplot of Customers with respect to different types of State Holiday
sns.barplot(x='StateHoliday', y='Customers', data=Store50, ax=axis1,ci=None);
​
#Plotting an instance when the State Holiday is not equal 0 but the Customer count is 0
mask = (Store50["StateHoliday"] != "0") & (Store50["Customers"] > 0)
sns.barplot(x='StateHoliday', y='Customers', data=Store50[mask], ax=axis2,ci=None);
​
Customer count is highest when Stateholiday=0.

# SchoolHoliday
​
# Plotting the count of School Holidays
sns.countplot(x='SchoolHoliday', data=Store50);
​
fig, (axis1) = plt.subplots(1,figsize=(15,4))
​
#Plotting the average number of Customers with respect to the School Holiday
sns.barplot(x='SchoolHoliday', y='Customers', data=Store50, ax=axis1);
​
When there is a school holiday, the customer count is more.

corr_all = Store50.drop('DayOfWeek', axis = 1).corr()
mask = np.array(corr_all)
mask[np.tril_indices_from(mask)] = False
fig,ax= plt.subplots()
fig.set_size_inches(15,8)
sns.heatmap(corr_all, mask=mask,vmax=.9, square=True,annot=True);
plt.show()
Open and Customers are highly correlated - This was expected. Day of the week is dropped from this correlation plot as ideally Day of the Week is a categorical type of variable Similarly Month, Day, Year should be read with respect to negative values, as these are being considered as integer wherein the values does not represent any kind of order

## We are considering the first store i.e. Store id = 1044
​
# store types
Store50_1044 = Store50[Store50.Store == 1044]['Customers']. sort_index(ascending=True)
f, (ax1) = plt.subplots(1, figsize = (12, 8))
Store50_1044.resample('W').sum().plot(color = c, ax = ax1)
​
plt.show()
​
Seasonality does exists in the data set. The store had a peak in December and May.

# Let's check the trend in the data set
decomposition_a = seasonal_decompose(Store50_1044, model = 'additive', freq = 365)
f, (ax1) = plt.subplots(1, figsize = (12, 8))
decomposition_a.trend.plot(color = c, ax = ax1)
plt.show()
There seems to be an increase in customer footfall year on year.

END

# -------------------------------------------------------------------------------------------------------------
### Video - Moving Average Code Walkthrough - Code
Moving average forecast
Moving Average Smoothing is a naive and effective technique in time series forecasting.

Smoothing is a technique applied to time series to remove the fine-grained variation between time steps.

Calculating a moving average involves creating a new series where the values are comprised of the average of raw observations in the original time series.

A moving average requires that you specify a window size called the window width. This defines the number of raw observations used to calculate the moving average value.

Two main types of moving averages:
1) Centered moving average - calculated as the average of raw observations at, before and after time, t.
2) Trailing moving average - uses historical observations and is used on time series forecasting.
The rolling() function on the Series Pandas object will automatically group observations into a window.

You can specify the window size, and by default, a trailing window is created. Once the window is created, we can use the mean value, which forms our transformed dataset.

Example 8
Average and moving average for Air Temp data
from    pandas                   import   read_csv, Grouper, DataFrame, concat
### Load required libraries
​
from    pandas                   import   read_csv, Grouper, DataFrame, concat
import  matplotlib.pyplot        as       plt
from    datetime                 import   datetime
import  pandas                   as       pd
​
AirTemp              =  pd.read_csv('D:/AirTemp.csv')
date_rng             =  pd.date_range(start='1/1/1920', end='31/12/1939', freq='M')
AirTemp['TimeIndex'] = pd.DataFrame(date_rng, columns=['Month'])
AirTemp.head()
Plot the average temp
plt.plot(AirTemp.TimeIndex, AirTemp.AvgTemp,label='AvgTemp')
plt.legend(loc='best')
plt.show()
Plot the average forecast
temp_avg                 = AirTemp.copy()
temp_avg['avg_forecast'] = AirTemp['AvgTemp'].mean()
​
plt.figure(figsize=(12,8))
plt.plot(AirTemp['AvgTemp'], label='Data')
plt.plot(temp_avg['avg_forecast'], label='Average Forecast')
plt.legend(loc='best')
plt.show()
Plot the moving average forecast and average temperature
mvg_avg = AirTemp.copy()
mvg_avg['moving_avg_forecast'] = AirTemp['AvgTemp'].rolling(12).mean()
plt.plot(AirTemp['AvgTemp'], label='Average Temperature')
plt.plot(mvg_avg['moving_avg_forecast'], label='Moving Average Forecast')
plt.legend(loc='best')
plt.show()
Example 9
Moving average of window size 5 for US GDP
### Load required libraries
​
from    pandas                   import   read_csv, Grouper, DataFrame, concat
import  matplotlib.pyplot        as       plt
from    datetime                 import   datetime
import  pandas                   as       pd
​
USGDP    = pd.read_csv('D:/GDPUS.csv', header=0)
date_rng = pd.date_range(start='1/1/1929', end='31/12/1991', freq='A')
print(date_rng)
​
USGDP['TimeIndex'] = pd.DataFrame(date_rng, columns=['Year'])
plt.plot(USGDP.TimeIndex, USGDP.GDP,label='GDP')
​
plt.legend(loc='best')
plt.show()
mvg_avg_USGDP = USGDP.copy()
mvg_avg_USGDP['moving_avg_forecast'] = USGDP['GDP'].rolling(5).mean()
plt.plot(USGDP['GDP'], label='US GDP')
plt.plot(mvg_avg_USGDP['moving_avg_forecast'], label='US GDP MA(5)')
plt.legend(loc='best')
plt.show()
Moving average line is close to the original data line.

Example 10
Moving average of window size 3 for India GDP
### Load required libraries
​
from    pandas                   import   read_csv, Grouper, DataFrame, concat
import  matplotlib.pyplot        as       plt
from    datetime                 import   datetime
import  pandas                   as       pd
IndiaGDP              = pd.read_csv('D:/GDPIndia.csv', header=0)
​
date_rng              = pd.date_range(start='1/1/1960', end='31/12/2017', freq='A')
IndiaGDP['TimeIndex'] = pd.DataFrame(date_rng, columns=['Year'])
​
print(IndiaGDP.head())
​
plt.plot(IndiaGDP.TimeIndex, IndiaGDP.GDPpercapita,label='GDPpercapita')
plt.legend(loc='best')
plt.show()
mvg_avg_IndiaGDP                        = IndiaGDP.copy()
mvg_avg_IndiaGDP['moving_avg_forecast'] = IndiaGDP['GDPpercapita'].rolling(3).mean()
​
plt.plot(IndiaGDP['GDPpercapita'], label='India GDP per Capita')
plt.plot(mvg_avg_IndiaGDP['moving_avg_forecast'], label='India GDP/Capita MA(3)')
plt.legend(loc='best')
plt.show()
Moving average line is close to the original data line.

END


# -------------------------------------------------------------------------------------------------------------
### Video - Modifying the Time Series Range_Hands-on - Code

Forecast Range, Accuracy and Various Requirements
Note: The forecasting techniques and model evaluation parameters will be covered in great detail in the upcoming weeks. The following lines of theoretical information is just to give you an introduction to Forecasting.
Time Series forecast models can both make predictions and provide a confidence interval for those predictions.

Forecast Range
*Confidence intervals provide an upper and lower expectation for the real observation. *

These are useful for assessing the range of real possible outcomes for a prediction and for better understanding the skill of the model.

For example, the ARIMA implementation in the statsmodel python library can be used to fit an ARIMA model. It returns an ARIMAResults object.

The object provides the forecast() function returns three values:

1) Forecast: The forecasted value in the
2) Standard Error of the model:
3) Confidence Interval: The 95% confidence interval for the forecast
Forecast Accuracy
The error in the forecast is the difference between the actual value and the forecast.

Two popular accuracy measures are RMSE and MAPE.

Forecast Requirements
A time series model must contain a key time column that contains unique values, input columns, and at least one predictable column.

Time series data often requires cleaning, scaling, and even transformation

Frequency: Data may be provided at a frequency that is too high to model or is unvenly spread through time requiring resampling for use in models.

Outliers: Data may contain corrupt or extreme outlier values that need to be identified and handled.

Frequency:

Frequencies may be too granular or not granular enough to get insights.
The pandas library in Pyhton provides the capability to increase or decrease the sampling frequency of the time series data.
Resampling:

Resampling may be required if the data is not available at the same frequency that you want to make predictions.
Resampling may be required to provide additional structure or insight into the learning problem for supervised learning models.
Up-sampling

Increase the frequencies of the sample, example: months to days

Care may be needed in deciding how the fine-grained observations are calculated using interpolation.

The function, resample() available in the pandas library works on the Series and DataFrame objects.

This can be used to group records when down-sampling and make space for new observations when up-sampling.

Example 12
Up-sampling frequency

The observations in the Shampoo Sales are monthly. We need to up-sample the frequency from monthly to daily and use an interpolation scheme to fill in the new daily frequency.

We can use this function to transform our monthly dataset into a daily dataset by calling resampling and specifying preferred frequency of calendar day frequency or D.

#upsample to daily sales
from   pandas            import read_csv
# from     pandas                   import datetime #this particular submodule from pandas will be deprecated in future
# versions, thus the next line of code
from     datetime                 import datetime
import matplotlib.pyplot as     plt
​
def parser(x):
       return datetime.strptime('190'+x, '%Y-%m')
​
tseries = read_csv('D:/Academic Operations/DSBA - Python/Online/Time Series Forecasting/Abhinanda Sir/Video Materials/Week 1/shampoo-sales.csv', header = 0, index_col = 0, parse_dates = True, 
                               squeeze = True, date_parser = parser)
​
upsampled_ts = tseries.resample('D').mean()
print(upsampled_ts .head(36))
Inference
We observe that the resample() function has created the rows by putting NaN values as new values for dates other than day 01.

Next we can interpolate the missing values at this new frequency. The function, interpolate() of pandas library is used to interpolate the missing values. We use a linear interpolation which draws a straight line between available data, on the first day of the month and fills in values at the chosen frequency from this line.

interpolated = upsampled_ts.interpolate(method = 'linear')
interpolated.plot()
plt.show()
Another common interpolation

Another common interpolation method is to use a polynomial or a spline to connect the values. This creates more curves and look more natural on many datasets.
Using a spline interpolation requires you specify the order (count of terms in the polynomial). Here, we are using 2.
interpolated1 = upsampled_ts.interpolate(method = 'spline', order = 2)
interpolated1.plot()
plt.show()
print(interpolated1.head(12))
Example 13
Down-sampling Frequency

The sales data is monthly, but we prefer the data to be quarterly. The year can be divided into 4 business quarters, 3 months a piece.
The resample() function will group all observations by the new frequency.
We need to decide how to create a new quarterly value from each group of 3 records. We shall use the mean() function to calculate the average monthly sales numbers for the quarter
resample             = tseries.resample('Q')
quarterly_mean_sales = resample.mean()
print(quarterly_mean_sales.head())
quarterly_mean_sales.plot()
plt.show()
Example 14
We can turn monthly data into yearly data. Down-sample the data using the alias, A for year-end frequency and this time use sum to calculate the total sales each year.

resample = tseries.resample('A')
yearly_mean_sales = resample.sum()
print(yearly_mean_sales.head() )
yearly_mean_sales.plot()
plt.show()
Outliers Data may contain corrupt or extreme outlier values that need to be identified and handled.

Detection of outliers in time series is difficult.
If a trend is present in the data, then usual method of detecting outliers by boxplot may not work.
If seasonality is present in the data, one particular season's data may be too small or too large compared to others.
Decomposition helps in identifying unsual observations
If trend and seasonality are not adequate to explain the observation
Outliers cannot be eliminated - they need to be imputed as closely as possible by using the knowledge gained from decomposition.
END

# -------------------------------------------------------------------------------------------------------------
### Video - ARIMA Models - Hands on Python - Code

Auto ARIMA
In an ARIMA model there are 3 parameters, namely p, q and d that help model major aspects of a time series: seasonality, trend and noise.

If our model has a seasonal component, we use Seasonal ARIMA with parameters, P, Q and D related to seasonal components of the model.

https://medium.com/@josemarcialportilla/using-python-and-auto-arima-to-forecast-seasonal-time-series-90877adff03c

auto.arima
The module auto.arima fits the best ARIMA model to univariate time series according to either AIC, AICc or BIC value. This function conducts a search over possible model within the order constraints provided.

AIC
The Akaike information criterion (AIC) is an estimator of the relative quality of statistical models for a given set of data. Given a collection of models for the data, AIC estimates the quality of each model, relative to each of the other models. Thus, AIC provides a means for model selection.

AICc is AIC with a correction for small sample sizes.
BIC
Bayesian information criterion (BIC) or Schwarz information criterion (also SIC, SBC, SBIC) is a criterion for model selection among a finite set of models; the model with the lowest BIC is preferred. It is based, in part, on the likelihood function and it is closely related to the Akaike information criterion (AIC).

https://en.wikipedia.org/wiki/Akaike_information_criterion#Comparison_with_BIC

https://en.wikipedia.org/wiki/Bayesian_information_criterion

Example 3
We use tractor sales data to replicate auto.arima in python.

import statsmodels.api as sm
import statsmodels.tsa.api as smt
import statsmodels.formula.api as smf
import sys
import warnings
import itertools
warnings.filterwarnings("ignore")
​
import pandas as pd
import numpy as np
​
import statsmodels.api as sm
import statsmodels.tsa.api as smt
import statsmodels.formula.api as smf
​
import matplotlib.pyplot as plt
%matplotlib inline
data = pd.read_csv("D:/TractorSales.csv")
data.head(5)
dates = pd.date_range(start='2003-01-01', freq='MS', periods=len(data))
#This particular 'calendar' library lets us play around with the Time Stamp and lets us extract various 
#features from the time stamp
import calendar
data['Month'] = dates.month
data['Month'] = data['Month'].apply(lambda x: calendar.month_abbr[x])
data['Year'] = dates.year
data.drop(['Month-Year'], axis=1, inplace=True)
data.rename(columns={'Number of Tractor Sold':'Tractor-Sales'}, inplace=True)
data = data[['Month', 'Year', 'Tractor-Sales']]
data.set_index(dates, inplace=True)
data.head(5)
# extract out the time-series
sales_ts = data['Tractor-Sales']
plt.figure(figsize=(8, 4))
plt.plot(sales_ts)
plt.xlabel('Years')
plt.ylabel('Tractor Sales')
plt.show()
Inference
We observe both trend and multiplicative seasonaliy from the plot shown above.

We try moving averages of various window widths such as 4, 6,8 and 12.

fig, axes = plt.subplots(2, 2, sharey=False, sharex=False)
fig.set_figwidth(14)
fig.set_figheight(8)
​
axes[0][0].plot(sales_ts.index, sales_ts, label='Original')
axes[0][0].plot(sales_ts.index, sales_ts.rolling(window=4).mean(), label='4-Months Rolling Mean')
axes[0][0].set_xlabel("Years")
axes[0][0].set_ylabel("Number of Tractor's Sold")
axes[0][0].set_title("4-Months Moving Average")
axes[0][0].legend(loc='best')
​
axes[0][1].plot(sales_ts.index, sales_ts, label='Original')
axes[0][1].plot(sales_ts.index, sales_ts.rolling(window=6).mean(), label='6-Months Rolling Mean')
axes[0][1].set_xlabel("Years")
axes[0][1].set_ylabel("Number of Tractor's Sold")
axes[0][1].set_title("6-Months Moving Average")
axes[0][1].legend(loc='best')
​
axes[1][0].plot(sales_ts.index, sales_ts, label='Original')
axes[1][0].plot(sales_ts.index, sales_ts.rolling(window=8).mean(), label='8-Months Rolling Mean')
axes[1][0].set_xlabel("Years")
axes[1][0].set_ylabel("Number of Tractor's Sold")
axes[1][0].set_title("8-Months Moving Average")
axes[1][0].legend(loc='best')
​
axes[1][1].plot(sales_ts.index, sales_ts, label='Original')
axes[1][1].plot(sales_ts.index, sales_ts.rolling(window=12).mean(), label='12-Months Rolling Mean')
axes[1][1].set_xlabel("Years")
axes[1][1].set_ylabel("Number of Tractor's Sold")
axes[1][1].set_title("12-Months Moving Average")
axes[1][1].legend(loc='best')
​
plt.tight_layout()
plt.show()
#Determing rolling statistics
​
rolmean = sales_ts.rolling(window = 4).mean()
rolstd = sales_ts.rolling(window = 4).std()
#Plot rolling statistics:
orig = plt.plot(sales_ts, label='Original')
mean = plt.plot(rolmean, label='Rolling Mean')
std = plt.plot(rolstd, label = 'Rolling Std')
plt.legend(loc='best')
plt.title('Rolling Mean & Standard Deviation')
plt.show()
Augmented Dickey-Fuller Test - Let's run the Augmented Dicky Fuller Test on the timeseries and verify the null hypothesis that the TS is non-stationary.

from statsmodels.tsa.stattools import adfuller
dftest = adfuller(sales_ts)
dftest
print('DF test statistic is %3.3f' %dftest[0])
print('DF test p-value is %1.4f' %dftest[1])
Though the variation in standard deviation is small, rolling mean is clearly increasing with time and this is not a stationary series. Also, the test statistic is way more than the critical values.

As we observed while plotting the moving average over months that there is a monthly pattern. Let us try to decipher the seasonal component.

Seasonality – Time Series Decomposition
Observe how number of tractors sold vary on a month on month basis. We will plot a stacked annual plot to observe seasonality in our data.

monthly_sales_data = pd.pivot_table(data, values = "Tractor-Sales", columns = "Year", index = "Month")
monthly_sales_data
#Second method to create the same pivot table
​
monthly_sales_data = monthly_sales_data.reindex(index = ['Jan','Feb','Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
monthly_sales_data
monthly_sales_data.plot();
yearly_sales_data = pd.pivot_table(data, values = "Tractor-Sales", columns = "Month", index = "Year")
yearly_sales_data = yearly_sales_data[['Jan','Feb','Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']]
yearly_sales_data
yearly_sales_data.plot();
yearly_sales_data.boxplot();
Inferences
The tractor sales have been increasing without fail every year. July and August are the peak months for tractor sales and the variance and the mean value in July and August are also much higher than any of the other months. We can see a seasonal cycle of 12 months where the mean value of each month starts with a increasing trend in the beginning of the year and drops down towards the end of the year. We can see a seasonal effect with a cycle of 12 months.

Time Series Decomposition
decomposition = sm.tsa.seasonal_decompose(sales_ts, model='multiplicative')
fig = decomposition.plot()
fig.set_figwidth(8)
fig.set_figheight(6)
fig.suptitle('Decomposition of multiplicative time series')
plt.show()
Some of our key observations from this analysis:
1) Trend: 12-months moving average looks quite similar to a straight line hence we could have easily used linear regression to estimate the trend in this data.

2) Seasonality: Seasonal plot displays a fairly consistent month-on-month pattern. The monthly seasonal components are average values for a month after removal of trend. Trend is removed from the time series using the following formula:

Seasonality_t × Remainder_t = Y_t/Trend_t

3) Irregular Remainder (random): is the residual left in the series after removal of trend and seasonal components. Remainder is calculated using the following formula:

Remainder_t = Y_t / (Trend_t × Seasonality_t)

plt.figure(figsize=(8, 4))
plt.plot(sales_ts.diff(periods=1))
plt.xlabel('Years')
plt.ylabel('Tractor Sales');
We observe seasonality even after differencing.

plt.figure(figsize=(8, 4))
plt.plot(np.log10(sales_ts))
plt.xlabel('Years')
plt.ylabel('Log (Tractor Sales)');
We observe trend and seasonality even after taking log of the observations.

plt.figure(figsize=(10, 5))
plt.plot(np.log10(sales_ts).diff(periods=1))
plt.xlabel('Years')
plt.ylabel('Differenced Log (Tractor Sales)');
sales_ts_log = np.log10(sales_ts)
sales_ts_log.dropna(inplace=True)
​
sales_ts_log_diff = sales_ts_log.diff(periods=1) # same as ts_log_diff = ts_log - ts_log.shift(periods=1)
sales_ts_log_diff.dropna(inplace=True)
fig, axes = plt.subplots(1, 2)
fig.set_figwidth(12)
fig.set_figheight(4)
smt.graphics.plot_acf(sales_ts_log, lags=30, ax=axes[0])
smt.graphics.plot_pacf(sales_ts_log, lags=30, ax=axes[1])
plt.tight_layout()
Nonstationary series have an ACF that remains significant for half a dozen or more lags, rather than quickly declining to zero. You must difference such a series until it is stationary before you can identify the process

The above ACF is “decaying”, or decreasing, very slowly, and remains well above the significance range (blue band) for at least a dozen lags. This is indicative of a non-stationary series.

fig, axes = plt.subplots(1, 2)
fig.set_figwidth(12)
fig.set_figheight(4)
plt.xticks(range(0,30,1), rotation = 90)
smt.graphics.plot_acf(sales_ts_log_diff, lags=30, ax=axes[0])
smt.graphics.plot_pacf(sales_ts_log_diff, lags=30, ax=axes[1])
plt.tight_layout()
Inference
The above ACF has “decayed” fast and remains within the significance range (blue band) except for a few (5) lags. This is indicative of a stationary series.

# Define the p, d and q parameters to take any value between 0 and 2
p = d = q = range(0, 2)
​
# Generate all different combinations of p, d and q triplets
pdq = list(itertools.product(p, d, q))
​
# Generate all different combinations of seasonal p, q and q triplets
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
pdq
seasonal_pdq
#Separate data into train and test
data['date'] = data.index
train = data[data.index < '2013-01-01']
test = data[data.index >= '2013-01-01']
train_sales_ts_log = np.log10(train['Tractor-Sales'])
best_aic = np.inf
best_pdq = None
best_seasonal_pdq = None
temp_model = None
for param in pdq:#looping through the (p,d,q) values for ARIMA
    for param_seasonal in seasonal_pdq:#looping through the (P,D,Q,freq) values for SARIMA
        
        try:
            temp_model = sm.tsa.statespace.SARIMAX(train_sales_ts_log,#defining the SARIMA model after taking
                                                   # the logarithm of the training data
                                             order = param,#setting the (p,d,q) values
                                             seasonal_order = param_seasonal,#setting the (P,D,Q,freq) values
                                             enforce_stationarity=True)
            results = temp_model.fit()#fitting the above built SARIMA model
​
            
            if results.aic < best_aic:#defining a conditional statement about whether the AIC of the model
                #just built is less than the best_aic
                best_aic = results.aic#defining the new value of AIC from the SARIMA model as the best_aic
                best_pdq = param#storing the (p,d,q) values in the variable best_pdq
                best_seasonal_pdq = param_seasonal#storing the (P,D,Q,freq) values in the variable 
                #best_seasonal_pdq
        except:
            #print("Unexpected error:", sys.exc_info()[0])
            continue
print("Best SARIMAX{}x{}12 model - AIC:{}".format(best_pdq, best_seasonal_pdq, best_aic))
Inference
The best fit model is selected based on Akaike Information Criterion (AIC) , and Bayesian Information Criterion (BIC) values. The idea is to choose a model with minimum AIC and BIC values.
For ARIMA(p, d, q) × (P, D, Q)S, we got SARIMAX(0, 1, 1)x(1, 0, 1, 12)12 model with the least AIC:-600.0908420381976

Here,

p = non-seasonal AR order = 0,
d = non-seasonal differencing = 1,
q = non-seasonal MA order = 1,
P = seasonal AR order = 1,
D = seasonal differencing = 0,
Q = seasonal MA order = 1,
S = time span of repeating seasonal pattern = 12
Predict sales on in-sample date using the best fit ARIMA model
best_model = sm.tsa.statespace.SARIMAX(train_sales_ts_log,
                                      order=(0, 1, 1),
                                      seasonal_order=(1, 0, 1, 12),
                                      enforce_stationarity=True)
best_results = best_model.fit()
print(best_results.summary().tables[0])
print(best_results.summary().tables[1])
pred_dynamic = best_results.get_prediction(start=pd.to_datetime('2012-01-01'), dynamic=True, full_results=True)
pred_dynamic_ci = pred_dynamic.conf_int()
pred99 = best_results.get_forecast(steps=24, alpha=0.1)
# Extract the predicted and true values of our time series
sales_ts_forecasted = pred_dynamic.predicted_mean
testCopy = test.copy()
#we need to change the scale of the logarithmic scale to the original scale by raising the predicted values
#to the power of 10
testCopy['sales_ts_forecasted'] = np.power(10, pred99.predicted_mean)
testCopy
# Compute the root mean square error
mse = ((testCopy['Tractor-Sales'] - testCopy['sales_ts_forecasted']) ** 2).mean()
rmse = np.sqrt(mse)
print('The Root Mean Squared Error of our forecasts is {}'.format(round(rmse, 3)))
axis = train['Tractor-Sales'].plot(label='Train Sales', figsize=(10, 6))
testCopy['Tractor-Sales'].plot(ax=axis, label='Test Sales', alpha=0.7)
testCopy['sales_ts_forecasted'].plot(ax=axis, label='Forecasted Sales', alpha=0.7)
axis.set_xlabel('Years')
axis.set_ylabel('Tractor Sales')
plt.legend(loc='best')
plt.show()
plt.close()
Forecast sales using the best fit ARIMA model
# Get forecast 36 steps (3 years) ahead in future
n_steps = 36
pred_uc_99 = best_results.get_forecast(steps=36, alpha=0.01) # alpha=0.01 signifies 99% confidence interval
pred_uc_95 = best_results.get_forecast(steps=36, alpha=0.05) # alpha=0.05 signifies 95% confidence interval
​
# Get confidence intervals 95% & 99% of the forecasts
pred_ci_99 = pred_uc_99.conf_int()
pred_ci_95 = pred_uc_95.conf_int()
n_steps = 36
​
idx = pd.date_range(data.index[-1], periods=n_steps, freq='MS')#defining the date range for 3 years
#into the future
​
fc_95 = pd.DataFrame(np.column_stack([np.power(10, pred_uc_95.predicted_mean), np.power(10, pred_ci_95)]), 
                     index=idx, columns=['forecast', 'lower_ci_95', 'upper_ci_95'])#creating a data frame
#by raising the results to the appropriate power for suitable predicted values - For 95% confidence interval
​
fc_99 = pd.DataFrame(np.column_stack([np.power(10, pred_ci_99)]), 
                     index=idx, columns=['lower_ci_99', 'upper_ci_99'])#creating a data frame
#by raising the results to the appropriate power for suitable predicted values - For 99% confidence interval
​
fc_all = fc_95.combine_first(fc_99)
​
fc_all = fc_all[['forecast', 'lower_ci_95', 'upper_ci_95', 'lower_ci_99', 'upper_ci_99']]# just reordering 
#columns
​
fc_all.head()
# plot the forecast along with the confidence band
​
axis = sales_ts.plot(label='Observed', figsize=(8, 4))
fc_all['forecast'].plot(ax=axis, label='Forecast', alpha=0.7)
axis.fill_between(fc_all.index, fc_all['lower_ci_95'], fc_all['upper_ci_95'], color='k', alpha=.15)
axis.set_xlabel('Years')
axis.set_ylabel('Tractor Sales')
plt.legend(loc='best')
plt.show()
Plot ACF and PACF for residuals of ARIMA model to ensure no more information is left for extraction
best_results.plot_diagnostics(lags=30, figsize=(16,12))
plt.show()
Inference
We need to ensure that the residuals of our model are uncorrelated and normally distributed with zero-mean. If it is not that it signifies that the model can be further improved and we repeat the process with the residuals.

In this case, our model diagnostics suggests that the model residuals are normally distributed based on the following:

The KDE plot of the residuals on the top right is almost similar with the normal distribution.
The qq-plot on the bottom left shows that the ordered distribution of residuals (blue dots) follows the linear trend of the samples taken from a standard normal distribution with N(0, 1). Again, this is a strong indication that the residuals are normally distributed.
The residuals over time (top left plot) don't display any obvious seasonality and appear to be white noise. This is confirmed by the autocorrelation (i.e. correlogram) plot on the bottom right, which shows that the time series residuals have low correlation with lagged versions of itself.
Those observations coupled with the fact that there are no spikes outside the insignificant zone for both ACF and PACF plots lead us to conclude that that residuals are random with no information or juice in them and our model produces a satisfactory fit that could help us understand our time series data and forecast future values. It sems that our ARIMA model is working fine.

END

# -------------------------------------------------------------------------------------------------------------
### Untitled.ipynb

s
df=pd.read_csv("train_.csv", parse_dates = True, index_col = 'Month')
df.head()
df.dtypes
df.shape
test=pd.read_csv("test_.csv", parse_dates = True, index_col = 'Month')
test.head()
p = d = q = range(0, 2)
​
# Generate all different combinations of p, d and q triplets
pdq = list(itertools.product(p, d, q))
​
# Generate all different combinations of seasonal p, q and q triplets
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
​
best_aic = np.inf
best_pdq = None
best_seasonal_pdq = None
temp_model = None
for param in pdq:#looping through the (p,d,q) values for ARIMA
    for param_seasonal in seasonal_pdq:#looping through the (P,D,Q,freq) values for SARIMA
        
        try:
            temp_model = sm.tsa.statespace.SARIMAX(df,#defining the SARIMA model after taking
                                                   # the logarithm of the training data
                                             order = param,#setting the (p,d,q) values
                                             seasonal_order = param_seasonal,#setting the (P,D,Q,freq) values
                                             enforce_stationarity=True)
            results = temp_model.fit()#fitting the above built SARIMA model
​
            
            if results.aic < best_aic:#defining a conditional statement about whether the AIC of the model
                #just built is less than the best_aic
                best_aic = results.aic#defining the new value of AIC from the SARIMA model as the best_aic
                best_pdq = param#storing the (p,d,q) values in the variable best_pdq
                best_seasonal_pdq = param_seasonal#storing the (P,D,Q,freq) values in the variable 
                #best_seasonal_pdq
        except:
            #print("Unexpected error:", sys.exc_info()[0])
            continue
print("Best SARIMAX: {} x: {} 12 model - AIC:{}".format(best_pdq, best_seasonal_pdq, best_aic))
param=(2,1,2)
temp_model = sm.tsa.statespace.SARIMAX(df, order = param)
results = temp_model.fit()
predictions=results.predict(start=test.index[0], end=test.index[-1])
print(predictions[0:])
​
output=pd.concat([predictions],axis=1)
numpy_array = output.to_numpy()
np.savetxt("test_file.txt", numpy_array, fmt = "%d")

# -------------------------------------------------------------------------------------------------------------
### Untitled(2).ipynb

T
df1=pd.read_csv('AirPassenger.csv',parse_dates=['Year-Month'],index_col=['Year-Month'])
df1.head()
df1['1949-12-01':'1948-01-01']
df1.loc['1949-01-01']
from pylab import rcParams
rcParams['figure.figsize']=[12,8]
df1.plot()
df1_Add=seasonal_decompose(df1, model='additive')
df1_Add.plot()
plt.show()
df1_Mul=seasonal_decompose(df1, model='multiplicative')
df1_Mul.plot()
plt.show()
df2=df1.copy()
df2_log=np.log(df2)
plt.subplot(2,1,1)
plt.title('Top')
plt.plot(df1)
plt.subplot(2,1,2)
plt.title('Bottom')
plt.plot(df2_log)
plt.show()
df1_Add.trend
df1_Add.trend.plot()
plt.plot(df1_Add.trend)
df1_Add.seasonal
df1_Add.seasonal.plot()
plt.plot(df1_Add.seasonal)
df1_Add.resid
df1_Add.resid.plot()
plt.plot(df1_Add.resid)
df1_q=df1.resample('Q').mean()
plt.subplot(3,3,1)
plt.plot(df1_q)
df1_h=df1.resample('H').interpolate()
plt.subplot(3,3,2)
plt.plot(df1_h)
df1_d=df1.resample('D').ffill()
plt.subplot(3,3,3)
plt.plot(df1_d)
plt.show()
df = pd.read_csv('AirPassenger.csv',parse_dates=True,index_col='Year-Month')
df.head()
df[(df.index>'1950') & (df.index<'1951')]
df[(df.index=='1950-02-01')]
rcParams['figure.figsize']=[15,8]
df.plot()
plt.plot(df)
df_Add=seasonal_decompose(df, model='additive', period =12)
df_Add.plot()
train=df[df.index<'1957']
test=df[df.index>'1957']
model_SES = SimpleExpSmoothing(train,initialization_method='estimated')
model_SES_autofit = model_SES.fit(optimized=True)
model_SES_autofit.params
SES_predict = model_SES_autofit.forecast(steps=len(test))
def MAPE_MY(Ytrue,Ypred):
    return np.mean(np.abs(Ytrue-Ypred)/Ytrue*100)
print('SES RMSE:',mean_squared_error(test.values,SES_predict.values,squared=False))
print('SES RMSE (calculated using statsmodels):',em.rmse(test.values,SES_predict.values)[0])
resultDF=pd.DataFrame({'Test_RMSE':[em.rmse(test.values, SES_predict.values)[0]]}, index=['0.99 alpha RMSE'])
resultDF
model_DES=Holt(train,initialization_method='estimated')
model_DES_Auto1=model_DES.fit(optimized=True)
# model_DES_Auto1.params
DES_Predict=model_DES_Auto1.forecast(len(test))
pd_temp=pd.DataFrame({'Test_RMSE':[mean_squared_error(test.values,DES_Predict, squared=False)]}, index=['Alpha=0.99, Beta=0.001:Double Exponential Smoothing predictions on Test Set'])
pd_temp
resultDF=pd.concat([resultDF, pd_temp])
resultDF
model_TES=ExponentialSmoothing(train, trend='add', seasonal='add', initialization_method='estimated')
model_TES_Auto=model_TES.fit(optimized=True)
# model_TES_Auto.params
pd_temp=pd.DataFrame({'Test_RMSE':[mean_squared_error(test.values,TES_Predict.values, squared=False)]}, index=['alpha=0.25, beta=0.0, gamma=0.75, AA: Triple Exponential Smoothing predictions on Test Set'])
resultDF=pd.concat([resultDF,pd_temp])
resultDF
model_TES_am=ExponentialSmoothing(train, trend='add', seasonal='mul', initialization_method='estimated')
model_TES_am_Auto=model_TES_am.fit(optimized=True)
TES_Predict_am=model_TES_am_Auto.forecast(len(test))
# model_TES_am_Auto.params
pd_temp=pd.DataFrame({'Test_RMSE':[mean_squared_error(test.values,TES_Predict_am.values, squared=False)]}, index=['alpha=0.74, beta=0.001, gamma=0.001, AM: Triple Exponential Smoothing predictions on Test Set'])
resultDF=pd.concat([resultDF,pd_temp])
resultDF
​
​
​
plt.plot(train, label='Train')
plt.plot(test, label='Test')
plt.plot(SES_predict, label='Alpha=0.99:Simple Exponential Smoothing predictions on Test Set')
plt.plot(DES_Predict, label='Alpha=0.99, Beta=0.001:Double Exponential Smoothing predictions on Test Set')
plt.plot(TES_Predict, label='alpha=0.25, beta=0.0, gamma=0.75, AA: Triple Exponential Smoothing predictions on Test Set')
plt.plot(TES_Predict_am, label='alpha=0.25, beta=0.0, gamma=0.75, AM: Triple Exponential Smoothing predictions on Test Set')
plt.grid()
plt.legend(loc='best')
​
​

# -------------------------------------------------------------------------------------------------------------
### S5_Faculty_Notebook.ipynb

Store id
Day of Week
Date
Customers: the number of customers on a given day.(Target Variable)
Open: an indicator for whether the store was open: 0 = closed, 1 = open.
Promo: indicates whether a store is running a promo on that day.
StateHoliday: indicates a state holiday. Normally all stores, with few exceptions, are closed on state holidays. This has value as "0", "a", "b", "c"
SchoolHoliday: indicates if the (Store, Date) was affected by the closure of public schools.
Store50 = pd.read_excel("Store_50.xlsx", parse_dates = True, index_col = 'Date')
Store50.head()
print("The number of rows: ",Store50.shape[0], "\n""The number of columns: ",Store50.shape[1])
## Checking the number of stores for which we have the data
​
Store50['Store'].unique()
## Selecting the store 1044 only for analysis.
## Here, we are also reversing the data as we need to contiguous data in the ascending order for a Time Series Analysis.
​
Store50_1044 = Store50[Store50.Store == 1044]. sort_index(ascending=True)
Store50_1044.head()
Store50_1041 = Store50[Store50.Store == 1041]. sort_index(ascending=True)
Store50_1041.head()
df = pd.DataFrame(columns=['Store_1044','Store_1041'])
df
## Putting the two desired Time Series together in one dataframe
​
df['Store_1044'] = Store50_1044['Customers']
df['Store_1041'] = Store50_1041['Customers']
df
df.info()
The 'Customers' variable is our desired Time Series. So let us plot it to understand how the series looks like. This is a daily series.

from pylab import rcParams
rcParams['figure.figsize'] = 15,8
df.plot(grid=True);
## Let us resample the data into a weekly time series to understand how the footfall of the customers change weekly.
​
df.resample('W').sum().plot(grid=True);
We see that the Store_1041 has a higher footfall of customers as compared to the Store_1044.

df.index.year.unique()
Split the data into training and test. The test data starts from 2016 and onwards.

train=df[df.index.year !=2016]
test=df[df.index.year ==2016]
print('First 5 rows of the training data')
display(train.head())
print('Last 5 rows of the training data')
display(train.tail())
print('First 5 rows of the test data')
display(test.head())
print('Last 5 rows of the test data')
display(test.tail())
Let us check the number of rows and columns of the training and test set.

print(train.shape)
print(test.shape)
Checking whether the training data is stationary.

## Importing the Augmented Dickey-Fuller test from the statsmodels library
​
from statsmodels.tsa.stattools import adfuller
## Defning a function
def adf_test(timeseries):
    #Perform Dickey-Fuller test:
    print ('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries,regression='ct')#running the adf test on the input time series
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    ## creating a series to format the output
    for key,value in dftest[4].items():##running a for loop to format the critical values of the test statistic
       dfoutput['Critical Value (%s)'%key] = value
    print (dfoutput)
adf_test(train['Store_1044'])
adf_test(train['Store_1041'])
Series is stationary and hence no need for differentiation.

Vector Auto-Regressive
Now, we are going to build a Vector Auto-Regressive Model. In this model, we will be using the lagged or past values of a particular Time Series to predict the other Time Series.

In this case, we have two stationary Time Series and we will be using these to build a VAR model.

Before we code up this model, let us understand how this model is interpreted and how the equation of this model looks like for two time-series.

The following is the example of a two-dimensional VAR(1) model.

𝑦1,𝑡 = 𝑐1 + 𝜙11,1𝑦1,𝑡−1 + 𝜙12,1𝑦2,𝑡−1 + 𝑒1,𝑡
𝑦2,𝑡 = 𝑐2 + 𝜙21,1𝑦1,𝑡−1 + 𝜙22,1𝑦2,𝑡−1 + 𝑒2,𝑡
Here e is the error term (white noise).

We can include the moving average terms to this kind of models as well. We can think of VAR models to AR models extended to multiple Time Series.

But we need to very careful in incorporating the number of variables in a VAR model and also be wary of the order of the VAR model. A complicated model by definition would work well on the training data but not so much on the test data. Introducing more time series would also include the error terms from those time series for the prediction of another time series.

VAR models are very powerful in a sense that it gives us an idea about the causation property a bit as well. If we get an improvement in the prediction accuracy by using a VAR model instead of an AR model, we can say that the past values of another time series aids in the prediction of our desired time series.

Build a VAR model.
import statsmodels.api as sm
## We need to convert these variables into float as that is the input that statsmodels api takes
​
train['Store_1044'] = train['Store_1044'].astype('float64')
train['Store_1041'] = train['Store_1041'].astype('float64')
train.info()
## We are running this iteration upto 7 days since this is a daily data and we have seen that the customer footfall
## of Store 1044 has a seasonality of 7.
​
for i in range(1,8):
    model = sm.tsa.VARMAX(train,order=(i,0),trend='c')
    model_result = model.fit()
    print('Order =',i)
    print('AIC:',model_result.aic)
model = sm.tsa.VARMAX(train,order=(7,0),trend='c')
model_result = model.fit()
model_result.summary()
pred = model_result.forecast(steps=len(test))
pred
## Calculating the RMSE for Store 1044
​
import math
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(test['Store_1044'],pred['Store_1044'])
rmse = math. sqrt(mse)
print('Store_1044:',mse)
print('Store_1044:',rmse)
## Calculating the RMSE for Store 1041
​
mse = mean_squared_error(test['Store_1041'],pred['Store_1041'])
rmse = math. sqrt(mse)
print('Store_1041:',mse)
print('Store_1041:',rmse)
​
​
Vector Auto-regression and Moving Average - (VARMA)
import os
from google.colab import drive 
drive.mount('/content/drive')
%cd /content/drive/My\ Drive/
​
df1=pd.read_csv('varma_data.csv')
df2 = df1[(df1['Date'] > '2016-01-14') & (df1['Date'] <= '2017-01-30')]
df2.head()
A Standard define functions for an Time-Series model evaluation metrics

def timeseries_evaluation_metrics_func(y_true, y_pred):
    
    def mean_absolute_percentage_error(y_true, y_pred): 
        y_true, y_pred = np.array(y_true), np.array(y_pred)
        return np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    print('Evaluation metric results:-')
    print(f'MSE is : {metrics.mean_squared_error(y_true, y_pred)}')
    print(f'MAE is : {metrics.mean_absolute_error(y_true, y_pred)}')
    print(f'RMSE is : {np.sqrt(metrics.mean_squared_error(y_true, y_pred))}')
    print(f'MAPE is : {mean_absolute_percentage_error(y_true, y_pred)}')
    print(f'R2 is : {metrics.r2_score(y_true, y_pred)}',end='\n\n')
Checking for stationarity of data using ADF test function:

def Augmented_Dickey_Fuller_Test_func(series , column_name):
    print (f'Results of Dickey-Fuller Test for column: {column_name}')
    dftest = adfuller(series, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','No Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
       dfoutput['Critical Value (%s)'%key] = value
    print (dfoutput)
    if dftest[1] <= 0.05:
        print("Conclusion:====>")
        print("Reject the null hypothesis")
        print("Data is stationary")
    else:
        print("Conclusion:====>")
        print("Fail to reject the null hypothesis")
        print("Data is non-stationary")
df2.columns
Infere the variables are stationary:

for name, column in df2[['Open', 'High', 'Low', 'Close']].iteritems():
    Augmented_Dickey_Fuller_Test_func(df2[name],name)
    print('\n')
We would be considering the train data that consists of all the data except the last 30 days, and the test data which consists of only the last 30 days to evaluate on future forcasting.

X = df2[['Open', 'High', 'Low', 'Close' ]]
train, test = X[0:-30], X[-30:]
Perform the Pandas differencing on data to stationarize

train_diff = train.diff()
train_diff.dropna(inplace = True)
Infere the variables are they stationarised after performing the first differencing.

for name, column in train_diff[['Open', 'High', 'Low', 'Close' ]].iteritems():
    Augmented_Dickey_Fuller_Test_func(train_diff[name],name)
    print('\n')
Cointegration is used to check for the existence of a long-run relationship between two or more variables. However, the correlation does not necessarily mean “long run.”

We can see the test says that there is the presence of a long-run relationship between features.

from statsmodels.tsa.vector_ar.vecm import coint_johansen
​
def cointegration_test(df2): 
    res = coint_johansen(df2,-1,5)
    d = {'0.90':0, '0.95':1, '0.99':2}
    traces = res.lr1
    cvts = res.cvt[:, d[str(1-0.05)]]
    def adjust(val, length= 6): 
        return str(val).ljust(length)
    print('Column Name   >  Test Stat > C(95%)    =>   Signif  \n', '--'*20)
    for col, trace, cvt in zip(df2.columns, traces, cvts):
        print(adjust(col), '> ', adjust(round(trace,2), 9),
              ">", adjust(cvt, 8), ' =>  ' , trace > cvt)
​
cointegration_test(train_diff[['Open', 'High', 'Low', 'Close']])
#pip install pmdarima
​
from pmdarima import auto_arima
pq = []
for name, column in train_diff[[ 'Open', 'High', 'Low', 'Close'  ]].iteritems():
    print(f'Searching order of p and q for : {name}')
    stepwise_model = auto_arima(train_diff[name],start_p=1, start_q=1,max_p=7, max_q=7, seasonal=False,
        trace=True,error_action='ignore',suppress_warnings=True, stepwise=True,maxiter=1000)
    parameter = stepwise_model.get_params().get('order')
    print(f'optimal order for:{name} is: {parameter} \n\n')
    pq.append(stepwise_model.get_params().get('order'))
​
Lets perform the inverse differencing function .

def inverse_diff(actual_df, pred_df):
    df_res = pred_df.copy()
    columns = actual_df.columns
    for col in columns: 
        df_res[str(col)+'_1st_inv_diff'] = actual_df[col].iloc[-1] + df_res[str(col)].cumsum()
    return df_res
​
pq
​
df_results = pd.DataFrame(columns=['p', 'q','RMSE Open','RMSE High','RMSE Low','RMSE Close'])
print('Grid Search Started')
start = timer()
for i in pq:
    if i[0]== 0 and i[2] ==0:
        pass
    else:
        print(f' Running for {i}')
        model = VARMAX(train_diff[[ 'Open', 'High', 'Low', 'Close'   ]], order=(i[0],i[2])).fit( disp=False)
        result = model.forecast(steps = 30)
        inv_res = inverse_diff(df2[[ 'Open', 'High', 'Low', 'Close'   ]] , result)
        Opensrmse = np.sqrt(metrics.mean_squared_error(test['Open'], inv_res.Open_1st_inv_diff))
        Highrmse = np.sqrt(metrics.mean_squared_error(test['High'], inv_res.High_1st_inv_diff))
        Lowrmse = np.sqrt(metrics.mean_squared_error(test['Low'], inv_res.Low_1st_inv_diff))
        Closermse = np.sqrt(metrics.mean_squared_error(test['Close'], inv_res.Close_1st_inv_diff))
        df_results = df_results.append({'p': i[0], 'q': i[2], 'RMSE Open':Opensrmse,'RMSE High':Highrmse,'RMSE Low':Lowrmse,'RMSE Close':Closermse }, ignore_index=True)
end = timer()
print(f' Total time taken to complete grid search in seconds: {(end - start)}')
df_results.sort_values(by = ['RMSE Open','RMSE High','RMSE Low','RMSE Close'] )
We can Infere that p=0, q=2 are the optimal which provides an the least RMSE.

Model building - fit and forecast, the time series data:

# from above example we can see that p=0 and q=2 gives least RMSE
model = VARMAX(train_diff[[ 'Open', 'High', 'Low', 'Close' ]], order=(0,2)).fit( disp=False)
result = model.forecast(steps = 30)
​
let’s inverse the forecasted results, as shown here:

results = inverse_diff(df2[['Open', 'High', 'Low', 'Close' ]],result)
results
Let's Evaluate the results individually,and infere from the output

for i in ['Open', 'High', 'Low', 'Close' ]:
    print(f'Evaluation metric for {i}')
    timeseries_evaluation_metrics_func(test[str(i)] , results[str(i)+'_1st_inv_diff'])
Visualize the results and infere from plots:

import matplotlib.pyplot as plt
%matplotlib inline
for i in ['Open', 'High', 'Low', 'Close' ]:
    
    plt.rcParams["figure.figsize"] = [10,7]
    plt.plot( train[str(i)], label='Train '+str(i))
    plt.plot(test[str(i)], label='Test '+str(i))
    plt.plot(results[str(i)+'_1st_inv_diff'], label='Predicted '+str(i))
    plt.legend(loc='best')
    plt.show()
​
​
​
END

# -------------------------------------------------------------------------------------------------------------
### In_Class_Whatsapp.ipynb

InClass
import required libraries
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from pylab import rcParams
rcParams['figure.figsize'] = 14, 7
Read Petrol. csv file
df = pd.read_csv('Petrol.csv')
df.Year.value_counts()
convert the given data into time series
date = pd.date_range(start='1/1/2001', end='1/1/2014', freq='Q')
date
df['TimeStamp'] = pd.DataFrame(date)
df.head()
df.info()
Plot the time series
df.set_index(keys='TimeStamp',drop=True,inplace=True)
df.head()
df_consumption = df.drop(['Year','Quarter'],axis=1)
df_consumption.plot(figsize=(15,8),grid=True)
fill the missing values using interpolation
df_consumption = df_consumption.interpolate()
df_consumption.isnull().sum()
df_consumption.plot(figsize=(15,8),grid=True)
decompose the given time series and give your inference on whether the series is additive or multiplicative
decomposition = seasonal_decompose(df_consumption,model='additive')
decomposition.plot()
decomposition = seasonal_decompose(df_consumption,model='multiplicative')
decomposition.plot()

# -------------------------------------------------------------------------------------------------------------
### In_Class.ipynb

InClass
import required libraries
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns
from warnings import filterwarnings
filterwarnings('ignore')
pd.options.display.float_format = '{:.6f}'.format
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import silhouette_score, silhouette_samples
from sklearn.cluster import KMeans
​
from sklearn.decomposition import PCA
from sklearn.impute import KNNImputer
from statsmodels.tsa.seasonal import seasonal_decompose
Read Petrol. csv file
df=pd.read_csv('Petrol.csv')
df.head()
df.dtypes
df.describe()
df.describe(include='object')
convert the given data into time series
df.Year.value_counts()
tsf = pd.date_range(start='1/1/2001', end='1/1/2014',tz=None, freq='Q')
tsf
df['QuarterEnd'] = pd.DataFrame(tsf)
df.head()
df.set_index(keys='QuarterEnd',drop=True,inplace=True)
df.head()
Plot the time series
df_tsf = df.drop(['Year','Quarter'],axis=1)
from pylab import rcParams
rcParams['figure.figsize'] = [15,10]
df_tsf.plot()
fill the missing values using interpolation
df_tsf=df_tsf.interpolate()
df_tsf.plot()
decompose the given time series and give your inference on whether the series is additive or multiplicative
tsf_decompose_add = seasonal_decompose(df_tsf,model='additive')
tsf_decompose_add.plot()
tsf_decompose_mul = seasonal_decompose(df_tsf,model='multiplicative')
tsf_decompose_mul.plot()
print("The magnitude of the seasonal component is not changing with time in both the above plots, Thus this series is not  multiplicative. This is an Additive Time Series")
# -------------------------------------------------------------------------------------------------------------
### Faculty_notebook_Stock_data.ipynb
As stock price data is available for buisness days only, time series might be discontinuos on daily basis. We should update the time series considering business days
from pandas.tseries.offsets import BDay
date = pd.date_range(start='05/01/2017', end='01/31/2019', freq=BDay())
date
adding business dates to time series as a new column
df['TimeStamp']=pd.DataFrame(date,columns=['Date'])
df.shape
df.head()
df['TimeStamp'] = pd.to_datetime(df['TimeStamp'])
df_model = df.set_index('TimeStamp')
df_model.head()
plotting time series
rcParams['figure.figsize'] = 25,8
df_model.plot(grid=True);
dropping unwanted columns
df_model=df_model.drop('Date',axis=1)
df_model.head()
cheking for NA values
df_model.isna().value_counts()
df_model.plot(grid=True);
lets plot mean across the months to check whether the time series is stationary or not
monthly_mean = df_model.resample('M').mean()
monthly_mean.plot.bar()
It can be observed that there are no as such fluctuations in mean with respect to time
Series seems to be stationary
applying Adfuller test to confirm the same
observations= df_model.values
test_result = adfuller(observations)
test_result
print('ADF Statistic: %f' % test_result[0])
print('p-value: %f' % test_result[1])
print('Critical Values:')
for key, value in test_result[4].items():
    print('\t%s: %.5f' % (key, value))
test results confirms that the series is stationary
Building ARMA model
To find p and q values of AR() and MA() processes, lets plot ACF and PACF
plot_acf(df_model);
plot_pacf(df_model);
ACF plot is clearly showing, time series observations are heavily impacted by past values. While PACF is showing limited number of spikes before cut-off
Can select AR(1) and MA(0) process to build ARMA model
splittng time series into training and testing sets
train_end=datetime(2018,10,30)
test_end=datetime(2019,1,31)
train             = df_model[:train_end] 
test              = df_model[train_end + timedelta(days=1):test_end]
train.shape
building ARMA model
model=ARMA(train,(1,0))
model_fit=model.fit()
print(model_fit.summary())
predicting forecasts using the model
pred_start=test.index[0]
pred_end=test.index[-1]
pred_end
forecast=model_fit.forecast(10)
forecast
predictions=model_fit.predict(start=pred_start, end=pred_end)
lets plot actual series and forecast
plt.plot(train,label='Training Data')
plt.plot(test,label='Test Data')
plt.plot(test.index,predictions,label='Predicted Data - ARMA(1,0)')
plt.legend(loc='best')
plt.grid();
finding residuals
residuals = test.Close - predictions
plt.plot(residuals)
plt.show()
accuracy matrix
from sklearn.metrics import mean_squared_error
mean_squared_error(test.values,predictions.values,squared=False)
def MAPE(y_true, y_pred):
    return np.mean((np.abs(y_true-y_pred))/(y_true))*100
MAPE(test.values,predictions.values)
residual q-q plot for to check model performance
qqplot(residuals,line="s");
forecast
model=ARMA(df_model,(1,0))
model_fit=model.fit()
forecast=model_fit.forecast(15)[0]
forecasting=pd.DataFrame(forecast)
date = pd.date_range(start='01/09/2019', periods=15, freq=BDay())
forecasting['timestamp']=date
forecasting=forecasting.set_index('timestamp')
forecasting
plt.plot(df_model,label='Data')
plt.plot(forecasting,label='forecast')
plt.legend(loc='best')
plt.grid();
End


# -------------------------------------------------------------------------------------------------------------
### Faculty_Notebook_AirPassenger.ipynb

Reading time series data
df = pd.read_csv('AirPassenger.csv',parse_dates=True,index_col = 'Year-Month')
df.head()
Plotting time series
rcParams['figure.figsize'] = 25,8
df.plot(grid=True);
Spliting time series data
Most recent observations will be used to test the model while remaining series will be used to train the model
if time series has seasonality, then test data must include atleast one seasonal period.
train_end=datetime(1958,12,31)
test_end=datetime(1960,12,31)
train             = df[:train_end] 
test              = df[train_end + timedelta(days=1):test_end]
print('Train')
display(train)
print('Test')
display(test)
Double Exponential Smoothing / Holt's linear Method
model_DES = Holt(train,exponential=True, initialization_method='estimated')
training the double exponential model
model_DES_fit1 = model_DES.fit(optimized=True)
model_DES_fit1.summary()
Predicting forecast
DES_predict1 = model_DES_fit1.forecast(steps=len(test))
Lets plot the forecast for SES and DES
plt.plot(train, label='Train')
plt.plot(test, label='Test')
​
plt.plot(DES_predict1, label='DES forecast')
plt.legend(loc='best')
plt.grid()
Triple Exponential Smoothing / Holt-Winters Method
lets build model using 'additive' seasonality
model_TES_add = ExponentialSmoothing(train,trend='additive',seasonal='additive',initialization_method='estimated')
training the model
model_TES_add = model_TES_add.fit(optimized=True)
model_TES_add.summary()
predicting forecast
TES_add_predict =  model_TES_add.forecast(len(test))
lets plot foecast results
plt.plot(train, label='Train')
plt.plot(test, label='Test')
​
plt.plot(TES_add_predict, label='TES forecast')
plt.legend(loc='best')
plt.grid()
Evaluating Model Performance
mean_squared_error(test.values,TES_add_predict.values,squared=False)
def MAPE(y_true, y_pred):
    return np.mean((np.abs(y_true-y_pred))/(y_true))*100
MAPE(test['Pax'],TES_add_predict)
lets build model uaing 'multiplicative' forecast
model_TES_mul = ExponentialSmoothing(train,trend='multiplicative',seasonal='multiplicative',initialization_method='estimated')
training the model
model_TES_mul = model_TES_mul.fit(optimized=True)
model_TES_mul.summary()
predicting forecast
TES_mul_predict =  model_TES_mul.forecast(len(test))
lets plot foecast results for H-W model with multiplicative seasonality
plt.plot(train, label='Train')
plt.plot(test, label='Test')
plt.plot(TES_mul_predict, label='TES forecast')
plt.legend(loc='best')
plt.grid()
Evaluating Model Performance
mean_squared_error(test.values,TES_mul_predict.values,squared=False)
Defining Mean Absolute Percentage error
def MAPE(y_true, y_pred):
    return np.mean((np.abs(y_true-y_pred))/(y_true))*100
Mean Absolute Percentage Error for simple forecasting model
MAPE(test['Pax'],TES_mul_predict)
forecasting
model_TES_mul = ExponentialSmoothing(df,trend='multiplicative',seasonal='multiplicative',initialization_method='estimated')
model_TES_mul = model_TES_mul.fit(optimized=True)
model_TES_mul.summary()
TES_mul_predict =  model_TES_mul.forecast(12)
plt.plot(df, label='data')
plt.plot(TES_mul_predict, label='TES forecast')
plt.legend(loc='best')
plt.grid()
END

# -------------------------------------------------------------------------------------------------------------
### Faculty Notebook_S4-ARIMA

Read the data set in a Time Series with proper Time frequency or period.
df = pd.read_csv('MaunaLoa.csv',parse_dates=['Year-Month'],index_col='Year-Month')
df.head(15)
Plot the Time Series Data.
from pylab import rcParams
rcParams['figure.figsize'] = 15,8
df.plot();
plt.grid()
Plot a boxplot to understand the variation of Carbon Dioxide in parts per million with respect to months across years.
sns.boxplot(x=df.index.month,y=df['CO2 ppm'])
plt.grid();
Plot a graph of monthly Carbon Dioxide in parts per million across years.
monthly_co2ppm_across_years = pd.pivot_table(df, values = 'CO2 ppm', columns = df.index.year, index = df.index.month_name())
monthly_co2ppm_across_years
monthly_co2ppm_across_years.plot()
plt.grid()
plt.legend(loc='best');
Decompose the Time Series to understand the various components.
decomposition = seasonal_decompose(df,model='additive')
decomposition.plot();
stationarity test
sns.boxplot(x=df.index.year,y=df['CO2 ppm'])
plt.grid();
observations= df.values
test_result = adfuller(observations)
test_result
applying differencing
df_diff = df.diff(periods=1).dropna()
observations= df_diff.values
test_result = adfuller(observations)
test_result
Check the ACF and PACF of the training data.
plot_acf(df,lags=30);
plot_pacf(df);
plot_acf(df_diff);
plot_pacf(df_diff);
Train-Test split
train_end=datetime(1978,12,1)
test_end=datetime(1980,12,1)
train             = df[:train_end] 
test              = df[train_end + timedelta(days=1):test_end]
Selecting an order of ARIMA model for data with the lowest Akaike Information Criteria (AIC).
import itertools
p = q = range(0, 4)
d= range(1,2)
pdq = list(itertools.product(p, d, q))
print('parameter combinations for the Model')
for i in range(1,len(pdq)):
    print('Model: {}'.format(pdq[i]))
dfObj1 = pd.DataFrame(columns=['param', 'AIC'])
dfObj1
for param in pdq:
            try:
                mod = ARIMA(train, order=param)
                results_Arima = mod.fit()
                print('ARIMA{} - AIC:{}'.format(param, results_Arima.aic))
                dfObj1 = dfObj1.append({'param':param, 'AIC': results_Arima.aic}, ignore_index=True)
​
            except:
                continue
dfObj1.sort_values(by=['AIC'])
model = ARIMA(train, order=(2,1,3))
​
results_Arima = model.fit()
​
print(results_Arima.summary())
Predict on the Test Set using this model and evaluate the model on the test set using RMSE and MAPE
pred_start=test.index[0]
pred_end=test.index[-1]
ARIMA_predictions=results_Arima.predict(start=pred_start, end=pred_end)
ARIMA_predictions
ARIMA_pred=ARIMA_predictions.cumsum()
ARIMA_pred
ARIMA_pred=pd.DataFrame(ARIMA_pred,columns=train.columns)
predict_fc = ARIMA_pred.copy()
columns = train.columns
for col in columns:        
        predict_fc[str(col)+'_forecast'] = train[col].iloc[-1] + predict_fc[str(col)]
predict_fc.head()
plt.plot(train,label='Training Data')
plt.plot(test,label='Test Data')
plt.plot(test.index,predict_fc['CO2 ppm_forecast'],label='Predicted Data - ARIMA')
plt.legend(loc='best')
plt.grid();
residuals = test['CO2 ppm'] - predict_fc['CO2 ppm_forecast']
qqplot(residuals,line="s");
from sklearn.metrics import  mean_squared_error
rmse = mean_squared_error(test['CO2 ppm'],predict_fc['CO2 ppm_forecast'], squared=False)
print(rmse)
def MAPE(y_true, y_pred):
    return np.mean((np.abs(y_true-y_pred))/(y_true))*100
mape=MAPE(test['CO2 ppm'].values,predict_fc['CO2 ppm_forecast'].values)
print(mape)
SARIMA Model
we will find the model parameters based on AIC criteria. Parameters will be generated using combination for the given range.
import itertools
p = q = range(0, 3)
d= range(1,2)
pdq = list(itertools.product(p, d, q))
​
model_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]
print('Examples of parameter combinations for Model...')
print('Model: {}{}'.format(pdq[1], model_pdq[1]))
print('Model: {}{}'.format(pdq[1], model_pdq[2]))
print('Model: {}{}'.format(pdq[2], model_pdq[3]))
print('Model: {}{}'.format(pdq[2], model_pdq[4]))
Creating an empty Dataframe with column names only where the model and AIC scores will be saved
dfObj2 = pd.DataFrame(columns=['param','seasonal', 'AIC'])
dfObj2
import statsmodels.api as sm
for param in pdq:
    for param_seasonal in model_pdq:
        mod = sm.tsa.statespace.SARIMAX(train,
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)
            
        results_SARIMA = mod.fit()
        print('SARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results_SARIMA.aic))
        dfObj2 = dfObj2.append({'param':param,'seasonal':param_seasonal ,'AIC': results_SARIMA.aic}, ignore_index=True)
sorting parameters for best AIC score
dfObj2.sort_values(by=['AIC'])
model = sm.tsa.statespace.SARIMAX(train,
                                order=(1,1,0),
                                seasonal_order=(1,1,2,12),
                                )
model_Sarima = model.fit()
print(model_Sarima.summary())
SARIMA_predictions=model_Sarima.predict(start=pred_start, end=pred_end)
plt.plot(train,label='Training Data')
plt.plot(test,label='Test Data')
plt.plot(test.index,SARIMA_predictions,label='Predicted Data - SARIMA')
plt.legend(loc='best')
plt.grid();
finding RSMA and MAPE
from sklearn.metrics import  mean_squared_error
rmse = mean_squared_error(test['CO2 ppm'],SARIMA_predictions, squared=False)
print(rmse)
mape = MAPE(test['CO2 ppm'],SARIMA_predictions)
print(mape)
model_Sarima.plot_diagnostics(figsize=(16, 8))
plt.show()
fitting model on whole data
model = sm.tsa.statespace.SARIMAX(df,
                                order=(1,1,0),
                                seasonal_order=(1,1,2,12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)
model_Sarima = model.fit()
print(model_Sarima.summary())
Forecast with confidence interval
forecast = model_Sarima.forecast(steps=24)
forecast
pred95 = model_Sarima.get_forecast(steps=24)
pred95=pred95.conf_int()
pred95
axis = df.plot(label='Observed', figsize=(15, 8))
forecast.plot(ax=axis, label='Forecast', alpha=0.7)
axis.fill_between(forecast.index, pred95['lower CO2 ppm'], pred95['upper CO2 ppm'], color='k', alpha=.15)
axis.set_xlabel('Year-Months')
axis.set_ylabel('CO2 ppm')
plt.legend(loc='best')
plt.show()
END



# -------------------------------------------------------------------------------------------------------------
###Assignment3_Inclass.ipynb

read AirTemp data and convert it to time series
df=pd.read_csv('AirTemp.csv')
df.head()
df.shape
df.dtypes
df.describe()
df.describe(include='object')
tsf = pd.date_range(start='1/1/1920',end='12/31/1939',freq='M')
tsf
df['MonthEnd'] = pd.DataFrame(tsf)
df.head()
df.set_index(keys='MonthEnd',drop=True,inplace=True)
df.head()
df_tsf = df.drop(['Year','Month'],axis=1)
df_tsf.head()
plot the time series
from pylab import rcParams
rcParams['figure.figsize'] = [15,10]
df_tsf.plot()
Check the stationarity of series using ADF test
ADFResult = adfuller(df_tsf.values)
ADF_Statistic=ADFResult[0]
p_value=ADFResult[1]
print('ADF_Statistic: %f' % ADF_Statistic)
print('p_value: %f' % p_value )
print('Critical Values:')
for key, value in ADFResult[4].items():
    print('\t%s: %.5f' % (key, value))
if p_value < 0.05:
    print ("Null Hypothesis failed. Data is Stationary")
If series is stationary, using ACF and PACF plot find the values of p and q
plot_acf(df_tsf)
plotting PACF
plot_pacf(df_tsf)
Split the data into traininga nd testing set
train_end = datetime(1938,12,31)
test_end = datetime(1939,12,31)
​
train = df_tsf[:train_end] 
test = df_tsf[train_end + timedelta(days=1):test_end]
train.shape
test.shape
train.tail()
test.head()
Build ARMA model for selected p and q
p=q=range(0, 4)
d=range(0,1)
pdq=list(itr.product(p, d, q))
print('combinations of parameters for the Model')
for i in range(1,len(pdq)):
    print('Model: {}'.format(pdq[i]))
df_pdq=pd.DataFrame(columns=['PARM', 'AIC'])
for parm in pdq:
    try:
        model=ARIMA(train,order=parm)
        results_Arima=model.fit()
        print('ARIMA',parm,' : AIC=',results_Arima.aic)
        df_pdq = df_pdq.append({'PARM':parm, 'AIC': results_Arima.aic}, ignore_index=True)
    except:
        continue
df_pdq.sort_values(by=['AIC'])
model = ARIMA(train, order=(2,0,3))
results= model.fit()
print(results.summary())
Find predictions of model for the range of test data
predictions=results.predict(start=test.index[0], end=test.index[-1])
predictions
Find residuals for the model and plot using Q-Q- plot
predict = pd.DataFrame(data=ARIMA_predictions,columns=test.columns,index=test.index)
predict.head()
residuals = test['AvgTemp'] - predict['AvgTemp']
qqplot(residuals,line="r")


# -------------------------------------------------------------------------------------------------------------
###  Assignment2_in_class

Read retail turnover data
df=pd.read_csv('RetailTurnover.csv')
df.head()
df.shape
df.dtypes
df.describe()
df.describe(include='object')
tsf = pd.date_range(start='9/1/1982', end='3/31/1992', freq='Q')
tsf
df['QuarterEnd'] = pd.DataFrame(tsf)
df.head()
df.set_index(keys='QuarterEnd',drop=True,inplace=True)
df.head()
df_tsf = df.drop(['Year','Quarter'],axis=1)
df_tsf.head()
Decompose the series to identify trends and seasonality
from pylab import rcParams
rcParams['figure.figsize'] = [15,10]
df_tsf.plot()
print('No Interpolation needed here')
tsf_decompose_add = seasonal_decompose(df_tsf,model='additive')
tsf_decompose_add.plot()
Split the time series data into training and testing sets
train=df_tsf[:datetime(1991,3,31)] 
test=df_tsf[datetime(1991,3,31) + timedelta(days=1):datetime(1992,3,31)]
train.head()
train.shape
test.head()
test.shape
Based on the trend and seasonality apply the Smoothing technique
model=ExponentialSmoothing(train, trend='add', seasonal='add', initialization_method='estimated')
model_seas=model.fit()
print(model_seas.params)
model_predict =  model_seas.forecast(len(test))
model_predict
plt.plot(train, label='Train',color='green')
plt.plot(test, label='Test',color='red')
plt.plot(model_predict, label='Test Smoothing technique' ,color='gold')
plt.legend()
plt.grid()
​
plt.title('Smoothing Predictions');
Find MAPE for your Model
metrics.mean_absolute_percentage_error(test.values, model_predict.values)
 """)