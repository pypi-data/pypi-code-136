from typing import Dict,Any
default_rcparams:Dict[str,Any] = None
def init_rcparams():
    global default_rcparams
    import matplotlib
    from yagamee.yagamee_rcparams import yagamee_rcparams
    default_rcparams = dict(matplotlib.rcParams)
    matplotlib.rcParams.update(yagamee_rcparams)

def restore_rcparams():
    import matplotlib
    matplotlib.rcParams.update(default_rcparams)

def init_matplotlib():
    init_rcparams()
    import japanize_matplotlib
