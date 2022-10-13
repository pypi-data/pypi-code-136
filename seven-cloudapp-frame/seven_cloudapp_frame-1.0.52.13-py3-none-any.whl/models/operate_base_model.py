# -*- coding: utf-8 -*-
"""
@Author: HuangJianYi
@Date: 2021-12-20 16:07:52
@LastEditTime: 2022-10-10 14:48:31
@LastEditors: HuangJianYi
@Description: 操作日志相关处理业务模型
"""
from seven_framework import *
from seven_cloudapp_frame.libs.customize.seven_helper import SevenHelper
from seven_cloudapp_frame.models.seven_model import *
from asq.initiators import query

from seven_cloudapp_frame.models.db_models.operation.operation_log_model import *
from seven_cloudapp_frame.models.db_models.operation.operation_config_model import *

class OperateBaseModel():
    """
    :description: 操作日志相关处理业务模型
    """
    def __init__(self, context=None, logging_error=None, logging_info=None):
        self.context = context
        self.logging_link_error = logging_error
        self.logging_link_info = logging_info

    
    def get_operate_log_list(self, model_name="", operation_type=-1, page_index = 0, page_size = 10, is_contrast = False, is_all_fields=False):
        """
        :description:  获取操作日志列表
        :param model_name:模块或表名称
        :param operation_type:操作类型
        :param page_index:页数
        :param page_size:条数
        :param is_contrast:是否对比新旧值返回contrast_info
        :param is_all_fields:是否返回所有匹配的字段包含没有变动的字段
        :return list: 
        :last_editors: HuangJianYi
        """
        operation_log_model = OperationLogModel(context=self.context)
        condition_where = ConditionWhere()
        params = []
        if model_name:
            condition_where.add_condition("model_name=%s")
            params.append(model_name)
        if operation_type != -1:
            condition_where.add_condition("operation_type=%s")
            params.append(operation_type)

        operation_log_list,total = operation_log_model.get_dict_page_list("*", page_index, page_size, condition_where.to_string(),"","id desc", params=params)
        for operation_log in operation_log_list:
            operation_log["detail"] = SevenHelper.json_loads(operation_log["detail"]) if operation_log["detail"] else {}
            operation_log["update_detail"] = SevenHelper.json_loads(operation_log["update_detail"]) if operation_log["update_detail"] else {}
            if is_contrast:
                operation_log = self.get_contrast_info(operation_log, is_all_fields)
        return operation_log_list,total

    
    def get_operate_log(self,id, is_contrast = True, is_all_fields=False):
        """
        :description:  获取操作日志列表
        :param id:操作日志标识
        :param model_name:模块或表名称
        :param operation_type:操作类型
        :param page_index:页数
        :param page_size:条数
        :param is_contrast:是否对比新旧值返回contrast_info
        :param is_all_fields:是否返回所有匹配的字段包含没有变动的字段
        :return list: 
        :last_editors: HuangJianYi
        """
        operation_log_model = OperationLogModel(context=self.context)
        operation_log = operation_log_model.get_dict_by_id(id)
        if is_contrast and operation_log:
            operation_log["detail"] = SevenHelper.json_loads(operation_log["detail"]) if operation_log["detail"] else {}
            operation_log["update_detail"] = SevenHelper.json_loads(operation_log["update_detail"]) if operation_log["update_detail"] else {}
            operation_log = self.get_contrast_info(operation_log, is_all_fields)
        return operation_log
    
    
    def _convert_remark(self,config_fields, value):
        """
        :description:  转换备注
        :param config_fields:配置字段
        :param value:处理值
        :return: 
        :last_editors: HuangJianYi
        """
        db = None
        value_remark = "-"
        if value not in [None,""]:
            read_config = config_fields.get("read_config",{})
            if len(read_config) > 0:
                db = MySQLHelper(config.get_value(OperationLogModel(context=self.context).db_connect_key))
                sql = "select %s from %s where %s=%s limit 1;" % (str(read_config["return_field"]), str(read_config["table_name"]), str(read_config["search_field"]), str(value))
                result = db.query(sql)
                if result:
                    value_remark = result[0][str(read_config["return_field"])] if result[0][str(read_config["return_field"])] else "-"
                else:
                    value_remark = "-"
            elif len(config_fields.get("value", {})) > 0:
                default = config_fields.get("value", {}).get("default", "")
                if default:
                    value_remark = default.replace("{0}", str(value))
                else:
                    value_remark = config_fields.get("value", {}).get(str(value), "-")
            elif value != "":
                value_remark = value
            else:
                value_remark = "-"
        return value_remark
        

    def get_contrast_info(self, operation_log, is_all_fields=False):
        """
        :description:  获取操作日志对比信息
        :param operation_log:日志信息字典
        :param is_all_fields:是否返回所有匹配的字段包含没有变动的字段
        :return info: 
        :last_editors: HuangJianYi
        """
        try:
            operation_log["contrast_info"] = []
            if operation_log["update_detail"] and isinstance(operation_log["update_detail"], dict):
                operation_config_model = OperationConfigModel(context=self.context)
                operation_config = operation_config_model.get_cache_dict("model_name=%s",params=[operation_log["model_name"]])
                for key in operation_log["update_detail"]:
                    old_value_remark = ""
                    new_value_remark = ""
                    if not operation_config:
                        config_fields = query(config.get_value("operate_log_config", {}).get(operation_log["model_name"], [])).where(lambda x: x["field"] == key).first_or_default(None)
                    else:
                        config_json = SevenHelper.json_loads(operation_config["config_json"]) if operation_config["config_json"] else {}
                        config_fields =  query(config_json).where(lambda x: x["field"] == key).first_or_default(None)
                    if not config_fields:
                        continue
                    old_value = operation_log["detail"].get(key, "")
                    new_value = operation_log["update_detail"].get(key, "")
                    old_value_remark = self._convert_remark(config_fields, old_value)
                    new_value_remark = self._convert_remark(config_fields, new_value)
                    if is_all_fields == True:
                        info = {}
                        info["field"] = key
                        info["old_value"] = old_value
                        info["new_value"] = new_value
                        info["is_update"] = 1 if info["old_value"] != info["new_value"] else 0
                        info["remark"] = config_fields.get("remark","-")
                        info["old_value_remark"] = old_value_remark
                        info["new_value_remark"] = new_value_remark
                        operation_log["contrast_info"].append(info)
                    else:
                        if new_value != old_value:
                            info = {}
                            info["field"] = key
                            info["old_value"] = old_value
                            info["new_value"] = new_value
                            info["is_update"] = 1
                            info["remark"] = config_fields.get("remark", "-")
                            info["old_value_remark"] = old_value_remark
                            info["new_value_remark"] = new_value_remark
                            operation_log["contrast_info"].append(info)
        except Exception as ex:
            if self.context:
                self.context.logging_link_error("【获取操作日志对比信息】" + traceback.format_exc())
            elif self.logging_link_error:
                self.logging_link_error("【获取操作日志对比信息】" + traceback.format_exc())
        return operation_log
