
__module_name__ = "__init__.py"
__doc__ = """
          __init__.py module for the base modules and core supporting functions
          within the core of the API.
          """
__author__ = ", ".join(["Michael E. Vinyard"])
__email__ = ", ".join(["vinyard@g.harvard.edu",])
__version__ = "0.0.4rc"


# -- import module groups: ---------------------------------------------------------------
from ._abstract_base_models import BaseLayer, BaseTorchDict, BaseNeuralNet
from ._base_torch_neural_net import TorchDict, TorchNeuralNet
from ._layer import Layer
from ._supporting_functions import as_list, io_dim, parse_kwargs
