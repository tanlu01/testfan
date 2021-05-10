from peewee import *

database = MySQLDatabase('mt_coupon', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': 'rm-uf6pec9k82nsk59o8.mysql.rds.aliyuncs.com', 'port': 3306, 'user': 'root', 'password': 'cFsc34^8pVm'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class AuditBuyCoupon(BaseModel):
    buyer_id = BigIntegerField(index=True)
    coin_num = IntegerField(constraints=[SQL("DEFAULT 0")])
    coupon_id = BigIntegerField(index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    user_coupon_id = BigIntegerField()

    class Meta:
        table_name = 'audit_buy_coupon'

class Coupon(BaseModel):
    alarm_receivers = TextField(null=True)
    alarm_threshold = IntegerField(constraints=[SQL("DEFAULT 0")])
    amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    biz_title = CharField(constraints=[SQL("DEFAULT ''")])
    can_change_amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    can_refund = IntegerField(constraints=[SQL("DEFAULT 1")])
    cannot_self_take = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    count = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    daily_limit = IntegerField(constraints=[SQL("DEFAULT 0")])
    freq_limit_mintues = IntegerField(constraints=[SQL("DEFAULT 0")])
    get_end_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    get_start_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_gift = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_show = IntegerField(constraints=[SQL("DEFAULT 0")])
    issued = IntegerField(constraints=[SQL("DEFAULT 0")])
    mall_amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    mall_name = CharField(constraints=[SQL("DEFAULT ''")])
    min_price = IntegerField(constraints=[SQL("DEFAULT 0")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    need_alarm = IntegerField(constraints=[SQL("DEFAULT 0")])
    no_change = IntegerField(constraints=[SQL("DEFAULT 0")])
    operator_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    operator_role = TextField(null=True)
    origin_stock = IntegerField(constraints=[SQL("DEFAULT 0")])
    per_user = IntegerField(constraints=[SQL("DEFAULT 1")])
    per_user_daily_limit = IntegerField(constraints=[SQL("DEFAULT 0")])
    purchase_coin = IntegerField(constraints=[SQL("DEFAULT 0")])
    risk_strategy = IntegerField(constraints=[SQL("DEFAULT 0")])
    rule_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    scene_text = CharField(constraints=[SQL("DEFAULT ''")])
    scene_type = IntegerField(null=True)
    source_goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    sub_name = CharField(constraints=[SQL("DEFAULT ''")])
    target_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    target_value = CharField(constraints=[SQL("DEFAULT ''")])
    type = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    use_end_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    use_relative = IntegerField(constraints=[SQL("DEFAULT 0")])
    use_relative_end_day = IntegerField(constraints=[SQL("DEFAULT 0")])
    use_relative_start_day = IntegerField(constraints=[SQL("DEFAULT 0")])
    use_start_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'coupon'
        indexes = (
            (('source_goods_id', 'status', 'is_deleted'), False),
        )

class CouponAuditLog(BaseModel):
    action = IntegerField(constraints=[SQL("DEFAULT 0")])
    coupon_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    operator_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    remark = TextField(null=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'coupon_audit_log'

class CouponAutoGiveLog(BaseModel):
    buyer_id = BigIntegerField(index=True)
    coupon_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    order_id = BigIntegerField(index=True, null=True)

    class Meta:
        table_name = 'coupon_auto_give_log'

class CouponCustomer(BaseModel):
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    coupon_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    id = BigAutoField()
    mall_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    operator_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    order_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    seller_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    type = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'coupon_customer'

class CouponGetGroup(BaseModel):
    config = TextField(null=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    operator_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    title = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'coupon_get_group'

class CouponGetGroupDetail(BaseModel):
    coupon_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    group_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'coupon_get_group_detail'
        indexes = (
            (('group_id', 'coupon_id'), True),
        )

class CouponGive(BaseModel):
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    coupon_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    operator_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'coupon_give'
        indexes = (
            (('buyer_id', 'coupon_id'), False),
        )

class CouponGoods(BaseModel):
    coupon_count = IntegerField(constraints=[SQL("DEFAULT 1")])
    coupon_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    ext_goods_id = CharField(constraints=[SQL("DEFAULT ''")])
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'coupon_goods'
        indexes = (
            (('goods_id', 'ext_goods_id', 'coupon_id', 'is_deleted'), True),
        )

class CouponLink(BaseModel):
    config = TextField(null=True)
    coupon_amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    coupon_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(null=True)
    end_date = DateField(null=True)
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_enabled = IntegerField(constraints=[SQL("DEFAULT 1")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    operator_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    start_date = DateField(null=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    url_type = IntegerField()
    url_value = CharField(null=True)

    class Meta:
        table_name = 'coupon_link'

class CouponPass(BaseModel):
    amount = IntegerField()
    buyer_id = BigIntegerField(index=True)
    coupon_id = BigIntegerField(null=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    expire_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    id = BigAutoField()
    message_id = CharField(constraints=[SQL("DEFAULT ''")], unique=True)
    promise_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    status = IntegerField()
    title = CharField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    user_coupon_id = BigIntegerField(null=True)

    class Meta:
        table_name = 'coupon_pass'

class CouponReceiveFilter(BaseModel):
    coupon_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], unique=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    filter_content = TextField(null=True)
    filter_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    filter_value = TextField(null=True)
    id = BigAutoField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'coupon_receive_filter'

class CouponRef(BaseModel):
    coupon_id = BigIntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    is_enabled = IntegerField(constraints=[SQL("DEFAULT 1")])
    ref_checker = CharField(constraints=[SQL("DEFAULT ''")])
    ref_name = CharField(index=True)

    class Meta:
        table_name = 'coupon_ref'
        indexes = (
            (('coupon_id', 'ref_name'), True),
        )

class CouponRelated(BaseModel):
    coupon_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    group_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    logo = CharField(constraints=[SQL("DEFAULT ''")])
    related_coupon_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'coupon_related'
        indexes = (
            (('coupon_id', 'group_type'), True),
        )

class CouponRule(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    description = CharField(constraints=[SQL("DEFAULT ''")])
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    rule = TextField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'coupon_rule'

class CouponSceneType(BaseModel):
    amount_max = IntegerField(constraints=[SQL("DEFAULT 0")])
    config = TextField(null=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    id = BigAutoField()
    name = CharField(constraints=[SQL("DEFAULT ''")])
    operator = CharField(constraints=[SQL("DEFAULT ''")])
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    sort = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    type = IntegerField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'coupon_scene_type'

class LabeledGoodsCoupon(BaseModel):
    amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    coupon_id = BigIntegerField(index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    get_end_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    get_start_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    goods_id = IntegerField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'labeled_goods_coupon'
        indexes = (
            (('goods_id', 'coupon_id'), True),
        )

class UserCoupon(BaseModel):
    amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    can_refund = IntegerField(constraints=[SQL("DEFAULT 1")])
    cat_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    coupon_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_gift = IntegerField(constraints=[SQL("DEFAULT 0")])
    link = CharField(constraints=[SQL("DEFAULT ''")])
    mall_amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    mall_name = CharField(constraints=[SQL("DEFAULT ''")])
    min_price = IntegerField(constraints=[SQL("DEFAULT 0")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    order_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    per_user = IntegerField(constraints=[SQL("DEFAULT 1")])
    rule_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    source_order_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    source_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    sub_name = CharField(constraints=[SQL("DEFAULT ''")])
    target_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    target_value = CharField(constraints=[SQL("DEFAULT ''")])
    transfer_from = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    type = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    use_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    use_end_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    use_start_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    used = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'user_coupon'
        indexes = (
            (('buyer_id', 'source_order_id'), False),
            (('buyer_id', 'used'), False),
            (('buyer_id', 'used', 'source_type'), False),
        )
