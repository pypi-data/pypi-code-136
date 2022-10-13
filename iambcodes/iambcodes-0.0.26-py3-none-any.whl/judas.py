import os
from datetime import date
import pandas as pd

def Create_New_ConfFile(workflow = str, target_dir = str):
    #task of the function is to generate a .txt file for the requested workflow
    #An excel file servng as a template library needs to be in the main-folder of iambjudas
    
    """
    Parameters:
    
    ##attributes = list of strings that end up as keys when loading the config file
        Comment: removed. Attributes are now stored as a library of excel sheets
    
    workflow = string of the type of worklow the conffile is generated for
    
    target_dir = string of the target directory
    
    Today = Date of use. Needs datetime-module
    
    """
    
    #generate the date
    Today = date.today().strftime('%y%m%d')
    
    
    #Check if workflow is correct
        #function Check_Workflow_Type has a list of all available Workflow types and checks if the chosen worflow
        #is part of the list
        #if true, continue
        #if false, error message about a false worklow
    if Check_Workflow_Type(workflow) == False:
        print("WARNING! The chosen worklow does not exist.")
        return False
    
    #
    #load of library.xlsx with Prewritten Files
    try:
        file = "220718_configfile_library.xlsx"
        df = pd.read_excel(file, sheet_name=workflow, keep_default_na=False)
    except FileNotFoundError:
        print("ERROR!\nThe config-file library was not found.\n\n")
        return False
    
    #write and open new file in directory indicated by Workflow
        #alternative: addition string input with the target directory
    #take list and writerow with one position per row
     
    ConfName = '{}_JUDAS_{}_{}_config.txt'.format(Today, workflow, "GENERATED")
    ConfAddress = os.path.join(target_dir, ConfName)
    print("ATTENTION!\n\n Your new config-file was generated in the folder "+ConfAddress)
    with open(ConfAddress, 'w') as f:
        for key in df.Parameters:
            print('{}'.format(key), file=f)
    #done
    
    
    return True


"""
Function to check if a workflow is legitimate or not

Sends back TRUE if workflow is known
Sends back FALSE is worklow is not recognized
"""
def Check_Workflow_Type(workflow = str):
    """
    Parameters:
    listofworklows: list of all available workflows
    """
    listofworkflows = ["BiologData",
                       "DoE",
                       'GSMM_Quality_Control',
                       "GrowthProfiler",
                       "MFA",
                       "RatesYields"
                      ]
    
    if workflow in listofworkflows:
        return True
    else:
        return False