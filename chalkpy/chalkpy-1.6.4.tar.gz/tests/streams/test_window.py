from pydantic import BaseModel

from chalk import realtime
from chalk.features import Features, features
from chalk.streams import KafkaSource
from chalk.streams.windows import Windowed, windowed


@features
class StreamFeatures:
    scalar_feature: Windowed[str] = windowed("10m")
    uid: str


class KafkaMessage(BaseModel):
    val_a: str


s = KafkaSource(message=KafkaMessage)


@realtime
def fn(x: StreamFeatures.scalar_feature) -> Features[StreamFeatures.uid]:
    pass


def test_window_definition():
    pass
