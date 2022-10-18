import logging
import random

import requests
import time

from django.forms import model_to_dict
from django.utils import timezone
from lxml import etree as et
from pathlib import Path

from xj_finance.services.finance_transact_service import FinanceTransactService
from xj_enroll.service.enroll_services import EnrollServices
from xj_thread.services.thread_item_service import ThreadItemService
from xj_user.services.user_service import UserService
from xj_payment.models import PaymentPayment
from ..utils.wechat_utils import my_ali_pay
from main.settings import BASE_DIR
from ..utils.j_config import JConfig
from ..utils.j_dict import JDict
from wechatpy.utils import random_string, to_text
from rest_framework import status
from django.http import HttpResponse

module_root = str(Path(__file__).resolve().parent)
# 配置之对象
main_config_dict = JDict(JConfig.get_section(path=str(BASE_DIR) + "/config.ini", section="xj_payment"))
module_config_dict = JDict(JConfig.get_section(path=str(BASE_DIR) + "/config.ini", section="xj_payment"))

sub_appid = main_config_dict.wechat_merchant_app_id or module_config_dict.wechat_merchant_app_id or ""

sub_app_secret = main_config_dict.wechat_merchant_app_secret or module_config_dict.wechat_merchant_app_secret or ""

sub_mch_id = main_config_dict.wechat_merchant_mch_id or module_config_dict.wechat_merchant_mch_id or ""

trade_type = main_config_dict.wechat_trade_type or module_config_dict.wechat_trade_type or ""
# 交易类型，小程序取值：JSAPI

# 商品描述，商品简单描述
description = main_config_dict.wechat_body or module_config_dict.wechat_body or ""
# 标价金额，订单总金额，单位为分
total_fee = main_config_dict.wechat_total_fee or module_config_dict.wechat_total_fee or ""
# 通知地址，异步接收微信支付结果通知的回调地址，通知url必须为外网可访问的url，不能携带参数。
notify_url = main_config_dict.wechat_notify_url or module_config_dict.wechat_notify_url or ""

# 用户标识，trade_type=JSAPI，此参数必传，用户在商户appid下的唯一标识。
# print("<trade_type>", trade_type)

url = "https://api.mch.weixin.qq.com/v3/pay/partner/transactions/jsapi"

logger = logging.getLogger(__name__)


