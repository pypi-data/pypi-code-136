import sys
from tornado.web import Application
from magpielib import service_map
RESPONSE_OK = 0  # 请求正常
RESPONSE_NO_METHOD_ERROR = -1  # 微服务异常
RESPONSE_SERVICE_ERROR = -2  # 微服务异常
RESPONSE_VALIDATE_ERROR = -3  # 返回结果参数校验失败
RESPONSE_SQL_ERROR = -4  # 数据库操作异常
RESPONSE_THIRD_ERROR = -5  # 第三方服务调用异常
RESPONSE_SYS_BUSY = -5  # 系统繁忙，微事务同步
TRANS_TASK_FAIL = -7  # 微事务 task 同步失败
PARSE_ERROR_REQ_P = -8  # 参数格式不正确
SYNC_LOCAL_FUNC_ERROR = -9  # 微事务同步时，同步执行本地方法报错
SESS_DEBUG = ('ss_debug' in sys.argv)  # db直接崩溃好找问题
UNITTEST = 'un_debug' in sys.argv  # 单元测试 debug 区分于使用微服务debug
INT_TRUE = 1
INT_FALSE = 0
from magpielib.util.log import get_logger
logger = get_logger("application")


def sh_application(path_api, server_name, debug, autoreload, gen_doc=False):
    """
    将sh_routers 注册到Tornado框架中
    """
    from magpielib.handler.patchhandler import patchHandler
    from magpielib.handler.wshandler import wsHandler
    from magpielib.parse import parse_apis
    routers = []
    _handler_map = {}  # 单纯的校验 handler 是否有重复
    _url_map = {}  # 单纯的校验 uri 是否有重复
    sh_routers = parse_apis(path_api, server_name)
    if not sh_routers:
        raise Exception("请配置apis yaml 文件！")
    for sh_router in sh_routers:
        if sh_router.handler in _handler_map and sh_router.handler not in (patchHandler, wsHandler):
            raise Exception("不同的uri 不能注册到同一个handler上->%s" % sh_router.handler)
        if sh_router.uri in _url_map:
            raise Exception("uri不能重复 ->%s" % sh_router.uri)
        _handler_map[sh_router.handler] = ''
        _url_map[sh_router.uri] = ''
        routers.append((sh_router.uri, sh_router.handler))
    if gen_doc and not UNITTEST:
        doc_router = gen_doc4routers(sh_routers, server_name)
        routers.append(doc_router)
    app = Application(routers, debug=debug, autoreload=autoreload, gzip=True)
    service_map.ServerName = server_name
    return app


def gen_doc4routers(sh_routers, server_name):
    """根据路由生产文档"""
    import os
    from magpielib.util.doc import generate_doc4router, init, close
    _doc_path = '../__doc'
    doc_path = os.path.join(os.getcwd(), _doc_path)
    if not os.path.exists(doc_path):
        os.mkdir(doc_path)
    init(os.path.join(doc_path, 'doc.py'), server_name)
    for sh_router in sh_routers:
        generate_doc4router(sh_router)
    close()
    # 执行apidoc命令,生产文档
    from magpielib.util.alembic import do_shell
    do_shell("apidoc -i " + doc_path + ' -o ' + doc_path, logger)
    from tornado import web
    root = os.path.join(os.getcwd(), doc_path)
    return r"/doc/(.*)", web.StaticFileHandler, {"path": root, "default_filename": "index.html"}
