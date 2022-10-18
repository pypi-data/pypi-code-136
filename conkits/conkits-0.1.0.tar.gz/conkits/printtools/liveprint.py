import re
import time
from pprint import pprint
from collections import namedtuple
from csistring import CsiStringMethods
from conkits.conkits import Colors256, Fore, Back, Style, Cursor, Conio


FIND_CSI_PATTERN = re.compile('\033\\[.*?[a-zA-z]')


class LivePrint(CsiStringMethods):
    """用于动态打印的类"""
    def __init__(self, screen_wid=35,  print_delay=0.012, csi_code='', step=1, is_auto=True):
        super().__init__(screen_wid)
        self.__print_delay = self.__param_value_limits('print_delay', print_delay)  # 控制lprint打印速度
        self.__csi_code = '\033[0m' + self.__param_value_limits('csi_code', csi_code)  # 控制格式的csi控制代码
        self.__step = self.__param_value_limits('step', step)  # 每次打印增加的字符数量
        self.is_reset = False  # 每次打印完是否重置样式设置
        self.is_auto = is_auto  # 是否自动打印
        self.interrupt_char_list = None  # 打印时用于打断

    def set_csi_code(self, *kwargs):
        """设置csi代码"""
        self.__csi_code = '\033[0m'
        for arg in kwargs:
            if not isinstance(arg, str):
                arg = str(arg)
            self.__csi_code += arg

    def get_csi_code(self):
        return self.__csi_code

    def set_print_delay(self, print_delay):
        """设置打印延时，不能小于零"""
        self.__print_delay = 0 if print_delay < 0 else print_delay

    def get_print_delay(self):
        return self.__print_delay

    def set_step(self, step):
        """设置打印的步数，不能小于1，否则会进入死循环"""
        if not isinstance(step, int):
            step = int(step)
        self.__step = 1 if step <= 0 else step

    def get_step(self):
        return self.__step

    def lprint(self, *kwargs, csi_code=None, print_delay=None, step=None, sep=' ', end='\n', is_auto=None,
               is_reset=None, dict_info=None):
        """
        动态逐字打印字符串
        :param step: 每次打印增加的字符数量，如果默认则使用类里面的step变量
        :param kwargs: 任意数量的可以转成字符串的对象
        :param csi_code: 用于修改打印样式的csi控制代码，不能是光标控制代码，
                        如果默认则使用类里面的csi控制代码，否则使用单独设置的csi控制代码
        :param print_delay: 每次打印的延迟时间，如果默认则使用类里面的print_delay参数
        :param sep: 同print里面的sep
        :param end: 同print里面的end，默认为换行
        :param is_auto: 打印完之后是否需要等待确认
        :param is_reset: 打印完是否重置字符串中所设置的样式
        :param dict_info 直接由CsiStringMethod类中_sort_string返回的列表
        :return: None
        """
        if dict_info is not None:
            sorted_info_ls = dict_info
        else:
            # 拼接字符串
            input_string = ''
            if len(kwargs) > 1:
                for arg in kwargs:
                    if not isinstance(arg, str):
                        input_string += str(arg) + sep
                    else:
                        input_string += arg + sep
            else:
                if len(kwargs) == 0:
                    return print(end=end)
                    pass
                else:
                    input_string = kwargs[0]
            sorted_info_ls = self._sort_string(input_string)
        # 如果参数未赋值就给参数添加默认值
        csi_code = self.__csi_code if csi_code is None else csi_code
        print_delay = self.__print_delay if print_delay is None else self.__param_value_limits('print_delay', print_delay)
        step = self.__step if step is None else self.__param_value_limits('step', step)
        is_auto = self.is_auto if is_auto is None else is_auto
        is_reset = self.is_reset if is_reset is None else is_reset
        is_jump = False
        right = 0
        right_idx = 0
        left = right
        left_idx = right_idx
        # 定位right的位置 end=''
        prt_csi_code = csi_code if sorted_info_ls[left_idx]['csi'] == '' else sorted_info_ls[left_idx]['csi']
        print(prt_csi_code, end='')
        while left_idx < len(sorted_info_ls):
            right += step
            # 判断right加上步长超过当前字符串长度之后，right和right_idx会到达的位置
            if right_idx < len(sorted_info_ls):
                while right > sorted_info_ls[right_idx]['len']:
                    right -= sorted_info_ls[right_idx]['len']
                    right_idx += 1
                    if right_idx >= len(sorted_info_ls):
                        break
            if left_idx != right_idx and left_idx < len(sorted_info_ls):
                # 设置格式
                prt_csi_code = csi_code if sorted_info_ls[left_idx]['csi'] == '' else sorted_info_ls[left_idx]['csi']
                # 防止重复设置csi_code，特别是里面含有光标控制符时
                if sorted_info_ls[left_idx]['str'][left:] != '':
                    print(prt_csi_code, end='')
                    print(sorted_info_ls[left_idx]['str'][left:], end='')
                left_idx += 1
                while left_idx < right_idx and left_idx < len(sorted_info_ls):
                    prt_csi_code = csi_code if sorted_info_ls[left_idx]['csi'] == '' else sorted_info_ls[left_idx]['csi']
                    print(prt_csi_code, end='')
                    print(sorted_info_ls[left_idx]['str'], end='')
                    left_idx += 1
                if left_idx >= len(sorted_info_ls):
                    break
                if right_idx < len(sorted_info_ls):
                    prt_csi_code = csi_code if sorted_info_ls[right_idx]['csi'] == '' else sorted_info_ls[right_idx]['csi']
                    print(prt_csi_code, end='')
                    print(sorted_info_ls[right_idx]['str'][:right], end='')
                    left = right
            else:
                if sorted_info_ls[left_idx]['str'][left:right] == '':
                    continue
                print(sorted_info_ls[left_idx]['str'][left:right], end='')
                left = right
            if not is_jump:
                ch = Conio.interruptible_sleep(print_delay)
                if ch is not None:
                    is_jump = True
        # 打印完之后看是否需要换行
        if not is_auto:
            Conio.getch()
        if self.is_reset:
            print(Style.RESET_ALLs, end=end, flush=True)
        else:
            print(end=end)

    def pop_print_line(self, *kwargs, csi_code=None, print_delay=None, step=None, sep=' ', end='\n',
                       dict_info=None, limited_wid=None, indent=0):
        """
        临时性的弹出效果打印函数，基本用法和lprint一样，
        但是只能打印一行，所以不建议使用
        """
        limited_wid = self.get_scrwid() if limited_wid is None else limited_wid
        if dict_info is not None:
            str_info_list = dict_info
        else:
            # 拼接字符串
            input_string = ''
            if len(kwargs) > 1:
                for arg in kwargs:
                    if not isinstance(arg, str):
                        input_string += str(arg) + sep
                    else:
                        input_string += arg + sep
            else:
                if len(kwargs) == 0:
                    return print(end=end)
                else:
                    input_string = kwargs[0]
            str_info_list = self._sort_string_with_limited_wid(input_string, limited_wid, limited_line=1)[0]['str_info']
        # pprint(str_info_list)
        # 如果参数未赋值就给参数添加默认值
        csi_code = self.__csi_code if csi_code is None else csi_code
        print_delay = self.__print_delay if print_delay is None else self.__param_value_limits('print_delay',
                                                                                               print_delay)
        step = self.__step if step is None else self.__param_value_limits('step', step)
        indent = 1 if indent < 1 else indent + 1
        left_idx = len(str_info_list) - 1
        left = str_info_list[left_idx]['len'] - 1
        is_end = False
        # 设置csi控制代码
        while not is_end:
            Cursor.hor_pos(indent)
            if left_idx < 0:
                is_end = True
                left_idx = 0
                left = 0
            for temp_idx in range(left_idx, len(str_info_list)):
                prt_csi_code = csi_code if str_info_list[temp_idx]['csi'] == '' else str_info_list[temp_idx]['csi']
                print(prt_csi_code, end='')
                if temp_idx == left_idx:
                    print(str_info_list[left_idx]['str'][left:], end='')
                else:
                    print(str_info_list[temp_idx]['str'], end='')
            print(Style.RESET_ALLs, end='')
            left -= step
            if left < 0:
                left_idx -= 1
                left += str_info_list[left_idx]['len']
                time.sleep(print_delay)
        print(Style.RESET_ALLs, end=end, flush=True)

    def __pop_print_multiline(self, sorted_str_info, print_delay=0.005, step=1, end='\n'):
        """
        可以多行同时弹出式的打印字符串，不建议在字符串中使用csi光标控制代码或者换行符等，会影响打印的效果
        只负责打印，不负责整理数据
        :param sorted_str_info: 直接由类方法preprocessing_for_pop_print返回的数据格式
        :param print_delay: 打印延迟时间
        :param step: 打印递增步数
        :param end: 打印完之后的输出的字符
        :return: None
        """

    def __param_value_limits(self, param, value):
        """限制相关类变量数值的私有函数"""
        if param == 'csi_code':
            if not isinstance(value, str):
                value = str(value)
            return value
        if param == 'print_delay':
            return 0 if value < 0 else value
        if param == 'step':
            if not isinstance(value, int):
                value = float(value) if isinstance(value, float) else 1
            return 1 if value < 1 else value


