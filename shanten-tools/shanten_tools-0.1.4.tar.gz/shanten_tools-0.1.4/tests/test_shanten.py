from shanten_tools import shanten

def test_churen():
    hand = [
        3,1,1,1,1,1,1,1,3,
        0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0]
    assert shanten(hand) == 0

    hand = [
        3,1,1,1,2,1,1,1,3,
        0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0]
    assert shanten(hand) == -1

def test_tenpai():
    hand = [
        0,1,1,1,1,1,0,0,0,
        0,0,0,1,1,1,2,0,0,
        0,0,0,0,0,0,1,1,1,
        0,0,0,0,0,0,0]
    assert shanten(hand) == 0

    hand = [
        0,0,0,0,0,0,3,1,0,
        0,0,0,1,1,1,0,0,0,
        0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,3,0]
    assert shanten(hand) == 0

def test_1shanten():
    hand = [
        0,1,1,1,1,1,0,0,0,
        0,0,0,1,1,1,2,0,0,
        0,0,0,0,0,0,1,1,0,
        1,0,0,0,0,0,0]
    assert shanten(hand) == 1

def test_perfect_1shanten():
    hand = [
        0,1,1,1,1,1,0,0,0,
        0,0,0,1,1,1,2,0,0,
        0,0,0,0,0,0,2,1,0,
        0,0,0,0,0,0,0]
    assert shanten(hand) == 1

def test_2shanten():
    hand = [
        0,1,1,1,1,1,0,0,0,
        0,0,0,1,1,0,2,0,0,
        0,0,0,0,0,0,2,1,0,
        1,0,0,0,0,0,0]
    assert shanten(hand) == 2
