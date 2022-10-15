import sys

ENGINE = sys.argv[1]
TOML = f"""\
[tool.ty]
type_checker = "{ENGINE}"
"""
with open("pyproject.toml", "w") as f:
    f.write(TOML)
