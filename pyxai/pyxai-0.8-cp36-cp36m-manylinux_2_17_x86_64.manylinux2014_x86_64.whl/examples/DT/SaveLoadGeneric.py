from pyxai import Learning, Explainer, Tools

#Save part
MLsolver = Learning.Scikitlearn(Tools.Options.dataset)
models = MLsolver.evaluate(method=Learning.LeaveOneGroupOut, output=Learning.DT)
instance = MLsolver.get_instances(n=1)
MLsolver.save(models, "try1", generic=True)

sufficients = []
for model in models:
  explainer = Explainer.initialize(model, instance=instance)
  sufficients.append(explainer.sufficient_reason())


#Load part
print()
print("#############################################")
print()
dataset_name = Tools.Options.dataset.split("/")[-1].split(".")[0]
MLsolver, models = Learning.load(model_directory="try1/"+dataset_name+"_model/") 
for i, model in enumerate(models):
  explainer = Explainer.initialize(model, instance=instance)
  sufficient = explainer.sufficient_reason()
  assert sufficient == sufficients[i], "Bad assert !"
  