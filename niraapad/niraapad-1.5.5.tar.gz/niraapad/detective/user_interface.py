import wx
import wx.lib.scrolledpanel
import ast


#######################################################################

class ConfigVariables:

    """ For distributed setup."""

    def __init__(self, init):
        print('__init__')
    
    def new_config(self, mode, list_of_predicates, init_state_table, transit_table, rule_table):
        print('Creating New File')
    
    def get_from_file(self, mode):
        return variables

    def add_predicate(self, mode, list_of_predicates, init_state_table, transit_table):
        print("Adding Predicates")

    def remove_predicates(self, mode, list_predicate_removal):
        print("Removing Predicates")

    def update_init_state(self, mode, init_state_table):
        print("Updating Initial State")

    def update_transit_table(self, mode, transit_table):
        print("Updating State Transition Table")

    def update_rule_table(self, mode, rule_table):
        print("Updating Rule Table")
    
    def remove_rule(self, mode, rule_table):
        print("Removing Rules")

#######################################################################

class MainFrame(wx.Frame):

    """Frame for creating rule base from scratch or updating the exisiting rule base."""

    def __init__(self):

        """Intilializing user interface frame for main frame."""

        super().__init__(parent=None, title='Generating Rule Base')
        panel = wx.ScrolledWindow(self,-1)
        panel.SetScrollbars(1, 1, 2000, 2000)

    
        new_btn = wx.Button(panel, label='Create Rule Base', pos=(5, 10))
        new_btn.Bind(wx.EVT_BUTTON, self.new_file)


        update_btn = wx.Button(panel, label='Update Rule Base', pos=(5, 60))
        update_btn.Bind(wx.EVT_BUTTON, self.update_file)

        self.Show()
    
    def new_file(self, event):

        """Creating a new config file for rule base."""

        self.Hide()
        adding_predicates_frame = AddingPredicatesFrame(0)
        adding_predicates_frame.Show()

    def update_file(self, event):

        """updating config file for rule base."""

        self.Destroy()
        updating_file_frame = UpdatingFileFrame()
        updating_file_frame.Show()


#######################################################################


class AddingPredicatesFrame(wx.Frame):  

    """Frame for entering list of predicates."""  


    def __init__(self, update):

        """Intilializing user interface frame for entering predicates."""

        super().__init__(parent=None, title='Entering list of predicates')
        panel = wx.ScrolledWindow(self,-1)
        panel.SetScrollbars(1, 1, 2000, 2000)

        wx.StaticText(panel, label = 'Please enter the different predicates as a comma_seperated list (e.g: heater_start,quantos_door,robot_in_heater etc.):')

        self.update = update
        self.predicates = wx.TextCtrl(panel, pos=(5, 20),size=(350,25))

        predicate_btn = wx.Button(panel, label='Submit', pos=(5, 55))
        predicate_btn.Bind(wx.EVT_BUTTON, self.enter_predicates)

        self.Show()

    
    def enter_predicates(self, event):

        """Getting a list of predicates."""

        predicates = self.predicates.GetValue()
        self.list_of_predicates = predicates.split(",")
        self.list_of_predicates = [state.strip() for state in self.list_of_predicates]

        self.Hide()

        initial_state_frame = InitialStateFrame(self, self.update)
        initial_state_frame.Show()


