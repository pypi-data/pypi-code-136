from dataclasses import dataclass
from typing import List

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
class GenerateRequest(betterproto.Message):
    quantity: int = betterproto.uint64_field(1)
    dry: bool = betterproto.bool_field(2)


@dataclass(eq=False, repr=False)
class GeneratedPost(betterproto.Message):
    id: str = betterproto.string_field(1)
    content: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class GenerateResponse(betterproto.Message):
    post: "GeneratedPost" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class RealPost(betterproto.Message):
    content: str = betterproto.string_field(1)
    score: float = betterproto.double_field(2)


@dataclass(eq=False, repr=False)
class FitPostsRequest(betterproto.Message):
    post: "RealPost" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class FitPostsResponse(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class PostScore(betterproto.Message):
    id: str = betterproto.string_field(1)
    score: float = betterproto.double_field(2)


@dataclass(eq=False, repr=False)
class FitScoresRequest(betterproto.Message):
    scores: List["PostScore"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class FitScoresResponse(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class StepRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class StepResponse(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class MetricConfig(betterproto.Message):
    id: str = betterproto.string_field(1)
    label: str = betterproto.string_field(2)
    group: str = betterproto.string_field(3)
    config: str = betterproto.string_field(4)


@dataclass(eq=False, repr=False)
class GetMetricsConfigRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class GetMetricsConfigResponse(betterproto.Message):
    configs: List["MetricConfig"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class WatchMetricsRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class WatchMetricsResponse(betterproto.Message):
    metric_id: str = betterproto.string_field(1)
    dataset_id: int = betterproto.uint64_field(2)
    data: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class ResetRequest(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class ResetResponse(betterproto.Message):
    pass
