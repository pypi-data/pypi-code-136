import csv
from dataclasses import astuple, dataclass
import pathlib
from typing import Generic, TypeVar

from python_utilisation.utils_list import UtilsList

T = TypeVar('T')

@dataclass
class ReadCSV(Generic[T]):
    """Class Read Csv."""

    path = pathlib.Path(__file__).parent.parent.parent
    newline:str = str("")
    delimiter:str = str(";")

    @property
    def path_file(self):
        """path file data."""
        return self.path.joinpath("data_csv22.csv")
    
    def insert(self, data:T):
        """insert into."""
        self._write_(data)

    def update(self, data:T):
        """Update from."""
        for_update = self._for_update_(data)
        self._update_(for_update)
   
    def delete(self,data:object):
        """Delete from."""
        self._delete_(data)


    def transform_data_to_tuple(self, data:T):
        """transform data to tuple"""
        if isinstance(data,list):return [astuple(i) for i in data]
        return astuple(data)
        
    def transform_data_to_object(self, data:object):
        """transform data to object"""
        if isinstance(data,list):return [T(*i) for i in data]
        return T(*data)

    def set_data(self, data:T)->list[T]:
        """Set data as tuple."""
        if isinstance(data, list): return [astuple(i) for i in data][0] 
        return astuple(data)
 
    
    def research_by_id(self, id:int)->list[T]:
        """Set research by id."""
        if self.select_as_object(): return [i for i in self.select_as_object() if id == int(i.id_etudiant)]

    def research_by_name(self, name:str)->list[T]:
        """Set research by name."""
        if self.select_as_object(): return [i for i in self.select_as_object() if str(name) in str(i.firstname)]


    def _header_(self, data:T)->list:
        return [str(i) for i in data.__dict__.keys()]


    def verify_paramerter(self, data:T):
        return [i for i in data.__dict__.keys()]


    def select(self)->list[tuple]:
        """select all from database csv."""
        return self._read_()

    def select_as_object(self)->list[T]:
        """select all from database csv as list[object]."""
        return [T(*i) for i in self.select()]


    def _read_(self)->list[T]:
        """read data csv."""

        if self.path:
            with open(self.path_file, "r", newline=self.newline) as file_csv:
                reading = csv.reader(file_csv, delimiter=self.delimiter, quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
                list_data = [tuple(i) for i in reading]
                file_csv.close()
                return list_data
        else: print('Open File Error: filename stores a None value')

    def _write_(self, data:T):
        """write data csv."""

        if self.path:
            header = self._header_(data)
            datas = self.set_data(data)
            with open(self.path_file, "a", newline=self.newline) as file_csv:
                writing = csv.writer(file_csv, delimiter=self.delimiter, quotechar='"')
                writing.writerow(datas)
                file_csv.close()
        else: print('Open File Error: filename stores a None value')

    def _update_(self, list_data:list[T]):
        """update data csv."""

        if self.path:
            with open(self.path_file, "w", newline=self.newline) as file_csv:
                updated = csv.writer(file_csv, delimiter=self.delimiter)
                for i in list_data: 
                    updated.writerow(astuple(i))
                file_csv.close()
        else: print('Open File Error: filename stores a None value')


    def _for_update_(self, data:T):
        """call update."""
        list_data = self.select_as_object()
        for key,value in enumerate(list_data):
            if int(data) == int(value.id_etudiant):
                UtilsList(list_data).add_at(data, key)
                break
        return list_data

    def _delete_(self, data:object):
        """call update."""
        for_delete = self._for_delete_(data)
        self._update_(for_delete)

    def _for_delete_(self, data:T):
        """call update."""
        list_data = self.select_as_object()
        for key,value in enumerate(list_data):
            if int(data.id_etudiant) == int(value.id_etudiant):
                UtilsList(list_data).remove_at(key)
                break
        return list_data

    def last_insert(self)->T:
        """last insert"""
        return self.select_as_object()[-1]
