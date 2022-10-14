# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastapi_crawler_scheduler',
 'fastapi_crawler_scheduler.service',
 'fastapi_crawler_scheduler.utils']

package_data = \
{'': ['*']}

install_requires = \
['APScheduler>=3.9.1,<4.0.0',
 'fastapi-utils>=0.2.1,<0.3.0',
 'fastapi>=0.85.0,<0.86.0',
 'redis>=4.3.4,<5.0.0',
 'uhashring>=2.1,<3.0']

setup_kwargs = {
    'name': 'fastapi-crawler-scheduler',
    'version': '2.0.7',
    'description': '新增查看任务的方法',
    'long_description': '*********\n\n# fastapi_crawler_scheduler\n\n*********\n\n## 使用\n\n*********\n\n```python\nimport uuid\nfrom fastapi import FastAPI\nfrom fastapi_crawler_scheduler import TaskScheduler\n\napp = FastAPI()\n\ntask_scheduler = TaskScheduler(\n    app=app,\n    ssl=False,\n    project_name="project_name",\n    uuid_number=uuid.uuid4().__str__(),\n    redis_username=\'redis_username\',\n    redis_password=\'redis_password\',\n    redis_host="127.0.0.1",\n    redis_port=6379,\n    thread_pool_size=50,\n)\n```\n\n### 添加|更新任务 - add_task\n\n#### interval类型\n\n```python\ndef add_spider(**crawler_info):\n    print(f"add_spider = {crawler_info}")\n    print("add_spider")\n\n\ntrigger = \'interval\'\ncrawler_info = {\n    "topic": "interval insert_task",\n    "title_handler_name": "interval insert_task",\n    "seconds": 4,\n}\njob_id = \'job_1\'\ntask_scheduler.add_task(\n    func=add_spider,\n    job_id=job_id,\n    trigger=trigger,\n    crawler_info=crawler_info,\n    seconds=4\n)\n```\n\n#### date类型\n\n```python\ndef add_spider(**crawler_info):\n    print(f"add_spider = {crawler_info}")\n    print("add_spider")\n\n\ntrigger = \'date\'\ncrawler_info = {\n    "topic": "date insert_task",\n    "title_handler_name": "date insert_task",\n    "run_date": "2022-10-03 11:30:00",\n}\njob_id = \'job_1\'\nrun_date = \'2022-10-03 11:30:00\'\ntask_scheduler.add_task(\n    func=add_spider,\n    job_id=job_id,\n    trigger=trigger,\n    crawler_info=crawler_info,\n    run_date=run_date,\n)\n```\n\n#### cron类型\n\n```python\ndef add_spider(**crawler_info):\n    print(f"add_spider = {crawler_info}")\n    print("add_spider")\n\n\njob_id = \'job_1\'\ntrigger = \'cron\'\nminute = \'*/2\'\ncrawler_info = {\n    "topic": "cron update_task",\n    "title_handler_name": "cron update_task",\n    "minute": minute,\n}\ntask_scheduler.add_task(\n    func=add_spider,\n    job_id=job_id,\n    trigger=trigger,\n    crawler_info=crawler_info,\n    minute=minute,\n)\n```\n\n### 删除任务 - delete_task\n\n```python\njob_id = \'job_1\'\ntask_scheduler.delete_task(job_id=job_id)\n```\n\n### 查看任务\n\n```python\n# 查看该项目的所有键\ntask_scheduler.show_all_redis_key()\n# 查看该项目的所进程\ntask_scheduler.show_all_redis_nodes()\n# 查看该项目的所有加载过的任务\ntask_scheduler.show_all_redis_tasks()\n# 查看该项目使用的apscheduler.get_jobs()方法获得的所有任务\ntask_scheduler.show_all_scheduler_get_jobs()\n# 查看该项目的apscheduler存储redis的所有任务\ntask_scheduler.show_all_apscheduler_stores_jobs()\n# 查看该项目的的apscheduler存储redis的所有任务的run_ttimes\ntask_scheduler.show_all_redis_apscheduler_run_times()\n# 查看该项目的所有任务不存在apscheduler存储redis的所有任务\ntask_scheduler.show_all_task_not_in_stores_jobs()\n# 查看该项目的任务没有执行的项目（不包含只执行过一次的项目）\ntask_scheduler.show_all_task_not_in_stores_run_times()\n```\n\n安装\n============\nPypi\n----\n\n    $ pip install fastapi-crawler-scheduler\n\n',
    'author': 'laowang',
    'author_email': '847063657@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
