from django.db import models
from django.utils import timezone

# from apps.user.models import User
from xj_thread.models import Thread


# class EnrollCategory(models.Model):
#     """ Enroll_EnrollRuleGroup 报名规则组表表 """
#
#     class Meta:
#         db_table = 'enroll_category'
#         verbose_name_plural = '报名分类表'
#
#     id = models.BigAutoField(verbose_name='报名规则组ID', primary_key=True, null=False, auto_created=True, help_text='')
#     value = models.CharField(verbose_name='分类值', max_length=255, blank=True, null=True, help_text='')
#     description = models.CharField(verbose_name='分类描述', max_length=255, blank=True, null=True, help_text='')
#
#     def __str__(self):
#         return f"{self.value}"
#
#
# class EnrollClassify(models.Model):
#     """ Enroll_EnrollRuleGroup 报名规则组表表 """
#
#     class Meta:
#         db_table = 'enroll_classify'
#         verbose_name_plural = '报名类别ID表'
#
#     id = models.BigAutoField(verbose_name='报名规则组ID', primary_key=True, null=False, auto_created=True, help_text='')
#     category = models.ForeignKey(EnrollCategory, verbose_name='类别ID', on_delete=models.DO_NOTHING)
#     value = models.CharField(verbose_name='分类值', max_length=255, blank=True, null=True, help_text='')
#     description = models.CharField(verbose_name='分类描述', max_length=255, blank=True, null=True, help_text='')
#     icon = models.CharField(verbose_name='图标', max_length=255, blank=True, null=True, help_text='')
#
#     def __str__(self):
#         return f"{self.value}"


class EnrollStatusCode(models.Model):
    """ Enroll_EnrollRuleValuate 报名状态表 [1:N]"""

    class Meta:
        db_table = 'enroll_status_code'
        verbose_name_plural = '报名状态表'

    id = models.AutoField(verbose_name='ID', primary_key=True, null=False, auto_created=True)
    enroll_status_code = models.IntegerField(verbose_name='状态code', blank=True, null=True)
    value = models.CharField(verbose_name='状态值', max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.value}"


class EnrollRuleGroup(models.Model):
    """ Enroll_EnrollRuleGroup 报名规则组表表 """

    class Meta:
        db_table = 'enroll_rule_group'
        verbose_name_plural = '报名规则组表表'

    id = models.BigAutoField(verbose_name='报名规则组ID', primary_key=True, null=False, auto_created=True, help_text='')
    rule_group = models.CharField(verbose_name='规则组', max_length=255, blank=True, null=True, help_text='')
    category_id = models.IntegerField(verbose_name='类别ID', blank=True, null=True, help_text='')
    classifyt_id = models.IntegerField(verbose_name='分类ID', blank=True, null=True, help_text='')
    description = models.CharField(verbose_name='描述', max_length=255, blank=True, null=True, help_text='')

    def __str__(self):
        return f"{self.rule_group}"


class EnrollRuleValuate(models.Model):
    """ Enroll_EnrollRuleValuate 报名规则计价表 [1:N]"""

    class Meta:
        db_table = 'enroll_rule_valuate'
        verbose_name_plural = '报名规则计价表'

    id = models.AutoField(verbose_name='单项计价ID', primary_key=True, null=False, auto_created=True, help_text='')
    enroll_rule_group = models.ForeignKey(EnrollRuleGroup, verbose_name='报名规则组ID', db_column='enroll_rule_group_id', related_name='+', unique=False, on_delete=models.DO_NOTHING, help_text='')
    name = models.CharField(verbose_name='计价名称', max_length=255, blank=True, null=True, help_text='')
    type = models.CharField(verbose_name='表类型', max_length=255, blank=True, null=True, help_text='')
    field = models.CharField(verbose_name='字段', max_length=255, blank=True, null=True, help_text='')
    expression_string = models.CharField(verbose_name='逻辑表达式', max_length=255, blank=True, null=True, help_text='')

    def __str__(self):
        return f"{self.id}"


