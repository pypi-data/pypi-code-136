import re

from apiview.view import APIView
from django.views.decorators.http import require_http_methods

from xj_enroll.models import EnrollExtendField
from xj_enroll.service.subitem_service import SubitemService
from xj_user.utils.user_wrapper import user_authentication_wrapper
from ..utils.custom_response import util_response
from ..utils.model_handle import parse_data


def extend_filed_filter():
    try:
        extend_field_list = list(EnrollExtendField.objects.all().values("field_index", "alias_name"))
        extend_field_map = {i["field_index"]: i["alias_name"] for i in extend_field_list}
        return extend_field_map
    except Exception as e:
        print("扩展字段映射错误：", str(e))
        return {}


class SubitemApis(APIView):

    @require_http_methods(['GET'])
    @user_authentication_wrapper
    def list(self, *args, **kwargs, ):
        request_params = parse_data(self)
        data, err = SubitemService.list(params=request_params)
        extend_field_map = extend_filed_filter()
        result = []
        for item in data["list"]:
            tem_dict = {}
            for k, v in item.items():
                if not re.search("field_.*", k):
                    tem_dict[k] = v
                else:
                    alias = extend_field_map.get(k)
                    if alias:
                        tem_dict[alias] = v
            result.append(tem_dict)
        data["list"] = result
        if err:
            return util_response(err=1000, msg=data)
        return util_response(data=data)

    @require_http_methods(['POST'])
    def add(self, *args, **kwargs, ):
        params = parse_data(self)
        data, err = SubitemService.add(params)
        if err:
            return util_response(err=1000, msg=err)
        return util_response(data=data)
