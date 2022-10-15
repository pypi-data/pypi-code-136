import hashlib
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox

try:  # When used as a package
    from NepalStockTracker.db import DB
    from NepalStockTracker import Include
    import NepalStockTracker._photo_image as pi
    from NepalStockTracker.DashBoard import DashBoard
    from NepalStockTracker._Entry import _Entry, _Password_Entry
    from NepalStockTracker.ForgotPassword import ForgotPasswordUI

except ImportError:  # When used as a normal script
    import Include
    from db import DB
    import _photo_image as pi
    from DashBoard import DashBoard
    from _Entry import _Entry, _Password_Entry
    from ForgotPassword import ForgotPasswordUI


class LoginUI:
    '''
    Show widgets for login
    '''

    def __init__(self, master, MainFrame, LOGIN, ComboValues, search):
        self.db = DB()
        self.bg = '#cbd0d6'
        self.LOGIN = LOGIN
        self.RightBG = '#4d3778'
        self.pi = pi.Image()
        self.SEARCH = search
        self.master = master
        self.MainFrame = MainFrame
        self.IsPasswordHidden = True
        self.ComboValues = ComboValues

    def ShowWidgets(self):
        '''
        Show corresponding widgets
        '''

        if self.LOGIN.username is None:
            self.master.withdraw()
            self.MainFrame.pack_forget()
            self.master.title('Nepal Stock Tracker | LOGIN')

            self.LoginFrame = Frame(self.master, bg=self.RightBG)
            self.LoginFrame.pack()

            self.LeftFrame = Frame(self.LoginFrame)
            self.LeftFrame.pack(side=LEFT, expand=TRUE)
            self.RightFrame = Frame(self.LoginFrame, bg=self.RightBG)
            self.RightFrame.pack(side=RIGHT, anchor=CENTER)

            self.LeftLabel = Label(self.LeftFrame, image=self.pi.LoginFrameImage, bg='#6847ae')
            self.LeftLabel.pack(ipadx=20, ipady=20)
            self.UsernameEntry = _Entry(self.RightFrame, 'LUE', 'Username', width=40, bg=self.RightBG)
            self.UsernameEntry.Frame.pack(ipady=5, pady=10)

            self.PasswordEntry = _Password_Entry(self.RightFrame, 'LPE', 'Password', self.RightBG, 40, True)
            self.PasswordEntry.PasswordFrame.pack(padx=(48, 0))

            self.SubmitButton = Button(self.RightFrame, imag=self.pi.LoginButtonImage, bg=self.RightBG, activebackground=self.RightBG, activeforeground="white", bd='0', cursor='hand2', font=Font(size=10, weight='bold'), command=self.SubmitButtonCommand)
            self.SubmitButton.pack(pady=15, ipady=5)

            self.ForgotPasswordLabel = Label(self.RightFrame, text='Forgot Password ?', fg='white', bg=self.RightBG, cursor='hand2', font=Font(size=10, underline=True))
            self.ForgotPasswordLabel.pack(padx=(0, 45), pady=(10, 10), anchor='e')

            self.BackButton = Button(self.RightFrame, image=self.pi.BackImage, bd=0, cursor='hand2', bg=self.RightBG, activebackground=self.RightBG, command=self.BackButtonCommand)
            self.BackButton.pack(pady=(30, 0))

            self.ForgotPassword = ForgotPasswordUI(self.master, self.LoginFrame)
            self.ForgotPasswordLabel.bind('<Button-1>', self.ForgotPassword.ShowWidgets)

            Include.SetWindowPosition(self.master)

        else:
            self.Dashboard = DashBoard(self.master, self.ComboValues, self.LOGIN, self.MainFrame, self.SEARCH)
            self.Dashboard.ShowWidgets()

    def SubmitButtonCommand(self):
        '''
        When user clicks login button after enter credentials
        '''

        UserNameDefault = self.UsernameEntry.IsDefault
        PasswordDefault = self.PasswordEntry.PasswordEntry.IsDefault

        username = self.UsernameEntry.var.get().strip()
        password = self.PasswordEntry.PasswordEntry.var.get().strip()

        contents = self.db.ReadJSON()

        if any([UserNameDefault, PasswordDefault]):
            messagebox.showerror('ERR', 'Provide valid values')

        else:
            if username not in contents:
                messagebox.showerror('ERR', 'Username or password did not match')

            password_from_file = contents[username]['password']
            encrypted_password = hashlib.sha256(password.encode()).hexdigest()

            if password_from_file == encrypted_password:
                self.UsernameEntry.SetToDefault()
                self.PasswordEntry.PasswordEntry.SetToDefault()

                self.LOGIN.login(username)
                self.Dashboard = DashBoard(self.master, self.ComboValues, self.LOGIN, self.LoginFrame, self.SEARCH, self.MainFrame)
                self.Dashboard.ShowWidgets()

            else:
                messagebox.showerror('ERR', 'Username or password did not match')

    def BackButtonCommand(self):
        '''
        Go back to homepage when user clicks back button
        '''

        self.master.title('Nepal Stock Tracker')

        self.LoginFrame.destroy()
        self.MainFrame.pack(padx=50, pady=50)
