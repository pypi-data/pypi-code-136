import sys
from curtsies import Input, FSArray , CursorAwareWindow, fsarray
from curtsies.fmtfuncs import red, bold, green, on_blue, yellow


import random

CHECKED = '\u25c9 '
UNCHECKED = '\u25cc '

def _no_fmt(s):
    return s

def choose(prompt, choices, multi=False,sel_fmt=red):
    choice_list = ChoiceList(choices,prompt=prompt, multi=multi,sel_fmt=sel_fmt)
    with CursorAwareWindow(out_stream=sys.stderr, extra_bytes_callback=lambda x: x) as window:
        options = choice_list.run(window)

    return options

class Choice:
    def __init__(self, obj):
        self._obj = obj

    def __str__(self):
        return str(self._obj)

    def render(self, fmt, width):
        lines = str(self).split('\n')
        arr = fsarray(fmt(line) for line in lines)
        return arr

class ChoiceList:
    def __init__(self, choices, prompt=None, multi=False, sel_fmt=bold, des_fmt=_no_fmt, selected=CHECKED, deselected=UNCHECKED):
        if prompt:
            self._prompt = fsarray([bold(line) for line in prompt.split('\n')])
        else:
            self._prompt = prompt
        if multi is True:
            multi = (0, len(choices))
        self._multi = multi
        if not choices:
            raise ValueError('No choices given')
        self._choices = [[False, Choice(c)] for c in choices]
        self._sel_fmt = sel_fmt
        self._des_fmt = des_fmt
        self._sel = selected
        self._des = deselected
        self._idx = 0

    def run(self, window):
        opt_arr = self.render(window.width)
        window.render_to_terminal(opt_arr)
        with Input() as keyGen:
            for key in keyGen:
                if key == '<UP>':
                    self.prev()
                elif key == '<DOWN>':
                    self.next()
                elif key == '<SPACE>':
                    if self._multi:
                        self.toggle()
                elif key == '<Ctrl-j>':
                    if not self._multi:
                        self.toggle()
                    break
                else:
                    continue
                window.render_to_terminal(self.render(window.width))
        options = self.get_selection()
        return options if self._multi else options[0]
        return self.get_selection()

    def toggle(self):
        state = self._choices[self._idx]
        state[0] = not state[0]

    def select(self, index):
        self._idx = index

    def render(self, width):
        arr = fsarray('', width=width)
        if self._prompt:
            arr.rows = self._prompt.rows + arr.rows
        l = len(arr)
        for checked, option in self._choices:
            current = self._choices[self._idx][1] == option
            fmt = self._sel_fmt if current else self._des_fmt
            opt_arr = option.render(fmt, width-3)
            arr[l:l+len(opt_arr), 2:width] = opt_arr
            if self._multi:
                state = self._sel if checked else self._des
            else:
                state = '> ' if current else '  '
            arr[l:l+1, 0:2] = fsarray([state])
            l += len(opt_arr)
        return arr

    def get_selection(self):
        return [item[1]._obj for item in self._choices if item[0]]

    def next(self):
        self._idx = min(len(self)-1, self._idx+1)

    def prev(self):
        self._idx = max(0, self._idx-1)

    def __len__(self):
        return len(self._choices)

    def __getitem__(self, key):
        item = self._choices[key]
        return item[1]._obj

    def __setitem__(self, key, value):
        self._choices[key] = [False, Choice(value)]

    def __delitem__(self, key):
        del self._choices[key]

    def __contains__(self, item):
        return item in [i[1]._obj for i in self._choices]


if __name__ == "__main__":
    c = choose('Prompt \n line 3: ', ['abc', 'def', 'ghi', 'jkl', 'mno'])
