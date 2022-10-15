import sys
from tkinter import *
import tkinter.ttk as ttk
from tkinter.font import Font
import pygame
import requests

try:  # When used as a package
    from NepalStockTracker import Search
    from NepalStockTracker import Include
    from NepalStockTracker._Login import _Login
    from NepalStockTracker.LoginUI import LoginUI
    from NepalStockTracker.SignUpUI import SignUpUI
    from NepalStockTracker import _photo_image as pi
    from NepalStockTracker._ComboBox import _ComboBox

except ImportError:  # When used as a normal script
    import Search
    import Include
    import _photo_image as pi
    from _Login import _Login
    from LoginUI import LoginUI
    from SignUpUI import SignUpUI
    from _ComboBox import _ComboBox


__all__ = ['StockTracker']


class StockTracker:
    def __init__(self, company_symbol=None, show_gui=True):
        if show_gui:
            self.LOGIN = _Login()

            self.StartTimer = 0
            self.ErrorTimer = None
            self.PreviousSearch = ''
            self.front_color = '#cdfa05'  # '#91db07' # '#db6307'   '#db4607'
            self.DEFAULTTEXT = 'COMPANY SYMBOL'

            if sys.platform == 'win32':
                self.ErrorAudio = Include.ResourcePath('WinErrSound.wav')

            else:
                self.ErrorAudio = Include.ResourcePath('LinuxErrSound.wav')

            pygame.mixer.init()
            pygame.mixer.music.load(self.ErrorAudio)

            self.master = Tk()
            self.pi = pi.Image()
            self.master.withdraw()
            self.master.title('Nepal Stock Tracker')
            self.master.iconphoto(False, self.pi.IconImage)
            self.SEARCH = Search.Search(self.ShowErrorMessage, self.CheckInternet, master=self.master)

            self.master.config(bg=self.front_color)
            self.OptionValues = self.SEARCH.GetCompaniesNameList()
            self.OptionValues.sort()

            self.MainFrame = Frame(self.master, bg=self.front_color)
            self.MainFrame.pack(padx=50, pady=50)

            self.WidgetsFrame = Frame(self.MainFrame, bg=self.front_color)
            self.WidgetsFrame.pack(side=LEFT)

            self.TitleLabel = Label(self.WidgetsFrame, image=self.pi.TitleImage, bg=self.front_color)
            self.TitleLabel.pack()

            self.CompanyName = _ComboBox(self.master, self.WidgetsFrame, self.OptionValues)
            self.CompanyName.ComboBox.pack(pady=10, ipady=3)

            self.DataButton = Button(self.WidgetsFrame, text="Get Company Details", width=33, fg='white', bg="#006837", activebackground="#006837", activeforeground="white", bd='0', cursor='hand2', font=Font(size=10, weight='bold'), command=self.GetMarketDetails)
            self.DataButton.pack(ipady=8)

            self.Login = LoginUI(self.master, self.MainFrame, self.LOGIN, self.OptionValues, self.SEARCH)
            self.LoginButton = Button(self.WidgetsFrame, text="LOGIN", width=33, fg='white', bg="#006837", activebackground="#006837", activeforeground="white", bd='0', cursor='hand2', font=Font(size=10, weight='bold'), command=self.Login.ShowWidgets)
            self.LoginButton.pack(pady=10, ipady=8)

            self.SignUp = SignUpUI(self.master, self.MainFrame, self.Login, self.front_color)
            self.SignUpLabelFrame = Frame(self.WidgetsFrame, bg=self.front_color)
            self.SignUpLabelFrame.pack(fill='x', pady=(10, 0), padx=(0, 18))
            self.SignUpLabelLabel = Label(self.SignUpLabelFrame, text='Don\'t have an account?', fg='#211a17', bg=self.front_color, bd=0, font=Font(size=10, underline=True), cursor='hand2')
            self.SignUpLabelLabel.pack(side=RIGHT)

            self.DetailsFrame = Frame(self.MainFrame, bg=self.front_color)
            self.DetailsFrame.pack(pady=(10, 0), padx=(30, 0), side=RIGHT)

            Include.SetWindowPosition(self.master)

            self.master.bind('<Control-r>', self.Retry)
            self.master.bind('<Button-1>', self.ChangeFocus)
            self.master.bind_all('<F5>', self.GetMarketDetails)
            self.CompanyName.ComboBox.bind('<Return>', self.GetMarketDetails)
            self.SignUpLabelLabel.bind('<Button-1>', self.SignUp.ShowWidgets)

            self.master.mainloop()

        else:
            self.SEARCH = Search.Search(self.ShowErrorMessage, self.CheckInternet)
            self.details = self.SEARCH.get_data(company_symbol)

    def Retry(self, event=None):
        '''Retry to get the company names if not retrieved at first'''

        if self.CheckInternet():
            self.OptionValues = self.SEARCH.GetCompaniesNameList()
            self.CompanyName.ComboBox.set(self.DEFAULTTEXT)
            self.CompanyName.ComboBox.config(values=self.OptionValues)
            self.ShowErrorMessage('Retrieved Company Names successfully')

        else:
            self.ShowErrorMessage('Failed to get Company Names. No Internet.\nPress Control + R to retry.', _time=5000)

    def CheckInternet(self):
        '''Check if the user is connected to internet'''

        try:
            requests.get('https://google.com')
            return True

        except requests.ConnectionError:
            return False

    def ChangeFocus(self, event=None):
        '''Change focus to the respective widget where user has clicked'''

        x, y = self.master.winfo_pointerxy()
        widget = self.master.winfo_containing(x, y)

        if not isinstance(widget, (ttk.Combobox, type(None))):
            widget.focus_set()

    def GetMarketDetails(self, event=None):
        '''Display company details if available'''

        for child in self.DetailsFrame.winfo_children():  # Destroying all widgets inside of self.DetailsFrame
            child.destroy()

        error_message = ''
        value = self.CompanyName.ComboVar.get().strip()

        if '(' in value:
            value = value[:value.index('(')]

        # Fonts for the extracted values
        label_font = Font(size=10, weight='bold')
        font1, font2 = Font(size=15), Font(size=10)

        if value and value != self.DEFAULTTEXT:
            if self.CheckInternet():
                details = self.SEARCH.get_data(value)

                company_name = details['company_name']
                sector = details['sector']
                share_value = details['market_price']
                change = details['change']
                date = details['last_traded_on']
                high_low = details['high_low']
                average_value = details['average']

                company_name_label = Label(self.DetailsFrame, text=company_name, font=font1, fg='green', wraplength=250, bg=self.front_color)
                company_name_label.pack(pady=(10, 20))

                # Displaying sector details
                sector_frame = Frame(self.DetailsFrame, bg=self.front_color)
                sector_frame.pack(fill='x')
                sector_label = Label(sector_frame, text="Sector", fg="#333333", font=label_font, bg=self.front_color)
                sector_label.pack(side=LEFT)
                sector_name = Label(sector_frame, text=sector, fg='#1c8b98', font=font2, bg=self.front_color)
                sector_name.pack(side=RIGHT)

                # Displaying current stock value of the company
                market_price_frame = Frame(self.DetailsFrame, bg=self.front_color)
                market_price_frame.pack(fill='x')
                market_label = Label(market_price_frame, text='Market Price', fg="#333333", font=label_font, bg=self.front_color)
                market_label.pack(side=LEFT)
                market_price = Label(market_price_frame, text=share_value, font=Font(size=10, weight='bold'), bg=self.front_color)
                market_price.pack(side=RIGHT)

                # Displaying change percentage
                change_frame = Frame(self.DetailsFrame, bg=self.front_color)
                change_frame.pack(fill='x')
                change_label = Label(change_frame, text='% Change', fg="#333333", font=label_font, bg=self.front_color)
                change_label.pack(side=LEFT)
                change_value = Label(change_frame, text=change, font=font2, bg=self.front_color)
                change_value.pack(side=RIGHT)

                # Displaying last trade date of the company
                last_trade_frame = Frame(self.DetailsFrame, bg=self.front_color)
                last_trade_frame.pack(fill='x')
                last_trade_date_label = Label(last_trade_frame, text='Last Traded On', fg="#333333", font=label_font, bg=self.front_color)
                last_trade_date_label.pack(side=LEFT)
                last_trade_date = Label(last_trade_frame, text=date, width=20, anchor='e', font=font2, bg=self.front_color)
                last_trade_date.pack(side=RIGHT)

                # Displaying high and low price of the company
                high_low_frame = Frame(self.DetailsFrame, bg=self.front_color)
                high_low_frame.pack(fill='x')
                high_low_label = Label(high_low_frame, text='High-Low', fg="#333333", font=label_font, bg=self.front_color)
                high_low_label.pack(side=LEFT)
                high_low_label_value = Label(high_low_frame, text=high_low, width=20, anchor='e', font=font2, bg=self.front_color)
                high_low_label_value.pack(side=RIGHT)

                # Displaying company's average market value of the company
                average_frame = Frame(self.DetailsFrame, bg=self.front_color)
                average_frame.pack(fill='x')
                average_label = Label(average_frame, text='120 Day Average', fg="#333333", font=label_font, bg=self.front_color)
                average_label.pack(side=LEFT)
                average_label_value = Label(average_frame, text=average_value, width=20, anchor='e', font=font2, bg=self.front_color)
                average_label_value.pack(side=RIGHT)

                if (share_value, change, date, high_low, average_value) == ('0.00', '0 %', '', '0.00-0.00', '0.00'):
                    color = '#ff3333'

                else:
                    changed = self.SEARCH.Profit_Loss_Or_Neutral(value)

                    if change == '0 %':  # When company stock price has not been changed
                        color = '#ed9c28'

                    elif 'decrease' in changed:  # When company stock price has been decreased
                        color = '#ff3333'

                    else:  # When company stock price has been increased
                        color = '#0dbe0d'

                market_price.config(fg=color)
                change_value.config(fg=color)

                self.master.update()

            else:
                # When user is not connected to internet
                error_message = 'No Internet Connection'

        else:
            # When user tries to get company market details without
            # inserting any company in the entry widget
            error_message = 'Invalid Company Symbol'

        if error_message:
            self.ShowErrorMessage(error_message)

    def ShowErrorMessage(self, error_message, _time=1500):
        '''
        Show error message when there is no internet and when user
        does not provide any company name

        error_message: The actual error message to display
        _time: For long should the error message be displayed (in millisecond)
        height: Height of window to fit error message        (in pixel)
        '''

        if self.ErrorTimer is None:
            for child in self.DetailsFrame.winfo_children():
                child.destroy()

            pygame.mixer.music.play()

            error_message_var = StringVar()
            error_message_var.set(error_message)

            label = Label(self.DetailsFrame, textvariable=error_message_var, fg='red', font=Font(size=10, weight='bold'), bg=self.front_color)
            label.pack()
            self.ErrorTimer = self.master.after(_time, lambda: self.RemoveErrorMessage(label))

        else:
            self.master.after_cancel(self.ErrorTimer)
            self.ErrorTimer = None
            self.master.after(0, lambda: self.ShowErrorMessage(error_message, _time))

    def RemoveErrorMessage(self, lbl):
        '''Destroy the error message'''

        lbl.destroy()
        temp_frame = Frame(self.DetailsFrame, width=1, height=1)
        temp_frame.pack()
        self.master.update_idletasks()
        temp_frame.destroy()

        self.ErrorTimer = None


if __name__ == '__main__':
    StockTracker()
