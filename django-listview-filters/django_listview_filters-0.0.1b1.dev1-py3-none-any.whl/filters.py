# from django.conf import settings

from django.contrib import messages

from django.contrib.admin.utils import (
    get_model_from_relation,
    get_fields_from_path,
    prepare_lookup_value,
    reverse_field_path,
    lookup_spawns_duplicates,
)
from django.contrib.admin.options import IncorrectLookupParameters

from django.core.exceptions import ImproperlyConfigured, ValidationError

from django.db import models

from django.db.models import Count

from furl import furl

from ._helpers import get_setting
from ._settings import (
    ALL_VAR,
    PAGE_VAR,
    SEARCH_VAR,
    ERROR_VAR,
    IGNORED_PARAMS,
    FILTER_PREFIX,
)


class ListViewFilter:
    """
    Base class for list view filters. Must create subclasses to provide specific functionality.
    """

    title = None  # Human-readable title to appear in the right sidebar.
    show_all = True
    show_unused_filters = True

    def __init__(self, request, params, model):
        self.used_parameters = {}
        self.show_all = get_setting("{}SHOW_ALL".format(FILTER_PREFIX), self.show_all)
        self.show_unused_filters = get_setting(
            "{}SHOW_UNUSED_FILTERS".format(FILTER_PREFIX), self.show_unused_filters
        )

        extra_ignored_params = get_setting(
            "{}EXTRA_IGNORED_PARAMS".format(FILTER_PREFIX), None
        )

        self.ignored_params = IGNORED_PARAMS

        if extra_ignored_params:
            self.ignored_params += extra_ignored_params

        if self.title is None:
            raise ImproperlyConfigured(
                "The list view filter '{}' does not specify a 'title'.".format(
                    self.__class__.__name__
                )
            )

    def has_output(self):
        """Return True if some choices would be output for this filter."""
        raise NotImplementedError(
            "Subclasses of ListViewFilter must provide a 'has_output()' method."
        )

    def choices(self, changelist):
        """
        Return choices ready to be output in the template.

        'changelist' is the ChangeList to be displayed.
        """
        raise NotImplementedError(
            "Subclasses of ListViewFilter must provide a 'choices()' method."
        )

    def queryset(self, request, queryset):
        """Return the filtered queryset."""
        raise NotImplementedError(
            "Subclasses of ListViewFilter must provide a 'queryset()' method."
        )

    def expected_parameters(self):
        """
        Return the list of parameter names that are expected from the
        request's query string and that will be used by this filter.
        """
        raise NotImplementedError(
            "Subclasses of ListViewFilter must provide an 'expected_parameters()' method."
        )

    def clear_filter_string(self, view):
        expected_params = self.expected_parameters()
        query = furl(view.request.get_full_path())
        has_param = False
        for expected_p in expected_params:
            if expected_p in query.args:
                has_param = True
                del query.args[expected_p]

        if has_param:
            return query.url
        else:
            return None


class FieldListViewFilter(ListViewFilter):
    """Filter for simple choice fields. Doesn't allow for multiple choice fields."""
    _field_list_filters = []
    _take_priority_index = 0
    list_separator = ","

    def __init__(self, field, request, params, model, field_path):
        self.field = field
        self.field_path = field_path
        self.title = getattr(field, "verbose_name", field_path)
        super().__init__(request, params, model)
        for p in self.expected_parameters():
            if p in params:
                value = params.pop(p)
                self.used_parameters[p] = prepare_lookup_value(
                    p,
                    value,  # , self.list_separator ### added in a future version of Django as an optional parameter
                )

    def has_output(self):
        return True

    def queryset(self, request, queryset):
        try:
            return queryset.filter(**self.used_parameters)
        except (ValueError, ValidationError) as err:
            raise IncorrectLookupParameters(err)

    @classmethod
    def register(cls, test, list_filter_class, take_priority=False):
        if take_priority:
            cls._field_list_filters.insert(
                cls._take_priority_index, (test, list_filter_class)
            )
            cls._field_list_filters.append((test, list_filter_class))

    @classmethod
    def create(cls, field, request, params, model, field_path):
        for test, list_filter_class in cls._field_list_filters:
            if test(field):
                return list_filter_class(
                    field, request, params, model, field_path=field_path
                )


