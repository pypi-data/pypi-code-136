import pytest
from pydantic import ValidationError

from ..commons import RestrictedBaseModel
from ..job import JobCreatorType


def test_job_creator_type():
    class ModelWithJobCreatorType(RestrictedBaseModel):
        creator_type: JobCreatorType

    ModelWithJobCreatorType(creator_type="USER")
    ModelWithJobCreatorType(creator_type="SCOPE")
    with pytest.raises(ValidationError):
        ModelWithJobCreatorType(creator_type="INVALID")
