import json
from .. import config
from .theme import BasicTheme

import os
import pathlib
import pandas as pd
from abc import ABC
from io import BufferedReader
from datetime import datetime
from typing import List, Dict, Union

class LogReporter(ABC):
    '''
    description 
    ----------
    (abstract class) LogReporter: doyle's logging management class

    import
    ----------
    dolye.utils.LogReporter

    class attributes
    ----------
        log : str           
            history of raw log
        
        clog : str           
            history of printed log (with ASCII ESC code)
        
        active : bool        
            active status of LogReporter if False LogReporter will be idle (default = active)
        
        verbose_level : int  
            verbose level for printing log: (default = 3)
                if >= 1: print error log
                if >= 2: print warning log
                if >= 3: print report log, title log and plain log
        
        theme : BasicTheme   
            theme class for reporting log (you can customize you our theme by inherite doyle.utils.theme.BasicTheme class and overwrite its methods)

    class method for class status
    ----------
        set_verbose(set_value : int) -> None
            set verbose level for LogReporter
        
        activate() -> None
            activate LogReporter
        
        deactivate() -> None
            deactivate LogReporter
        
        history(line: int or None = None, reverse : bool = False) -> None
            show n lines history log
        
        head(n : int = 10) -> None
            show first n lines of history log
        
        tail(n : int = 10) -> None
            show last n lines of history log
        
        save(path : str = ".", reset : bool = False) -> None
            save log history as file to specified path (there 2 new plain text files with extension 'log' and 'clog')
        
        clear(save_path : str = None) -> None
            clear log history

        render(path : str) -> None
            show log history of file from specified path
        
    class method for logging
    ----------
        title(text : str) -> None
            logging text as title log (show if verbose_level >= 3)

        plain(text : str) -> None
            logging text as plain log (show if verbose_level >= 3)

        report(text : str) -> None
            logging text as report log (show if verbose_level >= 3)

        warning(text : str) -> None
            logging text as warning log (show if verbose_level >= 2)

        error(text : str) -> None
            logging text as error log (show if verbose_level >= 1)
    '''
    
    log : str = ""
    "(class attribute) history of raw log"
    clog : str = ""
    "(class attribute) history of printed log (with ASCII ESC code)"
    verbose_level : int = 3
    '''(class attribute) verbose level for printing log: (default = 3)
                if >= 1: print error log
                if >= 2: print warning log
                if >= 3: print report log, title log and plain log'''
    active = True
    "(class attribute) active status of LogReporter if False LogReporter will be idle"
    theme = BasicTheme
    "(class attribute) theme class for reporting log (you can customize you our theme by inherite doyle.utils.theme.BasicTheme class and overwrite its methods)"

    @classmethod
    def set_verbose(cls, set_value: int): 
        '''
        description 
        ----------
        (class method) set verbose level for LogReporter

        parameters
        ----------
            set_value : int
                verbose level for printing log:
                    if >= 1: print error log
                    if >= 2: print warning log
                    if >= 3: print report log, title log and plain log
        '''
        cls.verbose_level = set_value

    @classmethod
    def activate(cls): 
        '''
        description 
        ----------
        (class method) activate LogReporter
        '''
        cls.active = True

    @classmethod
    def deactivate(cls): 
        '''
        description 
        ----------
        (class method) deactivate LogReporter
        '''
        cls.active = False

    @classmethod
    def title(cls, text: str):
        '''
        description 
        ----------
        (class method) logging text as title log (show if verbose_level >= 3)

        parameters
        ----------
            text : str
                text for logging
        '''
        if cls.active:
            original = str(text)
            text = cls.theme.title(text)
            if cls.verbose_level > 2: print(text, end="")
            cls.log += original + '\n'
            cls.clog += text

    @classmethod
    def plain(cls, text: str):
        '''
        description 
        ----------
        (class method) logging text as plain log (show if verbose_level >= 3)

        parameters
        ----------
            text : str
                text for logging
        '''
        if cls.active:
            original = str(text)
            text = cls.theme.plain(text)
            if cls.verbose_level > 2: print(text, end="")
            cls.log += original + '\n'
            cls.clog += text

    @classmethod
    def report(cls, text: str):
        '''
        description 
        ----------
        (class method) logging text as report log (show if verbose_level >= 3)

        parameters
        ----------
            text : str
                text for logging
        '''
        if cls.active:
            original = str(text)
            text = cls.theme.report(text)
            if cls.verbose_level > 2: print(text, end="")
            cls.log += original + '\n'
            cls.clog += text

    @classmethod
    def warning(cls, text: str):
        '''
        description 
        ----------
        (class method) logging text as warning log (show if verbose_level >= 2)

        parameters
        ----------
            text : str
                text for logging
        '''
        if cls.active:
            original = str(text)
            text = cls.theme.warning(text)
            if cls.verbose_level > 1: print(text, end="")
            cls.log += original + '\n'
            cls.clog += text

    @classmethod
    def error(cls, text: str):
        '''
        description 
        ----------
        (class method) logging text as error log (show if verbose_level >= 3)

        parameters
        ----------
            text : str
                text for logging
        '''
        if cls.active:
            original = str(text)
            text = cls.theme.error(text)
            if cls.verbose_level > 0: print(text, end="")
            cls.log += original + '\n'
            cls.clog += text

    @classmethod
    def render(cls, path):
        '''
        description 
        ----------
        (class method) show log history of file from specified path

        parameters
        ----------
            path : str
                path to log file
        '''
        with open(path, "r") as file: text = file.read()
        print(text)

    @classmethod
    def history(cls, line: int = None, reverse = False):
        '''
        description 
        ----------
        (class method) show n lines history log

        parameters
        ----------
            line : int
                number of line to show history log. show all line if None (default = None)
            reverse : bool
                if True show history start from last line and vice versa if False (default = False)
        '''
        log = cls.clog.split('\n')
        if line is None: 
            if reverse: print("\n".join(log[::-1]))
            else: print("\n".join(log))
        else:
            if line >= len(log): line = -1
            print(log[line])

    @classmethod
    def head(cls, n = 10):
        '''
        description 
        ----------
        (class method) show first n lines of history log

        parameters
        ----------
            n : int
                number of line to show (default = 10)
        '''
        log = cls.clog.split('\n')
        print("\n".join(log[:n]))

    @classmethod
    def tail(cls, n = 10):
        '''
        description 
        ----------
        (class method) show last n lines of history log

        parameters
        ----------
            n : int
                number of line to show (default = 10)
        '''
        log = cls.clog.split('\n')
        print("\n".join(log[-n:]))

    @classmethod
    def save(cls, path = ".", reset = False):
        '''
        description 
        ----------
        (class method) save log history as file to specified path (there 2 new plain text files with extension 'log' and 'clog')

        parameters
        ----------
            path : str
                path to directory for saving log files (default = '.' // current directory)
            reset : bool
                if True clear log history after saving (default = False) 
        '''
        now = datetime.now()
        path = pathlib.PurePath(path).as_posix()
        assert os.path.exists(path), f"path '{path}' is not exist."
        if os.path.isdir(path): path = os.path.join(path, \
            f"doyle-{now.year}-{now.month}-{now.day}_{now.timestamp()}")
        with open(path + ".log", "w") as file: file.write(cls.log)
        with open(path + ".clog", "w") as file: file.write(cls.clog)
        if reset: 
            cls.log = ""
            cls.clog = ""

    @classmethod
    def clear(cls, save_path = None):
        '''
        description 
        ----------
        (class method) clear log history

        parameters
        ----------
            save_path : str
                path to directory for saving log files. if None do not save (default = None)
        '''
        if save_path is not None: cls.save(save_path)
        cls.log = ""
        cls.clog = ""

