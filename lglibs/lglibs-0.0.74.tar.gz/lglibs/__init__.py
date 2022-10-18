import sys as _system
import inspect as _inspect
import time as _time
import os as _os
import base64 as _base64
import string as _string
import paramiko as _paramiko
from . import color as _color

def encode(content: str, save: bool = False, save_path:str=None):
    if not save and save_path is not None:
        raise ValueError("save is off, but still have save path")
    elif save and save_path is None:
        raise ValueError("save is on, but save path is None")
    elif save and save_path is not None:
        file = open(save_path, "wb")
        file.write(_base64.b64encode(content.encode("ascii")))
        file.close()
    else:
        return _base64.b64encode(content.encode("ascii"))
def decode(_bytes: bytes = None, read: bool = False, read_path: str = None):
    if _bytes is not None and read:
        raise ValueError("Bytes have been passed in but read mode is still on")
    elif not read and read_path is not None:
        raise ValueError("read is off, but still have read path")
    elif read and read_path is None:
        raise ValueError("read is on, but read path is None")
    elif read and read_path is not None:
        file = open(read_path, "rb")
        content = _base64.b64decode(file.read()).decode("utf-8")
        file.close()
        return content
    else:
        return _base64.b64decode(_bytes).decode("utf-8")
def decimal(obj: float):
    _obj = str(obj)
    returned = []
    for index in range(1, len(_obj)):
        if _obj[-index] == ".": break
        else: returned.append(_obj[-index])
    returned.reverse()
    rstring = ""
    for char in returned: rstring += char
    return rstring
def _merge_string_list(obj: list):
    new_string = ""
    for text in obj: new_string += text
    return new_string
def Round(obj: float, _to: int = 0):
    if not _to: return round(obj)
    if len(str(decimal(obj))) < _to:
        return round(obj, _to)
    decimals = list(str(decimal(obj)))
    count = 1
    AddOne = False
    if len(decimals) == 1: return obj
    if int(decimals[_to]) >= 5:
        decimals[_to - 1] = str(int(decimals[_to - 1]) + 1)
    del decimals[_to: len(decimals)]
    while int(decimals[_to - count]) == 10:
        if _to - count <= 0: decimals[_to - count] = "0"; AddOne = True; break
        decimals[_to - count] = "0"
        decimals[_to - count - 1] = str(int(decimals[_to - count - 1]) + 1)
        count += 1
    decimals = _merge_string_list(decimals)
    Object = str(int(obj))
    res = Object + "." + decimals
    if AddOne: return float(res) + 1
    else: return float(res)
def Range(range_x: int or float, range_y: int or float = None, step: int or float = None):
    if range_y is None: range_y = range_x; range_x = 0
    if step is None: step = 1
    if range_x < range_y:
        while range_x < range_y:
            yield range_x
            range_x += step
    if range_x > range_y:
        while range_x >= range_y:
            yield range_x
            range_x -= step

def get_ttyinfo():
    fd = _system.stdin.fileno()
    old_ttyinfo = _termios.tcgetattr(fd)
    new_ttyinfo = old_ttyinfo[:]
    new_ttyinfo[3] &= ~_termios.ICANON
    new_ttyinfo[3] &= ~_termios.ECHO
    return fd, old_ttyinfo, new_ttyinfo


# Convert variable name to string
def nameof(var):
    callers_local_vars = _inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var][0]

def createof(Type, *args, **kwargs):
    __object__ = Type(*args, **kwargs)
    for keys, vals in Type.__dict__.items():
        if type(vals) is list: __object__[keys] = Type.__dict__[keys].copy()
        if type(vals) is dict: __object__[keys] = Type.__dict__[keys].copy()
    return __object__
def Convert(obj, Type):
    if type(obj) is list:
        return_list = [].copy()
        for index in range(len(obj)):
            return_list[index] = Type(obj[index])
        return return_list
    elif type(obj) is dict:
        return_dict = {}.copy()
        for key in obj:
            return_dict[key] = Type(obj[key])
        return return_dict
    else: return Type(obj)
