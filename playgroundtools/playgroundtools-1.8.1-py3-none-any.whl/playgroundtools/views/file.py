import tkinter as tk


class FileView:
    """Represents the file preview section of the GUI."""

    def __init__(self, parent):
        self.parent = parent

        self.textarea = tk.Text(self.parent)

        self.textarea.configure(state=tk.DISABLED)

    def set_text(self, text):
        """Sets the text of the textarea."""
        text = "\n".join(text)
        self.clear_text()
        self.insert_text(1.0, text)

    def insert_text(self, index, text):
        self.textarea.configure(state=tk.NORMAL)
        self.textarea.insert(index, text)
        self.textarea.configure(state=tk.DISABLED)

    def clear_text(self):
        """Clears the text of the textarea."""
        self.textarea.configure(state=tk.NORMAL)
        self.textarea.delete(1.0, tk.END)
        self.textarea.configure(state=tk.DISABLED)