class InitialStateFrame(wx.Frame):

    """Frame for defining the states."""

    def __init__(self, parent, update):

        """Initializing user interface frame for entering the initial state."""

        super().__init__(parent=None, title='Setting Initial State')
        panel = wx.ScrolledWindow(self,-1)
        panel.SetScrollbars(1, 1, 2000, 2000)

        self.predicate_frame_panel = parent
        self.update = update

        wx.StaticText(panel, label = 'Please enter the commands and conditions associated with each predicate for setting the initial state (Note: By default the predicates are set to 0. If the predicates has to be set to 1 without entering the initial commands \n and conditions then enter \'Yes\' in the \'initial commands\' column).')


        wx.StaticText(panel, label = 'Predicate', pos=(5,50))
        wx.StaticText(panel, label = 'Define', pos=(155,50))
        wx.StaticText(panel, label = 'Initial Command', pos=(220,50))
        wx.StaticText(panel, label = 'Initial Conditions', pos=(360,50))
        
        y = 100
        self.init_state_table = []

        for state in parent.list_of_predicates:
            for define in ['0','1']:
            
                wx.StaticText(panel, label = state, pos=(5, y))
                wx.StaticText(panel, label = define, pos=(155, y))
                self.init_command = wx.TextCtrl(panel, pos=(220, y),size=(100,25))
                self.init_conditions = wx.TextCtrl(panel, pos=(360, y),size=(300,25))

                self.init_state_table.append([state, define, self.init_command, self.init_conditions])
                y = y + 50


        submit_btn = wx.Button(panel, label='Submit', pos=(580, y))
        submit_btn.Bind(wx.EVT_BUTTON, self.submit)

        self.Show()

    def submit(self, event):
        
        counter = 0
        for row in self.init_state_table:
            self.init_state_table[counter][2] = row[2].GetValue()
            self.init_state_table[counter][3] = row[3].GetValue()
            counter +=1


        self.predicate_frame_panel.init_state_table = self.init_state_table

        self.Hide()


        if self.update == 0:
            state_transit_frame = StateTransitioningFrame(self)
            state_transit_frame.Show()
        else:
            state_transit_frame = UpdateStateTransitioningFrame(self,self.predicate_frame_panel.list_of_predicates)
            state_transit_frame.Show()
       
            
class StateTransitioningFrame(wx.Frame):

    """Frame for defining the states."""

    def __init__(self, parent):

        """Initializing user interface frame for defining the states."""

        super().__init__(parent=None, title='Defining State Transitions')
        self.panel = wx.ScrolledWindow(self,-1)
        self.panel.SetScrollbars(1, 1, 20000, 20000)

        self.init_state_frame_panel = parent
        self.predicates_frame_panel = parent.predicate_frame_panel

        wx.StaticText(self.panel, label = 'Please enter the preconditions and actions (commands and conditions) for transitioning to different states. In addition, enter the effect of the cause of the action (Note: please enter \'x\' if predicate stays the same).')

      
        wx.StaticText(self.panel, label = 'Preconditions', pos=(5,50))
        wx.StaticText(self.panel, label = 'Command', pos=(255,50))
        wx.StaticText(self.panel, label = 'Conditions', pos=(455,50))

        x = 455
        for predicate in self.predicates_frame_panel.list_of_predicates:
            x = x + 200
            wx.StaticText(self.panel, label = predicate, pos=(x,50))

        
        y = 100
        self.transit_table = []
        self.transit_row = []

        self.preconditions = wx.TextCtrl(self.panel, pos=(5, y),size=(150,25))
        self.transit_row.append(self.preconditions)
        self.command = wx.TextCtrl(self.panel, pos=(255, y),size=(150,25))
        self.transit_row.append(self.command)
        self.conditions = wx.TextCtrl(self.panel, pos=(455, y),size=(150,25))
        self.transit_row.append(self.conditions)
        

        x = 455
        for predicate in self.predicates_frame_panel.list_of_predicates:
            x = x + 200
            self.predicate= wx.TextCtrl(self.panel, pos=(x, y),size=(150,25))
            self.transit_row.append(self.predicate)

        self.transit_table.append(self.transit_row)

        self.transit_row = []

        self.addrow_btn = wx.Button(self.panel, label='Add Row', pos=(x, y+50))
        self.addrow_btn.Bind(wx.EVT_BUTTON, self.add_row)

        self.submit_btn = wx.Button(self.panel, label='Submit', pos=(x, y+100))
        self.submit_btn.Bind(wx.EVT_BUTTON, self.submit)

    
        self.y = y + 50
        self.start_pos = 5

        self.Show()


    def add_row(self, event):

        self.addrow_btn.Hide()
        self.submit_btn.Hide()

        self.transit_row = []
        #self.start_pos = self.start_pos

        self.preconditions = wx.TextCtrl(self.panel, pos=(self.start_pos, self.y),size=(150,25))
        self.transit_row.append(self.preconditions)
        self.command = wx.TextCtrl(self.panel, pos=(self.start_pos  + 250, self.y),size=(150,25))
        self.transit_row.append(self.command)
        self.conditions = wx.TextCtrl(self.panel, pos=(self.start_pos  + 450, self.y),size=(150,25))
        self.transit_row.append(self.conditions)


        x = self.start_pos  + 450
        for predicate in self.predicates_frame_panel.list_of_predicates:
            x = x + 200
            self.predicate= wx.TextCtrl(self.panel, pos=(x, self.y),size=(150,25))
            self.transit_row.append(self.predicate)

        self.transit_table.append(self.transit_row)
        self.transit_row = []

        self.addrow_btn = wx.Button(self.panel, label='Add Row', pos=(x, self.y+50))
        self.addrow_btn.Bind(wx.EVT_BUTTON, self.add_row)

        self.submit_btn = wx.Button(self.panel, label='Submit', pos=(x, self.y+100))
        self.submit_btn.Bind(wx.EVT_BUTTON, self.submit)

        self.y = self.y + 50


    def submit(self, event):
        counter = 0

        for row in self.transit_table:
            for i in range(0,len(self.transit_table[0])):
                self.transit_table[counter][i] = row[i].GetValue()
            counter +=1

        self.predicates_frame_panel.transit_table = self.transit_table

        self.Hide()

        add_rule_frame = AddingRulesFrame(self)
        add_rule_frame.Show()



