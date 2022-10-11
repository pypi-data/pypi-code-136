"""Miscallaneous utility functionality."""
import io
import typing

from harper.audio.signal import Signal


# TODO: interleave should be generic. takes multiple iterables and a step size.
# takes a step of iterable1, step of iterable2, etc.

# TODO: implement in C
def interleave_signals(signals: typing.List[Signal]) -> Signal:
    """Combine two signals into one.

    Opposite of window. Takes two things and smushes them together,
    in alternating capacity. Primarily a zip with some flavor added in.

    Parameters
    ----------
    signals : harper.misc.signal.Signals
        A list of signals to be interleaved.

    Returns
    -------
    Signal
        A harper Signal object
    """
    source = dict()
    new = list()

    for idx, element in enumerate(signals):
        source[idx] = dict()
        x = element.reversed_timeseries
        source[idx]["data"] = x

    def keep_going(source):
        for signal in source.values():
            if signal["data"] != list():
                return True
        return False

    n_channels = len(source)
    current_signal = 0
    done = False
    while not done:
        try:
            add_me = source[current_signal]["data"].pop()
        except IndexError:
            add_me = 0
        new.append(add_me)
        current_signal += 1
        if current_signal >= n_channels:
            current_signal = 0
            if not keep_going(source):
                done = True
    return Signal.from_timeseries(new)


# TODO: implement in C
def interleave_bytes(signals, style="pad"):
    """Combine two byte strings into one.

    Opposite of window. Takes two things and smushes them together,
    in alternating capacity. Primarily a zip with some flavor added in.

    Parameters
    ----------
    signals : harper.misc.signal.Signals
        A list of signals to be interleaved.

    Returns
    -------
    bytes
        An interleaved byte string.
    """
    source = dict()
    new = list()

    for idx, element in enumerate(signals):
        source[idx] = dict()
        x = io.BytesIO(element.reversed_bytes)
        source[idx]["data"] = x
        source[idx]["width"] = element.minimum_bytes

    def keep_going(source):
        for signal in source.values():
            if signal["data"].tell() < len(signal["data"].getvalue()):
                return True
        return False

    n_channels = len(source)
    current_signal = 0
    while keep_going(source):
        add_me = source[current_signal]["data"].read(
            source[current_signal]["width"]
        )
        while len(add_me) < source[current_signal]["width"]:
            add_me = add_me + b" "
        new.append(add_me)
        current_signal += 1
        if current_signal >= n_channels:
            current_signal = 0
    return new
