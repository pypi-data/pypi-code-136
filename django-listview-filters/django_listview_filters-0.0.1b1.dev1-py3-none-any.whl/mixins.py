from django.db.models import Field

from django.views.generic import View
from django.views.generic.list import MultipleObjectMixin

from django.contrib.admin.utils import get_fields_from_path

from furl import furl

from ._helpers import get_setting
from .filters import FieldListViewFilter, ListViewFilter
from ._settings import (
    FILTER_PREFIX,
    ALL_VAR,
    PAGE_VAR,
    SEARCH_VAR,
    ERROR_VAR,
    IGNORED_PARAMS,
)


class FilterViewMixin(MultipleObjectMixin, View):
    def __init__(self) -> None:
        self.all_var = get_setting("{}ALL_VAR".format(FILTER_PREFIX), ALL_VAR)
        self.page_var = get_setting("{}PAGE_VAR".format(FILTER_PREFIX), PAGE_VAR)
        self.search_var = get_setting("{}SEARCH_VAR".format(FILTER_PREFIX), SEARCH_VAR)
        self.error_var = get_setting("{}ERROR_VAR".format(FILTER_PREFIX), ERROR_VAR)

        extra_ignored_params = get_setting(
            "{}EXTRA_IGNORED_PARAMS".format(FILTER_PREFIX), None
        )

        self.ignored_params = IGNORED_PARAMS

        if extra_ignored_params:
            self.ignored_params += extra_ignored_params

        return super().__init__()

    """Add filtering context"""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        fragment = furl(self.request.get_full_path())

        # Get list of args; should be a good proxy for filters
        non_page_args = []
        for arg in fragment.args:
            if arg != "page":
                non_page_args.append(arg)

        context["non_page_args"] = non_page_args

        # Start generating actual lists and paths for filters
        filter_list = []

        # for filter in self.filters:
        #     # filter_obj = PartRevisionFilter()
        #     objects, clear_filter_fragment = filter.filter_list(self.request)
        #     filter_list.append((filter.name, objects, clear_filter_fragment))

        for filter in self.filter_specs:
            clear_filter_url = filter.clear_filter_string(self)
            if isinstance(filter, FieldListViewFilter):
                choices = filter.choices(self)
                choices_list = []
                for counter, choice in enumerate(choices):
                    choices_list.append(choice)
                filter_list.append((filter.title, choices_list, clear_filter_url))

        context["filter_list"] = filter_list

        # Create "clear filter" paths
        new_fragment = fragment.copy()

        size = new_fragment.args.size()
        if size > 0 and not (
            size == 1 and new_fragment.args.has_key("page")
        ):  # Only offer "clear all" button if a non-page arg is present
            context["clear_filter_fragment"] = new_fragment.path

        return context

    def get_params(self, request):
        fragment = furl(request.get_full_path())
        new_fragment = fragment.copy()
        if self.page_var in new_fragment.args:
            del new_fragment.args[self.page_var]
        if self.error_var in new_fragment.args:
            del new_fragment.args[self.error_var]

        return dict(new_fragment.args)

    def filter_queryset(self, queryset):
        self.params = self.get_params(self.request)
        self.model = self.queryset.__getattribute__("model")

        (
            self.filter_specs,
            self.has_filters,
            remaining_lookup_params,
            filters_may_have_duplicates,
            self.has_active_filters,
        ) = self.get_filters(self.request)

        for filter_spec in self.filter_specs:
            new_qs = filter_spec.queryset(self.request, queryset)
            if new_qs is not None:
                queryset = new_qs

        return queryset

    def get_queryset(self):
        qs = super().get_queryset()

        qs = self.filter_queryset(qs)

        return qs

    def get_filters_params(self, params: dict = None):
        """Return all params except IGNORED_PARAMS."""
        params = params or self.params
        if not params:
            return {}
        lookup_params = params.copy()
        for ignored in self.ignored_params:
            if ignored in lookup_params:
                del lookup_params[ignored]
        return lookup_params

    def get_filters(self, request):
        lookup_params = self.get_filters_params()
        may_have_duplicates = False
        has_active_filters = False

        filter_specs = []
        for list_filter in self.list_filter:
            lookup_params_count = len(lookup_params)
            if callable(list_filter):
                spec = list_filter(request, lookup_params, self.model)
            else:
                field_path = None
                if isinstance(list_filter, (tuple, list)):
                    field, field_list_filter_class = list_filter
                else:
                    # This is simply a field name, so use the default
                    # FieldListFilter class that has been registered for the
                    # type of the given field.
                    field, field_list_filter_class = (
                        list_filter,
                        FieldListViewFilter.create,
                    )
                if not isinstance(field, Field):
                    field_path = field
                    field = get_fields_from_path(self.model, field_path)[-1]

                spec = field_list_filter_class(
                    field,
                    request,
                    lookup_params,
                    self.model,
                    field_path=field_path,
                )
                # field_list_filter_class removes any lookup_params it
                # processes. If that happened, check if duplicates should be
                # removed.
                # if lookup_params_count > len(lookup_params):
                #     may_have_duplicates |= lookup_spawns_duplicates(
                #         self.lookup_opts,
                #         field_path,
                #     )
            if spec and spec.has_output():
                filter_specs.append(spec)
                if lookup_params_count > len(lookup_params):
                    has_active_filters = True

        return (
            filter_specs,
            bool(filter_specs),
            lookup_params,
            may_have_duplicates,
            has_active_filters,
        )

    def get_query_string(self, new_params: dict = None, remove: list = None):
        if new_params is None:
            new_params = {}
        if remove is None:
            remove = []

        query = furl(self.request.get_full_path())

        for r in remove:
            list = [k for k in query.args if k.startswith(r)]
            for k in list:
                del query.args[k]
        for k, v in new_params.items():
            if v is None:
                if k in query.args:
                    del query.args[k]
            else:
                query.args[k] = v

        return query

    def get_filter_by_name(self, filter_name:str) -> ListViewFilter:
        """Return filter matching `filter_name`
        
        :param filter_name: name of filter
        :type filter_name: str
        :return: Filter that matches filter_name
        :rtype: ListViewFilter, None if no match found"""
        if len(self.filter_specs) > 0:
            for filter_spec in self.filter_spec:
                filter = filter_spec if filter_spec.field_path == filter_name else None
        else:
            filter = None

        return filter