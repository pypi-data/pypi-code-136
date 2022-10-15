import dateparser

for date_str in dateparser.find_dates('sam. 1 août 2020 à 09:34, Julien Rosin <julien.rosin4121@gmail.com<mailto:julien.rosin4121@gmail.com>>', source=True):
    print(date_str)