class RelatedFieldListViewFilter(FieldListViewFilter):
    """
    For model fields that use a ForeignKey relationship.
    Not for m2m fields."""

    empty_value_display = "--"

    def __init__(self, field, request, params, model, field_path):
        other_model = get_model_from_relation(field)
        self.lookup_kwarg = "%s__%s__exact" % (field_path, field.target_field.name)
        self.lookup_kwarg_isnull = "%s__isnull" % field_path
        self.lookup_val = params.get(self.lookup_kwarg)
        self.lookup_val_isnull = params.get(self.lookup_kwarg_isnull)
        super().__init__(field, request, params, model, field_path)
        self.lookup_choices = self.field_choices(field, request)
        if hasattr(field, "verbose_name"):
            self.lookup_title = field.verbose_name
        else:
            self.lookup_title = other_model._meta.verbose_name
        self.title = self.lookup_title
        # self.empty_value_display = model_admin.get_empty_value_display()

    @property
    def include_empty_choice(self):
        """
        Return True if a "(None)" choice should be included, which filters
        out everything except empty relationships.
        """
        return self.field.null or (self.field.is_relation and self.field.many_to_many)

    def has_output(self):
        if self.include_empty_choice:
            extra = 1
        else:
            extra = 0
        return len(self.lookup_choices) + extra > 1

    def expected_parameters(self):
        return [self.lookup_kwarg, self.lookup_kwarg_isnull]

    # def field_admin_ordering(self, field, request, model_admin):
    #     """
    #     Return the model admin's ordering for related field, if provided.
    #     """
    #     related_admin = model_admin.admin_site._registry.get(field.remote_field.model)
    #     if related_admin is not None:
    #         return related_admin.get_ordering(request)
    #     return ()

    def field_choices(self, field: models.Field, request):
        model = field.model
        parent_model = field.related_model
        p_qs = parent_model.objects.all()

        if not self.show_unused_filters:
            try:
                matched_fields = (
                    model.objects.order_by()
                    .values_list(field.name, flat=True)
                    .distinct()
                )
                qs = p_qs.filter(id__in=matched_fields)

                qs = [(x.pk, str(x)) for x in qs]
            except Exception as err:
                messages.warning(request, message=err)

        return qs

    def choices(self, changelist):
        """Return dictionaries for each choice in a filter.

        <changelist> is a ListView.
        """
        if self.show_all:
            yield {
                "selected": self.lookup_val is None and not self.lookup_val_isnull,
                "query_string": changelist.get_query_string(
                    remove=[self.lookup_kwarg, self.lookup_kwarg_isnull]
                ),
                "display": "All",
            }
        for pk_val, val in self.lookup_choices:
            yield {
                "selected": self.lookup_val == str(pk_val),
                "query_string": changelist.get_query_string(
                    {self.lookup_kwarg: pk_val}, [self.lookup_kwarg_isnull]
                ),
                "display": val,
            }
        if self.include_empty_choice:
            yield {
                "selected": bool(self.lookup_val_isnull),
                "query_string": changelist.get_query_string(
                    {self.lookup_kwarg_isnull: "True"}, [self.lookup_kwarg]
                ),
                "display": self.empty_value_display,
            }


FieldListViewFilter.register(lambda f: f.remote_field, RelatedFieldListViewFilter)


