import abc
from typing import Any, Dict, List, Optional, Tuple, TypeVar, Union

ModelStubType = TypeVar('ModelStubType', bound='_ModelStub')


class _ModelStub(metaclass=abc.ABCMeta):
    name: str
    descriptor: str
    description: str
    task: str
    architecture: str
    builder: str
    embedding_layer: Optional[str]
    input_names: List[str]
    input_shapes: List[Tuple[Union[int, str], ...]]
    input_dtypes: List[str]
    output_name: str
    output_shape: Tuple[Union[int, str], ...]
    dynamic_axes: Dict[str, Dict[int, str]]
    preprocess_types: Dict[str, str]
    collate_types: Dict[str, str]
    preprocess_options: Dict[str, Dict[str, Any]] = {}
    collate_options: Dict[str, Dict[str, Any]] = {}
    options: Dict[str, Any] = {}

    def __init__(
        self,
        preprocess_options: Optional[Dict[str, Dict[str, Any]]] = None,
        collate_options: Optional[Dict[str, Dict[str, Any]]] = None,
        **options: Any
    ) -> None:
        self.options = options
        if preprocess_options:
            self.preprocess_options.update(preprocess_options)
        if collate_options:
            self.collate_options.update(collate_options)

    @property
    @abc.abstractmethod
    def name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def descriptor(self) -> str:
        ...


class _CNNStub(_ModelStub, metaclass=abc.ABCMeta):
    """CNN model stub."""

    task = 'image-to-image'
    architecture = 'cnn'
    builder = 'CNNBuilder'
    input_names = ['image']
    input_dtypes = ['float32']
    output_name = 'embedding'
    dynamic_axes = {'image': {0: 'batch-size'}, 'embedding': {0: 'batch-size'}}
    preprocess_types = {'image': 'VisionPreprocess'}
    collate_types = {'image': 'DefaultCollate'}
    preprocess_options = {'image': {}}
    collate_options = {'image': {}}

    def __init__(
        self,
        preprocess_options: Optional[Dict[str, Dict[str, Any]]] = None,
        collate_options: Optional[Dict[str, Dict[str, Any]]] = None,
    ):
        super(_CNNStub, self).__init__(
            preprocess_options=preprocess_options, collate_options=collate_options
        )
        self.input_shapes = [
            (
                'batch-size',
                3,
                self.preprocess_options['image'].get('height', 224),
                self.preprocess_options['image'].get('width', 224),
            ),
        ]


class _TextTransformerStub(_ModelStub, metaclass=abc.ABCMeta):
    """Text transformer model stub."""

    task = 'text-to-text'
    architecture = 'transformer'
    builder = 'TextTransformerBuilder'
    input_names = ['input_ids', 'attention_mask']
    input_dtypes = ['int32', 'int32']
    input_shapes = [
        ('batch-size', 'sequence-length'),
        ('batch-size', 'sequence-length'),
    ]
    output_name = 'embedding'
    dynamic_axes = {
        'input_ids': {0: 'batch-size', 1: 'sequence-length'},
        'attention_mask': {0: 'batch-size', 1: 'sequence-length'},
        'embedding': {0: 'batch-size'},
    }
    preprocess_types = {'text': 'TextPreprocess'}
    collate_types = {'text': 'TransformersCollate'}
    preprocess_options = {'text': {}}
    collate_options = {'text': {}}

    def __init__(
        self,
        pooling: str = 'mean',
        preprocess_options: Optional[Dict[str, Dict[str, Any]]] = None,
        collate_options: Optional[Dict[str, Dict[str, Any]]] = None,
    ):
        self.collate_options = {
            'text': {'name': self.descriptor, 'truncation': True, 'padding': True}
        }
        super(_TextTransformerStub, self).__init__(
            preprocess_options=preprocess_options,
            collate_options=collate_options,
            pooling=pooling,
        )


