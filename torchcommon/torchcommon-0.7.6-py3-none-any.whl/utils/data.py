#!/usr/bin/env python3

import abc
import glob
import os
from typing import Union, Sequence, Any, Callable, MutableMapping

from docset import DocSet, ConcatDocSet
from torch.utils.data import Dataset

from .image import read_image, normalize_image

Doc = MutableMapping[str, Any]


class DocTransform(abc.ABC):

    @abc.abstractmethod
    def __call__(self, doc: Doc):
        pass


class DSDataset(Dataset):

    def __init__(self, path: Union[str, Sequence[str]]):
        path_list = []
        if isinstance(path, str):
            if os.path.isdir(path):
                path_list.extend(glob.iglob(os.path.join(path, '*.ds')))
            else:
                path_list.append(path)
        else:
            path_list.extend(path)

        self.ds_list = [DocSet(path) for path in path_list]
        self.ds = self.ds_list[0] if len(self.ds_list) == 1 else ConcatDocSet(self.ds_list)

        self.transforms = []

    def add_transform(self, transform: Callable[[Doc], Doc]):
        self.transforms.append(transform)

    def __len__(self):
        return len(self.ds)

    def __getitem__(self, i):
        doc = self.ds[i]
        for transform in self.transforms:
            doc = transform(doc)
        return doc


class ImageTransform(DocTransform):

    def __init__(self, image_field='image', augmenter=None):
        self.image_field = image_field
        self.augmenter = augmenter

    def __call__(self, doc: Doc):
        image = read_image(doc[self.image_field])
        image = self.augmenter(image=image)
        image = normalize_image(image, transpose=True)
        doc[self.image_field] = image
        return doc


class ImageClassificationDataset(DSDataset):

    def __init__(self, path):
        super(ImageClassificationDataset, self).__init__(path)

    def __getitem__(self, i):
        doc = super(ImageClassificationDataset, self).__getitem__(i)

        return doc