indents_tuple = namedtuple('indent', 'unchecked, checked')


class Choice(CsiStringMethods):
    def __init__(self, screen_wid=None):
        super().__init__(screen_wid)
        """可直接通过属性设置的变量"""
        self.checked_csi_code = Colors256.BACK10 + Colors256.FORE255 + Style.BRIGHTs  # 被选中效果
        self.unchecked_csi_code = Colors256.BACK233 + Colors256.FORE255 + Style.DIMs  # 未选中效果
        self.click_csi_code = Colors256.BACK249 + Colors256.FORE232  # 点击效果
        self.is_pop = True  # 弹出效果开关
        """需通过类方法设置/获取的变量"""
        self._options = []  # 选项列表 *
        self._methods = []  # 方法列表 *
        self._sep_line = 0  # 选项之间的间隔行度
        self._unchecked_indents = 2  # 未选中选项的缩进 *
        self._checked_indents = 4  # 被选中选项的缩进 *
        self._key_setting = {  # 按键设置
            'up': 'w', 'down': 's',
            'confirm': ['e', '\r', '\n']
        }
        """使用者无需考虑的变量"""
        self.__option_line = 1  # 选项可占行数
        self.__sorted_options_info = []  # 存储整理好的
        self.__lp = LivePrint(screen_wid, csi_code=self.unchecked_csi_code)  # 内置一个lp类实例
        self._current_index = 0  # 当前选项的索引
        self._previous_index = 0  # 前一个选项的索引（实际是根据光标位置来判断）
        self._is_confirm = False  # 是否按键确认了

    def set_indents(self, unchecked, checked):
        """
        设置缩进参数
        :param unchecked: 未选中选项行的缩进
        :param checked:  被选中选现行的缩进
        """
        unchecked = 0 if unchecked < 0 else unchecked
        checked = 0 if checked < 0 else checked
        if checked < unchecked:
            raise ValueError('\033[32;1m被选中选现行的缩进数值不能小于未选中选项行的缩进\033[0m')
        if checked > self.get_scrwid():
            raise ValueError('\033[32;1m选中选现行的缩进数值不能超过设定的屏幕宽度\033[0m')
        self._unchecked_indents = unchecked
        self._checked_indents = checked

    def get_indents(self):
        """返回一个命名元组，包含未选中选项行的缩进和被选中选现行的缩进的数值"""
        return indents_tuple(unchecked=self._unchecked_indents, checked=self._checked_indents)

    def set_sep_line(self, sep_line):
        """这个属性只需保证数值不小于0就行"""
        self._sep_line = 0 if sep_line < 0 else sep_line

    def get_sep_line(self):
        return self._sep_line

    def set_options(self, option_list):
        """
        设置选项
        :param option_list: 包含字符串的列表，为了能显示正常，不要在里面使用任何光标控制代码，包括 \n \r \b
        """
        if not isinstance(option_list, list):
            raise TypeError('\033[38;5;9m设置选项时需传递列表\033[0m')
        if len(option_list) <= 0:
            raise ValueError('\033[38;5;9m传递的列表长度不能为0\033[0m')
        for option in option_list:
            if not isinstance(option, str):
                self._options.append(str(option))
            else:
                self._options.append(option)
        self.__sort_options()
        self.__sort_methods()

    def get_options(self):
        return self._options

    def set_methods(self, method_list):
        """
        设置方法列表
        :param method_list: 包含方法（可调用元素的列表），如果设置了选项但是没设置对应的方法，那么会自动填充空函数
        """
        self._methods = []
        if not isinstance(method_list, list):
            raise TypeError('\033[38;5;9m设置选项对应的方法时需传递列表\033[0m')
        if len(method_list) <= 0:
            raise ValueError('\033[38;5;9m传递的列表长度不能为0\033[0m')
        for method in method_list:
            if not callable(method) and not None:
                raise TypeError('\033[38;5;9m传递的列表参数内含有不可调用对象\033[0m')
            else:
                self._options.append(method)
        self.__sort_methods()

    def get_methods(self):
        return self._methods

    def set_keys(self, setting_dict):
        self._key_setting['up'] = setting_dict['up']
        self._key_setting['down'] = setting_dict['down']
        self._key_setting['confirm'] = setting_dict['confirm']

    def get_key_setting(self):
        """返回包含键位设置的字典"""
        return self._key_setting

    def run(self):
        """运行实例的入口函数"""
        Cursor.hide()
        self._print_options()
        # 打印完先更新一下
        self._update_options()
        option_index = None
        while not self._is_confirm:
            # 先处理输入再更新
            self._processing_input()
            # 更新选项
            option_index = self._update_options()
        # 重置self._is_confirm，以便下次调用的时候重复使用
        self._is_confirm = False
        Cursor.show()
        self._methods[option_index]()
        return option_index

    def __set_available_option_line(self, num):
        """设置一个选项可占函数，目前只实现了单行选项，所以暂时不能用"""
        self.__option_line = 1 if num <= 0 else num

    def __get_option_line(self):
        return self.__option_line

    def __param_value_limit(self, param, value):
        """用来限制参数数值的，不过我打算一个选项列表对应一个对象，所以这个函数暂时没什么用"""
        if param == 'option_line':
            if not isinstance(value, int):
                value = float(value) if isinstance(value, float) else 1
            return 1 if value < 1 else value

    def __sort_options(self):
        """
        把方法_sort_string_with_limited_wid返回的数据格式里的每行字符串
        用空格填补成等宽的
        """
        sorted_str_info = []
        for option in self._options:
            sorted_str_info.append(self._sort_string_with_limited_wid(option,
                                                                      self.get_scrwid() - self._checked_indents, limited_line=1)[0])
        temp = []
        for line_info in sorted_str_info:
            temp.append(line_info['line_wid'])
        max_line_wid = max(temp)
        for line_info in sorted_str_info:
            diff = max_line_wid - line_info['line_wid']
            # 增加前导空格
            line_info['str_info'][-1]['str'] += ' '*diff
            line_info['str_info'][-1]['str_wid'] += diff
            line_info['str_info'][-1]['len'] += diff
            line_info['leftover_wid'] -= diff
            line_info['line_wid'] += diff
        for str_info in sorted_str_info:
            self.__sorted_options_info.append(str_info['str_info'])

    def __sort_methods(self):
        """整理选项，如果选项对应的方法没填，那么加上空函数"""
        for _ in range(len(self._options) - len(self._methods)):
            self._methods.append(self.__null_function)

    def _print_options(self):
        """打印整个选项"""
        if self.is_pop:
            for option_info in self.__sorted_options_info:
                self.__lp.pop_print_line(dict_info=option_info, indent=self._unchecked_indents)
                print('\n'*self._sep_line, end='')
        else:
            for option_info in self.__sorted_options_info:
                self.__lp.pop_print_line(dict_info=option_info, print_delay=0, indent=self._unchecked_indents)
                print('\n'*self._sep_line, end='')
        # 由于考虑到_update_options的处理逻辑和sep_line，这里把光标位置移动到选项的下面
        self._previous_index = len(self._options) - 1
        Cursor.up(self._sep_line)

    def _update_options(self):
        """更新部分选项"""
        Cursor.up(1)  # 此时光标就在选项的下面一行，所以直接上一一行光标
        # 如果确认了，就显示一次点击效果
        if self._is_confirm:
            Conio.erase_line()
            self.__lp.pop_print_line(
                dict_info=self.__sorted_options_info[self._previous_index], csi_code=self.click_csi_code,
                print_delay=0, indent=self._unchecked_indents, end=''
            )
            print(' ' * 2)
            Cursor.up(1)
            time.sleep(0.05)
        # 覆盖掉原来选中的效果
        self.__lp.pop_print_line(
            dict_info=self.__sorted_options_info[self._previous_index], csi_code=self.unchecked_csi_code,
            print_delay=0, indent=self._unchecked_indents, end=''
        )
        print(' '*(self._checked_indents - self._unchecked_indents))
        if self._is_confirm:
            move_to_endl = (len(self._options) - self._current_index - 1) * (self._sep_line + 1)
            Cursor.down(move_to_endl)
            return self._current_index   # 返回当前选项列表的索引
        diff = self._current_index - self._previous_index  # 记录当前选项索引和上一次选项索引的差值
        # 记录缩进差值，用于过度动画的打印
        indents_diff = self._checked_indents - self._unchecked_indents - 1
        indents_diff = 0 if indents_diff == 0 else indents_diff
        transition_speed = 0.02 / indents_diff if indents_diff != 0 else 0
        if diff != 0:
            if diff > 0:
                Cursor.down(abs(diff) * (self._sep_line + 1) - 1)
            elif diff < 0:
                Cursor.up(abs(diff) * (self._sep_line + 1) + 1)
            Conio.erase_line()
            # 加一个过度动画，让选项弹出更自然
            for _ in range(indents_diff):
                self.__lp.pop_print_line(
                    dict_info=self.__sorted_options_info[self._current_index], csi_code=self.checked_csi_code,
                    print_delay=0, indent=self._unchecked_indents + _
                )
                time.sleep(transition_speed)
                Cursor.up(1)
                Conio.erase_line()
            self.__lp.pop_print_line(
                dict_info=self.__sorted_options_info[self._current_index], csi_code=self.checked_csi_code,
                print_delay=0, indent=self._checked_indents
            )
        else:
            Cursor.up(1)
            Conio.erase_line()
            self.__lp.pop_print_line(
                dict_info=self.__sorted_options_info[self._current_index], csi_code=self.checked_csi_code,
                print_delay=0, indent=self._checked_indents
            )

    def _processing_input(self):
        """处理输入，暂时只有三种按键"""
        while True:
            char = Conio.getch()
            self._previous_index = self._current_index
            if isinstance(self._key_setting['up'], list):
                if char in self._key_setting['up']:
                    self._current_index -= 1
                    break
            else:
                if char == self._key_setting['up']:
                    self._current_index -= 1
                    break
            if isinstance(self._key_setting['down'], list):
                if char in self._key_setting['down']:
                    self._current_index += 1
                    break
            else:
                if char == self._key_setting['down']:
                    self._current_index += 1
                    break
            if isinstance(self._key_setting['confirm'], list):
                if char in self._key_setting['confirm']:
                    self._is_confirm = True
                    break
            else:
                if char == self._key_setting['confirm']:
                    self._is_confirm = True
                    break
        # 如果按键不是指定按键，那就没必要更新输出，所以这里加上循环直到按键为指定按键
        self._current_index %= len(self._options)

    def __null_function(self):
        """空函数，仅作占位符"""
        return

