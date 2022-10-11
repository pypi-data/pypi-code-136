from datetime import datetime

from tablib import Dataset


class datetimeZ(datetime):

    @classmethod
    def fromisoformat(cls, date_string):
        return super().fromisoformat(date_string[:-1])

    def isoformat(self, sep='T', timespec='auto'):
        return super().isoformat(sep=sep, timespec=timespec) + 'Z'

    def __str__(self):
        return super().__str__()[:-1]


class GeneralResponse:

    def __init__(self, json_data):
        for name, attr_type in self.__dict__.items():
            if name not in json_data.keys():
                json_data[name] = None
            if json_data[name] is None:
                pass
            elif isinstance(attr_type, list):
                json_data[name] = [attr_type[0](x) for x in json_data[name]]
            else:
                json_data[name] = attr_type(json_data[name])
        if json_data:
            self.__dict__.update(json_data)

    def __repr__(self):
        init = ", ".join(f'{key}={value}' for key, value in self.__dict__.items() if not key.startswith("_"))
        return f'{self.__class__.__name__}({init})'


class CommugenMain(GeneralResponse):

    @staticmethod
    def _is_list_of_Listlings(obj):
        try:
            for listable in obj:
                listable.dict()
        except (TypeError, AttributeError):
            return False
        else:
            return True

    def _things(self):
        for response in vars(self).values():
            for value in vars(response).values():
                if self._is_list_of_Listlings(value):
                    return value

    def df(self):
        a = Dataset()
        parsed = []
        list_of_lists = [w.dict(system=True) for w in self]
        keys = list(set().union(*list_of_lists))
        keys.sort()
        ur_line = {key: None for key in keys}
        for list_record in self:
            pending_line = list_record.dict(system=True)
            for key, value in pending_line.items():
                if isinstance(value, (dict, list)):
                    stringed = ', '.join(str(item) for item in value)
                    pending_line[key] = stringed
            line = ur_line.copy()
            line.update(pending_line)
            parsed.append(line)
        a.dict = parsed
        return a

    def __len__(self):
        return len(self._things())

    def __getitem__(self, item):
        return self._things()[item]

    def __repr__(self):
        init = ", ".join(f'{key}={value}' for key, value in self.__dict__.items() if not key.startswith("_"))
        return f'{self.__class__.__name__}({init})'

    def __str__(self):
        return str(self.df())



class CommugenModel(CommugenMain):

    def __init__(self, json_data):
        self.records = CommugenRecords
        """:type: CommugenRecords"""
        super().__init__(json_data)


class CommugenTables(CommugenMain):

    def __init__(self, json_data):
        self.forms = CommugenForms
        """:type: CommugenForms"""
        super().__init__(json_data)


class CommugenDomains(CommugenMain):

    def __init__(self, json_data):
        self.comms = CommugenComms
        """:type: CommugenComms"""
        super().__init__(json_data)


class CommugenList(GeneralResponse):

    def __init__(self, json_data):
        self.hasMore = bool
        """:type : bool"""
        self.offset = int
        """:type : int"""
        super().__init__(json_data)


class CommugenRecords(CommugenList):

    def __init__(self, json_data):

        self.list = [CommugenRecord]
        """:type : list[CommugenRecord]"""

        super().__init__(json_data)


class CommugenComms(CommugenList):

    def __init__(self, json_data):
        self.list = [CommugenDomain]
        """:type : list[CommugenDomain]"""

        super().__init__(json_data)


class CommugenForms(CommugenList):

    def __init__(self, json_data):
        self.list = [CommugenForm]
        """:type : list[CommugenForm]"""

        super().__init__(json_data)


class CommugenListling(GeneralResponse):

    def dict(self, system=False):
        if not system:
            return {key: value for key, value in self.__dict__.items() if not key.startswith("_")}
        return self.__dict__.copy()


class CommugenDomain(CommugenListling):

    def __init__(self, json_data):

        self.creationDate = datetimeZ.fromisoformat
        """:type : datetime"""
        self.domain = str
        """:type : str"""
        self.lang = str
        """:type : str"""
        self.title = str
        """:type : str"""
        super().__init__(json_data)


class CommugenForm(CommugenListling):

    def __init__(self, json_data):
        self.apiName = str
        """:type : str"""
        self.apiStatus = str
        """:type : str"""
        self.group = str
        """:type : str"""
        self.id = int
        """:type : int"""
        self.name = str
        """:type : str"""
        super().__init__(json_data)


class CommugenRecord(CommugenListling):

    def __init__(self, json_data):

        self._id = int
        """:type : int"""
        self._creatorID = int
        """:type : int"""
        self._lastUpdateDate = datetimeZ.fromisoformat
        """:type : datetime"""
        super().__init__(json_data)


class CommugenSingleRecord(GeneralResponse):

    def __init__(self, json_data):

        self.record = CommugenRecordMurchav
        ":type: CommugenRecordMurchav"
        super().__init__(json_data)


class CommugenRecordMurchav(CommugenRecord):

    def __init__(self, json_data):

        self._creationDate = datetimeZ.fromisoformat
        """:type : datetime"""
        self._lastUpdaterID = int
        """:type : int"""
        self._publicState = int
        """:type : int"""
        super().__init__(json_data)


class CommugenOptions(CommugenMain):
    def __init__(self, json_data):
        self.info = CommugenInfo
        """:type: CommugenInfo"""
        super().__init__(json_data)


class CommugenField(CommugenListling):

    def __init__(self, json_data):
        self.apiName = str
        """:type : str"""
        self.id = int
        """:type : int"""
        self.mode = str
        """:type : str"""
        self.name = str
        """:type : str"""
        self.type = str
        """:type : str"""
        super().__init__(json_data)


class CommugenFieldOptions(CommugenField):
    def __init__(self, json_data):
        self.options = [CommugenOption]
        """:type : [CommugenOption]"""
        super().__init__(json_data)


class CommugenOption(GeneralResponse):

    def __init__(self, json_data):
        self.apiName = str
        """:type : str"""
        self.id = int
        """:type : int"""
        self.title = str
        """:type : str"""
        super().__init__(json_data)

    def __str__(self):
        return self.apiName


class CommugenInfo(GeneralResponse):

    def __init__(self, json_data):
        self.fields = [CommugenFieldOptions]
        """ :type : [CommugenFieldOptions]"""
        self.header = dict
        """:type : dict"""
        self.listName = str
        """:type : str"""
        self.methods = [str]
        """:type : [str]"""
        self.type = str
        """:type : str"""
        super().__init__(json_data)
