import argparse
import os
import sys
import wx
import unittest
import argparse
import ast
from configparser import ConfigParser
import pandas as pd
import numpy as np

#Path to this file test_niraapad.py
file_path = os.path.dirname(os.path.abspath(__file__))
niraapad_path = os.path.dirname(os.path.dirname(file_path))
sys.path.append(niraapad_path)


import niraapad.backends
from niraapad.middlebox.niraapad_server import NiraapadServer
from niraapad.lab_computer.niraapad_client import NiraapadClient
import niraapad.shared.utils as utils
from niraapad.detective.detector import Detective

from niraapad.detective.user_interface import AddingPredicatesFrame,InitialStateFrame,StateTransitioningFrame,AddingRulesFrame,UpdateStateTransitioningFrame,UpdatingRulesFrame,RemovingRulesFrame,RemovingPredicatesFrame,UpdatingInitialStateFrame



parser = argparse.ArgumentParser()
parser.add_argument(
    '-D',
    '--distributed',
    help=
    'Distributed testing. Do not start server. Assume it is started on the provided host and port.',
    action="store_true")
parser.add_argument(
    '-H',
    '--host',
    default='localhost',
    help='Provide server hostname or IP address. Defaults to "localhost".',
    type=str)
parser.add_argument('-P',
                    '--port',
                    default='1337',
                    help='Provide the server port. Defaults to 1337.',
                    type=str)
parser.add_argument(
    '-C',
    '--configdir',
    default=os.path.join(niraapad_path, "niraapad", "detective", "config.xlsx"),
    help=
    'Provide path to the trace directory. Defaults to <project-dir>/niraapad/detective/config.xlsx.',
    type=str)


args = parser.parse_args()



class TestUserInterface(unittest.TestCase):

    def setUp(self):

        NiraapadClient.connect_to_middlebox(args.host,
                                            args.port)
        self.configdir = args.configdir

    def tearDown(self):
        if args.distributed == False:
            self.niraapad_server.stop()
            del self.niraapad_server


    def test_new_file(self):
        for mo in utils.MO:
            if mo != utils.MO.VIA_MIDDLEBOX:
                continue
            NiraapadClient.update_mos(default_mo=mo, debug=False)

            app = wx.App()
            add_frame = AddingPredicatesFrame(0)
            app.MainLoop()
      
            list_of_predicates = add_frame.list_of_predicates
            init_state_table = add_frame.init_state_table
            transit_table = add_frame.transit_table
            rule_table = add_frame.rule_table

            list_of_predicates_df = pd.read_excel(self.configdir, sheet_name='list_of_predicates',  engine='openpyxl')['List of Predicates'].tolist()
            init_state_table_df = pd.read_excel(self.configdir,  sheet_name='init_state_table',  engine='openpyxl').replace(np.nan, '').astype(str).values.tolist()
            transit_table_df = pd.read_excel(self.configdir, sheet_name='transit_table',  engine='openpyxl').replace(np.nan, '').astype(str).values.tolist()
            rule_table_df = pd.read_excel(self.configdir, sheet_name='rule_table',  engine='openpyxl').replace(np.nan, '').astype(str).values.tolist()


            self.assertEqual(list_of_predicates, list_of_predicates_df)
            self.assertEqual(init_state_table, init_state_table_df)
            self.assertEqual(transit_table, transit_table_df)
            self.assertEqual(rule_table, rule_table_df)
        

    def test_add_predicates(self):
        for mo in utils.MO:
            if mo != utils.MO.VIA_MIDDLEBOX:
                continue
            NiraapadClient.update_mos(default_mo=mo, debug=False)

            list_of_predicates_df = pd.read_excel(self.configdir, sheet_name='list_of_predicates',  engine='openpyxl')['List of Predicates'].tolist()
            init_state_table_df = pd.read_excel(self.configdir,  sheet_name='init_state_table',  engine='openpyxl').replace(np.nan, '').astype(str).values.tolist()
           
           

            app = wx.App()
            add_frame = AddingPredicatesFrame(1)
            app.MainLoop()

            list_of_predicates = list_of_predicates_df + add_frame.list_of_predicates
            init_state_table = init_state_table_df + add_frame.init_state_table

            list_of_predicates_df = pd.read_excel(self.configdir, sheet_name='list_of_predicates',  engine='openpyxl')['List of Predicates'].tolist()
            init_state_table_df = pd.read_excel(self.configdir,  sheet_name='init_state_table',  engine='openpyxl').replace(np.nan, '').astype(str).values.tolist()
           


            self.assertEqual(list_of_predicates, list_of_predicates_df)
            self.assertEqual(init_state_table, init_state_table_df)


    def test_remove_predicates(self):

        for mo in utils.MO:
            if mo != utils.MO.VIA_MIDDLEBOX:
                continue
            NiraapadClient.update_mos(default_mo=mo, debug=False)

            app = wx.App()
            remove_frame = RemovingPredicatesFrame()
            app.MainLoop()

            removed_predicates = [k for k, v in remove_frame.remove_predicates.items() if v is False]
            removed_predicates.reverse()

            list_of_predicates_df = pd.read_excel(self.configdir, sheet_name='list_of_predicates',  engine='openpyxl')['List of Predicates'].tolist()

            self.assertEqual(removed_predicates, list_of_predicates_df)
    

    def test_update_init(self):

        for mo in utils.MO:
            if mo != utils.MO.VIA_MIDDLEBOX:
                continue
            NiraapadClient.update_mos(default_mo=mo, debug=False)

            app = wx.App()
            update_frame = UpdatingInitialStateFrame()
            app.MainLoop()

            init_state_table_df = pd.read_excel(self.configdir,  sheet_name='init_state_table',  engine='openpyxl').replace(np.nan, '').astype(str).values.tolist()
        
            self.assertEqual(update_frame.init_state_table, init_state_table_df)

    def test_update_transit(self):

        for mo in utils.MO:
            if mo != utils.MO.VIA_MIDDLEBOX:
                continue
            NiraapadClient.update_mos(default_mo=mo, debug=False)

            app = wx.App()
            update_frame = UpdateStateTransitioningFrame(None,[])
            app.MainLoop()

            transit_table_df = pd.read_excel(self.configdir,  sheet_name='transit_table',  engine='openpyxl').replace(np.nan, '').astype(str).values.tolist()
        
            self.assertEqual(update_frame.transit_table, transit_table_df)
    
    def test_update_rule(self):

        for mo in utils.MO:
            if mo != utils.MO.VIA_MIDDLEBOX:
                continue
            NiraapadClient.update_mos(default_mo=mo, debug=False)

            app = wx.App()
            rule_frame = UpdatingRulesFrame()
            app.MainLoop()

            rule_table_df = pd.read_excel(self.configdir,  sheet_name='rule_table',  engine='openpyxl').replace(np.nan, '').astype(str).values.tolist()
        
            self.assertEqual(rule_frame.rule_table, rule_table_df)


    def test_remove_rules(self):

        for mo in utils.MO:
            if mo != utils.MO.VIA_MIDDLEBOX:
                continue
            NiraapadClient.update_mos(default_mo=mo, debug=False)

            rules_table = pd.read_excel(self.configdir, sheet_name='rule_table',  engine='openpyxl').replace(np.nan, '').astype(str).values.tolist()


            app = wx.App()
            remove_frame = RemovingRulesFrame()
            app.MainLoop()

            for key, value in remove_frame.remove_rules.items():
                if value == True:
                    a = rules_table.pop(int(key) - 1)


            rule_table_df = pd.read_excel(self.configdir, sheet_name='rule_table',  engine='openpyxl').replace(np.nan, '').astype(str).values.tolist()

            self.assertEqual(rules_table, rule_table_df)



