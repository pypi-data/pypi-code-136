from enum import Enum
from typing import Union, Any, List
from fastapi import APIRouter, Body, Request, Depends
from tortoise.queryset import QuerySet

from .model import BaseModel
from .response_code import ListApiOut, BaseApiOut, ItemListSchema


class Order(Enum):
    asc: str = ''
    desc: str = '-'


class ModelCrud(APIRouter):
    def __init__(self, model: Union[BaseModel, Any],
                 schema_list=None,
                 schema_create=None,
                 schema_read=None,
                 schema_update=None,
                 schema_delete=None,
                 schema_filters=None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model
        self.schema_list = schema_list or model.schema_list()
        self.schema_read = schema_read or model.schema_read()
        self.schema_update = schema_update or model.schema_update()
        self.schema_create = schema_create or model.schema_create()
        self.schema_delete = schema_delete or model.schema_delete()
        self.schema_filters = schema_filters or model.schema_filters()
        self.register_crud()

    @classmethod
    def pre_create(cls, item: dict) -> dict:
        return item

    @classmethod
    def pre_create_all(cls, items: list):
        for item in items:
            yield cls.pre_create(item.dict())

    @classmethod
    def pre_update(cls, item: dict) -> dict:
        return item

    @classmethod
    def pre_list(cls, queryset: QuerySet, item: dict) -> QuerySet:
        """
        数据预处理：搜索字段
        :param queryset:
        :param item:
        :return:
        """
        filter_field = {f'{k}__icontains': v for k, v in item.items() if v}
        return queryset.filter(**filter_field)

    def register_crud(self):
        # model_name =
        schema_create = self.schema_create
        schema_update = self.schema_update
        schema_filters = self.schema_filters

        @self.post('/list', response_model=ListApiOut[self.schema_list])
        async def handle_list(request: Request, filters: schema_filters, page: int = 1, pagesize: int = 10, sort='id',
                              order: Order = Order.desc, ):
            data = ItemListSchema(items=[])

            queryset = self.model.filter(is_delete=False)
            queryset = self.pre_list(queryset, filters.dict())
            queryset = queryset.order_by(f'{order.value}{sort}')
            data.items = await self.schema_list.from_queryset(queryset.offset((page - 1) * pagesize).limit(pagesize))
            data.total = await queryset.count()
            data.query = request.query_params
            data.filter = filters
            return ListApiOut(data=data)

        @self.get('/read/{item_id}', response_model=BaseApiOut[self.schema_read])
        async def handle_read(item_id):
            data = await self.model.find_one(id=item_id)
            data = await self.schema_read.from_tortoise_orm(data)
            return BaseApiOut(data=data)

        @self.post("/create", response_model=BaseApiOut[self.schema_create])
        async def handle_create(item: schema_create):
            item = self.pre_create(item.dict())
            new_item = await self.model.create_one(item)
            data = await self.schema_create.from_tortoise_orm(new_item)
            return BaseApiOut(data=data)

        @self.post('/create/all', response_model=BaseApiOut)
        async def handle_create_all(items: List[schema_create]):
            items = self.pre_create_all(items)
            await self.model.bulk_create([self.model(**item) for item in items], ignore_conflicts=True)
            return BaseApiOut(msg='批量创建成功')
            pass

        @self.put("/{item_id}", response_model=BaseApiOut[schema_update])
        async def handle_update(item_id: str, item: schema_update):
            item = self.pre_update(item.dict(exclude_unset=True))
            updated_item = await self.model.update_one(item_id, item)
            data = await schema_update.from_queryset_single(updated_item)
            return BaseApiOut(data=data)

        @self.delete("/{item_ids}", description='删除1条或多条数据example：1,2',
                     response_model=BaseApiOut[self.schema_delete])
        async def handle_delete(item_ids: str):
            ids = item_ids.split(',')
            data = await self.model.delete_many(ids)
            return BaseApiOut(data=data)

        # @self.post('/search', response_model=ListApiOut[schema_filters])
        # async def handle_search(filters: schema_filters):
        #     data = ItemListSchema(items=[])
        #     queryset = self.model.filter(is_delete=False, **filters.dict())
        #     data.items = await schema_filters.from_queryset(queryset.all())
        #     data.total = await queryset.count()
        #     data.filter = filters
        #     return ListApiOut(data=data)

        return self


__all__ = [
    'ModelCrud'
]
