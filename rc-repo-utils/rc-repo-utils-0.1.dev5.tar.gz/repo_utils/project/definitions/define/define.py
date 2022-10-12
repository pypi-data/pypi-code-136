import errno
import ntpath
import os
from os.path import join


def define(name: str):
    """Create definition files for definition at name
    name can be a path"""
    # Create folder
    path = os.path.abspath(os.path.expanduser(name))
    try:
        os.makedirs(path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise e
    name = ntpath.basename(name)

    # Create definition file
    if "/objects/" in path:
        def_contents = f"""
class {name}():
    \"\"\"  \"\"\"
    pass
"""
    else:
        def_contents = f"""
def {name}():
    \"\"\"

    Args:
        - 

    Returns:
        - 
    \"\"\"
    pass
"""
    def_filename = join(path, name + ".py")
    with open(def_filename, "w") as file:
        file.write(def_contents)

    # Create test file
    test_contents = f"""from {name} import {name}

def test_{name}():
    pass
"""
    test_filename = join(path, "test_{}.py".format(name))
    with open(test_filename, "w") as file:
        file.write(test_contents)


def snake_to_camel(text):
    """Convert from this_style to ThisStyle"""
    text = "".join(word.capitalize() or "_" for word in text.split("_"))
    return text
