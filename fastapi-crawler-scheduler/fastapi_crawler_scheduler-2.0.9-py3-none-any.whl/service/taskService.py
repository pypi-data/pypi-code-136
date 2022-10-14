from typing import Callable, Dict
import os

from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.base import ConflictingIdError, JobLookupError
from apscheduler.util import datetime_to_utc_timestamp
from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every
from apscheduler.util import obj_to_ref

try:
    import cPickle as pickle
except ImportError:  # pragma: nocover
    import pickle

try:
    from redis import Redis
except ImportError:  # pragma: nocover
    raise ImportError('RedisJobStore requires redis installed')

from fastapi_crawler_scheduler.utils.exception import SchedulerError
from fastapi_crawler_scheduler.service.dbRedisHelper import DbRedisHelper
from fastapi_crawler_scheduler.service.baseScheduler import BaseScheduler
from fastapi_crawler_scheduler.utils.objectToString import handle_trigger
from fastapi_crawler_scheduler.utils.objectToString import handle_datetime


class TaskScheduler(object):

    def __init__(self,
                 app: FastAPI,
                 project_name: str,
                 uuid_number: str,
                 ssl: bool,
                 thread_pool_size: int = 10,
                 job_coalesce: bool = True,
                 job_max_instance: int = 1,
                 job_misfire_grace_time: int = 10,
                 redis_host: str = "127.0.0.1",
                 redis_port: int = 6379,
                 redis_username: str = None,
                 redis_password: str = None,
                 ):
        self.app = app
        self.ssl = ssl
        self.project_name = project_name
        self.uuid_number = uuid_number
        self.redis_host = redis_host
        self.redis_port = redis_port
        self.username = redis_username
        self.password = redis_password
        self.jobs_key = self.project_name + ':apscheduler:jobs:' + uuid_number + ":" + str(os.getpid())
        self.run_times_key = self.project_name + ':apscheduler:run_times:' + uuid_number + ":" + str(os.getpid())
        self.thread_pool_size = thread_pool_size
        self.job_coalesce = job_coalesce
        self.job_max_instance = job_max_instance
        self.job_misfire_grace_time = job_misfire_grace_time
        self.redis = Redis(
            host=self.redis_host,
            port=self.redis_port,
            username=self.username,
            password=self.password,
            decode_responses=True,
            ssl=ssl,
        )
        self.pickle_protocol = pickle.HIGHEST_PROTOCOL

        # 实现 scheduler 注册
        self.register_scheduler()
        self.register_redis_db = DbRedisHelper(
            project_name=self.project_name,
            redis_host=self.redis_host,
            redis_port=self.redis_port,
            username=self.username,
            password=self.password,
            ssl=self.ssl,
        )
        self.register_base_scheduler = BaseScheduler(
            project_name=self.project_name,
            redis_db=self.register_redis_db,
            scheduler=self.scheduler,
            uuid_number=self.uuid_number,
            redis_job_store=self.redis_job_store
        )
        self.register_async_task()

    def register_async_task(self) -> None:
        @repeat_every(seconds=5)
        def check_process() -> None:
            self.register_base_scheduler.check_process()

        @repeat_every(seconds=8)
        def check_scheduler_run() -> None:
            self.register_base_scheduler.run()

        @repeat_every(seconds=10)
        def check_redis_jobstores() -> None:
            self.register_base_scheduler.check_redis_jobstores()

        def scheduler_start():
            self.scheduler.start()

        def scheduler_shutdown():
            self.scheduler.shutdown()

        self.app.on_event("startup")(check_process)
        self.app.on_event("startup")(check_scheduler_run)
        self.app.on_event("startup")(check_redis_jobstores)
        self.app.on_event("startup")(scheduler_start)
        self.app.on_event("shutdown")(scheduler_shutdown)

    def add_job(self, job):
        if self.redis.hexists(self.jobs_key, job.id):
            raise ConflictingIdError(job.id)
        self.redis.hset(self.jobs_key, job.id, pickle.dumps(job.__getstate__(), self.pickle_protocol))
        if job.next_run_time:
            self.redis.zadd(self.run_times_key, {job.id: datetime_to_utc_timestamp(job.next_run_time)})

    def update_job(self, job):
        if not self.redis.hexists(self.jobs_key, job.id):
            raise JobLookupError(job.id)
        self.redis.hset(self.jobs_key, job.id, pickle.dumps(job.__getstate__(), self.pickle_protocol))
        if job.next_run_time:
            self.redis.zadd(self.run_times_key,
                            {job.id: datetime_to_utc_timestamp(job.next_run_time)})
        else:
            self.redis.zrem(self.run_times_key, job.id)

    def remove_job(self, job_id):
        if not self.redis.hexists(self.jobs_key, job_id):
            raise JobLookupError(job_id)
        self.redis.hdel(self.jobs_key, job_id)
        self.redis.zrem(self.run_times_key, job_id)

    def remove_all_jobs(self):
        self.redis.delete(self.jobs_key)
        self.redis.delete(self.run_times_key)

    def register_scheduler(self) -> None:
        redis_job_store = getattr(self.app, "redis_job_store", None)
        if redis_job_store is None:
            redis_job_store = RedisJobStore(
                host=self.redis_host,
                port=self.redis_port,
                username=self.username,
                password=self.password,
                jobs_key=self.jobs_key,
                run_times_key=self.run_times_key,
                ssl=self.ssl,
            )
            redis_job_store.add_job = self.add_job
            redis_job_store.update_job = self.update_job
            redis_job_store.remove_job = self.remove_job
            redis_job_store.remove_all_jobs = self.remove_all_jobs

        self.redis_job_store = redis_job_store
        setattr(self.app, "redis_job_store", self.redis_job_store)
        scheduler = getattr(self.app, "scheduler", None)
        if scheduler is None:
            scheduler = BackgroundScheduler()
            scheduler.configure(
                jobstores={
                    "default": self.redis_job_store
                },
                executors={
                    "default": ThreadPoolExecutor(
                        max_workers=self.thread_pool_size,
                    )
                },
                job_defaults={
                    "coalesce": self.job_coalesce,
                    "max_instance": self.job_max_instance,
                    "misfire_grace_time": self.job_misfire_grace_time,
                }
            )
        elif isinstance(scheduler, BackgroundScheduler):
            pass
        else:
            raise SchedulerError("FastAPI应用已经包含scheduler对象，但是该对象并非BackgroundScheduler")
        self.scheduler = scheduler
        setattr(self.app, "scheduler", self.scheduler)

    def add_task(
            self,
            func: Callable,
            job_id: str,
            trigger: str,
            crawler_info: Dict = None,
            **trigger_args
    ) -> None:
        '''
        :param trigger: interval 、 date or cron
        '''
        task_info = dict()
        task_info['func'] = obj_to_ref(func)
        task_info['job_id'] = job_id
        task_info['trigger'] = trigger
        task_info['crawler_info'] = crawler_info
        task_info['trigger_args'] = trigger_args
        self.register_base_scheduler.insert_task(task_info=task_info)

    def delete_task(
            self,
            job_id: str,
    ) -> None:
        self.register_base_scheduler.delete_task(job_id=job_id)

    def get_all_apscheduler_stores_jobs(self):
        redis_apscheduler_jobs_dict = dict()
        for apscheduler_stores_job_key in self.register_redis_db.get_stores_job_task():
            value_dict = dict()
            job_states_byte_dict = self.redis_job_store.redis.hgetall(apscheduler_stores_job_key)
            for job_states_key_byte, job_states_value_byte in job_states_byte_dict.items():
                job_states_key = job_states_key_byte.decode()
                job_states_value = pickle.loads(job_states_value_byte)
                # print(f"handle_before： {job_states_value}")
                if 'trigger' in job_states_value:
                    # todo: combining 情况下有问题
                    trigger = job_states_value['trigger'].__getstate__()
                    job_states_value['trigger'] = handle_trigger(trigger)
                if 'next_run_time' in job_states_value:
                    job_states_value['next_run_time'] = handle_datetime(agefield=job_states_value.get('next_run_time'))
                # print(f"handle_after： {job_states_value}")
                value_dict[job_states_key] = job_states_value
            redis_apscheduler_jobs_dict[apscheduler_stores_job_key] = value_dict
        return redis_apscheduler_jobs_dict

    def get_all_redis_tasks(self):
        all_tasks = dict()
        for all_task_key in self.register_redis_db.connection.keys(pattern=f'{self.project_name}:all:*'):
            value = self.register_redis_db.from_key_get_value(all_task_key)
            all_tasks[all_task_key] = value
        return all_tasks

    def get_all_redis_apscheduler_run_times(self):
        redis_apscheduler_run_time_dict = dict()
        for apscheduler_run_time_key in self.register_redis_db.get_stores_job_run_time_task():
            value_dict = dict()
            apscheduler_run_time_byte_list = self.redis_job_store.redis.zrange(
                apscheduler_run_time_key, 0, 4821384687, withscores=True)
            for job_states_key_byte, run_time__byte_timestamp in apscheduler_run_time_byte_list:
                job_states_key = job_states_key_byte.decode()
                value_dict[job_states_key] = run_time__byte_timestamp
            redis_apscheduler_run_time_dict[apscheduler_run_time_key] = value_dict
        return redis_apscheduler_run_time_dict

    def show_all_redis_key(self):
        return self.register_redis_db.connection.keys(pattern=f'{self.project_name}:*')

    def show_all_redis_nodes(self):
        node_dict = dict()
        for node_key in self.register_redis_db.connection.keys(pattern=f'{self.project_name}:node:*'):
            value = self.register_redis_db.connection.get(node_key)
            node_dict[node_key] = value
        return node_dict

    def show_all_redis_tasks(self):
        return self.get_all_redis_tasks()

    def show_all_scheduler_get_jobs(self):
        all_tasks = dict()
        for all_task_key in self.register_redis_db.connection.keys(pattern=f'{self.project_name}:running_job:*'):
            value = dict()
            value['approximate_start_time'] = self.register_redis_db.connection.get(all_task_key)
            value['data_ttl'] = self.register_redis_db.connection.ttl(all_task_key)
            all_tasks[all_task_key] = value
        return all_tasks

    def show_all_apscheduler_stores_jobs(self):
        return self.get_all_apscheduler_stores_jobs()

    def show_all_redis_apscheduler_run_times(self):
        return self.get_all_redis_apscheduler_run_times()

    def show_all_task_not_in_stores_jobs(self):
        problem_task = {}
        redis_apscheduler_job_id_list = []
        for redis_apscheduler_jobs_value in self.get_all_apscheduler_stores_jobs().values():
            redis_apscheduler_job_id_list.extend(redis_apscheduler_jobs_value.keys())
        for all_key, all_value in self.get_all_redis_tasks().items():
            if all_value.get('job_id') not in redis_apscheduler_job_id_list:
                problem_task[all_key] = all_value
        return problem_task

    def show_all_task_not_in_stores_run_times(self):
        problem_task = {}
        redis_apscheduler_run_time_job_id_list = []
        for redis_apscheduler_job_run_time_value in self.get_all_redis_apscheduler_run_times().values():
            redis_apscheduler_run_time_job_id_list.extend(redis_apscheduler_job_run_time_value.keys())
        for all_key, all_value in self.get_all_redis_tasks().items():
            if all_value.get('job_id') not in redis_apscheduler_run_time_job_id_list:
                problem_task[all_key] = all_value
        return problem_task

    def clear_project_keys(self):
        for key in self.register_redis_db.connection.keys(pattern=f'{self.project_name}:*'):
            self.register_redis_db.connection.delete(key)
        return True
