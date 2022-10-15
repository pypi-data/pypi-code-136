# type: ignore

from sys import path

import tomli
import tomli_w

path.insert(0, "./src/ty_command")

import ty

with open("README.md", "w") as f:
    f.write(ty.__doc__)

with open("pyproject.toml", "rb") as f:
    toml = tomli.load(f)

print(
    f'updating `pyprojet.toml` version from `{toml["project"]["version"]}` to `{ ty.__version__}`'
)
toml["project"]["version"] = ty.__version__

with open("pyproject.toml", "w") as f:
    f.write(tomli_w.dumps(toml))
