import time, datetime
from python_helper import EnvironmentHelper, SettingHelper, ObjectHelper, log, Test, DateTimeHelper

# LOG_HELPER_SETTINGS = {
#     log.LOG : True,
#     log.SUCCESS : True,
#     log.SETTING : True,
#     log.DEBUG : True,
#     log.WARNING : True,
#     log.WRAPPER : True,
#     log.FAILURE : True,
#     log.ERROR : True,
    # log.TEST : False
# }

LOG_HELPER_SETTINGS = {
    log.LOG : False,
    log.SUCCESS : False,
    log.SETTING : False,
    log.DEBUG : False,
    log.WARNING : False,
    log.WRAPPER : False,
    log.FAILURE : False,
    log.ERROR : False,
    log.TEST : False
}

TEST_SETTINGS = {}

@Test()
def timeDelta() :
    # arrange
    # act
    # assert
    assert datetime.timedelta(days=2, hours=3, minutes=4, seconds=5, milliseconds=6, microseconds=7) == DateTimeHelper.timeDelta(days=2, hours=3, minutes=4, seconds=5, milliseconds=6, microseconds=7)
    assert datetime.timedelta(days=0, hours=3, minutes=4, seconds=5, milliseconds=6, microseconds=7) == DateTimeHelper.timeDelta(days=0, hours=3, minutes=4, seconds=5, milliseconds=6, microseconds=7)

# @Test()
# def dateTime_utcnow() :
#     # arrange
#     givenSimpleDateTime = time.time()
#     givenDateTime = date=datetime.datetime.utcnow()
#     givenDate = date=datetime.datetime.utcnow().date()
#     givenTime = date=datetime.datetime.utcnow().time()
#
#     # act
#     # assert
#     assert datetime.datetime.utcnow() == DateTimeHelper.dateTimeNow()
#     assert datetime.datetime.utcnow().date() == DateTimeHelper.dateOf(datetime.datetime.utcnow())
#     assert datetime.datetime.utcnow().time() == DateTimeHelper.timeOf(datetime.datetime.utcnow())
#     assert datetime.datetime.utcnow().date() == DateTimeHelper.dateNow()
#     assert datetime.datetime.utcnow().time() == DateTimeHelper.timeNow()
#     assert datetime.datetime.timestamp(datetime.datetime.utcnow()) == DateTimeHelper.timestampNow()
#     assert datetime.datetime.fromtimestamp(givenSimpleDateTime) == DateTimeHelper.ofTimestamp(givenSimpleDateTime)
#     assert datetime.datetime.utcnow() == DateTimeHelper.ofTimestamp(datetime.datetime.timestamp(DateTimeHelper.dateTimeNow()))
#
#     parsed = None
#     for pattern in DateTimeHelper.PATTERNS :
#         try :
#             parsed = datetime.datetime.strptime(str(givenDateTime), pattern)
#             break
#         except Exception as exception :
#             pass
#     assert parsed == DateTimeHelper.of(dateTime=givenDateTime)
#
#     parsed = None
#     for pattern in DateTimeHelper.PATTERNS :
#         try :
#             parsed = datetime.datetime.strptime(str(givenDate), pattern)
#             break
#         except Exception as exception :
#             pass
#     assert parsed == DateTimeHelper.of(date=givenDate)
#
#     parsed = None
#     for pattern in DateTimeHelper.PATTERNS :
#         try :
#             parsed = datetime.datetime.strptime(f'{datetime.datetime.utcnow().date()} {str(givenTime)}', pattern)
#             break
#         except Exception as exception :
#             pass
#     assert parsed == DateTimeHelper.of(time=givenTime), (parsed, DateTimeHelper.of(time=givenTime))
#
#     assert datetime.datetime.timestamp(givenDateTime) == DateTimeHelper.timestampOf(dateTime=givenDateTime), (datetime.datetime.timestamp(givenDateTime), DateTimeHelper.timestampOf(dateTime=givenDateTime))

