import pandas as pd
import numpy as np
import sys
import json
import re
import ast
from configparser import ConfigParser
import os
import re

file_path = os.path.dirname(os.path.abspath(__file__))
niraapad_path = os.path.dirname(file_path)
sys.path.append(niraapad_path)

import niraapad.detective.deck

def isfloat(element):
    try:
        float(element)
        return True
    except ValueError:
        return False


class Detective:

    """The detector class updates the states at run time
       and informs the user if predefined rules are violated."""

    def __init__(self, configdir):

        print("Initializing Detector")

        file_exist = os.path.exists(configdir)
        if file_exist == False:
            raise Exception('Config File is not available. Please disable IDS.')
            
        self.list_of_predicates = pd.read_excel(configdir, sheet_name='list_of_predicates',  engine='openpyxl')['List of Predicates'].tolist()
        self.init_state_table = pd.read_excel(configdir, sheet_name='init_state_table',  engine='openpyxl').replace(np.nan,'').astype(str)
        self.transit_table = pd.read_excel(configdir, sheet_name='transit_table',  engine='openpyxl').replace(np.nan,'').astype(str)
        self.rule_table = pd.read_excel(configdir, sheet_name='rule_table',  engine='openpyxl').replace(np.nan,'').astype(str)
   
        predicate = [list('0' * len(self.list_of_predicates))]
        self.current_state = pd.DataFrame(data = predicate,
                                    index = ['predicates'],
                                    columns = self.list_of_predicates)
        
        self.current_state = self.setting_initial_state(self.current_state)


    def setting_initial_state(self, current_state):

        skip_check = 0
        for index,row in self.init_state_table.iterrows():

            if skip_check == 1:
                skip_check = 0
                continue
            elif row['Initial Command'] == '':
                continue
            elif row['Initial Command'] == 'Yes':
                current_state[row['Predicate']]['predicates'] = str(row['Define'])
                if index%2 != 0:
                    skip_check = 1
            else:
                try:
                    variables  = eval('niraapad.detective.deck.' + row['Initial Command'] + '()')
                except:
                    variables  = eval('niraapad.detective.deck.' + row['Initial Command'])
            
                if type(variables) == str or type(variables) == int or type(variables) == float:
                    row['Initial Conditions'] = row['Initial Conditions'].replace(row['Initial Conditions'].split()[0],'variables')
                    if type(variables) == str:
                        row['Initial Conditions'] = row['Initial Conditions'].replace(row['Initial Conditions'].split()[2], '\'' + row['Initial Conditions'].split()[2] + '\'')
                    locals().update(variables)
                elif type(variables) == dict:
                    locals().update(variables)
                elif type(variables) == list:
                    items = row['Initial Conditions'].split()
                    variables = list(variables)
                    counter = 0
                    for i in range(0,len(items),4):
                        items[i] = 'variables[' + str(counter) + ']'
                        counter += 1
                    row['Initial Conditions'] = ' '.join(items)
                    locals().update(variables)
                else:
                    variables = str(variables)

                if '(' in variables and ')' in variables:
                    variables = variables.split('(')[1].replace(')','').replace('=',': ')
                    variables = dict(subString.split(": ") for subString in variables.split(", "))
                    variables = dict([a, float(x) if isfloat(x) else x] for a, x in variables.items())
                    locals().update(variables)
                


                check = 0
                ldic = locals()
                conditional_statement = 'if ' + row['Initial Conditions'] + ':\n   check = 1'
                exec(conditional_statement,globals(),ldic)
                check = ldic['check']
                if check == 0:
                    if str(row['Define']) == '0':
                        current_state[row['Predicate']]['predicates'] = '1'
                    else:
                        current_state[row['Predicate']]['predicates'] = '0'
                else:
                    current_state[row['Predicate']]['predicates'] = str(row['Define'])

                if index%2 != 0:
                    skip_check = 1
            
        return current_state
                    



    def updating_the_states(self, update_state, cmd, args):
            """Updates the temp_update_state according to command, arguments and preconditions passed."""

            # Convert args into variables to be evaluated
            if args != None:
                rept_check = 0
                for key, value in args.copy().items():
                    try:
                        args[key] = ast.literal_eval(value)
                        lst_value = dict([key+'_'+ str(i), args[key][i]] for i in range(0,len(args[key])))
                        args = {**args, **lst_value}
                        args.pop(key)
                    except:
                        if isfloat(value):
                            args[key] = float(value)
                        elif '(' in value and ')' in value:
                            value = value.split('(')[1].replace(')','').replace('=',': ')
                            value = dict(subString.split(": ") for subString in value.split(", "))
                            if rept_check == 1:
                                value = dict([a+'_1', float(x) if isfloat(x) else x] for a, x in value.items())
                            else:
                                value = dict([a, float(x) if isfloat(x) else x] for a, x in value.items())
                                rept_check = 1
                            args = {**args, **value}
                            args.pop(key)
                        
                                            
            locals().update(args)
            
            # Extract the preconditions into lists
            for index, row in self.transit_table.iterrows():
                precond_check = 0
                ldic = locals()
                

                if row['Preconditions'] != '':
                    condition = 'if '
                    state_conds = row['Preconditions'].split()
                    for word in state_conds:
                        if word not in ['and','or','not']:
                            if update_state[word]['predicates'] == '0':
                                condition = condition + '0'
                            else:
                                condition = condition + '1'
                        else:
                            condition =  condition + ' ' + word + ' '
                    
                    condition = condition + ':\n   precond_check = 1'
                    exec(condition,globals(),ldic)
                    precond_check = ldic['precond_check']
                else:
                    precond_check = 1

                # preconditions are met
                if precond_check == 1:
                   

                    # Check if command and args are met          
                    if row['Command'] == cmd:
                        if args == None:
                            #Accepting the state
                            for predicate in self.list_of_predicates:
                                if row[predicate] != 'x':
                                    update_state[predicate]['predicates'] = str(row[predicate])
                            break
                        elif row['Conditions'] == None:
                            #Accepting the state
                            for predicate in self.list_of_predicates:
                                if row[predicate] != 'x':
                                    update_state[predicate]['predicates'] = str(row[predicate])
                            break
                        else:
                            
                            args_cond = 0
                            adic = locals()
                            exec('if ' + row['Conditions']  + ":\n  args_cond = 1", globals(),adic)
                            args_cond = adic['args_cond']
                            # Arguments are met
                            if args_cond == 1:
                                #Accepting the state
                                for predicate in self.list_of_predicates:
                                    if row[predicate] != 'x':
                                        update_state[predicate]['predicates'] = str(row[predicate])
                                break
                    
            
            return update_state


    def detection_using_rules(self, state):

        """Detect if the rules in the 2d table are violated, returns 0(good) or 1(bad)."""

        for index, row in self.rule_table.iterrows():
            tmp_row = ''.join(row).replace('x',"[01]")
            state_list = state.values.tolist()
            malicious = re.match(tmp_row, ''.join(state_list[0]))

            if malicious != None:
                return 1, 'Rule_'+ str(index+1)
            
        return 0, "No Rule Violated"


    def alarm(self, cmd, args):

        """Raising an alarm if there is a malicious activity."""
            
        ## Check if current state is bad
        
        init_malicious, rule = self.detection_using_rules(self.current_state)
   
        if init_malicious == 0:

            ## Updating state
            pre_state = self.current_state.iloc[0].tolist()
            
            self.temp_update_state = self.current_state

            self.temp_update_state = self.updating_the_states(self.temp_update_state, cmd, args)


            ## Detection (Bad)
            malicious, rule = self.detection_using_rules(self.temp_update_state)

            if malicious == 1:
                return 'malicious', rule, pre_state, self.temp_update_state.iloc[0].tolist()
            else:
                self.current_state = self.temp_update_state
                return 'run_cmd', rule, pre_state, self.temp_update_state.iloc[0].tolist()
        else:
            return 'malicious', rule, [], self.current_state.iloc[0].tolist()

    
