from functools import reduce
from operator import iconcat
from typing import Iterable
from numpy import sum, mean
from termcolor import colored
import random
import platform
from pyxai.source.core.structure.type import PreferredReasonMethod
import shap
import wordfreq


from time import time

class Stopwatch:
  def __init__(self):
    self.initial_time = time()

  def elapsed_time(self, *, reset=False):
    elapsed_time = time() - self.initial_time
    if reset:
      self.initial_time = time()
    return "{:.2f}".format(elapsed_time)
    
def flatten(l):
  return reduce(iconcat, l, [])

def count_dimensions(l):
  n = 0
  tmp = l
  while True:
    if isinstance(tmp, Iterable):
      n = n + 1
      tmp = tmp[0]
    else:
      break
  return n


_verbose = 1

def set_verbose(v):
  global _verbose
  v = int(v)
  _verbose = v



def verbose(*message):
  global _verbose
  if(_verbose > 0):
    print(*message)

def get_os():
  return platform.system().lower()

def shuffle(l):
  random.shuffle(l)
  return l

def add_lists_by_index(list1, list2):
  """
  Adding two lists results in a new list where each element is the sum of the elements in the corresponding positions of the two lists.
  """
  return [x + y for (x, y) in zip(list1, list2)]

def compute_accuracy(prediction, right_prediction):
  return (sum(prediction == right_prediction) / len(right_prediction)) * 100

def display_observation(observation, size=28):
  for i, element in enumerate(observation):
    print(colored('X', 'blue') if element == 0 else colored('X', 'red'), end='')
    if (i+1) % size == 0 and i != 0:
      print()

def compute_weight(method, instance, weights, ML_solver_information):
  if method is None:
    raise ValueError("The 'method' parameter is not correct (possible choice: Minimal, Weights, Shapely, FeatureImportance, WordFrequency, WordFrequencyLayers).")
  elif method == PreferredReasonMethod.Minimal:
    weights = [1 for l in range(len(instance))]
  elif method == PreferredReasonMethod.Weights:
    # weights: the weights chosen by the user, which correspond to the user's preference
    if isinstance(weights, list):
      weights = [-weights[i] + 1 + max(weights) for i in range(len(weights))]
    elif isinstance(weights, dict):
      feature_name = ML_solver_information.feature_name
      new_weights = [0 for i in range(len(feature_name))]
      for i in weights.keys():
        new_weights[abs(i)] = weights[i]
      weights = [-new_weights[i] + 1 + max(new_weights) for i in range(len(new_weights))]
    else:
      raise ValueError("The 'weights' parameter is not correct (must be a list a feature weights or a dict of features weights).")
      
  elif method == PreferredReasonMethod.Shapley:
    # Shapely values for the model trained on data.
    raw_model = ML_solver_information.raw_model
    
    shapely_explainer = shap.TreeExplainer(raw_model, model_output='raw') 
    shapely_values = shapely_explainer.shap_values(instance, check_additivity=False) 
    shapely_value = mean(shapely_values, axis=0) if len(shapely_values) > 2 else shapely_values[0]
    # Decreasing monotonous affine transformation for shapely values, w = alpha * x + b , where x = shapely_value
    # alpha = - min(a, 1) where a is the minimum value greater than zero of abs (shapely_value)
    alpha = min([i for i in abs(shapely_value) if i != 0])
    shapely_value = -shapely_value / min(alpha,1)
    weights = [round(shapely_value[i] - min(shapely_value) + 1) for i in range(len(shapely_value))]
  elif method == PreferredReasonMethod.FeatureImportance:
    # Feature importance from sklearn
    # Decreasing monotonous affine transformation
    raw_model = ML_solver_information.raw_model
    feature_importances = raw_model.feature_importances_
    alpha = min([i for i in feature_importances if i != 0])  # the minimum value greater than zero
    feature_importances = -10 * feature_importances / alpha  # alpha = -10/a, b = 1
    weights = [round(feature_importances[i] - min(feature_importances) + 1) for i in range(len(feature_importances))]
  elif method == PreferredReasonMethod.WordFrequency:
    feature_name = ML_solver_information.feature_name
    weights_feature = [int(wordfreq.zipf_frequency(l, 'en') * 100 * (wordfreq.zipf_frequency(l, 'en') > 0) 
                        + (wordfreq.zipf_frequency(l, 'en') == 0)) for l in feature_name]
    weights = [-weights_feature[i] + 1 + max(weights_feature) for i in range(len(weights_feature))]
  elif method == PreferredReasonMethod.WordFrequencyLayers:
    feature_name = ML_solver_information.feature_name
    weights = [0 for i in range(len(feature_name))]
    a = [0 for i in range(3)]  # number of layers - 1
    for i in range(len(feature_name)):
      if 6 < wordfreq.zipf_frequency(feature_name[i], 'en'):
          a[0] += 1
          weights[i] = 1
      if 4 < wordfreq.zipf_frequency(feature_name[i], 'en') <= 6:
          a[1] += 1
          weights[i] = 10 + a[0]  # for non-compensation
      if 2 < wordfreq.zipf_frequency(feature_name[i], 'en') <= 4:
          a[2] += 1
          weights[i] = 20 + a[0] + 10 * a[1]  # for non-compensation
      if 0 <= wordfreq.zipf_frequency(feature_name[i], 'en') <= 2:
          weights[i] = 100 + a[0] + 10 * a[1] + 20 * a[2]  # for non-compensation
  else:
    raise ValueError("The method parameter is not correct (possible choice: Minimal, Weights, Shapely, FeatureImportance, WordFrequency, WordFrequencyLayers).")
  return weights