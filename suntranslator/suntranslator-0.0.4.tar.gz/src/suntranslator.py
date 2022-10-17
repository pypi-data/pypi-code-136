#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

from translator.translate import Translator
from gui.menubar import Menubar

sun_font = ("SUN7_8_1210", 16)


class Application(ttk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
        # self.grid(sticky=tk.NSEW)
        self.createWidgets()
        self.translator = Translator()

    def createWidgets(self):
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1, minsize=200)
        top.columnconfigure(0, weight=1, minsize=200)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.menubar = Menubar(self, top)

        self.textEntry = tk.Text(self)
        self.textEntry.grid(row=0, column=0,
                            sticky=tk.N+tk.S+tk.E+tk.W)
        self.textEntry.configure(font=("Times", 16),
                                 wrap=tk.WORD)

        self.textEntry2 = tk.Text(self)
        self.textEntry2.grid(row=0, column=1,
                             sticky=tk.N+tk.S+tk.E+tk.W)
        self.textEntry2.configure(font=sun_font,
                                  wrap=tk.WORD)
        self.textEntry2.configure(state=tk.DISABLED)

        self.translateButton = ttk.Button(self, text="Translate",
                                          command=self.translate)
        self.translateButton.grid(row=1, column=0, columnspan=2,
                                  sticky=tk.N+tk.S+tk.E+tk.W)

        self.saveButton = ttk.Button(self, text="Save",
                                     command=self.save)
        self.saveButton.grid(row=2, column=0, columnspan=2,
                             sticky=tk.N+tk.S+tk.E+tk.W)

        self.textEntry.bind("<Return>", self.__translate)

    def __translate(self, event):
        self.translateButton.invoke()

    def translate(self):
        text = self.textEntry.get('1.0', 'end')

        translated = self.translator.translateText(text)

        self.textEntry2.configure(state=tk.NORMAL)
        self.textEntry2.delete('1.0', 'end')
        self.textEntry2.insert('1.0', translated)
        self.textEntry2.configure(state=tk.DISABLED)

    def save(self):
        filename = filedialog.asksaveasfilename(filetypes=[("PDF", "*.pdf")],
                                                defaultextension='.pdf',
                                                title="Save As")
        text = self.textEntry2.get('1.0', 'end')
        self.translator.saveToPdf(text, filename)


def main():
    app = Application()
    app.master.title("Sun Translation")
    app.mainloop()


if __name__ == "__main__":
    main()
