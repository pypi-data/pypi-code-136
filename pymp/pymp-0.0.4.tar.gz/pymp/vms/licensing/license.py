import os
import re
import time
import datetime as dt
import pandas as pd
import numpy as np

class VMSSoftwareLicensingFile(object):
    """

    """
    def __init__(self, file_path):
        # If the path exists attempt to parse it.
        if os.path.exists(file_path):
            self.file_path = file_path
            self._parse()
        else:
            raise FileNotFoundError(f"'{file_path}' does not exist.")

    def _parse(self):
        """

        """
        # ==> Grab the Varian Licensing File (vms.lic) from the location ont he Web server
        f = open(self.file_path, 'r')
        lines = f.readlines()
        f.close()

        # ==> Loop thought the lines grabbing the various licenses

        # LIC_START_TIME = time.time()

        _license = []  # Temp list for storing the sep lines of each license section
        _licensing = []  # List containing the fully merged license info
        in_license = False  # Just used to skip the leading lines of the file (non-licensing)

        for line in lines:
            if line.startswith('INCREMENT'):

                # Determine if you are in the license section since it will start with an INCREMENT keyword
                # If this is the first license you come across set the in_license flag to trigger processing
                if not in_license:
                    in_license = True

                # If the license list is not empty continue to add the subsequent lines of the license from
                # the file. When you hit another INCREMENT you are in the next license so append it to the
                # licensing list and reset the license list to empty (i.e. ready for the next license section).
                if _license:
                    _licensing.append(''.join(_license))  # join licensing lines before adding the license
                    _license = []

                # Append the INCREMENT line ot he license list striping the continuation character '\'
                _license.append(line.strip().strip('\\'))
                # print(line.rstrip())
            else:
                # If you are not on an INCREMENT line and are in a licensing section append it to the license
                # list for future processing.
                if in_license:
                    _license.append(line.strip().strip('\\'))
                    # print(line.rstrip())

        # ==> Set the column headers for the dataframe that will store the sections of each license we want to keep

        license_headers = ['License_Name',
                           'Version',
                           'Duration',
                           'Total',
                           'Type',
                           'Issue_Date',
                           'Notice',
                           'Serial_Number',
                           'Start_Date',
                           'Signature'
                           ]
        license_data = []  # List of lists with individual license sections

        # Loop over the processed licensing sections and grab the section of interest
        for l in _licensing:
            # print(l)
            tmp = l.split()
            # print(tmp)

            name = tmp[1].strip()  # Name of License
            version = tmp[3].strip()  # Version of License
            duration = tmp[4].strip()  # Duration of the License
            total = int(tmp[5].strip())  # Number of available Licenses
            ltype = tmp[7].split('=')[1].strip()  # Type of License

            # Issue date of license (can use for post install comparison)
            issued = dt.datetime.strptime(tmp[9].split('=')[1].strip().strip('"'), '%d-%b-%Y')

            # Information on license
            NOTICE = l[l.find('NOTICE='):l.find('SN=')]
            # print(NOTICE)
            notice = NOTICE.split('=')[1].strip().strip('"')

            # License serial number
            SN = l[l.find('SN='):l.find('START=')]
            # print(SN)
            sn = SN.split('=')[1].strip()

            # Start date for license (maybe day of .lic file creation)
            START = l[l.find('START='):l.find('SIGN=')]
            # print(START)
            start = dt.datetime.strptime(START.split('=')[1].strip(), '%d-%b-%Y')

            # Varian signature of the license
            SIGN = l[l.find('SIGN='):]
            # print(SIGN)
            sign = SIGN.split('=')[1].strip()

            # Append the now segmented license data to a master list
            license_data.append([name, version, duration, total, ltype, issued, notice, sn, start, sign])

        # Turn the master license data into a datafram for later.
        self.dataframe = pd.DataFrame(data=license_data, columns=license_headers)
        self.dataframe['Issue_Date'] = self.dataframe['Issue_Date'].astype('datetime64[ns]')
        self.dataframe['Start_Date'] = self.dataframe['Start_Date'].astype('datetime64[ns]')
        self.dataframe.sort_values(by=['License_Name'], inplace=True)
        # print('Licensing Parsed')
        # print(self.dataframe)
        # print(time.time() - LIC_START_TIME)

