from datetime import timedelta as base_timedelta
from string import digits as digit_characters

_DATE_UNITS = {"Y": "years", "M": "months", "D": "days"}
_TIME_UNITS = {"H": "hours", "M": "minutes", "S": "seconds"}
_WEEK_UNITS = {"W": "weeks"}

_DECIMAL_POINT_CHARACTERS = frozenset(".,")
_FIELD_CHARACTERS = frozenset(digit_characters + "-:")

_GREGORIAN_MAXIMA = {
    "months": 12,
    "days_of_year": 366,
    "days_of_month": 31,
    "hours": 23,
    "minutes": 59,
    "seconds": 59,
}


class timedelta(base_timedelta):
    def isoformat(self):
        """Return the duration formatted according to ISO."""
        if not self:
            return "P0D"
        if not any([self.seconds, self.microseconds, self.days % 7]):
            return f"P{int(self.days / 7)}W"

        years, months, days = 0, 0, self.days
        hours, minutes, seconds = 0, 0, self.seconds
        days, seconds = days + int(seconds / 86400), seconds % 86400
        hours, seconds = hours + int(seconds / 3600), seconds % 3600
        minutes, seconds = minutes + int(seconds / 60), seconds % 60

        fields = (
            ("", "P"),
            ("Y", years),
            ("M", months),
            ("D", days),
        )
        if hours or minutes or seconds or self.microseconds:
            fields += (
                ("", "T"),
                ("H", hours),
                ("M", minutes),
                ("S", seconds + self.microseconds / 10**6),
            )
        return str().join(f"{v}{designator}" for designator, v in fields if v)

    @classmethod
    def _parse_date(cls, date_string):
        date_length = len(date_string)
        if not len("YYYYDDD") <= date_length <= len("YYYY-MM-DD"):
            raise ValueError(f"unable to parse '{date_string}' as a date")
        dash_positions = [i for i, c in enumerate(date_string) if c == "-"]

        # YYYYDDD
        if date_length == 7 and dash_positions == []:
            yield "years", int(date_string[0:4])
            yield "days_of_year", int(date_string[4:7])

        # YYYY-DDD
        elif date_length == 8 and dash_positions == [4]:
            yield "years", int(date_string[0:4])
            yield "days_of_year", int(date_string[5:8])

        # YYYYMMDD
        elif date_length == 8 and dash_positions == []:
            yield "years", int(date_string[0:4])
            yield "months", int(date_string[4:6])
            yield "days_of_month", int(date_string[6:8])

        # YYYY-MM-DD
        elif date_length == 10 and dash_positions == [4, 7]:
            yield "years", int(date_string[0:4])
            yield "months", int(date_string[5:7])
            yield "days_of_month", int(date_string[8:10])

    @classmethod
    def _parse_time(cls, time_string):
        time_length = len(time_string)
        if not len("HHMMSS") <= time_length <= len("HH:MM:SS.ssssss"):
            raise ValueError(f"unable to parse '{time_string}' as a time")
        colon_positions = [i for i, c in enumerate(time_string) if c == ":"]

        # HHMMSS[.ssssss]
        if time_length >= 6 and colon_positions == []:
            yield "hours", int(time_string[0:2])
            yield "minutes", int(time_string[2:4])
            yield "seconds", int(time_string[4:6])
            if time_length == 6:
                return
            if not time_string[6] == ".":
                raise ValueError(f"invalid suffix in '{time_string}'")
            yield "microseconds", int(time_string[7:]) * 10**3

        # HH:MM:SS[.ssssss]
        elif time_length >= 8 and colon_positions == [2, 5]:
            yield "hours", int(time_string[0:2])
            yield "minutes", int(time_string[3:5])
            yield "seconds", int(time_string[6:8])
            if time_length == 8:
                return
            if not time_string[8] == ".":
                raise ValueError(f"invalid suffix in '{time_string}'")
            yield "microseconds", int(time_string[9:]) * 10**3

    @classmethod
    def _filter_elements(cls, pairs):
        for k, v in pairs:
            # Note: ISO date elements (years, months, days) can be zero-valued
            max = _GREGORIAN_MAXIMA.get(k, v)
            if not 0 <= v <= max:
                raise ValueError(f"{k}: {v} exceeds permitted range 0..{max}")
            if k.startswith("days_of"):
                yield "days", v
            elif v:
                yield k, v

    @classmethod
    def _parse_duration(cls, duration_string):
        character_stream = iter(duration_string)
        if next(character_stream, None) != "P":
            raise ValueError("must start with the character 'P'")

        date_designators = iter(("Y", "M", "D"))
        time_designators = iter(("H", "M", "S"))
        week_designators = iter(("W",))
        remaining_designators, units = date_designators, _DATE_UNITS

        char, value, designator = None, str(), None
        for char in character_stream:
            if char in _FIELD_CHARACTERS:
                value += char
                continue

            if char in _DECIMAL_POINT_CHARACTERS:
                if not value:
                    raise ValueError("integer part required in decimals")
                value += "."
                continue

            if char == "T":
                if value and designator:
                    raise ValueError(f"unexpected content after {designator}")
                if value:
                    yield from cls._filter_elements(cls._parse_date(value))
                    value = str()
                remaining_designators, units = time_designators, _TIME_UNITS
                continue

            if char == "W":
                remaining_designators, units = week_designators, _WEEK_UNITS
                pass

            # Note: this 'in' condition advances and may exhaust the iterator
            designator = char if char in remaining_designators else None
            if not designator:
                raise ValueError(f"unexpected character '{char}'")
            if not value:
                raise ValueError(f"missing number before '{char}'")

            yield units[designator], float(value)
            value = str()

        if char == "T":
            raise ValueError("incomplete time-string")
        if value and designator:
            raise ValueError(f"unexpected content after {designator}")
        if value:
            segment_parser = {
                date_designators: cls._parse_date,
                time_designators: cls._parse_time,
            }[remaining_designators]
            yield from cls._filter_elements(segment_parser(value))

    @classmethod
    def fromisoformat(cls, duration_string):
        """Construct a duration from a string in ISO 8601 format."""
        if not isinstance(duration_string, str):
            raise TypeError("fromisoformat: argument must be str")

        def _invalid_format(reason):
            msg = f"Invalid isoformat string '{duration_string}': {reason}"
            return ValueError(msg)

        try:
            measurements = dict(cls._parse_duration(duration_string))
        except ValueError as e:
            raise _invalid_format(str(e)) from e
        if not measurements:
            raise _invalid_format("no duration measurements found")
        if "weeks" in measurements and len(measurements.keys()) > 1:
            raise _invalid_format("cannot mix weeks with other units")

        try:
            return cls(**measurements)
        except TypeError as e:
            msg = "Unsupported: could not create timedelta for this duration"
            raise NotImplementedError(msg) from e
