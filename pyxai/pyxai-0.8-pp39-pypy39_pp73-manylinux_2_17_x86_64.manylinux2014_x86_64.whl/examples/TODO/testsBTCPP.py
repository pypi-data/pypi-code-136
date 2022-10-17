from pyxai import *

node1_3 = DecisionNode(3, 0.5, left=0.3, right=-0.4)
node1_2 = DecisionNode(2, 0.5, left=-0.2, right=0.1)
node1_1 = DecisionNode(1, 0.5, left=node1_2, right=node1_3)
tree1 = DecisionTree(TypeTree.WEIGHT, 4, node1_1, target_class=0)

node2_4 = DecisionNode(4, 0.5, left=-0.2, right=0.5)
node2_3 = DecisionNode(3, 0.5, left=-0.3, right=0.1)
node2_2 = DecisionNode(2, 0.5, left=node2_3, right=node2_4)
tree2 = DecisionTree(TypeTree.WEIGHT, 4, node2_2, target_class=1)

instance = (1,1,1,1)
print("instance:", instance)
BTs = BoostedTrees([tree1, tree2], n_classes=2)

explainer = ExplainerBT(BTs, instance)
print(explainer.compute_abductive_reason())

print("target_prediction:",explainer.target_prediction)
assert explainer.target_prediction == 1, "Bad assert"

print("With C++:", explainer.compute_abductive_reason(cpp=True))

