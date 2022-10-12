from read_sheet import read_sheet

def test_read_sheet():
    data = read_sheet('', 0)
    assert data
