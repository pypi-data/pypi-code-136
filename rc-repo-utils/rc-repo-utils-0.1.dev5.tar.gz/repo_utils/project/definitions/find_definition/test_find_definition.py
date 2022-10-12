from find_definition import find_definition


def test_find_definition():
    path = find_definition("define")
    assert "repo_utils" in path

    path = find_definition("TestObj")
    assert "repo_utils" in path

    path = find_definition("TestObj", namespace="functions")
    assert path is None

    path = find_definition("TestObj", containing_folder=find_definition('find_definition'))
    assert path is None