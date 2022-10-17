
from pyxai.source.learning.MLSolver import MLSolver, MLSolverInformation, NoneData
from pyxai.source.core.tools.utils import flatten, shuffle, compute_accuracy
from pyxai.source.core.structure.decisionTree import DecisionTree, DecisionNode, LeafNode
from pyxai.source.core.structure.randomForest import RandomForest
from pyxai.source.core.structure.boostedTrees import BoostedTrees
from pyxai.source.core.structure.type import TypeReason

import pandas
import copy
import pickle
import os
import numpy
import json




class Generic(MLSolver):
    def __init__(self, data=NoneData):
      super().__init__(data)
    
    def get_solver_name(self):
      return str(self.__class__.__name__)

    def fit_and_predict_DT(self, instances_training, instances_test, labels_training, labels_test):
      assert False, "No possible evaluation for a generic ML solver"

    def fit_and_predict_RF(self, instances_training, instances_test, labels_training, labels_test):
      assert False, "No possible evaluation for a generic ML solver"

    def fit_and_predict_BT(self, instances_training, instances_test, labels_training, labels_test):
      assert False, "No possible evaluation for a generic ML solver"

    """
    Convert the Scikitlearn's decision trees into the program-specific objects called 'DecisionTree'.
    """
    def to_DT(self, ML_solver_information=None):  
      if ML_solver_information is not None: self.ML_solver_information = ML_solver_information
      decision_trees = []
      for id_solver_results,_ in enumerate(self.ML_solver_information):
        dt = self.ML_solver_information[id_solver_results].raw_model
        decision_trees.append(self.classifier_to_DT(dt, id_solver_results))
      return decision_trees
    
    def to_RF(self, ML_solver_information=None):
      if ML_solver_information is not None: self.ML_solver_information = ML_solver_information
      random_forests = []
      for id_solver_results,_ in enumerate(self.ML_solver_information):
        random_forest = self.ML_solver_information[id_solver_results].raw_model
        n_classes = random_forest[0]
        decision_trees = []
        for dt in random_forest[1]:
          decision_trees.append(self.classifier_to_DT(dt, id_solver_results))
        random_forests.append(RandomForest(decision_trees, n_classes=n_classes, ML_solver_information=self.ML_solver_information[id_solver_results]))
      return random_forests

    def to_BT(self, ML_solver_information=None):   
      if ML_solver_information is not None: self.ML_solver_information = ML_solver_information
      boosted_trees = []
      for id_solver_results,_ in enumerate(self.ML_solver_information):
        random_forest = self.ML_solver_information[id_solver_results].raw_model
        n_classes = random_forest[0]
        decision_trees = []
        for dt in random_forest[1]:
          decision_trees.append(self.classifier_to_DT(dt, id_solver_results))
        boosted_trees.append(BoostedTrees(decision_trees, n_classes=n_classes, ML_solver_information=self.ML_solver_information[id_solver_results]))
      return boosted_trees
   
    def classifier_to_DT(self, raw_dt, id_solver_results=0):
      n_features = raw_dt[0]
      target_class = raw_dt[1]
      root = self.raw_node_to_decision_node(raw_dt[2])
      return DecisionTree(n_features, root, target_class, id_solver_results=id_solver_results, ML_solver_information=self.ML_solver_information[id_solver_results])

    def raw_node_to_decision_node(self, raw_dt):
      if isinstance(raw_dt, (float, int)):
        # Leaf
        return raw_dt
      elif isinstance(raw_dt[0], str):
        # Node
        assert raw_dt[0].startswith("f"), "Have to start by f !"
        id_feature = int(raw_dt[0].split("<")[0].split("f")[1].strip())
        threshold = float(raw_dt[0].split("<")[1].strip())
        return DecisionNode(id_feature, threshold=threshold, left=self.raw_node_to_decision_node(raw_dt[1]), right=self.raw_node_to_decision_node(raw_dt[2]))
      else:
        assert False, "It is not possible !"

    def load_model(self, model_file):
      f = open(model_file)
      classifier = json.loads(json.load(f))
      f.close()
      return classifier
 