import subprocess
import os
import sys
import json
from threading import Timer

from pyxai import Learning, Explainer, Tools

def execute(command, time):
  p = subprocess.Popen(command.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, preexec_fn=os.setsid)
  
  my_timer = Timer(time, lambda process: process.kill(), [p])
  
  results = None
  try:
    my_timer.start()
    for line in p.stdout:
      sys.stdout.write(line)
      if "solution" in line:
        results = line

  finally:
    my_timer.cancel()
  p.wait()
  p.terminate()
  if results is not None:
    results = results.split(":")[1]
    results = results.replace("[", "").replace("]","").split(",")
    results = [int(element) for element in results]
  return results


main_stopwatch = Tools.Stopwatch()
local_stopwatch = Tools.Stopwatch()
print("Time limit: ", Tools.Options.time_limit)

#Machine learning part
machine_learning = Learning.Xgboost()
models = machine_learning.evaluate(
  method=Learning.LoadModel, 
  output=Learning.BT, 
  model_directory=Tools.Options.model_directory)
print("Load model time:", main_stopwatch.elapsed_time(), "seconds")

#Explanation part
for id, model in enumerate(models):
  local_stopwatch.elapsed_time(reset=True)
  instances = machine_learning.get_instances(
    dataset=Tools.Options.dataset, 
    indexes=Tools.Options.model_directory, 
    model=model, 
    backup_id=id)
  print("Get instances time:", local_stopwatch.elapsed_time(reset=True), "seconds")

  explainer = Explainer.initialize(model)
  
  id_instance = 0
  for instance, prediction in instances:
    explainer.set_instance(instance)
    local_stopwatch.elapsed_time(reset=True)

    print("Instance " + str(id_instance) + " of the " + str(id) + " CV in progress ...")
    
    # xreason phase:
    program = os.getcwd() + "/../xreason/src/xreason.py"
    #program = os.getcwd() + "/xreason/src/xreason.py" (for the cluster)
    
    filename_instance = Tools.Options.dataset.split("/")[-1].split(".")[0]+"_"+str(id)+"_"+str(id_instance) + ".instance"
    data_instance = instance.tolist()
    data_instance = {"data_instance": data_instance}
    json_string = json.dumps(data_instance)
    with open(filename_instance, 'w') as outfile:
      json.dump(json_string, outfile)

    instance_str = os.getcwd() + "/" + filename_instance
    print("instance str:", instance_str)
    filename_model = Tools.Options.model_directory + "/" + Tools.Options.dataset.split("/")[-1].split(".")[0]+"."+str(id) + ".model"

    command = "python3.8 -u " + program + " -X abd -R lin -e mx -s g3 --instance-file " + instance_str + " -vvv --from-py-learning-explainer " + filename_model
    
    print("command:", command)
    sufficient = execute(command, int(Tools.Options.time_limit))
    # /!\ This sufficient is here in the form of features (not conditions) /!\   
    
    print("sufficient:", sufficient)
    
    print(explainer.reason_statistics(sufficient, reason_expressivity=Explainer.FEATURES))
    
    time = float(local_stopwatch.elapsed_time(reset=True))
    print("sufficient_time:", str(time), "seconds")
    print("total_time:", main_stopwatch.elapsed_time(), "seconds")
    
    id_instance += 1
    print()
    exit(0)
  

