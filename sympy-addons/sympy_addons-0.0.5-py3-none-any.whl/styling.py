import re


def apply_style(target, style):
    pattern = '\%([0-9]+)(\[?[0-9]*\]?)'
    place_holders = re.findall(pattern, style)
    style = re.sub(pattern, '%s', style)
    if type(target) == type(type):
        func = lambda self, printer: style % (self.args[int(i)] for i in place_holders)
    else:
        func = lambda printer: style % (target.args[int(i)] for i in place_holders)
    target._latex = func
