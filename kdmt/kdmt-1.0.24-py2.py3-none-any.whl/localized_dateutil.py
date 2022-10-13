import calendar
from dateutil import parser
import locale

class LocaleParserInfo(parser.parserinfo):
    locale_list=[ 'de_DE.UTF-8', 'nl_BE', 'es_ES', 'fr_FR', 'it_IT', 'pt_PT']
    locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')
    WEEKDAYS=list(zip(calendar.day_abbr, calendar.day_name))
    for l in locale_list:
        locale.setlocale(locale.LC_TIME, l)
        WD = list(zip(calendar.day_abbr, calendar.day_name))
        for i, d in enumerate(WD):
            WEEKDAYS[i]+=d

    MONTHS = list(zip(calendar.month_abbr, calendar.month_name))[1:]
    for l in locale_list:
        locale.setlocale(locale.LC_TIME, l)
        MT = list(zip(calendar.month_abbr, calendar.month_name))[1:]
        for i, m in enumerate(MT):
            MONTHS[i]+=m
    MONTHS=[tuple(set(M)) for M in MONTHS]
    WEEKDAYS=[tuple(set(WD)) for WD in WEEKDAYS]

if __name__=="__main__":

    from dateutil.parser import parse

    print(parse("lundi 28 septembre 2020 12:59", parserinfo=LocaleParserInfo()))
