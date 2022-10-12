from repo_utils import def_from_dir, find_definition


def import_definition(name: str, namespace: str = None):
    """Import a definition based on its name without its path
    Returns the imported function or object, not the module
    namespace should be a directory or path from <repo_root>/src
    If the module name is not found, return None"""
    def_dir = find_definition(name, namespace=namespace)
    if def_dir:
        definition = def_from_dir(def_dir)
        if definition is None:
            print(f'Definition {def_dir} not found. Does the Python filename have the same name as the folder name?')
        return definition
    else:
        print(f'Definition {name} not found.')