class _VisionTransformerStub(_ModelStub, metaclass=abc.ABCMeta):
    """Vision transformer model stub."""

    task = 'image-to-image'
    architecture = 'transformer'
    builder = 'VisionTransformerBuilder'
    input_names = ['pixel_values']
    input_dtypes = ['float32']
    output_name = 'embedding'
    dynamic_axes = {
        'pixel_values': {
            0: 'batch-size',
        },
        'embedding': {0: 'batch-size'},
    }
    preprocess_types = {'image': 'VisionPreprocess'}
    collate_types = {'image': 'VisionTransformersCollate'}
    collate_options = {'image': {}}

    def __init__(
        self,
        preprocess_options: Optional[Dict[str, Dict[str, Any]]] = None,
        collate_options: Optional[Dict[str, Dict[str, Any]]] = None,
    ):
        self.collate_options = {'image': {'name': self.descriptor}}
        super(_VisionTransformerStub, self).__init__(
            preprocess_options=preprocess_options, collate_options=collate_options
        )
        self.input_shapes = [
            (
                'batch-size',
                3,
                self.preprocess_options['image'].get('height', 224),
                self.preprocess_options['image'].get('width', 224),
            ),
        ]


class _OpenCLIPTextStub(_ModelStub, metaclass=abc.ABCMeta):
    """Open CLIP text encoder model stub."""

    task = 'text-to-image'
    architecture = 'transformer'
    builder = 'OpenCLIPTextBuilder'
    input_names = ['text']
    input_dtypes = ['int32']
    input_shapes = [
        ('batch-size', 77),
    ]
    output_name = 'embedding'
    dynamic_axes = {
        'text': {0: 'batch-size'},
        'embedding': {0: 'batch-size'},
    }
    preprocess_types = {'text': 'TextPreprocess'}
    collate_types = {'text': 'OpenCLIPTextCollate'}
    preprocess_options = {'text': {}}
    collate_options = {'text': {}}
    embedding_layer = None
    output_shape = ('batch-size', 512)
    name = 'clip-text'


class _OpenCLIPVisionStub(_ModelStub, metaclass=abc.ABCMeta):
    """Open CLIP vision encoder model stub."""

    task = 'text-to-image'
    architecture = 'transformer'
    builder = 'OpenCLIPVisionBuilder'
    input_names = ['image']
    input_dtypes = ['float32']
    output_name = 'embedding'
    dynamic_axes = {
        'image': {
            0: 'batch-size',
        },
        'embedding': {0: 'batch-size'},
    }
    preprocess_types = {'image': 'VisionPreprocess'}
    collate_types = {'image': 'OpenCLIPVisionCollate'}
    preprocess_options = {
        'image': {'normalization': False, 'move_channel_axis': False, 'resize': False}
    }
    collate_options = {'image': {}}
    embedding_layer = None
    output_shape = ('batch-size', 512)
    name = 'clip-vision'

    def __init__(self):
        self.collate_options = {'image': {'name': self.descriptor}}
        super(_OpenCLIPVisionStub, self).__init__()
        self.input_shapes = [
            (
                'batch-size',
                3,
                self.preprocess_options['image'].get('height', 224),
                self.preprocess_options['image'].get('width', 224),
            ),
        ]


class _HFCLIPTextStub(_TextTransformerStub, metaclass=abc.ABCMeta):
    """Huggingface CLIP text encoder model stub."""

    name = 'clip-text'
    builder = 'CLIPTextBuilder'
    embedding_layer = None
    output_shape = ('batch-size', 512)


class _HFCLIPVisionStub(_VisionTransformerStub, metaclass=abc.ABCMeta):
    """Huggingface CLIP vision encoder model stub."""

    name = 'clip-vision'
    builder = 'CLIPVisionBuilder'
    embedding_layer = None
    output_shape = ('batch-size', 512)
    preprocess_options = {
        'image': {'normalization': False, 'move_channel_axis': True, 'resize': False}
    }


