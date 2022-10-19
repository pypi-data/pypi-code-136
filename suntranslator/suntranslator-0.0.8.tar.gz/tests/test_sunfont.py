from tkinter import Tk, font

root = Tk()


def test_sunfont_exists():
    assert "SUN7_8_1210" in font.families()
