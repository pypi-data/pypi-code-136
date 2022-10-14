# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['postprocess_sdist_make_rust_ext_opt']
install_requires = \
['redbaron>=0.9.2,<0.10.0', 'typer>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['postprocess-sdist-make-rust-ext-opt = '
                     'postprocess_sdist_make_rust_ext_opt:app']}

setup_kwargs = {
    'name': 'postprocess-sdist-make-rust-ext-opt',
    'version': '0.1.2',
    'description': 'Post-process sdists to make Rust extensions optional',
    'long_description': '# postprocess-sdist-make-rust-ext-opt\n\n[![CI badge](https://github.com/smheidrich/postprocess-sdist-make-rust-ext-opt/actions/workflows/test-build-release.yml/badge.svg)](https://github.com/smheidrich/postprocess-sdist-make-rust-ext-opt/actions/workflows/test-build-release.yml)\n[![PyPI package and version badge](https://img.shields.io/pypi/v/postprocess-sdist-make-rust-ext-opt)](https://pypi.org/project/postprocess-sdist-make-rust-ext-opt/)\n[![Supported Python versions badge](https://img.shields.io/pypi/pyversions/postprocess-sdist-make-rust-ext-opt)](https://pypi.org/project/postprocess-sdist-make-rust-ext-opt/)\n\nThis is a small tool to "post-process" Python source distributions ("sdists")\ncontaining `setuptools-rust`-based Rust extensions so that these extensions\nare marked as "optional" (cf. `optional` parameter in the\n[`setuptools-rust` API docs](https://setuptools-rust.readthedocs.io/en/latest/reference.html#setuptools_rust.RustExtension)).\n\n## What? Why?\n\n**What does it mean for an extension to be optional?**\n\nAn extension (Rust or otherwise) being optional means that if the build fails\nwhen installing the package, the installation of the remainder of the package\nwill proceed anyway and be considered successful. The package can then deal\nwith the extension\'s absence at runtime, e.g. by providing pure-Python\nfallbacks for its functionality.\n\n**Why set it as optional in a postprocessing step and not from the start?**\n\nBecause you\'ll probably want to build binary packages (wheels) from the project\nas well, but if your extension is marked as optional, any errors during their\nbuild will be ignored. So you don\'t generally want to have it set as optional\nwhen building wheels. It only really makes sense to have it set for the sdist,\nnothing else.\n\n**Why not do it the other way round?**\n\nAnother option would be to set the extension as optional from the start but\nchange it to non-optional before the wheel build. But the issue with that is\nthat if you\'re using tools like `setuptools-scm` that automatically determine\nyour package\'s version from its state as determined by a version control system\n(VCS) like Git, changing anything about the code will cause the version to be\nconsidered "dirty", which will be represented in the version string. A way to\nwork around this would be to manipulate the VCS history in this case, but that\nis even more of a hack than the postprocessing.\n\n**Why not change it prior to building the sdist?**\n\nThe same reason as above (dirty repo when building => modified\nautomatically-determined version).\n\n## Installation\n\n```\npip install postprocess-sdist-make-rust-ext-opt\n```\n\n## Usage\n\n```bash\n$ postprocess-sdist-make-rust-ext-opt --help\nUsage: postprocess-sdist-make-rust-ext-opt [OPTIONS] [SDIST_PATH]\n\nArguments:\n  [SDIST_PATH]  [default: path of the sdist .tar.gz archive to post-process]\n\nOptions:\n  --install-completion [bash|zsh|fish|powershell|pwsh]\n                                  Install completion for the specified shell.\n  --show-completion [bash|zsh|fish|powershell|pwsh]\n                                  Show completion for the specified shell, to\n                                  copy it or customize the installation.\n  --help                          Show this message and exit.\n```\n\nThe processed sdist will be written to a folder named `postprocessed` in the\nsame directory as the input sdist. Its filename will be the same as that of the\ninput sdist.\n\n## Caveats\n\nThe `RustExtension` calls for which the `optional` argument should be set to\n`True` *must* be placed directly inside the list that is assigned to the\n`rust_extensions` parameter of the top-level `setup()` call like so:\n\n```python3\nfrom setuptools import setup\n\nsetup(\n    ...\n    rust_extensions=[\n        RustExtension(...),\n    ]\n    ...\n)\n```\n\nAnything more indirect than that, e.g. assigning a `RustExtension` instance to\na variable and then placing that inside the `rust_extensions` list, will cause\nthe tool to exit with an error.\n\nThis is because the transformation is implemented at the syntax tree level and\nno static analysis is performed to trace arguments back to their origins.\n\n## Acknowledgements\n\nThe transformation is performed using\n[RedBaron](https://pypi.org/project/redbaron/)\'s full syntax tree (FST)\nrepresentation of the sdist\'s `setup.py`.\n',
    'author': 'smheidrich',
    'author_email': 'smheidrich@weltenfunktion.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
