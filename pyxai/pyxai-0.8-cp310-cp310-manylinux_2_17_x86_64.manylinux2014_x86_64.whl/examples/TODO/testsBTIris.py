from pyxai import *

#MLsolver part
MLsolver = Xgboost("dataset/iris.csv")

BTs = MLsolver.evaluate(method=EvaluationMethod.HoldOut, output=EvaluationOutput.BoostedTrees)[0]

instances = MLsolver.get_instances(BTs, correct=True)

for element in instances:
  instance, prediction_solver = element
  prediction_tree = BTs.predict(instance)
  assert prediction_tree == prediction_solver, "bad prediction" 

exit(0)
explainer = ExplainerBT(BTs, instance)

print("implicant:", explainer.implicant)
print("instance:", instance)
print("len(implicant):", len(explainer.implicant))

abductive = explainer.compute_abductive_reason()
print("abductive reason:", abductive)
print("len(abductive reason)", len(abductive))

print("is_abductive:", explainer.is_abductive_reason(abductive))

minimal_abductive = explainer.compute_minimal_abductive_reason()
print("minimal abductive reason:", minimal_abductive)
print("len(minimal_abductive)", len(minimal_abductive))
print("minimal is_abductive:", explainer.is_abductive_reason(minimal_abductive))

