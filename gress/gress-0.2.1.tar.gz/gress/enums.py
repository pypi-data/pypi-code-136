#  Created byMartin.cz
#  Copyright (c) Martin Strohalm. All rights reserved.

# default bars
DEFAULT_BAR = "{count} of {max} ({percent}%) {bar} {timer} | {speed}/s | ETA {autoeta}"
DEFAULT_BAR_NOMAX = "{count} {bar} {timer} | {speed}/s"

# available progress properties used by template widget
PROPS = ("current", "minimum", "maximum", "percent", "elapsed", "finished")

# prefixes used for value scaling
PREFIXES = ("", "k", "M",  "G",  "T",  "P",  "E",  "Z",  "Y")

# characters used for animated widget
ARROW = "→↘↓↙←↖↑↗"
CIRCLE = " .oO"
DOTS = " ⡀⡄⡆⡇⣇⣧⣷⣿"
FADE = " ░▒▓█"
LINE = "⎽⎼⎻⎺⎻⎼"
MOON = "◑◒◐◓"
PIE = "○◔◑◕●"
PIXEL = "⣾⣷⣯⣟⡿⢿⣻⣽"
HBAR = " ▏▎▍▌▋▊▉█"
SNAKE = " ▖▌▛█"
STAR = "-\\|/"
VBAR = " ▁▂▃▄▅▆▇█"

# special characters
LINE_UP = "\033[1A"
LINE_CLEAR = "\x1b[2K"
NA = "N/A"

# define time portions
MINUTE = 60
HOUR = 60 * MINUTE
DAY = 24 * HOUR

# define time templates
TIME_NA = NA
TIME_ABS = "%Y-%m-%d %H:%M:%S"

TIME_DHMS = "{d}:{h:02}:{m:02}:{s:02}"
TIME_HMS = "{h:02}:{m:02}:{s:02}"
TIME_MS = "{m:02}:{s:02}"
TIME_S = "{s}"

TIME_DHMS_U = "{d}d {h}h {m}m {s}s"
TIME_HMS_U = "{h}h {m}m {s}s"
TIME_MS_U = "{m}m {s}s"
TIME_S_U = "{s}s"
