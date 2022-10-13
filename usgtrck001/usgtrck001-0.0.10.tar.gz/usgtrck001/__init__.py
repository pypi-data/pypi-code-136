import os, platform
from datetime import datetime

def start_tracking():
    #get start date
    start_date = datetime.now()
    start_date_string = start_date.strftime("%d-%m-%Y %H:%M")
    #gets all user settings
    user_settings = dict(os.environ)
    #gets username from all settings
    user_username = user_settings['USERNAME']
    # gets hostname
    if platform.system() == "Windows":
        user_hostname = platform.uname().node # for windows
        user_hostname = user_hostname[user_hostname.index('PC')+len('PC'):] #returns hostname without substring 'PC'
    else:
        user_hostname = os.uname()[1]   # for other os
        user_hostname = user_hostname[user_hostname.index('PC')+len('PC'):] #returns hostname without substring 'PC'

    # replace text in .dat file
    def insert_values(source_str, first, last,insert_str):
        start = source_str.index( first ) + len( first)
        end = source_str.index( last, start )
        return source_str[:start]+insert_str+source_str[end:]
    
    #open .dat file and replace with os settings
    fin = open('C:/Users/DOZI/Desktop/iscowi.w39', 'r')
    primary_text = fin.read()
    text = insert_values(primary_text, '<Ini>', '</Ini>', user_username)
    text = insert_values(text, '<Pid>', '</Pid>', user_hostname)
    text = insert_values(text, '<Dat>', '</Dat>', start_date_string)
    

    end_date = datetime.now()
    total_time_spent = ((end_date-start_date).total_seconds())/60

    text = insert_values(text, '<Qua>', '</Qua>', str(round(total_time_spent,2)))
    fin.close()
    #write to .dat file changes
    fout = open('C:/Users/DOZI/Desktop/iscowi.w39', 'w')
    fout.write(text)
    fout.close()

    start_date = datetime.now()
    

