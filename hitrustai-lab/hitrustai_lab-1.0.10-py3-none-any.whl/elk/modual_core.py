import pandas as pd
import numpy as np
import sys
import re
from unittest import result
from hitrustai_lab.orm import Orm, get_orm_profile
from hitrustai_lab.orm.Tables.TBMarchant import TbmerchantriskValidationReport, TBmerchantRiskInfo, TBmerchantRiskPredictresult


class UpdateELKAPI:
    def __init__(self, dict_arg):
        self.ELK = dict_arg["obj_ELK"]
        self.table_reason = dict_arg["table_reason"]
        self.abnormal_threshold = dict_arg["abnormal_threshold"]
        self.INDEX_NAME = {
            'info': f'{dict_arg["DATA_SOURCE"]}_{dict_arg["modual_name"]}_info_data',
            'result': f'{dict_arg["DATA_SOURCE"]}_{dict_arg["modual_name"]}_result_data',
            'predict': f'{dict_arg["DATA_SOURCE"]}_{dict_arg["modual_name"]}_predict_data'
        }
        self.associationkey = {
            'info': dict_arg["info_id"],
            'result': dict_arg["result_id"]
            
        }
        self.realTime_mode = dict_arg["realTime_mode"]
        if not dict_arg["realTime_mode"]:
            self.n_rows = dict_arg["n_rows"]
            self.orm = Orm(profile=get_orm_profile(
                host=dict_arg["db_config"]["DB_HOST"],
                db=dict_arg["db_config"]["DB_NAME"],
                user=dict_arg["db_config"]["DB_USERNAME"],
                pwd=dict_arg["db_config"]["DB_PASS"],
                port=dict_arg["db_config"]["DB_PORT"]
            ))

    def get_update_data(self):
        info_start_point = self.ELK.get_start_time(self.INDEX_NAME['info'], date_col='pk_id')
        result_start_point = self.ELK.get_start_time(self.INDEX_NAME['result'], date_col='pk_id')

        if info_start_point is None:
            info_data = self.orm.elk_query_filter(self.dict_arg["orm_predict_info"], self.n_rows)
            result_data = self.orm.elk_query_filter(self.dict_arg["orm_predict_result"], self.n_rows)
        else:
            info_data = self.orm.elk_query_filter(self.dict_arg["orm_predict_info"], self.n_rows, (self.dict_arg["orm_predict_info"].pk_id > info_start_point))
            result_data = self.orm.elk_query_filter(self.dict_arg["orm_predict_result"], self.n_rows, (self.dict_arg["orm_predict_result"].pk_id > result_start_point))

        if info_data.shape[0] == 0 and result_data.shape[0] == 0:
            print(self.dict_arg["modual_name"] + ' Upload Complete ! ')
            return None
        elif info_data.shape[0] == 0 and result_data.shape[0] != 0:
            return {
                'result': result_data
            }
        elif info_data.shape[0] != 0 and result_data.shape[0] == 0:
            return {
                'info': info_data
            }
        else:
            predict_data = self.orm.elk_query_filter(self.dict_arg["orm_predict_result"], self.n_rows, (self.dict_arg["orm_result_id"].in_(info_data['pk_id'].tolist())))
            info_data, predict_data, merge_data = self.preprocess(info_data, predict_data)
            return {
                'info': info_data,
                'result': result_data,
                'predict': merge_data
            }

    def preprocess(self, info_data, result_data):
        merge_data = pd.merge(info_data, result_data, left_on=['pk_id'], right_on=[self.dict_arg["result_id"]], how='inner')
        merge_data = merge_data.reset_index(drop=True)

        # column rename
        merge_data.rename(columns={"pk_id_x": "pk_id", "create_time_y": "create_time","serial_number_x":"serial_number"}, inplace=True)
        merge_data.drop(["pk_id_y", "create_time_x","serial_number_y"], axis=1, inplace=True)
        
        modual_types = list(self.table_reason.keys())
        list_columns_ = []
        list_columns = []
        for modual_name_column in modual_types:
            modual_name = modual_name_column.split("_reason")[0]
            list_columns.append(modual_name)
            merge_data[modual_name_column] = self.table_reason[modual_name_column](merge_data[modual_name_column])
            merge_data[modual_name_column] = merge_data[modual_name_column].astype(str)
            merge_data[modual_name_column + '_'] = np.where(merge_data[modual_name + '_score'] > 0.5, merge_data[modual_name_column], 'nan')
            list_columns_.append(modual_name_column + '_')
        merge_data['abnormal_reason_'] = merge_data[list_columns_].agg(', '.join, axis=1)
        merge_data['abnormal_reason_'] = merge_data['abnormal_reason_'].str.replace(' nan,', '')
        merge_data['abnormal_reason_'] = merge_data['abnormal_reason_'].str.replace('nan, ', '')
        merge_data['abnormal_reason_'] = merge_data['abnormal_reason_'].str.replace(' nan', '')

        merge_data['abnormal_threshold'] = self.abnormal_threshold 
        merge_data['true_label'] = 0
        merge_data["predict_label"] = np.where(merge_data.total_score > self.abnormal_threshold, 1, 0)
        for modual_name in list_columns:
            merge_data[modual_name + "_label"] = np.where(merge_data[modual_name + "_score"] > self.abnormal_threshold, 1, 0)
        # tp fp tn fn
        merge_data['normal_tp'] = np.where(((merge_data["predict_label"] == 0) & (merge_data["predict_label"] == merge_data['true_label'])), 1, 0)
        merge_data['normal_tn'] = np.where(((merge_data["predict_label"] == 1) & (merge_data["predict_label"] == merge_data['true_label'])), 1, 0)
        merge_data['normal_fn'] = np.where(((merge_data["predict_label"] == 1) & (merge_data['true_label'] == 0)), 1, 0)
        merge_data['normal_fp'] = np.where(((merge_data["predict_label"] == 0) & (merge_data["true_label"] == 1)), 1, 0)
        merge_data['abnormal_tp'] = merge_data['normal_tn'].copy()
        merge_data['abnormal_tn'] = merge_data['normal_tp'].copy()
        merge_data['abnormal_fn'] = merge_data['normal_fp'].copy()
        merge_data['abnormal_fp'] = merge_data['normal_fn'].copy()
        merge_data['abnormal_count'] = merge_data['normal_tn'] + merge_data['normal_fn']

        merge_data['year_month'] = pd.to_datetime(merge_data['create_time']).dt.to_period('M').astype(str)
        merge_data['year_month_week'] = pd.to_datetime(merge_data['create_time']).dt.to_period('W').astype(str)
        merge_data['year_date'] = merge_data['create_time'].dt.date
        return info_data, result_data, merge_data

    def get_mappings(self, data):
        dict_type = {}
        for key, value in zip(data.columns, data.dtypes.values):
            if key in ['customer_id', 'profile_id', 'tag', 'model_id', 'training_id', 'data_version', 'mac', 'timestamp', 'udid', 'merchant_id']:
                dict_type[key] = {"type": "text", "fields": {"keyword": {"type": "keyword"}}}
            elif value == 'int64':
                dict_type[key] = {"type": "integer", "fields": {"keyword": {"type": "keyword"}}}
            elif value == 'float64' or 'score' in key:
                dict_type[key] = {"type": "scaled_float", "scaling_factor": 100, "fields": {"keyword": {"type": "keyword"}}}
            elif value == 'O':
                dict_type[key] = {"type": "text", "fields": {"keyword": {"type": "keyword"}}}
            elif 'create_time' in key or 'date' in key:
                dict_type[key] = {"type": "date"}
            else:
                dict_type[key] = {"type": "text", "fields": {"keyword": {"type": "keyword"}}}
        mappings = {
            "mappings": {
                "properties": dict_type
            }
        }
        return mappings

    def elk_insert(self, data_dict=None):
        if self.realTime_mode:
            for key, data in data_dict.items():
                data = data.fillna('undefined')
                mappings = self.get_mappings(data)
                self.ELK.create_index(self.INDEX_NAME[key], mappings)
                result = self.ELK.insert_data(data, self.INDEX_NAME[key])
            del data_dict
            if len(result['fails']) > 0:
                return False
            else:
                return True
        else:
            while True:
                data_dict = self.get_update_data()
                if data_dict != None:
                    for key, data in data_dict.items():
                        data = data.fillna('undefined')
                        mappings = self.get_mappings(data)
                        self.ELK.create_index(self.INDEX_NAME[key], mappings)
                        self.ELK.insert_data(data, self.INDEX_NAME[key])
                    del data_dict
                else:
                    break


