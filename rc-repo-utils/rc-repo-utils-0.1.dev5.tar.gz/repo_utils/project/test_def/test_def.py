import sys
from os import remove
from os.path import exists, join

from repo_utils import find_definition, pytest_on_path


def test_def(def_name: str, test_func: str = None, namespace: str = None):
    """
    Given the name of a definition to test_def,
    run the chosen test_def module on it.

    Args:
        - def_name (str): Definition name at which to find the test module file (test_<def_name>.py).
        - test_func (str): Test only this particular test function within the test module.

    """
    def_dir = find_definition(def_name, namespace=namespace)
    # In order to specify function, the specific
    # test_def file must be specified, so it
    # will only search within the test_def file named after
    # the definition
    if def_dir:
        init_filepath = join(def_dir, "__init__.py")
        if exists(init_filepath):
            remove(init_filepath)
        return pytest_on_path(join(def_dir), test_func=test_func)
    else:
        print(f"No definition found named {def_name}", file=sys.stderr)
