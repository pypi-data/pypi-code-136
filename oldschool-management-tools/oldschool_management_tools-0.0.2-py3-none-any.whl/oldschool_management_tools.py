from datetime import datetime, timedelta, date, time
from win32com import client
import pywintypes

# Ideas:
#  - See allocated time per day
#  - Plan in breaks
#  - Draw schedule in hours

# Do the work where it is fast :)

CATEGORIES_REQUIRING_PREP = ["Green category"]


def get_calendar(begin, end) -> client.CDispatch:
    outlook = client.Dispatch('Outlook.Application').GetNamespace('MAPI')
    calendar = outlook.getDefaultFolder(9).Items
    calendar.IncludeRecurrences = True
    calendar.Sort('[Start]')

    restriction = "[Start] >= '" + begin.strftime('%m/%d/%Y') + "' AND [END] <= '" + end.strftime('%m/%d/%Y') + "'"
    calendar = calendar.Restrict(restriction)
    return calendar


def nice_time_str(time_in_zone) -> str:
    return str(time_in_zone.time())[0:-3]


def get_day_cal(date: datetime):
    return get_calendar(date, date + timedelta(days=1))


def print_cal(cal):
    for apt in cal:
        start_time = nice_time_str(apt.StartInStartTimeZone)
        end_time = nice_time_str(apt.EndInEndTimeZone)
        location = apt.Location
        print(f"{start_time} to {end_time} - {apt.Subject} - {location}")


def start_of_day(day: date) -> datetime:
    return datetime.combine(day, time())


def parse_day(day) -> datetime:
    match day:
        case "today":
            return start_of_day(date.today())
        case "tomorrow":
            return start_of_day(date.today()) + timedelta(days=1)
        case d if day.isnumeric():
            return start_of_day(date.today()) + timedelta(days=int(d))
        case _:
            raise ValueError(f"Bad day [{day}]")


def show_day_sched(parsed_day=datetime.today()):
    cal = get_day_cal(parsed_day)
    print_cal(cal)


def prompt_day_tasks(parsed_day=datetime.today()):
    cal = get_day_cal(parsed_day)
    for apt in cal:
        if apt.Categories in CATEGORIES_REQUIRING_PREP:
            done = input(f"Prep for {apt.Subject} => Done?")


def main():
    die = False
    while not die:
        print("What do you want?  I'm busy")
        response = input("well?  ")
        match response.split():
            case ["prompt", "tasks", day]:
                parsed_day = parse_day(day)
                prompt_day_tasks(parsed_day)
            case ["show", "sched"]:
                show_day_sched()
            case ["show", "sched", day]:
                parsed_day = parse_day(day)
                show_day_sched(parsed_day)
            case ["plan", day]:
                print("Meh")
            case ["die"]:
                die = True
            case _:
                print(f"Bad command [{response}]")


if __name__ == '__main__':
    main()
