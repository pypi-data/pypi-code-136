import logging
import os
import warnings
from functools import partial
from operator import countOf
from typing import List, Union
from uuid import UUID

import orjson
from beartype import beartype
from beartype.roar import BeartypeDecorHintPep585DeprecationWarning

import picsellia.exceptions as exceptions
from picsellia import pxl_multithreading as mlt
from picsellia.colors import Colors
from picsellia.decorators import exception_handler
from picsellia.sdk.annotation import Annotation
from picsellia.sdk.connexion import Connexion
from picsellia.sdk.dao import Dao
from picsellia.sdk.multi_object import MultiObject
from picsellia.sdk.tag import Tag
from picsellia.sdk.taggable import Taggable
from picsellia.sdk.worker import Worker
from picsellia.types.enums import DataType, TagTarget
from picsellia.types.schemas import AssetSchema

logger = logging.getLogger("picsellia")
warnings.filterwarnings("ignore", category=BeartypeDecorHintPep585DeprecationWarning)


class Asset(Dao, Taggable):
    def __init__(self, connexion: Connexion, dataset_version_id: UUID, data: dict):
        Dao.__init__(self, connexion, data)
        Taggable.__init__(self, TagTarget.ASSET)
        self._dataset_version_id = dataset_version_id

    @property
    def dataset_version_id(self) -> UUID:
        return self._dataset_version_id

    @property
    def object_name(self) -> str:
        return self._object_name

    @property
    def filename(self) -> str:
        return self._filename

    @property
    def type(self) -> DataType:
        return self._type

    @property
    def width(self) -> int:
        if self.type == DataType.IMAGE:
            return self._width
        else:
            return 0

    @property
    def height(self) -> int:
        if self.type == DataType.IMAGE:
            return self._height
        else:
            return 0

    @property
    def duration(self) -> int:
        if self.type == DataType.VIDEO:
            return self._duration
        else:
            return 0

    def __str__(self):
        return f"{Colors.YELLOW}Asset '{self.filename}' ({self.type}) {Colors.ENDC} (id: {self.id})"

    @exception_handler
    @beartype
    def refresh(self, data: dict) -> AssetSchema:
        schema = AssetSchema(**data)
        self._filename = schema.data.filename
        self._object_name = schema.data.object_name
        self._type = schema.data.type
        if self._type == DataType.IMAGE:
            self._height = schema.data.meta.height
            self._width = schema.data.meta.width
        elif self._type == DataType.VIDEO:
            self._duration = schema.data.meta.duration
        return schema

    @exception_handler
    @beartype
    def sync(self) -> dict:
        r = self.connexion.get(f"/sdk/asset/{self.id}").json()
        self.refresh(r)
        return r

    @exception_handler
    @beartype
    def get_tags(self) -> List[Tag]:
        """Retrieve the tags of your asset.

        Examples:
            ```python
                tags = asset.get_tags()
                assert tags[0].name == "bicycle"
            ```

        Returns:
            List of tags as Tag
        """
        r = self.sync()
        return list(map(partial(Tag, self.connexion), r["tags"]))

    @exception_handler
    @beartype
    def get_annotation(self, worker: Union[Worker, None] = None) -> Annotation:
        """Retrieve the annotation of this asset by the given worker (if none given, it is the current user)

        Examples:
            ```python
                some_annotation = one_asset.get_annotation(my_worker)
                my_annotation = one_asset.get_annotation()
                assert some_annotation == my_annotation
            ```

        Returns:
            An object (Annotation)
        """
        params = {}
        if worker is not None:
            params["worker_id"] = worker.id
        r = self.connexion.get(
            f"/sdk/asset/{self.id}/annotations/find", params=params
        ).json()
        return Annotation(self.connexion, self.dataset_version_id, self.id, r)

    @exception_handler
    @beartype
    def create_annotation(
        self, duration: float, worker: Union[Worker, None] = None
    ) -> Annotation:
        """Create an annotation on this asset

        Examples:
            ```python
                some_annotation = one_asset.create_annotation(my_worker_1, 0.120)
            ```

        Returns:
            An object (Annotation)
        """
        payload = {
            "duration": duration,
        }
        if worker is not None:
            payload["worker_id"] = worker.id
        r = self.connexion.post(
            f"/sdk/asset/{self.id}/annotations", data=orjson.dumps(payload)
        ).json()
        return Annotation(self.connexion, self.dataset_version_id, self.id, r)

    @exception_handler
    @beartype
    def list_annotations(self) -> List[Annotation]:
        """List all annotation of an asset

        Examples:
            ```python
                annotations = one_asset.list_annotations()
            ```

        Returns:
            A list of (Annotation)
        """
        r = self.connexion.get(f"/sdk/asset/{self.id}/annotations").json()
        return list(
            map(
                partial(Annotation, self.connexion, self.dataset_version_id, self.id),
                r["items"],
            )
        )

    @exception_handler
    @beartype
    def delete_annotations(self, workers: List[Worker] = None) -> None:
        """Delete all annotations of an asset: it will erase every shape of every annotation.

        You can give workers on which it will be effectively erased.

        :warning: **DANGER ZONE**: Be careful here !

        Examples:
            ```python
                one_asset.delete_annotations()
            ```
        """
        payload = {"asset_ids": [self.id]}
        if workers is not None:
            payload["worker_ids"] = [worker.id for worker in workers]

        self.connexion.delete(
            f"/sdk/dataset/version/{self.dataset_version_id}/annotations",
            data=orjson.dumps(payload),
        )
        logger.info(f"All annotations of {self} were removed.")

    @exception_handler
    @beartype
    def delete(self) -> None:
        """Delete this asset from its dataset

        :warning: **DANGER ZONE**: Be very careful here!

        Remove this asset and its annotation from the dataset it belongs

        Examples:
            ```python
                one_asset.delete()
            ```
        """
        self.connexion.delete(f"/sdk/asset/{self.id}")
        logger.info(f"{self} removed from dataset")

    @exception_handler
    @beartype
    def download(self, target_path: str = "./", force_replace: bool = False) -> None:
        """Download this asset into given target path

        Examples:
            ```python
                pic.download('./assets/')
            ```

        Arguments:
            target_path (str, optional): Target path where assets will be downloaded. Defaults to './'.
            force_replace: (bool, optional): Replace an existing file if exists. Defaults to False.
        """
        data = self.sync()
        path = os.path.join(target_path, self.filename)
        if self.connexion.do_download_file(
            path,
            data["data"]["presigned_url"],
            is_large=True,
            force_replace=force_replace,
        ):
            logger.info(f"{self.filename} downloaded successfully")
        else:
            logger.error(f"Did not download file '{self.filename}'")


