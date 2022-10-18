import asyncio
import time
from deka_dubbo import boost, BrokerEnum
from test7 import test
# from distributed_framework.utils.get_logger import logger

# """
# 演示多进程启动消费，多进程和 asyncio/threading/gevnt/evntlet是叠加关系，不是平行的关系。
# """
#
# qps=5，is_using_distributed_frequency_control=True 分布式控频每秒执行5次。
# 如果is_using_distributed_frequency_control不设置为True,默认每个进程都会每秒执行5次。

# @boost('rabbitmq_test7',broker_kind=BrokerEnum.RABBITMQ_AMQPSTORM, qps=5, concurrent_mode=4, concurrent_num=5)


@boost('rabbitmq_test12', broker_kind=BrokerEnum.RABBITMQ_AMQPSTORM, concurrent_mode=2)
def ff(a_list):
    import os
    a_list[0] += 1
    a = a_list[0]
    b = a_list[1]
    time.sleep(2)
    # a_list[0] += 1
    c = test(a, b)
    # print(f'----:{os.getpid()}, {x}, {y}, {a}')
    print(f'----:{os.getpid()}, {c}')
    return c


if __name__ == '__main__':
    ff.clear()      # 清除
    # ff.publish()
    # for i in range(10):
    a_list = [1, 0]
    # for i in range(10):
    ff.push(a_list)

        # ff.publish
        # 这个与push相比是复杂的发布，第一个参数是函数本身的入参字典，后面的参数为任务控制参数，例如可以设置task_id，设置延时任务，设置是否使用rpc模式等。
        # ff.publish({'x': i * 10, 'y': i * 2}, priority_control_config=PriorityConsumingControlConfig(countdown=1, misfire_grace_time=15))

    # ff(666, 888)  # 直接运行函数
    # ff.start()  # 和 conusme()等效
    ff.consume()  # 和 start()等效
    # run_consumer_with_multi_process(ff, 2)  # 启动两个进程，建议不需要import这个函数现在。可以直接ff.multi_process_start(2)
    # ff.multi_process_start(2)  # 启动两个进程，和上面的run_consumer_with_multi_process等效,现在新增这个multi_process_start方法。
    # IdeAutoCompleteHelper(ff).multi_process_start(3)  # IdeAutoCompleteHelper 可以补全提示，但现在装饰器加了类型注释，ff. 已近可以在pycharm下补全了。
