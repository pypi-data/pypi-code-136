from svgdiagram.elements.svg import Svg
from svgdiagram.elements.group import Group
from svgdiagram.elements.text import Text
from svgdiagram.elements.path import Path
from svgdiagram.elements.rect import Rect
from datetime import datetime, timedelta, date
from svgdiagram.derived_elements.milestone import Milestone as UIMilestone
from svgdiagram.derived_elements.task import Task as UITask
from svgdiagram.derived_elements.multi_line_rect import MultiLineRect, TextLine

from .gantt_content import GanttContent

from svgdiagram.shapes.diamond_shape import DiamondShape
from svgdiagram.shapes.connection import Connection, ShapeConnectType
from svgdiagram.elements.marker import MarkerArrow


DEFAULT_STYLING = {
    "CALENDAR": {
        "STYLE": "DAY",  # DAY, WEEK, MONTH, AUTO
        "DAY_WIDTH": 50.0,
        "DAY_FONT": {
            "SIZE": 16.0
        },
        "DAY_COLUMN_COLOR": "#bbbbbb",
        "DAY_COLUMN_COLOR_ODD": "#dddddd",
    }
}
DEFAULT_OPTIONS = {
    "DATE_DEFAULT_TIME": "T12:00:00"
}


class Gantt(Svg):
    def __init__(self, content, style=None, options=None):
        super().__init__()

        self.content = GanttContent.parse_obj(content)
        self.style = style if style else DEFAULT_STYLING
        self.options = options if options else DEFAULT_OPTIONS

        self.group_calendar_tiles = Group()
        self.append_child(self.group_calendar_tiles)
        self.group_calendar_text = Group()
        self.append_child(self.group_calendar_text)

        self.group_swimlanes = Group()
        self.append_child(self.group_swimlanes)

        self.group_dependencies = Group()
        self.append_child(self.group_dependencies)

        self.id_shape_map = {}

    @property
    def start_date(self):
        if not self.content.start_date:
            min_date = min(self.content.iter_all_swimlane_dates())
            if isinstance(min_date, datetime):
                min_date = min_date.date()
            self.content.start_date = min_date
        return self.content.start_date

    @property
    def end_date(self):
        if not self.content.end_date:
            max_date = max(self.content.iter_all_swimlane_dates())
            if isinstance(max_date, datetime):
                max_date = max_date.date()
            self.content.end_date = max_date
        return self.content.end_date

    def date_to_column_index(self, date_value):
        """Gives the correct column index based on a date"""

        if isinstance(date_value, datetime):
            date_value = date_value.date()

        assert isinstance(date_value, date), \
            f'"{date_value}" is not a datetime.date!'

        return (date_value - self.start_date).days

    def date_to_column_fraction(self, datetime_value):
        """Gives the correct column index and the fraction within it based on a datetime."""

        if type(datetime_value) == date:
            datetimestr = datetime_value.isoformat() \
                + self.options["DATE_DEFAULT_TIME"]
            datetime_value = datetime.fromisoformat(datetimestr)

        assert isinstance(datetime_value, datetime), \
            f'"{datetime_value}" is not a datetime.datetime!'

        index = self.date_to_column_index(datetime_value)

        seconds_of_day = datetime_value.second \
            + datetime_value.minute * 60 \
            + datetime_value.hour * 3600
        fraction = seconds_of_day / float(24 * 3600)

        return index, fraction

    def date_to_column_x_pos(self, datetime_value):
        DAY_WIDTH = self.style["CALENDAR"]["DAY_WIDTH"]
        index, fraction = self.date_to_column_fraction(datetime_value)
        return (index + fraction) * DAY_WIDTH

    def _layout(self, x_con_min, x_con_max, y_con_min, y_con_max):
        calendar_x_left, calendar_x_right = self._build_calendar_text()
        swimlane_y_max = self._build_swimlanes(
            calendar_x_left, calendar_x_right)
        self._build_calender_tiles(swimlane_y_max)

        for dep in self.content.dependencies:
            connection = Connection(
                start_point=self.id_shape_map[dep.source_id],
                end_point=self.id_shape_map[dep.target_id],
                start_shape_connect_type=ShapeConnectType.CLOSEST,
                end_shape_connect_type=ShapeConnectType.CLOSEST,
                normal_len=15,
            )

            path = Path(connection.calculate_points(),
                        corner_radius=10, marker_end=MarkerArrow())
            self.group_dependencies.append_child(path)

        super()._layout(x_con_min, x_con_max, y_con_min, y_con_max)

    def _build_calendar_text(self):
        assert self.start_date <= self.end_date, \
            f'Enddate "{self.end_date}" is before startdate "{self.start_date}"!'

        DAY_WIDTH = self.style["CALENDAR"]["DAY_WIDTH"]
        DAY_FONT_SIZE = self.style["CALENDAR"]["DAY_FONT"]["SIZE"]
        DAY_COLUMN_COLOR = self.style["CALENDAR"]["DAY_COLUMN_COLOR"]
        DAY_COLUMN_COLOR_ODD = self.style["CALENDAR"]["DAY_COLUMN_COLOR_ODD"]

        c_date = self.start_date
        while c_date <= self.end_date:
            year, week, weekday = c_date.isocalendar()

            index, fraction = self.date_to_column_fraction(c_date)

            day_x = (index + fraction) * DAY_WIDTH
            day_y = 0

            day_color = DAY_COLUMN_COLOR if (
                index % 2) == 0 else DAY_COLUMN_COLOR_ODD

            self.group_calendar_tiles.append_child(Rect.midpoint_round_rect(
                mid_x=day_x,
                mid_y=day_y,
                width=DAY_WIDTH,
                height=DAY_FONT_SIZE,
                radius=0,
                stroke=day_color,
                stroke_width_px=0.1,
                fill=day_color,
            ))
            self.group_calendar_text.append_child(
                Text(day_x, day_y, c_date.strftime(r'%d')))

            if weekday == 1:
                self.group_calendar_text.append_child(
                    Text(index * DAY_WIDTH, -DAY_FONT_SIZE,
                         f"CW {week}", horizontal_alignment="left")
                )

            if c_date.day == 1:
                self.group_calendar_text.append_child(
                    Text(index * DAY_WIDTH, -DAY_FONT_SIZE*2,
                         c_date.strftime('%B').upper(), horizontal_alignment="left")
                )

            # iter
            c_date += timedelta(days=1)

        calendar_x_left = self.date_to_column_index(
            self.start_date) * DAY_WIDTH
        calendar_x_right = (self.date_to_column_index(
            self.end_date) + 1) * DAY_WIDTH
        return calendar_x_left, calendar_x_right

    def _build_swimlanes(self, calendar_x_left, calendar_x_right):
        for index, swimlane in enumerate(self.content.swimlanes):
            swimlane_y = 40+80*index
            self.group_swimlanes.append_child(
                Text(-8, swimlane_y, swimlane.name,
                     horizontal_alignment="right")
            )

            self.group_swimlanes.append_child(Path(
                points=[(calendar_x_left, swimlane_y),
                        (calendar_x_right, swimlane_y)]
            ))

            for task in swimlane.tasks:
                self.group_swimlanes.append_child(UITask(
                    x_start=self.date_to_column_x_pos(task.start_date),
                    x_end=self.date_to_column_x_pos(task.end_date),
                    y=swimlane_y,
                    height=20,
                    radius=5,
                    text=task.name,
                    progess=task.progress,
                ))

            for milestone in swimlane.milestones:
                milestone_x = self.date_to_column_x_pos(milestone.due_date)
                milestone_element = UIMilestone(
                    milestone_x,
                    swimlane_y,
                )
                if milestone.id:
                    self.id_shape_map[milestone.id] = DiamondShape(
                        milestone_element)

                self.group_swimlanes.append_child(
                    milestone_element
                )
                text_lines = list(map(lambda x: TextLine(
                    x, font_size=10), milestone.name.split('\n')))
                text_with = 100
                self.group_swimlanes.append_child(
                    MultiLineRect(
                        milestone_x-text_with/2.0,
                        swimlane_y+15,
                        text_with,
                        text_lines=text_lines,
                        fill="transparent",
                        stroke="transparent"
                    )
                    # Text(milestone_x, swimlane_y+30, milestone.name)
                )

        swimlane_y_max = 100+80*index
        return swimlane_y_max

    def _build_calender_tiles(self, swimlane_y_max):
        DAY_WIDTH = self.style["CALENDAR"]["DAY_WIDTH"]
        DAY_FONT_SIZE = self.style["CALENDAR"]["DAY_FONT"]["SIZE"]
        DAY_COLUMN_COLOR = self.style["CALENDAR"]["DAY_COLUMN_COLOR"]
        DAY_COLUMN_COLOR_ODD = self.style["CALENDAR"]["DAY_COLUMN_COLOR_ODD"]

        c_date = self.start_date
        while c_date <= self.end_date:
            year, week, weekday = c_date.isocalendar()

            index, fraction = self.date_to_column_fraction(c_date)

            day_x = index * DAY_WIDTH
            day_y = 0

            day_color = DAY_COLUMN_COLOR if (
                index % 2) == 0 else DAY_COLUMN_COLOR_ODD

            if weekday > 5:
                day_color = '#ffeb3b'

            self.group_calendar_tiles.append_child(Rect(
                x=day_x,
                y=day_y - DAY_FONT_SIZE/2.0,
                width=DAY_WIDTH,
                height=swimlane_y_max - (day_y - DAY_FONT_SIZE/2.0),
                rx=0, ry=0,
                stroke=day_color,
                stroke_width_px=0.1,
                fill=day_color,
            ))

            # iter
            c_date += timedelta(days=1)
