# Copyright (c) 2022 Shapelets.io
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from abc import ABC, abstractmethod
from typing import List

from ..model import DataAppProfile


class IDataAppsService(ABC):
    @abstractmethod
    def get_all(self) -> List[DataAppProfile]:
        pass

    @abstractmethod
    def create(self, attributes: DataAppProfile) -> DataAppProfile:
        pass

    @abstractmethod
    def get_dataapp(self, dataapp_name: str) -> DataAppProfile:
        pass

    @abstractmethod
    def delete_dataapp(self, dataapp_name: str):
        pass

    @abstractmethod
    def delete_all(self) -> bool:
        pass

    @abstractmethod
    def get_dataapp_privileges(self, dataapp_name: str) -> List[DataAppProfile]:
        pass

    @abstractmethod
    def get_dataapp_versions(self, dataapp_name: str) -> List[float]:
        pass

    @abstractmethod
    def get_dataapp_last_version(self, dataapp_name: str) -> float:
        pass

    @abstractmethod
    def get_dataapp_tags(self, dataapp_name: str) -> List[str]:
        pass
