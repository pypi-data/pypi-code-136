from fish_exposer import cleanhtml

def test_unitSimple():
    text1 = "<p>U.S. wild-caught</p>"
    text1_clean = "U.S. wild-caught"
    assert cleanhtml(text1) == text1_clean


def test_unitSlashN():
    text1 = "<p>U.S. wild-caught</p>\n"
    text1_clean = "U.S. wild-caught\n"
    assert cleanhtml(text1) == text1_clean

def test_unitComplex():
    text1 = "<p>The meat is pinkish with yellow tones when raw and turns somewhat lighter when cooked. Red snapper have trademark red skin and red eyes and come from domestic fisheries. To aid in identification, they are usually sold with the skin on.</p>\n"
    text1_clean = "The meat is pinkish with yellow tones when raw and turns somewhat lighter when cooked. Red snapper have trademark red skin and red eyes and come from domestic fisheries. To aid in identification, they are usually sold with the skin on.\n"
    assert cleanhtml(text1) == text1_clean
