"""
    patch 的使用场景：1.不阻塞组流程，比如下订单的时候 异步更新用户订单数据情况，或者更新分销返利数据
                    2.耗时任务处理，比如文件组装
    另外，对于调用patch方来说，如果给pid说明调用方关注结果（比如websocket 需要等待patch耗时操作的结果）
    实现方会将自己的结果写到redis对应的pid字段中。当然整个交互是通过redis来实现的，不用http方式
总体约束：patch 中的task 方法是没有返回值的（方法本身返回成功失败）
        如果patch需要返回相关数据的话就将patch 方法写成rest 形式就好
"""
from tornado.ioloop import IOLoop
from magpielib.handler.reqhandler import BaseReqHandler
from magpielib.handler.handler_util import ReqUtil
from magpielib.util.log import get_logger
from magpielib.util.pcorewait import PatchWaitDealer, WaitPatchInfo
logger = get_logger("patch_handler")


class patchHandler(BaseReqHandler):
    """将patch 方法统一注册到这个实例上，在这个实例上进行异步分发调用，及时返回
    """
    async def get(self):
        IOLoop.current().spawn_callback(
            self.async_handler().dispatch, self.async_handler,
            self.p, self.behavior, self.sync_trans, self.async_wait, self.request.path, "Get")
        return self.j_response()

    async def post(self):
        IOLoop.current().spawn_callback(
            self.async_handler().dispatch, self.async_handler,
            self.p, self.behavior, self.sync_trans, self.async_wait, self.request.path, "Post")
        return self.j_response()

    async def put(self):
        IOLoop.current().spawn_callback(
            self.async_handler().dispatch, self.async_handler,
            self.p, self.behavior, self.sync_trans, self.async_wait, self.request.path, "Put")
        return self.j_response()

    async def delete(self):
        IOLoop.current().spawn_callback(
            self.async_handler().dispatch, self.async_handler,
            self.p, self.behavior, self.sync_trans, self.async_wait, self.request.path, "Delete")
        return self.j_response()


class BasePatchHandler(ReqUtil):
    """task 通知调用方 调用成功或失败，如果调用方不关心结果的话，那么就发起报警
    整体交互都是和p-core 交互，调用方如果想得到结果也需要通过websocket访问p-core 等待结果
    """
    def __init__(self):
        super().__init__()
        self.p = None  # 参数
        self.behavior = None
        self.sync_trans = None  # 见BaseReqHandler 注释
        self.patch_wait = None  # # 见BaseReqHandler 注释
        self.async_handler = None
        self.session = None
        self.uri = None
        self.method = None

    async def dispatch(self, async_handler, p, b, st, pw, uri, method):
        self.async_handler = async_handler
        self.p = p
        self.behavior = b
        self.sync_trans = st
        self.patch_wait = pw
        self.uri = uri
        self.method = method
        # 判断是否要通知调用方结果
        if self.patch_wait:
            self.patch_wait_dealer = PatchWaitDealer.get_instance(WaitPatchInfo(self.patch_wait))
        err = await self.exec_method(method)
        if err and not isinstance(err, Exception):
            raise Exception("Patch方法实现错误-必须返回None, 或则异常error")
        if err and self.patch_wait_dealer:
            self.notify_to_caller(-1, msg=str(err))
        # 走到这里代表整体成功了，判断下最后有没有通知到
        if self.patch_wait_dealer and not self.patch_wait_dealer.done_notify_yet:
            self.notify_to_caller(1, "")  # 说明不注重结果了
        logger.info("@@@ in patch done->:%s", err)

    async def exec_method(self, method):
        """拆出来的原因主要因为 要兼容 ws，ws会重写该方法 见 WsHandler
        """
        try:
            if method == "Get":
                rest = await self.get()
            elif method == "Post":
                rest = await self.post()
            elif method == "Put":
                rest = await self.put()
            elif method == "Delete":
                rest = await self.delete()
            else:
                raise Exception('never happen....')
        except Exception as e:
            rest = e
        return rest

    def notify_to_caller(self, progress, msg=""):
        """ 把progress 当成status 使用；在同一个接口该方法可以多次被调用，以便传递progress（注意 progress >1 的时候就不通知调用方了；代表这个事件结束）
        当接收到 pcore 的patch_wait 时，业务处理过程中要通知调用方 可以通知过程的progress进度（最常见的是在调用完成通知 调用方结果）
        process: 0~1，!=1 这时候 可以传process msg 等信息； == 1 代表结束； == -1 事代表失败（结束），msg 代表失败原因

        **call_patch_wait4done 该方法和其对应，对于patch 和 rest 都有这个需求，故写 在 父类 ReqUtil 中实现了

        """
        self.patch_wait_dealer.notify(progress, msg)

    async def get(self):
        """will impl by 业务层
        """
        return self.j_response(-404, "patch -->get-方法未实现！！！")

    async def post(self):
        """will impl by 业务层
        """
        return self.j_response(-404, "patch -->post-方法未实现！！！")

    async def put(self):
        """will impl by 业务层
        """
        return self.j_response(-404, "patch -->put-方法未实现！！！")

    async def delete(self):
        """will impl by 业务层
        """
        return self.j_response(-404, "patch -->delete-方法未实现！！！")
