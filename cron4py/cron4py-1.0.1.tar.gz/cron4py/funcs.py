import calendar
import re
from copy import deepcopy
from datetime import datetime, timedelta
from typing import Union

BLOCKS = {
    'second': 'секунд',
    'minute': 'минут',
    'hour': 'часов',
    'month': 'месяцев',
    'year': 'лет',
    'day_of_month': 'дней месяца',
    'day_of_week': 'дней недели',
}


class Functions:
    """"""

    limits = {
        'second': [0, 59],
        'minute': [0, 59],
        'hour': [0, 23],
        'month': [1, 12],
        'day_of_month': [1, 31],
        # 0- вс, 1 - пн, 6-сб
        'day_of_week': [0, 6],
        'year': []
    }

    def __init__(self):
        self.last = {
            'second': -1,
            'minute': -1,
            'hour': -1,
            'month': -1,
            'day': -1,
            'year': -1,
        }

    def part_check(self, name, part):
        """
        second, minute, hour, month,year - ,-*/
        day_of_month - ,-*/L
        day_of_week - ,-*/#L
        :param part: part cron format string
        :param name: name part
        :return: None
        """
        if name in ['second', 'minute', 'hour', 'month', 'year']:
            # Проверка на допустимые символы
            if ('L' in part or '#' in part):
                raise Exception('Не поддерживаемый литерал ({}) в блоке {}.'.format(str(['L', '#']), BLOCKS[name]))
        if name == 'day_of_month' and '#' in part:
            raise Exception('Не поддерживаемый литерал ({}) в блоке {}.'.format('#', BLOCKS[name]))
        self.part_start_parser(
            name,
            part,
            **{
                'day': self.start.day,
                'month': self.start.month,
                'year': self.start.year
            } if name in ['day_of_month', 'day_of_week'] else {}
        )
        return name, part

    def part_parser(self, name, lparts, rparts, first_start=False, day=None, month=None, year=None) -> set:
        """
        Фукнция выполняет расчет базовых допустимых значений и вызывает парсинг

        :param lparts: левая часть строки крона
        :param rparts: правая часть строки крона
        :param name: название части
        :param first_start: флаг первого запуска
        :param month: месяц для которого расчитываются дни
        :param year: год для месяца
        :return list: allowed elements
        """
        if name in ['day_of_month', 'day_of_week']:
            if None not in [day, month, year] and not self.allowed['day']:
                start = day
                _, end = calendar.monthrange(year, month)
                allowed = list(range(start, end + 1))
            elif self.allowed['day']:
                allowed = self.allowed['day']
            else:
                raise Exception(
                    'Переданы не все параметры для расчета допустимых дней месяца '
                    '(день-{}, месяц-{}, год-{})'.format(day, month, year)
                )
        elif first_start and name in ['second', 'minute', 'hour']:
            allowed = list(range(getattr(self.start, name), self.limits[name][1] + 1))
        else:
            allowed = list(range(self.limits[name][0], self.limits[name][1] + 1))
        giterator, literator = self.__rpart_parser(rparts)
        if giterator and name == 'day_of_week':
            giterator = rparts[0]
        allowed = self.__lpart_parser(name, lparts, giterator, literator, allowed, year, month)
        return allowed

    def part_start_parser(self, name, part, first_start=False, day=1, month=None, year=None) -> None:
        """Функция выполняет инициализацию и запуск парсера"""

        parts = re.findall(r'([\d\*\?]+(?![-\d]))|(\d+-\d+)|((?:(?=[#L\/]).*))', part)
        lparts = [val[0] or val[1] for val in parts if any(val[:-1])]
        rparts = [val[2] for val in parts if val[2]]

        if 'L' in rparts and not lparts:
            lparts = ['*']

        # print(name, lparts, rparts, end=' ')

        allowed = self.part_parser(name, lparts, rparts, first_start, day=day, month=month, year=year)
        if name == 'day_of_month':
            name = 'day'
            self.allowed[name] = set(range(self.limits['day_of_month'][0], self.limits['day_of_month'][1] + 1))
            self.allowed[name] &= allowed
        elif name == 'day_of_week':
            name = 'day'
            self.allowed[name] = set(self.allowed[name]) & allowed
        else:
            self.allowed[name] = set(range(self.limits[name][0], self.limits[name][1] + 1))
            self.allowed[name] &= allowed

        self.allowed[name] = list(self.allowed[name])
        self.allowed[name].sort()
        # print('Допустимое -> {}'.format(self.allowed[name]))

    def gen_next(self):
        if self.result == self.start:
            for key in self.allowed_keys:
                if getattr(self.result, key) not in self.allowed[key]:
                    break
            else:
                self.last['second'] = self.result.second
                if self.last['second'] == self.allowed['second'][-1]:
                    self.last['second'] = -1
                result = self.result
                self.result += timedelta(seconds=1)
                return result

        result = self.__iterator('second')
        if isinstance(result, datetime):
            if self.last['second'] == self.allowed['second'][-1]:
                self.last['second'] = -1
            self.result = result
            return result
        elif (
                self.allowed['minute'] and self.allowed['minute'][-1] > self.result.minute
        ) and self.result.hour in self.allowed['hour']:
            self.last['minute'] = self.result.minute
            self.result = self.result.replace(
                minute=list(filter(lambda x: x > self.result.minute, self.allowed['minute']))[0],
                second=0
            )
            self.last['second'] = -1
            return self.gen_next()
        elif (
                self.allowed['hour'] and self.allowed['hour'][-1] > self.result.hour
        ) and self.result.day in self.allowed['day']:
            self.last['hour'] = self.result.hour
            self.result = self.result.replace(
                hour=list(filter(lambda x: x > self.result.hour, self.allowed['hour']))[0],
                minute=0,
                second=0
            )
            self.last['second'] = -1
            self.last['minute'] = -1
            return self.gen_next()
        elif (
                self.allowed['day'] and self.allowed['day'][-1] > self.result.day
        ) and self.result.month in self.allowed['month']:
            self.last['day'] = self.result.day
            self.result = self.result.replace(
                day=list(filter(lambda x: x > self.result.day, self.allowed['day']))[0],
                hour=0,
                minute=0,
                second=0
            )
            self.last['second'] = -1
            self.last['minute'] = -1
            self.last['hour'] = -1

            return self.gen_next()
        elif (
                self.allowed['month'] and self.allowed['month'][-1] > self.result.month
        ) and self.result.year in self.allowed['year']:
            self.last['month'] = self.result.month
            self.result = self.result.replace(
                month=list(filter(lambda x: x > self.result.month, self.allowed['month']))[0],
                day=1,
                hour=0,
                minute=0,
                second=0
            )
            self.last['second'] = -1
            self.last['minute'] = -1
            self.last['hour'] = -1
            self.last['day'] = -1
            # Сменив месяц, выполняем перерасчет допустимых дней
            self.allowed['day'] = []
            self.part_start_parser(
                name='day_of_month',
                part=self.cron_dict['day_of_month'],
                day=self.result.day,
                month=self.result.month,
                year=self.result.year
            )
            self.part_start_parser(
                name='day_of_week',
                part=self.cron_dict['day_of_week'],
                day=self.result.day,
                month=self.result.month,
                year=self.result.year
            )
            return self.gen_next()
        elif self.allowed['year'] and self.allowed['year'][-1] > self.result.year:
            self.last['year'] = self.result.year
            self.result = self.result.replace(
                year=list(filter(lambda x: x > self.result.year, self.allowed['year']))[0],
                month=self.allowed['month'][0],
                day=1,
                hour=0,
                minute=0,
                second=0
            )
            self.last['second'] = -1
            self.last['minute'] = -1
            self.last['hour'] = -1
            self.last['day'] = -1
            self.last['month'] = -1
            # Сменив месяц, выполняем перерасчет допустимых дней
            self.allowed['day'] = []
            self.allowed['month'] = []
            self.part_start_parser(
                name='month',
                part=self.cron_dict['month'],
                day=self.result.day,
                month=self.result.month,
                year=self.result.year
            )
            self.part_start_parser(
                name='day_of_month',
                part=self.cron_dict['day_of_month'],
                day=self.result.day,
                month=self.result.month,
                year=self.result.year
            )
            self.part_start_parser(
                name='day_of_week',
                part=self.cron_dict['day_of_week'],
                day=self.result.day,
                month=self.result.month,
                year=self.result.year
            )
            return self.gen_next()

        return None

    def __get_next_date_part(self, date_part) -> Union[None, int]:
        """Функция находит ближайшую доступную часть даты"""
        result = None
        for val in self.allowed[date_part]:
            if getattr(self.result, date_part) < val:
                result = val
                break
        return result

    def __iterator(self, name):
        """
        Функция выполняет поиск первого подходящего значения из разрешенных для указанной части

        :param name - название части

        :return None, datetime: подходящая дата или None
        """
        result = None
        for allowed in self.allowed[name]:
            if getattr(self.result, name) <= allowed and self.last[name] != allowed:
                result = {
                    'year': self.result.year,
                    'month': self.result.month,
                    'day': self.result.day,
                    'hour': self.result.hour,
                    'minute': self.result.minute,
                    'second': self.result.second,
                }
                result.update({name: allowed})
                result = datetime(**result)
                self.last[name] = allowed
                break
        if result == self.result and result == self.last_result:
            return None
        if isinstance(result, datetime):
            for key, value in self.allowed.items():
                if getattr(result, key) not in value:
                    return None
        return result

    def __rpart_parser(self, rparts):
        """
        Функция обрабатывающая правую часть

        literator (local iterator) - локальный итератор ((/) каждый второй день)
        giterator (global iterator) - глобальный итератор ((#) в конкретную неделю)

        """
        giterator = 0
        literator = set()
        if rparts:
            if len(rparts) == 1:
                rparts = rparts[0]
            else:
                raise Exception('Не удалось распознать содержимое части {}'.format(' '.join(rparts)))
            if '/' in rparts and '#' in rparts:
                raise Exception('Одновременно использовать # и / чтобы что? (ПН#2/2==ПН,СР,ПТ,ВС#2')
            if '/' in rparts:
                # Глобальный итератор, итерирует внутри своего блока
                giterator = int(rparts[1:])
            elif '#' in rparts:
                # Локальный итератор, итерирует внутри блока из которого состоит глобальный блок
                tmpliterator = rparts[1:]
                if ',' in tmpliterator:
                    tmpliterator = [val for val in tmpliterator.split(',')]
                for lit in tmpliterator:
                    if '-' in lit:
                        literator.update({int(val) for val in range(lit.split('-')[0], lit.split('-')[1] + 1)})
                    else:
                        literator.add(int(lit))
            elif rparts == 'L':
                giterator = -1
            else:
                raise Exception('Непредвиденная ситуация для правой части {}'.format(rparts))
            if giterator < 0 and 'L' not in rparts:
                raise Exception('Глобальный итератор не может быть меньше 0')
        return giterator, literator

    def __lpart_parser(self, name, lparts, giterator, literator, allowed, year, month):
        _allowed = set()
        acceptable = set(range(allowed[0], allowed[-1] + 1))
        for part_of_parts in lparts:
            if '-' in part_of_parts:
                start, end = part_of_parts.split('-')
                _allowed.update(set(range(int(start), int(end) + 1)))
            elif '*' in part_of_parts or '?' in part_of_parts:
                if not giterator:
                    _allowed = acceptable
                elif isinstance(giterator, int) and giterator < 0:
                    _allowed = {allowed[-1]}
                else:
                    # Что-то не помню зачем так сделал, возможен отстрел
                    _allowed = {allowed[0]}
            elif part_of_parts.isdigit():
                _allowed.update(set(allowed) & {int(part_of_parts)})
            else:
                raise Exception('Не удалось распознать содержимое левой части {}, а конкретно {}'.format(
                    lparts, part_of_parts
                ))

            if giterator and name != 'day_of_week':
                pre_allowed = deepcopy(_allowed)
                if giterator < 0:
                    _allowed.add(self.limits[name][-1])
                else:
                    for allow in pre_allowed:
                        for _allow in range(allow, self.limits[name][1] + 1, giterator):
                            _allowed.add(_allow)

        if name == 'day_of_week' and self.allowed['day']:
            if (
                    '*' not in lparts and '?' not in lparts
            ) or (isinstance(giterator, str) and 'L' in giterator):
                # Если это день недели, то в _allowed день недели, а не день месяца
                _allowed_wdays = set()
                weeks = self.calendar.monthdayscalendar(year, month)
                if giterator:
                    if isinstance(giterator, str) and '#' in giterator:
                        giterator = int(giterator[1:])
                        weeks = [val for i, val in enumerate(weeks, start=1) if i % giterator == 0]
                    elif isinstance(giterator, str) and 'L' in giterator and '*' not in lparts:
                        # Если мы ищем последний день недели месяца, то разворачиваем порядок недель в месяце
                        weeks = reversed(weeks)
                    elif isinstance(giterator, str) and 'L' in giterator and '*' in lparts:
                        return {d for d in weeks[-1] if d > 0}
                for week in weeks:
                    if self.allowed['day'][-1] < week[0] and isinstance(giterator, str) and 'L' not in giterator:
                        # Отключаем проверку на преувеличение итераций при поиске последнего дня недели в месяце
                        break
                    if isinstance(giterator, str) and 'L' in giterator and _allowed_wdays:
                        # Если мы нашли нужный день, дальше итерироваться не стоит
                        break
                    for _allow in _allowed:
                        if isinstance(giterator, str) and '/' in giterator:
                            _allowed_wdays.update({d for d in week[_allow::int(giterator[1:])] if d > 0})
                        else:
                            if week[_allow] != 0:
                                _allowed_wdays.add(week[_allow])
                                if isinstance(giterator, str) and 'L' in giterator:
                                    # Если мы нашли нужный день, дальше итерироваться не стоит
                                    break
                _allowed = _allowed_wdays
        return _allowed
