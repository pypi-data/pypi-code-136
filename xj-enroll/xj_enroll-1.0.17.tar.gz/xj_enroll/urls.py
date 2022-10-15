from django.urls import re_path

from xj_enroll.api.subitem_apis import SubitemApis
from .api.enroll_apis import EnrollAPI
from .api.rarely_data_list_api import OtherListAPIView
from .api.record_apis import RecordAPI
from .api.rule_apis import RuleAPI
from .api.valuation_api import ValuationAPIView

urlpatterns = [
    # 报名API
    re_path(r'^list/?$', EnrollAPI.list),
    re_path(r'^detail/?(?P<enroll_id>\d+)?$', EnrollAPI.detail),
    re_path(r'^edit/?(?P<enroll_id>\d+)?$', EnrollAPI.edit),
    re_path(r'^delete/?(?P<enroll_id>\d+)?$', EnrollAPI.delete),
    re_path(r'^add/?$', EnrollAPI.add),
    re_path(r'^subitem_add/?$', SubitemApis.add),

    # re_path(r'^category_list/?$', CategoryApi.list),
    # re_path(r'^category_edit/?(?P<category_id>\d+)?$', CategoryApi.edit),
    # re_path(r'^category_delete/?(?P<category_id>\d+)?$', CategoryApi.delete),
    # re_path(r'^category_add/?$', CategoryApi.add),
    #
    # re_path(r'^classify_list/?$', ClassifyApi.list),
    # re_path(r'^classify_edit/?(?P<classify_id>\d+)?$', ClassifyApi.edit),
    # re_path(r'^classify_delete/?(?P<classify_id>\d+)?$', ClassifyApi.delete),
    # re_path(r'^classify_add/?$', ClassifyApi.add),

    # 报名规则
    re_path(r'^rule_list/?$', RuleAPI.list),
    re_path(r'^rule_edit/?(?P<rule_value_id>\d+)?$', RuleAPI.edit),
    re_path(r'^rule_delete/?(?P<rule_value_id>\d+)?$', RuleAPI.delete),
    re_path(r'^rule_add/?$', RuleAPI.add),
    re_path(r'^rule_group_list/?$', RuleAPI.group_list),  # 分组列表

    # 报名记录
    re_path(r'^record_list/?$', RecordAPI.list),
    re_path(r'^record_add/?$', RecordAPI.add),

    # 计价接口
    re_path(r'^valuation_item/?$', ValuationAPIView.list),

    # 非热更新列表返回
    re_path(r'^status_code/?$', OtherListAPIView.enroll_status_code),

]
