from pyxai import *

MLsolver = Scikitlearn("dataset/mnist38.csv")

#One tree
trees = MLsolver.simple_validation().to_decision_trees()
instance = MLsolver.get_instance(trees[0], correct=True)
explanation = ExplanationDT(trees[0], instance)
print("One tree: ok")

#Several Trees
trees = MLsolver.cross_validation(n_trees=4).to_decision_trees()
instance = MLsolver.get_instance(trees[0], correct=True)
explanation = ExplanationDT(trees[0], instance)
print("Several trees: ok")

