# coding=utf-8
# Copyright Studio Ousia and The HuggingFace Inc. team.
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
""" LUKE configuration"""

from ...configuration_utils import PretrainedConfig
from ...utils import logging


logger = logging.get_logger(__name__)

LUKE_PRETRAINED_CONFIG_ARCHIVE_MAP = {
    "studio-ousia/luke-base": "https://huggingface.co/studio-ousia/luke-base/resolve/main/config.json",
    "studio-ousia/luke-large": "https://huggingface.co/studio-ousia/luke-large/resolve/main/config.json",
}


class LukeConfig(PretrainedConfig):
    r"""
    This is the configuration class to store the configuration of a [`LukeModel`]. It is used to instantiate a LUKE
    model according to the specified arguments, defining the model architecture. Instantiating a configuration with the
    defaults will yield a similar configuration to that of the LUKE
    [studio-ousia/luke-base](https://huggingface.co/studio-ousia/luke-base) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.


    Args:
        vocab_size (`int`, *optional*, defaults to 30522):
            Vocabulary size of the LUKE model. Defines the number of different tokens that can be represented by the
            `inputs_ids` passed when calling [`LukeModel`].
        entity_vocab_size (`int`, *optional*, defaults to 500000):
            Entity vocabulary size of the LUKE model. Defines the number of different entities that can be represented
            by the `entity_ids` passed when calling [`LukeModel`].
        hidden_size (`int`, *optional*, defaults to 768):
            Dimensionality of the encoder layers and the pooler layer.
        entity_emb_size (`int`, *optional*, defaults to 256):
            The number of dimensions of the entity embedding.
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
            The vocabulary size of the `token_type_ids` passed when calling [`LukeModel`].
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-12):
            The epsilon used by the layer normalization layers.
        use_entity_aware_attention (`bool`, defaults to `True`):
            Whether or not the model should use the entity-aware self-attention mechanism proposed in [LUKE: Deep
            Contextualized Entity Representations with Entity-aware Self-attention (Yamada et
            al.)](https://arxiv.org/abs/2010.01057).
        classifier_dropout (`float`, *optional*):
            The dropout ratio for the classification head.

    Examples:

    ```python
    >>> from transformers import LukeConfig, LukeModel

    >>> # Initializing a LUKE configuration
    >>> configuration = LukeConfig()

    >>> # Initializing a model from the configuration
    >>> model = LukeModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```"""
    model_type = "luke"

    def __init__(
        self,
        vocab_size=50267,
        entity_vocab_size=500000,
        hidden_size=768,
        entity_emb_size=256,
        num_hidden_layers=12,
        num_attention_heads=12,
        intermediate_size=3072,
        hidden_act="gelu",
        hidden_dropout_prob=0.1,
        attention_probs_dropout_prob=0.1,
        max_position_embeddings=512,
        type_vocab_size=2,
        initializer_range=0.02,
        layer_norm_eps=1e-12,
        use_entity_aware_attention=True,
        classifier_dropout=None,
        pad_token_id=1,
        bos_token_id=0,
        eos_token_id=2,
        **kwargs
    ):
        """Constructs LukeConfig."""
        super().__init__(pad_token_id=pad_token_id, bos_token_id=bos_token_id, eos_token_id=eos_token_id, **kwargs)

        self.vocab_size = vocab_size
        self.entity_vocab_size = entity_vocab_size
        self.hidden_size = hidden_size
        self.entity_emb_size = entity_emb_size
        self.num_hidden_layers = num_hidden_layers
        self.num_attention_heads = num_attention_heads
        self.hidden_act = hidden_act
        self.intermediate_size = intermediate_size
        self.hidden_dropout_prob = hidden_dropout_prob
        self.attention_probs_dropout_prob = attention_probs_dropout_prob
        self.max_position_embeddings = max_position_embeddings
        self.type_vocab_size = type_vocab_size
        self.initializer_range = initializer_range
        self.layer_norm_eps = layer_norm_eps
        self.use_entity_aware_attention = use_entity_aware_attention
        self.classifier_dropout = classifier_dropout
