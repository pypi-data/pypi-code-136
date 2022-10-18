import inspect
import warnings
import torch


class QuantLayerFactory:
    """
    Decorator for registering all quantized modules.
    """

    patterns_qmodules_dict_1 = {}  # for non-modules
    patterns_qmodules_dict_2 = {}  # for modules

    @classmethod
    def register(self, name, patterns):
        """
        Register function.
        Use case example: @QuantLayerFactory.register('qconv2d', (torch.nn.Conv2d,))

        Args:

            name: the name of the quantized module.

            patterns: the patterns to be matched.
        """
        def inner_wrapper(wrapped_qmodule):
            if name in self.patterns_qmodules_dict_1 or name in self.patterns_qmodules_dict_2:
                warnings.warn(
                    f'Quantized layer {name} already exists. Will replace it')
            non_module_patterns = []
            module_patterns = []
            for pattern in patterns:
                if inspect.isclass(pattern) and issubclass(
                        pattern, torch.nn.Module):
                    # a module
                    module_patterns.append(pattern)
                else:
                    # not a module
                    non_module_patterns.append(pattern)

            if non_module_patterns:
                self.patterns_qmodules_dict_1[name] = (
                    tuple(non_module_patterns), wrapped_qmodule)
            if module_patterns:
                self.patterns_qmodules_dict_2[name] = (
                    tuple(module_patterns), wrapped_qmodule)

            return wrapped_qmodule

        return inner_wrapper