class Enroll(models.Model):
    """ 1、Enroll_Enroll 报名主表 """

    class Meta:
        db_table = 'enroll_enroll'
        verbose_name_plural = '1. 报名主表'

    trading_choice = [(0, 'None 未知'), (1, 'Sell 卖家'), (2, 'Buy 买家'), (3, 'Cooperate 合资'), ]
    bool_choice = [(0, '否'), (1, "是")]

    id = models.BigAutoField(verbose_name='ID', primary_key=True, null=False, auto_created=True, help_text='')
    thread_id = models.BigIntegerField(verbose_name='信息ID', blank=False, null=False, help_text='')
    trading_relate = models.IntegerField(verbose_name='买卖关系', choices=trading_choice, blank=True, null=True, help_text='1: Sell 卖家, 2: Buy 买家, 3: Cooperate 合资')
    region_code = models.IntegerField(verbose_name='行政区划编码', blank=True, null=True, help_text='详见GB/T2260《中华人民共和国行政区划代码》、GB/T10114《县以下行政区划代码编制规则》')
    occupy_room = models.CharField(verbose_name='占用房间号', max_length=255, blank=True, null=True, help_text='如填写占用房间号，则同一时段内不允许重复占用房间号')
    # category = models.ForeignKey(EnrollCategory, db_column="category_id", on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name="分类ID", help_text='')
    # classify = models.ForeignKey(EnrollClassify, db_column="classify_id", on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name="类别ID", help_text='')
    enroll_status_code = models.IntegerField(verbose_name='报名状态码', default=1, help_text='尚未开始/报名中/已结束等14个状态码', )
    min_number = models.IntegerField(verbose_name='最小起报人数', blank=True, null=True, help_text='', )
    max_number = models.IntegerField(verbose_name='最大报名人数', blank=True, null=True, help_text='')
    min_count_apiece = models.IntegerField(verbose_name='每人最小购买数', blank=True, null=True, help_text='')
    max_count_apiece = models.IntegerField(verbose_name='每人最大购买数', blank=True, null=True, help_text='')
    enroll_rule_group = models.ForeignKey(verbose_name='报名规则组', to=EnrollRuleValuate, db_column='enroll_rule_group_id', related_name='+', unique=False, blank=True, null=True,
                                          on_delete=models.DO_NOTHING, help_text='')
    price = models.DecimalField(verbose_name='单价', max_digits=32, decimal_places=8, default=0, db_index=True, help_text='')
    count = models.IntegerField(verbose_name='总数量', blank=True, null=True, help_text='')
    unit = models.CharField(verbose_name='单位', max_length=255, blank=True, null=True, help_text='')
    fee = models.DecimalField(verbose_name='小费', max_digits=32, decimal_places=2, db_index=True, blank=True, null=True, help_text='')
    reduction = models.DecimalField(verbose_name='商家减免', max_digits=32, decimal_places=2, db_index=True, default=0, help_text='商家减免额')
    subitems_amount = models.DecimalField(verbose_name='分项合计', max_digits=32, decimal_places=2, db_index=True, default=0, help_text='')
    amount = models.DecimalField(verbose_name='总收/付金额', max_digits=32, decimal_places=2, db_index=True, blank=True, null=True, help_text='')
    paid_amount = models.DecimalField(verbose_name='已收/付金额', max_digits=32, decimal_places=2, db_index=True, blank=True, null=True, help_text='')
    unpaid_amount = models.DecimalField(verbose_name='未收/付金额', max_digits=32, decimal_places=2, db_index=True, blank=True, null=True, help_text='补差价')
    commision = models.DecimalField(verbose_name='佣金', max_digits=32, decimal_places=2, db_index=True, default=0, help_text='每份提成')
    deposit = models.DecimalField(verbose_name='每份预付押金', max_digits=32, decimal_places=8, default=0, db_index=True, help_text='')
    hide_price = models.IntegerField(verbose_name='匿价', blank=True, null=True, help_text='', choices=bool_choice, default=0)
    hide_user = models.IntegerField(verbose_name='匿名', blank=True, null=True, help_text='', choices=bool_choice, default=0)
    has_repeat = models.IntegerField(verbose_name='有重复报名', blank=True, null=True, help_text='', choices=bool_choice, default=0)
    has_subitem = models.IntegerField(verbose_name='有分项', blank=True, null=True, help_text='', choices=bool_choice, default=0)
    has_audit = models.IntegerField(verbose_name='有审核', blank=True, null=True, help_text='', choices=bool_choice, default=1)
    need_vouch = models.IntegerField(verbose_name='需三方担保', choices=bool_choice, default=1, blank=True, null=True, help_text='需三方担保')
    need_deposit = models.IntegerField(verbose_name='需押金', choices=bool_choice, default=1, blank=True, null=True, help_text='')
    need_imprest = models.IntegerField(verbose_name='需预付款', choices=bool_choice, default=1, blank=True, null=True, help_text='')
    enable_pool = models.IntegerField(verbose_name='启用报名池', choices=bool_choice, default=1, blank=True, null=True, help_text='')
    pool_limit = models.IntegerField(verbose_name='报名池容纳人数', blank=True, null=True, help_text='')
    pool_stopwatch = models.IntegerField(verbose_name='报名池倒计时', blank=True, null=True, help_text='单位（秒）')
    open_time = models.DateTimeField(verbose_name='报名开放时间', blank=True, null=True, help_text='')
    close_time = models.DateTimeField(verbose_name='报名关闭时间', blank=True, null=True, help_text='')
    launch_time = models.DateTimeField(verbose_name='活动开始时间', blank=True, null=True, help_text='')
    finish_time = models.DateTimeField(verbose_name='活动完成时间', blank=True, null=True, help_text='')
    spend_time = models.CharField(verbose_name='活动花费时间', max_length=255, blank=True, null=True, help_text='')
    create_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now, help_text='')
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True, help_text='')
    snapshot = models.JSONField(verbose_name='快照', blank=True, null=True, help_text='')
    remark = models.CharField(verbose_name='备注', max_length=255, blank=True, null=True, help_text='')

    def __str__(self):
        return f"{self.id}"