class MLPStub(_ModelStub):
    """MLP model stub.

    :param input_size: Size of the input representations.
    :param hidden_sizes: A list of sizes of the hidden layers. The last hidden size is
        the output size.
    :param bias: Whether to add bias to each layer.
    :param activation: A string to configure activation function, `relu`, `tanh` or
        `sigmoid`. Set to `None` for no activation.
    :param l2: Apply L2 normalization at the output layer.
    """

    name = 'mlp'
    descriptor = 'mlp'
    description = 'Simple MLP encoder trained from scratch'
    task = 'any'
    architecture = 'mlp'
    builder = 'MLPBuilder'
    embedding_layer = None
    input_names = ['features']
    input_dtypes = ['float32']
    output_name = 'embedding'
    dynamic_axes = {'features': {0: 'batch-size'}, 'embedding': {0: 'batch-size'}}
    preprocess_types = {'features': 'DefaultPreprocess'}
    collate_types = {'features': 'DefaultCollate'}
    preprocess_options = {'features': {}}
    collate_options = {'features': {}}

    def __init__(
        self,
        input_size: int,
        hidden_sizes: Tuple[int] = (),
        bias: bool = True,
        activation: Optional[str] = None,
        l2: bool = False,
        preprocess_options: Optional[Dict[str, Dict[str, Any]]] = None,
        collate_options: Optional[Dict[str, Dict[str, Any]]] = None,
    ):
        super(MLPStub, self).__init__(
            preprocess_options=preprocess_options,
            collate_options=collate_options,
            input_size=input_size,
            hidden_sizes=hidden_sizes,
            bias=bias,
            activation=activation,
            l2=l2,
        )
        self.input_shapes = [('batch-size', input_size)]
        self.output_shape = (
            'batch-size',
            hidden_sizes[-1] if len(hidden_sizes) > 0 else input_size,
        )


class ResNet50Stub(_CNNStub):
    """ResNet50 model stub."""

    name = 'resnet50'
    descriptor = 'resnet50'
    description = 'ResNet50 pre-trained on ImageNet'
    embedding_layer = 'adaptiveavgpool2d_173'
    output_shape = ('batch-size', 2048)


class ResNet152Stub(_CNNStub):
    """ResNet152 model stub."""

    name = 'resnet152'
    descriptor = 'resnet152'
    description = 'ResNet152 pre-trained on ImageNet'
    embedding_layer = 'adaptiveavgpool2d_513'
    output_shape = ('batch-size', 2048)


class EfficientNetB0Stub(_CNNStub):
    """EfficientNetB0 model stub."""

    name = 'efficientnet_b0'
    descriptor = 'efficientnet_b0'
    description = 'EfficientNet B0 pre-trained on ImageNet'
    embedding_layer = 'dropout_254'
    output_shape = ('batch-size', 1280)


class EfficientNetB4Stub(_CNNStub):
    """EfficientNetB4 model stub."""

    name = 'efficientnet_b4'
    descriptor = 'efficientnet_b4'
    description = 'EfficientNet B4 pre-trained on ImageNet'
    embedding_layer = 'dropout_507'
    output_shape = ('batch-size', 1792)


class BERTStub(_TextTransformerStub):
    """BERT model stub."""

    name = 'bert-base-cased'
    descriptor = 'bert-base-cased'
    description = 'BERT model pre-trained on BookCorpus and English Wikipedia'
    embedding_layer = None
    output_shape = ('batch-size', 768)


class SBERTStub(_TextTransformerStub):
    """SentenceTransformer model stub."""

    name = 'sentence-transformers/msmarco-distilbert-base-v3'
    descriptor = 'sentence-transformers/msmarco-distilbert-base-v3'
    description = 'Pretrained BERT, fine-tuned on MS Marco'
    embedding_layer = None
    output_shape = ('batch-size', 768)


class CLIPTextBase32PStub(_HFCLIPTextStub):
    """Huggingface CLIP text model stub."""

    task = 'text-to-image'
    descriptor = 'openai/clip-vit-base-patch32'
    description = 'CLIP base model'


