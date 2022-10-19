from loading_display import spinner


def test_next_spinner_frame():
    s = spinner()
    expected_frames = ["\u25DC ", " \u25DD", " \u25DE", "\u25DF "]
    actual_frames = [next(s), next(s), next(s), next(s)]
    assert expected_frames == actual_frames
