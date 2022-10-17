from pyxai import *

#MLsolver part
MLsolver = Xgboost("dataset/mnist38.csv")
BTs = MLsolver.simple_validation().to_boosted_trees()[0]

instances = MLsolver.get_instances(BTs, correct=True)

for element in instances:
  instance, prediction_solver = element
  prediction_tree = BTs.predict(instance)
  assert prediction_tree == prediction_solver, "bad prediction" 


# instance with the prediction 0
instance_of_class_0 = [instance[0] for instance in instances if instance[1] == 0][0]
explanation = ExplanationBT(BTs, instance_of_class_0)

print("instance_of_class_0:", instance_of_class_0)
print("implicant0:", explanation.implicant)
print("size implicant:", len(explanation.implicant))

abductive = explanation.compute_abductive_reason()
print("abductive reason0:", abductive)
print("len abductive reason0:", len(abductive))

print("is_abductive0:", explanation.is_abductive_reason(abductive))

minimal_abductive = explanation.compute_minimal_abductive_reason()
print("minimal abductive reason:", minimal_abductive)
print("minimal is_abductive:", explanation.is_abductive_reason(minimal_abductive))

heatmap = HeatMap(28, 28, instance)

image1 = heatmap.new_image("Instance").set_instance(instance_of_class_0)

image2 = heatmap.new_image("Abductive")
image2.add_features(explanation.to_features(abductive, details=True))

heatmap.display()
exit(0)
# instance with the prediction 1
instance_of_class_1 = [instance[0] for instance in instances if instance[1] == 1][0]
explanation = ExplanationBT(BTs, instance_of_class_1)

print("implicant1:", explanation.implicant)
print("instance_of_class_1:", instance_of_class_1)

abductive = explanation.compute_abductive_reason()
print("abductive reason1:", abductive)
print("is_abductive1:", explanation.is_abductive_reason(abductive))

heatmap = HeatMap(28, 28, instance)

image1 = heatmap.new_image("Instance").set_instance(instance_of_class_1)

image2 = heatmap.new_image("Abductive")
image2.add_features(explanation.to_features(abductive, details=True))

heatmap.display()

#minimal_abductive = explanation.compute_minimal_abductive_reason()
#print("minimal abductive reason:", minimal_abductive)
#print("minimal is_abductive:", explanation.is_abductive_reason(minimal_abductive))

