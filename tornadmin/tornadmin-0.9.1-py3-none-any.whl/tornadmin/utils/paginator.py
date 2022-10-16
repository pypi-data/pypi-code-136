from math import ceil
from functools import cached_property


class Paginator:
    ELLIPSIS = '...'

    def __init__(self, object_list, per_page, count):
        """
        Pagintator class.

        :param object_list: Can be any iterable or tortoise queryset.
            If it's a queryset, tortoise's .offset() and .limit() 
            methods are used, otherwise Python's slicing [:] is used.

        :param per_page: No. of objects to list on a page.

        :param count: Total number of objects. 
        """
        self.object_list = object_list
        self.per_page = per_page
        self.count = count

    def validate_page_num(self, page_num):
        try:
            page_num = int(page_num)
            if page_num < 1:
                page_num = 1
            elif page_num > self.num_pages:
                page_num = max(self.num_pages, 1) # use max to avoid 0 page_num
        except ValueError:
            page_num = 1

        return page_num

    def get_page(self, page_num):
        page_num = self.validate_page_num(page_num)

        offset = (page_num - 1) * self.per_page
        until = offset + self.per_page

        if isinstance(self.object_list, list):
            return Page(self.object_list[offset:until], page_num, self)
        else:
            return self.get_page_from_queryset(page_num)

    def get_page_from_queryset(self, page_num):
        """Admin backends must override this to return objects from database."""
        raise NotImplementedError('Implement in subclass')

    @cached_property
    def num_pages(self):
        """Returns total pages"""
        if self.count == 0:
            return 0
        hits = max(1, self.count)
        return ceil(hits / self.per_page)

    @property
    def page_range(self):
        """
        Return a 1-based range of pages for iterating through within
        a template for loop.
        """
        return range(1, self.num_pages + 1)


    def get_elided_page_range(self, page_num=1, *, on_each_side=3, on_ends=2):
        """
        Return a 1-based range of pages with some values elided.
        If the page range is larger than a given size, the whole range is not
        provided and a compact form is returned instead, e.g. for a paginator
        with 50 pages, if page 43 were the current page, the output, with the
        default arguments, would be:
            1, 2, …, 40, 41, 42, 43, 44, 45, 46, …, 49, 50.
        """

        if page_num == 1 or page_num == self.num_pages:
            on_each_side = 2
        else:
            on_each_side = 1

        page_num = self.validate_page_num(page_num)

        if self.num_pages <= (on_each_side + on_ends) * 2:
            yield from self.page_range
            return

        if page_num > (1 + on_each_side + on_ends) + 1:
            yield from range(1, on_ends + 1)
            yield self.ELLIPSIS
            yield from range(page_num - on_each_side, page_num + 1)
        else:
            yield from range(1, page_num + 1)

        if page_num < (self.num_pages - on_each_side - on_ends) - 1:
            yield from range(page_num + 1, page_num + on_each_side + 1)
            yield self.ELLIPSIS
            yield from range(self.num_pages - on_ends + 1, self.num_pages + 1)
        else:
            yield from range(page_num + 1, self.num_pages + 1)


class Page:
    def __init__(self, object_list, number, paginator):
        self.objects = object_list
        self.number = number
        self.paginator = paginator

    def __repr__(self):
        return '<Page %s of %s>' % (self.number, self.paginator.num_pages)

    def has_next(self):
        return self.number < self.paginator.num_pages

    def has_previous(self):
        return self.number > 1

    def next_page_number(self):
        return self.number + 1

    def previous_page_number(self):
        return self.number - 1
