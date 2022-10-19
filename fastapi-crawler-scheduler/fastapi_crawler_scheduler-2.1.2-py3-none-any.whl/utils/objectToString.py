import datetime


def handle_datetime(agefield):
    if agefield is None:
        agefield = None
    else:
        if isinstance(agefield, datetime.datetime):
            agefield = agefield.strftime("%Y-%m-%d %H:%M:%S")
        else:
            agefield = '解析失败'
    return agefield


def handle_every_trigger(trigger):
    # print(f"handle_before： {trigger}")
    if 'timezone' in trigger:
        timezone = trigger.get('timezone')
        if timezone is None:
            timezone = None
        else:
            timezone = timezone.__str__()
        trigger['timezone'] = timezone
    if 'start_date' in trigger:
        trigger['start_date'] = handle_datetime(agefield=trigger.get('start_date'))
    if 'end_date' in trigger:
        trigger['end_date'] = handle_datetime(agefield=trigger.get('end_date'))
    if 'interval' in trigger:
        interval = trigger.get('interval')
        if interval is None:
            interval = None
        else:
            interval = interval.total_seconds()
        trigger['interval'] = interval
    # print(f"handle_after： {trigger}")
    return trigger


def handle_trigger(trigger):
    if isinstance(trigger, list):
        temp = []
        for every_trigger in trigger:
            temp.append(handle_every_trigger(every_trigger))
        return temp
    else:
        return handle_every_trigger(trigger)