class EnrollExtendField(models.Model):
    """ EnrollExtendField 报名扩展字段表 """

    class Meta:
        db_table = 'enroll_extend_field'
        verbose_name_plural = '报名分项表'

    id = models.AutoField(verbose_name='ID', primary_key=True, null=False, help_text='清单单价')
    field_index = models.IntegerField(verbose_name='原有字段', max_length=32, blank=True, null=True, help_text='')
    alias_name = models.CharField(verbose_name='映射名称', max_length=32, blank=True, null=True, help_text='')
    description = models.CharField(verbose_name='分项小计', max_length=255, blank=True, null=True, help_text='')


class EnrollSubitem(models.Model):
    """ Enroll_EnrollSubitem 报名分项表 [1:N] """

    class Meta:
        db_table = 'enroll_subitem'
        verbose_name_plural = '报名分项表'

    id = models.BigAutoField(verbose_name='ID', primary_key=True, null=False, auto_created=True, help_text='报名分项ID')
    enroll_id = models.IntegerField(verbose_name='报名ID', blank=True, null=True, help_text='报名ID')
    name = models.CharField(verbose_name='分项名称', max_length=128, blank=True, null=True, help_text='')
    price = models.DecimalField(verbose_name='分项单价', max_digits=32, decimal_places=8, db_index=True, blank=True, null=True, help_text='清单单价')
    count = models.IntegerField(verbose_name='分项数量', blank=True, null=True, help_text='')
    unit = models.CharField(verbose_name='单位', max_length=32, blank=True, null=True, help_text='')
    amount = models.DecimalField(verbose_name='分项小计', max_digits=32, decimal_places=8, db_index=True, blank=True, null=True, help_text='')
    description = models.CharField(verbose_name='描述', max_length=255, blank=True, null=True, help_text='')
    remark = models.CharField(verbose_name='备注', max_length=255, blank=True, null=True, help_text='')
    field_1 = models.CharField(verbose_name='字段1', max_length=255, blank=True, null=True, help_text='')
    field_2 = models.CharField(verbose_name='字段2', max_length=255, blank=True, null=True, help_text='')
    field_3 = models.CharField(verbose_name='字段3', max_length=255, blank=True, null=True, help_text='')
    field_4 = models.CharField(verbose_name='字段4', max_length=255, blank=True, null=True, help_text='')
    field_5 = models.CharField(verbose_name='字段5', max_length=255, blank=True, null=True, help_text='')
    field_6 = models.CharField(verbose_name='字段6', max_length=255, blank=True, null=True, help_text='')
    field_7 = models.CharField(verbose_name='字段7', max_length=255, blank=True, null=True, help_text='')
    field_8 = models.CharField(verbose_name='字段8', max_length=255, blank=True, null=True, help_text='')
    field_9 = models.CharField(verbose_name='字段9', max_length=255, blank=True, null=True, help_text='')
    field_10 = models.CharField(verbose_name='字段10', max_length=255, blank=True, null=True, help_text='')

    def __str__(self):
        return f"{self.id}"


