from import_all_defs import import_all_defs


def test_load_all_defs():
    defs = import_all_defs(load_defs=True)
    assert len(defs) > 0
    assert type(defs) == dict
    # Test that functions were loaded
    funcs = defs.get("functions")
    assert funcs
    for key, definition in funcs.items():
        assert hasattr(definition, "__call__")


def test_find_all_defs():
    defs = import_all_defs(load_defs=False)
    assert len(defs) > 0
    assert type(defs) == dict
    # Test that definition paths were returned
    funcs = defs.get("functions")
    assert funcs
    for key, definition in funcs.items():
        assert type(definition) == str
