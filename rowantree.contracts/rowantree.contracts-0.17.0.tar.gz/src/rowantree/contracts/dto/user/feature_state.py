""" User Feature State Definition """

from typing import Optional

from ...types.feature_detail_type import FeatureDetailType
from ...types.feature_type import FeatureType
from ..base_model import BaseModel


class UserFeatureState(BaseModel):
    """
    UserFeatureState DTO

    Attributes
    ----------
    name: Optional[FeatureType]
        An optional `FeatureType` of the user feature state.
    details: Optional[FeatureDetailType]
        An optional `FeatureDetailType` of the user feature state.
    description: Optional[str]
        An optional textual description of the user feature state.
    """

    name: Optional[FeatureType]
    details: Optional[FeatureDetailType]
    description: Optional[str]