class EnrollAuthStatus(models.Model):
    class Meta:
        db_table = 'enroll_auth_status'
        verbose_name_plural = '审核状态表'

    id = models.AutoField(verbose_name='ID', primary_key=True)
    value = models.CharField(verbose_name='值', max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.value}"


class EnrollPayStatus(models.Model):
    class Meta:
        db_table = 'enroll_pay_status'
        verbose_name_plural = '支付状态表'

    id = models.AutoField(verbose_name='ID', primary_key=True)
    value = models.CharField(verbose_name='值', max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.value}"


class EnrollRecord(models.Model):
    """ Enroll_EnrollRecord 报名记录表 [1:N] """

    class Meta:
        db_table = 'enroll_record'
        verbose_name_plural = '报名记录表'

    id = models.BigAutoField(verbose_name='报名记录ID', primary_key=True, null=False, auto_created=True, help_text='报名记录ID')
    enroll = models.ForeignKey(verbose_name='报名ID', to=Enroll, db_column='enroll_id', related_name='+', on_delete=models.DO_NOTHING)
    user_id = models.BigIntegerField(verbose_name='用户ID', db_index=True)
    enroll_auth_status_id = models.ForeignKey(verbose_name='报名权限状态ID', to=EnrollAuthStatus, db_column='enroll_auth_status_id', related_name='+', on_delete=models.DO_NOTHING, blank=True, null=True,
                                              help_text='')
    enroll_pay_status_id = models.ForeignKey(verbose_name='报名支付状态ID', to=EnrollPayStatus, db_column='enroll_pay_status_id', related_name='+', on_delete=models.DO_NOTHING, blank=True, null=True,
                                             help_text='')
    enroll_status_code = models.IntegerField(verbose_name='报名状态码', blank=True, null=True, help_text='')
    create_time = models.DateTimeField(verbose_name='报名时间', default=timezone.now, blank=True, null=True, help_text='')
    price = models.DecimalField(verbose_name='应付单价', max_digits=32, decimal_places=8, db_index=True, blank=True, null=True, default=0, help_text='')
    deposit = models.DecimalField(verbose_name='应付押金', max_digits=32, decimal_places=8, db_index=True, blank=True, null=True, default=0, help_text='')
    count = models.DecimalField(verbose_name='购买数量', max_digits=32, decimal_places=8, db_index=True, blank=True, null=True, default=0, help_text='')
    main_amount = models.DecimalField(verbose_name='主项合计', max_digits=32, decimal_places=8, db_index=True, blank=True, null=True, default=0, help_text='')
    coupon_amount = models.DecimalField(verbose_name='优惠券合计', max_digits=32, decimal_places=8, db_index=True, blank=True, null=True, default=0, help_text='')
    again_reduction = models.DecimalField(verbose_name='商家再减免', max_digits=32, decimal_places=8, db_index=True, blank=True, null=True, default=0, help_text='商家再减免(发起人填)')
    subitems_amount = models.DecimalField(verbose_name='分项合计', max_digits=32, decimal_places=8, db_index=True, blank=True, null=True, default=0, help_text='')
    deposit_amount = models.DecimalField(verbose_name='押金合计', max_digits=32, decimal_places=8, db_index=True, blank=True, null=True, default=0, help_text='')
    amount = models.DecimalField(verbose_name='总计应收/付金额', max_digits=32, decimal_places=8, db_index=True, blank=True, null=True, default=0, help_text='')
    paid_amount = models.DecimalField(verbose_name='已收/付金额', max_digits=32, decimal_places=8, db_index=True, blank=True, null=True, default=0, help_text='')
    unpaid_amount = models.DecimalField(verbose_name='未收/付金额', max_digits=32, decimal_places=8, db_index=True, blank=True, null=True, default=0, help_text='')
    fee = models.DecimalField(verbose_name='小费', max_digits=32, decimal_places=8, db_index=True, blank=True, null=True, default=0, help_text='')
    photos = models.JSONField(verbose_name='图册地址', blank=True, null=True, default=list, help_text='')
    files = models.JSONField(verbose_name='文件地址', blank=True, null=True, default=list, help_text='')
    score = models.FloatField(verbose_name='评分', blank=True, null=True, help_text='')
    reply = models.CharField(verbose_name='发起人答复', max_length=1024, blank=True, null=True, help_text='发起人答复(发起人填)')
    remark = models.CharField(verbose_name='备注', max_length=1024, blank=True, null=True, help_text='')

    def __str__(self):
        return f"{self.id}"


