import sys

if sys.platform == "win32":
    from windows import Listener as Listener
elif sys.platform == "darwin":
    from macos import Listener as Listener
else:
    raise NotImplementedError("bedtime is not implemented for this platform")