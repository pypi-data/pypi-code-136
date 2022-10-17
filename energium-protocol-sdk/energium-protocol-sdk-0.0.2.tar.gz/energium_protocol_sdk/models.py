from typing import Optional, Iterable

from pydantic import BaseModel
from pydantic.errors import ConfigError

from enum import Enum

from pydantic.utils import sequence_like

from energium_protocol_sdk.fields import reception, patient
from energium_protocol_sdk.fields.base import EnergiumField


class EnergiumDelimiter(str, Enum):
    Patient = "^^^P"
    Reception = "^^^S"
    ReceptionData = "^SS"


class EnergiumModel(BaseModel):
    delimiter: Optional[EnergiumDelimiter] = None
    list_delimiter: Optional[EnergiumDelimiter] = None

    def _get_energium_value(self, v, pretty=False):
        newline = "\n" if pretty else ""
        result = ""
        if not v:
            return result
        if isinstance(v, EnergiumDelimiter):
            # delimiter is not for representation
            return result
        if isinstance(v, EnergiumField):
            result += v.as_energium()
        elif isinstance(v, EnergiumModel):
            result += v.energium(pretty)
        elif sequence_like(v) and v:
            list_delimiter: Optional[EnergiumDelimiter] = v[0].list_delimiter
            if list_delimiter:
                result += f"{list_delimiter}{newline}"
            for item in v:
                result += self._get_energium_value(item, pretty)
            if list_delimiter:
                cnt = list_delimiter.count("^")
                closing_delimiter = list_delimiter.replace("^" * cnt, "^" * cnt + "_")
                result += f"{closing_delimiter}{newline}"
        else:
            raise ConfigError(
                f"Field {v} must be instance of EnergiumField or EnergiumModel"
            )
        return result

    def energium(self, pretty=False) -> str:
        """Convert data into energium protocol."""
        result: str = ""
        newline = "\n" if pretty else ""
        if self.delimiter:
            result += f"{self.delimiter.value}{newline}"
        for _, v in self._iter():
            result += self._get_energium_value(v, pretty)
        if self.delimiter:
            cnt = self.delimiter.value.count("^")
            closing_delimiter = self.delimiter.replace("^"*cnt, "^"*cnt + "_")
            result += f"{newline}{closing_delimiter}{newline}"
        return result


class Patient(EnergiumModel):
    """May have 20 user-defined fields ^P1 - ^P20."""
    delimiter = EnergiumDelimiter.Patient

    id: patient.Id
    name: patient.Name
    sex: Optional[patient.Sex]
    age: Optional[patient.Age]
    room: Optional[patient.Room]


class Reception(EnergiumModel):
    """May have 20 user-defined fields ^T01 - ^T23."""
    delimiter = EnergiumDelimiter.ReceptionData
    list_delimiter = EnergiumDelimiter.Reception

    number: reception.SpecimenNumber
    code: reception.TubeCode
    tube_name: Optional[reception.TubeName]
    count: Optional[reception.TubeCount]
    specimen_name: Optional[reception.SpecimenName]


class Order(EnergiumModel):
    patient: Patient
    reception: list[Reception]