class AddingRulesFrame(wx.Frame):  

    """Frame for entering list of rules."""  

    def __init__(self, parent):

        """Intilializing user interface frame for entering rules."""

        super().__init__(parent=None, title='Adding Rules')
        self.panel = wx.ScrolledWindow(self,-1)
        self.panel.SetScrollbars(1, 1, 2000, 2000)

        self.state_transit_frame_panel = parent
        self.init_state_frame_panel = parent.init_state_frame_panel
        self.predicates_frame_panel = parent.predicates_frame_panel

        wx.StaticText(self.panel, label = 'Please enter the different bad rules for all states by specifying 0(off),1(on),x(on/off).')


        x = 5
        for predicate in self.predicates_frame_panel.list_of_predicates:
            wx.StaticText(self.panel, label = predicate, pos=(x,50))
            x = x + 200

        
        y = 100
        self.rule_table = []
        self.rule_row = []

        x = 5
        for predicate in self.predicates_frame_panel.list_of_predicates:
            self.predicate_rule = wx.TextCtrl(self.panel, pos=(x, y),size=(150,25))
            self.rule_row.append(self.predicate_rule)
            x = x + 200

        self.rule_table.append(self.rule_row)

        self.rule_row = []

        self.addrow_btn = wx.Button(self.panel, label='Add Row', pos=(x-200, y+50))
        self.addrow_btn.Bind(wx.EVT_BUTTON, self.add_row)

        self.submit_btn = wx.Button(self.panel, label='Submit', pos=(x-200, y+100))
        self.submit_btn.Bind(wx.EVT_BUTTON, self.submit)

    
        self.y = y + 50
        self.start_pos = 5

        self.Show()


    def add_row(self, event):

        self.addrow_btn.Hide()
        self.submit_btn.Hide()

        self.rule_row = []
        #self.start_pos = self.start_pos

        x = self.start_pos
        for predicate in self.predicates_frame_panel.list_of_predicates:
            self.predicate_rule = wx.TextCtrl(self.panel, pos=(x, self.y),size=(150,25))
            self.rule_row.append(self.predicate_rule)
            x = x + 200

        self.rule_table.append(self.rule_row)
        self.rule_row = []

        self.addrow_btn = wx.Button(self.panel, label='Add Row', pos=(x-200, self.y+50))
        self.addrow_btn.Bind(wx.EVT_BUTTON, self.add_row)

        self.submit_btn = wx.Button(self.panel, label='Submit', pos=(x-200, self.y+100))
        self.submit_btn.Bind(wx.EVT_BUTTON, self.submit)

        self.y = self.y + 50


    def submit(self, event):
        counter = 0

        for row in self.rule_table:
            for i in range(0,len(self.rule_table[0])):
                self.rule_table[counter][i] = row[i].GetValue()
            counter +=1
        
        self.predicates_frame_panel.rule_table = self.rule_table

        config_vars = ConfigVariables('__init__')
        config_vars.new_config(1, self.predicates_frame_panel.list_of_predicates, self.init_state_frame_panel.init_state_table, self.state_transit_frame_panel.transit_table, self.rule_table)
       

        self.Destroy()
        self.state_transit_frame_panel.Destroy()
        self.init_state_frame_panel.Destroy()
        self.predicates_frame_panel.Destroy()


