from pyxai import Learning, Explainer, Tools

#Save part
MLsolver = Learning.Scikitlearn(Tools.Options.dataset)
models = MLsolver.evaluate(method=Learning.LEAVE_ONE_GROUP_OUT, output=Learning.RF)
instance, prediction = MLsolver.get_instances(n=1)

MLsolver.save(models, "try1", generic=True)

majoritaries = []
for model in models:
  explainer = Explainer.initialize(model, instance=instance)
  majoritaries.append(explainer.sufficient_reason())


#Load part
print()
print("#############################################")
print()
MLsolver, models = Learning.load(models_directory="try1") 
for i, model in enumerate(models):
  explainer = Explainer.initialize(model, instance=instance)
  majoritary = explainer.sufficient_reason()
  print("majoritary1:", majoritary)
  print("majoritary2:", majoritaries[i])
  
  
  assert majoritary == majoritaries[i], "Bad assert !"
  