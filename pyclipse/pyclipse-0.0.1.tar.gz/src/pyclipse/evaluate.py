"""Methods for evaluating model performance."""
import numpy as np
from datasets import load_metric
import torch
from tqdm import tqdm

from datetime import datetime
import logging
from pathlib import Path
import os
import json
import pprint
import math

import numpy as np

from transformers import AutoTokenizer
from transformers import AutoModelForTokenClassification
from transformers import Trainer, TrainingArguments
from datasets import load_metric

# local packages
from transformer_deid.data import DeidDataset, DeidTask
from transformer_deid.evaluation import compute_metrics
from transformer_deid.tokenization import assign_tags, encode_tags, split_sequences
from transformer_deid.utils import convert_dict_to_native_types

def eval_model(modelDir: str, deid_task: DeidTask, train_dataset: DeidDataset,
               val_dataset: DeidDataset, test_dataset: DeidDataset):
    """Generates all metrics for single a model making inferences on a single dataset.

       Args:
            modelDir: directory containing config.json, pytorch_model.bin, and training_args.bin
                e.g., 'i2b2_2014_{base architecture}_Model_{epochs}'
            deid_task: DeidTask, see data.py
            train, val, and test_dataset: DeidDatasets, see data.py

       Returns:
            results_multiclass: dict of operating point statistics (precision, recall, f1) for each datatype
                datatypes are: age, contact, date, ID, location, name, profession
            results_binary: dict of operating point statistics (precision, recall, f1) for binary label
                i.e., PHI or non-PHI labels
    """

    epochs = int(modelDir.split('_')[-1])
    out_dir = '/'.join(modelDir.split('/')[0:-1])
    train_batch_size = 8

    device = 'cuda:0' if torch.cuda.is_available() else 'cpu'

    model = AutoModelForTokenClassification.from_pretrained(
        modelDir, num_labels=len(deid_task.labels)).to(device)

    model.eval()

    training_args = TrainingArguments(
        output_dir=out_dir,
        num_train_epochs=epochs,
        per_device_train_batch_size=train_batch_size,
        per_device_eval_batch_size=8,
        warmup_steps=500,
        weight_decay=0.01,
        logging_dir='./logs',
        logging_steps=10,
        save_strategy='epoch')

    trainer = Trainer(model=model,
                      args=training_args,
                      train_dataset=train_dataset,
                      eval_dataset=val_dataset)

    predictions, labels, _ = trainer.predict(test_dataset)
    predicted_label = np.argmax(predictions, axis=2)

    # load metric to be used -- if none is passed, default to seqeval
    metric_dir = "transformer_deid/token_evaluation.py"
    metric = load_metric(metric_dir)

    results_multiclass = compute_metrics(predicted_label,
                                         labels,
                                         deid_task.labels,
                                         metric=metric)

    results_binary = compute_metrics(predicted_label,
                                     labels,
                                     deid_task.labels,
                                     metric=metric,
                                     binary_evaluation=True)

    return results_multiclass, results_binary


# function to return all metrics in two lists


def eval_model_list(modelDirList: list,
                    dataDir: str,
                    testDirList: list,
                    output_metric=None) -> list:
    """Generate all metrics or a specific metric for a list of models over all test sets in a list of test sets

       Args:
            modelDirList: list of model directories
                each modelDir should have the form 'i2b2_2014_{base architecture}_Model_{epochs}'
            dataDir: directory containing training/validation data with txt and ann folders
            testDirList: list of test data directories
                each test dir must have txt and ann folders
            output_metric: name of metric to be returned from binary evaluation
                if None, returns all metrics (multiclass and binary)

       Returns:
            results: list of lists, each entry corresponding to the output_metric argument
                for a model's inference on a test dataset
    """

    results = []

    for j, modelDir in enumerate(modelDirList):
        baseArchitecture = modelDir.split('_')[-3].lower()
        task_name = dataDir.split('/')[-1]

        if baseArchitecture == 'bert':
            tokenizerArch = 'bert-base-cased'
        elif baseArchitecture == 'roberta':
            tokenizerArch = 'roberta-base'
        elif baseArchitecture == 'distilbert':
            tokenizerArch = 'distilbert-base-cased'

        modelResults = []

        for i, testDir in enumerate(testDirList):
            if (i == 0) and (j == 0):
                deid_task, train_dataset, val_dataset, test_dataset = load_data(
                    task_name, dataDir, testDir, tokenizerArch)
            else:
                deid_task, test_dataset = load_new_test_set(
                    deid_task, testDir, tokenizerArch)

            results_multiclass, results_binary = eval_model(
                modelDir, deid_task, train_dataset, val_dataset, test_dataset)

            if output_metric is None:
                modelResults += [[results_multiclass, results_binary]]
            else:
                modelResults += [results_binary[output_metric]]

        results += [modelResults]

    return results

def compute_metrics(predictions, labels, label_list, metric=load_metric("seqeval"), binary_evaluation=False) -> dict:
    """Returns a dictionary of operating point statistics (Precision/Recall/F1)."""
    # Remove ignored index (special tokens)
    true_predictions = [
        [label_list[p] for (p, l) in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions, labels)
    ]
    true_labels = [
        [label_list[l] for (p, l) in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions, labels)
    ]

    if binary_evaluation:
        # convert all labels to PHI or not PHI
        true_predictions = [
            ['PHI' if w != 'O' else 'O' for w in sequence]
            for sequence in true_predictions
        ]
        true_labels = [
            ['PHI' if w != 'O' else 'O' for w in sequence]
            for sequence in true_labels
        ]
    
    # convert to BIOC
    # true_predictions = convert_to_bio_scheme(true_predictions)
    # true_labels = convert_to_bio_scheme(true_labels)

    return metric.compute(predictions=true_predictions, references=true_labels)