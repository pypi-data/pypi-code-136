import time

class FetchParam:
    def __init__(self,url_template,url_params,method,respose_type):
        self.parms = {
            'url_template':url_template,
            'url_params':url_params,
            'method':method,
            'response_type':respose_type
        }
    
    def add_time_stamp(self):
        pass


class ParseParams:
    def __init__(self,parse_function,kwargs):
        self.params = {
            'parse_function':parse_function,
            'kwargs':kwargs
        }

class Parameter:
    def __init__(self):
        pass

