from time import time
from pyxai import Learning, Explainer, Tools

# To use with the minist dataset for example
# (classification between 4 and 9 or between 3 and 8)
# available here:
# http://www.cril.univ-artois.fr/expekctation/datasets/mnist38.csv
# http://www.cril.univ-artois.fr/expekctation/datasets/mnist49.csv


# the location of the dataset
path = "."
dataset = "mnist49.csv"



#Machine learning part
machine_learning = Learning.Scikitlearn(f"{path}/{dataset}")
model = machine_learning.evaluate(method=Learning.HOLD_OUT, output=Learning.RF)
instance, prediction = machine_learning.get_instances(model, n=1, correct=True)

#Explanation part
explainer = Explainer.initialize(model, instance)
direct = explainer.direct_reason()
print("len direct:", len(direct))

majoritary_reason = explainer.majoritary_reason(n=1) # take 100 in order to have different reasons
print("len majoritary_reason:", len(majoritary_reason))
# It is too time consuming to check it is majoritary, limit to implicant
assert explainer.is_implicant(majoritary_reason), "This is have to be a sufficient reason !"

#minimal_majoritary = explainer
minimal_reason = explainer.minimal_majoritary_reason(time_limit=5)
assert explainer.is_implicant(minimal_reason), "This is have to be an implicant"
if explainer.elapsed_time == Explainer.TIMEOUT: print("This is an approximation")
print("len minimal majoritary reason:", len(minimal_reason))


#Heatmap part
heatmap = Tools.Vizualisation(28, 28, instance)

heatmap.new_image("Instance").set_instance(instance)
heatmap.new_image("direct").add_reason(explainer.to_features(direct, details=True)).set_background_instance(instance)
heatmap.new_image("Majoritary").add_reason(explainer.to_features(majoritary_reason, details=True)).set_background_instance(instance)
heatmap.new_image("minimal").add_reason(explainer.to_features(minimal_reason, details=True)).set_background_instance(instance)

heatmap.display()