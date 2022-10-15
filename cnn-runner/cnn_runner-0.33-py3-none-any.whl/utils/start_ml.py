import numpy as np
import pandas as pd
import math
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.model_selection import GridSearchCV
import pickle
import os
import time


def create_models(dataset_url='../seg_datasets/sem_seg_data.csv', reg_models_path='../seg_datasets/reg_models'):

    df = pd.read_csv(dataset_url, delimiter=';')

    df_v1 = df.iloc[:, :]

    print(df.info)

    print(df_v1.head())

    y = df_v1.iloc[:, 3]
    new_y = []
    for yy in y:
        if yy == "forest":
            new_y.append(0)
        elif yy == "water":
            new_y.append(1)
        else:
            new_y.append(2)
    y = new_y

    print(y)

    X = df_v1.iloc[:, :3]

    poly_pipeline = Pipeline([
        ('std_scaler', StandardScaler())
    ])

    X_poly = poly_pipeline.fit_transform(X)

    # print("Start LR ")
    # lr_start = time.process_time()
    # lr = LinearRegression()
    # lr.fit(X_poly, y)
    # lr_time = time.process_time() - lr_start
    #
    # print("Start SGD ")
    # sgd_start = time.process_time()
    # sgd = SGDRegressor()
    # sgd.fit(X_poly, y)
    # sgd_time = time.process_time() - sgd_start

    # print("Start DecisionTree")
    # tree_start = time.process_time()
    # dt = DecisionTreeRegressor()
    # dt.fit(X_poly, y)
    # dt_time = time.process_time() - tree_start
    #
    print("Start Random Forest Regressor")
    random_tree_start = time.process_time()
    rf = RandomForestRegressor()
    rf.fit(X_poly, y)
    rf_time = time.process_time() - random_tree_start
    #
    # print("Start AdaBoost Regressor")
    # ada_start = time.process_time()
    # ada = AdaBoostRegressor()
    # ada.fit(X_poly, y)
    # ada_time = time.process_time() - ada_start
    #
    print("Start Bagging Regressor")
    bag_start = time.process_time()
    bag = BaggingRegressor()
    bag.fit(X_poly, y)
    bag_time = time.process_time() - bag_start

    print('{0:^30s}'.format('ML Training time'))
    print('-' * 50)
    format_str_s = "{0:^10s}|{1:^10s}|{2:^10s}|{3:^10s}|{4:^10s}|{5:^10s}|{6:^10s}"
    print(format_str_s.format('LR t', 'SGD t', 'SVR t', 'Tree t', 'RF t', 'AdaBoost t', 'Bagging t'))
    print('-' * 50)
    format_str = "{0:^10.3f}|{1:^10.3f}|{2:^10.3f}|{3:^10.3f}|{4:^10.3f}|{5:^10.3f}|{6:^10.3f}"
    print(format_str.format(0, 0, 0, 0, rf_time, 0, bag_time))
    print('-' * 50)

    if not os.path.exists(reg_models_path):
        os.makedirs(reg_models_path)

    pickle.dump(poly_pipeline, open(os.path.join(reg_models_path, 'poly_pipeline.pkl', ), 'wb'), protocol=4)

    # pickle.dump(lr, open(os.path.join(dest, 'lin_reg.pkl'), 'wb'), protocol=4)
    # pickle.dump(sgd, open(os.path.join(dest, 'sgd_reg.pkl'), 'wb'), protocol=4)
    # pickle.dump(svr, open(os.path.join(dest, 'svr_reg.pkl'), 'wb'), protocol=4)
    # pickle.dump(ada, open(os.path.join(dest, 'ada_boost_reg.pkl'), 'wb'), protocol=4)
    # pickle.dump(bag, open(os.path.join(reg_models_path, 'bagging_reg.pkl'), 'wb'), protocol=4)
    # pickle.dump(dt, open(os.path.join(dest, 'tree_reg.pkl'), 'wb'), protocol=4)
    pickle.dump(rf, open(os.path.join(reg_models_path, 'random_forest_reg.pkl'), 'wb'), protocol=4)



if __name__ == '__main__':
    create_models()
