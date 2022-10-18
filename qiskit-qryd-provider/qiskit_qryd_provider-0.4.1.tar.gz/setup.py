# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['qiskit_qryd_provider']

package_data = \
{'': ['*']}

install_requires = \
['qiskit-terra>=0.20.2,<0.21.0', 'requests>=2.27.1,<3.0.0']

setup_kwargs = {
    'name': 'qiskit-qryd-provider',
    'version': '0.4.1',
    'description': 'Qiskit provider for accessing the emulator and future Rydberg quantum computer of the QRydDemo consortium',
    'long_description': '# Qiskit QRyd Provider\n\n![Supported Python versions](https://img.shields.io/pypi/pyversions/qiskit_qryd_provider.svg?color=blue)\n[![Package version on PyPI](https://img.shields.io/pypi/v/qiskit_qryd_provider.svg?color=blue)](https://pypi.org/project/qiskit_qryd_provider/)\n[![Documentation](https://img.shields.io/badge/docs-Sphinx-blue.svg)](https://thequantumlaend.de/docs/)\n[![License](https://img.shields.io/pypi/l/qiskit_qryd_provider.svg?color=green)](https://www.apache.org/licenses/LICENSE-2.0)\n\nThis Python library contains a provider for the [Qiskit](https://qiskit.org) quantum computing framework. The provider allows for accessing the GPU-based emulator and the future Rydberg quantum computer of the [QRydDemo](https://thequantumlaend.de/qryddemo/) consortium.\n\nInteractive tutorials can be found on QRydDemo\'s [Jupyter server](https://thequantumlaend.de/frontend).\n\n## Installation\n\nThe provider can be installed via [pip](https://pip.pypa.io/) from\n[PyPI](https://pypi.org/project/qiskit_qryd_provider/):\n\n```bash\npip install qiskit-qryd-provider\n```\n\n## Basic Usage\n\nTo use the provider, a QRydDemo API token is required. The token can be obtained via our [online registration form](https://thequantumlaend.de/frontend/signup_form.php). You can use the token to initialize the provider:\n\n```python\nfrom qiskit_qryd_provider import QRydProvider\n\nprovider = QRydProvider("MY_TOKEN")\n```\n\nAfterwards, you can choose a backend. Different backends are available that are capable of running ideal simulations of quantum circuits. An inclusion of noise models is planned for the future. You can either choose a backend emulating 30 qubits arranged in a 5x6 square lattice with nearest-neighbor connectivity\n\n```python\nbackend = provider.get_backend("qryd_emu_localcomp_square")\n```\n\nor a backend emulating 30 qubits arranged in a triangle lattice with nearest-neighbor connectivity\n\n```python\nbackend = provider.get_backend("qryd_emu_localcomp_triangle")\n```\n\nIf you use these backends, Qiskit automatically transpiles arbitrary quantum circuits to comply with the native gate set and connectivity of the Rydberg platform. The backends are also available as variants where the compilation happens on our servers (`"qryd_emu_cloudcomp_square"` and `"qryd_emu_cloudcomp_triangle"`), using a decomposer developed by [HQS Quantum Simulations](https://quantumsimulations.de/).\n\nAfter selecting a backend, you can run a circuit on the backend:\n\n```python\nfrom qiskit import QuantumCircuit, execute\n\nqc = QuantumCircuit(2, 2)\nqc.h(0)\nqc.cx(0, 1)\nqc.measure([0, 1], [0, 1])\njob = execute(qc, backend, shots=200, optimization_level=3)\nprint(job.result().get_counts())\n```\n\n## Expert Options\n\nThe provider adds the phase-shifted controlled-Z gate to Qiskit ([PCZGate](https://thequantumlaend.de/docs/gates.html)). This gate equals the controlled-Z gate up to single-qubit phase gates. It can be realized by the Rydberg platform in multiple ways [[1](https://doi.org/10.1103/PhysRevLett.123.170503), [2](https://doi.org/10.1103/PhysRevResearch.4.033019), [3](https://doi.org/10.22331/q-2022-05-13-712)]. The value of the phase shift can be modified before using the backend via:\n\n```python\nfrom qiskit_qryd_provider import PCZGate\n\nPCZGate.set_theta(1.234)\n```\n\n## License\n\nThe Qiskit QRyd Provider is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).\n',
    'author': 'Sebastian Weber',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
