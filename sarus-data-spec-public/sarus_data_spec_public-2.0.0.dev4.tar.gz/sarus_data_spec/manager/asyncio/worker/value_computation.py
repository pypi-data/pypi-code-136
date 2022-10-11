import logging
import os
import pickle as pkl
import traceback
import typing as t

from sarus_data_spec import typing as st
from sarus_data_spec.constants import (
    CACHE_PATH,
    CACHE_TYPE,
    SCALAR_TASK,
    ScalarCaching,
)
from sarus_data_spec.manager.asyncio.worker.worker_computation import (
    WorkerComputation,
)
from sarus_data_spec.scalar import Scalar
import sarus_data_spec.protobuf as sp
import sarus_data_spec.status as stt

logger = logging.getLogger(__name__)


class ValueComputation(WorkerComputation[t.Any]):
    """Class responsible for handling the computation
    of scalars."""

    task_name = SCALAR_TASK

    async def task_result(
        self, dataspec: st.DataSpec, **kwargs: t.Any
    ) -> t.Any:

        status = await self.complete_task(dataspec=dataspec)
        stage = status.task(self.task_name)
        assert stage
        if stage.ready():
            if stage[CACHE_TYPE] == ScalarCaching.PICKLE.value:
                with open(stage.properties()[CACHE_PATH], "rb") as f:
                    data = pkl.load(f)
                return data

            return sp.python_proto_factory(
                stage.properties()[CACHE_PATH], stage.properties()[CACHE_TYPE]
            )

    def cache_path(self, dataspec: st.DataSpec) -> str:
        return os.path.join(
            self.manager().parquet_dir(), f"{dataspec.uuid()}.pkl"
        )

    async def execute_computation(self, dataspec: st.DataSpec) -> None:

        try:
            logger.debug(f'STARTED SCALAR {dataspec.uuid()}')
            scalar = await self.manager().async_value_op(
                scalar=t.cast(Scalar, dataspec)
            )
        except Exception:
            stt.error(
                dataspec=dataspec,
                manager=self.manager(),
                task=self.task_name,
                properties={"message": traceback.format_exc()},
            )
        else:
            logging.debug(f'FINISHED SCALAR {dataspec.uuid()}')
            if isinstance(scalar, st.HasProtobuf):
                res = sp.to_base64(scalar.protobuf())
                stt.ready(
                    dataspec=dataspec,
                    task=self.task_name,
                    properties={
                        CACHE_PATH: res,
                        CACHE_TYPE: sp.type_name(scalar.prototype()),
                    },
                )
                return

            caching_properties = {}
            with open(self.cache_path(dataspec=dataspec), "wb") as f:
                pkl.dump(scalar, f)
            caching_properties[CACHE_TYPE] = ScalarCaching.PICKLE.value
            caching_properties[CACHE_PATH] = self.cache_path(dataspec)
            stt.ready(
                dataspec=dataspec,
                manager=self.manager(),
                task=self.task_name,
                properties=caching_properties,
            )
