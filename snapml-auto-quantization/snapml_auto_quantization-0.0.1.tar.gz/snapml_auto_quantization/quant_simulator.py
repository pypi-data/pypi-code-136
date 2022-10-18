"""
Simulate quantization in floating point.
"""

from . quant_utils import *
from . brew_networks import *
import copy


class QuantizationSimulator():
    def __init__(self, trained_float_model):
        """
        Initialize QuantizationSimulator with a trained floating point model.

        Args:

            trained_float_model: A trained model in floating point.
        """
        self.fmodel = copy.deepcopy(trained_float_model)

        # fuse bn to conv or deconv
        self.fmodel.eval()
        fuse_all_conv_bn(self.fmodel)

        # convert float model to quantization simulation model
        quant_sim_model = convert_fmodel_to_qmodel(
            copy.deepcopy(self.fmodel), disable_quant=False)
        quant_sim_model.eval()

        # load float model's weight into quantization simulation model
        quant_sim_model.load_state_dict(self.fmodel.state_dict(), strict=False)

        self.quant_sim_model = quant_sim_model

        # convert float model to quantized model
        quant_model = convert_fmodel_to_qmodel(
            copy.deepcopy(self.fmodel), disable_quant=True)
        quant_model.eval()
        self.quant_model = quant_model

    def post_training_quantization(self, inference_loop_function, config):
        """
        Apply post training quantization to the floating point model.

        Args:

            inference_loop_function: A functin which takes in a model and a config dictionary as input, and runs inference of the model on the dataloader specified in the config dictionary.

            config: A dictionary containing necessary components to run inference; and these components are specified by the user, for example, one can specify the dataloader like this config = {"dataloader": trainloader,}.

        Returns:

            A quantized model for export to onnx, and a quantization simulation model, after applying post training quantization.

        """
        set_measure(self.quant_sim_model, True)

        # calibration through dataset
        inference_loop_function(self.quant_sim_model, config)

        set_measure(self.quant_sim_model, False)

        # load quantization simulation model's weights into quantized model's
        # weight
        self.quant_model.load_state_dict(
            self.quant_sim_model.state_dict(), strict=False)

        return self.quant_model, self.quant_sim_model

    def export_quantized_model_to_onnx(
            self,
            dummy_input,
            input_names,
            output_names,
            save_onnx_name):
        """
        Export the quantized model into onnx format.

        Args:

            dummy_input: A dummy input tensor to the model.

            input_names: Names to assign to the input nodes of the graph, in order.

            output_names: Names to assign to the output nodes of the graph, in order.

            save_onnx_name: The onnx file name to save.

        Returns:

            None.

        """
        quant_model_cpu = copy.deepcopy(self.quant_model)
        quant_model_cpu.to(device='cpu')
        quant_model_cpu = quant_model_cpu.eval()
        quant_model_cpu(dummy_input.detach())

        torch.onnx.export(
            quant_model_cpu,
            dummy_input,
            save_onnx_name,
            verbose=False,
            input_names=input_names,
            output_names=output_names,
            enable_onnx_checker=False)
