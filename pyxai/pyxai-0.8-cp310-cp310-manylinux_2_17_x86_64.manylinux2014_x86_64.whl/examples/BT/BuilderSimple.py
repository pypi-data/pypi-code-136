from pyxai import Builder, Explainer

node1_3 = Builder.DecisionNode(3, 0.5, left=0.3, right=-0.4)
node1_2 = Builder.DecisionNode(2, 0.5, left=-0.2, right=0.1)
node1_1 = Builder.DecisionNode(1, 0.5, left=node1_2, right=node1_3)
tree1 = Builder.DecisionTree(4, node1_1, target_class=0)

node2_4 = Builder.DecisionNode(4, 0.5, left=-0.2, right=0.5)
node2_3 = Builder.DecisionNode(3, 0.5, left=-0.3, right=0.1)
node2_2 = Builder.DecisionNode(2, 0.5, left=node2_3, right=node2_4)
tree2 = Builder.DecisionTree(4, node2_2, target_class=0)

instance = (0,0,0,0)
print("instance:", instance)
BTs = Builder.BoostedTrees([tree1, tree2], n_classes=2)

explainer = Explainer.initialize(BTs, instance)

print("target_prediction:",explainer.target_prediction)
#assert explainer.target_prediction == 1, "Bad assert"

direct = explainer.direct_reason()
print("direct reason:", direct)

ts = explainer.tree_specific_reason(reason_expressivity=Explainer.CONDITIONS)
print("ts:", ts)

#assert abductive==(2, 4), "Bad assert"
#assert(explainer.is_abductive_reason(abductive), "Bad assert")

