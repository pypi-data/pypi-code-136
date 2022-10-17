# KNN回归器
from sklearn.neighbors import KNeighborsRegressor
# KNN分类器
from sklearn.neighbors import KNeighborsClassifier

from itproject.machinelearning.KNNRegressor import KNNRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
# 随机森林 回归
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
# 支持向量机 分类
from sklearn.svm import SVC
# 支持向量机 回归
from sklearn.svm import SVR
from sklearn.tree import plot_tree
from itproject.utils import DataUtil, ChartUtil, AnalyseUtil

knn_regressor = KNeighborsRegressor()
myknn_regressor = KNNRegressor()
knn_classifier = KNeighborsClassifier()
knnType = "R"


def fit(X_train, y_train, knn_type="R",self=False):
    """用训练数据训练模型,默认是用KNN回归器，type=C表示用KNN分类器, self=False表示用Numpy的库，self=true表示用自定义的"""
    global knn_regressor
    global myknn_regressor
    global knn_classifier
    global knnType
    knnType = knn_type
    if knn_type == "R":
        if not self:
            knn_regressor.fit(X_train, y_train)
        else:
            myknn_regressor.fit(X_train, y_train)
    else:
        knn_classifier.fit(X_train, y_train)


def predict(X_test):
    """预测"""
    print("预测用的算法：{}".format(knnType))
    if knnType == "R":
        return knn_regressor.predict(X_test)
    else:
        return knn_classifier.predict(X_test)
