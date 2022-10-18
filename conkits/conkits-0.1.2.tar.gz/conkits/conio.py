from time import time
from sys import platform, stdin
from .csi import Fore, Back, Style, Cursor, CSI, RESET_ALL


if platform == 'win32':
    import msvcrt
else:
    import termios
    import select
    import tty


ERROR_CSI_STR = Fore.LIGHTRED


class Consoleio:

    CSI = '\033['
    RESET_ALL = '\033[0m'

    def __init__(self):
        if platform == 'win32':
            self.platform = 'win32'
        elif platform == 'linux':
            self.platform = 'linux'
        else:
            self.platform = 'unknow'

        self.fore = Fore
        self.back = Back
        self.style = Style
        self.cursor = Cursor

        self.f = self.fore
        self.b = self.back
        self.s = self.style
        self.c = self.cursor

    """同前面，带s后缀的返回字符串，不带的直接执行"""
    def erase_line_s(self, mode=2):
        """
        有3种模式（如果缺失该参数则认为是模式0，这里我默认选择模式2）
        模式0：清除光标到该行行尾之间的部分
        模式1：清除光标到改行行首之间的部分
        模式2：清除整行
        """
        if mode < 0 or mode > 2:
            raise ValueError(ERROR_CSI_STR + f'清除行模式{mode}选择错误，需在范围0 - 2' + RESET_ALL)
        return CSI + f'{mode}K'

    def erase_display_s(self, mode=2):
        """
        共有4种模式（如果缺失该参数则认为是模式0，这里我默认选择模式2）
        模式0：清除光标位置到屏幕末尾的部分
        模式1：清除光标位置到屏幕开头的部分
        模式2：清除整个屏幕
        模式3：清除整个屏幕并且删除回滚区中所有行（某些终端可能不支持）
        """
        if mode < 0 or mode > 3:
            raise ValueError(ERROR_CSI_STR + f'清除屏幕模式{mode}选择错误，需在范围0 - 3' + RESET_ALL)
        return CSI + f'{mode}J'

    def clrscr_s(self):
        """仅清除屏幕，不重置之前的设置（如设置颜色样式等）"""
        return self.erase_display_s() + self.cursor.pos_s()

    def reset_to_init_s(self):
        """清除屏幕，并且重置之前的设置"""
        return '\033c'

    def erase_line(self, mode=2):
        if mode < 0 or mode > 2:
            raise ValueError(ERROR_CSI_STR + f'清除行模式{mode}选择错误，需在范围0 - 2' + RESET_ALL)
        print(CSI + f'{mode}K', end='', flush=True)

    def erase_display(self, mode=2):
        if mode < 0 or mode > 3:
            raise ValueError(ERROR_CSI_STR + f'清除屏幕模式{mode}选择错误，需在范围0 - 3' + RESET_ALL)
        print(CSI + f'{mode}J', end='', flush=True)

    def clrscr(self):
        self.erase_display()
        self.cursor.pos()

    def reset_to_init(self):
        print('\033c', end='')

    def 擦除行(self, mode):
        return self.erase_line(mode)

    def 擦除显示(self, mode):
        return self.erase_display(mode)

    def 清屏(self):
        return self.clrscr()

    def 重置所有(self):
        return self.reset_to_init()

    def getch(self):
        """同c语言的getch()"""
        if self.platform == 'win32':
            return self.__getch_msvcrt()
        elif self.platform == 'linux':
            return self.__getch_termios()
        elif self.platform == 'unknow':
            return self.__getch_termios()

    def kbhit(self):
        """同c语言的kbhit()"""
        if self.platform == 'win32':
            return self.__kbhit_msvcrt()
        elif self.platform == 'linux':
            return self.__kbhit_termios()
        elif self.platform == 'unknow':
            return self.__kbhit_termios()

    def get_csistr(self, *kwargs):
        """
        :param kwargs: 任意数量的Fore, Back, Style参数，实际类型为int
        :return: 返回整理好的csi字符串
        """
        format_str = '\033['
        for arg in kwargs:
            if not 0 <= arg <= 9 and arg != 5 and arg != 6:
                pass
            elif not 30 <= arg <= 49:
                pass
            elif not 90 <= arg <= 107:
                raise ValueError(ERROR_CSI_STR + '所给参数不格式控制代码范围内' + RESET_ALL)
            format_str += str(arg) + ';'
        return format_str[:-1] + 'm'

    def 获取csi字符串(self, *kwargs):
        return self.get_csistr(*kwargs)

    def paket_str(self, text, *kwargs):
        """
        :param text: 要包装的字符串，或其他可以被str()调用的类型
        :param kwargs: 任意数量的Fore, Back, Style参数，实际类型为int
        :return: 返回整理好的csi字符串，并在尾部自动附上\033[0m
        """
        if not isinstance(text, str):
            text = str(text)
        return self.get_csistr(*kwargs) + text + RESET_ALL

    def 包装字符串(self, text, *kwargs):
        return self.paket_str(text, *kwargs)

    def interruptible_sleep(self, delay, *break_char_set, case_insensitive=False):
        """
        可打断的sleep
        :param: delay 延时时长（单位秒）
        :param: break_char_set 为触发打断按键字符列表，留空即为任意键打断
        :param: case_insensitive 大小写敏感开关
        """
        if case_insensitive:
            temp = [char.lower() for char in break_char_set]
            break_char_set = tuple(set(temp))
        start = time()
        while (time() - start) < delay:
            ch = self.kbhit()
            if len(break_char_set) == 0:
                if ch is not None:
                    return ch
            else:
                if not case_insensitive and ch is not None:
                    ch = ch.lower()
                if ch in break_char_set:
                    return ch

    def 可打断的sleep(self, delay, *break_char_set):
        return self.interruptible_sleep(delay, *break_char_set)

    def __getch_msvcrt(self):
        return msvcrt.getch().decode('utf-8')

    def __getch_termios(self):
        fd = stdin.fileno()
        old = termios.tcgetattr(fd)
        new = termios.tcgetattr(fd)
        new[3] = new[3] & ~termios.ECHO & ~termios.ICANON
        try:
            termios.tcsetattr(fd, termios.TCSADRAIN, new)
            char = stdin.read(1)
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
            return char
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)

    def __kbhit_msvcrt(self):
        if msvcrt.kbhit():
            return self.__getch_msvcrt()

    def __kbhit_termios(self):
        old_settings = termios.tcgetattr(stdin)
        tty.setcbreak(stdin.fileno())
        if select.select([stdin], [], [], 0) == ([stdin], [], []):
            c = stdin.read(1)
            termios.tcsetattr(stdin, termios.TCSADRAIN, old_settings)
            return c
        termios.tcsetattr(stdin, termios.TCSADRAIN, old_settings)


Conio = Consoleio()
