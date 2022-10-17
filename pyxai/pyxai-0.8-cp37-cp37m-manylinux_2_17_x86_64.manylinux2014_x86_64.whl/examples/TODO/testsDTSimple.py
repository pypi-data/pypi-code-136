from pyxai import *

node4 = DecisionNode(4, 0.5, left=0, right=1)
node3 = DecisionNode(3, 0.5, left=0, right=node4)
node2 = DecisionNode(2, 0.5, left=1, right=node3)
node1 = DecisionNode(1, 0.5, left=0, right=node2)
observation = [1,1,1,1,1]

print("instance:", observation)

tree = DecisionTree(TypeTree.PREDICTION, 5, node1)
explanation = ExplanationDT(tree, observation)

cnf = tree.to_CNF(observation)
print("implicant:", tree.observation_to_binaries(observation))

direct = explanation.compute_reasons(TypeReason.Direct)
print("direct:", direct)

sufficient = explanation.compute_reasons(TypeReason.Sufficient)
print("sufficient:", sufficient)

minimal_sufficient = explanation.compute_reasons(TypeReason.MinimalSufficient)
print("minimal_sufficient:", minimal_sufficient)

sufficients = explanation.compute_reasons(TypeReason.Sufficient, size=ALL)
print("sufficients:", sufficients)

contrastives = explanation.compute_reasons(TypeReason.Contrastive, size=ALL)
print("Contrastives:", contrastives)
