from shanten_tools import shanten
import numpy as np

def test_churen():
    hand = np.array([
        3,1,1,1,1,1,1,1,3,
        0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0], dtype=np.uint8)
    assert shanten(hand) == 0

    hand = np.array([
        3,1,1,1,2,1,1,1,3,
        0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,0,0], dtype=np.uint8)
    assert shanten(hand) == -1

def test_tenpai():
    hand = np.array([
        0,1,1,1,1,1,0,0,0,
        0,0,0,1,1,1,2,0,0,
        0,0,0,0,0,0,1,1,1,
        0,0,0,0,0,0,0], dtype=np.uint8)
    assert shanten(hand) == 0

    hand = np.array([
        0,0,0,0,0,0,3,1,0,
        0,0,0,1,1,1,0,0,0,
        0,0,0,0,0,0,0,0,0,
        0,0,0,0,0,3,0], dtype=np.uint8)
    assert shanten(hand) == 0

def test_1shanten():
    hand = np.array([
        0,1,1,1,1,1,0,0,0,
        0,0,0,1,1,1,2,0,0,
        0,0,0,0,0,0,1,1,0,
        1,0,0,0,0,0,0], dtype=np.uint8)
    assert shanten(hand) == 1

    hand = np.array([
        0,1,1,1,1,1,1,0,0,
        0,0,0,1,1,1,0,0,0,
        0,0,0,0,0,0,2,0,0,
        1,1,0,0,0,0,0], dtype=np.uint8)
    assert shanten(hand) == 1

def test_perfect_1shanten():
    hand = np.array([
        0,1,1,1,1,1,0,0,0,
        0,0,0,1,1,1,2,0,0,
        0,0,0,0,0,0,2,1,0,
        0,0,0,0,0,0,0], dtype=np.uint8)
    assert shanten(hand) == 1

def test_2shanten():
    hand = np.array([
        0,1,1,1,1,1,0,0,0,
        0,0,0,1,1,0,2,0,0,
        0,0,0,0,0,0,2,1,0,
        1,0,0,0,0,0,0], dtype=np.uint8)
    assert shanten(hand) == 2
