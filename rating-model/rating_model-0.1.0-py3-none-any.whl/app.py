import os
import pandas as pd
import numpy as np
import xgboost as xgb
import joblib

package_dir = os.path.dirname(__file__)


class size_finder(object):

    def __init__(self, df):
        super(size_finder, self).__init__()
        self.df = df.copy()

    def __repr__(self) -> str:
        return 'this is a size classifier'

    def predict(self):

        path1 = os.path.join(package_dir, 'models/initail_preprocess.pkl')
        path2 = os.path.join(package_dir, 'models/final_preprocess.pkl')
        path3 = os.path.join(package_dir, 'models/rating_classifier.model')
        data_link = os.path.join(package_dir, 'data/data.csv')
        p1 = joblib.load(path1)
        p2 = joblib.load(path2)

        model = xgb.XGBClassifier()
        model.load_model(path3)

        xx = pd.read_csv(data_link, index_col=0)
        xx = p1.transform(xx, drop_col=True)
        p2.fit(xx)

        x = p1.transform(self.df, drop_col=True)
        x = p2.transform(x)
        predict = model.predict(x)

        return predict
