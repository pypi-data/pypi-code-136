from pyxai import Learning, Explainer, Tools

# Learning part
machine_learning = Learning.Scikitlearn("./compas.csv")
model = machine_learning.evaluate(method=Learning.HOLD_OUT, output=Learning.RF)
instance, prediction = machine_learning.get_instances(model, n=1, correct=False)

# Explanation part
explainer = Explainer.initialize(model, instance=instance)
print("instance:", instance)
print("instance binarized: ", explainer.implicant, len(explainer.implicant))
print("prediction:", prediction)
print("features: ", model.ML_solver_information.feature_name)
# excluded = ['Female']
excluded = ['Other', 'score_factor']

explainer.set_excluded_features(excluded)  # I do not understand the meaning of this features
direct_reason = explainer.direct_reason()
print("\ndirect reason:", direct_reason)  # None if excluded features appear in direct

sufficient_reason = explainer.sufficient_reason(time_limit=5)

print("\nsufficient reason:", "None" if sufficient_reason is None else explainer.to_features(sufficient_reason))
if explainer.elapsed_time == Explainer.TIMEOUT: print("Time out, this is an approximation")
if sufficient_reason is not None: print("is reason (for 50 checks)", sufficient_reason, explainer.is_reason(sufficient_reason, n_samples=50))

majoritary_reason = explainer.majoritary_reason(n=1)
print("\nmajoritary: ", "None" if majoritary_reason is None else explainer.to_features(majoritary_reason))

if majoritary_reason is not None:
  print("is_majoritary_reason:", explainer.is_majoritary_reason(majoritary_reason,))

minimal_majoritary_reason = explainer.minimal_majoritary_reason(n=1)
print("\nminimal majoritary: ", "None" if minimal_majoritary_reason is None else explainer.to_features(minimal_majoritary_reason))
if minimal_majoritary_reason is not None:
  print("is_majoritary_reason:", explainer.is_majoritary_reason(majoritary_reason))

# all_majoritariy_reasons = explainer.majoritary_reason(n=Explainer.ALL)
# print("all majoritaries", all_majoritariy_reasons[0], len(all_majoritariy_reasons))

minimal_constrative_reason = explainer.minimal_contrastive_reason(time_limit=5)
print("\nMinimal contrastive:", minimal_constrative_reason,
      "" if minimal_constrative_reason is None else explainer.to_features(minimal_constrative_reason))
if explainer.elapsed_time == Explainer.TIMEOUT: print("Time out, this is an approximation")
if minimal_constrative_reason is not None:
  print("is  contrastive: ", explainer.is_contrastive_reason(minimal_constrative_reason))
