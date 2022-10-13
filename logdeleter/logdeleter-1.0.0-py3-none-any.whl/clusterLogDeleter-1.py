from .LogDeleter import LogDeleter
import datetime as DT
import os
import shutil

class ClusterLogDeleter(LogDeleter):

    """ ClusterLogDeleter class for deleting each type of logs with some customization


    Attributes:
        cluster_path represents the DBFS path where the cluster logs are saved (e.g. "/cluster-logs-script/0928-211731-34160a28") 
        number_days_to_keep_logs represents the number of days in the past for which we want to keep the logs. All logs older than X number of days will be deleted.
    """

    def __init__(self, cluster_path, number_days_to_keep_logs=7, delete_ALL_event_logs=False):
        LogDeleter.__init__(self,cluster_path)
        self.number_days_to_keep_logs = number_days_to_keep_logs
        self.delete_event_log = delete_ALL_event_logs
        

    def deleteOldLogs(self):
        '''
        Function to trigger deletion of old logs in folders init_scripts, driver and executor. 
        The deletion of all files is triggered when parameter delete_ALL_event_logs is set to True
        
        '''
        self.getDatesToKeep()
        self.deleteInitScriptLogs()
        self.deleteDriverLogs()
        self.deleteExecutorLogs()

        if self.delete_event_log:
            self.deleteEventLog()
        else:
            print("Didn't delete logs in eventlog folder. Since the logs in eventlog folder don't have a date in their file name we will either delete them all or none at all. Default is none at all. If you wish to delete ALL event logs please set the parameter delete_ALL_event_logs as True when initializing ClusterLogDeleter().")

    def deleteEventLog(self):
        '''Function to delete all the logs inside the eventlog folder
        '''
        print("Started deleting all the event log files")
        shutil.rmtree(self.file_api_cluster_path + "/eventlog/")
        print("Finished deleting all the event log files")

    def deleteInitScriptLogs(self):
        '''Function to delete the old logs inside the init_scripts folder
        '''
        print('Started deleting old Init Script logs')
        init_folder = self.file_api_cluster_path + "/init_scripts"

        for dirpath,_,filenames in os.walk(init_folder):
            for f in filenames:
                if f[:8] not in self.dates_to_keep_without_hifens:
                    os.remove(os.path.abspath(os.path.join(dirpath, f)))

        # Delete empty folders
        for f in os.listdir(init_folder):
            if len(os.listdir(os.path.abspath(os.path.join(init_folder, f))))==0:
                shutil.rmtree(os.path.abspath(os.path.join(init_folder, f)))

        print('Finished deleting old Init Script logs')


    def deleteDriverLogs(self):
        '''Function to delete the old logs inside the driver folder
        '''
        print('Started deleting old Driver logs')

        for dirpath,_,filenames in os.walk(self.file_api_cluster_path + "/driver"):
            for f in filenames:
                if f[6:16] not in self.dates_to_keep_with_hifens:
                    os.remove(os.path.abspath(os.path.join(dirpath, f)))
        print('Finished deleting old Driver logs')


    def deleteExecutorLogs(self):
        '''Function to delete the old logs inside the executor folder
        '''
        print('Started deleting old Executor logs')

        exec_folder = self.file_api_cluster_path + "/executor"

        for f in os.listdir(exec_folder):
            if f[4:12] not in self.dates_to_keep_without_hifens:
                print(os.path.abspath(os.path.join(exec_folder, f)))
                shutil.rmtree(os.path.abspath(os.path.join(exec_folder, f)))
        print('Finished deleting old Executor logs')


    def getDatesToKeep(self):
        '''Function to create list of dates to keep logs for
        Args:
            None

        Returns:
            dates_to_keep_with_hifens: List of dates to keep logs for in format %Y-%m-%d
            dates_to_keep_without_hifens: List of dates to keep logs for in format %Y%m%d
        '''
        today = DT.datetime.today()
        self.dates_to_keep_with_hifens = [today.strftime('%Y-%m-%d')]
        self.dates_to_keep_without_hifens = [today.strftime('%Y%m%d')]

        for i in range(self.number_days_to_keep_logs - 1):
            date = today - DT.timedelta(days=(i+1))
            self.dates_to_keep_with_hifens.append(date.strftime('%Y-%m-%d'))
            self.dates_to_keep_without_hifens.append(date.strftime('%Y%m%d'))
        
        print('Logs will be kept for the dates: {}'.format(self.dates_to_keep_with_hifens))



