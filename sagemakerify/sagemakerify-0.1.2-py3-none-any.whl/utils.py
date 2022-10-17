import os
import ast
import json
import shutil
import astor
import pickle
import inspect
import hashlib
import sagemaker_utils
import pandas as pd
from importlib_resources import files, as_file
from sagemakerify import globals
from sagemaker import Session
from sagemaker import get_execution_role as sm_get_execution_role


class Cache:
    def __init__(self, path, file, clear=False) -> None:
        self.path = path
        self.file = os.path.join(path, file)
        self._data = {"images": {}}
        if not clear:
            self.load()
        else:
            self.save()

    def save(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path)

        with open(self.file, "w") as config_file:
            json.dump(self._data, config_file)
        return

    def load(self):
        if os.path.isfile(self.file):
            with open(self.file) as config_file:
                self._data = json.load(config_file)
                return True
        else:
            return False

    def get_image(self, name):
        return self._data["images"].get(name, {"uri": None, "hash": None})

    def set_image(self, name, uri, hash):
        self._data["images"][name] = {"uri": uri, "hash": hash}
        self.save()


class Defaults:
    def __init__(
        self,
        base_image="public.ecr.aws/docker/library/python:3.7-slim-buster",
        session=Session(),
        secret=None,
        codebuild_role=None,
        bucket=Session().default_bucket(),
        prefix="sagemakerify",
        project=None,
        role=None,
        instance_count=1,
        instance_type="ml.m5.2xlarge",
        volume_size_in_gb=5,
        max_runtime_in_seconds=60 * 60 * 5,
        source_code_location=".code",
        clear_cache=False,
        tags=None,
        enable_network_isolation=None,
        security_group_ids=None,
        subnets=None,
        encrypt_inter_container_traffic=None,
        use_spot_instances=None,
        max_wait=None,
        volume_kms_key=None,
        output_kms_key=None,
        timeout=300,
        memory_size=256,
    ):
        self.source_code_location = source_code_location
        self.base_image = base_image
        self.session = session
        self.secret = secret
        self.codebuild_role = codebuild_role
        self.bucket = bucket
        self.prefix = prefix
        self.project = project
        self.role = role
        self.instance_count = instance_count
        self.instance_type = instance_type
        self.volume_size_in_gb = volume_size_in_gb
        self.max_runtime_in_seconds = max_runtime_in_seconds
        self.clear_cache = clear_cache
        self.tags = tags
        self.volume_kms_key = volume_kms_key
        self.output_kms_key = output_kms_key
        self.enable_network_isolation = enable_network_isolation
        self.security_group_ids = security_group_ids
        self.subnets = subnets
        self.encrypt_inter_container_traffic = encrypt_inter_container_traffic
        self.use_spot_instances = use_spot_instances
        self.max_wait = max_wait
        self.timeout = timeout
        self.memory_size = memory_size

        globals.CACHE = Cache(
            os.path.join(os.path.expanduser("~"), ".sagemakerify"),
            "cache.json",
            self.clear_cache,
        )

    def get(self, attr, default):
        value = getattr(self, attr, default)
        return value if value != None else default


globals.DEFAULTS = Defaults()


def set_defaults(**kwargs):
    globals.DEFAULTS = Defaults(**kwargs)


def get_region_name():
    return globals.DEFAULTS.get("session", None).boto_region_name


def get_execution_role(role):
    try:
        if role is None:
            role = sm_get_execution_role()
        return role
    except:
        raise Exception("You have to specify an execution role")


def get_decorators(cls):
    target = cls
    decorators = {}

    def visit_FunctionDef(node):
        decorators[node.name] = []
        for n in node.decorator_list:
            name = ""
            if isinstance(n, ast.Call):
                name = n.func.attr if isinstance(n.func, ast.Attribute) else n.func.id
            else:
                name = n.attr if isinstance(n, ast.Attribute) else n.id

            decorators[node.name].append(name)

    node_iter = ast.NodeVisitor()
    node_iter.visit_FunctionDef = visit_FunctionDef
    node_iter.visit(ast.parse(inspect.getsource(target)))
    return decorators


def get_function_code(func):
    code = {}

    def visit_FunctionDef(node):
        node.decorator_list = []
        code[node.name] = astor.to_source(node)

    node_iter = ast.NodeVisitor()
    node_iter.visit_FunctionDef = visit_FunctionDef
    node_iter.visit(ast.parse(inspect.getsource(func)))

    return code


def get_function_outputs(fnc):
    outputs = [
        line.strip() for line in inspect.getsourcelines(fnc)[0] if " return " in line
    ]
    if len(outputs) > 0:
        outputs = outputs[0].replace("return ", "").split(",")
        outputs = [output.strip() for output in outputs]
    return outputs


