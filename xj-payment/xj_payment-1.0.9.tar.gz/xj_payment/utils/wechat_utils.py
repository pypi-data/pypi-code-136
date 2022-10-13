import os
from pathlib import Path
from wechatpy import WeChatPay
from main.settings import BASE_DIR
from ..utils.j_config import JConfig
from ..utils.j_dict import JDict

module_root = str(Path(__file__).resolve().parent)
# 配置之对象
main_config_dict = JDict(JConfig.get_section(path=str(BASE_DIR) + "/config.ini", section="xj_payment"))
module_config_dict = JDict(JConfig.get_section(path=str(BASE_DIR) + "/config.ini", section="xj_payment"))
# 服务商商户的APPID
app_id = main_config_dict.wechat_service_app_id or module_config_dict.wechat_service_app_id or ""
app_secret = main_config_dict.wechat_service_app_secret or module_config_dict.wechat_service_app_secret or ""
mch_id = main_config_dict.wechat_service_mch_id or module_config_dict.wechat_service_mch_id or ""
merchant_key = main_config_dict.wechat_service_merchant_key or module_config_dict.wechat_service_merchant_key or ""

def my_ali_pay(notify_url=None):
    wechat = WeChatPay(
        app_id,
        merchant_key,
        mch_id,
    )
    return wechat