#######################################################################


class UpdatingFileFrame(wx.Frame):

    def __init__(self):

        """Intilializing user interface frame for updating frame."""

        super().__init__(parent=None, title='Generating Rule Base')
        panel = wx.ScrolledWindow(self,-1)
        panel.SetScrollbars(1, 1, 2000, 2000)

        add_pred_btn = wx.Button(panel, label='Add Predicates', pos=(5, 5))
        add_pred_btn.Bind(wx.EVT_BUTTON, self.add_predicates)

        remove_pred_btn = wx.Button(panel, label='Remove Predicates', pos=(5, 50))
        remove_pred_btn.Bind(wx.EVT_BUTTON, self.remove_predicates)

        update_initial_states_def_btn = wx.Button(panel, label='Update Initial State Definition', pos=(5, 100))
        update_initial_states_def_btn.Bind(wx.EVT_BUTTON, self.update_initial_state)

        update_transit_def_btn = wx.Button(panel, label='Update States Definition', pos=(5, 150))
        update_transit_def_btn.Bind(wx.EVT_BUTTON, self.update_transit_table)

        add_rules_btn = wx.Button(panel, label='Add/Update Rules', pos=(5, 200))
        add_rules_btn.Bind(wx.EVT_BUTTON, self.update_rules)

        remove_rules_btn = wx.Button(panel, label='Remove Rules', pos=(5, 250))
        remove_rules_btn.Bind(wx.EVT_BUTTON, self.remove_rules)


        self.Show()


    def add_predicates(self, event):

        self.Destroy()

        app = wx.App()
        adding_predicates_frame = AddingPredicatesFrame(1)
        app.MainLoop()

    def remove_predicates(self, event):

        self.Destroy()

        removing_predicates_frame = RemovingPredicatesFrame()
        removing_predicates_frame.Show()

    
    def update_initial_state(self, event):

        self.Destroy()

        removing_predicates_frame = UpdatingInitialStateFrame()
        removing_predicates_frame.Show()


    def update_transit_table(self, event):

        self.Destroy()

        updating_states_frame = UpdateStateTransitioningFrame(None,[])
        updating_states_frame.Show()


    def update_rules(self, event):

        self.Destroy()

        updating_rules_frame = UpdatingRulesFrame()
        updating_rules_frame.Show()

    def remove_rules(self, event):

        self.Destroy()

        removing_rules_frame = RemovingRulesFrame()
        removing_rules_frame.Show()



