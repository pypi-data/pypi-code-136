# 目前db框架，只支持 类协程形式，形式下边定义了
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session as Session_  # 为了去警告！
from functools import wraps
from magpielib.util.log import get_logger
from magpielib.application import RESPONSE_OK, SESS_DEBUG
from magpielib.util.pcoresync import SyncTransDealer, SyncTransInfo

Session = Session_  # class 对象
trans_loop = None
logger = get_logger('db_conf')
engine: any
engine = None


class _Session(Session_):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.read_only = False
        self.is_has_commit = False

    def commit(self):
        if self.read_only:
            raise Exception('-read_only can not commit...')
        self.is_has_commit = True
        super().commit()


class DbLocalHandler:
    """针对本地一次性的情况，和请求无关
    """
    def __init__(self):
        self.session = None
        self.sync_trans = None
        self.async_handler = None


def db_config(mysql):
    global engine, Session
    if engine is not None:  # 说明已经被初始化过来
        logger.debug('___this db has been initialized!')
        return engine
    dbconf = {'pool_timeout': mysql.PoolTimeout, 'echo': False, 'pool_size': mysql.PoolSize}
    engine = create_engine(mysql.Uri, **dbconf)
    engine.connect()
    logger.info('db_config- the uri is:%s, pool_size->%s', mysql.Uri, mysql.PoolSize)
    Session = sessionmaker(engine, class_=_Session)
    return engine


def load_dbsession(*, read_only=True, j_response=True):
    """类的获取session 通常服务于tornado，兼容协程
    --important协程只支持class 形式！
    ignore_trans 普通调用 做微事务，要不还要返回dict
    """
    def wraps_(func):
        if read_only:
            @wraps(func)
            async def _wraps(handler, *args, **kwargs):
                return await obtain_sess(func, handler, *args, **kwargs)
        else:
            @wraps(func)
            async def _wraps(handler, *args, **kwargs):
                return await obtain_sess_trans(func, handler, j_response, *args, **kwargs)
        return _wraps
    return wraps_


async def obtain_sess_trans(f, handler, j_response=True, *args, **kwargs):
    """只针对协程，相关业务需要在 base或task中实现
    """
    result = None
    sync_trans_info = None
    while True:
        conn = engine.connect()
        sess = Session(bind=conn, autoflush=False)
        trans = conn.begin()
        try:
            handler.session = sess
            _result = await f(handler, *args, **kwargs)  # 执行方法
            if handler.sync_trans:
                sync_trans_info = SyncTransInfo(handler.sync_trans)
            if j_response:  # 兼容migrate, 默认是处理请求 result.get('status')
                result = handler.j_response_data
                if not isinstance(result, dict):
                    raise Exception('请实现BaseReqHandler 或 SyncReqHandler 类方法')
                if result.get('status') == RESPONSE_OK:
                    deal_commit(handler, sess, trans, conn, sync_trans_info)
                else:
                    trans.rollback()
                    deal_fail(f, result.get('msg'), handler, sync_trans_info)
                return None
            else:  # response false 代表一次性，本地(或patch情况）
                # 这种情况一定要要求函数返回一个结果 None 代表成功，Exception 代表失败
                err = _result
                if err and not isinstance(err, Exception):
                    raise Exception("类协程方法必须返回None, 或则异常error")
                if not err:
                    deal_commit(handler, sess, trans, conn, sync_trans_info)
                else:
                    trans.rollback()
                    deal_fail(f, str(result), handler, sync_trans_info)
                return err
        except Exception as e:  # 连接失败重新获取连接！
            if 'OperationalError' in str(type(e)) and 'MySQL server' in str(e):
                continue
            else:
                trans.rollback()  # 回滚后 再 close 释放资源
                sess.close()
                trans.close()
                conn.close()
                result = e
                break
        finally:
            if not sync_trans_info:  # 不为空的时候 异步 等待微事务同步
                sess.close()
                trans.close()
                conn.close()
    # 走到这里，一定是异常了，要不上上边就返回了
    return deal_fail(f, result, handler, sync_trans_info)


async def obtain_sess(f, handler, *args, **kwargs):
    """只针对协程，相关业务需要在 base或task中实现
    """
    while True:
        async def doit():
            sess = None
            try:
                sess = Session()
                sess.read_only = True
                handler.session = sess
                return await f(handler, *args, **kwargs)
            finally:
                sess.close()
        if SESS_DEBUG:
            return await doit()
        try:
            return await doit()
        except Exception as e:  # 连接失败重新获取连接！
            if 'OperationalError' in str(type(e)) and 'MySQL server' in str(e):
                continue
            else:
                return deal_fail(f, e, handler)


def deal_fail(f, fail_error, handler, sync_trans_info=None):
    """处理异常情况的返回，兼容异步 微事务同步
    """
    logger.error('db->deal_fail f:%s, e:%s, self:%s', f, fail_error, handler)
    if sync_trans_info and handler.async_handler is not None:
        # 需要微事务同步，并且 是 patch 方法，我们才需要通知 pcore 失败状态；
        # rest 方式直接通过返回结果就可以知道该事件结果了
        SyncTransDealer.get_instance(sync_trans_info).notify_fail4patch(fail_error)
    if isinstance(fail_error, Exception):  # 直接抛出异常
        raise fail_error


def deal_commit(handler, sess, trans, conn, sync_trans_info=None):
    """提交commit事务（包含异步，事务同步）
    """
    if not sync_trans_info:
        sess.commit()
        trans.commit()
        return
    if sync_trans_info:
        if handler.async_handler is not None:
            # 上面的 close 会在finally 中 完成，下边的是非阻塞的微事务同步
            SyncTransDealer.get_instance(sync_trans_info).notify_success4patch(sess, trans, conn)
            return
        SyncTransDealer.get_instance(sync_trans_info).wait_result4rest(sess, trans, conn)
