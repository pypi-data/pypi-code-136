"""
snapml_auto_quantization is a SnapML library for quantizing floating point model in an automatic manner, which means the users do not need to manually construct the quantization model, instead this is accomplished by the libary automatically. Features described in this documentation are classified by their level.

API for end users:

`snapml_auto_quantization.quant_simulator`


Quantized version of different layer types:

`snapml_auto_quantization.quant_adaptive_avg_pool`

`snapml_auto_quantization.quant_add`

`snapml_auto_quantization.quant_avgpool`

`snapml_auto_quantization.quant_base_module`

`snapml_auto_quantization.quant_concat`

`snapml_auto_quantization.quant_conv`

`snapml_auto_quantization.quant_deconv`

`snapml_auto_quantization.quant_flatten`

`snapml_auto_quantization.quant_leakyrelu`

`snapml_auto_quantization.quant_linear`

`snapml_auto_quantization.quant_maxpool`

`snapml_auto_quantization.quant_mean`

`snapml_auto_quantization.quant_mul`

`snapml_auto_quantization.quant_pad`

`snapml_auto_quantization.quant_prelu`

`snapml_auto_quantization.quant_relu`

`snapml_auto_quantization.quant_reshape`

`snapml_auto_quantization.quant_resize`

`snapml_auto_quantization.quant_sigmoid`

`snapml_auto_quantization.quant_softmax`

`snapml_auto_quantization.quant_sub`

`snapml_auto_quantization.quant_view`

Quantized layer factory:

`snapml_auto_quantization.quant_layer_factory`


Utilities functions for low-level quantization:

`snapml_auto_quantization.quant_utils`


API for brewing networks:

`snapml_auto_quantization.brew_networks`
"""