class VMSFlexnetLogFile(object):
    """

    """
    def __init__(self, file_path):
        # If the path exists attempt to parse it.
        if os.path.exists(file_path):
            self.file_path = file_path
            self._parse()
        else:
            raise FileNotFoundError(f"'{file_path}' does not exist.")

    def _parse(self):
        """
        """
        # ==> Grab the Varian debug.log file from the location ont he Web server

        # USE_START_TIME = time.time()

        f = open(self.file_path, 'r')
        lines = f.readlines()
        f.close()

        # TIMESTAMPS
        TS = []  # Holds the (line #, TIMESTAMP) tuples
        hours = []  # Holds the hour value for detecting the day changes

        # Grab the hour value for every line and construct and store the  (line #, TIMESTAMP) tuples
        for e, line in enumerate(lines):
            hours.append(dt.datetime.strptime(line.split()[0].strip(), "%H:%M:%S").hour)
            if ('TIMESTAMP' in line):
                TS.append((e, dt.datetime.strptime(line.split()[-1].strip(), "%m/%d/%Y")))
        hours = np.array(hours, dtype=int)

        # for i, j in TS:
        #     print(f"{i}\t{j}")

        # Day changes should be where the (-) values are where hours[1:] - hours[0:-1]
        day_breaks = np.where((hours[1:] - hours[0:-1]) < 0)[0]
        # print(day_breaks)

        # Grab the first TIMESTAMP and its line values
        ts_line0, ts1 = TS[0]
        # print(ts1)

        # CHeck to see if there are and day changes before it occured using the line value
        delta = len(np.where(day_breaks < ts_line0)[0])

        # The first date TIMESTAMP is the first TIMESTAMP minus the number of day changes that came before it
        dt_TIMESTAMP = ts1 - dt.timedelta(days=delta)
        TIMESTAMP = dt_TIMESTAMP.strftime("%m/%d/%Y")
        # print(TIMESTAMP)

        # Simple counters for easy inspection of the number of transactions of each type
        IN_COUNT = 0
        OUT_COUNT = 0
        DENIED_COUNT = 0
        UNSUPPORTED_COUNT = 0

        # Temporary lists to hold entries that may come before a date timestamp
        _IN = []
        _OUT = []
        _DENIED = []
        _UNSUPPORTED = []

        # Processed lists of log entries
        PROCESSED = [[], [], [], []]
        IN, OUT, DENIED, UNSUPPORTED = PROCESSED

        # Processing FLags
        # TIMESTAMP = None # Holds the current date timestamp (Starts with None)
        # PROCESS_INS = False # Flags to process the INs (Used to avoid INs without OUTs at the beginning of the log)

        time_re = re.compile(r'\d+:\d+:\d+')
        user_re = re.compile(r'\b\S+@\S+\b')

        stops = day_breaks + 1
        days = []
        for e in range(len(stops)):
            if e == 0:
                days.append((0, stops[e]))
            elif e == (len(stops) - 1):
                days.append((stops[e - 1], stops[e]))
                days.append((stops[e], len(lines)))
            else:
                days.append((stops[e - 1], stops[e]))
        # print(day_breaks)
        # print(days)

        for o, x in days:
            # print(TIMESTAMP, '-', o, x)
            for e in range(o, x):
                line = lines[e]
                # ==> Process the license check in calls
                if 'IN: ' in line:
                    IN_COUNT += 1  # Increment the IN count

                    # Split the simple IN line to get he fields you want
                    _in = [i.strip().strip(':').strip('"').strip('()') for i in line.split()]

                    # Split the user from the server name
                    tmp = _in[-1].split('@')

                    if len(_in) == 5:
                        # Set the last field to the user
                        _in[-1] = tmp[0]

                        # Add the server name to the end
                        _in.append(tmp[-1])
                    elif len(_in) == 6:
                        # Set the second to last field to the user
                        _in[-2] = _in[-2] + ' ' + tmp[0]

                        # Add the server name to the end
                        _in[-1] = tmp[-1]
                    else:
                        raise ValueError(f'Something wrong with the user info on IN line {e + 1}')

                    # Add the log entry position (they are chronological)
                    _in.insert(0, e + 1)

                    _in[1] = f'{TIMESTAMP} {_in[1]}'
                    IN.append(_in)

                # ==> Process the license check out calls
                elif 'OUT: ' in line:
                    OUT_COUNT += 1  # Increment the OUT count

                    # Split the simple OUT line to get he fields you want
                    _out = [i.strip().strip(':').strip('"').strip('()') for i in line.split()]

                    # Split the user from the server name
                    tmp = _out[-1].split('@')


                    if len(_out) == 5:
                        # Set the last field to the user
                        _out[-1] = tmp[0]

                        # Add the server name to the end
                        _out.append(tmp[-1])
                    elif len(_out) == 6:
                        # Set the second to last field to the user
                        _out[-2] = _out[-2]+' '+tmp[0]

                        # Add the server name to the end
                        _out[-1] = tmp[-1]
                    else:
                        raise ValueError(f'Something wrong with the user info on OUT line {e+1}')

                    # Add the log entry position (they are chronological)
                    _out.insert(0, e + 1)

                    _out[1] = f'{TIMESTAMP} {_out[1]}'
                    OUT.append(_out)

                # ==> Process the DENIED license calls
                elif 'DENIED: ' in line:
                    DENIED_COUNT += 1  # Increment the DENIED count

                    # Split the simple OUT line to get he fields you want
                    _denied = [i.strip().strip(':').strip('"').strip('()') for i in line.split()]
                    _denied = _denied[0:5]

                    # Split the user from the server name
                    tmp = _denied[-1].split('@')

                    if len(_denied) == 5:
                        # Set the last field to the user
                        _denied[-1] = tmp[0]

                        # Add the server name to the end
                        _denied.append(tmp[-1])
                    elif len(_denied) == 6:
                        # Set the second to last field to the user
                        _denied[-2] = _denied[-2] + ' ' + tmp[0]

                        # Add the server name to the end
                        _denied[-1] = tmp[-1]
                    else:
                        raise ValueError(f'Something wrong with the user info on DENIED line {e + 1}')

                    # Add the log entry position (they are chronological)
                    _denied.insert(0, e + 1)

                    _denied[1] = f'{TIMESTAMP} {_denied[1]}'
                    DENIED.append(_denied)

                # ==> Process the UNSUPPORTED license calls
                elif 'UNSUPPORTED: ' in line:
                    # Skip ERROR Lines for now
                    if 'ERROR' not in line:
                        UNSUPPORTED_COUNT += 1  # Increment the UNSUPPORTED count

                        # Split the simple OUT line to get he fields you want
                        _tmp = [i.strip().strip(':').strip('"').strip('()') for i in line.split()]
                        _unsupported = [_tmp[i] for i in range(4)]

                        # Split the user from the server name
                        _unsupported.extend(re.findall('\S+@\S+', line))
                        tmp = _unsupported[-1].split('@')

                        if len(_unsupported) == 5:
                            # Set the last field to the user
                            _unsupported[-1] = tmp[0]

                            # Add the server name to the end
                            _unsupported.append(tmp[-1])
                        elif len(_unsupported) == 6:
                            # Set the second to last field to the user
                            _unsupported[-2] = _unsupported[-2] + ' ' + tmp[0]

                            # Add the server name to the end
                            _unsupported[-1] = tmp[-1]
                        else:
                            raise ValueError(f'Something wrong with the user info on UNSUPPORTED line {e + 1}')

                        # Add the log entry position (they are chronological)
                        _unsupported.insert(0, e + 1)

                        _unsupported[1] = f'{TIMESTAMP} {_unsupported[1]}'
                        UNSUPPORTED.append(_unsupported)
                else:  # Skip everything else for now
                    pass

            dt_TIMESTAMP = dt_TIMESTAMP + dt.timedelta(days=1)
            TIMESTAMP = dt_TIMESTAMP.strftime("%m/%d/%Y")

        # Setup the log entry headers
        log_headers = ['Log_Entry',
                       'Date',
                       'Service',
                       'Msg_Type',
                       'License_Name',
                       'User',
                       'Server'
                       ]

        # Setup the usage dataframe
        data_ = [item for sublist in PROCESSED for item in sublist]
        for v, d in enumerate(data_):
            if len(d) == 8:
                print(v, d)

        self.dataframe = pd.DataFrame(data=[item for sublist in PROCESSED for item in sublist],
                                      columns=log_headers
                                      )

        # Convert the date column to the datetime format and sort it in chronological order
        self.dataframe['Date'] = self.dataframe['Date'].astype('datetime64[ns]')
        self.dataframe.sort_values(by=['Log_Entry'], inplace=True)

        # print('Usage Log Parsed')
        # # print(usage_df)
        # print(time.time() - USE_START_TIME)

        # ==> Loop over the users and see if all their Ins and OUTs are accounted for

        # IN_OUT_START_TIME = time.time()

        # Add a column to the dataframe to store the diagnostic flag
        # usage_df['IN_No_OUT'] = 0
        # usage_df.sort_values(by=['Log_Entry'], inplace=True)

        # Grab all unique users and sort them in alphabetical order
        user_names = list(self.dataframe['User'].unique())
        user_names.sort()

        # Setup a test dictionary to store INs and OUTs to check against
        INnoOUT = []  # Diagnostic use only just used to collect entry ids for inspection

        user_dict = {}

        # Loop over every user and check their INs and OUTs
        for user in user_names:
            # test_dict = {}
            user_dict[user] = {'IN': {}, 'OUT': {}}
            for index, row in self.dataframe.loc[self.dataframe.User == user].iterrows():
                # If the log entry is a license check OUT store it as out
                if row['Msg_Type'] == 'OUT':
                    if row['License_Name'] in user_dict[user]['OUT']:
                        user_dict[user]['OUT'][row['License_Name']].append(row['Log_Entry'])
                    else:
                        user_dict[user]['OUT'][row['License_Name']] = [row['Log_Entry']]
                # If the log entry is a license check IN pop off the store one of the
                # corresponding check OUTs
                if row['Msg_Type'] == 'IN':
                    # If it has a corresponding check OUT pop it off the stack
                    if row['License_Name'] in user_dict[user]['OUT']:
                        user_dict[user]['OUT'][row['License_Name']].pop()
                        if len(user_dict[user]['OUT'][row['License_Name']]) == 0:
                            del user_dict[user]['OUT'][row['License_Name']]  # If the store is empty remove it
                    # If it doesn't have a corresponding check set the flag and store it for
                    # diagnostics later
                    else:
                        if row['License_Name'] in user_dict[user]['IN']:
                            user_dict[user]['IN'][row['License_Name']].append(row['Log_Entry'])
                        else:
                            user_dict[user]['IN'][row['License_Name']] = [row['Log_Entry']]
            # print(test_dict)

        self.dataframe['IN_No_OUT'] = 0
        self.dataframe['OUT_No_IN'] = 0
        for user, log in user_dict.items():
            for lic, in_orphan in log['IN'].items():
                for entry in in_orphan:
                    self.dataframe.loc[self.dataframe.Log_Entry == entry, 'IN_No_OUT'] = 1
            for lic, out_orphan in log['OUT'].items():
                for entry in out_orphan:
                    self.dataframe.loc[self.dataframe.Log_Entry == entry, 'OUT_No_IN'] = 1

        # print('INs with no OUTs Identified')
        # # print(user_dict)
        # print(time.time() - IN_OUT_START_TIME)

    def determine_usage(self, license_file_obj=None):
        """
        """
        # ==> Generate the usage stats from the log entries and extend the dataframe


        # STATS_START_TIME = time.time()
        #
        # print('Starting to generate usage stats')
        # Grab the unique license names and sort them in alphabetical order
        if license_file_obj is None:
            license_names = list(self.dataframe['License_Name'].unique())
        else:
            license_names = list(license_file_obj.dataframe['License_Name'].unique())
        license_names.sort()

        # # Construct a dict from the names and add the 0 value columns to the flexnet_log.dataframe
        # d = dict.fromkeys(license_names, 0)
        # self.dataframe.assign(**d)

        for name in license_names:
            #     print(name)
            self.dataframe[name] = 0
            self.dataframe.loc[(self.dataframe['Msg_Type'] == 'IN') & (self.dataframe['License_Name'] == name), name] = -1
            self.dataframe.loc[(self.dataframe['Msg_Type'] == 'OUT') & (self.dataframe['License_Name'] == name), name] = 1

        # print(time.time() - STATS_START_TIME)
