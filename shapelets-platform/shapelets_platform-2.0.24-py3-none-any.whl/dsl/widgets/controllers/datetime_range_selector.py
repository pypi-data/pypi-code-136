# Copyright (c) 2021 Grumpy Cat Software S.L.
#
# This Source Code is licensed under the MIT 2.0 license.
# the terms can be found in LICENSE.md at the root of
# this project, or at http://mozilla.org/MPL/2.0/.
from __future__ import annotations

import datetime

from dataclasses import dataclass
from typing import Optional, Tuple, Union

from shapelets.dsl.widgets import AttributeNames, StateControl, Widget


@dataclass
class DatetimeRangeSelector(StateControl):
    title: str = None
    start_date_time: Union[float, int, str, datetime.datetime, datetime.date, datetime.time] = None
    end_date_time: Union[float, int, str, datetime.datetime, datetime.date, datetime.time] = None
    min_date: Union[float, int, str, datetime.date] = None
    max_date: Union[float, int, str, datetime.date] = None
    _format: Optional[str] = None

    def _validate_date(self, date):
        if isinstance(date, str):
            try:
                datetime.datetime.strptime(date, '%Y-%m-%d')
                return date
            except ValueError:
                return None

    def _check_datetime_aware(self, date):
        try:
            dt = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f %z')
            self._format = 'YYYY-MM-DD HH:mm:ss TZ'
            return date
        except:
            try:
                dt = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f%z')
                self._format = 'YYYY-MM-DD HH:mm:ss TZ'
                return date
            except:
                return None

    def _check_datetime(self, date):
        try:
            dt = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            self._format = 'YYYY-MM-DD HH:mm:ss'
            return date
        except:
            try:
                dt = datetime.datetime.strptime(self.start_date_time, '%Y-%m-%d %I:%M:%S %p')
                self._format = 'YYYY-MM-DD h:mm:ss a'
                size = len(date)
                mod_string = date[:size - 3]
                return mod_string
            except:
                return None

    def _check_date(self, date):
        try:
            dt = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            self._format = 'YYYY-MM-DD'
            return date
        except:
            return None

    def _check_time(self, time):
        try:
            dt = datetime.datetime.strptime(time, '%H:%M:%S').time()
            self._format = 'HH:mm:ss'
            return time
        except:
            try:
                dt = datetime.datetime.strptime(time, '%I:%M:%S %p').time()
                self._format = 'h:mm:ss a'

                size = len(time)
                mod_string = self.start_date_time[:size - 3]
                return mod_string
            except:
                return None

    def _check_datetime_float(self, date):
        try:
            result = datetime.datetime.fromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S')
            self._format = 'YYYY-MM-DD HH:mm:ss'
            return result
        except:
            return None

    def _validate_datetime(self, date):

        if isinstance(date, str):

            result = self._check_datetime_aware(date)
            if result is None:
                result = self._check_datetime(date)
                if result is None:
                    result = self._check_date(date)
                    if result is None:
                        result = self._check_time(date)
                        if result is None:
                            raise ValueError("Incorrect date format")

            return result


