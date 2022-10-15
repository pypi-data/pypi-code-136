import string
import hashlib
from tkinter import *
from tkinter.font import Font
from tkinter import messagebox

try:  # When used as a package
    from NepalStockTracker.db import DB
    from NepalStockTracker import Include
    import NepalStockTracker._photo_image as pi
    from NepalStockTracker._Entry import _Entry, _Password_Entry
    from NepalStockTracker.SecurityQuestionUI import SecurityQuestionUI

except ImportError:  # When used as a normal script
    import Include
    from db import DB
    import _photo_image as pi
    from _Entry import _Entry, _Password_Entry
    from SecurityQuestionUI import SecurityQuestionUI


class SignUpUI:
    '''
    Show widgets to create new account
    '''

    def __init__(self, master, MainFrame, Login, MainFrameBg):
        self.db = DB()
        self.pi = pi.Image()
        self.RightBG = '#e3a002'
        self.MainFrameBg = MainFrameBg

        self.Login = Login
        self.master = master
        self.MainFrame = MainFrame
        self.IsPasswordHidden = True

    def ShowWidgets(self, event):
        '''
        Show corresponding widgets
        '''

        self.master.withdraw()

        self.MainFrame.pack_forget()
        self.master.title('Nepal Stock Tracker | SIGN-UP')

        self.SignupFrame = Frame(self.master, bg=self.RightBG)
        self.SignupFrame.pack()

        self.LeftFrame = Frame(self.SignupFrame)
        self.LeftFrame.pack(side=LEFT)
        self.RightFrame = Frame(self.SignupFrame, bg=self.RightBG)
        self.RightFrame.pack(side=RIGHT)

        self.LeftImage = Label(self.LeftFrame, image=self.pi.SignUpFrameImage, bg='#e3be02')
        self.LeftImage.pack(ipadx=50, ipady=50)

        self.UsernameEntry = _Entry(self.RightFrame, 'SUE', 'Username', width=63, bg=self.RightBG)
        self.UsernameEntry.Frame.pack(pady=(10, 0), ipady=5)

        self.PasswordEntry = _Password_Entry(self.RightFrame, 'SPE', 'Password', self.RightBG, 63, True)
        self.PasswordEntry.PasswordFrame.pack(padx=(48, 0))

        self.ConfirmPasswordEntry = _Password_Entry(self.RightFrame, 'CSPE', 'Confirm Password', self.RightBG, 63, True)
        self.ConfirmPasswordEntry.PasswordFrame.pack(pady=10, padx=(48, 0))

        self.SecurityQuestionsUI = SecurityQuestionUI(self.master, self.RightFrame, pady=10, bg=self.RightBG)
        self.SecurityQuestionsUI.frame.pack()

        self.SubmitButton = Button(self.RightFrame, image=self.pi.SubmitImage, bg=self.RightBG, activebackground=self.RightBG, activeforeground="white", bd='0', cursor='hand2', font=Font(size=10, weight='bold'), command=self.SubmitButtonCommand)
        self.SubmitButton.pack(pady=(0, 10), ipady=5)

        self.BackButton = Button(self.RightFrame, image=self.pi.BackImage, bd=0, cursor='hand2', bg=self.RightBG, activebackground=self.RightBG, command=self.BackButtonCommand)
        self.BackButton.pack(pady=(30, 0))

        Include.SetWindowPosition(self.master)

    def CheckForStrongPassword(self, password):
        '''
        Check if user have entered the strong password
        '''

        length = len(password)

        hasLower = False
        hasUpper = False
        hasDigit = False
        hasSpecialChar = False
        hasLengthMoreThanEight = False

        if length >= 8:
            hasLengthMoreThanEight = True

        for i in range(length):
            if password[i] in string.ascii_lowercase:
                hasLower = True

            elif password[i] in string.ascii_uppercase:
                hasUpper = True

            elif password[i] in string.digits:
                hasDigit = True

            elif password[i] in string.punctuation:
                hasSpecialChar = True

        return all([hasLower, hasUpper, hasDigit, hasSpecialChar, hasLengthMoreThanEight])

    def SubmitButtonCommand(self):
        '''
        When user clicks submit button
        '''

        UserNameDefault = self.UsernameEntry.IsDefault
        PasswordDefault = self.PasswordEntry.PasswordEntry.IsDefault
        ConfirmPasswordDefault = self.ConfirmPasswordEntry.PasswordEntry.IsDefault
        SecurityQuestionAnswerDefault = self.SecurityQuestionsUI.SecurityQuestionAnswerEntry.IsDefault

        password = self.PasswordEntry.PasswordEntry.var.get().strip()
        ConfirmPassword = self.ConfirmPasswordEntry.PasswordEntry.var.get().strip()
        username = self.UsernameEntry.var.get().strip()
        SecurityQuestion = self.SecurityQuestionsUI.ComboBoxVar.get()

        db = DB()
        contents = db.ReadJSON()

        if any([UserNameDefault, PasswordDefault, SecurityQuestionAnswerDefault, ConfirmPasswordDefault]):
            messagebox.showerror('Invalid', 'Provide valid values')

        elif SecurityQuestion not in self.SecurityQuestionsUI.ComboValues:
            messagebox.showerror('Invalid', 'Select valid SECURITY QUESTION')

        elif self.CheckForStrongPassword(password) is False:
                StrongPasswordConditions = f'''A password is said to be strong if it satisfies the following criteria:
    1. Its length is at least 8.
    2. It contains at least one digit.
    3. It contains at least one lowercase English character.
    4. It contains at least one uppercase English character.
    5. It contains at least one special character. The special{' ' * 18}characters are: !@#$%^&*()-+
                '''
                messagebox.showerror('ERR', StrongPasswordConditions)

        elif username in contents:
            messagebox.showerror('ERR', f'Username: "{username}" already exists')

        elif password != ConfirmPassword:
            messagebox.showerror('ERR', 'Passwords are incorrect')

        else:
            question = SecurityQuestion.lower()
            answer = self.SecurityQuestionsUI.SecurityQuestionAnswerEntry.var.get().lower()

            encrypted_answer = hashlib.sha256(answer.encode()).hexdigest()
            encrypted_password = hashlib.sha256(password.encode()).hexdigest()
            encrypted_question = hashlib.sha256(question.encode()).hexdigest()

            data = {
                username:
                    {
                        'question': encrypted_question,
                        'answer': encrypted_answer,
                        'password': encrypted_password,
                        'companies': []
                    }
            }

            contents.update(data)
            self.db.WriteJSON(contents)

            messagebox.showinfo('Success', 'Account has been created!!!\n\nEnter credentials to LOGIN-IN')
            self.SignupFrame.destroy()
            self.Login.ShowWidgets()

    def BackButtonCommand(self):
        '''
        Send user to first window when user clicks to back button
        '''

        self.master.title('Nepal Stock Tracker')

        self.SignupFrame.destroy()
        self.MainFrame.pack(padx=50, pady=50)
