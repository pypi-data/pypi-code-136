from wtforms import validators
from wtforms import fields
from tornadmin.backends.forms import (
    BaseModelForm, NullDateField, NullDateTimeField, SelectField,
)
from tornadmin.utils.text import get_display_name
from tortoise.query_utils import Q


class ModelForm(BaseModelForm):
    async def set_field_choices(self, request_handler, obj=None):
        """Sets choices foreignkey and manytomany fields"""
        for field_name in self.Meta.model._meta.fk_fields | self.Meta.model._meta.o2o_fields:
            form_field = getattr(self, '%s_id' % field_name, None)
            if not form_field:
                continue
            choices = await self._get_field_choices(request_handler, field_name, obj)
            form_field.choices = choices

        for field_name in self.Meta.model._meta.m2m_fields:
            form_field = getattr(self, field_name, None)
            if not form_field:
                continue
            choices = await self._get_field_choices(request_handler, field_name, obj)
            form_field.choices = choices

    async def _get_field_choices(self, request_handler, field_name, obj=None):
        """Returns choices for the given field name."""

        if hasattr(self, 'get_%s_choices' % field_name):
            return await getattr(self, 'get_%s_choices' % field_name)(request_handler)

        model_field = self.Meta.model._meta.fields_map[field_name]
        if field_name in self.Meta.model._meta.o2o_fields:
            if obj:
                objects = await model_field.related_model.filter(
                    Q(**{model_field.related_name: None}) |
                    Q(**{model_field.related_name: obj.id})
                )
            else:
                objects = await model_field.related_model.filter(**{model_field.related_name: None})
        else:
            objects = await model_field.related_model.all()
        return [(obj.id, str(obj)) for obj in objects]


TORTOISE_TO_WTF_MAP = {
    'BigIntField': fields.IntegerField,
    'BooleanField': fields.BooleanField,
    'CharField': fields.StringField,
    'DateField': NullDateField,
    'DatetimeField': NullDateTimeField,
    'FloatField': fields.FloatField,
    'IntField': fields.IntegerField,
    'SmallIntField': fields.IntegerField,
    'TextField': fields.TextAreaField,
    'ForeignKeyField': SelectField,
    'ManyToManyFieldInstance': fields.SelectMultipleField,
}


def tortoise_to_wtf(tortoise_field, is_fk=False):
    if is_fk:
        return TORTOISE_TO_WTF_MAP['ForeignKeyField']

    return TORTOISE_TO_WTF_MAP.get(
        type(tortoise_field).__name__, 
        fields.StringField
    )


def modelform_factory(admin, model):
    fields = {}
    fk_id_fields = []

    for field_name in model._meta.fk_fields | model._meta.o2o_fields:
        fk_id_fields.append('%s_id' % field_name)

    for field_name, model_field in model._meta.fields_map.items():

        if admin.fields:
            if field_name not in admin.fields:
                continue

        if field_name in admin.exclude:
            continue

        if field_name not in admin.readonly_fields:
            if model_field.pk:
                continue

            if getattr(model_field, 'auto_now', False):
                continue

            if getattr(model_field, 'auto_now_add', False):
                continue

        if field_name in fk_id_fields:
            continue

        if field_name in model._meta.backward_fk_fields:
            continue

        if field_name in model._meta.backward_o2o_fields:
            continue

        name = get_display_name(field_name)

        validators_list = []

        if model_field.required and field_name not in admin.readonly_fields:
            validators_list.append(validators.required())
        else:
            validators_list.append(validators.optional())

        if hasattr(model_field, 'max_length'):
            validators_list.append(validators.Length(max=model_field.max_length))

        field_kwargs = {}
        attrs = {'placeholder': name}

        if field_name in admin.readonly_fields:
            attrs['readonly'] = True

        is_fk = field_name in model._meta.fk_fields
        is_m2m = field_name in model._meta.m2m_fields
        is_o2o = field_name in model._meta.o2o_fields

        form_field = tortoise_to_wtf(model_field, is_fk=is_fk or is_o2o)

        if is_fk or is_o2o:
            # For foreignkeys, we'll render a select input
            # with the "_id" appended to the name
            field_name = '%s_id' % field_name

        if is_fk or is_m2m:
            field_kwargs['coerce'] = int # :TODO: use the type of primary key

        fields[field_name] = form_field(
            name,
            validators_list,
            render_kw=attrs,
            **field_kwargs
        )

    fields['_fields'] = list(fields.keys())

    form = type('%sForm' % model.__name__, (ModelForm,), fields)
    form.Meta.model = model

    return form
