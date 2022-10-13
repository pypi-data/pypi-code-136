# Copyright (c) 2022 Shapelets.io
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from abc import ABC, abstractmethod
from typing import List, Optional, Set, Tuple

from ..model import DataAppField, DataAppProfile, PrincipalId


class IDataAppsRepo(ABC):
    @abstractmethod
    def create(self, details: DataAppProfile) -> Optional[DataAppProfile]:
        pass

    @abstractmethod
    def load_by_name(self, dataapp_name: str) -> Optional[DataAppProfile]:
        pass

    @abstractmethod
    def load_by_principal(self, principal: PrincipalId) -> Optional[DataAppProfile]:
        pass

    @abstractmethod
    def delete_all(self):
        pass

    @abstractmethod
    def delete_by_name(self, dataapp_name: str):
        pass

    @abstractmethod
    def load_all(self,
                 attributes: Set[DataAppField],
                 skip: Optional[int],
                 sort_by: Optional[List[Tuple[DataAppField, bool]]],
                 limit: Optional[int]) -> List[DataAppProfile]:
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
