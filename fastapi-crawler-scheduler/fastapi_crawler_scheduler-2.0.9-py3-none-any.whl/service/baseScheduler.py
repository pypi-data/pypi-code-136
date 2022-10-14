import os
import json
import six
import traceback
from typing import Dict

from uhashring import HashRing
from apscheduler.jobstores.redis import RedisJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.util import ref_to_obj

from fastapi_crawler_scheduler.service.dbRedisHelper import DbRedisHelper, standard_time


class BaseScheduler(object):
    """
    任务管理和自身的异步任务
    :param DbRedisHelper对象 redis_db: DbRedisHelper对象
    :param BackgroundScheduler对象 scheduler: BackgroundScheduler对象
    :param str uuid_number: uuid
    :param str project_name: 项目名字，主要区分不同项目
    :param RedisJobStore对象 redis_job_store: RedisJobStore对象
    """

    def __init__(
            self,
            redis_db: DbRedisHelper,
            scheduler: BackgroundScheduler,
            uuid_number: str,
            project_name: str,
            redis_job_store: RedisJobStore,

    ) -> None:
        self.uuid_number = uuid_number
        self.project_name = project_name
        self.redis_db = redis_db
        self.scheduler = scheduler
        self.process_id_list = []
        self.redis_job_store = redis_job_store

    def scheduler_add_job(
            self,
            **task_info
    ) -> None:
        '''
        向 apscheduler 中添加一个任务
        :param crawler_info: 任务参数
        :return:
        '''
        try:
            func = ref_to_obj(task_info.get('func'))
        except Exception as e:
            print(f"scheduler_add_job   函数错误 ：{e}")
            print(traceback.format_exc())
            return
        trigger = task_info.get('trigger')
        job_id = task_info.get('job_id')
        crawler_info = task_info.get('crawler_info')
        trigger_args = task_info.get('trigger_args')
        if self.redis_job_store.redis.hexists(self.redis_job_store.jobs_key, job_id):
            self.redis_job_store.remove_job(job_id=job_id)
        self.scheduler.add_job(
            func=func,
            id=job_id,
            trigger=trigger,
            kwargs=crawler_info,
            **trigger_args,
        )

    def check_process(self) -> None:
        '''
        检查进程
        :return:
        '''
        self.redis_db.process_acquire(f'{self.project_name}:node:{self.uuid_number}:{os.getpid()}')

    def get_process_list(self) -> list:
        '''
        获取当前项目所有进程信息
        :return:
        '''
        return self.redis_db.get_proces_info()

    def process_check_count(self, process_id: int, check_key: str) -> None:
        '''
        检查任务策略
        :param process_id: 进程pid
        :param check_key:  待检查任务键
        :return:
        '''
        if process_id not in self.process_id_list:
            if self.redis_db.acquire(lock_name=check_key):
                check_value = self.redis_db.from_key_get_value(key_name=check_key)
                if check_value is None:
                    return None
                check_process_number = check_value.get('check_process_number')
                if check_process_number is None:
                    check_process_number = 1
                else:
                    check_process_number += 1
                if check_process_number >= 2:
                    self.redis_db.delete_key(lock_name=check_key)
                else:
                    check_value['check_process_number'] = check_process_number
                    self.redis_db.string_set(key=check_key, value=json.dumps(check_value, ensure_ascii=False))
                self.redis_db.release(lock_name=check_key)

    def check_backend_task(self) -> None:
        '''
        检查后端任务
        :return:
        '''
        node_process_id_list = self.get_process_list()
        self.process_id_list = [int(str(node_id).strip().split(':')[-1]) for node_id in node_process_id_list]
        # 处理后端操作
        hr = HashRing(nodes=node_process_id_list)
        for backend_key in self.redis_db.get_backend_task():
            backend_info = self.redis_db.from_key_get_value(backend_key)
            if backend_info is None:
                continue
            lock_all_backend_key = f'{self.redis_db.prefix}:all:{backend_info["job_id"]}'
            all_backend_key = f'{self.project_name}:all:{backend_info["job_id"]}'
            if not self.redis_db.lock_exists(lock_name=lock_all_backend_key):
                process_node_id = hr.get_node(backend_info["job_id"])
                backend_info['process_node_id'] = process_node_id
                self.redis_db.string_set(key=all_backend_key, value=json.dumps(backend_info, ensure_ascii=False))
                self.redis_db.delete_key(lock_name=backend_key)

    def check_all_task(self) -> None:
        '''
        检查所有任务
        :return:
        '''
        node_process_id_list = self.get_process_list()
        self.process_id_list = [int(str(node_id).strip().split(':')[-1]) for node_id in node_process_id_list]
        hr = HashRing(nodes=node_process_id_list)
        # 处理 all_task
        for all_key in self.redis_db.get_all_task():
            all_value = self.redis_db.from_key_get_value(all_key)
            if all_value is None:
                continue
            if self.redis_db.acquire(lock_name=all_key):
                redis_process_node_id = all_value["process_node_id"]
                new_process_node_id = hr.get_node(all_value["job_id"])
                if new_process_node_id == redis_process_node_id:
                    process_id = int(str(redis_process_node_id).strip().split(':')[-1])
                    # 进程没变化
                    if all_value['is_change'] == 1:
                        next_key = f'{self.project_name}:{all_value["operation"]}:{self.uuid_number}:{all_value["job_id"]}:{process_id}'
                        self.redis_db.string_set(key=next_key, value=json.dumps(all_value, ensure_ascii=False))
                        all_value["is_change"] = 0
                        self.redis_db.string_set(key=all_key, value=json.dumps(all_value, ensure_ascii=False))
                    else:
                        pass
                else:
                    # 进程有变化
                    new_process_id = int(str(new_process_node_id).strip().split(':')[-1])
                    redis_process_id = int(str(redis_process_node_id).strip().split(':')[-1])
                    delete_key = f'{self.project_name}:delete:{self.uuid_number}:{all_value["job_id"]}:{redis_process_id}'
                    all_value["details"] = "删除任务"
                    self.redis_db.string_set(key=delete_key, value=json.dumps(all_value, ensure_ascii=False))
                    all_value["process_node_id"] = new_process_node_id
                    if all_value['operation'] == 'delete':
                        # 无需向下一步添加任务
                        pass
                    else:
                        insert_key = f'{self.project_name}:insert:{self.uuid_number}:{all_value["job_id"]}:{new_process_id}'
                        all_value["details"] = "进程变化，新增任务"
                        self.redis_db.string_set(key=insert_key, value=json.dumps(all_value, ensure_ascii=False))
                    all_value["is_change"] = 0
                    self.redis_db.string_set(key=all_key, value=json.dumps(all_value, ensure_ascii=False))
                self.redis_db.release(lock_name=all_key)

    def check_insert_task(self) -> None:
        '''
        检查新增任务
        :return:
        '''
        for insert_key in self.redis_db.get_insert_task():
            insert_value = self.redis_db.from_key_get_value(insert_key)
            if insert_value is None:
                continue
            try:
                process_node_id = insert_value['process_node_id']
                apscheduler_id = insert_value['job_id']
                process_id = int(str(process_node_id).strip().split(':')[-1])
                if os.getpid() == process_id:
                    if self.scheduler.get_job(job_id=apscheduler_id):
                        self.scheduler.remove_job(job_id=apscheduler_id)
                    self.scheduler_add_job(**insert_value)
                    self.redis_db.delete_key(lock_name=insert_key)
                else:
                    pass
                    self.process_check_count(process_id=process_id, check_key=insert_key)
            except Exception as e:
                print(f"check_insert_task 函数 错误 ：{e}")
                print(traceback.format_exc())

    def check_update_task(self) -> None:
        '''
        检查更新任务
        :return:
        '''
        for update_key in self.redis_db.get_update_task():
            update_value = self.redis_db.from_key_get_value(update_key)
            if update_value is None:
                continue
            try:
                process_node_id = update_value['process_node_id']
                apscheduler_id = update_value['job_id']
                process_id = int(str(process_node_id).strip().split(':')[-1])
                if os.getpid() == process_id:
                    if self.scheduler.get_job(job_id=apscheduler_id):
                        self.scheduler.remove_job(job_id=apscheduler_id)
                    self.scheduler_add_job(**update_value)
                    self.redis_db.delete_key(lock_name=update_key)
                else:
                    self.process_check_count(process_id=process_id, check_key=update_key)
            except Exception as e:
                print(f"check_update_task 函数 错误 ：{e}")
                print(traceback.format_exc())

    def check_delete_task(self) -> None:
        '''
        检查删除任务
        :return:
        '''

        for delete_key in self.redis_db.get_delete_task():
            delete_value = self.redis_db.from_key_get_value(delete_key)
            if delete_value is None:
                continue
            try:
                process_node_id = delete_value['process_node_id']
                apscheduler_id = delete_value['job_id']
                process_id = int(str(process_node_id).strip().split(':')[-1])
                if os.getpid() == process_id:
                    if self.scheduler.get_job(job_id=apscheduler_id):
                        self.scheduler.remove_job(job_id=apscheduler_id)
                    self.redis_db.delete_key(lock_name=delete_key)
                    self.redis_db.delete_key(
                        lock_name=f'{self.project_name}:running_job:{os.getpid()}:{apscheduler_id}')
                else:
                    self.process_check_count(process_id=process_id, check_key=delete_key)
            except Exception as e:
                print(f"check_delete_task 函数 错误 ：{e}")
                print(traceback.format_exc())

    def insert_task(self, task_info: Dict) -> None:
        '''
        新增任务
        :param task_info:
        :return:
        '''
        task_info['operation'] = 'insert'
        task_info['is_change'] = 1
        self.redis_db.string_set(f'{self.project_name}:backend:{task_info.get("job_id")}',
                                 json.dumps(task_info, ensure_ascii=False))

    def delete_task(self, job_id: str) -> None:
        '''
        删除任务
        :param job_id:
        :return:
        '''
        crawler_info = dict()
        crawler_info['job_id'] = job_id
        crawler_info['is_change'] = 1
        crawler_info['operation'] = 'delete'
        self.redis_db.string_set(f'{self.project_name}:backend:{crawler_info.get("job_id")}',
                                 json.dumps(crawler_info, ensure_ascii=False))

    def sync_running_job(self) -> None:
        '''
        同步当前apscheduler进程中的任务到redis
        :return:
        '''
        job_list = self.scheduler.get_jobs()
        for job in job_list:
            key = f'{self.project_name}:running_job:{os.getpid()}:{job.id}'
            lock_value = standard_time()
            self.redis_db.process_acquire(lock_name=key, lock_value=lock_value, expire_time=180)

    def check_redis_jobstores(self):
        '''
        异步检查 redis 中 apscheduler 的任务
        :return:
        '''
        job_process_dict = {}
        for all_key in self.redis_db.get_all_task():
            all_value = self.redis_db.from_key_get_value(all_key)
            if all_value is None:
                continue
            process_node_id = all_value["process_node_id"]
            job_id = all_value["job_id"]
            job_process_dict[job_id] = process_node_id
        if len(job_process_dict) == 0:
            return job_process_dict
        stores_job_task = self.redis_db.get_stores_job_task()
        for stores_job_key in stores_job_task:
            stores_job_run_times_key = stores_job_key.replace('jobs', 'run_times')
            job_states = self.redis_job_store.redis.hgetall(stores_job_key)
            stores_job_process_id = stores_job_key.replace('apscheduler:jobs', 'node')
            for job_id, job_state in six.iteritems(job_states):
                job_id = job_id.decode('utf-8')
                try:
                    belongs_to_process_id = job_process_dict[job_id]
                except KeyError:
                    continue
                if stores_job_process_id == belongs_to_process_id:
                    pass
                else:
                    if self.redis_job_store.redis.hexists(stores_job_key, job_id):
                        pass
                        with self.redis_job_store.redis.pipeline() as pipe:
                            pipe.hdel(stores_job_key, job_id)
                            pipe.execute()
                        with self.redis_job_store.redis.pipeline() as pipe:
                            pipe.zrem(stores_job_run_times_key, job_id)
                            pipe.execute()
                    continue

    def run(self) -> None:
        '''
        异步检查所有任务
        :return:
        '''
        self.check_backend_task()
        self.check_all_task()
        self.check_insert_task()
        self.check_update_task()
        self.check_delete_task()
        self.sync_running_job()
