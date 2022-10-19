import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from translator.translate import Translator

sun_font = ("SUN7_8_1210", 16)


class EntryView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.translator = Translator()

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.textEntry = tk.Text(self)
        self.textEntry.grid(row=0, column=0,
                            sticky=tk.N+tk.S+tk.E+tk.W)
        self.textEntry.configure(font=("Times", 16),
                                 wrap=tk.WORD)

        self.translatedText = tk.Text(self)
        self.translatedText.grid(row=0, column=1,
                                 sticky=tk.N+tk.S+tk.E+tk.W)
        self.translatedText.configure(font=sun_font,
                                      wrap=tk.WORD)
        self.translatedText.configure(state=tk.DISABLED)

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

        self.translatedText.configure(state=tk.NORMAL)
        self.translatedText.delete('1.0', 'end')
        self.translatedText.insert('1.0', translated)
        self.translatedText.configure(state=tk.DISABLED)

    def save(self):
        filename = filedialog.asksaveasfilename(filetypes=[("PDF", "*.pdf")],
                                                defaultextension='.pdf',
                                                title="Save As")
        text = self.translatedText.get('1.0', 'end')
        self.translator.saveToPdf(text, filename)