class CLIPVisionBase32PStub(_HFCLIPVisionStub):
    """Huggingface CLIP vision model stub."""

    task = 'text-to-image'
    descriptor = 'openai/clip-vit-base-patch32'
    description = 'CLIP base model'


class CLIPTextLarge14PStub(_HFCLIPTextStub):
    """Huggingface CLIP text model stub."""

    task = 'text-to-image'
    descriptor = 'openai/clip-vit-large-patch14'
    description = 'CLIP large model with patch size 14'
    output_shape = ('batch-size', 1024)


class CLIPVisionLarge14PStub(_HFCLIPVisionStub):
    """Huggingface CLIP vision model stub."""

    task = 'text-to-image'
    descriptor = 'openai/clip-vit-large-patch14'
    description = 'CLIP large model with patch size 14'
    output_shape = ('batch-size', 1024)


class CLIPTextBase16PStub(_HFCLIPTextStub):
    """Huggingface CLIP text model stub."""

    task = 'text-to-image'
    descriptor = 'openai/clip-vit-base-patch16'
    description = 'CLIP base model with patch size 16'


class CLIPVisionBase16PStub(_HFCLIPVisionStub):
    """Huggingface CLIP vision model stub."""

    task = 'text-to-image'
    descriptor = 'openai/clip-vit-base-patch16'
    description = 'CLIP base model with patch size 16'


class CLIPTextLarge14P336Stub(_HFCLIPTextStub):
    """Huggingface CLIP text model stub."""

    task = 'text-to-image'
    descriptor = 'openai/clip-vit-large-patch14-336'
    description = 'CLIP large model for 336x336 images'
    output_shape = ('batch-size', 768)


class CLIPVisionLarge14P336Stub(_HFCLIPVisionStub):
    """Huggingface CLIP vision model stub."""

    task = 'text-to-image'
    descriptor = 'openai/clip-vit-large-patch14-336'
    description = 'CLIP large model for 336x336 images'
    output_shape = ('batch-size', 1024)

    def __init__(self):
        self.preprocess_options['image']['height'] = 336
        self.preprocess_options['image']['width'] = 336
        super().__init__()


class OpenCLIPTextRN50OpenaiStub(_OpenCLIPTextStub):
    """Open CLIP text model stub."""

    descriptor = 'RN50#openai'
    description = 'Open CLIP "RN50#openai" model'
    output_shape = ('batch-size', 1024)


class OpenCLIPVisionRN50OpenaiStub(_OpenCLIPVisionStub):
    """Open CLIP vision model stub."""

    descriptor = 'RN50#openai'
    description = 'Open CLIP "RN50#openai" model'
    output_shape = ('batch-size', 1024)


class OpenCLIPTextRN50Yfcc15MStub(_OpenCLIPTextStub):
    """Open CLIP text model stub."""

    descriptor = 'RN50#yfcc15m'
    description = 'Open CLIP "RN50#yfcc15m" model'
    output_shape = ('batch-size', 1024)


class OpenCLIPVisionRN50Yfcc15MStub(_OpenCLIPVisionStub):
    """Open CLIP vision model stub."""

    descriptor = 'RN50#yfcc15m'
    description = 'Open CLIP "RN50#yfcc15m" model'
    output_shape = ('batch-size', 1024)


class OpenCLIPTextRN50Cc12MStub(_OpenCLIPTextStub):
    """Open CLIP text model stub."""

    descriptor = 'RN50#cc12m'
    description = 'Open CLIP "RN50#cc12m" model'
    output_shape = ('batch-size', 1024)


class OpenCLIPVisionRN50Cc12MStub(_OpenCLIPVisionStub):
    """Open CLIP vision model stub."""

    descriptor = 'RN50#cc12m'
    description = 'Open CLIP "RN50#cc12m" model'
    output_shape = ('batch-size', 1024)


class OpenCLIPTextRN50QuickgeluOpenaiStub(_OpenCLIPTextStub):
    """Open CLIP text model stub."""

    descriptor = 'RN50-quickgelu#openai'
    description = 'Open CLIP "RN50-quickgelu#openai" model'
    output_shape = ('batch-size', 1024)


