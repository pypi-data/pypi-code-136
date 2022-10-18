import logging
from datetime import datetime

from contextlib import suppress
from django.conf import settings
from django.urls import resolve
from django.db.models import Q
from mongoengine.queryset.visitor import Q as MONGO_Q

from article.models import Article, ArticleFile
from rbac.publick_tools import get_ur_subdomain
from system_setting.models import Setting
from vulnerability.models import Vulnerability

logger = logging.getLogger("django")


def check_permission_hook(request):
    print("check_permission_hook")
    return True


# 函数名称最好与权限codename保持一致，后续可用于自动导入权限条目标
def service_center_article_get(request):
    """
    根据审核角色获取资讯列表
    ------如果当前用户是审核角色，获取全部待审核|全部已发布|当前用户的草稿|当前用户的回退
    ------如果登当前用户是非审核角色， 获取全部已发布|当前用户的草稿|当前用户的回退
    :param request:
    :return:
    """
    msg = "ok"
    group_name_list = list(request.user.groups.all().values_list("name", flat=True))
    audict_role = set(group_name_list) & set(Setting.objects.get(key="ARTICLE_AUDIT_ROLE").value)
    q = Q()
    q.connector = "OR"
    q.children.append(("publisher_id", request.user.id))
    q.children.append(("news_state", Article.NEWS_ON_PUBLISH))
    if audict_role:
        q.children.append(("news_state", Article.NEWS_WAIT_AUDIT))
    permission_queryset = Article.objects.filter(q).extra(
        select={
            "content": "left(article.content, 80)",
            "publisher": "select username from user where article.publisher_id = user.id",
            "auditer": "select username from user where article.auditer_id = user.id",
            "cover_name_url": 'select concat("{\'name\':\'", article_file.name, "\',\'url\':\'", article_file.file, "\'}") as cover_name_url from article_file '
                              'where article_file.type = %d and article_file.article_id=article.id' % ArticleFile.COVER,
        }
    )
    setattr(request, "permission_queryset", permission_queryset)
    return True, msg


def service_center_article_pk_delete(request):
    """
    删除资讯
    ------如果该资讯是当前用户发布的，则允许删除，否则不允许
    :param request:
    :return:
    """
    msg = "ok"
    func, args, kwargs = resolve(request.path)
    qs = Article.objects.filter(id=kwargs.get("pk"))
    if qs.exists() and qs.first().publisher_id != request.user.id:
        return False, msg
    return True, msg


def service_center_article_pk_agree_put(request):
    """
    同意发布资讯
    ------如果当前用户角色属于审核角色，则允许同意发布该资讯，否则不允许
    :param request:
    :return:
    """
    msg = "ok"
    func, args, kwargs = resolve(request.path)
    group_name_list = list(request.user.groups.all().values_list("name", flat=True))
    audit_role = set(group_name_list) & set(Setting.objects.get(key="ARTICLE_AUDIT_ROLE").value)
    qs = Article.objects.filter(id=kwargs.get("pk"))
    if qs.exists() and not audit_role:
        return False, msg
    return True, msg


def service_center_article_pk_disagree_put(request):
    """
    不同意发布资讯
    ------如果当前用户角色属于审核角色，则允许不同意发布该资讯，否则不允许
    :param request:
    :return:
    """
    msg = "ok"
    func, args, kwargs = resolve(request.path)
    group_name_list = list(request.user.groups.all().values_list("name", flat=True))
    audit_role = set(group_name_list) & set(Setting.objects.get(key="ARTICLE_AUDIT_ROLE").value)
    qs = Article.objects.filter(id=kwargs.get("pk"))
    if qs.exists() and not audit_role:
        return False, msg
    return True, msg


def service_center_article_pk_submit_put(request):
    """
    编辑资讯(提交)
    ------如果该资讯是当前用户发布的，则允许提交，否则不允许
    :param request:
    :return:
    """
    msg = "ok"
    func, args, kwargs = resolve(request.path)
    qs = Article.objects.filter(id=kwargs.get("pk"))
    if qs.exists() and qs.first().publisher_id != request.user.id:
        return False, msg
    return True, msg


def service_center_article_pk_save_put(request):
    """
    编辑资讯(保存)
    ------如果该资讯是当前用户发布的，则允许保存，否则不允许
    :param request:
    :return:
    """
    msg = "ok"
    func, args, kwargs = resolve(request.path)
    qs = Article.objects.filter(id=kwargs.get("pk"))
    if qs.exists() and qs.first().publisher_id != request.user.id:
        return False, msg
    return True, msg


def service_center_article_file_pk_delete(request):
    """
    删除资讯附件
    ------如果该资讯是当前用户发布的，则允许保存，否则不允许
    :param request:
    :return:
    """
    msg = "ok"
    func, args, kwargs = resolve(request.path)
    qs = ArticleFile.objects.filter(id=kwargs.get("pk")).extra(
        select={"publisher_id": "article.publisher_id"},
        tables=["article"],
        where=["article.id = article_file.article_id"],
    )
    if qs.exists() and qs.first().publisher_id != request.user.id:
        return False, msg
    return True, msg


def service_center_article_delete_delete(request):
    """
    批量删除资讯
    ------如果选中的所有资讯是当前用户发布的，则允许删除，否则都不允许删除
    :param request:
    :return:
    """
    msg = "ok"
    ids = []
    for i in request.GET.get("ids").split(","):
        with suppress(ValueError, TypeError):
            ids.append(int(i))
    publisher_id_list = list(set(Article.objects.filter(Q(id__in=ids)).values_list("publisher_id", flat=True)))
    if len(publisher_id_list) == 1 and publisher_id_list[0] == request.user.id:
        return True, msg
    return False, msg


