"""
Functions to brew networks.
"""

from .quant_utils import *
from .quant_conv import *
from .quant_linear import *
from .quant_maxpool import *
from .quant_relu import *
from .quant_flatten import *
from .quant_add import *
from .quant_mean import *
from .quant_adaptive_avg_pool import *
from .quant_concat import *
from .quant_mul import *
from .quant_deconv import *
from .quant_avgpool import *
from .quant_reshape import *
from .quant_resize import *
from .quant_view import *
from .quant_sub import *
from .quant_sigmoid import *
from .quant_softmax import *
from .quant_leakyrelu import *
from .quant_prelu import *
from .quant_pad import *
from .quant_layer_factory import *

from torch.nn.utils.fusion import fuse_conv_bn_eval
import torch.fx as fx
import copy
import warnings

def _parent_name(target):
    """
    Splits a qualname into parent path and last atom.
    For example, `foo.bar.baz` -> (`foo.bar`, `baz`)

    Args:

        target: qualname to be split.

    Returns:

        parent path name and target name.

    """
    *parent, name = target.rsplit('.', 1)
    return parent[0] if parent else '', name


def replace_node_module(node, modules, new_module):
    """
    Replace the module of a node with a new module.

    Args:

        node: the node whose module to be replaced.

        modules: dictionary of all modules.

        new_module: the new module.

    """
    assert (isinstance(node.target, str))
    parent_name, name = _parent_name(node.target)
    modules[node.target] = new_module
    setattr(modules[parent_name], name, new_module)


def get_source_module(module, dotted_name):
    """
    Find the corresponding module given the name.

    Args:

        module: module hierachy.

        dotted_name: the name of target module.

    Returns:

        target module.
    """
    if '.' in dotted_name:
        module_name, _, remainder = dotted_name.partition('.')
        return get_source_module(module._modules[module_name], remainder)

    return getattr(module, dotted_name)


def convert_fmodel_to_qmodel(model, disable_quant):
    """
    Convert floating point model into the quantized version.

    Args:

        model: the floating point model to be quantized.

        disable_quant: A boolean variable. True means we disable quantization statistics collection; While False means we collect quantization statistics.

    Returns:

        The same model converted into quantized version.

    """
    # count for each non-module so that we can name them
    counts = dict()

    patterns_qmodules_dict_1 = QuantLayerFactory.patterns_qmodules_dict_1  # for non-modules
    patterns_qmodules_dict_2 = QuantLayerFactory.patterns_qmodules_dict_2  # for modules

    traced = fx.symbolic_trace(model)

    all_modules = dict(traced.named_modules())

    # go through all the nodes in the Graph
    visited = set()
    for n in traced.graph.nodes:
        # non-modules
        if n.target in visited:
                raise Exception("Found duplicate nodes in the graph, node name is '" + n.target + "'")
        visited.add(n.target)
        if n.op in ['call_function', 'call_method']:
            for name in patterns_qmodules_dict_1.keys():
                patterns = patterns_qmodules_dict_1[name][0]
                qmodule = patterns_qmodules_dict_1[name][1]
                # if the target matches one of the patterns
                if any(n.target == pattern for pattern in patterns):
                    # set the insert point, add the new node, and replace all
                    # uses of `n` with the new node
                    with traced.graph.inserting_after(n):
                        if name in counts:
                            counts[name] += 1
                        else:
                            counts[name] = 0
                        if name == 'qconcat':
                            traced.add_module(
                                f'quantized_{name}_{counts[name]}', qmodule(
                                    num_inputs=len(n.args[0]),
                                    disable_quant=disable_quant))
                        else:
                            traced.add_module(
                                f'quantized_{name}_{counts[name]}', qmodule(
                                    disable_quant=disable_quant))
                        new_node = traced.graph.call_module(
                            f'quantized_{name}_{counts[name]}', n.args, n.kwargs)
                        n.replace_all_uses_with(new_node)
                    # remove the old node from the graph
                    traced.graph.erase_node(n)
        # modules
        elif n.op in ['call_module', ]:
            for name in patterns_qmodules_dict_2.keys():
                patterns = patterns_qmodules_dict_2[name][0]
                qmodule = patterns_qmodules_dict_2[name][1]
                fmodule = copy.deepcopy(get_source_module(traced, n.target))
                # if the float module is an intance of any of the pattern
                # modules
                if any(isinstance(fmodule, pattern) for pattern in patterns):
                    # set the insert point, add the new node, and replace all
                    # uses of `n` with the new node
                    with traced.graph.inserting_after(n):
                        replace_node_module(
                            n, all_modules, qmodule(
                                fmodule, disable_quant=disable_quant))

    # don't forget to recompile!
    traced.recompile()

    return traced


def fuse_all_conv_bn(model):
    """
    Fuse batchnorm of floating point model into convolution or deconvolution, as in the patterns conv-bn or deconv-bn.

    Args:

         model: The floating point model whose batchnorm to be fused.

    Returns:

         The same model where all batchnorm are fused into convolution or deconvolution.
    """
    stack = []
    for name, module in model.named_children():
        if list(module.named_children()):
            fuse_all_conv_bn(module)

        if isinstance(module, nn.BatchNorm2d):
            if stack == []:
                warnings.warn(
                    'Only conv-batchnorm, or deconv-batchnorm can be fused together. There are batchnorms not in these patterns. Please consider remove/modify them.')
            elif isinstance(stack[-1][1], nn.Conv2d):
                setattr(model, stack[-1][0],
                        fuse_conv_bn_eval(stack[-1][1], module))
                setattr(model, name, nn.Identity())
            elif isinstance(stack[-1][1], nn.ConvTranspose2d):
                setattr(model,
                        stack[-1][0],
                        fuse_conv_bn_eval(stack[-1][1],
                                          module,
                                          transpose=True))
                setattr(model, name, nn.Identity())
            else:
                warnings.warn(
                    'Only conv-batchnorm, or deconv-batchnorm can be fused together. There are batchnorms not in these patterns. Please consider remove/modify them.')
        else:
            stack.append((name, module))
