from ast import Import
from tkinter import PhotoImage

try:  # When used as a package
    from NepalStockTracker import Include

except ImportError:  # When used as a normal script
    import Include


class Image:
    '''
    PhotoImage object to reduce code redundancy
    '''

    def __init__(self):
        self.AddImage = PhotoImage(file=Include.ResourcePath('Add.png'))
        self.IconImage = PhotoImage(file=Include.ResourcePath('icon.png'))
        self.BackImage = PhotoImage(file=Include.ResourcePath('Back.png'))
        self.ResetImage = PhotoImage(file=Include.ResourcePath('Reset.png'))
        self.SubmitImage = PhotoImage(file=Include.ResourcePath('Submit.png'))
        self.LogoutImage = PhotoImage(file=Include.ResourcePath('Logout.png'))
        self.ConfirmImage = PhotoImage(file=Include.ResourcePath('Confirm.png'))
        self.TitleImage = PhotoImage(file=Include.ResourcePath('Title Image.png'))
        self.LoginButtonImage = PhotoImage(file=Include.ResourcePath('Login.png'))
        self.LoginFrameImage = PhotoImage(file=Include.ResourcePath('Login Frame.png'))
        self.SignUpFrameImage = PhotoImage(file=Include.ResourcePath('Signup Frame.png'))
        self.DashBoardImage = PhotoImage(file=Include.ResourcePath('DashBoard Frame.png'))
        self.HidePasswordImage = PhotoImage(file=Include.ResourcePath('Hide Password.png'))
        self.ShowPasswordImage = PhotoImage(file=Include.ResourcePath('Show Password.png'))
        self.ForgotPasswordFrameImage = PhotoImage(file=Include.ResourcePath('Forgot Password Frame.png'))
