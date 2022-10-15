
__module_name__ = "_torch_net.py"
__doc__ = """Module to define dictionary organizing torch Sequential components."""
__author__ = ", ".join(["Michael E. Vinyard"])
__email__ = ", ".join(["vinyard@g.harvard.edu"])


# -- import packages: --------------------------------------------------------------------
import torch


# -- import local dependencies: ----------------------------------------------------------
from . import _base as base


# -- Main module class - user-facing API object: -----------------------------------------
class TorchNet(object):
    """Object-oriented user-facing API for TorchNet"""

    def __new__(
        obj_class,
        in_dim,
        out_dim,
        hidden={1: [200, 200]},
        activation_function=torch.nn.LeakyReLU(negative_slope=0.01),
        dropout=0,
        input_bias=True,
        output_bias=True,
    ):
        """
        Compose a torch neural network.

        Parameters:
        -----------
        in_dim
            neural network input dimension. dimensionality of data passed to neural network.
            default: 50
            type: int

        out_dim
            neural network out dimension
            default: 50
            type: int

        hidden
            dictionary describing the hidden layer architecture in addition to the first/input hidden layer.
            Connecting node shapes are automatically adjusted from hidden_layer_0 (input) to the second layer
            as well as the final hidden layer to the output dimension.
            default: {1:[500,500], 2:[500,500]}
            type: dict

        activation_function
            default: torch.nn.Tanh()
            type: torch.nn.modules.activation

        dropout
            probability of a dropout for the nodes in a given layer.
            default: 0
            type: float

        input_bias
            boolean indicator of bias for input layer.
            default: True
            type: bool

        output_bias
            boolean indicator of bias for output layer.
            default: True
            type: bool
        """
        return base.TorchNeuralNet(
            in_dim,
            out_dim,
            hidden,
            activation_function,
            dropout,
            input_bias,
            output_bias,
        )()