class UpdateStateTransitioningFrame(wx.Frame):


    def __init__(self, parent, added_predicates):

        """Initializing user interface frame for defining the states."""

        super().__init__(parent=None, title='Generating Rule Base')
        self.panel = wx.ScrolledWindow(self,-1)
        self.panel.SetScrollbars(1, 1, 20000, 20000)

        self.parent = parent
        
        if parent != None:
           self.predicate_frame_panel = parent.predicate_frame_panel
           self.init_state_frame_panel = parent

        config_vars = ConfigVariables('__init__')
        list_of_predicates_response = config_vars.get_from_file(1)
        self.list_of_predicates = ast.literal_eval(list_of_predicates_response.resp)

        config_vars = ConfigVariables('__init__')
        transit_table_response = config_vars.get_from_file(2)
        self.transit_table_init = ast.literal_eval(transit_table_response.resp)

        self.total_predicates = self.list_of_predicates + added_predicates

       
        wx.StaticText(self.panel, label = 'Please enter the preconditions and actions (commands and conditions) for transitioning to different states. In addition, enter the effect of the cause of the action (Note: please enter \'x\' if predicate stays the same).')

      
        wx.StaticText(self.panel, label = 'Preconditions', pos=(5,50))
        wx.StaticText(self.panel, label = 'Command', pos=(255,50))
        wx.StaticText(self.panel, label = 'Conditions', pos=(455,50))

        x = 455
        for predicate in self.total_predicates:
            x = x + 200
            wx.StaticText(self.panel, label = predicate, pos=(x,50))

        
        y = 100
        self.transit_table = []
        self.transit_row = []


        for counter in range(0,len(self.transit_table_init)):
            self.preconditions = wx.TextCtrl(self.panel, pos=(5, y),size=(150,25))
            self.preconditions.SetValue(self.transit_table_init[counter][0])
            self.transit_row.append(self.preconditions)

            self.command = wx.TextCtrl(self.panel, pos=(255, y),size=(150,25))
            self.command.SetValue(self.transit_table_init[counter][1])
            self.transit_row.append(self.command)

            self.conditions = wx.TextCtrl(self.panel, pos=(455, y),size=(150,25))
            self.conditions.SetValue(self.transit_table_init[counter][2])
            self.transit_row.append(self.conditions)
            

            x = 455
            i = 3
            for predicate in self.total_predicates:
                x = x + 200
                self.predicate= wx.TextCtrl(self.panel, pos=(x, y),size=(150,25))
                if i < len(self.transit_table_init[0]):
                    self.predicate.SetValue(str(self.transit_table_init[counter][i]))
                self.transit_row.append(self.predicate)
                i = i + 1

            self.transit_table.append(self.transit_row)

            self.transit_row = []

        self.addrow_btn = wx.Button(self.panel, label='Add Row', pos=(x, y+50))
        self.addrow_btn.Bind(wx.EVT_BUTTON, self.add_row)

        self.submit_btn = wx.Button(self.panel, label='Submit', pos=(x, y+100))
        self.submit_btn.Bind(wx.EVT_BUTTON, self.submit)

    
        self.y = y + 50
        self.start_pos = 5

        self.Show()


    def add_row(self, event):

        self.addrow_btn.Hide()
        self.submit_btn.Hide()

        self.transit_row = []
        self.start_pos = self.start_pos - 1

        self.preconditions = wx.TextCtrl(self.panel, pos=(self.start_pos, self.y),size=(150,25))
        self.transit_row.append(self.preconditions)
        self.command = wx.TextCtrl(self.panel, pos=(self.start_pos  + 250, self.y),size=(150,25))
        self.transit_row.append(self.command)
        self.conditions = wx.TextCtrl(self.panel, pos=(self.start_pos  + 450, self.y),size=(150,25))
        self.transit_row.append(self.conditions)


        x = self.start_pos  + 450
        for predicate in self.total_predicates:
            x = x + 200
            self.predicate= wx.TextCtrl(self.panel, pos=(x, self.y),size=(150,25))
            self.transit_row.append(self.predicate)

        self.transit_table.append(self.transit_row)
        self.transit_row = []

        self.addrow_btn = wx.Button(self.panel, label='Add Row', pos=(x, self.y+50))
        self.addrow_btn.Bind(wx.EVT_BUTTON, self.add_row)

        self.submit_btn = wx.Button(self.panel, label='Submit', pos=(x, self.y+100))
        self.submit_btn.Bind(wx.EVT_BUTTON, self.submit)

        self.y = self.y + 50


    def submit(self, event):
        counter = 0

        for row in self.transit_table:
            for i in range(0,len(self.transit_table[0])):
                self.transit_table[counter][i] = row[i].GetValue()
            counter +=1


        self.Destroy()

        if self.parent != None:
            self.predicate_frame_panel.Destroy()
            config_vars = ConfigVariables('__init__')
            config_vars.add_predicate(2, self.predicate_frame_panel.list_of_predicates,self.init_state_frame_panel.init_state_table,self.transit_table)
            self.predicate_frame_panel.Destroy()
            self.init_state_frame_panel.Destroy()
        else:
            config_vars = ConfigVariables('__init__')
            config_vars.update_transit_table(5,self.transit_table)

