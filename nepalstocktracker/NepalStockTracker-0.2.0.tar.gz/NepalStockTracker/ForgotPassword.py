import hashlib
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox

try:  # When used as a package
    from NepalStockTracker.db import DB
    from NepalStockTracker import Include
    from NepalStockTracker._Entry import _Entry
    import NepalStockTracker._photo_image as pi
    from NepalStockTracker.NewPasswordUI import NewPasswordUI
    from NepalStockTracker.SecurityQuestionUI import SecurityQuestionUI

except ImportError:  # When used as a normal script
    import Include
    from db import DB
    import _photo_image as pi
    from _Entry import _Entry
    from NewPasswordUI import NewPasswordUI
    from SecurityQuestionUI import SecurityQuestionUI


class ForgotPasswordUI:
    '''
    Display widgets to get corresponding
    credentials to reset the password
    '''

    def __init__(self, master, LoginFrame):
        self.db = DB()
        self.bg = '#cbd0d6'
        self.RightBG = '#90d604'
        self.pi = pi.Image()

        self.master = master
        self.LoginFrame = LoginFrame

    def ShowWidgets(self, event):
        '''
        Show corresponding widgets
        '''

        self.master.withdraw()

        self.LoginFrame.pack_forget()
        self.master.title('Nepal Stock Tracker | Reset Password')

        self.ForgotPasswordFrame = Frame(self.master, bg=self.RightBG)
        self.ForgotPasswordFrame.pack()

        self.LeftFrame = Frame(self.ForgotPasswordFrame)
        self.LeftFrame.pack(side=LEFT)
        self.RightFrame = Frame(self.ForgotPasswordFrame, bg=self.RightBG)
        self.RightFrame.pack(side=RIGHT, ipadx=50, pady=(50, 0))
        self.InnerRightFrame = Frame(self.RightFrame, bg=self.RightBG)
        self.InnerRightFrame.pack()

        self.LeftImage = Label(self.LeftFrame, image=self.pi.ForgotPasswordFrameImage, bg='#aaff00')
        self.LeftImage.pack(ipadx=30, ipady=3)

        self.UsernameEntry = _Entry(self.InnerRightFrame, 'FPE', 'Username', width=62, bg=self.RightBG)
        self.UsernameEntry.Frame.pack(ipady=5)

        self.SecurityQuestion = SecurityQuestionUI(self.master, self.InnerRightFrame, bg=self.RightBG)
        self.SecurityQuestion.frame.pack()

        self.ResetButton = Button(self.InnerRightFrame, image=self.pi.ResetImage, fg='white', bg=self.RightBG, activebackground=self.RightBG, activeforeground="white", bd='0', cursor='hand2', font=Font(size=10, weight='bold'), command=self.ResetButtonCommand)
        self.ResetButton.pack(ipady=8)

        self.BackButton = Button(self.InnerRightFrame, image=self.pi.BackImage, bd=0, cursor='hand2', bg=self.RightBG, activebackground=self.RightBG, command=self.BackButtonCommand)
        self.BackButton.pack(pady=(20, 0))

        Include.SetWindowPosition(self.master)

    def ResetButtonCommand(self):
        '''
        When user clicks reset button after entering credentials
        '''

        contents = self.db.ReadJSON()
        UsernameEntryDefault = self.UsernameEntry.IsDefault
        SecurityQuestionEntryDefault = self.SecurityQuestion.SecurityQuestionAnswerEntry.IsDefault

        username = self.UsernameEntry.var.get().strip()
        SecurityQuestionCombo = self.SecurityQuestion.ComboBoxVar.get().strip()
        SecurityAnswer = self.SecurityQuestion.SecurityQuestionAnswerEntry.var.get().strip().lower()

        if any([UsernameEntryDefault, SecurityQuestionEntryDefault]) or SecurityQuestionCombo not in self.SecurityQuestion.ComboValues:
            messagebox.showerror('ERR', 'Provide valid information')

        elif username not in contents:
            messagebox.showerror('ERR', f'Username: "{username}" not found')

        else:
            EncryptedSecurityAnswer = hashlib.sha256(SecurityAnswer.encode()).hexdigest()
            EncryptedSecurityQuestion = hashlib.sha256(SecurityQuestionCombo.lower().encode()).hexdigest()

            if EncryptedSecurityQuestion != contents[username]['question'] or EncryptedSecurityAnswer != contents[username]['answer']:
                messagebox.showerror('ERR', 'Invalid Security Question or Security Answer')

            else:
                NewPassword = NewPasswordUI(username, self.master, self.ForgotPasswordFrame, self.LoginFrame, self.RightFrame, self.InnerRightFrame)
                NewPassword.ShowWidgets()

    def BackButtonCommand(self):
        '''
        When user clicks back button
        '''

        self.ForgotPasswordFrame.destroy()
        self.LoginFrame.pack()
