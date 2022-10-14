import sys
import os
import ast
import json

#path ="C:/Users/garima.singh/PycharmProjects/django_redis_demo"
path ="/home/cavisson/shop/my-shop/pythonagent_garima"

modules = []
default_path = []

for root, dirs, files  in os.walk(path):
    for file in files:
        if(file.endswith(".py")):
            modules.append(file)
            default_path.append(os.path.join(root,file))
           
print("modules",modules)
print("default_path",default_path)


data = {
  "modules": [
    {
      "moduleName": filename,
      "moduleLevelMethod": [
      {
        "name":fname.name ,
        "signature":"NA"
      }
      for fname in [n for n in ast.parse(open(filename).read()).body if isinstance(n, ast.FunctionDef)]
      ],
      "classes": [
        {
          "className": cname.name,
          "classLevelMethods": [
      {
        "name":clmname.name,
        "signature":"NA"
     
      } 
        for clmname in [n for n in cname.body if isinstance(n, ast.FunctionDef)]      
      ]
        }
        for cname in [n for n in ast.parse(open(filename).read()).body if isinstance(n, ast.ClassDef)]
      ]
    }
    for filename in default_path
   ]
   }

json_object = json.dumps(data, indent = 2) 
with open("sample_json.json", "w") as outfile: 
    outfile.write(json_object)
