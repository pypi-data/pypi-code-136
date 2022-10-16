from tornadmin.backends.base import BaseModelAdmin
from tornadmin.backends.tortoise.forms import modelform_factory
from tornadmin.backends.tortoise.paginator import Paginator
from tornadmin.backends.tortoise.actions import delete_selected
from tornadmin.utils.text import split_camel, slugify, get_display_name


class ModelAdmin(BaseModelAdmin):
    order_by = [
        ('Newest first', '-id'),
        ('Oldest first', 'id'),
    ]

    def __init__(self, model, **kwargs):
        name = model.__name__

        self.model = model
        self.name = kwargs.get('name', ' '.join(split_camel(name)))
        self.slug = kwargs.get('slug', name.lower())
        self.app = kwargs['app']
        self.app_slug = slugify(self.app)

    def get_list_headers(self):
        # :TODO: cache this function
        headers = []
        for header in self.list_headers:
            if isinstance(header, tuple) or isinstance(header, list):
                headers.append(header)
            else:
                headers.append((header, get_display_name(header)))
        return headers

    async def get_list(self, request_handler, page_num, q, o, filters):
        queryset = self.model.all()

        if q:
            queryset = self.get_search_results(queryset, q)

        if filters:
            queryset = self.get_filtered_results(queryset, filters)

        count = await queryset.count()

        paginator = Paginator(queryset, per_page=self.items_per_page, count=count)
        page = paginator.get_page(page_num)
        page_queryset = page.objects

        # fetch related fields which are also shown on list page table
        # :TODO: pre-fetch chained related fields
        related_fields = [field for field in self.prefetch_fields]
        for header in self.get_list_headers():
            field = header[0]

            if not isinstance(field, str):
                continue

            if '__' in field:
                field = field.split('__')[0]
            if field in [*self.model._meta.fk_fields, *self.model._meta.o2o_fields]:
                related_fields.append(field)

        if not o:
            try:
                o = self.get_order_by(request_handler)[0][1]
            except IndexError: # order_by list is set to empty
                o = '-id'

        if related_fields:
            page_list = await page_queryset.order_by(o).prefetch_related(*related_fields)
        else:
            page_list = await page_queryset.order_by(o)

        return (page_list, page)

    def get_search_results(self, queryset, search_term):
        raise NotImplementedError('Implement in subclass')

    def get_actions(self, request_handler):
        actions = super().get_actions(request_handler)
        actions.append(delete_selected)
        return actions

    async def get_action_queryset(self, request_handler, action_name, selected, selected_all):
        if selected_all:
            return self.self.model.all()
        else:
            return self.model.filter(id__in=selected)

    async def get_fitlers(self, request_handler):
        filters = await super().get_filters(request_handler)
        return filters

    def get_filtered_results(self, queryset, filters):
        return queryset

    async def get_object(self, request_handler, id):
        return await self.model.get(id=id)

    async def get_form_data(self, obj):
        """Returns initial form data from the given model object"""
        # first fetch related fields
        await obj.fetch_related(*obj._meta.fk_fields, *obj._meta.m2m_fields)

        data = {}

        for field_name, model_field in obj._meta.fields_map.items():
            if field_name in obj._meta.m2m_fields:
                data[field_name] = [item.id for item in getattr(obj, field_name)]
            else:
                data[field_name] = getattr(obj, field_name)

        return data

    def get_form(self, request_handler):
        form = modelform_factory(self, self.model)
        return form

    async def save_model(self, request_handler, form, obj=None):
        if obj:
            for field in form._fields:
                if field in obj._meta.m2m_fields:
                    continue
                setattr(obj, field, getattr(form, field).data)
            await obj.save()
        else:
            data = {}
            for field, value in form.data.items():
                if field not in self.model._meta.m2m_fields:
                    data[field] = value

            obj = await self.model.create(**data)

        await self.save_m2m(request_handler, form, obj)

        return obj

    async def save_m2m(self, request_handler, form, obj):
        for field in form._fields:
            if not field in obj._meta.m2m_fields:
                continue

            await obj.fetch_related(field)

            model_field = getattr(obj, field)

            current = {related.id for related in model_field}

            data = set(getattr(form, field).data)

            to_add = set()
            for id in data:
                if id not in current:
                    to_add.add(await model_field.remote_model.get(id=id))

            to_remove = {related for related in model_field if related.id in current - data}

            if len(to_add):
                await model_field.add(*to_add)

            if len(to_remove):
                await model_field.remove(*to_remove)