class ChoicesFieldListViewFilter(FieldListViewFilter):
    """
    For model fields that use dropdowns populated by static
    variables (not a foreign key)."""

    def __init__(self, field, request, params, model, field_path):
        self.lookup_kwarg = "%s__exact" % field_path
        self.lookup_kwarg_isnull = "%s__isnull" % field_path
        self.lookup_val = params.get(self.lookup_kwarg)
        self.lookup_val_isnull = params.get(self.lookup_kwarg_isnull)
        self.lookup_choices = self.get_choices(field)
        super().__init__(field, request, params, model, field_path)

    def expected_parameters(self):
        return [self.lookup_kwarg, self.lookup_kwarg_isnull]

    def get_choices(self, field):
        model = field.model
        qs = field.flatchoices

        if not self.show_unused_filters:
            try:
                qs_dict = dict(qs)
                new_list = []
                for value in qs_dict:
                    kwargs = {field.name: value}
                    valid = model.objects.filter(**kwargs).exists()
                    if valid:
                        new_list.append((value, qs_dict[value]))
                qs = new_list
            except Exception as err:
                raise
                # messages.warning(self.request, message=err)

        return qs

    def choices(self, changelist):
        if self.show_all:
            yield {
                "selected": self.lookup_val is None,
                "query_string": changelist.get_query_string(
                    remove=[self.lookup_kwarg, self.lookup_kwarg_isnull]
                ),
                "display": "All",
            }
        none_title = ""
        for lookup, title in self.get_choices(self.field):
            if lookup is None:
                none_title = title
                continue
            yield {
                "selected": str(lookup) == self.lookup_val,
                "query_string": changelist.get_query_string(
                    {self.lookup_kwarg: lookup}, [self.lookup_kwarg_isnull]
                ),
                "display": title,
            }
        if none_title:
            yield {
                "selected": bool(self.lookup_val_isnull),
                "query_string": changelist.get_query_string(
                    {self.lookup_kwarg_isnull: "True"}, [self.lookup_kwarg]
                ),
                "display": none_title,
            }


FieldListViewFilter.register(lambda f: bool(f.choices), ChoicesFieldListViewFilter)


# This should be registered last, because it's a last resort. For example,
# if a field is eligible to use the BooleanFieldListFilter, that'd be much
# more appropriate, and the AllValuesFieldListFilter won't get used for it.
class AllValuesFieldListFilter(FieldListViewFilter):
    def __init__(self, field, request, params, model, field_path):
        self.lookup_kwarg = field_path
        self.lookup_kwarg_isnull = "%s__isnull" % field_path
        self.lookup_val = params.get(self.lookup_kwarg)
        self.lookup_val_isnull = params.get(self.lookup_kwarg_isnull)
        self.empty_value_display = self.empty_value_display
        parent_model, reverse_path = reverse_field_path(model, field_path)
        # Obey parent ModelAdmin queryset when deciding which options to show
        # if model == parent_model:
        #     queryset = model_admin.get_queryset(request)
        # else:
        queryset = parent_model._default_manager.all()
        self.lookup_choices = (
            queryset.distinct().order_by(field.name).values_list(field.name, flat=True)
        )
        super().__init__(field, request, params, model, field_path)

    def expected_parameters(self):
        return [self.lookup_kwarg, self.lookup_kwarg_isnull]

    def choices(self, changelist):
        if self.get_show_all:
            yield {
                "selected": self.lookup_val is None and self.lookup_val_isnull is None,
                "query_string": changelist.get_query_string(
                    remove=[self.lookup_kwarg, self.lookup_kwarg_isnull]
                ),
                "display": "All",
            }
        include_none = False
        for val in self.lookup_choices:
            if val is None:
                include_none = True
                continue
            val = str(val)
            yield {
                "selected": self.lookup_val == val,
                "query_string": changelist.get_query_string(
                    {self.lookup_kwarg: val}, [self.lookup_kwarg_isnull]
                ),
                "display": val,
            }
        if include_none:
            yield {
                "selected": bool(self.lookup_val_isnull),
                "query_string": changelist.get_query_string(
                    {self.lookup_kwarg_isnull: "True"}, [self.lookup_kwarg]
                ),
                "display": self.empty_value_display,
            }


FieldListViewFilter.register(lambda f: True, AllValuesFieldListFilter)
