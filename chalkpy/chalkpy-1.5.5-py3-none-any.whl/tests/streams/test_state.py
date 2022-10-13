from pydantic import BaseModel

from chalk.features import features
from chalk.streams import KafkaSource, State, stream


@features
class StreamFeatures:
    scalar_feature: str


class KafkaMessage(BaseModel):
    val_a: str


s = KafkaSource(message=KafkaMessage)


@stream
def fn(message: KafkaMessage, total: State[int]):
    total.update(4)
    return StreamFeatures(
        scalar_feature=message.val_a,
    )


def test_state_works():
    total = State[int]
    assert total.kind == int
    initial_state = State[int](2)
    assert initial_state.value == 2
    fn(KafkaMessage(val_a="3"), initial_state)
    assert initial_state.value == 4