class DatetimeRangeSelectorWidget(DatetimeRangeSelector, Widget):

    def __init__(self, title: str = None,
                 start_date_time: Union[float, int, str, datetime.datetime, datetime.date, datetime.time] = None,
                 end_date_time: Union[float, int, str, datetime.datetime, datetime.date, datetime.time] = None,
                 min_date: Union[float, int, str, datetime.date] = None,
                 max_date: Union[float, int, str, datetime.date] = None, **additional):

        Widget.__init__(self, DatetimeRangeSelector.__name__, **additional)
        DatetimeRangeSelector.__init__(self, title, start_date_time, end_date_time, min_date, max_date)

        self._parent_class = DatetimeRangeSelector.__name__
        self._compatibility: Tuple = (DatetimeRangeSelector.__name__, float, str,
                                      datetime.datetime, datetime.date, datetime.time)

        if self.start_date_time is not None:
            if isinstance(self.start_date_time, datetime.datetime):
                if (self.start_date_time.tzinfo is not None and self.start_date_time.tzinfo.utcoffset(
                        self.start_date_time) is not None):
                    self._is_aware = True  # datetime is aware
                    self.start_date_time.strftime("%Y-%m-%d %H:%M:%S.%f %z")
                    self._format = 'YYYY-MM-DD HH:mm:ss TZ'

                else:
                    self._is_aware = False  # datetime is naive
                    self.start_date_time.strftime("%Y-%m-%d %H:%M:%S")
                    self._format = 'YYYY-MM-DD HH:mm:ss'

            elif isinstance(self.start_date_time, datetime.date):
                self._is_aware = False  # always date is naive
                self.start_date_time.strftime("%Y-%m-%d")
                self._format = 'YYYY-MM-DD'

            elif isinstance(self.start_date_time, datetime.time):
                if (self.start_date_time.tzinfo is not None and self.start_date_time.tzinfo.utcoffset(
                        None) is not None):
                    self._is_aware = True  # time is aware
                    self.start_date_time.strftime("%H:%M:%S.%f %z")
                    self._format = 'HH:mm:ss TZ'
                else:
                    self._is_aware = False  # time is naive
                    self.start_date_time.strftime("%H:%M:%S")
                    self._format = 'HH:mm:ss'

            elif isinstance(self.start_date_time, str):
                self._validate_datetime(self.start_date_time)

            elif isinstance(self.start_date_time, float):
                self._check_datetime_float(self.start_date_time)

        if self.min_date is not None:
            if isinstance(self.min_date, str):
                self._validate_date(self.min_date)
            elif isinstance(self.min_date, datetime.date):
                pass
            elif isinstance(self.min_date, float) or isinstance(self.min_date, int):
                try:
                    self.min_date = datetime.datetime.fromtimestamp(self.min_date).strftime('%Y-%m-%d')
                except:
                    raise ValueError("Incorrect date format for min_date. Wrong float or int")

        if self.max_date is not None:
            if isinstance(self.max_date, str):
                self._validate_date(self.max_date)
            elif isinstance(self.max_date, datetime.date):
                pass
            elif isinstance(self.max_date, float) or isinstance(self.max_date, int):
                try:
                    self.max_date = datetime.datetime.fromtimestamp(self.max_date).strftime('%Y-%m-%d')
                except:
                    raise ValueError("Incorrect date format for max_date. Wrong float or int")

    def to_dict_widget(self):
        date_dict = Widget.to_dict_widget(self)

        if self.title is not None:
            if isinstance(self.title, str):
                date_dict[AttributeNames.PROPERTIES.value].update({
                    AttributeNames.TITLE.value: self.title
                })

        if self.start_date_time is not None:
            if isinstance(self.start_date_time, str):
                result = self._validate_datetime(self.start_date_time)

                date_dict[AttributeNames.PROPERTIES.value].update({
                    AttributeNames.START_DATE.value: result
                })

            elif isinstance(self.start_date_time, datetime.datetime):
                if (self.start_date_time.tzinfo is not None and self.start_date_time.tzinfo.utcoffset(
                        self.start_date_time) is not None):
                    result = self.start_date_time.strftime("%Y-%m-%d %H:%M:%S.%f %z")
                    self._format = 'YYYY-MM-DD HH:mm:ss TZ'

                else:
                    result = self.date_time.strftime("%Y-%m-%d %H:%M:%S")
                    self._format = 'YYYY-MM-DD HH:mm:ss'

                if result is not None:
                    date_dict[AttributeNames.PROPERTIES.value].update({
                        AttributeNames.START_DATE.value: result
                    })

            elif isinstance(self.start_date_time, datetime.date):
                result = self.start_date_time.strftime("%Y-%m-%d")
                self._format = 'YYYY-MM-DD'

                if result is not None:
                    date_dict[AttributeNames.PROPERTIES.value].update({
                        AttributeNames.START_DATE.value: result
                    })

            elif isinstance(self.start_date_time, datetime.time):
                if (self.start_date_time.tzinfo is not None and self.start_date_time.tzinfo.utcoffset(
                        None) is not None):
                    result = self.start_date_time.strftime("%H:%M:%S.%f %z")
                    self._format = 'HH:mm:ss TZ'
                else:
                    result = self.start_date_time.strftime("%H:%M:%S")
                    self._format = 'HH:mm:ss'

                if result is not None:
                    date_dict[AttributeNames.PROPERTIES.value].update({
                        AttributeNames.START_DATE.value: result
                    })

            elif isinstance(self.start_date_time, float) or isinstance(self.start_date_time, int):
                result = self._check_datetime_float(self.start_date_time)
                if result is not None:
                    date_dict[AttributeNames.PROPERTIES.value].update({
                        AttributeNames.START_DATE.value: result
                    })

        if self.end_date_time is not None:
            if isinstance(self.end_date_time, str):
                result = self._validate_datetime(self.end_date_time)

                date_dict[AttributeNames.PROPERTIES.value].update({
                    AttributeNames.END_DATE.value: result
                })

            elif isinstance(self.end_date_time, datetime.datetime):
                if (self.end_date_time.tzinfo is not None and self.end_date_time.tzinfo.utcoffset(
                        self.end_date_time) is not None):
                    result = self.end_date_time.strftime("%Y-%m-%d %H:%M:%S.%f %z")
                    self._format = 'YYYY-MM-DD HH:mm:ss TZ'

                else:
                    result = self.date_time.strftime("%Y-%m-%d %H:%M:%S")
                    self._format = 'YYYY-MM-DD HH:mm:ss'

                if result is not None:
                    date_dict[AttributeNames.PROPERTIES.value].update({
                        AttributeNames.END_DATE.value: result
                    })

            elif isinstance(self.end_date_time, datetime.date):
                result = self.end_date_time.strftime("%Y-%m-%d")
                self._format = 'YYYY-MM-DD'

                if result is not None:
                    date_dict[AttributeNames.PROPERTIES.value].update({
                        AttributeNames.END_DATE.value: result
                    })

            elif isinstance(self.end_date_time, datetime.time):
                if (self.end_date_time.tzinfo is not None and self.end_date_time.tzinfo.utcoffset(None) is not None):
                    result = self.end_date_time.strftime("%H:%M:%S.%f %z")
                    self._format = 'HH:mm:ss TZ'
                else:
                    result = self.end_date_time.strftime("%H:%M:%S")
                    self._format = 'HH:mm:ss'

                if result is not None:
                    date_dict[AttributeNames.PROPERTIES.value].update({
                        AttributeNames.END_DATE.value: result
                    })

            elif isinstance(self.end_date_time, float) or isinstance(self.end_date_time, int):
                result = self._check_datetime_float(self.end_date_time)
                if result is not None:
                    date_dict[AttributeNames.PROPERTIES.value].update({
                        AttributeNames.END_DATE.value: result
                    })

        if self._format is not None:
            date_dict[AttributeNames.PROPERTIES.value].update({
                AttributeNames.FORMAT.value: self._format
            })

        if self.min_date is not None:

            if isinstance(self.min_date, datetime.date):
                result = self.min_date.isoformat()
            elif isinstance(self.min_date, str):
                result = self._validate_date(self.min_date)
            elif isinstance(self.min_date, float) or isinstance(self.min_date, int):
                try:
                    result = datetime.datetime.fromtimestamp(self.min_date).strftime('%Y-%m-%d')
                except:
                    result = None
            else:
                result = None

            if result is not None:
                date_dict[AttributeNames.PROPERTIES.value].update({
                    AttributeNames.MIN_DATE.value: result
                })

        if self.max_date is not None:

            if isinstance(self.max_date, datetime.date):
                result = self.max_date.isoformat()
            elif isinstance(self.max_date, str):
                result = self._validate_date(self.max_date)
            elif isinstance(self.max_date, float) or isinstance(self.max_date, int):
                try:
                    result = datetime.datetime.fromtimestamp(self.max_date).strftime('%Y-%m-%d')
                except:
                    result = None
            else:
                result = None

            if result is not None:
                date_dict[AttributeNames.PROPERTIES.value].update({
                    AttributeNames.MAX_DATE.value: result
                })

        return date_dict