class RemovingPredicatesFrame(wx.Frame): 

    def __init__(self):

        """Intilializing user interface frame for updating frame."""

        super().__init__(parent=None, title='Generating Rule Base')
        panel = wx.ScrolledWindow(self,-1)
        panel.SetScrollbars(1, 1, 2000, 2000)

        config_vars = ConfigVariables('__init__')
        list_of_predicates_response = config_vars.get_from_file(1)
        list_of_predicates = ast.literal_eval(list_of_predicates_response.resp)

        transit_table_response = config_vars.get_from_file(2)
        self.transit_table = ast.literal_eval(transit_table_response.resp)

        wx.StaticText(panel, label = 'Please click the box/s for the predicates that need to be removed.')


        y = 20
        for predicate in list_of_predicates:
            cb = wx.CheckBox(panel, label = predicate, pos = (10,y)) 
            y = y + 30

        self.Bind(wx.EVT_CHECKBOX,self.onChecked) 
        self.remove_predicates = {key: False for key in list_of_predicates[::-1]}

        submit_btn = wx.Button(panel, label='Submit', pos=(10, y))
        submit_btn.Bind(wx.EVT_BUTTON, self.submit)


        self.Show()

    def onChecked(self, event): 
       cb = event.GetEventObject() 
       self.remove_predicates[cb.GetLabel()] = cb.GetValue()
    
    def submit(self, event):
        config_vars = ConfigVariables('__init__')
        config_vars.remove_predicates(3,self.remove_predicates)

        self.Destroy()


class UpdatingInitialStateFrame(wx.Frame):

    def __init__(self):

        """Initializing user interface frame for entering the initial state."""

        super().__init__(parent=None, title='Setting Initial State')
        panel = wx.ScrolledWindow(self,-1)
        panel.SetScrollbars(1, 1, 2000, 2000)


        config_vars = ConfigVariables('__init__')
        list_of_predicates_response = config_vars.get_from_file(1)
        self.list_of_predicates = ast.literal_eval(list_of_predicates_response.resp)

        config_vars = ConfigVariables('__init__')
        init_table_response = config_vars.get_from_file(4)
        self.init_table_init = ast.literal_eval(init_table_response.resp)

        wx.StaticText(panel, label = 'Please enter the commands and conditions associated with each predicate for setting the initial state (Note: By default the predicates are set to 0. If the predicates has to be set to 1 without entering the initial commands \n and conditions then enter \'Yes\' in the \'initial commands\' column).')


        wx.StaticText(panel, label = 'Predicate', pos=(5,50))
        wx.StaticText(panel, label = 'Define', pos=(155,50))
        wx.StaticText(panel, label = 'Initial Command', pos=(220,50))
        wx.StaticText(panel, label = 'Initial Conditions', pos=(360,50))
        
        y = 100
        self.init_state_table = []

        i = 0
        for state in self.list_of_predicates:
            for define in ['0','1']:
                    wx.StaticText(panel, label = state, pos=(5, y))
                    wx.StaticText(panel, label = define, pos=(155, y))

                    self.init_command = wx.TextCtrl(panel, pos=(220, y),size=(100,25))
                    self.init_command.SetValue(str(self.init_table_init[i][2]))

                    self.init_conditions = wx.TextCtrl(panel, pos=(360, y),size=(300,25))
                    self.init_conditions.SetValue(str(self.init_table_init[i][3]))

                    self.init_state_table.append([state, define, self.init_command, self.init_conditions])
                    y = y + 50
                    i = i + 1


        submit_btn = wx.Button(panel, label='Submit', pos=(580, y))
        submit_btn.Bind(wx.EVT_BUTTON, self.submit)

        self.Show()

    def submit(self, event):
        
        counter = 0
        for row in self.init_state_table:
            self.init_state_table[counter][2] = row[2].GetValue()
            self.init_state_table[counter][3] = row[3].GetValue()
            counter +=1

        self.Destroy()
        config_vars = ConfigVariables('__init__')
        config_vars.update_init_state(4,self.init_state_table)
        

