from dataclasses import dataclass
from datetime import datetime
from typing import Optional

import betterproto


class Status(betterproto.Enum):
    STATUS_UNSPECIFIED = 0
    STATUS_LOADING = 1
    STATUS_READY = 2


@dataclass(eq=False, repr=False)
class GetMetadataRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class GetMetadataResponse(betterproto.Message):
    key: str = betterproto.string_field(1)
    description: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class GetPostSchemaRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class GetPostSchemaResponse(betterproto.Message):
    schema: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class GetStatusRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class GetStatusResponse(betterproto.Message):
    status: "Status" = betterproto.enum_field(1)


@dataclass(eq=False, repr=False)
class WatchStatusRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class WatchStatusResponse(betterproto.Message):
    status: "Status" = betterproto.enum_field(1)


@dataclass(eq=False, repr=False)
class GetConfigSchemaRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class GetConfigSchemaResponse(betterproto.Message):
    schema: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class GetConfigRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class GetConfigResponse(betterproto.Message):
    config: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class WatchConfigRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class WatchConfigResponse(betterproto.Message):
    config: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class SetConfigRequest(betterproto.Message):
    config: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class SetConfigResponse(betterproto.Message):
    config: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class GeneratedPost(betterproto.Message):
    content: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class PostRequest(betterproto.Message):
    post: "GeneratedPost" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class PostResponse(betterproto.Message):
    post_id: str = betterproto.string_field(1)
    post_url: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class ScoreRequest(betterproto.Message):
    post_id: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class ScoreResponse(betterproto.Message):
    score: float = betterproto.double_field(1)


@dataclass(eq=False, repr=False)
class ScrapRequest(betterproto.Message):
    limit: Optional[int] = betterproto.uint64_field(
        1, optional=True, group="_limit"
    )
    before: Optional[datetime] = betterproto.message_field(
        2, optional=True, group="_before"
    )
    after: Optional[datetime] = betterproto.message_field(
        3, optional=True, group="_after"
    )


@dataclass(eq=False, repr=False)
class RealPost(betterproto.Message):
    id: str = betterproto.string_field(1)
    content: str = betterproto.string_field(2)
    score: float = betterproto.double_field(3)


@dataclass(eq=False, repr=False)
class ScrapResponse(betterproto.Message):
    post: "RealPost" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class ResetRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class ResetResponse(betterproto.Message):
    pass
