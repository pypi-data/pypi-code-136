import string

from .api import hexacolor, rgb, cmyk
from .str import stringcolor

a = list(string.ascii_letters)

def autodetect(args:str) -> str:

    if args[0] == '#':

        hexacolor(args)
    
    elif args[0] in a:

        stringcolor(args)

    elif args.count(',') == 2:

        print(rgb(args))
    
    elif args.count(',') == 3:

        cmyk(args)
