"""
An example of how to use tuning module.
"""
# Imports
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd)
import pandas as pd
import numpy as np
from core_of_theaisphere.tuning.tune import TuneClassifier
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler, MinMaxScaler

"""
Author: vickyparmar
File: hyper_tuning.py
Created on: 11-10-2022, Tue, 16:20:28

Last modified by: vickyparmar
Last modified on: 13-10-2022, Thu, 16:44:46
"""


# DF
df = pd.read_csv("/Users/vickyparmar/git/theAIsphere/kaggle/data/ds-salaries/train.csv")
y = pd.Series(np.where(df.salary_in_usd <= 10000, 0, 1), name='target')
X = df.drop(['salary_in_usd'], axis=1, inplace=False)

cat_cols = ['employment_type', 'job_title', 'employee_residence', 'company_location',
            'company_size']
for col in cat_cols:
    X[col] = X[col].astype('category')

X.drop(cat_cols, axis=1, inplace=True)
ss = MinMaxScaler()
X_ss = pd.DataFrame(ss.fit_transform(X), columns=X.columns)

# Tuner
objectives = ['lr', 'svm', 'xgb', 'rf', 'dt', 'cat', 'lgbm', 'sgd', 'gnb']
metrics = ['roc_auc_score', 'accuracy_score', 'f1_score', 'fbeta_score', 'precision_score', 'recall_score']
metrics_directions = ['maximize', 'maximize', 'maximize', 'maximize', 'maximize', 'maximize']
cv = KFold(n_splits=3, shuffle=True, random_state=99)

optimization_config = {
                'n_trials': 5,
                'timeout': 3600
}
max_trials_callback = 5


tuner = TuneClassifier(x=X_ss, y=y, objective=objectives, save_loc='tmp/data', metrics=metrics,
                       metrics_directions=metrics_directions, cv=cv, random_state=99)
# print(f"Instance successfully created.")
tuner.tune(optimization_config=optimization_config, max_trials_callback=max_trials_callback)
print(tuner.multi_trials_df.head())
print(tuner.multi_trials_df.shape)
print(tuner.trials_df.head())
print(tuner.trials_df.shape)
