
'''

颜色助手

'''
import logging
import os
import random
class Color:
    Black = 0
    Red = 1
    Green = 2
    Yellow = 3
    Blue = 4
    Magenta = 5
    Cyan = 6
    White = 7

class Mode:

    Foreground = 30
    Background = 40
    ForegroundBright = 90
    BackgroundBright = 100
    def __init__(self):
        pass
        # self.Foreground = 30
        # self.Background = 40
        # self.ForegroundBright = 90
        # self.BackgroundBright = 100
    @staticmethod
    def tcolor(c, m=30):
        return '\033[{}m'.format(m + c)

    @staticmethod
    def treset():
        return '\033[0m'
class Logger:
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(format=LOG_FORMAT, filename='selenium.log',
                        filemode="w")
    @staticmethod
    def error(msg,end='\n'):
        os.system('')
        print(Mode.tcolor(Color.Red, Mode.ForegroundBright) + str(msg) + Mode.treset(),end)
        logging.error(msg)

    @staticmethod
    def info(msg,end='\n'):
        os.system('')
        print(Mode.tcolor(Color.Blue, Mode.ForegroundBright) + str(msg) + Mode.treset(),end=end)
        logging.info(msg)
    @staticmethod
    def warning(msg,end='\n'):
        os.system('')
        print(Mode.tcolor(Color.Yellow, Mode.Background) + str(msg) + Mode.treset())
        logging.warning(msg)
    @staticmethod
    def randlog(msg,end='\n'):
        os.system('')
        background=[Mode.Background,Mode.BackgroundBright,Mode.ForegroundBright,Mode.Foreground]
        color=[Color.Green,Color.Yellow,Color.Red,Color.Blue,Color.Cyan,Color.White,Color.Magenta]
        print(Mode.tcolor(random.choice(color), random.choice(background)) + str(msg) + Mode.treset(),end)
        logging.info(msg)
if __name__ == '__main__':
    Logger.error('HELLO')
    Logger.info('HELLO')
    Logger.warning('HELLO')
    Logger.randlog('HELLO')
