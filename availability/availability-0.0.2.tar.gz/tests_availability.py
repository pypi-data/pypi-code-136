import datetime
from unittest.mock import Mock, patch
from zoneinfo import ZoneInfo

from django.test import TestCase

from .availability import Availability, AvailabilityRange

tz_name = "America/Chicago"
tz = ZoneInfo(tz_name)

secondary_tz_name = "America/Denver"
secondary_tz = ZoneInfo(secondary_tz_name)


def short_dt(
    hour=8, minute=0, year=2021, month=5, day=10, tzinfo=ZoneInfo(key="America/Chicago")
):
    return datetime.datetime(year, month, day, hour, minute, tzinfo=tzinfo)


class AvailabilityTests(TestCase):
    maxDiff = None

    def test_create_ranges(self):
        availability = Availability()
        availability.append(
            AvailabilityRange(
                start_time=datetime.datetime(
                    2021, 5, 10, 8, 0, tzinfo=ZoneInfo(key="America/Chicago")
                ),
                end_time=datetime.datetime(
                    2021, 5, 10, 10, 0, tzinfo=ZoneInfo(key="America/Chicago")
                ),
            )
        )
        availability.append(
            AvailabilityRange(
                start_time=datetime.datetime(
                    2021, 5, 10, 12, 0, tzinfo=ZoneInfo(key="America/Chicago")
                ),
                end_time=datetime.datetime(
                    2021, 5, 10, 14, 0, tzinfo=ZoneInfo(key="America/Chicago")
                ),
            )
        )

    def test_create_range(self):
        ar = AvailabilityRange(
            start_time=datetime.datetime(
                2021, 5, 10, 8, 0, tzinfo=ZoneInfo(key="America/Chicago")
            ),
            end_time=datetime.datetime(
                2021, 5, 10, 10, 0, tzinfo=ZoneInfo(key="America/Chicago")
            ),
        )

    def test_add_availabilities(self):
        availability = Availability(
            [
                AvailabilityRange(
                    short_dt(8),
                    short_dt(10),
                ),
                AvailabilityRange(
                    short_dt(12),
                    short_dt(14),
                ),
            ]
        )
        availability2 = Availability(
            [
                AvailabilityRange(
                    short_dt(10),
                    short_dt(12),
                ),
                AvailabilityRange(
                    short_dt(14),
                    short_dt(16),
                ),
            ]
        )

        availability3 = availability + availability2

        self.assertEqual(
            availability3,
            Availability(
                [
                    AvailabilityRange(
                        datetime.datetime(
                            2021, 5, 10, 8, 0, tzinfo=ZoneInfo(key="America/Chicago")
                        ),
                        datetime.datetime(
                            2021, 5, 10, 16, 0, tzinfo=ZoneInfo(key="America/Chicago")
                        ),
                    ),
                ]
            ),
        )

    def test_add_disjoint_availabilities(self):
        availability = Availability(
            [
                AvailabilityRange(
                    short_dt(8),
                    short_dt(10),
                ),
                AvailabilityRange(
                    short_dt(12),
                    short_dt(14),
                ),
            ]
        )
        availability2 = Availability(
            [
                AvailabilityRange(
                    short_dt(11),
                    short_dt(12),
                ),
                AvailabilityRange(
                    short_dt(14, 30),
                    short_dt(16),
                ),
            ]
        )

        availability3 = availability + availability2

        self.assertEqual(
            availability3,
            Availability(
                [
                    AvailabilityRange(
                        short_dt(8),
                        short_dt(10),
                    ),
                    AvailabilityRange(
                        short_dt(11),
                        short_dt(14),
                    ),
                    AvailabilityRange(
                        short_dt(14, 30),
                        short_dt(16),
                    ),
                ]
            ),
        )

    def test_add_overlapping_availabilities(self):
        availability = Availability(
            [
                AvailabilityRange(
                    short_dt(8),
                    short_dt(10),
                ),
                AvailabilityRange(
                    short_dt(12),
                    short_dt(14),
                ),
            ]
        )
        availability2 = Availability(
            [
                AvailabilityRange(
                    short_dt(8, 30),
                    short_dt(11),
                ),
                AvailabilityRange(
                    short_dt(11, 45),
                    short_dt(13),
                ),
            ]
        )

        availability3 = availability + availability2

        self.assertEqual(
            availability3,
            Availability(
                [
                    AvailabilityRange(
                        short_dt(8),
                        short_dt(11),
                    ),
                    AvailabilityRange(
                        short_dt(11, 45),
                        short_dt(14),
                    ),
                ]
            ),
        )

    def test_subtract_availabilities(self):
        availability = Availability(
            [
                AvailabilityRange(
                    short_dt(8),
                    short_dt(10),
                ),
            ]
        )
        availability2 = Availability(
            [
                AvailabilityRange(
                    short_dt(9),
                    short_dt(10),
                ),
            ]
        )

        availability3 = availability - availability2

        self.assertEqual(
            availability3,
            Availability(
                [
                    AvailabilityRange(
                        short_dt(8),
                        short_dt(9),
                    ),
                ]
            ),
        )

    def test_subtract_availabilities_causing_split(self):
        availability = Availability(
            [
                AvailabilityRange(
                    short_dt(8),
                    short_dt(10),
                ),
            ]
        )
        availability2 = Availability(
            [
                AvailabilityRange(
                    short_dt(9),
                    short_dt(9, 45),
                ),
            ]
        )

        availability3 = availability - availability2

        self.assertEqual(
            availability3,
            Availability(
                [
                    AvailabilityRange(
                        short_dt(8),
                        short_dt(9),
                    ),
                    AvailabilityRange(
                        short_dt(9, 45),
                        short_dt(10),
                    ),
                ]
            ),
        )

    def test_availabilities_equal(self):
        availability = Availability(
            [
                AvailabilityRange(
                    start_time=datetime.datetime(
                        2021, 5, 10, 8, 0, tzinfo=ZoneInfo(key="America/Chicago")
                    ),
                    end_time=datetime.datetime(
                        2021, 5, 10, 10, 0, tzinfo=ZoneInfo(key="America/Chicago")
                    ),
                ),
            ]
        )

        self.assertEqual(
            availability,
            Availability(
                [
                    AvailabilityRange(
                        datetime.datetime(
                            2021, 5, 10, 8, 0, tzinfo=ZoneInfo(key="America/Chicago")
                        ),
                        datetime.datetime(
                            2021, 5, 10, 10, 0, tzinfo=ZoneInfo(key="America/Chicago")
                        ),
                    ),
                ]
            ),
        )

        # test two not equal
        self.assertNotEqual(
            availability,
            Availability(
                [
                    AvailabilityRange(
                        datetime.datetime(
                            2021, 5, 10, 8, 0, tzinfo=ZoneInfo(key="America/Chicago")
                        ),
                        datetime.datetime(
                            2021, 5, 10, 15, 0, tzinfo=ZoneInfo(key="America/Chicago")
                        ),
                    ),
                ]
            ),
        )

        # test two equal with different time zones
        self.assertEqual(
            availability,
            Availability(
                [
                    AvailabilityRange(
                        datetime.datetime(
                            2021, 5, 10, 7, tzinfo=ZoneInfo(key="America/Denver")
                        ),
                        datetime.datetime(
                            2021, 5, 10, 11, tzinfo=ZoneInfo(key="America/Detroit")
                        ),
                    ),
                ]
            ),
        )

    def test_subtract_availabilities_with_padding(self):
        availability = Availability(
            [
                AvailabilityRange(
                    short_dt(8),
                    short_dt(10),
                ),
            ],
            padding_time_before=0,  # these shouldn't matter or should they??
            padding_time_after=0,
        )
        availability2 = Availability(
            [
                AvailabilityRange(
                    short_dt(9),
                    short_dt(10),
                ),
            ],
            padding_time_before=15,
            padding_time_after=15,
        )

        availability3 = availability - availability2

        self.assertEqual(
            availability3,
            Availability(
                [
                    AvailabilityRange(
                        short_dt(8),
                        short_dt(8, 45),
                    ),
                ],
                padding_time_before=0,  # these shouldn't matter or should they??
                padding_time_after=0,
            ),
        )
