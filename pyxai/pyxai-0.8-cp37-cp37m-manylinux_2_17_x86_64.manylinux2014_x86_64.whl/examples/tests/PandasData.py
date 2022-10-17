from pyxai import Learning, Tools

import pandas

# case where there no labels, you must add the labels
data = pandas.read_csv("pyxai/examples/tests/iris.data", names=['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width', 'Class'])

MLsolver = Learning.Xgboost(data)