def breakdown(obj):
    return_list = [].copy()
    for index in range(len(obj)):
        try:
            for _index in range(len(obj[index])):
                return_list.append(obj[index][_index])
        except TypeError:
            continue
    return return_list
                
def varconvert(var):
    try:
        int(var)
        if "." in var:
            return float(var)
        else: return int(var)
    except ValueError:
        if var.lower() in ("none", "null"):
            return None
        if var.lower() == "true":
            return True
        if var.lower() == "false":
            return False
        import ast
        return ast.literal_eval(var)
            
            

class cursor:
    def __init__(self):
        self.ci = None
        if _os.name == "nt":
            self._msvcrt = __import__("msvcrt")
            self._ctypes = __import__("ctypes")
            class _CursorInfo(self._ctypes.Structure):
                _fields_ = [("size", self._ctypes.c_int), ("visible", self._ctypes.c_byte)]
            self.ci = _CursorInfo()
    def hide(self):
        if _os.name == "nt":
            handle = self._ctypes.windll.kernel32.GetStdHandle(-11)
            self._ctypes.windll.kernel32.GetConsoleCursorInfo(handle, self._ctypes.byref(self.ci))
            self.ci.visible = False
            self._ctypes.windll.kernel32.SetConsoleCursorInfo(handle, self._ctypes.byref(self.ci))
        elif _os.name == "posix":
            _system.stdout.write("\033[?25l")
            _system.stdout.flush()
    def show(self):
        if _os.name == "nt":
            handle = self._ctypes.windll.kernel32.GetStdHandle(-11)
            self._ctypes.windll.kernel32.GetConsoleCursorInfo(handle, self._ctypes.byref(self.ci))
            self.ci.visible = True
            self._ctypes.windll.kernel32.SetConsoleCursorInfo(handle, self._ctypes.byref(self.ci))
        elif _os.name == "posix":
            _system.stdout.write("\033[?25h")
            _system.stdout.flush()

class console:
    @staticmethod
    def write(*content, timer: int = 0.02, skip=breakdown(_color.__color__),sep=" " ,end="\n"):
        for text in content:
            text = str(text)
            for index in range(len(text)):
                _system.stdout.write(text[index])
                _system.stdout.flush()
                if type(skip) is str and text[index] != skip: _time.sleep(timer)
                elif type(skip) is list and text[index] not in skip: _time.sleep(timer)
                elif type(skip) is not str and type(skip) is not list: raise Exception("Error, arg skip should be \'str\' or \'list\', not " + type(skip).__name__)
            _system.stdout.write(sep)
            _system.stdout.flush()
        print(end=end, flush=True)
    @staticmethod
    def read(putout: str = "", rtype=str, **args):
        console.write(putout, end="", **args)
        return rtype(input(""))
    @staticmethod
    def clsline(clear_char=50): _system.stdout.write("\r" + " " * clear_char + "\r"); _system.stdout.flush()
    @staticmethod
    def reline(): print(end="\033[F", flush=True)
    if _os.name == "posix":
        import termios as _termios
        @staticmethod
        def simulation(desc="command: ", key_event=lambda :None):
            def writef(content):
                _system.stdout.write(content)
                _system.stdout.flush()
            command = ""
            ttyinfo = get_ttyinfo()
            key = ""
            writef(desc)
            while 1:
                _termios.tcsetattr(ttyinfo[0], _termios.TCSANOW, ttyinfo[2])
                key = _os.read(ttyinfo[0], 7).decode("utf-8")
                _termios.tcsetattr(ttyinfo[0], _termios.TCSANOW, ttyinfo[1])
                writef("\r")
                if key == "\n": break
                if key == "\x7f":
                     command = command[:-1]
                     writef(" " * (len(command) + len(desc) + 1) + "\r")
                     writef(desc + command)
                     continue
                key_event()
                command += key
                writef(desc + command)
            print(flush = True)
            command = command.split(" ")
            return command
