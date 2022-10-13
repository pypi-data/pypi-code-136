# Copyright (c) 2022 Shapelets.io
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT


from typing import List, Optional, Set, Tuple

from .idataappsrepo import IDataAppsRepo
from .idataappsservice import IDataAppsService
from ..db import transaction
from ..model import (
    DataAppField,
    DataAppAllFields,
    DataAppProfile
)


class DataAppsService(IDataAppsService):
    __slots__ = ('_dataapps_repo',)

    def __init__(self, dataapp_repo: IDataAppsRepo) -> None:
        self._dataapp_repo = dataapp_repo

    def get_all(self,
                attributes: Optional[Set[DataAppField]] = DataAppAllFields,
                sort_by: Optional[List[Tuple[DataAppField, bool]]] = None,
                skip: Optional[int] = None,
                limit: Optional[int] = None) -> List[DataAppProfile]:
        return self._dataapp_repo.load_all(attributes, sort_by, skip, limit)

    def create(self, attributes: DataAppProfile) -> DataAppProfile:
        # TODO: some checks
        # if attributes.version is None:
        #     raise ValueError("Invalid version")
        with transaction():
            return self._dataapp_repo.create(attributes)

    def get_dataapp(self, dataapp_name: str):
        return self._dataapp_repo.load_by_name(dataapp_name)

    def delete_dataapp(self, dataapp_name: str) -> DataAppProfile:
        return self._dataapp_repo.delete_by_name(dataapp_name)

    def delete_all(self) -> bool:
        self._dataapp_repo.delete_all()

    def get_dataapp_privileges(self, dataapp_name: str) -> List[DataAppProfile]:
        pass

    def get_dataapp_versions(self, dataapp_name: str) -> List[float]:
        self._dataapp_repo.get_dataapp_versions(dataapp_name)

    def get_dataapp_last_version(self, dataapp_name: str) -> float:
        self._dataapp_repo.get_dataapp_last_version(dataapp_name)

    def get_dataapp_tags(self, dataapp_name: str) -> List[str]:
        self._dataapp_repo.get_dataapp_tags(dataapp_name)
