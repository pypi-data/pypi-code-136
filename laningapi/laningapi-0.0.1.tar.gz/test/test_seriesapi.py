import pytest
from lib.mock import http_mock
from laningapi import Series

@pytest.fixture(scope='function', autouse=True)
async def func_scope():
    pass

@pytest.mark.anyio
async def test_submit_1():
    with http_mock() as mock:
        mock.register_once('/program_video/submit', {
            "code": 0,
            "msg": "",
            "data": {
                "id": 100,
            }
        })

        api = Series("http://mock")
        id = api.submit(bucket_name='face', realpath='/2022-10/01/112.mp4', filename='乱世风云/01.mp4')
        assert id==100

        histories = mock.get_histories(path='/program_video/submit')
        # print(histories)
        assert len(histories)==1
        assert histories[0]['param']=={
            'bucket_name': 'face', 
            'realpath': '/2022-10/01/112.mp4', 
            'filename': '乱世风云/01.mp4'
        }

@pytest.mark.anyio
async def test_submit_fail():
    with http_mock() as mock:
        mock.register_once('/program_video/submit', {
            "code": 1,
            "msg": ""
        })

        api = Series("http://mock")
        try:
            id = api.submit(bucket_name='face', realpath='/2022-10/01/112.mp4', filename='乱世风云/01.mp4')

            assert 1==0, '没有抛出异常'
        except Exception as e:
            #print(e)
            pass

@pytest.mark.anyio
async def test_submit_huashu_1():
    with http_mock() as mock:
        mock.register_once('/program_video/huashu/submit', {
            "code": 0,
            "msg": "",
            "data": {
                "id": 100,
            }
        })

        api = Series("http://mock")
        id = api.submit_by_huashu(bucket_name='face', realpath='/2022-10/01/112.mp4', filename='乱世风云/01.mp4', id="xxx", source="huashu")
        assert id==100

        histories = mock.get_histories(path='/program_video/huashu/submit')
        # print(histories)
        assert len(histories)==1
        assert histories[0]['param']=={
            'id': 'xxx',
            'source': 'huashu',
            'bucket_name': 'face', 
            'realpath': '/2022-10/01/112.mp4', 
            'filename': '乱世风云/01.mp4'
        }

@pytest.mark.anyio
async def test_submit_huashu_fail():
    with http_mock() as mock:
        mock.register_once('/program_video/huashu/submit', {
            "code": 1,
            "msg": ""
        })

        api = Series("http://mock")
        try:
            id = api.submit_by_huashu(bucket_name='face', realpath='/2022-10/01/112.mp4', filename='乱世风云/01.mp4', id="xxx", source="huashu")

            assert 1==0, '没有抛出异常'
        except Exception as e:
            pass

@pytest.mark.anyio
async def test_add_urls_1():
    with http_mock() as mock:
        mock.register_once('/program_video/add_urls', {
            "code": 0,
            "msg": "",
            "data": {
                "result": [1,2,3],
            }
        })

        urls = [
            {
                'url': 'http://w/1.mp4',
                'title': 'D01'
            },
            {
                'url': 'http://w/2.mp4',
                'title': 'D02'
            },
            {
                'url': 'http://w/3.mp4',
                'title': 'D03'
            },
        ]

        api = Series("http://mock")
        ret = api.add_urls(7, urls)
        assert ret==[1,2,3]

        histories = mock.get_histories(path='/program_video/add_urls')
        # print(histories)
        assert len(histories)==1
        assert histories[0]['param']=={
            'program_id': 7,
            'urls': ["http://w/1.mp4||D01", "http://w/2.mp4||D02", "http://w/3.mp4||D03"],
        }

@pytest.mark.anyio
async def test_submit_by_copy_1():
    with http_mock() as mock:
        mock.register_once('/program_video/submit_by_copy', {
            "code": 0,
            "msg": "",
            "data": {
                "id": 100,
            }
        })

        api = Series("http://mock")
        id = api.submit_by_copy(program_id=10, realpath='/2022-10/01/112.mp4', filename='乱世风云/01.mp4')
        assert id==100

        histories = mock.get_histories(path='/program_video/submit_by_copy')
        # print(histories)
        assert len(histories)==1
        assert histories[0]['param']=={
            'program_id': 10, 
            'realpath': '/2022-10/01/112.mp4', 
            'filename': '乱世风云/01.mp4'
        }