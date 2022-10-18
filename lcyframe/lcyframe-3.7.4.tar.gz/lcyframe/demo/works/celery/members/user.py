# -*- coding: utf-8 -*-
from celery import shared_task
import random, time
from lcyframe.libs.celery_route import BaseTask
from lcyframe.libs.celery_route import BaseEvent

@shared_task(ignore_result=False)  # 普通函数装饰为 celery task
def save_image(x):
    """
    self.application.celery.save_image.delay(111)
    :param x:
    :return:
    """
    n = round(random.random(), 2)
    time.sleep(n)

    # model.UserModel.get_xxx()
    return x, n


class UserEvent(BaseEvent):
    @staticmethod
    @shared_task(ignore_result=False)
    def register(x):
        """
        按类名划分任务组
        :use self.application.celery.UserEvent.register.delay(111)
        :param x:
        :return:

        """
        n = round(random.random(), 2)
        time.sleep(n)

        return x, n