if __name__ == '__main__':
    def modify_deviceconsistency_reason(deviceconsistency_reason):
        if deviceconsistency_reason == 'DeviceConsistency-normal':
            deviceconsistency_reason = deviceconsistency_reason.replace('DeviceConsistency-normal', 'Device Consistency - Normal')
        elif deviceconsistency_reason == 'DeviceConsistency-abnormal':
            deviceconsistency_reason = deviceconsistency_reason.replace('DeviceConsistency-abnormal', 'Device Consistency - Abnormal')
        elif deviceconsistency_reason == 'DeviceConsistency-abnormal(ua_model)':
            deviceconsistency_reason = deviceconsistency_reason.replace('DeviceConsistency-abnormal(ua_model)', 'Device Consistency - Abnormal(UA anomaly)')
        return deviceconsistency_reason

    def modify_internetinfo_reason(internetinfo_reason):
        if bool(re.search("InternetInfo-normal", internetinfo_reason)):
            internetinfo_reason = internetinfo_reason.replace('InternetInfo-normal', 'Internet Info - Normal')
        elif bool(re.search("InternetInfo-abnormal", internetinfo_reason)):
            internetinfo_reason = internetinfo_reason.replace('InternetInfo-abnormal', 'Internet Info - Abnormal')
        internetinfo_reason = internetinfo_reason.replace('conflictlanguage', 'language inconsistent in os and browser')
        internetinfo_reason = internetinfo_reason.replace('diffTimezonIPrequestOs', 'timezone inconsistent in ip and os')
        internetinfo_reason = internetinfo_reason.replace('diffTimezonIPrequestOs_withoutTool', 'timezone inconsistent in ip(without proxy) and os')
        internetinfo_reason = internetinfo_reason.replace('diffUseragent', 'request UA and source UA is inconsistent')
        internetinfo_reason = internetinfo_reason.replace('ip_is_tor', 'ip is tor')
        internetinfo_reason = internetinfo_reason.replace('ip_is_proxy', 'ip is proxy')
        internetinfo_reason = internetinfo_reason.replace('ip_cloud_server', 'ip cloud server')
        return internetinfo_reason

    def modify_personaldevice_reason(personaldevice_reason):
        if personaldevice_reason == 'PersonalDevice-normal':
            personaldevice_reason = personaldevice_reason.replace('PersonalDevice-normal', 'Personal Device - Normal')
        elif personaldevice_reason == 'PersonalDevice-normal(NoEnoughHistoryData)':
            personaldevice_reason = personaldevice_reason.replace('PersonalDevice-normal(NoEnoughHistoryData)', 'Insufficient Device Historical Data')
        elif personaldevice_reason == 'PersonalDevice-abnormal(ip_is_proxy)':
            personaldevice_reason = personaldevice_reason.replace('PersonalDevice-abnormal(ip_is_proxy)', 'Personal Device - Abnormal(ip is proxy)')
        elif personaldevice_reason == 'PersonalDevice-abnormal(ip_is_tor)':
            personaldevice_reason = personaldevice_reason.replace('PersonalDevice-abnormal(ip_is_tor)', 'Personal Device - Abnormal(ip is tor)')
        elif personaldevice_reason == 'PersonalDevice-abnormal(ip_is_vpn)':
            personaldevice_reason = personaldevice_reason.replace('PersonalDevice-abnormal(ip_is_vpn)', 'Personal Device - Abnormal(ip is vpn)')
        elif personaldevice_reason == 'PersonalDevice-abnormal(browser_name)':
            personaldevice_reason = personaldevice_reason.replace('PersonalDevice-abnormal(browser_name)', 'Personal Device - Abnormal(browser name infrequently used)')
        elif personaldevice_reason == 'PersonalDevice-abnormal(browser_language)':
            personaldevice_reason = personaldevice_reason.replace('PersonalDevice-abnormal(browser_language)', 'Personal Device - Abnormal(browser language infrequently used)')
        elif personaldevice_reason == 'PersonalDevice-abnormal(os_screen_resolution)':
            personaldevice_reason = personaldevice_reason.replace('PersonalDevice-abnormal(os_screen_resolution)', 'Personal Device - Abnormal(os screen resolution infrequently used)')
        elif personaldevice_reason == 'PersonalDevice-abnormal(os_local_timezone_offset)':
            personaldevice_reason = personaldevice_reason.replace('PersonalDevice-abnormal(os_local_timezone_offset)', 'Personal Device - Abnormal(os local timezone offset infrequently used)')
        elif personaldevice_reason == 'PersonalDevice-abnormal(os_screen_orientation)':
            personaldevice_reason = personaldevice_reason.replace('PersonalDevice-abnormal(os_screen_orientation)', 'Personal Device - Abnormal(os screen orientation infrequently used)')
        elif personaldevice_reason == 'PersonalDevice-abnormal(browser_is_private_mode)':
            personaldevice_reason = personaldevice_reason.replace('PersonalDevice-abnormal(browser_is_private_mode)', 'Personal Device - Abnormal(browser is private mode)')
        return personaldevice_reason

    dict_arg = {
        "obj_ELK": obj_ELK,
        "DATA_SOURCE": "",
        "db_config": dict(),
        "n_rows": "100000",
        "modual_name": "tb_model_fraud_detect",
        "realTime_mode": False,
        "orm_train_report": TbmerchantriskValidationReport,
        "orm_predict_info": TBmerchantRiskInfo,
        "orm_predict_result": TBmerchantRiskPredictresult,
        "table_reason": {
            "device_consistency_reason": np.vectorize(modify_deviceconsistency_reason, otypes=[str]),
            "internet_info_reason": np.vectorize(modify_internetinfo_reason, otypes=[str]),
            "personal_device_reason": np.vectorize(modify_personaldevice_reason, otypes=[str])
        },
        "abnormal_threshold": 0.5,
        "info_id" : "pk_id",
        "result_id" : "mr_info_id"
    }
    UpdateELKAPI(dict_arg)

