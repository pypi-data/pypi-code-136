from fa_purity import (
    JsonValue,
)
from fa_purity.frozen import (
    freeze,
)
from fa_singer_io.singer.state.core import (
    SingerState,
)
from fa_singer_io.singer.state.decoder import (
    build_state,
)
from fa_singer_io.singer.state.encode import (
    encode_state,
)


def test_inverse() -> None:
    state = SingerState(
        freeze({"state": JsonValue("some state")}),
    )
    assert state == build_state(encode_state(state)).unwrap()
