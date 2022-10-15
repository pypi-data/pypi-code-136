import dateparser

for date_str in dateparser.find_dates('Mon, 13 Jul 2020 at 12:45, Sofie de Volder,', source=True):
    print(date_str)

