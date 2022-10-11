"""Preloaded Signal samples for ease of use."""

import os
from harper.io.wavfile import WavFile

RESOURCE_PATH = os.path.realpath(
    os.path.join(__file__, "..", "..", "resources")
)

THANK_GOD = WavFile(
    os.path.realpath(os.path.join(RESOURCE_PATH, "thank-god-its-friday.wav"))
)

KICKSOUND = WavFile(
    os.path.realpath(os.path.join(RESOURCE_PATH, "kicksound.wav"))
)


STEREO_16BIT_44100 = WavFile(
    os.path.realpath(os.path.join(RESOURCE_PATH, "stereo_16bit_44100hz.wav"))
)


MONO_16BIT_44100 = WavFile(
    os.path.realpath(
        os.path.join(RESOURCE_PATH, "1kHz_44100Hz_16bit_05sec.wav")
    )
)