class EnrollSubitemRecord(models.Model):
    """ Enroll_EnrollRecordSubitem 报名记录分项表 [1:N] """

    class Meta:
        db_table = 'enroll_subitem_record'
        verbose_name_plural = '报名记录分项表'

    id = models.BigAutoField(verbose_name='报名记录分项ID', primary_key=True, null=False, auto_created=True, help_text='')
    enroll_record_id = models.ForeignKey(
        verbose_name='报名记录ID', to=EnrollRecord, db_column='enroll_record_id', related_name='+', unique=False, blank=True, null=True, on_delete=models.DO_NOTHING, help_text=''
    )
    enroll_subitem_id = models.ForeignKey(
        verbose_name='报名分项ID', to=EnrollSubitem, db_column='enroll_subitem_id', related_name='+',
        unique=False, blank=True, null=True, on_delete=models.DO_NOTHING,
        help_text='说明：如果分项选择失败，行业规定是整单取消重新购买，不支持选择某项来取消。但为了灵活，允许后台工作端修改每项单价和数量（分项小计不可以修改），也能达到取消的效果。'
    )
    user_id = models.BigIntegerField(verbose_name='用户ID', blank=True, null=True, help_text='')
    price = models.DecimalField(verbose_name='分项单价', max_digits=32, decimal_places=8, db_index=True, blank=True, null=True, default=0, help_text='')
    count = models.DecimalField(verbose_name='分项数量', max_digits=32, decimal_places=8, db_index=True, blank=True, null=True, default=0, help_text='')
    subitem_amount = models.DecimalField(verbose_name='分项小计', max_digits=32, decimal_places=8, db_index=True, blank=True, null=True, default=0, help_text='')

    def __str__(self):
        return f"{self.id}"
