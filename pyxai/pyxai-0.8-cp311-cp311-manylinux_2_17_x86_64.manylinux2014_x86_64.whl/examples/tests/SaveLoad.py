
from pyxai import Learning, Tools

### BT LeaveOneGroupOut ###

model_directory="save_test"
dataset="examples/tests/yeast.csv"

#Evaluate and save the model
main_stopwatch = Tools.Stopwatch()
local_stopwatch = Tools.Stopwatch()

machine_learning = Learning.Xgboost(dataset)
models = machine_learning.evaluate(method=Learning.LeaveOneGroupOut,output=Learning.BT)
machine_learning.save(models, model_directory=model_directory)
print("Evaluate and save models time:", main_stopwatch.elapsed_time(), "seconds")

#Save some instance of your choice :)
for id, model in enumerate(models):
  local_stopwatch.elapsed_time(reset=True)
  instances = machine_learning.get_instances(
    indexes=Learning.Test, 
    n=10, 
    model=model, 
    backup_directory=model_directory,
    backup_id=id)
  print("Save instance time:", local_stopwatch.elapsed_time(reset=True), "seconds")

model_directory=model_directory+"/yeast_model/"

#Load models
machine_learning = Learning.Xgboost()
models = machine_learning.load(model_directory=model_directory+"/yeast_model/")
print("Load model time:", local_stopwatch.elapsed_time(reset=True), "seconds")

#Load instances
for id, model in enumerate(models):
  local_stopwatch.elapsed_time(reset=True)
  instances = machine_learning.get_instances(
    dataset=Tools.Options.dataset, 
    indexes=Tools.Options.model_directory, 
    model=model, 
    backup_id=id)
  print("Get instances time:", local_stopwatch.elapsed_time(reset=True), "seconds")
