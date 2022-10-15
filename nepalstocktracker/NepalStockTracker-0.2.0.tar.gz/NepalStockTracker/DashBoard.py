from logging import exception
import threading
from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox

try:  # When used as a package
    from NepalStockTracker.db import DB
    from NepalStockTracker import exceptions
    import NepalStockTracker._photo_image as pi
    from NepalStockTracker._ComboBox import _ComboBox

except ImportError:  # When used as a normal script
    import exceptions
    from db import DB
    import _photo_image as pi
    from _ComboBox import _ComboBox


class DashBoard:
    '''
    Show the information of respective user when
    user logs in successfully
    '''

    def __init__(self, master, ComboValues, LOGIN, MainFrame, search, destroy_main_frame=None):
        self.sn = 0
        self.db = DB()
        self.LOGIN = LOGIN
        self.master = master
        self.PrevHash = None
        self.pi = pi.Image()
        self.RightBG = '#15c2af'
        self.MainFrame = MainFrame
        self.ComboValues = ComboValues
        self.username = self.LOGIN.username
        self.destroy_main_frame = destroy_main_frame

        self.SEARCH = search
        self.EndThread = False

    def ShowWidgets(self):
        '''
        Show corresponding widgets
        '''

        self.MainFrame.pack_forget()
        self.ThreadEvent = threading.Event()
        self.master.title('Nepal Stock Tracker | DashBoard')

        self.DashboardFrame = Frame(self.master, bg=self.RightBG)
        self.DashboardFrame.pack()

        self.LogOutButton = Button(self.DashboardFrame, image=self.pi.LogoutImage, bd=0, cursor='hand2', bg=self.RightBG, activebackground=self.RightBG, command=self.LogOutButtonCommand)
        self.LogOutButton.pack(side=RIGHT, fill='y')

        self.LeftFrame = Frame(self.DashboardFrame)
        self.LeftFrame.pack(side=LEFT)
        self.RightFrame = Frame(self.DashboardFrame, bg=self.RightBG)
        self.RightFrame.pack(side=RIGHT)

        self.LeftImage = Label(self.LeftFrame, image=self.pi.DashBoardImage, bg='#a4f5ec')
        self.LeftImage.pack()

        self.ComboFrame = Frame(self.RightFrame, bg=self.RightBG)
        self.ComboFrame.pack(pady=15)

        self.combobox = _ComboBox(self.master, self.ComboFrame, self.ComboValues)
        self.combobox.ComboBox.pack(side=LEFT, ipady=3)
        self.add_button = Button(self.ComboFrame, image=self.pi.AddImage, bd=0, cursor='hand2', bg=self.RightBG, activebackground=self.RightBG, command=self.AddButtonCommand)
        self.add_button.pack(side=LEFT)

        self.TreeviewFrame = Frame(self.RightFrame)
        self.TreeviewFrame.pack(pady=(0, 10), padx=20)
        self.Treeview = ttk.Treeview(self.TreeviewFrame, columns=('SN', 'Scrip', 'Sector', 'Price'), show='headings', height=15)
        self.Treeview.pack(side=LEFT)

        self.Scrollbar = ttk.Scrollbar(self.TreeviewFrame, orient='vertical', command=self.Treeview.yview)
        self.ShowScrollBar()

        self.BackButton = Button(self.RightFrame, image=self.pi.BackImage, bd=0, cursor='hand2', bg=self.RightBG, activebackground=self.RightBG, command=self.BackButtonCommand)
        self.BackButton.pack(pady=(20, 10))

        self.Treeview.column('SN', width=50, anchor='center')
        self.Treeview.column('Scrip', width=100, anchor='center')
        self.Treeview.column('Price', width=100, anchor='center')
        self.Treeview.column('Sector', width=300, anchor='center')

        self.Treeview.heading('SN', text='SN')
        self.Treeview.heading('Scrip', text='Scrip')
        self.Treeview.heading('Sector', text='Sector')
        self.Treeview.heading('Price', text='Price')

        self.Treeview.bind('<Button-3>', self.RightClick)
        self.Treeview.bind('<Motion>', self.RestrictResizingHeading)

        self.Threads = []

        for func in [self.InsertAtFirst, self.UpdateMarketPrice]:
            thread = threading.Thread(target=func)
            self.Threads.append(thread)

        for thread in self.Threads:
            thread.start()

    def RestrictResizingHeading(self, event):
        '''
        Restrict user to resize the columns of Treeview
        '''

        if self.Treeview.identify_region(event.x, event.y) == "separator":
            return "break"

    def ShowScrollBar(self):
        '''
        Show ScrollBar when the contents of TreeView is
        more than the height of TreeView
        '''

        if self.Treeview.cget('height') < len(self.Treeview.get_children()):
            self.Scrollbar.pack(side=RIGHT, fill='y')
            self.Treeview.config(yscrollcommand=self.Scrollbar.set)

            self.ScrollBarUpdateTimer = self.master.after(250, self.HideScrollBar)

        else:
            self.ScrollBarUpdateTimer = self.master.after(250, self.ShowScrollBar)

    def HideScrollBar(self):
        '''
        Hide ScrollBar when the contents of TreeView is
        less or equal than the height of TreeView
        '''

        if self.Treeview.cget('height') >= len(self.Treeview.get_children()):
            self.Scrollbar.pack_forget()
            self.ScrollBarUpdateTimer = self.master.after(250, self.ShowScrollBar)

        else:
            self.ScrollBarUpdateTimer = self.master.after(250, self.HideScrollBar)

    def UpdateMarketPrice(self):
        '''
        Update changed market_price of respective company in Treeview
        '''

        for child in self.Treeview.get_children():
            thread = threading.Thread(target=self.ModifyTreeView, args=(child,), daemon=True)
            thread.start()

        self.UpdateMarketPriceTimer = self.master.after(250, self.UpdateMarketPrice)

    def ModifyTreeView(self, child):
        '''
        This function actually searches current market_price from
        the web, compares it with the current one present in the
        TreeView and changes the current one with the fetched one
        if it has been changed.

        When the search is being done, it takes a little time(like 5sec) which
        freezes the window for that about of time. To prevent this , this
        function gets called from the threading module.
        '''

        tree_view_value = self.Treeview.item(child)['values']

        tree_view_company_abbr = tree_view_value[1]
        tree_view_value_market_value = tree_view_value[-1]

        web_market_value = self.GetData(tree_view_company_abbr)

        if web_market_value is not None:
            web_market_value = web_market_value[-1]

            if tree_view_value_market_value != web_market_value:
                insert_value = tree_view_value[:-1] + [web_market_value]

                self.Treeview.item(child, values=insert_value)

    def GetData(self, company):
        '''
        Get values required to insert at TreeView
        '''

        try:
            details = self.SEARCH.get_data(company)
            return [company, details['sector'], details['market_price']]

        except exceptions.ConnectionError:
            return None

    def InsertAtFirst(self):
        '''
        Insert values stored in files each time when dashboard is shown
        '''

        companies = self.db.ReadJSON()[self.username]['companies']

        for company in companies:
            try:
                self.InsetToTreeView(company)

            except RuntimeError:
                self.EndThread = True
                return

    def InsetToTreeView(self, FromComboBox):
        '''
        Insert values to the TreeView
        '''

        self.sn += 1
        details = self.GetData(FromComboBox)

        if details is not None:
            values = [self.sn] + details
            self.Treeview.insert('', END, values=values)

    def AddButtonCommand(self):
        '''
        Add selected company to respective user
        '''

        FromComboBox = self.combobox.ComboVar.get().strip()

        if FromComboBox not in self.combobox.values:
            messagebox.showerror('ERR', 'Select valid company name')

        else:
            contents = self.db.ReadJSON()
            username = self.LOGIN.username

            FromComboBox = FromComboBox.split()[0]
            companies = contents[username]['companies']

            if FromComboBox not in companies:
                companies.append(FromComboBox)

                contents[username]['companies'] = companies
                self.db.WriteJSON(contents)

                thread = threading.Thread(target=self.InsetToTreeView, args=(FromComboBox,))
                thread.start()

            self.combobox.ComboVar.set('COMPANY NAME')

    def LogOutButtonCommand(self):
        '''
        Logs out of the current logged in account
        '''

        self.LOGIN.username = None
        self.BackButtonCommand()

    def RightClick(self, event=None):
        '''
        When user right clicks inside Treeview
        '''

        CurrentSelections = self.Treeview.selection()
        RightClickMenu = Menu(self.master, tearoff=False)
        iid = self.Treeview.identify_row(event.y)

        if not CurrentSelections and not iid:
            return

        if not CurrentSelections:
            self.Treeview.selection_set(iid)

        RightClickMenu.add_command(label='Delete', activeforeground='white', activebackground='red', command=self.RightClickDelete)

        try:
            RightClickMenu.post(event.x_root, event.y_root)

        finally:
            RightClickMenu.grab_release()

    def RightClickDelete(self):
        '''
        Delete the selected company(ies) when
        clicked to delete option from right click
        '''

        contents = self.db.ReadJSON()
        CurrentSelections = self.Treeview.selection()

        if CurrentSelections:
            companies = contents[self.username]['companies']

            for selection in CurrentSelections:
                values = self.Treeview.item(selection)['values'][1]
                companies.remove(values)
                self.Treeview.delete(selection)

            contents[self.username]['companies'] = companies
            self.db.WriteJSON(contents)

            for idx, child in enumerate(self.Treeview.get_children()):
                index = idx + 1
                values = self.Treeview.item(child)['values']

                if values[0] != index:
                    values[0] = index
                    self.Treeview.item(child, values=values)

    def BackButtonCommand(self):
        '''
        Display homepage when user clicks back
        button or log-out button
        '''

        self.EndThread = True
        self.master.after_cancel(self.ScrollBarUpdateTimer)
        self.master.after_cancel(self.UpdateMarketPriceTimer)

        if self.destroy_main_frame is None:
            self.destroy_main_frame = self.MainFrame

        self.DashboardFrame.destroy()
        self.destroy_main_frame.pack(padx=50, pady=50)

        self.master.title('Nepal Stock Tracker')