class OpenCLIPVisionRN50QuickgeluOpenaiStub(_OpenCLIPVisionStub):
    """Open CLIP vision model stub."""

    descriptor = 'RN50-quickgelu#openai'
    description = 'Open CLIP "RN50-quickgelu#openai" model'
    output_shape = ('batch-size', 1024)


class OpenCLIPTextRN50QuickgeluYfcc15MStub(_OpenCLIPTextStub):
    """Open CLIP text model stub."""

    descriptor = 'RN50-quickgelu#yfcc15m'
    description = 'Open CLIP "RN50-quickgelu#yfcc15m" model'
    output_shape = ('batch-size', 1024)


class OpenCLIPVisionRN50QuickgeluYfcc15MStub(_OpenCLIPVisionStub):
    """Open CLIP vision model stub."""

    descriptor = 'RN50-quickgelu#yfcc15m'
    description = 'Open CLIP "RN50-quickgelu#yfcc15m" model'
    output_shape = ('batch-size', 1024)


class OpenCLIPTextRN50QuickgeluCc12MStub(_OpenCLIPTextStub):
    """Open CLIP text model stub."""

    descriptor = 'RN50-quickgelu#cc12m'
    description = 'Open CLIP "RN50-quickgelu#cc12m" model'
    output_shape = ('batch-size', 1024)


class OpenCLIPVisionRN50QuickgeluCc12MStub(_OpenCLIPVisionStub):
    """Open CLIP vision model stub."""

    descriptor = 'RN50-quickgelu#cc12m'
    description = 'Open CLIP "RN50-quickgelu#cc12m" model'
    output_shape = ('batch-size', 1024)


class OpenCLIPTextRN101OpenaiStub(_OpenCLIPTextStub):
    """Open CLIP text model stub."""

    descriptor = 'RN101#openai'
    description = 'Open CLIP "RN101#openai" model'
    output_shape = ('batch-size', 512)


class OpenCLIPVisionRN101OpenaiStub(_OpenCLIPVisionStub):
    """Open CLIP vision model stub."""

    descriptor = 'RN101#openai'
    description = 'Open CLIP "RN101#openai" model'
    output_shape = ('batch-size', 512)


class OpenCLIPTextRN101Yfcc15MStub(_OpenCLIPTextStub):
    """Open CLIP text model stub."""

    descriptor = 'RN101#yfcc15m'
    description = 'Open CLIP "RN101#yfcc15m" model'
    output_shape = ('batch-size', 512)


class OpenCLIPVisionRN101Yfcc15MStub(_OpenCLIPVisionStub):
    """Open CLIP vision model stub."""

    descriptor = 'RN101#yfcc15m'
    description = 'Open CLIP "RN101#yfcc15m" model'
    output_shape = ('batch-size', 512)


class OpenCLIPTextRN101QuickgeluOpenaiStub(_OpenCLIPTextStub):
    """Open CLIP text model stub."""

    descriptor = 'RN101-quickgelu#openai'
    description = 'Open CLIP "RN101-quickgelu#openai" model'
    output_shape = ('batch-size', 512)


class OpenCLIPVisionRN101QuickgeluOpenaiStub(_OpenCLIPVisionStub):
    """Open CLIP vision model stub."""

    descriptor = 'RN101-quickgelu#openai'
    description = 'Open CLIP "RN101-quickgelu#openai" model'
    output_shape = ('batch-size', 512)


class OpenCLIPTextRN101QuickgeluYfcc15MStub(_OpenCLIPTextStub):
    """Open CLIP text model stub."""

    descriptor = 'RN101-quickgelu#yfcc15m'
    description = 'Open CLIP "RN101-quickgelu#yfcc15m" model'
    output_shape = ('batch-size', 512)


