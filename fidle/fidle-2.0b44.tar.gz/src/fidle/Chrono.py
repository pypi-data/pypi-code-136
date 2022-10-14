# ==================================================================
#                  _____ _                           
#                 / ____| |                          
#                | |    | |__  _ __ ___  _ __   ___  
#                | |    | '_ \| '__/ _ \| '_ \ / _ \ 
#                | |____| | | | | | (_) | | | | (_) |
#                 \_____|_| |_|_|  \___/|_| |_|\___/ 
#                                                    fidle.Chrono
# ==================================================================
# A simple class pour implement a stopwatch (and a bit more)
# Jean-Luc Parouty CNRS/MIAI/SIMaP 2022

import datetime
import fidle.config as config
import fidle.utils  as utils


class Chrono:

    def __init__(self):
        __version__   = config.VERSION
        self.reset_chrono()


    def start(self, id='default'):
        '''
        Start a chronometer
        args:
            id : chronometer name ('default')
        return:
            nothing
        '''
        self.start_time[id] = datetime.datetime.now()


    def stop(self, id='default'):
        '''
        Stop a chronometer
        args:
            id : chronometer name ('default')
        return:
            nothing
        '''
        self.end_time[id]   = datetime.datetime.now()


    def get_delay(self, id='default', format='str'):
        '''
        Return a delay from a chronometer
        If chronometer is stopped, return delay=(stop-start)
        If chronometer is running, return delay=(now()-start)
        args:
            id     : chronometer name                        ('default')
            format : delay format, 'str', 'seconds', 'human' (str)
        return:
            formated delay
        '''
        t1 = self.start_time[id]
        t2 = self.end_time.get(id, datetime.datetime.now())
        dt = t2 - t1
        # ---- in seconds
        if format=='seconds': 
            return round(dt.total_seconds(),2)
        # ---- str, seconds without microseconds
        if format=='str':
            dt = dt - datetime.timedelta(microseconds=dt.microseconds)
            return str(dt)
        # ---- Human
        if format=='human':
            return utils.hdelay(dt)
        # ---- timedelta
        return dt


    @staticmethod
    def now(format='%d/%m/%y %H:%M:%S'):
        '''
        Return a formated string for current date/time
        args:
            format : a strftime format ('%d/%m/%y %H:%M:%S')
        return:
            current formated date/time
        '''
        t = datetime.datetime.now()
        if format is None:  return t
        return t.strftime(format)
    

    @staticmethod
    def tag_now():
        '''
        Return a string tag for current date/time
        args:
            nothing
        return:
            current formated date/time tag as '%Y-%m-%d_%Hh%Mm%Ss'
        '''
        return datetime.datetime.now().strftime("%Y-%m-%d_%Hh%Mm%Ss")


    def get_start(self, id='default', format='%d/%m/%y %H:%M:%S'):
        '''
        Return start time from a chronometer
        args:
            id     : chronometer name         ('default')
            format : strftime format or None  ('%d/%m/%y %H:%M:%S')
        return:
            formated start time or datetime if format is None
        '''
        t1 = self.start_time[id]
        if format is None:  return t1
        return t1.strftime(format)


    def get_end(self, id='default', format='%d/%m/%y %H:%M:%S'):
        '''
        Return end time from a chronometer
        args:
            id     : chronometer name         ('default')
            format : strftime format or None  ('%d/%m/%y %H:%M:%S')
        return:
            formated start time or datetime if format is None
        '''
        t2 = self.end_time[id]
        if format is None:  return t2
        return t2.strftime(format)


    def reset_chrono(self):
        '''
        Reset all chronometers.
        Remove all start/stop entries.
        args:
            nothing
        return:
            nothing
        '''
        self.start_time = {} 
        self.end_time   = {}


    def show(self,id='default'):
        '''
        Print current duration for a chronometer in seconds
        args:
            id : chronometer name ('default')
        return
            nothing, just print
        '''
        print('Duration : ', self.get_delay(id,format='seconds'),'seconds')