class MultiAsset(MultiObject[Asset], Taggable):
    @beartype
    def __init__(
        self, connexion: Connexion, dataset_version_id: UUID, items: List[Asset]
    ):
        MultiObject.__init__(self, connexion, items)
        Taggable.__init__(self, TagTarget.ASSET)
        self.dataset_version_id = dataset_version_id

    def __str__(self):
        return f"{Colors.GREEN}MultiAsset{Colors.ENDC} object, size: {len(self)}"

    def __getitem__(self, key) -> Union[Asset, "MultiAsset"]:
        if isinstance(key, slice):
            indices = range(*key.indices(len(self.items)))
            assets = [self.items[i] for i in indices]
            return MultiAsset(self.connexion, self.dataset_version_id, assets)
        return self.items[key]

    @beartype
    def __add__(self, other):
        self.assert_same_connexion(other)
        items = self.items.copy()
        if isinstance(other, MultiAsset):
            items.extend(other.items.copy())
        elif isinstance(other, Asset):
            items.append(other)
        else:
            raise exceptions.PicselliaError("You can't add these two objects")

        return MultiAsset(self.connexion, self.dataset_version_id, items)

    @beartype
    def __iadd__(self, other):
        self.assert_same_connexion(other)

        if isinstance(other, MultiAsset):
            self.extend(other.items.copy())
        elif isinstance(other, Asset):
            self.append(other)
        else:
            raise exceptions.PicselliaError("You can't add these two objects")

        return self

    def copy(self):
        return MultiAsset(self.connexion, self.dataset_version_id, self.items.copy())

    @exception_handler
    @beartype
    def delete(self) -> None:
        """Delete assets from their dataset

        :warning: **DANGER ZONE**: Be very careful here!

        Remove these assets and its annotation from the dataset it belongs

        Examples:
            ```python
                some_assets = dataset.list_assets()[:10]
                some_assets.delete()
            ```
        """
        payload = self.ids
        self.connexion.delete(
            f"/sdk/dataset/version/{self.dataset_version_id}/assets",
            data=orjson.dumps(payload),
        )
        logger.info(f"{len(self.items)} assets removed from {self}")

    @exception_handler
    @beartype
    def download(
        self,
        target_path: str = "./",
        force_replace: bool = False,
        max_workers: int = 12,
    ) -> None:
        """Download this multi asset in given target path


        Examples:
            ```python
                bunch_of_assets = client.get_dataset("foo_dataset").get_version("first").list_assets()
                bunch_of_assets.download('./downloads/')
            ```
        Arguments:
            target_path (str, optional): Target path where to download. Defaults to './'.
            max_workers (int, optional): Number of max workers used to download. Defaults to 20.
            force_replace: (bool, optional): Replace an existing file if exists. Defaults to False.
        """

        def download_one_data(item: Asset):
            data = item.sync()
            path = os.path.join(target_path, item.filename)
            return self.connexion.do_download_file(
                path,
                data["data"]["presigned_url"],
                is_large=True,
                force_replace=force_replace,
            )

        results = mlt.do_mlt_function(
            self.items, download_one_data, lambda item: item.id, max_workers=max_workers
        )
        downloaded = countOf(results.values(), True)

        logger.info(
            f"{downloaded} assets downloaded (over {len(results)}) in directory {target_path}"
        )

    @exception_handler
    @beartype
    def delete_annotations(self, workers: List[Worker] = None) -> None:
        """Delete all annotations of all these assets: it will erase every shape of every annotation of every asset.

        You can give workers on which it will be effectively erased.

        :warning: **DANGER ZONE**: Be careful here !

        Examples:
            ```python
                multiple_assets.delete_annotations(workers=)
            ```
        """
        payload = {"asset_ids": self.ids}
        if workers is not None:
            payload["worker_ids"] = [worker.id for worker in workers]

        self.connexion.delete(
            f"/sdk/dataset/version/{self.dataset_version_id}/annotations",
            data=orjson.dumps(payload),
        )
        logger.info(f"All annotations of {len(self)} assets were removed.")
