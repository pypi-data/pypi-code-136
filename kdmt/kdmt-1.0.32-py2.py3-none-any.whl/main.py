import dateparser

for date_str in dateparser.find_dates('mardi 9 juin 2020 01 h 27 pecqueur,', source=True):
    print(date_str)

