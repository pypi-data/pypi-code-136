import json

from scrapy.utils.misc import load_object
from scrapy.utils.serialize import ScrapyJSONEncoder
from twisted.internet.threads import deferToThread
from scrapy_swarm.nsq import NsqWriter
from . import connection, defaults


default_serialize = ScrapyJSONEncoder().encode


class RedisPipeline(object):
    """Pushes serialized item into a redis list/queue

    Settings
    --------
    REDIS_ITEMS_KEY : str
        Redis key where to store items.
    REDIS_ITEMS_SERIALIZER : str
        Object path to serializer function.

    """

    def __init__(self, server,
                 bot,
                 key=defaults.PIPELINE_KEY,
                 serialize_func=default_serialize):
        """Initialize pipeline.

        Parameters
        ----------
        server : StrictRedis
            Redis client instance.
        key : str
            Redis key where to store items.
        serialize_func : callable
            Items serializer function.

        """
        self.server = server
        self.key = key
        self.bot = bot
        self.serialize = serialize_func

    @classmethod
    def from_settings(cls, settings):
        params = {
            'server': connection.from_settings(settings),
            'bot': settings.get("BOT_NAME", 'bot')
        }
        if settings.get('REDIS_ITEMS_KEY'):
            params['key'] = settings['REDIS_ITEMS_KEY']
        if settings.get('REDIS_ITEMS_SERIALIZER'):
            params['serialize_func'] = load_object(
                settings['REDIS_ITEMS_SERIALIZER']
            )

        return cls(**params)

    @classmethod
    def from_crawler(cls, crawler):
        return cls.from_settings(crawler.settings)

    def process_item(self, item, spider):
        return deferToThread(self._process_item, item, spider)

    def _process_item(self, item, spider):

        key = self.item_key(item, spider)
        data = self.serialize(item)

        # data = self.serialize(item)
        data = json.loads(data)
        data['spider'] = spider.name
        data['bot'] = self.bot
        # ok = NsqWriter.push(topic='scrapy', data=data)
        # key = f"queue:scrapy:{self.bot}:{spider.name}"
        key = f"queue:scrapy"
        self.server.lpush(key, json.dumps(data))
        return item

    def item_key(self, item, spider):
        """Returns redis key based on given spider.

        Override this function to use a different key depending on the item
        and/or spider.

        """
        return self.key % {'spider': spider.name}


class NsqPipeline(object):
    def __init__(self, bot, serialize_func=default_serialize):
        self.serialize = serialize_func
        self.bot = bot
        pass

    @classmethod
    def from_settings(cls, settings):
        params = {
            'bot': settings.get("BOT_NAME", 'bot-default')
        }
        return cls(**params)

    @classmethod
    def from_crawler(cls, crawler):
        return cls.from_settings(crawler.settings)

    def process_item(self, item, spider):
        return deferToThread(self._process_item, item, spider)

    def _process_item(self, item, spider):
        # key = self.item_key(item, spider)
        data = self.serialize(item)
        data = json.loads(data)
        data['spider'] = spider.name
        data['bot'] = self.bot
        ok = NsqWriter.push(topic='scrapy', data=data)
        print(f"nsq 成功发送到scrapy [{ok}]")
        # self.server.rpush(key, data)
        return item

