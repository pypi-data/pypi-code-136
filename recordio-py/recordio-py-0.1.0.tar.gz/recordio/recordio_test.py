import os

import pytest

from recordio import recordio


def test_recordio_reader(tmp_path):
    file_name = os.path.join(tmp_path, "data.recordio")
    expected_record = "Hello, World!"
    with open(file_name, "wb") as f:
        w = recordio.Writer(f)
        w.write(expected_record)

    with open(file_name, "rb") as f:
        r = recordio.Reader(f)
        record = r.next()

        assert record == expected_record

        with pytest.raises(EOFError):
            r.next()


def test_recordio_scanner(tmp_path):
    file_name = os.path.join(tmp_path, "data.recordio")
    expected_records = [
        "Hello, World!",
        "\n",
        "",
        "foo",
    ]
    with open(file_name, "wb") as f:
        w = recordio.Writer(f)
        for record in expected_records:
            w.write(record)

    with open(file_name, "rb") as f:
        s = recordio.Scanner(f)
        records = list(s.scan())

        assert records == expected_records
