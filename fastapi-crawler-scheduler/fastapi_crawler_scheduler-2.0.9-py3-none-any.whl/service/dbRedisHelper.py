import time
import json
from typing import Union

from redis import StrictRedis


def standard_time() -> str:
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(time.time())))


class DbRedisHelper(object):
    """
    操作redis的类

    :param str project_name: 项目名字，主要区分不同项目
    :param bool ssl: redis 的 ssl
    """

    def __init__(
            self,
            project_name: str,
            ssl: bool,
            redis_host: str = "127.0.0.1",
            redis_port: int = 6379,
            username: str = None,
            password: str = None,

    ) -> None:
        self.project_name = project_name
        self.connection = StrictRedis(
            host=redis_host,
            port=redis_port,
            username=username,
            password=password,
            decode_responses=True,
            ssl=ssl,
        )
        self.prefix = f'{self.project_name}:lock'

    def __del__(self) -> None:
        self.connection.close()

    def acquire(self, lock_name: str, expire_time: int = None) -> bool:
        '''
        加锁
        :param lock_name:  加锁键
        :param expire_time: 锁过期时间
        :return: bool
        '''
        lock_key = f'{self.prefix}:{lock_name}'
        lock_value = standard_time()
        if expire_time is None:
            expire_time = 10
        if self.connection.setnx(lock_key, lock_value):
            self.connection.expire(lock_key, expire_time)
            return True
        else:
            if self.connection.ttl(lock_key) == -1:
                self.connection.expire(lock_key, expire_time)
            return False

    def lock_exists(self, lock_name: str) -> int:
        '''
        查询键是否存在
        :param lock_name: 键名称
        :return:
        '''
        return self.connection.exists(lock_name)

    def release(self, lock_name: str) -> None:
        '''
        释放锁
        :param lock_name:
        :return:
        '''

        lock_key = f'{self.prefix}:{lock_name}'
        self.connection.delete(lock_key)

    def process_acquire(self, lock_name: str, lock_value: str = None, expire_time: int = None) -> None:
        '''
        进程锁
        :param lock_name: 锁名
        :param lock_value: 锁值
        :param expire_time: 过期时间
        :return:
        '''
        if lock_value is None:
            lock_value = standard_time()
        if expire_time is None:
            expire_time = 15
        if self.connection.setnx(lock_name, lock_value):
            self.connection.expire(lock_name, expire_time)
        else:
            self.connection.expire(lock_name, expire_time)

    def delete_key(self, lock_name: str) -> int:
        '''
        删除键
        :param lock_name: 键名
        :return:
        '''
        return self.connection.delete(lock_name)

    def from_key_get_value(self, key_name: str) -> Union[dict, None]:
        '''
        获取键对应的值
        :param key_name:
        :return:
        '''
        try:
            return json.loads(self.connection.get(key_name))
        except:
            return None

    def get_tasks(self, keys: list[str], is_load: bool = True) -> dict:
        '''
        获取键值对
        :param keys: 键列表
        :param is_load: 是否进行json.loads的
        :return:
        '''
        values = self.connection.mget(keys)
        if is_load:
            values = []
            for value in self.connection.mget(keys):
                if value is not None:
                    value = json.loads(value)
                values.append(value)
        return dict(zip(keys, values))

    def get_proces_info(self) -> list:
        '''
        获取进程信息
        :return:
        '''
        return self.connection.keys(pattern=f'{self.project_name}:node:*')

    def get_backend_task(self) -> list:
        '''
        获取当前后端任务
        :return:
        '''
        return self.connection.keys(pattern=f'{self.project_name}:backend:*')

    def get_all_task(self) -> list:
        '''
        获取当前所有异步任务
        :return:
        '''
        return self.connection.keys(pattern=f'{self.project_name}:all:*')

    def get_insert_task(self) -> list:
        '''
        获取当前插入任务
        :return:
        '''
        return self.connection.keys(pattern=f'{self.project_name}:insert:*')

    def get_delete_task(self) -> list:
        '''
        获取当前删除任务
        :return:
        '''
        return self.connection.keys(pattern=f'{self.project_name}:delete:*')

    def get_update_task(self) -> list:
        '''
        获取当前更新任务
        :return:
        '''
        return self.connection.keys(pattern=f'{self.project_name}:update:*')

    def string_set(self, key: str, value: str) -> bool:
        '''
        向redis插入任务
        :param key:
        :param value:
        :return:
        '''
        return self.connection.set(key, value)

    def get_stores_job_task(self) -> list:
        '''
        获取apscheduler存储在redis的所有任务
        :return:
        '''
        return self.connection.keys(pattern=f'{self.project_name}:apscheduler:jobs:*')

    def get_stores_job_run_time_task(self) -> list:
        '''
        获取apscheduler存储在redis的所有任务
        :return:
        '''
        return self.connection.keys(pattern=f'{self.project_name}:apscheduler:run_times:*')
