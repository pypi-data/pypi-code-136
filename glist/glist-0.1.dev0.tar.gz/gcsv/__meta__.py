# `name` is the name of the package as used for `pip install package`
name = "glist"
# `path` is the name of the package for `import package`
path = name.lower().replace("-", "_").replace(" ", "_")
# Your version number should follow https://python.org/dev/peps/pep-0440 and
# https://semver.org
version = "0.1.dev0"
author = "Joshua Mathias"
author_email = "joshuaamathias@gmail.com"
description = "Read and write from Google Sheets as if it were a csv."  # One-liner
url = "https://github.com/JoshuaMathias/glist"  # your project homepage
license = "CCO-1.0"  # See https://choosealicense.com