from datetime import datetime
from random import random, randint


def date(start: str, end: str, n=None) -> list[str] | str:
    """
        Generate a random date between `start` and `end` dates.

        :param str start: start date in the format YYYY-MM-DD.
        :param str end: end date in the format YYYY-MM-DD.
        :param int n: number of random dates to generate.

        :return: A random date between start and end dates.
        :rtype: list[str] | str

        :Example:
            >>> random_date('2022-01-01', '2022-12-31')
            >>> random_date('2022-01-01', '2022-12-31', 2)
    """
    if n is not None:
        date_list = []
        for i in range(n):
            start_list = datetime.strptime(start, '%Y-%m-%d')
            end_list = datetime.strptime(end, '%Y-%m-%d')
            random_date = start_list + (end_list - start_list) * random()
            date_list.append(random_date.strftime('%Y-%m-%d'))
            date_list.sort()
        return f'de {date_list[0]} ate {date_list[-1]}'
    else:
        start = datetime.strptime(start, '%Y-%m-%d')
        end = datetime.strptime(end, '%Y-%m-%d')
        random_date = start + (end - start) * random()
        return random_date.strftime('%Y-%m-%d')


def last_date(n=None) -> str:
    """
        It is a function to generate a random last n days.

        :param int n: number of random dates to generate.
        :return: A random checkbox between the present checkboxes.
        :rtype: str

        :Example:
            >>> random_last_date()
            >>> random_last_date(60)

    """
    if n is not None:
        random_choice = randint(1, n)
    else:
        random_choice = randint(1, 180)
    return f'u{random_choice}d'


def month():
    """
        It is a function to generate a random month.

        :return: A random month between the present months.
        :rtype: str

        :Example:
            >>> random_month()

    """
    today = datetime.today()
    month_id = randint(0, today.month)
    month = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
             'Novembro', 'Dezembro']
    return f'em {month[month_id - 1]}'


def year(start=None) -> str:
    """
        It is a function to generate a random year.

        :param: int start: start year to generate a year

        :return: A random year between the present years.
        :rtype: str

        :Example:
            >>> random_year()
            >>> random_year(2010)

    """
    today = datetime.today()
    if start is not None:
        year = randint(start, today.year)
    else:
        year = randint(2018, today.year)
    return f'em {year}'


def month_year(start=None) -> str:
    """
        It is a function to generate a random month and year.

        :return: A random month and year between the present month and year.
        :rtype: str

        :Example:
            >>> random_month_year()

    """
    today = datetime.today()
    month = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
             'Novembro', 'Dezembro']
    month_id = randint(0, 12)
    if month_id <= today.month:
        month = month[month_id - 1]
    else:
        month_id = randint(0, today.month)
        month = month[month_id - 1]
    if start is not None:
        year = randint(start, today.year)
    else:
        year = randint(2018, today.year)
    return f'em {month} de {year}'
