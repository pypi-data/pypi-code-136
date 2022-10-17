from pyxai import Learning, Explainer, Tools

# Learning part
machine_learning = Learning.Scikitlearn("./compas.csv")
model = machine_learning.evaluate(method=Learning.HOLD_OUT, output=Learning.DT)
instance, prediction = machine_learning.get_instances(model, n=1, correct=False)

#Explanation part
explainer = Explainer.initialize(model, instance)
print("instance:", instance)
print("instance binarized: ", explainer.implicant)
print("prediction:", prediction)

excluded = ['Other', 'score_factor']
#excluded = ['Other', 'Number_of_Priors']
explainer.set_excluded_features(excluded)  #I do not understand the meaning of this features

direct_reason = explainer.direct_reason()
print("\ndirect reason:", direct_reason) # None if excluded features appears in direct

print("\nnecessary literals", explainer.necessary_literals())
print("necessary are in excluded: ", explainer.reason_contains_features(explainer.necessary_literals(), excluded))
print("relevant literals", explainer.relevant_literals())
sufficient_reason = explainer.sufficient_reason(n=1)
print("\nsufficient reason", sufficient_reason, "" if sufficient_reason is None else explainer.to_features(sufficient_reason))
if sufficient_reason is not None:
  print("is sufficient reason ", explainer.is_sufficient_reason(sufficient_reason))

contrastives_reasons = explainer.contrastive_reason(n=Explainer.ALL)
print("\ncontrastives reasons", contrastives_reasons)

minimal_reason = explainer.minimal_sufficient_reason(n=1)
print("\nminimal reason", minimal_reason, "" if sufficient_reason is None else explainer.to_features(minimal_reason))

print("\nn reasons per attributes: ", explainer.n_sufficient_reasons_per_attribute())

explainer.unset_specific_features()
print("Without excluded feature\nn reasons per attributes: ", explainer.n_sufficient_reasons_per_attribute())
