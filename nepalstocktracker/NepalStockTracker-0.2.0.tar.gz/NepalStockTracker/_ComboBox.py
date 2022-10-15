import timeit
from tkinter import *
import tkinter.ttk as ttk


class _ComboBox:
    '''
    A combo-box with the list of fetched company names with
    auto-complete functionality.
    '''

    def __init__(self, master, frame, values):
        self.master = master
        self.frame = frame

        self.values = values
        self.StartTimer = None

        self.StartTimer = 0
        self.PreviousSearch = ''
        self.LocalSearchIndex = 0

        self.DEFAULT_TEXT = 'COMPANY SYMBOL'

        self.ComboVar = StringVar()
        self.ComboVar.set(self.DEFAULT_TEXT)

        self.ComboBox = ttk.Combobox(self.frame, textvariable=self.ComboVar, values=self.values, width=41, justify='center', state='readonly')

        self.ComboBox.config(values=self.values)
        self.ComboBox.bind('<KeyRelease>', self.AutoComplete)

    def AutoComplete(self, event=None):
        '''
        Search value when the focus is in ttk.Combobox
        '''

        _char = event.char.upper()

        if _char == '':
            return 'break'

        if self.StartTimer:
            end_timer = timeit.default_timer()
            escaped = end_timer - self.StartTimer

            if 0 < escaped < 0.27:
                _char = self.PreviousSearch + _char

        common_names = list(filter(lambda item: item.startswith(_char), self.values))

        if self.PreviousSearch != _char or self.LocalSearchIndex == len(common_names) - 1:
            self.LocalSearchIndex = 0

        self.PreviousSearch = _char
        self.StartTimer = timeit.default_timer()

        if common_names:
            self.ToSelectValue = common_names[self.LocalSearchIndex]
            self.LocalSearchIndex += 1

            self.ComboBox.set(self.ToSelectValue)
            self.ComboVar.set(self.ToSelectValue)
