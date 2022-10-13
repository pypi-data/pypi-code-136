from typing import Optional
import uuid

import ulid
import ulid.codec

UniqueId = uuid.UUID


def make_unique_id(t: Optional[ulid.codec.TimestampPrimitive] = None) -> UniqueId:
    return ulid.new().uuid if t is None else ulid.from_timestamp(t).uuid
