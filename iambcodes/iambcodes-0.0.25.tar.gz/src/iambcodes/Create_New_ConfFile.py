import os
from datetime import date

def Create_New_ConfFile(attributes = list, workflow = str, target_dir = str):
    #Aufgabe der Funktion ist es, die liste anzunehmen und eine .txt datei zu erstellen
    
    """
    Parameters:
    
    attributes = list of strings that end up as keys when loading the config file
    
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
    
    #Check if attributes is a list
        #if true, continue
        #if not, error message about wrong type of attribute
    if type(attributes) == list:
        #check if list contains only strings
        #if true continue
        #if false, error message about wrong data types
        for i in attributes:
            if type(i) != str:
                print("WARNING! Incorrect data-type found. All Parameters for the config-file have to be in string-format!")
                return False
    else:
        print("WARNING! Function recieved incorrect information. Please check if everything is in order!")
        return False
    
    #write and open new file in directory indicated by Workflow
        #alternative: addition string input with the target directory
    #take list and writerow with one position per row
    
    ConfComment = "#This is a freshly generated configuration file for a {} workflow.\n#Please fill in the parameters according to the {} notebook.".format(workflow, workflow)
    
    ConfName = '{}_JUDAS_{}_{}_config.txt'.format(Today, workflow, "GENERATED")
    ConfAddress = os.path.join(target_dir, ConfName)
    print(ConfAddress)
    with open(ConfAddress, 'w') as f:
        print(ConfComment, file=f)
        for key in attributes:
            print('{}:'.format(key), file=f)
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
                       "GrowthProfiler",
                       "MFA",
                       "RatesYields"
                      ]
    
    if workflow in listofworkflows:
        return True
    else:
        return False
