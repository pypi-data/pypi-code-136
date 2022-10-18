from copy import copy

from django.db.models import DEFERRED
from django.forms.models import model_to_dict


class ModelDiffMixin(object):
    """
    A model mixin that tracks model fields' values and provide some useful api
    to know what fields have been changed.
    """

    __is_creation = False

    def __init__(self, *args, **kwargs):
        super(ModelDiffMixin, self).__init__(*args, **kwargs)
        self._saving_change_callbacks = False
        self.__initial = self._get_model_dict()
        self.__is_creation = self.pk is None

    def save(self, *args, **kwargs):
        """
        Saves model and set initial state.
        """
        self.__is_creation = self.pk is None
        if not self._saving_change_callbacks:
            self._saving_change_callbacks = True
            try:
                for field in self.changed_fields:
                    on_change_func = getattr(self, "on_%s_change" % field, None)
                    if callable(on_change_func):
                        on_change_func(*self.get_field_diff(field))
            finally:
                self._saving_change_callbacks = False
        super(ModelDiffMixin, self).save(*args, **kwargs)
        self.__initial = self._get_model_dict()

    def _get_model_dict(self):
        """

        :return:
        :rtype: dict
        """
        all_fields = [(field.name, field.get_attname()) for field in self._meta.fields]
        deferred_fields = self.get_deferred_fields()

        data_dict = model_to_dict(
            self, fields=[f[0] for f in all_fields if f[1] not in deferred_fields]
        )
        for f in deferred_fields:
            data_dict[f] = DEFERRED

        # Make copies of dicts, lists (when fields are JSONField & ArrayField, respectively)
        for k, v in data_dict.items():
            if isinstance(v, (list, dict)):
                data_dict[k] = copy(v)

        return data_dict

    def _get_diff(self):
        diffs = []
        d1 = self.__initial
        d2 = self._get_model_dict()

        for k, v in d1.items():
            f = self._meta.get_field(k)
            v2 = f.to_python(d2[k])
            if v != DEFERRED and v != v2:
                diffs.append((k, (v, v2)))

        return dict(diffs)

    @property
    def has_changed(self):
        """True if the model has changed
        :rtype: bool
        """
        return bool(self._get_diff())

    @property
    def is_creation(self):
        """
        True if the model is being created for the first time
        """
        return self.__is_creation

    @property
    def changed_fields(self):
        """

        :return:
        :rtype: list(str)
        """
        return self._get_diff().keys()

    @property
    def initial(self):
        """
        Returns the old version of the model.

        Note: if the model save has been committed, the old version will be gone.
        """
        return self.__initial

    def get_field_diff(self, field_name):
        """
        Returns a diff for field if it's changed and None otherwise.

        :rtype: tuple(any)
        """
        return self._get_diff().get(field_name, None)
