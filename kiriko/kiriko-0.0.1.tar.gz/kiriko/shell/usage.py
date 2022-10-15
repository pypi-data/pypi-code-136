from time import ctime

from kiriko import __version__


def run():
    cur_time = ctime()
    text = f"""
    # kiriko
    
    version {__version__} ({cur_time} +0800)
    """
    print(text)
