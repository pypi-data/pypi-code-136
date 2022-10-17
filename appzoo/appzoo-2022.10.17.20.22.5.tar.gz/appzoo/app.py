#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : mi.
# @File         : iapp
# @Time         : 2020/10/22 11:01 上午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : https://www.w3cschool.cn/fastapi/fastapi-8jam3ld6.html
# todo：定时任务 https://www.jianshu.com/p/090dd72a7266

from io import BytesIO

from starlette.status import *
from starlette.responses import *
from starlette.staticfiles import StaticFiles

from fastapi import FastAPI, Form, Depends, File, UploadFile, Body, Request, BackgroundTasks

# ME
from meutils.pipe import *
from meutils.str_utils import json_loads

# logger.add('runtime_{time}.log')

class App(object):
    """
    from appzoo import App
    app = App()
    app_ = app.app
    app.add_route()

    if __name__ == '__main__':
        app.run(app.app_from(__file__), port=9955, debug=True)
    """

    def __init__(self, config_init=None, **kwargs):
        self.app = FastAPI(**kwargs)

        # 原生接口
        self.get = self.app.get
        self.post = self.app.post
        self.api_route = self.app.api_route
        self.mount = self.app.mount  # mount('/subapi', subapp)

        # 增加配置项，方便热更新
        self.config = get_config(config_init)  # 全局变量

        # 功能性接口
        self.add_route_plus(self.app_config, methods=["GET", "POST"])
        self.add_route_plus(self.proxy_app, methods="POST")  # 代理服务，自己调自己有问题

    def run(self, app=None, host="0.0.0.0", port=8000, workers=1, access_log=True, debug=False, **kwargs):
        """

        :param app:   app字符串可开启热更新 debug/reload
        :param host:
        :param port:
        :param workers:
        :param access_log:
        :param debug: reload
        :param kwargs:
        :return:
        """

        import uvicorn
        """
        https://www.cnblogs.com/poloyy/p/15549265.html 
        https://blog.csdn.net/qq_33801641/article/details/121313494
        """

        # _ = uvicorn.Config(
        #     app if app else self.app,
        #     host=host, port=port, workers=workers, access_log=access_log, debug=debug, **kwargs
        # )
        # server = uvicorn.Server(_)
        # from appzoo.utils.settings import uvicorn_logger_init
        # uvicorn_logger_init()
        # server.run()

        # uvicorn.config.LOGGING_CONFIG['formatters']['access']['fmt'] = f"""
        #      🔥 %(asctime)s | {LOCAL_HOST} - %(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s
        #      """.strip()
        uvicorn.config.LOGGING_CONFIG['formatters']['access']['fmt'] = f"""
              🔥 %(asctime)s - %(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s
              """.strip()
        uvicorn.run(
            app if app else self.app,
            host=host, port=port, workers=workers, access_log=access_log, debug=debug, **kwargs
        )

    def gunicorn_run(self, main_app='main:app_', gunicorn_conf=None):
        if gunicorn_conf is None:
            gunicorn_conf = get_resolve_path('gunicorn.conf.py', __file__)

        assert Path(gunicorn_conf).exists()

        os.system(f"gunicorn -c {gunicorn_conf} {main_app}")

    def add_route(self, path='/xxx', func=lambda x='demo': x, method="GET", **kwargs):

        handler = self._handler(func, method, **kwargs)
        self.app.api_route(path=path, methods=[method])(handler)

    def add_route_plus(self, func, path=None, methods: Union[List, str] = "GET", **kwargs):
        """

        :param path:
        :param func:
            @lru_cache()
            def cache(kwargs: str):
                time.sleep(3)
                return kwargs # json.load(kwargs.replace("'", '"'))

            def nocache(kwargs: dict): # 不指定类型默认字典输入
                time.sleep(3)
                return kwargs
        :param method:
        :param kwargs:
        :return:
        """
        assert isinstance(func, Callable)

        if isinstance(methods, str):
            methods = [methods]

        if path is None:
            path = f"""/{func.__name__.replace('_', '-')}"""  # todo 前缀

        assert path.startswith('/')

        handler = self._handler_plus(func, **kwargs)
        self.app.api_route(path=path, methods=methods)(handler)  # method

    def add_route_uploadfiles(self, path='/xxx', func=lambda x='demo': x, **kwargs):
        """
        def read_func(**kwargs):
            logger.info(kwargs)
            return pd.read_csv(kwargs['files'][0], names=['word']).to_dict('r')

        app.add_route_uploadfiles('/upload', read_func)

        """

        handler = self._handler4files(func, **kwargs)
        self.app.api_route(path=path, methods=['POST'])(handler)  # method

    def add_apps(self, app_dir='apps', main_func='main', **kwargs):  # todo: 优化
        """加载当前app_dir文件夹下的所有app（递归）, 入口函数都是main
        1. 过滤掉 _ 开头的py文件
        2. 支持单文件

        appcli easy-run <app_dir>
        """

        app_home = Path(sys_path_append(app_dir))
        n = app_home.parts.__len__()

        pattern = Path(app_dir).name if Path(app_dir).is_file() else '*.py'

        routes = []
        for p in app_home.rglob(pattern):
            home_parts = p.parts[n:]
            route = f'/{app_home.stem}/' + "/".join(home_parts)[:-3]
            module = importlib.import_module('.'.join(home_parts)[:-3])

            if hasattr(module, main_func):
                func = getattr(module, main_func)
                self.add_route(route, func, method='POST', **kwargs)
                routes.append(route)
            else:
                logger.warning(f"Filter: {p}")

        logger.info(f"Add Routes: {routes}")

        self.add_route(f'/__{app_home.stem}', lambda: routes, method='GET', **kwargs)
        return routes

    def _handler(self, func, method='GET', result_key='data', **kwargs):
        """

        :param func:
        :param method:
            get -> request: Request
            post -> kwargs: dict
        :param result_key:
        :return:
        """
        if method == 'GET':
            async def handler(request: Request):
                input = request.query_params._dict
                return self._try_func(input, func, result_key, **kwargs)

        elif method == 'POST':
            async def handler(kwargs_: dict):
                input = kwargs_
                return self._try_func(input, func, result_key, **kwargs)

        else:
            async def handler():
                return {'Warning': 'method not in {"GET", "POST"}'}

        return handler

    def _handler4files(self, func, **kwargs):

        async def handler(request: Request, files: List[UploadFile] = File(...)):
            input = request.query_params._dict
            # input['files'] = [BytesIO(await file.read()) for file in files]

            for file in files:
                bio = BytesIO(await file.read())
                bio.name = file.filename
                input.setdefault('files', []).append(bio)

            return self._try_func_plus(input, func, **kwargs)

        return handler

    def _handler_plus(self, func, **kwargs):

        async def handler(request: Request):
            input = request.query_params._dict
            body = await request.body()

            if body.startswith(b'{'):  # 主要分支
                input.update(json_loads(body))

            elif request.method == 'POST' and 'multipart/form-data' == request.headers.get("Content-Type"):
                form = await request.form()  # 重复 await
                for file in form.getlist('files'):  # files
                    bio = BytesIO(await file.read())
                    bio.name = file.filename
                    input.setdefault('files', []).append(bio)
            elif body:  # data:dict => application/x-www-form-urlencoded
                input.update({'__data__': body})  # 非 json 请求体

            # input4str 方便 cache
            if 'str' in str(func.__annotations__):  # todo: cachek可支持dict 取消判断
                input = str(input)  # json.loads
            elif 'tuple' in str(func.__annotations__):
                input = tuple(input.items())  # dict

            return self._try_func_plus(input, func, **kwargs)

        return handler

    @staticmethod
    def _try_func(input, func, result_key='data', **kwargs):  # todo: 可否用装饰器
        __debug = input.pop('__debug', 0)

        output = OrderedDict()
        output['error_code'] = 0
        output['error_msg'] = "SUCCESS"

        if __debug:
            output['requestParams'] = input
            output['timestamp'] = time.ctime()

        try:
            output[result_key] = func(**input)

        except Exception as error:
            output['error_code'] = 1  # 通用错误
            output['error_msg'] = traceback.format_exc().strip() if __debug else error  # debug状态获取详细信息

        finally:
            output.update(kwargs)

        return output

    @staticmethod
    def _try_func_plus(input, func, **kwargs):

        output = OrderedDict(code=0, msg="SUCCESS", **kwargs)

        try:
            output['data'] = func(input)

        except Exception as error:
            output['code'] = 1  # 通用错误
            output['data'] = kwargs.get('data')
            output['msg'] = traceback.format_exc().strip().split('\n') \
                if output['data'] is None else error  # 无默认值则获取详细信息

            logger.error(output['msg'])

        return output

    def app_from(self, file=__file__, app='app_'):
        return f"{Path(file).stem}:{app}"

    def app_config(self, kwargs: str):
        _ = json_loads(kwargs)
        if _ and _ != self.config:  # 更新配置
            self.config.update(_)
            logger.warning("Configuration item is modified ！！！")

        return self.config

    def proxy_app(self, kwargs: dict):
        """代理层
        {
            "url": "http://0.0.0.0:8000/xx",
            "method": "post",
            "json": {"a": 1}
        }
        """
        r = requests.request(**kwargs)
        return r.json()


if __name__ == '__main__':
    import uvicorn

    app = App()
    app_ = app.app
    app.add_route('/get', lambda **kwargs: kwargs, method="GET", result_key="GetResult")
    app.add_route('/post', lambda **kwargs: kwargs, method="POST", result_key="PostResult")

    app.run(port=9000, debug=False, reload=False, access_log=True)
    # app.run(f"{app.app_from(__file__)}", port=9000, debug=False, reload=False) # app_的在 __main__ 之上
