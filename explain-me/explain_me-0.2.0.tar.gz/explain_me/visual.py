import importlib
import pkgutil
import inspect


from .class_inspect import ClassDiagram

def get_classmodules(member):
    
    return inspect.getmembers(member, lambda mem: inspect.isclass(mem))
    

def get_all_submodule(package, recursive=True):
    """ Import all submodules of a module, recursively, including subpackages

    :param package: package (name or actual module)
    :type package: str | module
    :rtype: dict[str, types.ModuleType]
    """
    if isinstance(package, str):
        package = importlib.import_module(package)
        
    results = {}
    
    for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
        full_name = package.__name__ + '.' + name
        
        results[full_name] = importlib.import_module(full_name)
        
        # print(get_classmodules(results[full_name]), results[full_name], full_name)
        
        if recursive and is_pkg:
            results.update(get_all_submodule(full_name))
    
    return results



def visualize_package(package):
    list_cls = []
    
    for key, item in get_all_submodule(package).items():
        
        
        for key, classmodule in get_classmodules(item):
            if classmodule in list_cls:
                continue
            
            list_cls.append(classmodule)
                
            func = ClassDiagram(classmodule)
            # try:
            yield func()
            # except Exception as e:
            #     # traceback.print_exc()
            #     pass


