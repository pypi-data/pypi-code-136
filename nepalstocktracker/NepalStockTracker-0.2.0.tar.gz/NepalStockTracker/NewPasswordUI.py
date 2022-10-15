import hashlib
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox

try:  # When used as a package
    from NepalStockTracker.db import DB
    import NepalStockTracker._photo_image as pi
    from NepalStockTracker._Entry import _Password_Entry

except ImportError:  # When used as a normal script
    from db import DB
    import _photo_image as pi
    from _Entry import _Password_Entry


class NewPasswordUI:
    '''
    Show widgets to enter New Password when
    user clicks reset button after providing
    credentials.
    '''

    def __init__(self, username, master, ForgotPasswordFrame, LoginFrame, RightFrame, InnerRightFrame):
        self.db = DB()
        self.bg = '#90d604'  # '#cbd0d6'
        self.pi = pi.Image()

        self.master = master
        self.username = username
        self.LoginFrame = LoginFrame
        self.RightFrame = RightFrame
        self.InnerRightFrame = InnerRightFrame
        self.ForgotPasswordFrame = ForgotPasswordFrame

    def ShowWidgets(self):
        '''
        Showing corresponding widgets
        '''

        self.InnerRightFrame.pack_forget()
        self.master.title('Nepal Stock Tracker | New Password')

        self.NewPasswordFrame = Frame(self.RightFrame, bg=self.bg)
        self.NewPasswordFrame.pack(padx=50, pady=50)

        self.PasswordEntry = _Password_Entry(self.NewPasswordFrame, 'RPE', 'Password', self.bg, 40, True)
        self.PasswordEntry.PasswordFrame.pack(padx=(48, 0))

        self.ConfirmPasswordEntry = _Password_Entry(self.NewPasswordFrame, 'CRPE', 'Confirm Password', self.bg, 40, True)
        self.ConfirmPasswordEntry.PasswordFrame.pack(padx=(48, 0), pady=10)

        self.SubmitButton = Button(self.NewPasswordFrame, image=self.pi.ConfirmImage, bg=self.bg, activebackground=self.bg, bd='0', cursor='hand2', font=Font(size=10, weight='bold'), command=self.SubmitButtonCommand)
        self.SubmitButton.pack(pady=(0, 15), ipady=10)

        self.BackButton = Button(self.NewPasswordFrame, image=self.pi.BackImage, bd=0, cursor='hand2', bg=self.bg, activebackground=self.bg, command=self.BackButtonCommand)
        self.BackButton.image = self.pi.BackImage
        self.BackButton.pack()

    def SubmitButtonCommand(self):
        '''
        Notify user that his/her password has been
        changed and send them to login page.
        '''

        PasswordDefault = self.PasswordEntry.PasswordEntry.IsDefault
        ConfirmPasswordDefault = self.ConfirmPasswordEntry.PasswordEntry.IsDefault

        Password = self.PasswordEntry.PasswordEntry.var.get().strip().strip()
        ConfirmPassword = self.ConfirmPasswordEntry.PasswordEntry.var.get().strip()

        if any([PasswordDefault, ConfirmPasswordDefault]):
            messagebox.showerror('ERR', 'Provide new password')

        elif Password != ConfirmPassword:
            messagebox.showerror('ERR', 'Provide same passwords')

        else:
            contents = self.db.ReadJSON()
            EncryptedPassword = hashlib.sha256(Password.encode()).hexdigest()

            contents[self.username]['password'] = EncryptedPassword

            messagebox.showinfo('Success', 'You password has been changed!!!\n\nNow you can login')
            self.master.title('Nepal Stock Tracker | LOGIN')

            self.ForgotPasswordFrame.destroy()
            self.LoginFrame.pack()

    def BackButtonCommand(self):
        '''
        When user clicks back button
        '''

        self.NewPasswordFrame.destroy()
        self.InnerRightFrame.pack()
        self.master.title('Nepal Stock Tracker | Change Password')
