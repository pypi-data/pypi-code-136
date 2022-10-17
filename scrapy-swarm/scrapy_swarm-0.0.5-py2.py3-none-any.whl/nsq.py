import asyncio
import json
from queue import Queue
import threading
import time
import logging
import nsq
import requests
import tornado.ioloop
from scrapy_swarm.utils import TextColor

msq_params = {
    'lookupd_poll_interval': 30,
    'lookupd_connect_timeout': 100000,
    'lookupd_request_timeout':100000,
    'max_tries': 10
}

SETTINGS_PARAMS_MAP = {
    'NSQ_ADDRESS': 'nsqd_tcp_addresses',
    'NSQ_TOPIC': 'topic',
    'NSQ_CHANNEL': 'channel',
}

logger = logging.getLogger(__name__)

def synchronized(func):
    func.__lock__ = threading.Lock()

    def lock_func(*args, **kwargs):
        with func.__lock__:
            return func(*args, **kwargs)
    return lock_func


# class NsqWriter:
#
#     __writer_instance = None
#     __writer_thread = None
#     __topic_writer_queue = Queue(10000)
#
#     @staticmethod
#     def __finish_pub(conn, data):
#         print(data)
#         print(conn)
#         pass
#
#     @classmethod
#     def push(cls, topic: str = "default-topic", data: dict= {}):
#         wrapper = {
#             'topic': topic,
#             "data": data
#         }
#         try:
#             cls.__topic_writer_queue.put(wrapper, block=False)
#         except BaseException as e:
#             logger.warn(f"{TextColor.WARNING}WARNING:__queue队列塞满了  {type(e)}{TextColor.ENDC}")
#
#     @staticmethod
#     async def __to_nsq_task():
#         await asyncio.sleep(1)  # very need or SendError: no open connections (None)
#         queue1 = NsqWriter.__topic_writer_queue
#         while True:
#             try:
#                 # 一直等待
#                 task: dict = queue1.get(block=True, timeout=60)
#                 if not task:
#                     continue
#                 topic = task['topic']
#                 data = task['data']
#                 data = json.dumps(data, ensure_ascii=False)
#                 await asyncio.sleep(1)
#                 await NsqWriter.__writer_instance.pub(
#                     topic,
#                     data.encode(),
#                     NsqWriter.__finish_pub)
#             except Exception as e:
#                 # logger.warn(f"{TextColor.WARNING}WARNING: {type(e)}{TextColor.ENDC}")
#                 pass
#
#     @classmethod
#     def __thread_writer_body(cls, url, loop):
#         asyncio.set_event_loop(loop)
#         cls.__writer_instance = nsq.Writer(nsqd_tcp_addresses=[url], reconnect_interval=10)
#         # loop = asyncio.get_event_loop()
#         # AsyncIOMainLoop().install()
#         loop.create_task(cls.__to_nsq_task())
#         loop.run_forever()
#
#     @classmethod
#     @synchronized
#     def start(cls, url):
#         if cls.__writer_instance is None:
#             loop = asyncio.new_event_loop()
#             cls.__writer_thread = threading.Thread(target=cls.__thread_writer_body, args=(url, loop))
#             cls.__writer_thread.start()
#             return cls.__writer_thread
#         else:
#             return cls.__writer_thread
#
#     @classmethod
#     def is_instance(cls):
#         return cls.__writer_thread is None
class NsqWriter:
    __writer_instance = None
    __writer_thread = None
    __url = None
    @staticmethod
    def __finish_pub(conn, data):
        print(data)
        print(conn)
        pass

    @classmethod
    def push(cls, topic: str = "default-topic", data: dict= {}):
        data = json.dumps(data)
        resp = requests.post(
            "%s/pub?topic=%s" % (cls.__url, topic),
            data=data)
        return resp.text

    @classmethod
    @synchronized
    def start(cls, url):
        cls.__url = f"http://{url[:url.rfind(':')]}:4151"

    @classmethod
    def is_instance(cls):
        return cls.__url is None


class NsqReader:
    __reader_thread = None

    @classmethod
    def __thread_reader_body(cls, kwargs, loop):
        asyncio.set_event_loop(loop)
        reader = nsq.Reader(
            message_handler=cls.__handler, **kwargs)
        tornado.ioloop.IOLoop.instance().start()

    @classmethod
    @synchronized
    def start(cls, kwargs):
        if cls.__reader_thread is None:
            loop = asyncio.new_event_loop()
            cls.__reader_thread = threading.Thread(target=cls.__thread_reader_body, args=(dict(**kwargs), loop))
            cls.__reader_thread.start()
            return cls.__reader_thread
        else:
            return cls.__reader_thread

    # 监听到的消息
    @staticmethod
    def __handler(message: nsq.Message):
        print("ID:", str(message.id))
        print("body:", json.loads(message.body))
        try:
            data = json.loads(message.body)
            to = data['to']
            payload = data['data']
            spider = NsqHelper.spiders_map[to]
            call = getattr(spider, 'call_nsq', None)
            if callable(call):
                call(data=payload, ts=message.timestamp, id=message.id)
        except Exception as e:
            logger.error(f"{TextColor.FAIL}ERROR: {str(e)}{TextColor.ENDC}")
        return True

    @classmethod
    def is_instance(cls):
        return cls.__reader_thread is None


class NsqHelper:
    spiders_map = {}

    @staticmethod
    def __get_settings(settings):
        params = msq_params.copy()
        for source, dest in SETTINGS_PARAMS_MAP.items():
            val = settings.get(source)
            if val:
                params[dest] = val
        return params

    @classmethod
    def register(cls, redis_key, spider):
        cls.spiders_map[redis_key] = spider

    @classmethod
    def start(cls, settings):
        if NsqReader.is_instance() or NsqWriter.is_instance():
            NsqReader.start(cls.__get_settings(settings))
            NsqWriter.start(settings.get('NSQ_ADDRESS'))

    @classmethod
    def push_data(cls, data):
        if 'topic' in data and 'data' in data:
            NsqWriter.push(data)


