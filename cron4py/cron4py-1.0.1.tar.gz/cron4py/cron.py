import calendar
from datetime import datetime, timedelta

from cron4py.funcs import Functions


class Cron(Functions):
    """
    :param cron: - Строка cron формата:
    "*second minute hour day_of_month month day_of_week year"
    Разрешенные разделители:
    ,-*/ ,-*/ ,-*/ ,-*/L ,-*/ ,-*/#L ,-*/

    Каждый блок поддерживает ?, это эквивалентно *.
    Но при указании в одном из "дня месяца" и "дня недели" будет выполняться пересечение,
    например при указании "дня месяца" = * или ?, а в "день недели" = Пн(числом),
    тогда выберутся все числа являющиеся Пн.

    :param start: - Время начала генерации (по умолчанию datetime.min)
    :param end: - Время окончания генерации (по умолчанию datetime.max)

    :param with_second: - Строка cron содержит часть с секундами
    :param start_sunday: - Воскресенье в cron строке имеет индекс 0, а не 6
    """

    def __init__(self, cron: str,
                 start: datetime = datetime.min,
                 end: datetime = datetime.max,
                 with_second=False,
                 week_start_sunday=True):

        self.start = start
        self.end = end
        self.curr_date = datetime.now()
        self.result = start
        self.last_result = start - timedelta(days=1)
        self.calendar = calendar.Calendar(firstweekday=6 if week_start_sunday else 0)
        self.part_list = ['minute', 'hour', 'day_of_month', 'month', 'day_of_week', 'year']

        if with_second:
            self.part_list.insert(0, 'second')
        cron_parts = cron.split(' ')

        assert len(cron_parts) == len(self.part_list), 'Количество частей строки cron отличается от разрешенного'

        self.allowed_keys = ['second', 'minute', 'hour', 'day', 'month', 'year']
        self.allowed = dict(
            **{'second': []} if with_second else {},
            minute=[],
            hour=[],
            day=[],
            month=[],
            year=[]
        )
        self.limits['year'] = [self.start.year, self.end.year]

        super(Cron, self).__init__()

        self.cron_dict = dict([self.part_check(_tuple[0], _tuple[1]) for _tuple in zip(self.part_list, cron_parts)])

    def generator(self) -> datetime:
        """Функция возвращает генератор, где каждый элемент - объект datetime"""
        # print('generator')
        while True:
            result = self.gen_next()

            if not result or result > self.end:
                return "Достигнут предел последовательности"
            self.last_result = result
            # print(result)
            yield result
