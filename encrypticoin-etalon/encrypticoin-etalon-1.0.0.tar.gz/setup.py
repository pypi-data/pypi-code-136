import os
import shutil
from collections import defaultdict

from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))
VERSION = "1.0.0"

with open(os.path.join(HERE, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

requirements = defaultdict(list)
for name in os.listdir(os.path.join(HERE, "requirements")):
    if name not in ("base.in",):
        continue
    reqs = requirements[name.rpartition(".")[0]]
    with open(os.path.join(HERE, "requirements", name)) as f:
        for line in f:
            line = line.strip()
            if line.startswith("#") or line.startswith("-r"):
                continue
            reqs.append(line)
install_requirements = requirements.pop("base")


def _package_data_files(pkg: str):
    root = os.path.join(HERE, pkg)
    for parent, _, files in os.walk(root):
        for file in files:
            if file.endswith(".py") or file.endswith(".pyc"):
                continue
            yield os.path.relpath(os.path.join(parent, file), root)


package_data = {
    "encrypticoin_etalon": sorted(_package_data_files("encrypticoin_etalon")),
}
if package_data != {
    "encrypticoin_etalon": [
        "contract/BEP20EtalonToken.sol",
        "contract/BEP20EtalonToken.sol.abi",
        "contract/BEP20EtalonToken.sol.bin",
        "contract/BEP20EtalonToken.sol.scv",
        "contract/BEP20EtalonToken.sol.sha256",
        "contract/IBEP20.sol",
        "contract/README.txt",
        "contract/openzeppelin-contracts-4.7.3-Context.sol",
        "contract/openzeppelin-contracts-4.7.3-ERC20.sol",
        "contract/openzeppelin-contracts-4.7.3-IERC20.sol",
        "contract/openzeppelin-contracts-4.7.3-IERC20Metadata.sol",
        "contract/openzeppelin-contracts-4.7.3-Ownable.sol",
    ]
}:
    raise Exception(f"Package data has changed\n{str(package_data)}")


# Manually cleaning before build is required.
for p in [os.path.join(HERE, "build"), os.path.join(HERE, "dist"), os.path.join(HERE, "encrypticoin_etalon.egg-info")]:
    if os.path.exists(p):
        shutil.rmtree(p)

setup(
    name="encrypticoin-etalon",
    version=VERSION,
    description="Etalon token implementation by Encrypticoin UAB",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/encrypticoin-uab/encrypticoin-etalon",
    author="Nándor Mátravölgyi",
    author_email="dev@etalon.cash",
    license="Apache 2.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
    ],
    packages=find_packages(where=HERE, include=["encrypticoin_etalon*"]),
    package_data=package_data,
    install_requires=install_requirements,
    # entry_points={"console_scripts": console_scripts},
    extras_require=dict(requirements),
    python_requires=">=3.8",
)
