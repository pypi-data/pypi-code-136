from enum import Enum


class DeepLearningTask(str, Enum):
    CLASSIFICATION = "classification"
    SEMANTIC_SEGMENTATION = "semantic_segmentation"
    OBJECT_DETECTION = "object_detection"
    NLP = "nlp"
    OTHER = "other"


class DeepLearningTaskLabel(str, Enum):
    CLASSIFICATION = "Classification"
    SEMANTIC_SEGMENTATION = "Semantic Segmentation"
    OBJECT_DETECTION = "Object Detection"
    NLP = "NLP"
    OTHER = "Other"