class OpenCLIPVisionRN101QuickgeluYfcc15MStub(_OpenCLIPVisionStub):
    """Open CLIP vision model stub."""

    descriptor = 'RN101-quickgelu#yfcc15m'
    description = 'Open CLIP "RN101-quickgelu#yfcc15m" model'
    output_shape = ('batch-size', 512)


class OpenCLIPTextRN50X4OpenaiStub(_OpenCLIPTextStub):
    """Open CLIP text model stub."""

    descriptor = 'RN50x4#openai'
    description = 'Open CLIP "RN50x4#openai" model'
    output_shape = ('batch-size', 640)


class OpenCLIPVisionRN50X4OpenaiStub(_OpenCLIPVisionStub):
    """Open CLIP vision model stub."""

    descriptor = 'RN50x4#openai'
    description = 'Open CLIP "RN50x4#openai" model'
    output_shape = ('batch-size', 640)

    def __init__(self):
        self.preprocess_options['image']['height'] = 288
        self.preprocess_options['image']['width'] = 288
        super().__init__()


class OpenCLIPTextRN50X16OpenaiStub(_OpenCLIPTextStub):
    """Open CLIP text model stub."""

    descriptor = 'RN50x16#openai'
    description = 'Open CLIP "RN50x16#openai" model'
    output_shape = ('batch-size', 768)


class OpenCLIPVisionRN50X16OpenaiStub(_OpenCLIPVisionStub):
    """Open CLIP vision model stub."""

    descriptor = 'RN50x16#openai'
    description = 'Open CLIP "RN50x16#openai" model'
    output_shape = ('batch-size', 768)

    def __init__(self):
        self.preprocess_options['image']['height'] = 384
        self.preprocess_options['image']['width'] = 384
        super().__init__()


class OpenCLIPTextRN50X64OpenaiStub(_OpenCLIPTextStub):
    """Open CLIP text model stub."""

    descriptor = 'RN50x64#openai'
    description = 'Open CLIP "RN50x64#openai" model'
    output_shape = ('batch-size', 1024)


class OpenCLIPVisionRN50X64OpenaiStub(_OpenCLIPVisionStub):
    """Open CLIP vision model stub."""

    descriptor = 'RN50x64#openai'
    description = 'Open CLIP "RN50x64#openai" model'
    output_shape = ('batch-size', 1024)

    def __init__(self):
        self.preprocess_options['image']['height'] = 448
        self.preprocess_options['image']['width'] = 448
        super().__init__()


class OpenCLIPTextViTB32OpenaiStub(_OpenCLIPTextStub):
    """Open CLIP text model stub."""

    descriptor = 'ViT-B-32#openai'
    description = 'Open CLIP "ViT-B-32#openai" model'
    output_shape = ('batch-size', 512)


class OpenCLIPVisionViTB32OpenaiStub(_OpenCLIPVisionStub):
    """Open CLIP vision model stub."""

    descriptor = 'ViT-B-32#openai'
    description = 'Open CLIP "ViT-B-32#openai" model'
    output_shape = ('batch-size', 512)


class OpenCLIPTextViTB32Laion2B_e16Stub(_OpenCLIPTextStub):
    """Open CLIP text model stub."""

    descriptor = 'ViT-B-32#laion2b_e16'
    description = 'Open CLIP "ViT-B-32#laion2b_e16" model'
    output_shape = ('batch-size', 512)


class OpenCLIPVisionViTB32Laion2B_e16Stub(_OpenCLIPVisionStub):
    """Open CLIP vision model stub."""

    descriptor = 'ViT-B-32#laion2b_e16'
    description = 'Open CLIP "ViT-B-32#laion2b_e16" model'
    output_shape = ('batch-size', 512)


class OpenCLIPTextViTB32Laion400M_e31Stub(_OpenCLIPTextStub):
    """Open CLIP text model stub."""

    descriptor = 'ViT-B-32#laion400m_e31'
    description = 'Open CLIP "ViT-B-32#laion400m_e31" model'
    output_shape = ('batch-size', 512)


