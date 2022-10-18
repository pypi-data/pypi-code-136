from re import sub
import sklearn
# import lightgbm as lgb
import xgboost as xgb

def logistic_regression(**params):
    model = sklearn.linear_model.LogisticRegression(**params["parameters"])
    return model

def svm_svc(**params):
    model = sklearn.svm.SVC(**params["parameters"])
    return model

def gaussian_naive_bayes(**params):
    model = sklearn.sklearn.naive_bayes.GaussianNB(**params["parameters"])
    return model

def multinomial_naive_bayes(**params):
    model = sklearn.naive_bayes.MultinomialNB(**params["parameters"])
    return model

def st_gradient_descent(**params):
    model = sklearn.linear_model.SGDClassifier(**params["parameters"])
    return model

def knn(**params):
    model = sklearn.neighbors.KNeighborsClassifier(**params["parameters"])
    return model

def decision_tree(**params):
    model = sklearn.tree.DecisionTreeClassifier(**params["parameters"])
    return model

def random_forest(**params):
    model = sklearn.ensemble.RandomForestClassifier(**params["parameters"])
    return model

def gradient_boosting(**params):
    model = sklearn.ensemble.GradientBoostingClassifier(**params["parameters"])
    return model

# def lgbm(**params):
#     model = lgb.LGBMClassifier(**params["parameters"])
#     return model

def xgboost(**params):
    model = xgb.XGBClassifier(**params["parameters"])
    return model

