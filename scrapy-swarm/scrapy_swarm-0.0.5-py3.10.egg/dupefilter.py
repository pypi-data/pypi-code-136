import logging
import time

import redis
import scrapy
from scrapy.dupefilters import BaseDupeFilter
from scrapy.utils.request import request_fingerprint

from scrapy_swarm import defaults
from scrapy_swarm.connection import get_redis_from_settings
from scrapy_swarm.utils import fp
from scrapy_swarm.utils import CodeHelper
logger = logging.getLogger(__name__)


# TODO: Rename class to RedisDupeFilter.
class RFPDupeFilter(BaseDupeFilter):
    """
        Redis-based request duplicates filter.
        This class can also be used with default Scrapy's scheduler.
    """
    logger = logger

    def __init__(self, server, key, debug=False):
        """
            Initialize the duplicates filter.
            Parameters
            server : redis.StrictRedis The redis server instance.
            key : str Redis key Where to store fingerprints.
            debug : bool, optional Whether to log filtered requests.
        """
        self.server = server
        self.key = key
        self.debug = debug
        self.logdupes = True

    @classmethod
    def from_settings(cls, settings):
        """Returns an instance from given settings.

        This uses by default the key ``dupefilter:<timestamp>``. When using the
        ``scrapy_redis.scheduler.Scheduler`` class, this method is not used as
        it needs to pass the spider name in the key.

        Parameters
            settings : scrapy.settings.Settings

        Returns
            RFPDupeFilter  A RFPDupeFilter instance.
        """
        server = get_redis_from_settings(settings)
        # XXX: This creates one-time key. needed to support to use this
        # class as standalone dupefilter with scrapy's default scheduler
        # if scrapy passes spider on open() method this wouldn't be needed
        # TODO: Use SCRAPY_JOB env as default and fallback to timestamp.
        key = defaults.DUPEFILTER_KEY % {'timestamp': int(time.time())}
        debug = settings.getbool('DUPEFILTER_DEBUG')
        return cls(server, key=key, debug=debug)

    @classmethod
    def from_crawler(cls, crawler: scrapy.crawler.Crawler):
        """ Returns instance from crawler.
        Parameters
            crawler : scrapy.crawler.Crawler
        Returns
            RFPDupeFilter Instance of RFPDupeFilter.
        """
        return cls.from_settings(crawler.settings)

    def request_seen(self, request: scrapy.http.Request) -> bool:
        """
            Returns True if request was already seen.
            获取请求指纹并添加到redis的去重集合中去
            self.request_figerprints 就是一个指纹集合
        """
        fp = self.request_fingerprint(request)
        if fp is None:
            return False
        # This returns the number of values added, zero if already exists.
        # 注意很多地方  关机会清除这个key  导致重启爬虫  会重新爬取
        added = self.server.sadd(self.key, fp)
        self.server.expire(self.key, time=24*60*60, nx=True)

        return added == 0
        # bl 过滤优化  https://blog.csdn.net/bone_ace/article/details/53107018
        # fp = request_fingerprint(request)
        # if self.rd.sismember('fp', fp):
        #     return True
        # self.rd.sadd('fp', fp)

    @classmethod
    def remove_fp(cls, fp):
        cls.server.srem('fp', fp)

    @classmethod
    def del_fp_key(cls, fp):

        pass

    def request_fingerprint(self, request: scrapy.http.Request) -> str | None:
        """
            Returns a fingerprint for a given request.
        """
        # return request_fingerprint(request)
        meta = request.meta
        if 'fp' in meta:
            return fp(meta.get('fp'))
        else:
            return None

    @classmethod
    def from_spider(cls, spider):
        settings = spider.settings
        server = get_redis_from_settings(settings)
        dupe_filter_key = settings.get("SCHEDULER_DUPEFILTER_KEY", defaults.SCHEDULER_DUPEFILTER_KEY)
        # 修改dupe key
        key = dupe_filter_key % {'spider': spider.name, 'code': CodeHelper.now_code()}
        debug = settings.getbool('DUPEFILTER_DEBUG')
        return cls(server, key=key, debug=debug)

    def close(self, reason=''):
        """
            Delete data on close. Called by Scrapy's scheduler.
            Parameters
                reason : str, optional
        """
        # 关闭爬虫时不清除key   不能清除
        # self.clear()
        pass

    def clear(self):
        """Clears fingerprints data."""
        print("----\n--- clear")
        self.server.delete(self.key)

    def log(self, request: scrapy.http.Request, spider: scrapy.spiders.Spider):
        """
            Logs given request.
        """
        if self.debug:
            msg = "Filtered duplicate request: %(request)s"
            self.logger.debug(msg, {'request': request}, extra={'spider': spider})
        elif self.logdupes:
            msg = ("Filtered duplicate request %(request)s"
                   " - no more duplicates will be shown"
                   " (see DUPEFILTER_DEBUG to show all duplicates)")
            self.logger.debug(msg, {'request': request}, extra={'spider': spider})
            self.logdupes = False
