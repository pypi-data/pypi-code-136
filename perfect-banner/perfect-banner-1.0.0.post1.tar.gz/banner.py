__author__ = "phoenixR"
__version__ = "1.0.0.post1"

from os import get_terminal_size

def choose(
    *texts: str,
    width: bool = True,
    height: bool = False
) -> str:
    """
    Chooses the text that fits the terminal size the best.
    
    Parameters
    ----------
    *texts
        May be multiline strings with different sizes
    
    width
        Take into account of the terminal width?
        Default: True
    
    height
        Take into account of the terminal height?
        Default: False
    
    Returns
    -------
    The string that fits the terminal size the best.
    
    """
    assert width or height, "one of width and height must be set to True"
    
    def get_max_width(text):
        if not text:
            return 0
        return len(max(text.splitlines(), key = len))
    
    def get_max_height(text):
        if not text:
            return 1
        return len(text.splitlines())
    
    def get_max_size(text):
        return get_max_width(text), get_max_height(text)
    try:
        twidth, theight = get_terminal_size()
    except OSError:
        twidth, theight = 80, 80
    use = (get_max_size(""), "") # ((max width, max height), text)
    might_use = use
    
    for text in texts:
        w, h  = get_max_size(text)
        passed_w = passed_h = True
        
        if width:
            passed_w = False
            if use[0][0] < w <= twidth:
                might_use = (get_max_size(text), text)
                passed_w = True
        
        if height:
            passed_h = False
            if use[0][1] < h <= theight:
                might_use = (get_max_size(text), text)
                passed_h = True
        
        if passed_w and passed_h:
            use = might_use
    
    return use[1]
