#!/usr/bin/env python
# coding: utf-8
import argparse
import logging
import importlib
from importlib.resources import open_text
import json
import os
import sys
from functools import partial

import toml

import pyclipse.label as label
from pyclipse.dataset import DeidDataset
# from pyclipse.io import read_task, write_task

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
_LOGGER = logging.getLogger(__name__)


def parse_arguments(arguments: list=None) -> argparse.Namespace:
    """Initialize argument parser and sub-argument parsters."""
    parser = argparse.ArgumentParser(
        description="mimic command line interface"
    )

    subparsers = parser.add_subparsers(dest="action", title="action")
    subparsers.required = True

    # === preprocess the dataset
    preprocess = subparsers.add_parser(
        "preprocess", help=("Preprocess a deidentification dataset.")
    )
    preprocess.add_argument(
        '-d',
        '--dataset',
        type=str,
        required=True,
        help='Dataset to use.'
    )
    preprocess.add_argument(
        '-o',
        '--output',
        type=str,
        required=True,
        help='Dataset to output.'
    )

    # === train a model
    train = subparsers.add_parser(
        "train", help=("Train a deidentification model with a given dataset.")
    )
    train.add_argument(
        '-d',
        '--dataset',
        type=str,
        required=True,
        help='Dataset to use.'
    )

    # === annotate a model
    annotate = subparsers.add_parser(
        "annotate", help=("Annotate a dataset given a model.")
    )
    # === evaluate a model
    evaluate = subparsers.add_parser(
        "evaluate", help=("Evaluate a model using a given dataset.")
    )
    evaluate.add_argument(
        '-d',
        '--dataset',
        type=str,
        required=True,
        help='Dataset to use.'
    )

    return parser.parse_args(arguments)

def preprocess(args):
    """Preprocess a dataset."""
    data_dir = args.dataset
    
    deid_task = DeidDataset.from_standoff(data_dir)

    # apply a transform to simplify the labels
    deid_task.transform_labels('base')

    # output
    write_task(deid_task, './out/', format='csv')

def train(args):
    """Train a model given a dataset."""
    pass

def annotate(args):
    """Annotate a dataset using a given model."""
    pass

def evaluate(args):
    """Evaluate a model given a dataset."""
    pass


def main_cli(argv=sys.argv):
    # load in a trained model
    args = parse_arguments(argv[1:])

    # load in the specified toml config for parsing notes
    # with open(args.toml, 'r') as fp:
    #     parsed_toml = toml.load(fp)

    # each note action has subactions
    if args.action == 'preprocess':
        preprocess(args)
    else:
        raise NotImplementedError('Unimplemented action.')

if __name__ == '__main__':
    main_cli()