from fa_purity import (
    JsonValue,
)
from fa_purity.cmd import (
    unsafe_unwrap,
)
from fa_purity.frozen import (
    freeze,
)
from fa_singer_io.singer.record.decoder import (
    build_record,
)
from fa_singer_io.singer.record.encode import (
    encode_record,
)
from fa_singer_io.singer.record.factory import (
    new_record_auto_time,
)


def test_inverse() -> None:
    record = unsafe_unwrap(
        new_record_auto_time(
            "test_stream",
            freeze({"data": JsonValue(123)}),
        )
    )
    assert record == build_record(encode_record(record)).unwrap()