@Test()
def dateTime_now() :
    # arrange
    givenDateTimeNow = datetime.datetime.now()
    timestampFromDatetimeNow = datetime.datetime.timestamp(datetime.datetime.now())
    givenSimpleDateTime = time.time()
    givenDateTime = datetime.datetime.now()
    givenDate = datetime.datetime.now().date()
    givenTime = datetime.datetime.now().time()
    margin = 500

    # act
    # assert
    assert (DateTimeHelper.dateTimeNow() - givenDateTimeNow).microseconds < margin, f'datetime.datetime.now() == DateTimeHelper.dateTimeNow() => {datetime.datetime.now()} == {DateTimeHelper.dateTimeNow()}'
    assert datetime.datetime.now().date() == DateTimeHelper.dateOf(datetime.datetime.now()), f'datetime.datetime.now().date() == DateTimeHelper.dateOf(datetime.datetime.now()) => {datetime.datetime.now().date()} == {DateTimeHelper.dateOf(datetime.datetime.now())}'
    assert abs(
        (
            datetime.datetime.now().time().second * 60000 + datetime.datetime.now().time().microsecond
        ) - (
            DateTimeHelper.timeNow().second * 60000 + DateTimeHelper.timeOf(datetime.datetime.now()).microsecond
        )
    ) < margin, f'datetime.datetime.now().time() == DateTimeHelper.timeOf(datetime.datetime.now()) => {datetime.datetime.now().time()} == {DateTimeHelper.timeOf(datetime.datetime.now())}'
    assert datetime.datetime.now().date() == DateTimeHelper.dateNow(), f'datetime.datetime.now().date() == DateTimeHelper.dateNow() => {datetime.datetime.now().date()} == {DateTimeHelper.dateNow()}'
    assert abs(
        (
            datetime.datetime.now().time().second * 60000 + datetime.datetime.now().time().microsecond
        ) - (
            DateTimeHelper.timeNow().second * 60000 + DateTimeHelper.timeNow().microsecond
        )
    ) < margin, f'datetime.datetime.now().time() == DateTimeHelper.timeNow() => {datetime.datetime.now().time()} == {DateTimeHelper.timeNow()}'
    assert DateTimeHelper.timestampNow() - timestampFromDatetimeNow < margin, f'datetime.datetime.timestamp(datetime.datetime.now()) == DateTimeHelper.timestampNow() => {datetime.datetime.timestamp(datetime.datetime.now())} == {DateTimeHelper.timestampNow()}'
    assert datetime.datetime.fromtimestamp(givenSimpleDateTime) == DateTimeHelper.ofTimestamp(givenSimpleDateTime), f'datetime.datetime.fromtimestamp(givenSimpleDateTime) == DateTimeHelper.ofTimestamp(givenSimpleDateTime) => {datetime.datetime.fromtimestamp(givenSimpleDateTime)} == {DateTimeHelper.ofTimestamp(givenSimpleDateTime)}'
    assert (DateTimeHelper.ofTimestamp(datetime.datetime.timestamp(DateTimeHelper.dateTimeNow())) - givenDateTimeNow).microseconds < margin, f'datetime.datetime.now() == DateTimeHelper.ofTimestamp(datetime.datetime.timestamp(DateTimeHelper.dateTimeNow())) => {datetime.datetime.now()} == {DateTimeHelper.ofTimestamp(datetime.datetime.timestamp(DateTimeHelper.dateTimeNow()))}'

    parsed = None
    for pattern in DateTimeHelper.PATTERNS :
        try :
            parsed = datetime.datetime.strptime(str(givenDateTime), pattern)
            break
        except Exception as exception :
            pass
    assert parsed == DateTimeHelper.of(dateTime=givenDateTime)

    parsed = None
    for pattern in DateTimeHelper.PATTERNS :
        try :
            parsed = datetime.datetime.strptime(str(givenDate), pattern)
            break
        except Exception as exception :
            pass
    assert parsed == DateTimeHelper.of(date=givenDate)

    parsed = None
    for pattern in DateTimeHelper.PATTERNS :
        try :
            parsed = datetime.datetime.strptime(f'{datetime.datetime.now().date()} {str(givenTime)}', pattern)
            break
        except Exception as exception :
            pass
    assert parsed == DateTimeHelper.of(time=givenTime), (parsed, DateTimeHelper.of(time=givenTime))

    assert datetime.datetime.timestamp(givenDateTime) == DateTimeHelper.timestampOf(dateTime=givenDateTime), (datetime.datetime.timestamp(givenDateTime), DateTimeHelper.timestampOf(dateTime=givenDateTime))

@Test()
def getWeekDay() :
    # arrange
    dateTimeNow = datetime.datetime.now()
    timeNow = datetime.datetime.now().time()
    dateNow = datetime.datetime.now().date()

    # act
    # assert
    assert datetime.datetime.now().weekday() == DateTimeHelper.getWeekDay()
    assert datetime.datetime.now().weekday() == DateTimeHelper.getWeekDay(dateTime=dateTimeNow)
    assert datetime.datetime.now().weekday() == DateTimeHelper.getWeekDay(date=dateNow, time=timeNow)
    assert datetime.datetime.now().weekday() == DateTimeHelper.getWeekDay(date=dateNow)