class TestDetector(unittest.TestCase):

    def setUp(self):

        if args.distributed == False:
            NiraapadClient.connect_to_middlebox(args.host,
                                            args.port)
            self.niraapad_server.start()

        NiraapadClient.connect_to_middlebox(args.host,
                                            args.port)
        self.configdir = args.configdir


        list_of_predicates = ['start_heater', 'quantos_door', 'pump_liquid', 'robot_region_quantos']
        list_of_predicates_df = pd.DataFrame(list_of_predicates, columns = ['List of Predicates'])

        init_state_table = [['start_heater','0','',''],['start_heater','1','',''],['quantos_door','0','quan.test_front_door_position','pos == CLOSE'],['quantos_door','1','quan.test_front_door_position','pos == OPEN'],['pump_liquid','0','',''],['pump_liquid','1','Yes',''],['robot_region_quantos','0','',''],['robot_region_quantos','1','robo.test_get_robot_pos','x > 23 and y < 45']]
        init_state_table_df = pd.DataFrame(init_state_table, columns = ['Predicate', 'Define', 'Initial Command', 'Initial Conditions'])

        
        transit_table = [['not start_heater','START_1','','1','x','x','x'],['start_heater','STOP_1','','0','x','x','x'],['quantos_door','CLOSE_DOOR','','x','0','x','x'],['not quantos_door','CLOSE_DOOR','','x','1','x','x'],['not pump_liquid','PUMP','','x','x','1','x'],['pump_liquid','DISPENSE','','x','x','0','x'],['not robot_region_quantos and not quantos_door','MOVE','x > 23 and y < 45','x','x','x','1']]
        transit_table_df = pd.DataFrame(transit_table, columns = ['Preconditions', 'Command', 'Conditions'] + list_of_predicates)
        
        rule_table = [['x', '0', 'x', '1'], ['1', 'x', '1', 'x'], ['1', '1', 'x', 'x']]
        rule_table_df = pd.DataFrame(rule_table, columns = list_of_predicates)


        writer = pd.ExcelWriter(self.configdir, engine='xlsxwriter')

        list_of_predicates_df.to_excel(writer, sheet_name='list_of_predicates', index=False)
        init_state_table_df.to_excel(writer, sheet_name='init_state_table', index=False)
        transit_table_df.to_excel(writer, sheet_name='transit_table', index=False)
        rule_table_df.to_excel(writer, sheet_name='rule_table', index=False)

        writer.save()

    def tearDown(self):
        if args.distributed == False:
            self.niraapad_server.stop()
            del self.niraapad_server

    def test_initial_state(self):
        for mo in utils.MO:
            if mo != utils.MO.VIA_MIDDLEBOX:
                continue
            NiraapadClient.update_mos(default_mo=mo, debug=False)

            expected_init_state = ['0','1','1','0']

            detector = Detective(self.configdir)
            self.assertEqual(detector.current_state.values.tolist()[0],expected_init_state)


    def test_updating_state(self):
        for mo in utils.MO:
            if mo != utils.MO.VIA_MIDDLEBOX:
                continue
            NiraapadClient.update_mos(default_mo=mo, debug=False)

            cmd = ['START_1','DISPENSE','CLOSE_DOOR','MOVE']
            args = [None,None,None, {'x': 24, 'y': 15}]

            detector = Detective(self.configdir)
            
            update_state = detector.current_state
            expected_state = ['1','0','0','1'] 

            for i in range(0, len(cmd)):
                update_state =  detector.updating_the_states(update_state, cmd[i], args[i])

            self.assertEqual(update_state.values.tolist()[0],expected_state)

    def test_detecting_rules(self):
        for mo in utils.MO:
            if mo != utils.MO.VIA_MIDDLEBOX:
                continue
            NiraapadClient.update_mos(default_mo=mo, debug=False)

            list_of_predicates = ['start_heater', 'quantos_door', 'pump_liquid', 'robot_region_quantos']

            detector = Detective(self.configdir)
            state = detector.current_state


            state[list_of_predicates[0]]['predicates'] = '1'
            state[list_of_predicates[1]]['predicates'] = '0'
            state[list_of_predicates[2]]['predicates'] = '1'
            state[list_of_predicates[3]]['predicates'] = '1'

            expected_activity = 1
            expected_rule = 'Rule_1'
            
            malicious, rule = detector.detection_using_rules(state)
            print(malicious,rule)
            
            self.assertEqual(malicious, expected_activity)
            self.assertEqual(rule, expected_rule)


            state[list_of_predicates[0]]['predicates'] = '1'
            state[list_of_predicates[1]]['predicates'] = '0'
            state[list_of_predicates[2]]['predicates'] = '1'
            state[list_of_predicates[3]]['predicates'] = '0'

            expected_activity = 1
            expected_rule = 'Rule_2'
            
            
            malicious, rule = detector.detection_using_rules(state)

            
            self.assertEqual(malicious, expected_activity)
            self.assertEqual(rule, expected_rule)



            state[list_of_predicates[0]]['predicates'] = '0'
            state[list_of_predicates[1]]['predicates'] = '0'
            state[list_of_predicates[2]]['predicates'] = '0'
            state[list_of_predicates[3]]['predicates'] = '0'

            expected_activity = 0
            expected_rule = 'No Rule Violated'
            
            
            malicious, rule = detector.detection_using_rules(state)

            self.assertEqual(malicious, expected_activity)
            self.assertEqual(rule, expected_rule)

    def test_alarm(self):
        for mo in utils.MO:
            if mo != utils.MO.VIA_MIDDLEBOX:
                continue
            NiraapadClient.update_mos(default_mo=mo, debug=False)

        
            cmd = ['START_1','DISPENSE','CLOSE_DOOR','MOVE']
            args = [None,None,None, {'x': 24, 'y': 15}]

            expected_rules = ['Rule_2','Rule_3','','Rule_1']


            for i in range(0, len(cmd)):
                detector = Detective(self.configdir)
                state, rule, pre_state, tmp_state = detector.alarm(cmd[i], args[i])
                if state == 'malicious':
                    expected_activity = 'malicious'
                    self.assertEqual(state, expected_activity)
                    self.assertEqual(rule, expected_rules[i])
                else:
                    expected_activity = 'run_cmd'
                    expected_rule = 'No Rule Violated'
                    self.assertEqual(state, expected_activity)
                    self.assertEqual(rule, expected_rule)


def suite_user_interface():
    suite = unittest.TestSuite()
    # suite.addTest(TestUserInterface('test_new_file'))
    # suite.addTest(TestUserInterface('test_add_predicates'))
    # suite.addTest(TestUserInterface('test_remove_predicates'))
    # suite.addTest(TestUserInterface('test_update_init'))
    # suite.addTest(TestUserInterface('test_update_transit'))
    # suite.addTest(TestUserInterface('test_update_rule'))
    suite.addTest(TestUserInterface('test_remove_rules'))
    return suite

def suite_detector():
    suite = unittest.TestSuite()
    # suite.addTest(TestDetector('test_initial_state'))
    # suite.addTest(TestDetector('test_updating_state'))
    # suite.addTest(TestDetector('test_detecting_rules'))
    suite.addTest(TestDetector('test_alarm'))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite_user_interface())
    #runner.run(suite_detector())