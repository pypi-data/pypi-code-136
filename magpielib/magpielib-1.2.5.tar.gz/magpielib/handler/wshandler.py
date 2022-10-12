"""
配合hcore 伪装patch 实现微服务端实现ws
"""
from tornado.ioloop import IOLoop
from magpielib.handler.reqhandler import BaseReqHandler
from magpielib.handler.patchhandler import BasePatchHandler as _BasePatchHandler
from magpielib.util.log import get_logger
logger = get_logger("ws_handler")


class wsHandler(BaseReqHandler):
    """对Websocket 支持（本质上是一个patch），只不过为了开发方便抽离出来了，要不的话太难理解，影响效率
    """
    async def post(self):
        if not self.async_wait:  # 一定是patch core 分发调用过来的
            return self.j_response(
                -405, "Ws 调用方式有误（请通过httpcore访问，不支持直接访问！！！）")
        IOLoop.current().spawn_callback(
            self.async_handler().dispatch, self.async_handler,
            self.p, self.behavior, self.sync_trans, self.async_wait, self.request.path, "Post")
        return self.j_response()

    async def get(self):
        return self.j_response(
            -404, "Ws方法只支持 post 对 type=Ws情况（请通过httpcore访问，不支持直接访问！！！）")

    async def put(self):
        return self.j_response(
            -404, "Ws方法只支持 post 对 type=Ws情况（请通过httpcore访问，不支持直接访问！！！）")

    async def delete(self):
        return self.j_response(
            -404, "Ws方法只支持 post 对 type=Ws情况（请通过httpcore访问，不支持直接访问！！！）")


class BaseWsHandler(_BasePatchHandler):
    """微服务对接httpcore的长连接，本质上是一个patch；
    这样写的原因是让httpcore能发现yaml文件中该接口（Ws）并注册出去....该方法只支持post
    """

    async def ws_do(self):
        """will impl by 业务层
        """
        return self.j_response(-404, "ws -->wsdo-方法未实现！！！")

    async def exec_method(self, _):
        """ws 只关注post 方法，method 也必然是 post; 见WsHandler
        """
        msg = ""
        try:
            await self.ws_do()
        except Exception as e:
            msg = " ws 异常**** %s" % str(e)
        return msg