FSIGN: Dict[str, str] = json.load(open(f"{config.__statics__}/fsign.json", "r"))

class FileReader(ABC):
    
    ignore_error = True
    header_limit = 32

    @classmethod
    def check_signature(cls, 
                        file_path: str or pathlib.PurePath or BufferedReader, 
                        xheader: str = None
                        ):
        if xheader is None:
            xheader = cls.extract_filesignature(file_path)
        det_type = None
        for sign in FSIGN.keys():
            if xheader.startswith(sign):
                det_type = FSIGN[sign]
                break
        return det_type, sign

    @classmethod
    def detect_file(cls, files: List[str or pathlib.PurePath]):
        fbuffer = list()
        for path in files:
            try: fbuffer.append(open(path, 'rb'))
            except Exception as e: LogReporter.error(f"read fail: {path} ({e})")
        xheaders = [ cls.extract_filesignature(file) for file in fbuffer ]
        filetypes: List[Dict] = list()

        for path, xheader, buffer in zip(files, xheaders, fbuffer):
            det_by_sign, sign = cls.check_signature(path, xheader)
            det_by_ext = cls.extract_extention(path)
            filetype = {
                        "path": pathlib.PurePath(path).as_posix(),
                        "signature": sign,
                    }
            if det_by_sign is not None:
                filetype['ftype'] = det_by_sign
            else:
                filetype['ftype'] = det_by_ext
            filetypes.append(filetype)
            buffer.close()

        return filetypes

    @classmethod
    def extract_filesignature(cls, file: Union[str, pathlib.PurePath, BufferedReader]):
        if isinstance(file, pathlib.PurePath) or isinstance(file, str):
            assert os.path.isfile(file), "{file} is not file."
            file = open(file, "rb")
        head_file = file.read(cls.header_limit)
        hex = " ".join([ f"{b:02X}" for b in head_file])
        return hex

    @classmethod
    def extract_extention(cls, file: str or pathlib.PurePath):
        assert os.path.isfile(file), "{file} is not file."
        if isinstance(file, pathlib.PurePath):
            file = file.as_posix()
        return file[file.rfind('.') + 1:].lower()

    @classmethod
    def read_files(cls, path: str, keep_none: bool = False):
        path = pathlib.PurePath(path)
        assert os.path.exists(path), f"do not found path; {path}"
        if os.path.isdir(path):
            ls = os.listdir(path)
            files = list()
            for f in ls:
                if os.path.isfile(path.as_posix() + '/' + f):
                    files.append(path.as_posix() + '/' + f)
        else:
            files = [ path.as_posix() ]
        meta = cls.detect_file(files)
        dfs: Dict[str, Union[pd.DataFrame, None]] = dict()
        for file in meta:
            LogReporter.report(f"read file at {file['path']} as {file['ftype']}")
            switch = cls.__switch_reader(file["ftype"])
            if keep_none: 
                dfs[file['path']] = switch(file["path"]) if switch is not None else None
            elif switch is not None:
                    dfs[file['path']] = switch(file["path"])
        return dfs

    @classmethod
    def __switch_reader(cls, type: str):
        if type == "xlsx" or type == "xls":
            return cls.excel_to_df
        if type == "xml":
            return cls.xml_to_df
        if type == "json":
            return cls.json_to_df
        if type == "csv":
            return cls.csv_to_df

        return None

    @classmethod
    def csv_to_df(cls, path: str or pathlib.PurePath or BufferedReader):
        try: df = pd.read_csv(path, sep=None, engine='python')
        except Exception as e:
            if not cls.ignore_error: raise e
            LogReporter.error(f"read fail: {path} ({e})")
            return None

        return df

    @classmethod
    def json_to_df(cls, path: str or pathlib.PurePath or BufferedReader):
        try:
            df = pd.read_json(path)
        except Exception as e:
            if not cls.ignore_error: raise e
            LogReporter.error(f"read fail: {path} ({e})")
            return None

        return df

    @classmethod
    def excel_to_df(cls, path: str or pathlib.PurePath or BufferedReader):
        try:
            df = pd.read_excel(path, sheet_name=None)
        except Exception as e:
            if not cls.ignore_error: raise e
            LogReporter.error(f"read fail: {path} ({e})")
            return None

        return df

    @classmethod
    def xml_to_df(cls, path: str or pathlib.PurePath or BufferedReader):
        try:
            df = pd.read_xml(path)
        except Exception as e:
            if not cls.ignore_error: raise e
            LogReporter.error(f"read fail: {path} ({e})")
            return None

        return df