# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tapdata_cli', 'tapdata_cli.params']

package_data = \
{'': ['*'], 'tapdata_cli': ['startup/*']}

install_requires = \
['PyYAML==5.4.1',
 'allure-pytest>=2.9.45,<3.0.0',
 'asyncio==3.4.3',
 'atomicwrites==1.4.0',
 'attrs==21.2.0',
 'certifi==2020.12.5',
 'chardet==4.0.0',
 'colorama==0.4.4',
 'colorlog==5.0.1',
 'idna==2.10',
 'iniconfig==1.1.1',
 'javascripthon>=0.12,<0.13',
 'jupyter>=1.0.0,<2.0.0',
 'packaging==20.9',
 'pluggy==0.13.1',
 'py==1.10.0',
 'pymongo==4.1.1',
 'pyparsing==2.4.7',
 'pytest-parallel>=0.1.1,<0.2.0',
 'pytest>=7.1.2,<8.0.0',
 'requests==2.25.1',
 'toml==0.10.2',
 'urllib3==1.26.4',
 'websockets==10']

setup_kwargs = {
    'name': 'tapdata-cli',
    'version': '2.3.0',
    'description': 'Tapdata Python Sdk',
    'long_description': '# Tapdata Python Sdk\n\n[English](https://github.com/tapdata/tapdata/tree/master/tapshell/docs/Python-Sdk.md)\n\n*Applicable version*\n\n- tapshell / Python-Sdk: ^2.3.0\n- tapdata: ^2.9\n\n## Install\n\n1. Install python3.7、pip；\n2. Run ```pip install tapdata_cli``` to install sdk；\n3. if use Poetry, run ```poetry add tapdata_cli``` to install dependence.\n\n## Initial\n\n```python\nserver = "127.0.0.1:3000"\naccess_code = "3324cfdf-7d3e-4792-bd32-571638d4562f"\nfrom tapdata_cli import cli\ncli.init(server, access_code)\n```\n\n**Multi-thread concurrency is not supported**\n\nIt will send a request to the server to obtain the identity information and save it as a global variable. Therefore, after multiple init the \'server\' and \'access_code\' variable will be overwritten.\n\nFor situations where you need to use different servers and access_codes concurrently, use Python\'s multiprocess.\n\n## DataSource\n\n### Create DataSource\n\nTo create DataSource by Python Sdk, you can do it by form or uri mode.\n\nExample for uri mode:\n\n```python\nfrom tapdata_cli import cli\n\nconnector = "mongodb"  # 数据源类型，mongodb mysql postgres\nmongo = cli.DataSource("mongodb", name="mongo")\nmongo.uri("mongodb://localhost:8080")  # 数据源uri\nmongo.save()\n```\n\nor form mode:\n\n```python\nfrom tapdata_cli import cli\n\nmongo = cli.DataSource("mongodb", name="mongo")\nmongo.host("localhost:27017").db("source").username("user").password("password").props("")\nmongo.type("source")  # 数据源类型，source -> 只可作为源，target -> 只可作为目标，source_and_target -> 可以作为源和目标（默认）\nmongo.save()  # success -> True, Failure -> False\n```\n\nMore infomation to create DataSource, please read [this file](https://github.com/tapdata/tapdata/blob/master/tapshell/docs/Param-Check_zh-hans.md).\n\n### DataSource List\n\n```python\nfrom tapdata_cli import cli\n\ncli.DataSource().list()\n\n# return datastruct\n\n{\n    "total": 94,\n    "items": [{\n        "id": "",\n        "lastUpdBy": "",\n        "name": "",\n        "config": {},\n        "connection_type": "",\n        "database_type": "",\n        "definitionScope": "",\n        "definitionVersion": "",\n        "definitionGroup": "",\n        "definitionPdkId": "",\n        ...\n        }]\n        }\n        ```\n\n### get datasource by id/name\n\n```python\nfrom tapdata_cli import cli\n\ncli.DataSource(id="")  # 根据id获取数据源信息\ncli.DataSource(name="")  # 根据name获取数据源信息\n```\n\n## Pipeline\n\n### Migrate job\n\n```python\nfrom tapdata_cli import cli\n\n# Create DataSource\ncli.DataSource("mongodb", name="source").uri("").save()\ncli.DataSource("mongodb", name="target").uri("").save()\n\n# Create Source and target node\nsource = cli.Source("source")\ntarget = cli.Sink("target")\n\n# copy all table by default;\n# copy by tables you want to, use table=[]\n# filter table, by table_re\nsource = cli.Source("source", table=["table_1", "table_2", "table_3"], table_re="table_*")\nsource.config({"migrateTableSelectType": "custom"})  # change migrateTableSelectType: from all to custom\n\n# init pipeline install\np = cli.Pipeline(name="example_job")\np.readFrom(source).writeTo(target)\n# start\np.start()\n# stop\np.stop()\n# delete\np.delete()\n# check status\np.status()\n# job list\ncli.Job.list()\n```\n\nJob is th underlying implementation of Pipeline，so you can start job by `job.start()` like `pipeline.start()`。\n\n```python\n# init job (get job info) by id\nfrom tapdata_cli import cli\njob = cli.Job(id="some id string")\njob.save() # success -> True, failure -> False\njob.start() # success -> True, failure -> False\n```\n\n### Sync job\n\nBefore you start a sync job, update job mode to `sync`.\n\n```python\nfrom tapdata_cli import cli\n\ncli.DataSource("mongodb", name="source").uri("").save()  # create datasource\ncli.DataSource("mongodb", name="target").uri("").save()  # create target\np = cli.Pipeline(name="sync_job", mode="sync")  # update to sync mode, or use p.dag.jobType = JobType.sync\np.mode(cli.JobType.sync)  # or you can update to sync mode by this way\n\n# read source\np = p.readFrom("source.player") # source is db, player is table\np = p.readFrom(cli.Source("source", table="player", mode="sync"))  # or you init a Source Node in sync mode\n\n# continue to complex operation next\n\n# filter cli.FilterType.keep (keep data) / cli.FilterType.delete (delete data)\np = p.filter("id > 2", cli.FilterType.keep)\n\n# filerColumn cli.FilterType.keep (keep column) / cli.FilterType.delete (delete column)\np = p.filterColumn(["name"], cli.FilterType.delete)\n\n# rename\np = p.rename("name", "player_name")\n\n# valueMap\np = p.valueMap("position", 1)\n\n# js\np = p.js("return record;")\n\np.writeTo("target.player")  # target is db, player is table\np.writeTo(cli.Sink("target", table="player", mode="sync")\n```\n\nMaster-slave Merge：\n\n```python\np2 = cli.Pipeline(name="source_2")  # create pipeline which will be merged\np3 = p.merge(p2, [(\'id\', \'id\')])  # merge p2 and set joinkey, then writeTo a table\n\np3.writeTo("target.player")  # target is db, player is table\n```\n\n### Initial_sync\n\nIt\'s "initial_sync+cdc" mode by default. You can create a "initial_sync" job by this way:\n\n```python\nfrom tapdata_cli import cli\n\np = cli.Pipeline(name="")\np.readFrom("source").writeTo("target")\nconfig = {"type": "initial_sync"}  # initial_sync job\np1 = p.config(config=config)\np1.start()\n```\n\nChange config by config method like `{"type": "cdc"}` to create a initial_sync job。\n\nPython sdk has built-in param verification, you can update config by Pipeline.config, to see more configuration, you can see [this file](https://github.com/tapdata/tapdata/blob/master/tapshell/tapdata_cli/params/job.py)\n\n## Api Operation\n\n### Create/Update Apiserver\n\n```python\nfrom tapdata_cli import cli\n\n# Create\ncli.ApiServer(name="test", uri="http://127.0.0.1:3000/").save()\n\n# Update\n# 1.Get ApiServer id\napi_server_id = cli.ApiServer.list()["id"]\n# 2.Update ApiServer and save\ncli.ApiServer(id=api_server_id, name="test_2", uri="http://127.0.0.1:3000/").save()\n\n# delete apiserver\ncli.ApiServer(id=api_server_id).delete()\n```\n\n### Publish Api\n\n```python\nfrom tapdata_cli import cli\ncli.Api(name="test", table="source.player").publish() # source is db, player is table\n```\n\n### Unpublish Api\n\n```python\nfrom tapdata_cli import cli\ncli.Api(name="test").unpublish()\n```\n\n### Delete api\n\n```python\nfrom tapdata_cli import cli\ncli.Api(name="test").delete()\n```\n\n### Check api status\n\n```python\nfrom tapdata_cli import cli\ncli.Api().status("test")  # success -> "pending" or "active" / failure -> None\n```\n',
    'author': 'Tapdata',
    'author_email': 'team@tapdata.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/tapdata/tapdata/tree/master/tapshell',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