class OpenCLIPVisionViTB32Laion400M_e31Stub(_OpenCLIPVisionStub):
    """Open CLIP vision model stub."""

    descriptor = 'ViT-B-32#laion400m_e31'
    description = 'Open CLIP "ViT-B-32#laion400m_e31" model'


class OpenCLIPTextViTB32Laion400M_e32Stub(_OpenCLIPTextStub):
    """Open CLIP text model stub."""

    descriptor = 'ViT-B-32#laion400m_e32'
    description = 'Open CLIP "ViT-B-32#laion400m_e32" model'
    output_shape = ('batch-size', 512)


class OpenCLIPVisionViTB32Laion400M_e32Stub(_OpenCLIPVisionStub):
    """Open CLIP vision model stub."""

    descriptor = 'ViT-B-32#laion400m_e32'
    description = 'Open CLIP "ViT-B-32#laion400m_e32" model'
    output_shape = ('batch-size', 512)


class OpenCLIPTextViTB32QuickgeluOpenaiStub(_OpenCLIPTextStub):
    """Open CLIP text model stub."""

    descriptor = 'ViT-B-32-quickgelu#openai'
    description = 'Open CLIP "ViT-B-32-quickgelu#openai" model'
    output_shape = ('batch-size', 512)


class OpenCLIPVisionViTB32QuickgeluOpenaiStub(_OpenCLIPVisionStub):
    """Open CLIP vision model stub."""

    descriptor = 'ViT-B-32-quickgelu#openai'
    description = 'Open CLIP "ViT-B-32-quickgelu#openai" model'
    output_shape = ('batch-size', 512)


class OpenCLIPTextViTB32QuickgeluLaion400M_e31Stub(_OpenCLIPTextStub):
    """Open CLIP text model stub."""

    descriptor = 'ViT-B-32-quickgelu#laion400m_e31'
    description = 'Open CLIP "ViT-B-32-quickgelu#laion400m_e31" model'
    output_shape = ('batch-size', 512)


class OpenCLIPVisionViTB32QuickgeluLaion400M_e31Stub(_OpenCLIPVisionStub):
    """Open CLIP vision model stub."""

    descriptor = 'ViT-B-32-quickgelu#laion400m_e31'
    description = 'Open CLIP "ViT-B-32-quickgelu#laion400m_e31" model'
    output_shape = ('batch-size', 512)


class OpenCLIPTextViTB32QuickgeluLaion400M_e32Stub(_OpenCLIPTextStub):
    """Open CLIP text model stub."""

    descriptor = 'ViT-B-32-quickgelu#laion400m_e32'
    description = 'Open CLIP "ViT-B-32-quickgelu#laion400m_e32" model'
    output_shape = ('batch-size', 512)


class OpenCLIPVisionViTB32QuickgeluLaion400M_e32Stub(_OpenCLIPVisionStub):
    """Open CLIP vision model stub."""

    descriptor = 'ViT-B-32-quickgelu#laion400m_e32'
    description = 'Open CLIP "ViT-B-32-quickgelu#laion400m_e32" model'
    output_shape = ('batch-size', 512)


class OpenCLIPTextViTB16OpenaiStub(_OpenCLIPTextStub):
    """Open CLIP text model stub."""

    descriptor = 'ViT-B-16#openai'
    description = 'Open CLIP "ViT-B-16#openai" model'
    output_shape = ('batch-size', 512)


class OpenCLIPVisionViTB16OpenaiStub(_OpenCLIPVisionStub):
    """Open CLIP vision model stub."""

    descriptor = 'ViT-B-16#openai'
    description = 'Open CLIP "ViT-B-16#openai" model'
    output_shape = ('batch-size', 512)


class OpenCLIPTextViTB16Laion400M_e31Stub(_OpenCLIPTextStub):
    """Open CLIP text model stub."""

    descriptor = 'ViT-B-16#laion400m_e31'
    description = 'Open CLIP "ViT-B-16#laion400m_e31" model'
    output_shape = ('batch-size', 512)


