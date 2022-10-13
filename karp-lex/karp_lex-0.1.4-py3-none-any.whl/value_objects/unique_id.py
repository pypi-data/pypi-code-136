from typing import Optional
import uuid

import ulid
import ulid.codec

UniqueId = uuid.UUID


def make_unique_id(t: Optional[ulid.codec.TimestampPrimitive] = None) -> UniqueId:
    """Generate an UniqueId that are sortable.

    >>> from karp_lex.value_objects import make_unique_id
    >>> from datetime import datetime
    >>> old_id = make_unique_id(datetime(1999,12,31,23,59,59))
    >>> make_unique_id() > old_id
    True
    """
    return ulid.new().uuid if t is None else ulid.from_timestamp(t).uuid
