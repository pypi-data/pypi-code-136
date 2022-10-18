import typing as t

import pyarrow as pa

from sarus_data_spec.arrow.array import convert_record_batch
from sarus_data_spec.constants import DATASET_SLUGNAME
from sarus_data_spec.manager.ops.asyncio.processor.standard.standard_op import (  # noqa: E501
    StandardDatasetOp,
)
from sarus_data_spec.manager.ops.asyncio.processor.standard.visitor_selector import (  # noqa: E501
    filter_primary_keys,
    select_rows,
    update_fks,
)
from sarus_data_spec.schema import schema
import sarus_data_spec.type as sdt
import sarus_data_spec.typing as st


class Filter(StandardDatasetOp):
    """Computes schema and arrow
    batches for a dataspec transformed by
    a user_settings transform
    """

    async def schema(self) -> st.Schema:
        parent_schema = await self.parent_schema()
        new_type = sdt.Type(
            self.dataset.transform().protobuf().spec.filter.filter
        )
        new_type = update_fks(
            curr_type=new_type, original_type=new_type  # type:ignore
        )
        old_properties = parent_schema.properties()

        if 'primary_keys' in old_properties.keys():
            new_pks = filter_primary_keys(
                old_properties['primary_keys'],
                new_type,
            )
            old_properties['primary_keys'] = new_pks  # type:ignore

        # VERY UGLY SHOULD BE REMOVED WHEN WE HAVE PROTECTED TYPE
        previous_fields = parent_schema.type().children()
        if 'data' in previous_fields.keys():
            previous_fields['data'] = new_type.data_type()
            new_type = sdt.Struct(fields=previous_fields)
        return schema(
            self.dataset,
            schema_type=new_type,
            protected_paths=parent_schema.protobuf().protected,
            properties=old_properties,
            name=self.dataset.properties().get(DATASET_SLUGNAME, None),
        )

    async def to_arrow(
        self, batch_size: int
    ) -> t.AsyncIterator[pa.RecordBatch]:

        schema = await self.dataset.manager().async_schema(
            dataset=self.dataset
        )
        parent_schema = await self.parent_schema()

        async def async_generator(
            parent_iter: t.AsyncIterator[pa.RecordBatch],
        ) -> t.AsyncIterator[pa.RecordBatch]:
            async for batch in parent_iter:
                # TODO: what follows is really ugly and is necessary
                # because we do not have a proper type for the
                # protected entity, it will be removed when we
                # switch to that formalism

                array = convert_record_batch(
                    record_batch=batch, _type=parent_schema.type()
                )
                # VERY UGLY SHOULD BE REMOVED WHEN WE HAVE PROTECTED TYPE
                if 'data' in parent_schema.type().children():
                    old_arrays = array.flatten()
                    array = array.field('data')
                    updated_array, filter_indices = select_rows(
                        schema.data_type(),
                        array,
                    )
                    old_arrays[0] = updated_array
                    new_struct = pa.StructArray.from_arrays(
                        old_arrays,
                        names=list(parent_schema.type().children().keys()),
                    )
                    yield pa.RecordBatch.from_struct_array(
                        new_struct.filter(filter_indices)
                    )
                else:
                    updated_array, filter_indices = select_rows(
                        schema.data_type(),
                        array,
                    )
                    yield pa.RecordBatch.from_struct_array(
                        updated_array.filter(filter_indices)
                    )

        return async_generator(
            parent_iter=await self.parent_to_arrow(batch_size=batch_size)
        )
