
__module_name__ = "_layer.py"
__doc__ = """Layer module."""
__author__ = ", ".join(["Michael E. Vinyard"])
__email__ = ", ".join(["vinyard@g.harvard.edu"])


# -- import packages: --------------------------------------------------------------------
import torch


# -- import local dependencies: ----------------------------------------------------------
from ._abstract_base_models import BaseLayer


# -- Layer module: -----------------------------------------------------------------------
class Layer(BaseLayer):
    def __init__(
        self,
        name=None,
        nodes_m=50,
        nodes_n=1,
        activation_function=None,
        dropout=0,
        bias=True,
        layer_type=None
    ):
        super(Layer).__init__()
        self.__name__(name)
        if activation_function:
            self.__add_activation__(activation_function)
        self.__add_layer__(nodes_m, nodes_n, bias, layer_type)
        if dropout:
            self.__add_dropout__(dropout)
            
    def __name__(self, name):
        if name:
            setattr(self, "_name", "_{}".format(name))
        else:
            setattr(self, "_name", "")

    def __add_activation__(self, activation_function):
        setattr(
            self,
            "activation{}".format(self._name),
            activation_function,
        )

    def __add_layer__(self, nodes_m, nodes_n, bias, layer_type=""):
        if layer_type:
            layer_name = "{}{}".format(layer_type, self._name)
        else:
            layer_name = "{}".format(self._name)
        setattr(self, layer_name, torch.nn.Linear(nodes_m, nodes_n, bias=bias))

    def __add_dropout__(self, dropout):
        setattr(self, "dropout{}".format(self._name), torch.nn.Dropout(p=dropout))

    def __collect_attributes__(self):

        attributes = [attr for attr in self.__dir__() if not attr.startswith("_")]
        for attr in attributes:
            yield attr, getattr(self, attr),

    def __call__(self) -> dict:
        return dict(self.__collect_attributes__())