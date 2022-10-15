#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022-08-25
# @Author  : wuxiangbin
# @Site    : www.0-9.ink
# @File    : test.py
# @Software: orm
# @Function:
import datetime
import json
import time
import unittest

from bson import ObjectId

from zawn_orm import field
from zawn_orm import model
from zawn_orm.impl.mongodb import MongoDB
from zawn_orm.tool import datetime_format, MakeID

with open('../uri.json', 'rb') as fp:
    config = json.load(fp)

test_json = {
    'id': ObjectId(),
    'name': MakeID.next(''),
    'height': 180.5,
    'create_time': '2022-01-01T00:00:00.000+0800',
    'balance': '100.00',
    'enabled': True,
    'object_field': {
        's_id': '11',
        's_name': 11,
        's_height': '181.5',
        's_create_time': '2020-01-01T00:00:00.000+0800',
        's_balance': '200.00',
        's_enabled': 1,
    },
    'array_field': [
        {
            's_id': '11',
            's_name': 11,
            's_height': '181.5',
            's_balance': '200.00',
            's_enabled': 1,
            'b': 123,
        },
        {
            's_id': '110',
            's_name': 110,
            's_height': '185.5',
            's_balance': '250.00',
            's_enabled': 0,
            'b': lambda x: x,
        },
    ],
}


class TestMongoDB(unittest.IsolatedAsyncioTestCase):

    async def init_database(self):
        database = MongoDB()
        database.connect(config['mongodb_uri'])
        model.Model.set_database(database)

    def init_class(self):
        class EmbeddedModel(model.Model):
            s_name = field.StringField()
            s_id = field.IntegerField()
            s_height = field.FloatField()
            s_create_time = field.DatetimeField()
            s_balance = field.DecimalField()
            s_enabled = field.BooleanField()

        class TestModel(model.Model):
            id = field.IDField(index=True)
            name = field.StringField(unique=True)
            height = field.FloatField()
            create_time = field.DatetimeField()
            balance = field.DecimalField()
            enabled = field.BooleanField()
            object_field = field.ObjectField(EmbeddedModel.load_fields())
            array_field = field.ArrayField(EmbeddedModel.load_fields())

        self.EmbeddedModel = EmbeddedModel
        self.TestModel = TestModel

    async def asyncSetUp(self) -> None:
        self.test_json = test_json
        await self.init_database()
        self.init_class()

    async def asyncTearDown(self) -> None:
        pass

    async def test__objects_equal(self):
        self.assertEqual(self.TestModel().table_name, 'test_model')
        self.assertEqual(self.EmbeddedModel().table_name, 'embedded_model')
        self.assertEqual(self.TestModel().table_name, 'test_model')
        self.assertEqual(self.TestModel(), self.TestModel(), '相同模型的objects返回对象应该相同')
        self.assertEqual(self.EmbeddedModel(), self.EmbeddedModel(), '相同模型的objects返回对象应该相同')
        self.assertNotEqual(self.TestModel(), self.EmbeddedModel(), '不同模型的objects返回对象应该不同')

    async def test__transform(self):
        now = datetime.datetime.now().astimezone()
        now_str = now.strftime(datetime_format)
        test_model = self.TestModel()
        test_json = self.test_json
        test_json['create_time'] = now_str

        data = test_model.objects().load(test_json)
        test_to_db = test_model.to_db(data)
        test_to_json = test_model.to_json(data)

        self.assertEqual(data['create_time'], now)
        self.assertEqual(test_to_db['create_time'], now)
        self.assertEqual(test_to_json['create_time'], now_str)

    async def test__write_and_read(self):
        now = datetime.datetime.now().astimezone()
        now_str = now.strftime(datetime_format)
        id_1 = int(now.timestamp())
        id_2 = id_1 + 1
        test_model = self.TestModel()
        test_json = self.test_json
        test_json['create_time'] = now_str
        test_json['id'] = id_1
        test_json['name'] = MakeID.next('')
        test_json_2 = test_json.copy()
        test_json_2['id'] = id_2
        test_json_2['name'] = MakeID.next('')

        operation_list = [
            test_model.new_operation('delete', {}, {}),
            test_model.new_operation('insert', {}, test_json),
            test_model.new_operation('update', {'id': id_1}, {'$inc': {'balance': 100}}),
            test_model.new_operation('insert', {}, test_json_2),
            test_model.new_operation('delete', {'id': id_2}, {}),
        ]
        result = await test_model.execute(operation_list)

        meta, data = await test_model.search({'$project': {'_id': 0, 'create_time': 1}})
        test_to_json = [test_model.to_json(i) for i in data]

        self.assertEqual(result[test_model.table_name]['insert'], 2)
        self.assertGreaterEqual(result[test_model.table_name]['update'], 0)
        self.assertGreater(meta['total'], 0)
        self.assertTrue(test_to_json[0]['create_time'].startswith(now_str[:10]))
        self.assertIsNone(test_to_json[0].get('id'))

    async def test__quick_write_and_read(self):
        now = datetime.datetime.now().astimezone()
        now_str = now.strftime(datetime_format)
        test_model = self.TestModel()
        test_json = self.test_json
        test_json['create_time'] = now_str
        test_json['name'] = MakeID.next('')

        delete_result_0 = await test_model.delete({})
        insert_result = await test_model.insert(test_json, assert_dict={'test_model': {'insert': 1}})
        update_result = await test_model.update({'id': test_json['id']}, {'name': 'set_name', '$inc': {'balance': 55}})
        one_data = await test_model.find_one({})
        meta, data = await test_model.search(
            {'$filter': [
                {'$group': {'_id': '$name', 'count': {'$sum': '$balance'}}},
            ]},
            raw=True,
        )
        delete_result_1 = await test_model.delete({}, assert_dict={'test_model': {'delete': 1}})
        delete_result_2 = await test_model.delete({}, assert_dict={'test_model': {'delete': 0}})

        self.assertIn('id', one_data)
        self.assertGreaterEqual(meta['total'], 1)
        self.assertGreaterEqual(data[0]['count'], 1)
        self.assertEqual(insert_result['insert'], 1)
        self.assertGreaterEqual(update_result['update'], 1)
        self.assertIn('delete', delete_result_1)
        self.assertIn('delete', delete_result_2)


if __name__ == '__main__':
    unittest.main()
