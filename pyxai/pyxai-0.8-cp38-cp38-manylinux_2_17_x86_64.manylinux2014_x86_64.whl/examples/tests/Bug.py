from pyxai import Learning, Explainer, Tools
MLsolver = Learning.Scikitlearn("../pylearningexplainer-web/assets/notebooks/dataset/iris.csv")
model = MLsolver.evaluate(method=Learning.HOLD_OUT, output=Learning.DT)

instance, prediction = MLsolver.get_instances(model, n=1, correct=True, predictions=[0])
explainer = Explainer.initialize(model, instance)

print("instance:", instance)
print("implicant:", explainer.implicant)
print("target_prediction:", explainer.target_prediction)

print("to_features:", explainer.to_features(explainer.implicant))

