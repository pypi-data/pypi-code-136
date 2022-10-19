#!/usr/bin/env python
# coding: utf-8

from copy import copy, deepcopy

from nopea.exceptions import TooManyResultsError


class QuerySet:

    def __init__(self, base):
        self.base = base
        self.adaptor = self.base.adaptor
        self.query = ''
        self.query_args = []
        self.partials = {
            'filters': [],
            'excludes': [],
            'updates': [],
            'orders': [],
            'offset': None,
            'limit': None,
            'create': None,
            'all': False,
            'count': False,
            'delete': False,
        }

    def __repr__(self):
        result = self()
        appendix = ""
        if len(result) > 20:
            appendix = " ..remainung elements truncated."
        return "%s%s" % (str([item for item in result[:20]]), appendix)

    def __len__(self):
        result = self()
        return len(result)

    def make_objects(self, instance, db_results) -> list:
        objects = []
        cls = instance.__class__
        for result in db_results:
            _object = cls()
            mapped = zip(instance.fields, result)
            for field, value in mapped:
                field.make_value(value)
                setattr(_object, field.fieldname, field.value)

            for reverse_name, related_manager in cls.related_managers.items():
                new_manager = copy(related_manager)
                new_manager.id = _object.id
                setattr(_object, reverse_name, new_manager)

            objects.append(_object)

        return objects

    def _make_query_base(self):
        if self.partials['count'] == True:
            self.query = self.adaptor.get_count_query(self.base)
        else:
            self.query = self.adaptor.get_select_query(self.base)

    def _make_where_clause(self):
        if self.partials['filters'] or self.partials['excludes']:
            self.query += ' WHERE '

    def _make_updates(self):
        if self.partials['updates']:
            self.query, update_args = self.adaptor.get_update_query(self.base, self.partials['updates'][0])
            self.query_args.extend(update_args)
            if self.partials['filters']:
                self.query += 'WHERE '

    def _make_deletions(self):
        if self.partials['delete']:
            self.query = self.adaptor.get_delete_query(self.base)
            if self.partials['filters']:
                self.query += 'WHERE '

    def _make_filters(self):
        if self.partials['filters']:
            filters = []
            for filter_partial in self.partials['filters']:
                filter_query, filter_args = self.adaptor.get_filter_query(filter_partial)
                filters.append(filter_query)
                if isinstance(filter_args, list):
                    self.query_args.extend(filter_args)
                else:
                    self.query_args.append(filter_args)
            self.query += ' AND '.join([item for item in filters])
            if self.partials['excludes']:
                self.query += ' AND '

    def _make_excludes(self):
        if self.partials['excludes']:
            excludes = []
            for exclude_partial in self.partials['excludes']:
                exclude_query, exclude_args = self.adaptor.get_exclude_query(exclude_partial)
                excludes.append(exclude_query)
                if isinstance(exclude_args, list):
                    self.query_args.extend(exclude_args)
                else:
                    self.query_args.append(exclude_args)
            self.query += ' AND '.join([item for item in excludes])

    def _make_orders(self):
        if self.partials['orders']:
            self.query += ' ORDER BY '
            orders = []
            for order_partial in self.partials['orders']:
                direction = 'DESC' if order_partial[0].startswith('-') else 'ASC'
                orders.append('%s %s' % (order_partial[0].replace('-', ''), direction))
            self.query += ', '.join(orders)

    def _make_offset(self):
        if self.partials['offset']:
            self.query += self.adaptor.get_offset_query(self.partials['offset'], self.partials['limit'])

    def _make_limit(self):
        if self.partials['limit']:
            self.query += self.adaptor.get_limit_query(self.partials['limit'], self.partials['offset'])

    def compile_query(self) -> tuple:
        self.query_args = []

        self._make_query_base()
        self._make_where_clause()
        self._make_updates()
        self._make_deletions()
        self._make_filters()
        self._make_excludes()
        self._make_orders()
        self._make_limit()
        self._make_offset()
        return (self.query, self.query_args)

    def execute_sql(self):
        query, query_args = self.compile_query()
        result = self.adaptor.execute_query(query, query_args)[0]
        return result

    def __call__(self):
        result = self.execute_sql()
        if self.partials['count']:
            return result[0][0]
        return self.make_objects(self.base, result)

    def __iter__(self):
        objects = self.make_objects(self.base, self.execute_sql())
        for item in objects:
            yield item

    def __getitem__(self, s):
        if isinstance(s, int):
            start = s
            stop = s + 1

            self.partials['offset'] = start
            self.partials['limit'] = stop
            return list(self)[0]
        if isinstance(s, slice):
            start = s.start
            stop = s.stop

        self.partials['offset'] = start
        self.partials['limit'] = stop
        return list(self)

    def filter(self, *args, **kwargs):
        if not kwargs:
            self.partials['all'] = True
        for key, value in kwargs.items():
            self.partials['filters'].append({key: value})
        return self

    def exclude(self, *args, **kwargs):
        for key, value in kwargs.items():
            self.partials['excludes'].append({key: value})
        return self

    def all(self):
        return self.filter()

    def get(self, *args, **kwargs):
        result = self.filter(*args, **kwargs)()

        if len(result) <= 1:
            try:
                return result[0]
            except IndexError:
                raise IndexError("No %s object found" % self.base.__class__.__name__)
        raise TooManyResultsError('To many results for get(): %s' % len(result))

    def delete(self, *args, **kwargs) -> None:
        self.partials['delete'] = True
        self()
        return None

    def update(self, *args, **kwargs):
        count = 0
        filters = self.partials['filters']
        if filters:
            count_qs = QuerySet(self.base)
            for item in filters:
                count_qs = count_qs.filter(**item)
            count = len(count_qs)

        for key, value in kwargs.items():
            self.partials['updates'].append({key: value})
        self()
        return count

    def order_by(self, *args):
        self.partials['orders'].append(args)
        return self

    def first(self):
        self.partials['limit'] = 1
        result = self()
        if result:
            return result[0]

    def last(self):
        count_qs = QuerySet(self.base)
        filters = self.partials['filters']
        for item in filters:
            count_qs = count_qs.filter(**item)
        count = len(count_qs)

        self.partials['offset'] = count - 1
        result = self()
        if result:
            return result[0]

    def count(self):
        self.partials['count'] = True
        return self()

    def exists(self):
        return len(self) > 0
