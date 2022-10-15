#Imports
from os import system as execc
from math import modf

#Color codes
__cblack = "\u001b[30m"
__cred = "\u001b[31m"
__cgreen = "\u001b[32m"
__cyellow = "\u001b[33m"
__cblue = "\u001b[34m"
__cmagenta = "\u001b[35m"
__ccyan = "\u001b[36m"
__cwhite = "\u001b[37m"
__cgray = "\u001b[0;90m"
__cbgblack = "\u001b[40m"
__cbgred = "\u001b[41m"
__cbggreen = "\u001b[42m"
__cbgyellow = "\u001b[43m"
__cbgblue = "\u001b[44m"
__cbgmagenta = "\u001b[45m"
__cbgcyan = "\u001b[46m"
__cbgwhite = "\u001b[47m"
__cbggray = "\u001b[0;100m"
__sbold = "\u001b[1m"
__sitalic = "\u001b[3m"
__sunderlined = "\u001b[4m"
__sinverted = " \u001b[7m"
__endcolor = "\u001b[0m"

#RGB
def rgb(r, g, b, text): 
    """
    Takes 4 values, the red, the blue, the green and the text. The color is based on what rgb you inputed.
    """
    execc('')
    return f"\u001b[38;2;{r};{g};{b}m{text}{__endcolor}"

def bgrgb(r, g, b, text): 
    """
    Same thing as rgb(r, g, b, text) but it colors the background instead.
    """
    execc('')
    return f"\u001b[48;2;{r};{g};{b}m{text}{__endcolor}"

#Hex
def hex(hex: str, text):
    """
    Takes a hex code and a text, converts it to rgb and uses the existing rgb function in this library.
    """
    execc('')
    try:
        RGBHEX = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        hexcode = hex.replace('#', '').casefold()
        hexr = int(RGBHEX.index(hexcode[0]))*16
        hexr += int(RGBHEX.index(hexcode[1]))
        hexg = int(RGBHEX.index(hexcode[2]))*16
        hexg += int(RGBHEX.index(hexcode[3]))
        hexb = int(RGBHEX.index(hexcode[4]))*16
        hexb += int(RGBHEX.index(hexcode[5]))
        return rgb(hexr, hexg, hexb, text)
    except IndexError:
        raise Exception(red(underlined('Uh oh, invalid hex code...')))
    except ValueError:
        raise Exception(red(underlined('Uh oh, invalid hex code...')))
    except TypeError:
        raise Exception(red(underlined('Hex code can\'t be an actual hexdecimal input. Why? This is due to how the code works.')))

def bghex(hex: str, text):
    """
    Same thing as hex(hex, text) but it colors the background instead.
    """
    try:
        RGBHEX = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        hexcode = hex
        hexr = int(RGBHEX.index(hexcode[0]))*16
        hexr += int(RGBHEX.index(hexcode[1]))
        hexg = int(RGBHEX.index(hexcode[2]))*16
        hexg += int(RGBHEX.index(hexcode[3]))
        hexb = int(RGBHEX.index(hexcode[4]))*16
        hexb += int(RGBHEX.index(hexcode[5]))
        return bgrgb(hexr, hexg, hexb, text)
    except IndexError:
        raise Exception(red(underlined('Uh oh, invalid hex code...')))
    except ValueError:
        raise Exception(red(underlined('Uh oh, invalid hex code...')))
    except TypeError:
        raise Exception(red(underlined('Hex code can\'t be an actual hexadecimal input. Why? This is due to how the code works.')))

#Color Functions

def black(text):
    execc('')
    return f"{__cblack}{text}{__endcolor}"

def red(text):
    execc('')
    return f"{__cred}{text}{__endcolor}"

def green(text):
    execc('')
    return f"{__cgreen}{text}{__endcolor}"

def yellow(text):
    execc('')
    return f"{__cyellow}{text}{__endcolor}"

def blue(text):
    execc('')
    return f"{__cblue}{text}{__endcolor}"

def magenta(text):
    execc('')
    return f"{__cmagenta}{text}{__endcolor}"

def cyan(text):
    execc('')
    return f"{__ccyan}{text}{__endcolor}"

def white(text):
    execc('')
    return f"{__cwhite}{text}{__endcolor}"

def gray(text):
    execc('')
    return f"{__cgray}{text}{__endcolor}"

def grey(text):
    return gray(text)

def brightblack(text):
    return gray(text)

def lightblack(text):
    return gray(text)

def rainbowtext(text):
    """
    Enjoy I guess
    """
    exec('')
    formedstr = ''
    i = 0
    for char in text:
        if char in ' \t\n': continue
        mi = i%7
        if mi == 0:
            formedstr += hex('f33444', char)
        elif mi == 1:
            formedstr += hex('ff8901', char)
        elif mi == 2:
            formedstr += hex('fad716', char)
        elif mi == 3:
            formedstr += hex('00ba70', char)
        elif mi == 4:
            formedstr += hex('00c0dd', char)
        elif mi == 5:
            formedstr += hex('00408a', char)
        elif mi == 6:
            formedstr += hex('5e2779', char)
        i+=1
    return formedstr

#Background colors

def bgblack(text):
    execc('')
    return f"{__cbgblack}{text}{__endcolor}"

def bgred(text):
    execc('')
    return f"{__cbgred}{text}{__endcolor}"

def bggreen(text):
    execc('')
    return f"{__cbggreen}{text}{__endcolor}"

def bgyellow(text):
    execc('')
    return f"{__cbgyellow}{text}{__endcolor}"

def bgblue(text):
    execc('')
    return f"{__cbgblue}{text}{__endcolor}"

def bgmagenta(text):
    execc('')
    return f"{__cbgmagenta}{text}{__endcolor}"

def bgcyan(text):
    execc('')
    return f"{__cbgcyan}{text}{__endcolor}"

def bgwhite(text):
    execc('')
    return f"{__cbgwhite}{text}{__endcolor}"

def bggray(text):
    execc('')
    return f"{__cbggray}{text}{__endcolor}"

def bggrey(text):
    return bggray(text)

def bgbrightblack(text):
    return bggray(text)

def bglightblack(text):
    return bggray(text)

#Style/Look
def bold(text):
    """
    Makes your text bold.
    """
    execc('')
    return f"{__sbold}{text}{__endcolor}"

def italic(text):
    """
    Makes your text italic.
    """
    execc('')
    return f"{__sitalic}{text}{__endcolor}"

def underlined(text):
    """
    Shows a line under your text.
    """
    execc('')
    return f"{__sunderlined}{text}{__endcolor}"

def inverted(text):
    """
    I can't explain this, just try it and see what it looks like for you.
    """
    execc('')
    return f"{__sinverted}{text}{__endcolor}"
