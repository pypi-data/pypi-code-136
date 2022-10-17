from pyxai import *

nodeT1_1 = DecisionNode(1, left=0, right=1)
nodeT1_3 = DecisionNode(3, left=0, right=nodeT1_1)
nodeT1_2 = DecisionNode(2, left=0, right=nodeT1_3)
nodeT1_4 = DecisionNode(4, left=0, right=nodeT1_2)

tree1 = DecisionTree(TypeTree.PREDICTION, 4, nodeT1_1)

nodeT2_4 = DecisionNode(4, left=0, right=1)
nodeT2_1 = DecisionNode(1, left=0, right=nodeT2_4)
nodeT2_2 = DecisionNode(2, left=nodeT2_1, right=1)

tree2 = DecisionTree(TypeTree.PREDICTION, 4, nodeT2_2) #4 features but only 3 used

nodeT3_1_1 = DecisionNode(1, left=0, right=1)

nodeT3_1_2 = DecisionNode(1, left=0, right=1)
nodeT3_4_1 = DecisionNode(4, left=0, right=nodeT3_1_1)
nodeT3_4_2 = DecisionNode(4, left=0, right=1)

nodeT3_2_1 = DecisionNode(2, left=nodeT3_1_2, right=nodeT3_4_1)
nodeT3_2_2 = DecisionNode(2, left=0, right=nodeT3_4_2)

nodeT3_3_1 = DecisionNode(3, left=nodeT3_2_1, right=nodeT3_2_2)

tree3 = DecisionTree(TypeTree.PREDICTION, 4, nodeT3_3_1)

observation = [1,1,1,1]
forest = RandomForest([tree1, tree2, tree3])

cnf = forest.to_CNF(observation)
print(cnf)