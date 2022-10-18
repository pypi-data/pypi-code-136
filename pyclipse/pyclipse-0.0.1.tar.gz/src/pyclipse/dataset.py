from pathlib import Path
from typing import List, Optional, Union, TextIO
import os
from dataclasses import dataclass, field
from importlib.resources import open_text
import json

from .label import Label

@dataclass
class DeidDataset(object):
    """Store multiple text/label entries for a corpus."""
    documents: list
    labels: list
    ids: list

    def __post_init__(self, examples):
        """Add entity types."""
        # create a list of unique labels and mapping dict
        self._update_entity_type()

    def get_unique_entity_types(self):
        """Gets the list of labels for this data set."""
        entity_types = set(label.entity_type for labels in self.labels for label in labels)
        entity_types = sorted(list(entity_types))
        # add in the object tag
        # ensure it is the first element as a convention
        # TODO: move 'O' out of here into load labels
        if 'O' in entity_types:
            entity_types.pop('O')
            entity_types = ['O'] + entity_types

        return entity_types

    def _update_entity_type(self):
        self.entity_types = self.get_unique_entity_types()
        self.entity2id = {tag: id for id, tag in enumerate(self.entity_types)}
        self.id2entity = {id: tag for tag, id in self.entity2id.items()}

    def get_labels(self):
        """Return a copy of all labels in the task."""
        return [
            label for label in self.labels
        ]

    def set_labels(self, labels: List[Label]):
        self.labels = labels
        self._update_entity_type()

    def transform_labels(self, transform: str):
        """
        Transforms the datasets labels based on a predefined transform.

        Essentially applies a dict to each entity type.
        """

        with open_text('pyclipse', 'entity_map.json') as fp:
            label_map = json.load(fp)
        
        # label_membership has different label transforms as keys
        if transform not in label_map:
            raise KeyError('Unable to find label transform %s in label.json' % transform)
        label_map = label_map[transform]

        # mapper has items "harmonized_label": ["label 1", "label 2", ...]
        # invert this for the final label mapping
        mapper = {
            label.lower(): harmonized_label.lower()
            for harmonized_label, original_labels in label_map.items()
            for label in original_labels
        }
        self.set_labels(
            [Label(mapper[l.entity_type], l.start, l.length)
            for l in self.labels]
        )

    @classmethod
    def from_standoff(cls, path) -> dict:
        """Creates a DeidDataset from txt/ann files."""
        ids, documents, labels = [], [], []

        # for deid datasets, "path" is a folder containing txt/ann subfolders
        # "txt" subfolder has text files with the text of the examples
        # "ann" subfolder has annotation files with the labels
        txt_path = path / 'txt'
        ann_path = path / 'ann'
        for f in os.listdir(txt_path):
            if not f.endswith('.txt'):
                continue

            # guid is the file name
            guid = f[:-4]
            with open(txt_path / f, 'r') as fp:
                text = ''.join(fp.readlines())

            # load the annotations from disk
            # these datasets have consistent folder structures:
            #   root_path/txt/RECORD_NAME.txt - has text
            #   root_path/ann/RECORD_NAME.gs - has annotations
            document_labels = Label.load_csv(ann_path / f'{f[:-4]}.gs')

            ids.append(guid)
            documents.append(text)
            labels.append(document_labels)

        return cls(
            documents=documents,
            labels=labels,
            ids=ids
        )
