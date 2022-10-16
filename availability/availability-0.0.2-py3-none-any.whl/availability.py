import datetime
import logging
from copy import deepcopy
from typing import Optional

logger = logging.getLogger(__name__)


class AvailabilityRange:
    def __init__(self, start_time: datetime.datetime, end_time: datetime.datetime):
        self.start_time = start_time
        self.end_time = end_time

        if not start_time.tzinfo:
            raise Exception("start_time is missing timezone information")
        if not end_time.tzinfo:
            raise Exception("end_time is missing timezone information")

    def __str__(self) -> str:
        if (
            self.start_time.date() == self.end_time.date()
            and self.start_time.tzinfo == self.end_time.tzinfo
        ):
            return f"{self.start_time.date()}({self.start_time.tzinfo.key}): {self.start_time.time()}-{self.end_time.time()}"
        return f"{self.start_time} - {self.end_time}"

    def __repr__(self) -> str:
        return f"AvailabilityRange({self.start_time.__repr__()}, {self.end_time.__repr__()} )"

    def __eq__(self, y: "AvailabilityRange") -> bool:
        if self.start_time == y.start_time and self.end_time == y.end_time:
            return True
        return False

    def update(
        self,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
    ) -> None:
        if start_time:
            self.start_time = start_time
        if end_time:
            self.end_time = end_time


class Availability:
    def __init__(
        self,
        ranges: list[AvailabilityRange] = [],
        padding_time_before: int = 0,
        padding_time_after: int = 0,
    ):
        self.padding_time_before = padding_time_before
        self.padding_time_after = padding_time_after

        if not ranges:
            self.ranges = []
        else:
            self.ranges = ranges
        self.sort()

    def __bool__(self) -> bool:
        return bool(self.ranges)

    def __getitem__(self, items) -> AvailabilityRange:
        return self.ranges[items]

    def extend(self, other, **kwargs):
        return self.ranges.extend(other.ranges, **kwargs)

    def pop(self) -> AvailabilityRange:
        return self.ranges.pop()

    def sort(self):
        self.ranges.sort(key=lambda x: x.start_time)

    def __add__(self, other: "Availability") -> "Availability":
        """Add 2 Availability sets together to show the Availability of both of them combined"""
        new_availability = Availability(
            padding_time_before=self.padding_time_before,
            padding_time_after=self.padding_time_after,
        )

        concatinated = self.ranges + other.ranges
        concatinated.sort(key=lambda x: x.start_time)

        if not concatinated:
            return new_availability

        # compare sorted list of availability ranges and add them together
        ar = concatinated.pop(0)
        for other_ar in concatinated:
            if ar.end_time >= other_ar.start_time:
                if ar.end_time < other_ar.end_time:
                    ar.end_time = other_ar.end_time
            else:
                new_availability.append(ar)
                ar = other_ar
        else:
            new_availability.append(ar)

        return new_availability

    def __sub__(self, other: "Availability") -> "Availability":
        new_availability = Availability(
            padding_time_before=self.padding_time_before,
            padding_time_after=self.padding_time_after,
        )

        ranges = deepcopy(self.ranges)
        for time_range in ranges:
            for other_ar in other.ranges:
                if other_ar.start_time <= time_range.start_time <= other_ar.end_time:
                    time_range.start_time = other_ar.end_time + datetime.timedelta(
                        minutes=other.padding_time_after
                    )

                # the end time is in the window
                if other_ar.start_time <= time_range.end_time <= other_ar.end_time:
                    time_range.end_time = other_ar.start_time - datetime.timedelta(
                        minutes=other.padding_time_before
                    )

                # if the other_ar starts after the window start and before the window ends
                if time_range.start_time <= other_ar.start_time <= time_range.end_time:
                    if (
                        time_range.start_time
                        <= other_ar.end_time
                        <= time_range.end_time
                    ):
                        # split the window up.
                        logger.debug(
                            f"splitting the window {time_range.start_time} - {time_range.end_time} for {other_ar.start_time} - {other_ar.end_time}"
                            f"\n\t into {time_range.start_time} - {other_ar.start_time - datetime.timedelta(minutes=other.padding_time_before)} and {other_ar.end_time + datetime.timedelta(minutes=other.padding_time_after)} - {time_range.end_time}"
                        )

                        ranges.append(
                            AvailabilityRange(
                                other_ar.end_time
                                + datetime.timedelta(minutes=other.padding_time_after),
                                time_range.end_time,
                            )
                        )

                        time_range.end_time = other_ar.start_time - datetime.timedelta(
                            minutes=other.padding_time_before
                        )

            if time_range.end_time <= time_range.start_time:
                continue

            new_availability.append(
                AvailabilityRange(
                    time_range.start_time,
                    time_range.end_time,
                )
            )

        return new_availability

    def __str__(self) -> str:
        return (
            f"***Availability***{self.padding_time_before}, {self.padding_time_after}: \n\t"
            + "\n\t".join([str(x) for x in self.ranges])
        )

    def __repr__(self) -> str:
        return f"Availability({self.ranges}, padding_time_before={self.padding_time_before}, padding_time_after={self.padding_time_after})"

    def __eq__(self, other: "Availability") -> bool:
        """check to see if 2 Availability sets are equal"""
        if not isinstance(other, Availability):
            return False

        a1 = deepcopy(other.ranges)
        for ar in self.ranges:
            if ar not in a1:
                return False
            a1.remove(ar)
        if a1:
            return False

        if self.padding_time_before != other.padding_time_before:
            return False

        if self.padding_time_after != other.padding_time_after:
            return False

        return True

    def append(self, ar: AvailabilityRange) -> None:
        self.ranges.append(ar)
        self.sort()
