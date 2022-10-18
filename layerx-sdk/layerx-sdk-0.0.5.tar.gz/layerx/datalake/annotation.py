import json
from typing import TYPE_CHECKING

from .keys import CATEGORIES
from .label import Label
from .logger import get_debug_logger

if TYPE_CHECKING:
    from . import DatalakeClient

datalake_logger = get_debug_logger('Annotation')


class Annotation:
    def __init__(self, client: "DatalakeClient"):
        self._client = client

    def upload_coco(self, file_path: str):
        # load json file
        f = open(file_path)
        coco_data = json.load(f)
        f.close()

        label = Label(client=self._client)
        label.create_label_from_cocojson(categories=coco_data[CATEGORIES])
        # TODO: format Images and Annotations as MetaUpdates format, then call metaUpdates API