class UpdatingRulesFrame(wx.Frame):  

    """Frame for entering list of rules."""  

    def __init__(self):

        """Intilializing user interface frame for updating rules."""

        super().__init__(parent=None, title='Adding Rules')
        self.panel = wx.ScrolledWindow(self,-1)
        self.panel.SetScrollbars(1, 1, 2000, 2000)

        config_vars = ConfigVariables('__init__')
        list_of_predicates_response = config_vars.get_from_file(1)
        self.list_of_predicates = ast.literal_eval(list_of_predicates_response.resp)

        config_vars = ConfigVariables('__init__')
        rule_table_response = config_vars.get_from_file(3)
        self.rule_table_init = ast.literal_eval(rule_table_response.resp)

       

        wx.StaticText(self.panel, label = 'Please enter the different bad rules for all states by specifying 0(off),1(on),x(on/off).')

        x = 5
        for predicate in self.list_of_predicates:
            wx.StaticText(self.panel, label = predicate, pos=(x,50))
            x = x + 200

        
        y = 50
        self.rule_table = []

        for counter in range(0, len(self.rule_table_init)):
            self.rule_row = []
            x = 5
            y = y + 50
            for predicate_counter in range(0,len(self.list_of_predicates)):
                self.predicate_rule = wx.TextCtrl(self.panel, pos=(x, y),size=(150,25))
                self.predicate_rule.SetValue(str(self.rule_table_init[counter][predicate_counter]))
                self.rule_row.append(self.predicate_rule)
                x = x + 200
            self.rule_table.append(self.rule_row)

        self.rule_row = []

        self.addrow_btn = wx.Button(self.panel, label='Add Row', pos=(x-200, y+50))
        self.addrow_btn.Bind(wx.EVT_BUTTON, self.add_row)

        self.submit_btn = wx.Button(self.panel, label='Submit', pos=(x-200, y+100))
        self.submit_btn.Bind(wx.EVT_BUTTON, self.submit)

    
        self.y = y + 50
        self.start_pos = 5

        self.Show()


    def add_row(self, event):

        self.addrow_btn.Hide()
        self.submit_btn.Hide()

        self.rule_row = []
        #self.start_pos = self.start_pos

        x = self.start_pos
        for predicate in self.list_of_predicates:
            self.predicate_rule = wx.TextCtrl(self.panel, pos=(x, self.y),size=(150,25))
            self.rule_row.append(self.predicate_rule)
            x = x + 200

        self.rule_table.append(self.rule_row)
        self.rule_row = []

        self.addrow_btn = wx.Button(self.panel, label='Add Row', pos=(x-200, self.y+50))
        self.addrow_btn.Bind(wx.EVT_BUTTON, self.add_row)

        self.submit_btn = wx.Button(self.panel, label='Submit', pos=(x-200, self.y+100))
        self.submit_btn.Bind(wx.EVT_BUTTON, self.submit)

        self.y = self.y + 50


    def submit(self, event):
        counter = 0

        for row in self.rule_table:
            for i in range(0,len(self.rule_table[0])):
                self.rule_table[counter][i] = row[i].GetValue()
            counter +=1

        config_vars = ConfigVariables('__init__')
        config_vars.update_rule_table(6,self.rule_table)
        self.Destroy()

class RemovingRulesFrame(wx.Frame):  

    def __init__(self):

        super().__init__(parent=None, title='Generating Rule Base')
        panel = wx.ScrolledWindow(self,-1)
        panel.SetScrollbars(1, 1, 2000, 2000)

        wx.StaticText(panel, label = 'Please click the box/s for the rules that need to be removed:')


        config_vars = ConfigVariables('__init__')
        list_of_predicates_response = config_vars.get_from_file(1)
        self.predicates = ast.literal_eval(list_of_predicates_response.resp)

        config_vars = ConfigVariables('__init__')
        rules_table_response = config_vars.get_from_file(3)
        self.rules_table = ast.literal_eval(rules_table_response.resp)

        self.no_of_rules = len(self.rules_table)


        x = 100
        y = 20
        for state in self.predicates:
            wx.StaticText(panel, label = state, pos=(x, y))
            x = x + 100
        
       
        x = 20
        y = 40

        
        for i in range(0, self.no_of_rules):
            x = 20
            label = 'Rule ' + str(i+1)
            wx.CheckBox(panel, label = label, pos=(x, y))
            for j in range(0,len(self.predicates)):
                value = wx.StaticText(panel, label = str(self.rules_table[i][j]), pos=(x + 100, y))
                x = x + 100
            y = y + 40
        

        self.Bind(wx.EVT_CHECKBOX,self.onChecked) 
        self.remove_rules = {key: False for key in range(int(self.no_of_rules), 0, -1)}

        submit_btn = wx.Button(panel, label='Submit', pos=(x, y))
        submit_btn.Bind(wx.EVT_BUTTON, self.submit)



        self.Show()

    def onChecked(self, event): 

        cb = event.GetEventObject() 
        self.remove_rules[int(cb.GetLabel().split(' ')[1])] = cb.GetValue()
    
    def submit(self, event):

        config_vars = ConfigVariables('__init__')
        config_vars.remove_rule(7,self.remove_rules)

        self.Destroy()