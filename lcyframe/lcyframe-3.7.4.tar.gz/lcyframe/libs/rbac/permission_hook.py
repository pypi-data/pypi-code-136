import logging
from datetime import datetime

from contextlib import suppress
from django.conf import settings
from django.urls import resolve
from django.db.models import Q
from mongoengine.queryset.visitor import Q as MONGO_Q

# from .publick_tools import get_ur_subdomain

logger = logging.getLogger("django")


def check_permission_hook(request):
    print("check_permission_hook")
    return True


# def tasks_tasks_post(request):
#     """
#     扫描任务判断
#     ------判断user的公司的权限组
#     :param request:
#     :return:
#     """
#     msg = "ok"
#
#     try:
#         if Tasks.objects.filter(
#                 company_id=request.user.company_id,
#                 create_time__year=datetime.now().year,
#                 create_time__month=datetime.now().month
#         ).exclude(state=Tasks.STATE_ABEND).count() >= request.user.company.groups.role.scan_times:
#             msg = "扫描任务次数达到上限，请联系管理员"
#             return False, msg
#     except Exception as e:
#         msg = "用户异常，请联系客服"
#         return False, msg
#
#     return True, msg


def user_company_user_get(request):
    msg = "ok"
    # 接口限制, 数据限制
    # role_list = request.user.groups.all().values_list("id", flat=True)
    # if settings.ADMIN_ROLE_GROUP not in role_list:
    #     q = Q()
    #     q.connector = 'AND'
    #     q.children.append(('id', request.user.id))
    #     setattr(request, 'permission_qobject', q)
    return True, msg


def user_logging_register_get(request):
    msg = "ok"
    # 接口限制, 数据限制
    role_list = request.user.groups.all().values_list("id", flat=True)
    if settings.ADMIN_ROLE_GROUP not in role_list:
        q = MONGO_Q()
        q.AND = 1
        q.OR = 0
        q.query.setdefault("user_id", request.user.id)
        setattr(request, "permission_qobject", q)
    return True, msg


def user_logging_register_execl_get(request):
    msg = "ok"
    # 接口限制, 数据限制
    role_list = request.user.groups.all().values_list("id", flat=True)
    if settings.ADMIN_ROLE_GROUP not in role_list:
        q = MONGO_Q()
        q.AND = 1
        q.OR = 0
        q.query.setdefault("user_id", request.user.id)
        setattr(request, "permission_qobject", q)
    return True, msg


def user_logging_operation_get(request):
    msg = "ok"
    # 接口限制, 数据限制
    role_list = request.user.groups.all().values_list("id", flat=True)
    if settings.ADMIN_ROLE_GROUP not in role_list:
        q = MONGO_Q()
        q.AND = 1
        q.OR = 0
        q.query.setdefault("user_id", request.user.id)
        setattr(request, "permission_qobject", q)
    return True, msg


def user_logging_operation_execl_get(request):
    msg = "ok"
    # 接口限制, 数据限制
    role_list = request.user.groups.all().values_list("id", flat=True)
    if settings.ADMIN_ROLE_GROUP not in role_list:
        q = MONGO_Q()
        q.AND = 1
        q.OR = 0
        q.query.setdefault("user_id", request.user.id)
        setattr(request, "permission_qobject", q)
    return True, msg



def user_user_site_info_get(request):

    return True, ""