def get_function_required_inputs(fnc):
    signature = inspect.signature(fnc)
    return [
        k
        for k, v in signature.parameters.items()
        if v.default is inspect.Parameter.empty
    ]


def get_default_args(func):
    signature = inspect.signature(func)
    return {
        k: v.default
        for k, v in signature.parameters.items()
        if v.default is not inspect.Parameter.empty
    }


def get_imports(Cls, num_spaces=0):
    imports = []
    spaces = " ".join(["" for i in range(num_spaces + 1)])

    for name, member in inspect.getmembers(Cls):
        code_line = ""
        if inspect.ismodule(member):
            module = inspect.getmodule(member).__name__.split(".")
            module_name = module[-1]
            module = ".".join(module[:-1])
            if len(module) > 0:
                code_line = f"from {module} import {module_name}"
            else:
                code_line = f"import {module_name}"

            if module_name != name:
                code_line += f" as {name}"

            imports.append(code_line)

        elif inspect.isclass(member):
            module = inspect.getmodule(member).__name__
            if module != "builtins":
                code_line = f"from {module} import {name}"
                imports.append(code_line)

        elif inspect.isfunction(member):
            module = inspect.getmodule(member).__name__
            if module != "__main__":
                code_line = f"from {module} import {name}"
                imports.append(code_line)

        elif inspect.isbuiltin(member):
            module = inspect.getmodule(member)
            if module is not None:
                code_line = f"from {module.__name__} import {name}"
                imports.append(code_line)

        if (
            inspect.isfunction(member)
            and object.__qualname__ + "." + member.__name__ == member.__qualname__
        ):
            print(inspect.getfile(member))

    return "\n".join(sorted([spaces + line for line in imports], key=len))


def get_class_code(Cls):
    methods = {
        name: member
        for name, member in inspect.getmembers(Cls)
        if inspect.isfunction(member)
    }

    if "model_fn" not in methods:
        raise Exception("model_fn method is required")

    if "input_fn" not in methods:
        raise Exception("input_fn methid is required")

    if "predict_fn" not in methods:
        raise Exception("predict_fn method is required")

    if "output_fn" not in methods:
        raise Exception("output_fn method is required")

    line = inspect.getsource(methods["model_fn"])
    num_spaces = len(line) - len(line.lstrip())

    code_lines = [f"class {Cls.__name__}:", get_imports(Cls, num_spaces), ""]

    for method in methods:
        code_lines.append(inspect.getsource(methods[method]))

    code = f"""

serving = {Cls.__name__}()

def model_fn(model_dir):
    return serving.model_fn(model_dir)

def input_fn(request_body, request_content_type):
    return serving.input_fn(request_body, request_content_type)

def predict_fn(input_data, model):
    return serving.predict_fn(input_data, model)

def output_fn(predictions, response_content_type):
    return serving.output_fn(predictions, response_content_type)
    """

    return "\n".join(code_lines) + code


def create_class_file(Cls):
    name = Cls.__name__.lower()
    code = get_class_code(Cls)
    class_file = f"{globals.DEFAULTS.source_code_location}/{name}.py"
    sagemaker_utils.make_dirs(class_file)
    with open(class_file, "w") as f:
        f.write(code)

    return name, class_file


def copy_serving_files():
    import sagemakerify.serving

    serving_directory = f"{globals.DEFAULTS.source_code_location}/serving"
    if os.path.exists(serving_directory):
        shutil.rmtree(serving_directory)

    with as_file(files(sagemakerify.serving)) as serving_path:
        shutil.copytree(serving_path, serving_directory)


def create_function_file(func, directory=None, name=None):
    function_name = func.__name__
    num_outputs = len(get_function_outputs(func))
    num_inputs = len(get_function_required_inputs(func))

    if directory == None:
        function_file = f"{globals.DEFAULTS.source_code_location}/{function_name if name == None else name}.py"
    else:
        function_file = f"{globals.DEFAULTS.source_code_location}/{directory}/{function_name if name == None else name}.py"

    sagemaker_utils.make_dirs(function_file)
    with open(function_file, "w") as f:
        f.write(get_function_code(func)[function_name])

    return function_name, function_file, num_inputs, num_outputs


def save_file(data, file):
    sagemaker_utils.make_dirs(file)
    if isinstance(data, pd.DataFrame):
        filename = f"{file}.parquet.gzip"
        data.to_parquet(filename, compression="gzip")
    else:
        filename = f"{file}.pkl"
        with open(filename, "wb") as f:
            pickle.dump(data, f)
    return filename


def dict_hash(dictionary):
    dhash = hashlib.md5()

    encoded = json.dumps(dictionary, sort_keys=True).encode()

    dhash.update(encoded)

    return dhash.hexdigest()


def is_builtin_class_instance(obj):
    return obj.__class__.__module__ == "builtins"
