import dateparser

for date_str in dateparser.find_dates('samedi 1 août 2020 02 h 01', source=True):
    print(date_str)