class PaymentWechatService:

    @staticmethod
    def get_user_info(code):
        # https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx0c2a8db23b2e7c28&redirect_uri=REDIRECT_URI&response_type=code&scope=snsapi_userinfo&state=STATE#wechat_redirect
        req_params = {
            'appid': sub_appid,
            'secret': sub_app_secret,
            'js_code': code,
            'grant_type': 'authorization_code',
        }
        user_info = requests.get('https://api.weixin.qq.com/sns/jscode2session', params=req_params, timeout=3,
                                 verify=False)
        return user_info.json()

    # 微信小程序支付
    @staticmethod
    def payment_applets_pay(params):

        out_trade_no = timezone.now().strftime('%Y%m%d%H%M%S') + ''.join(map(str, random.sample(range(0, 9), 4)))
        data, err_txt = EnrollServices.enroll_detail(params['enroll_id'])
        if err_txt:
            return "报名记录不存在"
        # UserSsoServeService.user_sso_to_user(data['user_id'])
        payment_data = {
            "order_no": out_trade_no,
            "enroll_id": data['id'],
            "user_id": data['user_id'],
            "total_amount": int(params['total_fee']),
            "create_time": timezone.localtime(),
        }
        pay = my_ali_pay()
        order = pay.order.create(
            trade_type="JSAPI",  # 交易类型，小程序取值：JSAPI
            body=description,  # 商品描述，商品简单描述
            total_fee=int(params['total_fee']),  # 标价金额，订单总金额，单位为分
            notify_url=notify_url,  # 通知地址，异步接收微信支付结果通知的回调地址，通知url必须为外网可访问的url，不能携带参数。
            sub_mch_id=sub_mch_id,
            sub_appid=sub_appid,
            sub_user_id=params['openid'],  # 用户标识，trade_type=JSAPI，此参数必传，用户在商户appid下的唯一标识。
            out_trade_no=out_trade_no
        )
        wxpay_params = pay.jsapi.get_jsapi_params(order['prepay_id'])
        PaymentPayment.objects.create(**payment_data)
        # wxpay_params = PaymentWechatService.get_jsapi_params(order['prepay_id'])
        return wxpay_params

        # 微信扫码支付

    # @staticmethod
    # def get_jsapi_params(prepay_id, timestamp=None, nonce_str=None, jssdk=False):
    #     """
    #     获取 JSAPI 参数
    #
    #     :param prepay_id: 统一下单接口返回的 prepay_id 参数值
    #     :param timestamp: 可选，时间戳，默认为当前时间戳
    #     :param nonce_str: 可选，随机字符串，默认自动生成
    #     :param jssdk: 前端调用方式，默认使用 WeixinJSBridge
    #                   使用 jssdk 调起支付的话，timestamp 的 s 为小写
    #                   使用 WeixinJSBridge 调起支付的话，timeStamp 的 S 为大写
    #     :return: 参数
    #     """
    #     data = {
    #         'appId': sub_appid,
    #         'timeStamp': timestamp or to_text(int(time.time())),
    #         'nonceStr': nonce_str or random_string(32),
    #         'package': 'prepay_id={0}'.format(prepay_id),
    #     }
    #     # sign = calculate_sign(data, "POST", url, data['timeStamp'], data['nonceStr'])
    #     sign = get_pay_sign_info(data, prepay_id)
    #     logger.debug('JSAPI payment parameters: data = %s, sign = %s', data, sign)
    #     data['paySign'] = sign
    #     if jssdk:
    #         data['timestamp'] = data.pop('timeStamp')
    #     return data

    # 微信扫码支付
    @staticmethod
    def payment_scan_pay(params):
        pay = my_ali_pay()
        order = pay.order.create(
            trade_type="NATIVE",  # 交易类型，小程序取值：JSAPI
            body=description,  # 商品描述，商品简单描述
            total_fee=params['total_fee'],  # 标价金额，订单总金额，单位为分
            notify_url=notify_url,  # 通知地址，异步接收微信支付结果通知的回调地址，通知url必须为外网可访问的url，不能携带参数。
            sub_mch_id=sub_mch_id,
            sub_appid=sub_appid,
            out_trade_no=params['out_trade_no']
        )
        wxpay_params = pay.jsapi.get_jsapi_params(order['prepay_id'])
        # sign = calculate_sign(body, "POST", self.url, timestamp, nonce_str)
        return wxpay_params

    @staticmethod
    def callback(_xml):
        """
        <xml><appid><![CDATA[wx56232dd67c7e5a18]]></appid> 微信分配的小程序ID
        <bank_type><![CDATA[CFT]]></bank_type>付款银行
        <cash_fee><![CDATA[1]]></cash_fee>现金支付金额订单现金支付金额
        <fee_type><![CDATA[CNY]]></fee_type>货币类型
        <is_subscribe><![CDATA[N]]></is_subscribe>用户是否关注公众账号，Y-关注，N-未关注
        <mch_id><![CDATA[1521497251]]></mch_id>微信支付分配的商户号
        <nonce_str><![CDATA[1546088296922]]></nonce_str>随机字符串，不长于32位
        <openid><![CDATA[oEHJT1opJZLYBWssRlyjq9bSdnao]]></openid>用户在商户appid下的唯一标识
        <out_trade_no><![CDATA[10657298351779092719122609746693]]></out_trade_no>商户系统内部订单号，要求32个字符内
        <result_code><![CDATA[SUCCESS]]></result_code>业务结果 SUCCESS/FAIL
        <return_code><![CDATA[SUCCESS]]></return_code>返回状态码 return_code
        <sign><![CDATA[2EB71F6237E04C3DA4B1509A502E8F62]]></sign>签名
        <time_end><![CDATA[20181229205830]]></time_end>支付完成时间
        <total_fee>1</total_fee>订单总金额，单位为分
        <trade_type><![CDATA[MWEB]]></trade_type>交易类型 JSAPI、NATIVE、APP
        <transaction_id><![CDATA[4200000224201812291041578058]]></transaction_id>微信支付订单号
        </xml>
        """

        # _xml = request.body
        # 拿到微信发送的xml请求 即微信支付后的回调内容
        xml = str(_xml, encoding="utf-8")
        return_dict = {}
        tree = et.fromstring(xml)
        # xml 解析
        return_code = tree.find("return_code").text
        try:
            if return_code == 'FAIL':
                # 官方发出错误
                return_dict['message'] = '支付失败'
                logging.error("微信支付失败")
                # return Response(return_dict, status=status.HTTP_400_BAD_REQUEST)
            elif return_code == 'SUCCESS':
                # 拿到自己这次支付的 out_trade_no
                out_trade_no = tree.find("out_trade_no").text  # 订单号
                total_fee = tree.find("total_fee").text  # 金额（单位分）
                transaction_id = tree.find("transaction_id").text  # 微信支付订单号
                # 根据订单号查询支付记录是否存在
                payment = PaymentPayment.objects.filter(order_no=int(out_trade_no)).first()
                payment_message = model_to_dict(payment)
                # 根据支付记录用户 查询用户基本信息
                user_set, err = UserService.user_basic_message(payment_message['user_id'])
                project_name = None
                summary = None
                if user_set:
                    if payment_message['enroll_id']:
                        # 如果存在报名id 查询报名记录
                        enroll_set, err = EnrollServices.enroll_detail(payment_message['enroll_id'])
                        if enroll_set:
                            # 报名表支付状态修改
                            enroll_data = {
                                "enroll_status_code": "422",
                                "paid_amount": total_fee
                            }
                            enroll_data, enroll_err_txt = EnrollServices.enroll_edit(enroll_data,
                                                                                     payment_message['enroll_id'])
                            if enroll_err_txt:
                                logging.info("payment_callback_enroll" + enroll_err_txt)
                            # 根据报名记录获取 信息模块项目基本信息
                            thread_set, err = ThreadItemService.detail(enroll_set['thread_id'])
                            if thread_set:
                                project_name = thread_set['title']
                    summary = "【" + user_set['full_name'] + "】支付 【" + project_name + "】款项"
                # # TODO 拿到订单号后的操作 看自己的业务需求
                # 资金写入
                finance_data = {
                    "order_no": out_trade_no,
                    "account_id": payment_message['user_id'],
                    "enroll_id": payment_message['enroll_id'],
                    "transact_id": transaction_id,
                    "their_account_id": "1",
                    "platform": "muzpay",
                    "amount": total_fee,
                    "currency": "CNY",
                    "pay_mode": "WECHAT",
                    "summary": summary
                }
                funance_add_data, err_txt = FinanceTransactService.post(finance_data)
                if err_txt:
                    logging.info("payment_callback" + err_txt)
                # 根据唯一交易id 查询主键id
                funance_data, err = FinanceTransactService.finance_transact_detailed(transaction_id)
                if funance_data:
                    funance_data = model_to_dict(funance_data)
                    payment_data = {
                        "transact_no": transaction_id,
                        "transact_id": funance_data['id'],
                        "order_status_id": "24"
                    }
                    # 更改支付记录
                    PaymentPayment.objects.filter(order_no=int(out_trade_no)).update(**payment_data)

                return_dict['message'] = '支付成功'
                logging.info("payment_callback" + "微信支付成功")
        except Exception as e:
            return_dict['message'] = e
        finally:
            return return_dict
