import logging
import typing as t

import pyarrow as pa

from sarus_data_spec.manager.ops.asyncio.base import (
    BaseDatasetOp,
    BaseScalarOp,
)
from sarus_data_spec.manager.ops.asyncio.processor.external.external_op import (  # noqa: E501
    ExternalDatasetOp,
    ExternalScalarOp,
)
from sarus_data_spec.manager.ops.asyncio.processor.standard.filter import (
    Filter,
)
from sarus_data_spec.manager.ops.asyncio.processor.standard.get_item import (
    GetItem,
)
from sarus_data_spec.manager.ops.asyncio.processor.standard.project import (
    Project,
)
from sarus_data_spec.manager.ops.asyncio.processor.standard.sample import (
    Sample,
)
from sarus_data_spec.manager.ops.asyncio.processor.standard.shuffle import (
    Shuffle,
)
from sarus_data_spec.manager.ops.asyncio.processor.standard.synthetic import (
    Synthetic,
)

try:
    from sarus_data_spec.manager.ops.asyncio.processor.standard.protection_utils.protected_paths import (  # noqa: E501
        ProtectedPaths,
        PublicPaths,
    )
    from sarus_data_spec.manager.ops.asyncio.processor.standard.protection_utils.protection import (  # noqa: E501
        ProtectedDataset,
    )
except ModuleNotFoundError:
    logger = logging.getLogger(__name__)
    logger.info("Transforms: Protection not available.")

try:
    from sarus_data_spec.manager.ops.asyncio.processor.standard.user_settings.automatic import (  # noqa: E501
        AutomaticUserSettings,
    )
    from sarus_data_spec.manager.ops.asyncio.processor.standard.user_settings.user_settings import (  # noqa: E501
        UserSettingsDataset,
    )
except ModuleNotFoundError:
    logger = logging.getLogger(__name__)
    logger.info("Transforms: UserSettings not available.")

import sarus_data_spec.typing as st


def get_dataset_op(transform: st.Transform) -> t.Type[BaseDatasetOp]:
    if transform.is_external():
        return ExternalDatasetOp
    elif transform.protobuf().spec.HasField('sample'):
        return Sample
    elif transform.protobuf().spec.HasField('protect_dataset'):
        return ProtectedDataset
    elif transform.protobuf().spec.HasField('user_settings'):
        return UserSettingsDataset
    elif transform.protobuf().spec.HasField('filter'):
        return Filter
    elif transform.protobuf().spec.HasField('project'):
        return Project
    elif transform.protobuf().spec.HasField('shuffle'):
        return Shuffle
    elif transform.protobuf().spec.HasField('synthetic'):
        return Synthetic
    elif transform.protobuf().spec.HasField('get_item'):
        return GetItem
    else:
        raise NotImplementedError(
            f"{transform.protobuf().spec.WhichOneof('spec')}"
        )


def get_scalar_op(transform: st.Transform) -> t.Type[BaseScalarOp]:
    if transform.is_external():
        return ExternalScalarOp
    elif transform.name() == 'protected_paths':
        # here we assume this transform is called
        # on a single dataset
        return ProtectedPaths
    elif transform.name() == 'public_paths':
        # here we assume this transform is called
        # on a single dataset
        return PublicPaths
    elif transform.name() == 'automatic_user_settings':
        return AutomaticUserSettings
    else:
        raise NotImplementedError(f"scalar_transformed for {transform}")


class TransformedDataset(BaseDatasetOp):
    async def to_arrow(
        self, batch_size: int
    ) -> t.AsyncIterator[pa.RecordBatch]:
        transform = self.dataset.transform()
        OpClass = get_dataset_op(transform)
        return await OpClass(self.dataset).to_arrow(batch_size)

    async def schema(self) -> st.Schema:
        transform = self.dataset.transform()
        OpClass = get_dataset_op(transform)
        return await OpClass(self.dataset).schema()


class TransformedScalar(BaseScalarOp):
    async def value(self) -> t.Any:
        transform = self.scalar.transform()
        OpClass = get_scalar_op(transform)
        return await OpClass(self.scalar).value()