class Server:
    class __SFTP:
        def __init__(self, ssh: _paramiko.SSHClient = None):
            if ssh is not None:
                self.scp = ssh.open_sftp()
        def update(self, *args, **kwargs):
            self.scp.get(*args, **kwargs)
        def upload(self, *args, **kwargs):
            self.scp.put(*args, **kwargs)
        def close(self):
            self.scp.close()
    def __init__(self, host: str, user: str, password: str, keypath: str, port: int = 22, **kwargs):
        self.ssh = _paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(_paramiko.AutoAddPolicy())
        self.host = host
        self.user = user
        self.password = password
        self.keypath = keypath
        self.port = port
        self.kwargs = kwargs
        self.sftp = self.__SFTP(None)

    def connect(self, timeout: int = 3, wait_time: float = 5.5):
        while True:
            try:
                self.ssh.connect(self.host, self.port, self.user, self.password, key_filename=self.keypath, **self.kwargs)
                break
            except Exception as error:
                _time.sleep(wait_time)
                timeout -= 1
                if timeout <= 0:
                    return error
        self.sftp = self.__SFTP(self.ssh)

    def send(self, command):
        class Standard:
            def __init__(self, stdin: _paramiko.channel.ChannelStdinFile, stdout: _paramiko.channel.ChannelFile, stderr: _paramiko.channel.ChannelStderrFile):
                self.input = stdin
                self.output = stdout
                self.error = stderr
                self.stdin = stdin
                self.stdout = stdout
                self.stderr = stderr
                self.value = (stdin, stdout, stderr)
            def __getitem__(self, key):
                if key is int: return self.value[key]
                if key is str: return self.__dict__[key]
            def get(self, standard):
                if type(standard) is str:
                    return self.__dict__[standard].read().decode("utf-8")
                else: return standard.read().decode("utf-8")

        return Standard(*tuple(self.ssh.exec_command(command)))

    def get(self, server_file, local_file=None, mode="r"):
        if local_file is None: local_file = server_file
        self.sftp.update(server_file, local_file)
        file = open(local_file, mode)
        content = file.read()
        file.close()
        os.remove(local_file)
        return content

    def close(self):
        self.ssh.close()
        self.sftp.close()

if _os.name == "posix":
    import termios as _termios
    def localmode(event=lambda fd: _os.read(fd, 7).decode("utf-8")):
        fd = _system.stdin.fileno()
        old_ttyinfo = _termios.tcgetattr(fd)
        new_ttyinfo = old_ttyinfo[:]
        new_ttyinfo[3] &= ~_termios.ICANON
        new_ttyinfo[3] &= ~_termios.ECHO
        _termios.tcsetattr(fd, _termios.TCSANOW, new_ttyinfo)
        key = event(fd)
        _termios.tcsetattr(fd, _termios.TCSANOW, old_ttyinfo)
        return key

    def getpass(echo="*"):
        fd = _system.stdin.fileno()
        old_ttyinfo = _termios.tcgetattr(fd)
        new_ttyinfo = old_ttyinfo[:]
        new_ttyinfo[3] &= ~_termios.ICANON
        new_ttyinfo[3] &= ~_termios.ECHO
        password = ""
        key = ""
        while key != "\n":
            _termios.tcsetattr(fd, _termios.TCSANOW, new_ttyinfo)
            key = _os.read(fd, 7).decode("utf-8")
            _termios.tcsetattr(fd, _termios.TCSANOW, old_ttyinfo)
            if key == "\x7f":
                password = password[:-1]
                _system.stdout.write("\r" + " " * (len(password) + len(echo)) + "\r")
                _system.stdout.flush()
                _system.stdout.write(echo * len(password))
                _system.stdout.flush()
                continue
            password += key
            _system.stdout.write("\r")
            _system.stdout.flush()
            _system.stdout.write(echo * len(password))
            _system.stdout.flush()
        print(flush=True)
        return password


