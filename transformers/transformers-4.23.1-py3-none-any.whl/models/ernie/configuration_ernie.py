# coding=utf-8
# Copyright 2022 The Google AI Language Team Authors and The HuggingFace Inc. team.
# Copyright (c) 2018, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
""" ERNIE model configuration"""
from collections import OrderedDict
from typing import Mapping

from ...configuration_utils import PretrainedConfig
from ...onnx import OnnxConfig
from ...utils import logging


logger = logging.get_logger(__name__)

ERNIE_PRETRAINED_CONFIG_ARCHIVE_MAP = {
    "nghuyong/ernie-1.0-base-zh": "https://huggingface.co/nghuyong/ernie-1.0-base-zh/resolve/main/config.json",
    "nghuyong/ernie-2.0-base-en": "https://huggingface.co/nghuyong/ernie-2.0-base-en/resolve/main/config.json",
    "nghuyong/ernie-2.0-large-en": "https://huggingface.co/nghuyong/ernie-2.0-large-en/resolve/main/config.json",
    "nghuyong/ernie-3.0-base-zh": "https://huggingface.co/nghuyong/ernie-3.0-base-zh/resolve/main/config.json",
    "nghuyong/ernie-3.0-medium-zh": "https://huggingface.co/nghuyong/ernie-3.0-medium-zh/resolve/main/config.json",
    "nghuyong/ernie-3.0-mini-zh": "https://huggingface.co/nghuyong/ernie-3.0-mini-zh/resolve/main/config.json",
    "nghuyong/ernie-3.0-micro-zh": "https://huggingface.co/nghuyong/ernie-3.0-micro-zh/resolve/main/config.json",
    "nghuyong/ernie-3.0-nano-zh": "https://huggingface.co/nghuyong/ernie-3.0-nano-zh/resolve/main/config.json",
    "nghuyong/ernie-gram-zh": "https://huggingface.co/nghuyong/ernie-gram-zh/resolve/main/config.json",
    "nghuyong/ernie-health-zh": "https://huggingface.co/nghuyong/ernie-health-zh/resolve/main/config.json",
}


class ErnieConfig(PretrainedConfig):
    r"""
    This is the configuration class to store the configuration of a [`ErnieModel`] or a [`TFErnieModel`]. It is used to
    instantiate a ERNIE model according to the specified arguments, defining the model architecture. Instantiating a
    configuration with the defaults will yield a similar configuration to that of the ERNIE
    [nghuyong/ernie-3.0-base-zh](https://huggingface.co/nghuyong/ernie-3.0-base-zh) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.


    Args:
        vocab_size (`int`, *optional*, defaults to 30522):
            Vocabulary size of the ERNIE model. Defines the number of different tokens that can be represented by the
            `inputs_ids` passed when calling [`ErnieModel`] or [`TFErnieModel`].
        hidden_size (`int`, *optional*, defaults to 768):
            Dimensionality of the encoder layers and the pooler layer.
        num_hidden_layers (`int`, *optional*, defaults to 12):
            Number of hidden layers in the Transformer encoder.
        num_attention_heads (`int`, *optional*, defaults to 12):
            Number of attention heads for each attention layer in the Transformer encoder.
        intermediate_size (`int`, *optional*, defaults to 3072):
            Dimensionality of the "intermediate" (often named feed-forward) layer in the Transformer encoder.
        hidden_act (`str` or `Callable`, *optional*, defaults to `"gelu"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"silu"` and `"gelu_new"` are supported.
        hidden_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
        attention_probs_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout ratio for the attention probabilities.
        max_position_embeddings (`int`, *optional*, defaults to 512):
            The maximum sequence length that this model might ever be used with. Typically set this to something large
            just in case (e.g., 512 or 1024 or 2048).
        type_vocab_size (`int`, *optional*, defaults to 2):
            The vocabulary size of the `token_type_ids` passed when calling [`ErnieModel`] or [`TFErnieModel`].
        task_type_vocab_size (`int`, *optional*, defaults to 3):
            The vocabulary size of the `task_type_ids` for ERNIE2.0/ERNIE3.0 model
        use_task_id (`bool`, *optional*, defaults to `False`):
            Whether or not the model support `task_type_ids`
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-12):
            The epsilon used by the layer normalization layers.
        position_embedding_type (`str`, *optional*, defaults to `"absolute"`):
            Type of position embedding. Choose one of `"absolute"`, `"relative_key"`, `"relative_key_query"`. For
            positional embeddings use `"absolute"`. For more information on `"relative_key"`, please refer to
            [Self-Attention with Relative Position Representations (Shaw et al.)](https://arxiv.org/abs/1803.02155).
            For more information on `"relative_key_query"`, please refer to *Method 4* in [Improve Transformer Models
            with Better Relative Position Embeddings (Huang et al.)](https://arxiv.org/abs/2009.13658).
        use_cache (`bool`, *optional*, defaults to `True`):
            Whether or not the model should return the last key/values attentions (not used by all models). Only
            relevant if `config.is_decoder=True`.
        classifier_dropout (`float`, *optional*):
            The dropout ratio for the classification head.

    Examples:

    ```python
    >>> from transformers import ErnieModel, ErnieConfig

    >>> # Initializing a ERNIE nghuyong/ernie-3.0-base-zh style configuration
    >>> configuration = ErnieConfig()

    >>> # Initializing a model from the nghuyong/ernie-3.0-base-zh style configuration
    >>> model = ErnieModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```"""
    model_type = "ernie"

    def __init__(
        self,
        vocab_size=30522,
        hidden_size=768,
        num_hidden_layers=12,
        num_attention_heads=12,
        intermediate_size=3072,
        hidden_act="gelu",
        hidden_dropout_prob=0.1,
        attention_probs_dropout_prob=0.1,
        max_position_embeddings=512,
        type_vocab_size=2,
        task_type_vocab_size=3,
        use_task_id=False,
        initializer_range=0.02,
        layer_norm_eps=1e-12,
        pad_token_id=0,
        position_embedding_type="absolute",
        use_cache=True,
        classifier_dropout=None,
        **kwargs
    ):
        super().__init__(pad_token_id=pad_token_id, **kwargs)

        self.vocab_size = vocab_size
        self.hidden_size = hidden_size
        self.num_hidden_layers = num_hidden_layers
        self.num_attention_heads = num_attention_heads
        self.hidden_act = hidden_act
        self.intermediate_size = intermediate_size
        self.hidden_dropout_prob = hidden_dropout_prob
        self.attention_probs_dropout_prob = attention_probs_dropout_prob
        self.max_position_embeddings = max_position_embeddings
        self.type_vocab_size = type_vocab_size
        self.task_type_vocab_size = task_type_vocab_size
        self.use_task_id = use_task_id
        self.initializer_range = initializer_range
        self.layer_norm_eps = layer_norm_eps
        self.position_embedding_type = position_embedding_type
        self.use_cache = use_cache
        self.classifier_dropout = classifier_dropout


class ErnieOnnxConfig(OnnxConfig):
    @property
    def inputs(self) -> Mapping[str, Mapping[int, str]]:
        if self.task == "multiple-choice":
            dynamic_axis = {0: "batch", 1: "choice", 2: "sequence"}
        else:
            dynamic_axis = {0: "batch", 1: "sequence"}
        return OrderedDict(
            [
                ("input_ids", dynamic_axis),
                ("attention_mask", dynamic_axis),
                ("token_type_ids", dynamic_axis),
                ("task_type_ids", dynamic_axis),
            ]
        )