class OpenCLIPVisionViTB16Laion400M_e31Stub(_OpenCLIPVisionStub):
    """Open CLIP vision model stub."""

    descriptor = 'ViT-B-16#laion400m_e31'
    description = 'Open CLIP "ViT-B-16#laion400m_e31" model'
    output_shape = ('batch-size', 512)


class OpenCLIPTextViTB16Laion400M_e32Stub(_OpenCLIPTextStub):
    """Open CLIP text model stub."""

    descriptor = 'ViT-B-16#laion400m_e32'
    description = 'Open CLIP "ViT-B-16#laion400m_e32" model'
    output_shape = ('batch-size', 512)


class OpenCLIPVisionViTB16Laion400M_e32Stub(_OpenCLIPVisionStub):
    """Open CLIP vision model stub."""

    descriptor = 'ViT-B-16#laion400m_e32'
    description = 'Open CLIP "ViT-B-16#laion400m_e32" model'
    output_shape = ('batch-size', 512)


class OpenCLIPTextViTB16Plus240Laion400M_e31Stub(_OpenCLIPTextStub):
    """Open CLIP text model stub."""

    descriptor = 'ViT-B-16-plus-240#laion400m_e31'
    description = 'Open CLIP "ViT-B-16-plus-240#laion400m_e31" model'
    output_shape = ('batch-size', 640)


class OpenCLIPVisionViTB16Plus240Laion400M_e31Stub(_OpenCLIPVisionStub):
    """Open CLIP vision model stub."""

    descriptor = 'ViT-B-16-plus-240#laion400m_e31'
    description = 'Open CLIP "ViT-B-16-plus-240#laion400m_e31" model'
    output_shape = ('batch-size', 640)

    def __init__(self):
        self.preprocess_options['image']['height'] = 240
        self.preprocess_options['image']['width'] = 240
        super().__init__()


class OpenCLIPTextViTB16Plus240Laion400M_e32Stub(_OpenCLIPTextStub):
    """Open CLIP text model stub."""

    descriptor = 'ViT-B-16-plus-240#laion400m_e32'
    description = 'Open CLIP "ViT-B-16-plus-240#laion400m_e32" model'
    output_shape = ('batch-size', 640)


class OpenCLIPVisionViTB16Plus240Laion400M_e32Stub(_OpenCLIPVisionStub):
    """Open CLIP vision model stub."""

    descriptor = 'ViT-B-16-plus-240#laion400m_e32'
    description = 'Open CLIP "ViT-B-16-plus-240#laion400m_e32" model'
    output_shape = ('batch-size', 640)

    def __init__(self):
        self.preprocess_options['image']['height'] = 240
        self.preprocess_options['image']['width'] = 240
        super().__init__()


class OpenCLIPTextViTL14OpenaiStub(_OpenCLIPTextStub):
    """Open CLIP text model stub."""

    descriptor = 'ViT-L-14#openai'
    description = 'Open CLIP "ViT-L-14#openai" model'
    output_shape = ('batch-size', 768)


class OpenCLIPVisionViTL14OpenaiStub(_OpenCLIPVisionStub):
    """Open CLIP vision model stub."""

    descriptor = 'ViT-L-14#openai'
    description = 'Open CLIP "ViT-L-14#openai" model'
    output_shape = ('batch-size', 768)


class OpenCLIPTextViTL14336OpenaiStub(_OpenCLIPTextStub):
    """Open CLIP text model stub."""

    descriptor = 'ViT-L-14-336#openai'
    description = 'Open CLIP "ViT-L-14-336#openai" model'
    output_shape = ('batch-size', 768)


class OpenCLIPVisionViTL14336OpenaiStub(_OpenCLIPVisionStub):
    """Open CLIP vision model stub."""

    descriptor = 'ViT-L-14-336#openai'
    description = 'Open CLIP "ViT-L-14-336#openai" model'
    output_shape = ('batch-size', 768)

    def __init__(self):
        self.preprocess_options['image']['height'] = 336
        self.preprocess_options['image']['width'] = 336
        super().__init__()
