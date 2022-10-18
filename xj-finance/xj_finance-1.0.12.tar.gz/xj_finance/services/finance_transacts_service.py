import math
import random
import time
import os
from decimal import Decimal

import pytz
from django.db.models import Q
from django.utils import timezone
from django.utils.datetime_safe import datetime
from rest_framework import serializers
from django.db.models import Q, F
from django.db.models import Sum, Count
from xj_user.models import BaseInfo, Platform
from xj_user.services.user_platform_service import UserPlatformService

from ..utils.jt import Jt
from ..models import Transact, Currency, PayMode, SandBox
from .finance_service import FinanceService


# 声明用户序列化
class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return BaseInfo.objects.create(**validated_data)

    class Meta:
        model = BaseInfo
        # 序列化验证检查，是否要必填的字典
        fields = ['id', 'platform_uid', 'full_name', 'platform_id']


class FinanceTransactsSerializer(serializers.ModelSerializer):
    # 方法一：使用SerializerMethodField，并写出get_platform, 让其返回你要显示的对象就行了
    # p.s.SerializerMethodField在model字段显示中很有用。
    # order = serializers.SerializerMethodField()
    lend = serializers.SerializerMethodField()
    amount = serializers.SerializerMethodField()
    balance = serializers.SerializerMethodField()
    transact_time = serializers.SerializerMethodField()
    # transact_timestamp = serializers.SerializerMethodField()
    sand_box = serializers.SerializerMethodField()

    # # 方法二：增加一个序列化的字段platform_name用来专门显示品牌的name。当前前端的表格columns里对应的’platform’列要改成’platform_name’
    # account_id = serializers.ReadOnlyField(source='account.id')
    account_name = serializers.ReadOnlyField(source='account.full_name')
    # their_account_id = serializers.ReadOnlyField(source='their_account.id')
    their_account_name = serializers.ReadOnlyField(source='their_account.full_name')
    # platform_id = serializers.ReadOnlyField(source='platform.platform_id')
    # platform_name = serializers.ReadOnlyField(source='platform.platform_name')
    # platform = serializers.ReadOnlyField(source='platform.platform_name')
    pay_mode = serializers.ReadOnlyField(source='pay_mode.pay_mode')
    currency = serializers.ReadOnlyField(source='currency.currency')
    # income = serializers.ReadOnlyField(source='income')
    # outgo = serializers.ReadOnlyField(source='outgo')

    class Meta:
        model = Transact
        fields = [
            # 'order',
            'id',
            'transact_id',
            'transact_time',
            # 'transact_timestamp',
            'platform_id',
            # 'platform_name',
            # 'platform',
            # 'account_id',
            'account_name',
            # 'their_account_id',
            'their_account_name',
            'order_no',
            'opposite_account',
            'summary',
            'currency',
            # 'income',
            # 'outgo',
            'lend',
            'amount',
            'balance',
            'pay_mode',
            # 'goods_info',
            # 'pay_info',
            'sand_box',
            'remark',
            'images',
        ]

    # def get_order(self, obj):
    #     print("get_order:", obj.id, obj, self)
    #     return 1

    def get_lend(self, obj):
        income = obj.income if obj.income is not None else Decimal(0)
        outgo = obj.outgo if obj.outgo is not None else Decimal(0)
        amount = income - outgo
        return '借' if amount < 0 else '贷' if amount > 0 else '平'

    def get_amount(self, obj):
        income = obj.income if obj.income is not None else Decimal(0)
        outgo = obj.outgo if obj.outgo is not None else Decimal(0)
        return income - outgo

    def get_balance(self, obj):
        balance = obj.balance
        return balance

    def get_sand_box(self, obj):
        return obj.sand_box.sand_box_name if obj.sand_box else None

    def get_transact_time(self, obj):
        return obj.transact_time.astimezone(tz=pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')

    # def get_transact_timestamp(self, obj):
    #     return int(obj.transact_time.timestamp())



class FinanceTransactsService:
    @staticmethod
    def get(params, user_id):
        # ========== 三、内容的类型准确性检查 ==========

        valid = FinanceService.check_filter_validity(params=params)
        print(">>> check_filter_validity", valid)
        if valid['err'] > 0:
            # return Response({'err': valid['err'], 'msg': valid['msg'], })
            return None, valid['msg']
        transacts = Transact.objects.filter(account_id=user_id).filter(**valid['query_dict'])
        transacts = transacts.order_by('-transact_time')

        print(">>> transacts: ", transacts)

        # statistic_list = []
        # aggr = transacts.aggregate(
        #     outgo=Sum('outgo', filter=Q(currency__currency='CNY')),
        #     income=Sum('income', filter=Q(currency__currency='CNY')),
        # )
        # aggr['income'] = aggr['income'] or Decimal(0.0)
        # aggr['outgo'] = aggr['outgo'] or Decimal(0.0)
        # aggr['balance'] = aggr['income'] - aggr['outgo']
        # statistic_list.append(aggr)

        # images = 'http://' + request.headers['Host'] + ''

        # ========== 四、相关前置业务逻辑处理 ==========


        # ========== 五、翻页 ==========

        page = int(params['page']) - 1 if 'page' in params else 0
        size = int(params['size']) if 'size' in params else 10

        total = transacts.count()

        current_page_set = transacts[page * size: page * size + size] if page >= 0 and size > 0 else transacts

        serializer = FinanceTransactsSerializer(current_page_set, many=True)

        res_list = []
        for i, it in enumerate(serializer.data):
            # print("current_page_set:", i, it)
            it['order'] = page * size + i + 1
            it['platform_name'] = params.get('platform', '')
            res_list.append(it)

        # return {'total': total, 'list': res_list, 'statistics': statistic_list}, None

        return {'size': int(size), 'page': int(page+1), 'total': total, 'list': res_list}, None

        # return {'total': total, 'list': res_list}, None
        # 翻译
        # output = _("Welcome to my site.")

        # return Response({
        #     'err': 0,
        #     'msg': 'OK',
        #     'data': {'total': total, 'list': res_list, 'statistics': statistic_list},
        #     # 'data': output,
        # })

    # 生成随机的4位数数字
    @staticmethod
    def random_four_int():
        str = ""
        for i in range(4):
            ch = chr(random.randrange(ord('0'), ord('9') + 1))
            str += ch
        return str
