# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Constants for classification tasks."""


class DatasetLiterals:
    """Key columns for Dataset"""
    TEXT_COLUMN = 'text'
    DATAPOINT_ID = 'datapoint_id'
    INPUT_IDS = 'input_ids'
    TOKEN_TYPE_IDS = 'token_type_ids'
    ATTENTION_MASK = 'attention_mask'


class MultiClassInferenceLiterals:
    """Defining names of the artifacts used during multi-class inference"""
    MODEL_FILE_NAME = 'pytorch_model.bin'
    TOKENIZER_FILE_NAME = 'tokenizer_config.json'
    TRAINING_ARGS = 'training_args.bin'
    LABEL_LIST = "label_list.npy"
    MAX_SEQ_LENGTH = "max_seq_length.npy"
