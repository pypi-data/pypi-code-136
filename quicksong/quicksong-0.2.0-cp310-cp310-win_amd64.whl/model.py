# -*- coding: utf-8 -*-
# -*- mode: python -*-
""" Example support vector classifier model """


def train_classifier(X, y, cls_params, split_params):
    from sklearn.svm import SVC
    from sklearn.model_selection import train_test_split
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler

    ppl = make_pipeline(StandardScaler(), SVC(**cls_params))

    X_train, X_test, y_train, y_test = train_test_split(X, y, **split_params)

    ppl.fit(X_train, y_train)
    score = ppl.score(X_test, y_test)
    return ppl, score


