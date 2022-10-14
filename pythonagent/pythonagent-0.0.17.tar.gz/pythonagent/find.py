import os
import ast
import json

import sys
py_ver = sys.version_info[0]

local = False

def find(path):
    modules = []
    default_path = []
    for root, dirs, files in os.walk(path):
        for file in files:
            # print(file)
            if file.endswith(".py"):
                default_path.append(os.path.join(root, file))
                file = file[:-3]  # Remove .py extension
                modules.append(file)

    # print("modules", modules)
    # print("\n\n")
    # print("default_path", default_path)
    # print("\n\n")

    path_module_dict = dict(zip(default_path, modules))

    data = {
        "modules": [
            {
                "moduleName": path_module_dict[filename],
                "moduleLevelMethod": [
                    {
                        "name": f_name.name,
                        "signature": [a.arg if py_ver == 3 else a.id for a in f_name.args.args]
                        # "signature": [[a.arg for a in f_name.args.args],[f_name.returns]]

                    }
                    for f_name in [n for n in ast.parse(open(filename).read()).body if isinstance(n, ast.FunctionDef)]
                ],
                "classes": [
                    {
                        "className": cname.name,
                        "classLevelMethods": [
                            {
                                "name": clm_name.name,
                                "signature": [a.arg if py_ver == 3 else a.id for a in clm_name.args.args]
                                # "signature": [[a.arg for a in clm_name.args.args], [clm_name.returns]]

                            }
                            for clm_name in [n for n in cname.body if isinstance(n, ast.FunctionDef)]
                        ]
                    }
                    for cname in [n for n in ast.parse(open(filename).read()).body if isinstance(n, ast.ClassDef)]
                ]
            }
            for filename in default_path
        ]
    }

    json_object = json.dumps(data, indent=2)
    # print("\n\n\n\n")
    # print(json_object)
    # return str(json_object)

    with open(os.environ.get('ND_HOME') + "/python/CavAgent/instrumentationprofile.json", "w") as outfile:
        outfile.write(json_object)
        #print(outfile)

if local:
    path = "/home/cavisson/shop/my-shop/pythonagent/"
    find(path)
