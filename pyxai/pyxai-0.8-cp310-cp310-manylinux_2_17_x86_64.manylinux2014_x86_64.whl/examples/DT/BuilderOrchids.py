
# Example taken from the paper quoted below: "The decision tree in Figure 1 separates Cattleya orchids from other
# orchids using the following features: x1: “has fragrant flowers”, x2: “has one or
# two leaves”, x3: “has large flowers”, and x4: “is sympodial”."

# @misc{https://doi.org/10.48550/arxiv.2108.05266,
#   doi = {10.48550/ARXIV.2108.05266},
#   url = {https://arxiv.org/abs/2108.05266},
#   author = {Audemard, Gilles and Bellart, Steve and Bounia, Louenas and Koriche, Frédéric and Lagniez, Jean-Marie and Marquis, Pierre},
#   keywords = {Artificial Intelligence (cs.AI), FOS: Computer and information sciences, FOS: Computer and information sciences, I.2.6},
#   title = {On the Explanatory Power of Decision Trees},
#   publisher = {arXiv},
#   year = {2021},
#   copyright = {Creative Commons Attribution 4.0 International}
# }

from pyxai import Builder, Explainer


#Builder part
node_x4_1 = Builder.DecisionNode(4, left=0, right=1)
node_x4_2 = Builder.DecisionNode(4, left=0, right=1)
node_x4_3 = Builder.DecisionNode(4, left=0, right=1)
node_x4_4 = Builder.DecisionNode(4, left=0, right=1)
node_x4_5 = Builder.DecisionNode(4, left=0, right=1)

node_x3_1 = Builder.DecisionNode(3, left=0, right=node_x4_1)
node_x3_2 = Builder.DecisionNode(3, left=node_x4_2, right=node_x4_3)
node_x3_3 = Builder.DecisionNode(3, left=node_x4_4, right=node_x4_5)

node_x2_1 = Builder.DecisionNode(2, left=0, right=node_x3_1)
node_x2_2 = Builder.DecisionNode(2, left=node_x3_2, right=node_x3_3)

node_x1_1 = Builder.DecisionNode(1, left=node_x2_1, right=node_x2_2)

tree = Builder.DecisionTree(4, node_x1_1, force_features_equal_to_binaries=True)

#Explainer part for instance = (1,1,1,1)
print("instance = (1,1,1,1):")
explainer = Explainer.initialize(tree, instance=(1,1,1,1))

print("target_prediction:", explainer.target_prediction)
direct = explainer.direct_reason()
print("direct:", direct)
assert direct == (1, 2, 3, 4), "The direct reason is not good !"

sufficient_reasons = explainer.sufficient_reason(n=Explainer.ALL)
print("sufficient_reasons:", sufficient_reasons)
assert sufficient_reasons == ((1, 4), (2, 3, 4)), "The sufficient reasons are not good !"

for sufficient in sufficient_reasons:
  assert explainer.is_sufficient_reason(sufficient), "This is have to be a sufficient reason !"

minimals = explainer.minimal_sufficient_reason()
print("Minimal sufficient reasons:", minimals)
assert minimals == (1, 4), "The minimal sufficient reasons are not good !"

contrastives = explainer.contrastive_reason(n=Explainer.ALL)
print("Contrastives:", contrastives)
for contrastive in contrastives:
  assert explainer.is_contrastive_reason(contrastive), "This is have to be a contrastive reason !"



#Explainer part for instance = (0,0,0,0)
print("\ninstance = (0,0,0,0):")

explainer.set_instance((0,0,0,0))

print("target_prediction:", explainer.target_prediction)
direct = explainer.direct_reason()
print("direct:", direct)
assert direct == (-1, -2), "The direct reason is not good !"

sufficient_reasons = explainer.sufficient_reason(n=Explainer.ALL)
print("sufficient_reasons:", sufficient_reasons)
assert sufficient_reasons == ((-4,), (-1, -2), (-1, -3)), "The sufficient reasons are not good !"
for sufficient in sufficient_reasons:
  assert explainer.is_sufficient_reason(sufficient), "This is have to be a sufficient reason !"
minimals = explainer.minimal_sufficient_reason(n=1)
print("Minimal sufficient reasons:", minimals)
assert minimals == (-4,), "The minimal sufficient reasons are not good !"

