import redis


# For standalone use.
# 去重的键名key
DUPEFILTER_KEY = 'dupe_filter:%(timestamp)s'

# 定义的存储items的键名，spiders是爬虫的名称
PIPELINE_KEY = 'items:%(spider)s'

STATS_KEY = 'stats:%(spider)s'

# redis连接对象，是用于连接redis
REDIS_CLS = redis.StrictRedis

# 字符集编码
REDIS_ENCODING = 'utf-8'

# Sane connection defaults.
# redis的连接的参数
REDIS_PARAMS = {
    'socket_timeout': 30,
    'socket_connect_timeout': 30,
    'retry_on_timeout': True,
    'encoding': REDIS_ENCODING,
}
REDIS_CONCURRENT_REQUESTS = 16

# 队列的变量名，用于存储爬取的url队列
SCHEDULER_QUEUE_KEY = 'requests:%(spider)s'

# 优先级队列，用于规定队列的进出方式
SCHEDULER_QUEUE_CLASS = 'scrapy_swarm.queue.PriorityQueue'

# 用于去重的key，给request加指纹存储的地方
SCHEDULER_DUPEFILTER_KEY = 'filter:%(code)s:%(spider)s'

# 用于生成指纹的类
SCHEDULER_DUPEFILTER_CLASS = 'scrapy_swarm.dupefilter.RFPDupeFilter'

SCHEDULER_PERSIST = False

# 起始url对应的key
START_URLS_KEY = 'start_urls:%(name)s'

# 起始url的类型
START_URLS_AS_SET = False
START_URLS_AS_ZSET = False
MAX_IDLE_TIME = 0




