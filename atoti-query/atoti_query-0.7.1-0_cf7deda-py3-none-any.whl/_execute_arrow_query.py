import json
from http import HTTPStatus
from typing import Any, Mapping
from urllib.request import Request, urlopen

import pandas as pd
import pyarrow as pa
from atoti_core import EMPTY_MAPPING

from ._arrow_to_pandas import arrow_to_pandas


def execute_arrow_query(
    url: str, *, data: Mapping[str, Any], headers: Mapping[str, str] = EMPTY_MAPPING
) -> pd.DataFrame:
    headers = {**headers, "Content-Type": "application/json"}
    request = Request(
        url, method="POST", headers=headers, data=json.dumps(data).encode("utf-8")
    )

    with urlopen(request) as response:  # nosec
        if response.status != HTTPStatus.OK:
            try:
                # Try to get the first error of the chain if it exists.
                error = RuntimeError(
                    f"Query failed: {json.loads(response)['error']['errorChain'][0]}"
                )
            except Exception:  # pylint: disable=broad-except
                error = RuntimeError(response.content)
            raise error
        record_batch_stream = pa.ipc.open_stream(response)
        schema = record_batch_stream.schema
        for name in schema.names:
            schema.field(name).with_nullable(True)
        table = pa.Table.from_batches(record_batch_stream, schema=schema)

    return arrow_to_pandas(table)
