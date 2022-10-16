from tornadmin.utils.paginator import Page, Paginator as BasePaginator


class Paginator(BasePaginator):
    def get_page_from_queryset(self, page_num):
        offset = (page_num - 1) * self.per_page
        return Page(self.object_list.offset(offset).limit(self.per_page), page_num, self)
