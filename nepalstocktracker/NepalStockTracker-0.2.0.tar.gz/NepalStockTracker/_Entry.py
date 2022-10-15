from tkinter import *
import tkinter.ttk as ttk

try:  # When used as a package
    import NepalStockTracker._photo_image as pi

except ImportError:  # When used as a normal script
    import _photo_image as pi


class _Entry:
    def __init__(self, frame, style_name, default_text, bg='black', width=19, show=None):
        '''
        An Entry widget having a placeholder text like of HTML. When user
        focuses to the entry widget then the placeholder text gets removed.
        When user focuses out of that Entry widget without entering any value
        then the placeholder text gets inserted.
        '''

        self.dot = '●'
        self.show = show
        self.frame = frame
        self.IsDefault = True
        self.default_text = default_text
        self.style_name = f'{style_name}.TEntry'

        self.var = StringVar()
        self.var.set(self.default_text)

        self.Frame = Frame(frame, bg=bg)
        self.Entry = Entry(self.Frame, textvariable=self.var, width=width, justify='center')
        self.Entry.pack(ipady=5)
        self.Entry.config(fg='grey')
        self.LineFrame = Frame(self.Frame, height=5, bg='#9da17d')
        self.LineFrame.pack(fill='x')

        self.Entry.bind('<FocusIn>', self.FocusIn)
        self.Entry.bind('<FocusOut>', self.FocusOut)

    def FocusIn(self, event=None):
        '''
        When ttk.Entry gets focus either by click
        to it or by pressing TAB key
        '''

        self.LineFrame.config(bg='#02c4f5')

        if self.IsDefault and self.var.get().strip() == self.default_text:
            self.IsDefault = False
            self.var.set('')
            self.Entry.config(fg='black')

            if self.show is True:
                self.Entry.config(show=self.dot)

    def FocusOut(self, event=None):
        '''
        When ttk.Entry gets focus out either by click
        to another widget or by pressing TAB key
        '''

        self.LineFrame.config(bg='#9da17d')

        if self.IsDefault is False and not self.var.get().strip():
            self.IsDefault = True

            self.Entry.config(fg='grey')
            self.var.set(self.default_text)

            if self.show is True:
                self.Entry.config(show='')

    def SetToDefault(self):
        '''
        Set the default values to respective ttk.Entry when
        user finish adding, deleting or renaming values
        '''

        self.IsDefault = True

        if self.show is not None:
            self.show = True
            self.Entry.config(show='')

        self.var.set(self.default_text)
        self.Entry.config(fg='grey')


class _Password_Entry:
    '''
    An Entry widget having placeholder text "●". Also
    draw button that hide or show the text when clicked.
    '''

    def __init__(self, frame, style_name, default_text, bg, width=19, show=None):
        self.pi = pi.Image()
        self.IsPasswordHidden = True

        self.bg = bg
        self.show = show
        self.width = width
        self.frame = frame
        self.style_name = style_name
        self.default_text = default_text

        self.PasswordFrame = Frame(self.frame, bg=self.bg)

        self.PasswordEntry = _Entry(self.PasswordFrame, self.style_name, self.default_text, show=True, width=width, bg=self.bg)
        self.PasswordEntry.Frame.pack(side=LEFT)
        self.ShowHidePassword = Button(self.PasswordFrame, image=self.pi.HidePasswordImage, bd=0, bg=self.bg, activebackground=self.bg, cursor='hand2', takefocus=False, command=self.ShowHidePasswordCommand)
        self.ShowHidePassword.pack(side=RIGHT, padx=(5, 0))

    def ShowHidePasswordCommand(self):
        '''
        Toggle between "●" and text when user
        clicks to hide-show-password button
        '''

        if self.IsPasswordHidden:
            self.IsPasswordHidden = False
            self.PasswordEntry.show = False
            self.PasswordEntry.Entry.config(show='')
            self.ShowHidePassword.config(image=self.pi.ShowPasswordImage)

        else:
            self.IsPasswordHidden = True
            self.PasswordEntry.show = True

            if self.PasswordEntry.IsDefault is False:
                self.PasswordEntry.Entry.config(show=self.PasswordEntry.dot)

            self.ShowHidePassword.config(image=self.pi.HidePasswordImage)
