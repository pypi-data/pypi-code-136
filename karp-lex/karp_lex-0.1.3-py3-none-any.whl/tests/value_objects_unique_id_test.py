from datetime import datetime

from karp_lex.value_objects import make_unique_id


def test_unique_ids_are_sortable():
    assert make_unique_id() > make_unique_id(datetime(1999, 12, 31))
