import datetime
import inspect
import time


class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    WHITE = '\033[7m'
    RED = '\033[41m'
    YELLOW = '\033[43m'
    GREEN = '\033[42m'
    BLUE = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN = '\033[46m'
    BLACK = '\033[40m'
    GREY = '\033[47m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    HIDDEN = '\033[8m'
    RESET = '\033[0m'
    BOLDBLACK = '\033[1m\033[30m'
    BOLDRED = '\033[1m\033[31m'
    BOLDGREEN = '\033[1m\033[32m'
    BOLDYELLOW = '\033[1m\033[33m'
    BOLDBLUE = '\033[1m\033[34m'
    BOLDMAGENTA = '\033[1m\033[35m'
    BOLDCYAN = '\033[1m\033[36m'
    BOLDWHITE = '\033[1m\033[37m'
    BOLDBLACK = '\033[1m\033[90m'
    BOLDRED = '\033[1m\033[91m'
    BOLDGREEN = '\033[1m\033[92m'
    BOLDYELLOW = '\033[1m\033[93m'
    BOLDBLUE = '\033[1m\033[94m'
    BOLDMAGENTA = '\033[1m\033[95m'
    BOLDCYAN = '\033[1m\033[96m'
    BOLDWHITE = '\033[1m\033[97m'
    BACKBLACK = '\033[40m'
    BACKRED = '\033[41m'
    BACKGREEN = '\033[42m'
    BACKYELLOW = '\033[43m'
    BACKBLUE = '\033[44m'
    BACKMAGENTA = '\033[45m'
    BACKCYAN = '\033[46m'
    BACKWHITE = '\033[47m'
    BACKBLACK = '\033[100m'
    BACKRED = '\033[101m'
    BACKGREEN = '\033[102'
                        

class PrintSettings:
    _shared_state = {}
    
    _variable_color = BColors.OKGREEN
    _logs_color = BColors.OKBLUE

    def __new__(cls, *args, **kargs):
        inst = super().__new__(cls)
        inst.__dict__ = cls._shared_state
        return inst


class Print(PrintSettings):
    
    __check_variables = True
    

    def __init__(self, text:str, var=None, num_separators=50, al=True, num_al=1, bl=True, num_bl=1, include_time=False, 
                include_caller_file=False, include_caller_line=True) -> None:
        
        
        if num_al < 1:
            num_al = 1
        
        if num_bl < 1:
            num_bl = 1
        
        if al:
            for _ in range(0, num_al):
                print('-'*num_separators)
        
        
        if type(text) is list or type(text) is tuple:
            for index, t in enumerate(text):
                if var:
                    if type(var) is list or type(var) is tuple:
                        print(f'{self._variable_color}{t}{BColors.ENDC}: {var[index]}')
                    else:
                        print(f'{self._variable_color}{t}{BColors.ENDC}: {var}')
                else:
                    if self.__check_variables:
                        
                        # check if t is a variables, during the loop through we found that a
                        # certain t value is not a variable we call __check_variables to be false,
                        # since we have to assumed that all following values for t aren't going to be a variable

                        # the only thing to consider if in the case that some values are variables and others are not
                        
                        # we choose the first approach since is the most common to encounter

                        if (var_name := self.get_variable_name(t)):
                            print(f'{self._variable_color}{var_name}{BColors.ENDC}: {t}')
                        else:
                            print(t)
                            self.__check_variables = False
                    else:
                        print(t)
        else:
            if var:
                if text is None:
                    print(f'{self._variable_color}{self.get_variable_name(var)}{BColors.ENDC}: {var}')
                elif text is not None:
                    print(f'{self._variable_color}{text}{BColors.ENDC}: {var}')
            else:

                # even though we're calling for text, this text can be a variable, so ,
                # we need to check if it's a variable, if it is a variable, we are going 
                # to perform special treatment

                if (var_name := self.get_variable_name(text)):
                    print(f'{self._variable_color}{var_name}{BColors.ENDC}: {text}')
                else:
                    print(text)


        if include_time:
            print(f'{self._logs_color}runtime{BColors.ENDC}: {datetime.datetime.now().time()}')
            
        caller = inspect.getframeinfo(inspect.stack()[1][0])
        
        if include_caller_file:
            print(f'{self._logs_color}file{BColors.ENDC}: {caller.filename}')
        
        if include_caller_line:
            print(f'{self._logs_color}line{BColors.ENDC}: {caller.lineno}')
            
        if bl:
            for _ in range(0, num_bl):
                print('-'*num_separators)


    def get_variable_name(self, var):
            
        callers_local_vars = inspect.currentframe().f_back.f_back.f_locals.items()
        var_name = [(var_name, var_val) for var_name, var_val in callers_local_vars]
                
        if var_name[0][0] == 'self':
            cls = var_name[0][1]

            boring = dir(type('dummy', (object,), {}))
            items = [item for item in inspect.getmembers(cls) if item[0] not in boring]

            var_name = list(filter(lambda pair: pair[1] == var, items))   
            
        return var_name[0][0] if var_name else None
    
    

class MeassureTime:


    def __init__(self, func, parameters=dict()) -> None:
        self.func = func
        self.parameters = parameters

        start = time.time()
        func(*parameters)
        end = time.time()

        Print('time', end - start)



def check_caller_line(show_file=False):
    def decorator(func):
        def wrapper(*args, **kwargs):
            caller = inspect.getframeinfo(inspect.stack()[1][0])
            
            to_print = (
                f'{BColors.OKGREEN}Calling function:{BColors.ENDC} {BColors.OKBLUE}{func.__name__}{BColors.ENDC}', 
                f'{BColors.OKGREEN}Line:{BColors.ENDC} {caller.lineno}')
            
            if show_file:
                to_print = (
                f'{BColors.OKGREEN}Calling function:{BColors.ENDC} {BColors.OKBLUE}{func.__name__}{BColors.ENDC}', 
                f'{BColors.OKGREEN}File:{BColors.ENDC} {caller.filename}', 
                f'{BColors.OKGREEN}Line:{BColors.ENDC} {caller.lineno}')
                
            
            Print(to_print, include_caller_line=False)
            r = func(*args, **kwargs)
            return r            
        return wrapper
    return decorator
