from pyxai import Tools, Learning, Explainer

import pandas
import numpy 
import random
import functools
import operator
import copy

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import LeaveOneGroupOut

def load_dataset(dataset):
  data = pandas.read_csv(dataset).copy()
  labels = data[data.columns[-1]]
  labels = numpy.array(labels)
  data = data.drop(columns=[data.columns[-1]])
  features_name = list(data.columns)
  data = data.values
  return data, labels, features_name

def random_forest_cross_validation(X, Y, n_trees=100, n_forests=10) :
  n_instance = len(Y)
  quotient = n_instance // n_forests
  remain = n_instance % n_forests
  
  groups = [quotient*[i] for i in range(1,n_forests+1)]
  groups = functools.reduce(operator.iconcat, groups, [])
  groups += [i for i in range(1,remain+1)]
  random.shuffle(groups)
  
  loo = LeaveOneGroupOut()
  score = 0
  forests = []
  i = 0
  for index_training, index_test in loo.split(X, Y, groups=groups):
    if i < n_forests:
      i += 1
      x_train = [X[x] for x in index_training]
      y_train = [Y[x] for x in index_training]
      x_test = [X[x] for x in index_test]
      y_test = [Y[x] for x in index_test]
      rf = RandomForestClassifier(n_estimators=n_trees)
      rf.fit(x_train, y_train)
      y_predict = rf.predict(x_test)
      accuracy = (numpy.sum(y_predict == y_test)/len(y_test))*100
      score += accuracy
      forests.append(Learning.MLSolverInformation(copy.deepcopy(rf),index_training,index_test, groups, accuracy))
  return forests  

data, labels, features_name = load_dataset(Tools.Options.dataset)
# In order to convert the ML solver results, you need to pass by the MLSolverInformation object
forests = random_forest_cross_validation(data, labels)
# And the Learning.Scikitlearn() object
machine_learning = Learning.Scikitlearn(Tools.Options.dataset)
# Convert the Scikitlearn models into pyxai models
models = machine_learning.to_RF(forests)
# Get an instance 
instance = machine_learning.get_instances(n=1)

# Explainer part
explainer = Explainer.initialize(models[0], instance=instance)

direct = explainer.direct_reason()
print("direct:", direct)

sufficient = explainer.sufficient_reason()
print("sufficient:", sufficient)