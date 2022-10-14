from pydantic import BaseModel

from chalk.features import features
from chalk.streams import KafkaSource, stream


@features
class StreamFeatures:
    scalar_feature: str


class KafkaMessage(BaseModel):
    val_a: str


s = KafkaSource(message=KafkaMessage)


@stream
def fn(message: s.Message):
    return StreamFeatures(
        scalar_feature=message.val_a,
    )


def test_callable():
    assert fn(KafkaMessage(val_a="hello")) == StreamFeatures(scalar_feature="hello")


def test_parsed_source():
    assert fn.source == s