def service_center_article_pk_istop_put(request):
    """
    置顶开关
    ------如果当前用户角色属于审核角色，则允许置顶该资讯，否则不允许
    :param request:
    :return:
    """
    msg = "ok"
    func, args, kwargs = resolve(request.path)
    group_name_list = list(request.user.groups.all().values_list("name", flat=True))
    audit_role = set(group_name_list) & set(Setting.objects.get(key="ARTICLE_AUDIT_ROLE").value)
    qs = Article.objects.filter(id=kwargs.get("pk"))
    if qs.exists() and not audit_role:
        return False, msg
    return True, msg


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


def vulnerability_vuln_risk_count_get(request):
    vuln_qs = Vulnerability.objects.filter(is_delete=False, company_id=request.user.company_id)
    user_groups = request.user.groups.all().values_list("id", flat=True)
    if settings.ADMIN_ROLE_GROUP in user_groups:
        vuln_qs_ids = vuln_qs.values_list("id", flat=True)
    else:
        subdomain_ids = get_ur_subdomain(request.user)
        vuln_qs_ids = vuln_qs.filter(subdomain_id__in=subdomain_ids).values_list("id", flat=True)
    setattr(request, "permission_qids", set(vuln_qs_ids))
    return True, "ok"


def vulnerability_vuln_risk_list_get(request):
    vuln_params = {"company_id": request.user.company_id, "is_delete": 0}

    user_groups = request.user.groups.all().values_list("id", flat=True)
    if settings.ADMIN_ROLE_GROUP in user_groups:
        vuln_qs = Vulnerability.objects.filter(**vuln_params)
    else:
        subdomain_ids = get_ur_subdomain(request.user)
        vuln_qs = Vulnerability.objects.filter(subdomain_id__in=subdomain_ids, **vuln_params)
    setattr(request, "permission_qobject", vuln_qs)
    return True, "ok"


def vulnerability_vuln_risk_detail_get(request):
    """
    漏洞详情限制
    """
    vuln_count = 5
    # 接口限制
    try:
        if (
            request.user.company.groups.id == 1
            and Vulnerability.objects.filter(company_id=request.user.company_id, is_read=0).count() >= vuln_count
        ):
            msg = "体验用户只可查看5次漏洞详情"
            return False, msg
    except Exception as e:
        msg = "用户异常，请联系客服"
        return False, msg

    vuln_id = request.GET.get("id", None)
    if not vuln_id:
        return False, "参数不全"

    vuln_params = {"company_id": request.user.company_id, "is_delete": 0}
    user_groups = request.user.groups.all().values_list("id", flat=True)
    if settings.ADMIN_ROLE_GROUP in user_groups:
        user_vuln_ids = Vulnerability.objects.filter(**vuln_params).values_list("id", flat=True)
    else:
        subdomain_ids = get_ur_subdomain(request.user)
        user_vuln_ids = Vulnerability.objects.filter(subdomain_id__in=subdomain_ids, **vuln_params).values_list("id", flat=True)

    if int(vuln_id) not in user_vuln_ids:
        return False, "当前资产超出查看范围，详情请联系单位管理员"
    vuln_qs = Vulnerability.objects.filter(id=int(vuln_id), **vuln_params)
    if not vuln_qs:
        return False, "数据不存在"
    setattr(request, "permission_qobject", vuln_qs)
    return True, "ok"


def vulnerability_vuln_risk_detail_put(request):
    """
    更新漏洞详情限制
    """
    vuln_params = {"company_id": request.user.company_id, "is_delete": 0}
    vuln_id = request.POST.get("id", None)
    if not vuln_id:
        return False, "参数不全"

    user_groups = request.user.groups.all().values_list("id", flat=True)
    if settings.ADMIN_ROLE_GROUP in user_groups:
        user_vuln_ids = Vulnerability.objects.filter(**vuln_params).values_list("id", flat=True)
    else:
        subdomain_ids = get_ur_subdomain(request.user)
        user_vuln_ids = Vulnerability.objects.filter(subdomain_id__in=subdomain_ids, **vuln_params).values_list("id", flat=True)

    if int(vuln_id) not in user_vuln_ids:
        return False, "当前资产超出查看范围，详情请联系单位管理员"
    vuln_qs = Vulnerability.objects.filter(id=int(vuln_id), **vuln_params)
    if not vuln_qs:
        return False, "数据不存在"

    setattr(request, "permission_qobject", vuln_qs)
    return True, "ok"



def user_user_site_vuln_get(request):
    subdomain_ids = get_ur_subdomain(request.user)
    vuln_qs = Vulnerability.objects.filter(is_delete=False, company_id=request.user.company_id)

    user_groups = request.user.groups.all().values_list("id", flat=True)
    if settings.ADMIN_ROLE_GROUP in user_groups:
        vuln_qs_ids = vuln_qs.values_list("id", flat=True)
    else:
        vuln_qs_ids = vuln_qs.filter(subdomain_id__in=subdomain_ids).values_list("id", flat=True)

    setattr(request, "permission_qids", set(vuln_qs_ids))
    return True, "ok"


def user_user_site_info_get(request):

    return True, ""


