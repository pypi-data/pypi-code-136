#exec(open('def_read_line_transitions.py').read())
#home_dir = os.environ['HOME']
#ion_dir = os.path.join(home_dir,'Dropbox','VoigtFit', 'static', '')
ion_dict = {'OI_1302':0, 'NI_1199':1, 'NI_1200':2, 'NI_1200.7':3, 'SII_1250':4, 'SII_1253':5, 'SII_1259':6,\
             'NiII_1317':7, 'NiII_1370':8, 'CII_1334':9, 'CIIx_1335':10,'FeII_1144':11, 'FeII_1608':12, 'AlII_1670':13,\
             'PII_1152':14, 'SiII_1190':15, 'SiII_1193':16,'SiII_1260':17,'SiII_1304':18,'SiII_1526':19,'SiIII_1206':20,\
             'SiIV_1393':21, 'SiIV_1402':22, 'CIV_1548':23, 'CIV_1550':24, 'NV_1238':25, 'NV_1242':26,'OVI_1031':27, 'OVI_1037':28 
            }
#add SiII 1304, PII1152 to the ion dictionary
#OI-1302 SII-1253 NI-1199 SiII-1190 PII-1152 FeII-1144 \
#              NI-1134 FeII-1125 ArI-1048 OI-1039 SiII-1020 \
#              OI-988a  NI-972  PII-963  NI-953  HI-949  OI-948a
import numpy as np
def read_line_transitions(ion_dir, ion_dict):
    """
    Reads in the line transitions, central wavelengths, and oscillator strengths for the given ions in the ion_dict from the linelist.dat
    file located under VoigtFit package located in the Dropbox directory. There are multiple linelist.dat files under the main VoigtFit directory.
    We want to use the linelist.dat in the main Voigtfit directory in static. 
    ----------
    ion_dir : This is the location path to the linelist.dat file
    ion_dict :this is a hard coded dictionary containing all of the line transitions you are interested in plotting

    Defaults
    ---------
    This code is specifically hard coded to read in the linelist.dat file in the static directory under the 1st Voigtfit directory
    given a specific ion dictionary. 

    Returns
    -------
    central_wl_ion_dict and ion_f_value_dict: Two dictionaries enclosed in a list. central_wl_ion_dict hold the central wavelengths
    of the line transitions as the keys and the string name of the line transitions as the values. ion_f_value_dict holds the string name 
    of the line transitions as the keys and the oscillator strengths as values. To access each dictionary by itself use the following notation:
    read_line_transitions(ion_dir, ion_dict)[0] to return central_wl_ion_dict
    and read_line_transitions(ion_dir, ion_dict)[1] to return ion_f_value_dict
    
    Example on How to Run Code
    --------------------------
    read_line_transitions(ion_dir,ion_dict)[0] returns the first dictionary (central_wl_ion_dict)
    
    Written by April Horton 4/10/2022
    """
    line_list_file  = open(ion_dir+'linelist.dat', "r")
    line_list_data = line_list_file.readlines()[7:]#start reading at index 7 because of the headers, this should be standard
    #for all users because we are using the same linelist.dat
    ions = []
    central_wl = []
    oscillator = []
    #ion_dict is a hard coded dictionary. If you want to add additional line transitions to the plots stacks, they will need to be added by hand. 
    for line in line_list_data: #iterate through each of the lines in the data file
        line = line.strip() #removes spaces at the beginning and at the end of the string. Returns a copy of the string with both leading and trailing characters removed
        if not line or line.startswith("#"): #if the line is blank or is a comment, starts with #
            continue #ends the current iteration and goes to the next one
   
        columns = line.split() # line.split() splits the line of strings into a list of strings.     
        col_id = columns[0] #holds the line transition string name
        ions.append(col_id)
        cen_wl = columns[2] #holds the central wavelengths of the transitions from the linelist.dat file
        central_wl.append(cen_wl)
        f_value = columns[3] #holds the oscillator values of the transitions 
        oscillator.append(f_value)
    line_list_file.close()

    ions_array=np.array(ions) #convert the ions list to an array for numpy functionality 
    keys = [] #these keys will be the central wavelengths
    ion_strings = [] #the string name of the line transitions
    oscillator_strengths = [] #holds the oscillator strengths for each line transition
    for i in ion_dict: #loop through all of the ions inside the ion_dict
        if i in ions_array: #is the ion actually in the line_list.dat file, helps for human mistakes when creating ion_dict
            if np.count_nonzero(ions_array==i)>1: #if there are duplicate ions at the same wavelength, compare oscillator strengths to find the ion with the larger f_value
                indices = np.where(ions_array==i)[0] #find the indices where duplicate ions occur
                f_value_list = [] #stores the oscillator values of the duplicate ions
                for x in range(len(indices)): #iterate over the indices to grab the oscillator values for comparison
                    f_value_list.append(float(oscillator[indices[x]]))
                #then, I find the maximum value in the oscillator strength list and return that index. I use that index in the indices list to grab the right element frm the ions, central wl and oscillator lists.
                keys.append(float(central_wl[indices[f_value_list.index(max(f_value_list))]]))
                ion_strings.append(ions[indices[f_value_list.index(max(f_value_list))]])
                oscillator_strengths.append(float(oscillator[indices[f_value_list.index(max(f_value_list))]]))
            else:
                keys.append(float(central_wl[ions.index(i)]))
                ion_strings.append(ions[ions.index(i)])
                oscillator_strengths.append(float(oscillator[ions.index(i)]))
            #I use the ions.index(i) because i is a string of the ion's name. Therefore, I need the index from the ions list where that ion string occurs
        else:
            return("Sorry, ion "+i+" is not in line_list.dat")

    #the zip function essentially works as a zipper. It "zips" together the first item with the second item. It joins the two iterators together
    x = zip(keys, ion_strings)
    central_wl_ion_dict = dict(x) #this dictionary has the central wavelengths as the keys and the line transition strings as the value

    y = zip(ion_strings, oscillator_strengths)
    ion_f_value_dict = dict(y) #this dictionary holds the line transitions as the keys and the oscillator strengths as the values
    return [central_wl_ion_dict, ion_f_value_dict]
#ion_dict = ['CII_1334']
#rest_wl = list(read_line_transitions(ion_dir,ion_dict)[0].keys())[0] #getting just the laboratory frame rest wavelength
#print(rest_wl)


