from peewee import *
import os

database = MySQLDatabase('pay', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': os.getenv('INCOME_MYSQL_HOST'), 'user': os.getenv('INCOME_MYSQL_USER'), 'password': os.getenv('INCOME_MYSQL_PWD')})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class AccountItemBase(BaseModel):
    account_status = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    amount = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    app_id = CharField(constraints=[SQL("DEFAULT ''")])
    batch_no = CharField(constraints=[SQL("DEFAULT ''")])
    created_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], index=True)
    id = BigAutoField()
    out_trade_no = CharField(constraints=[SQL("DEFAULT ''")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    trade_no = CharField(constraints=[SQL("DEFAULT ''")])
    updated_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])

    class Meta:
        table_name = 'account_item_base'
        indexes = (
            (('batch_no', 'app_id'), False),
            (('out_trade_no', 'batch_no'), False),
            (('trade_no', 'batch_no'), False),
        )

class AccountItemCompare(BaseModel):
    account_status = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    amount = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    app_id = CharField(constraints=[SQL("DEFAULT ''")])
    batch_no = CharField(constraints=[SQL("DEFAULT ''")])
    created_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], index=True)
    id = BigAutoField()
    out_trade_no = CharField(constraints=[SQL("DEFAULT ''")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    trade_no = CharField(constraints=[SQL("DEFAULT ''")])
    updated_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])

    class Meta:
        table_name = 'account_item_compare'
        indexes = (
            (('batch_no', 'app_id'), False),
            (('out_trade_no', 'batch_no'), False),
            (('trade_no', 'batch_no'), False),
        )

class AccountItemResult(BaseModel):
    amount_base = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    amount_compare = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    app_base = CharField(constraints=[SQL("DEFAULT ''")])
    app_compare = CharField(constraints=[SQL("DEFAULT ''")])
    batch_no = CharField(constraints=[SQL("DEFAULT ''")])
    created_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    except_code = CharField(constraints=[SQL("DEFAULT ''")])
    id = BigAutoField()
    status_base = IntegerField(constraints=[SQL("DEFAULT 0")])
    status_compare = IntegerField(constraints=[SQL("DEFAULT 0")])
    trade_no_base = CharField(constraints=[SQL("DEFAULT ''")])
    trade_no_compare = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    updated_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])

    class Meta:
        table_name = 'account_item_result'
        indexes = (
            (('batch_no', 'app_base', 'app_compare'), False),
            (('trade_no_base', 'app_base'), False),
        )

class AccountSlicer(BaseModel):
    app_base = CharField(constraints=[SQL("DEFAULT ''")])
    app_compare = CharField(constraints=[SQL("DEFAULT ''")])
    batch_no = CharField(constraints=[SQL("DEFAULT ''")])
    created_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], index=True)
    id = BigAutoField()
    item_id_end = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    item_id_start = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    updated_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])

    class Meta:
        table_name = 'account_slicer'
        indexes = (
            (('batch_no', 'app_base'), False),
        )

class Accounts(BaseModel):
    app_id = CharField(constraints=[SQL("DEFAULT ''")])
    balance = IntegerField(constraints=[SQL("DEFAULT 0")])
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP(6)")])
    cut_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP(6)")], index=True)
    cut_version = IntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    sub_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    type = IntegerField(constraints=[SQL("DEFAULT 0")])
    uid = CharField(constraints=[SQL("DEFAULT ''")])
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP(6)")])

    class Meta:
        table_name = 'accounts'
        indexes = (
            (('app_id', 'uid', 'type', 'sub_type'), True),
        )

class Apps(BaseModel):
    alipay = IntegerField(constraints=[SQL("DEFAULT 0")])
    app_id = CharField(constraints=[SQL("DEFAULT ''")], unique=True)
    coin = IntegerField(constraints=[SQL("DEFAULT 0")])
    coin_dedu = IntegerField(constraints=[SQL("DEFAULT 0")])
    coin_merchant_id = CharField(constraints=[SQL("DEFAULT ''")])
    created_at = IntegerField()
    pay_merchant_id = CharField(constraints=[SQL("DEFAULT ''")])
    settlement_index = IntegerField(constraints=[SQL("DEFAULT 0")])
    updated_at = IntegerField()
    wechat = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'apps'

class AppsBak(BaseModel):
    alipay = IntegerField(constraints=[SQL("DEFAULT 0")])
    app_id = CharField(constraints=[SQL("DEFAULT ''")], unique=True)
    coin = IntegerField(constraints=[SQL("DEFAULT 0")])
    coin_dedu = IntegerField(constraints=[SQL("DEFAULT 0")])
    coin_merchant_id = CharField(constraints=[SQL("DEFAULT ''")])
    created_at = IntegerField(constraints=[SQL("DEFAULT 0")])
    pay_merchant_id = CharField(constraints=[SQL("DEFAULT ''")])
    settlement_index = IntegerField(constraints=[SQL("DEFAULT 0")])
    updated_at = IntegerField(constraints=[SQL("DEFAULT 0")])
    wechat = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'apps_bak'

class AppsTest(BaseModel):
    alipay = IntegerField(constraints=[SQL("DEFAULT 0")])
    app_id = CharField(constraints=[SQL("DEFAULT ''")], unique=True)
    coin = IntegerField(constraints=[SQL("DEFAULT 0")])
    coin_dedu = IntegerField(constraints=[SQL("DEFAULT 0")])
    coin_merchant_id = CharField(constraints=[SQL("DEFAULT ''")])
    created_at = IntegerField()
    pay_merchant_id = CharField(constraints=[SQL("DEFAULT ''")])
    settlement_index = IntegerField(constraints=[SQL("DEFAULT 0")])
    updated_at = IntegerField()
    wechat = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'apps_test'

class AttributeValues(BaseModel):
    app_id = CharField(constraints=[SQL("DEFAULT ''")])
    attribute_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    created_at = IntegerField(constraints=[SQL("DEFAULT 0")])
    desc = CharField(constraints=[SQL("DEFAULT ''")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    updated_at = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'attribute_values'
        indexes = (
            (('app_id', 'attribute_id'), False),
        )

class AttributeValuesCopy(BaseModel):
    app_id = CharField(constraints=[SQL("DEFAULT ''")])
    attribute_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    created_at = IntegerField(constraints=[SQL("DEFAULT 0")])
    desc = CharField(constraints=[SQL("DEFAULT ''")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    updated_at = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'attribute_values_copy'
        indexes = (
            (('app_id', 'attribute_id'), False),
        )

class Attributes(BaseModel):
    app_id = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    created_at = IntegerField(constraints=[SQL("DEFAULT 0")])
    desc = CharField(constraints=[SQL("DEFAULT ''")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    updated_at = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'attributes'

class AttributesCopy(BaseModel):
    app_id = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    created_at = IntegerField(constraints=[SQL("DEFAULT 0")])
    desc = CharField(constraints=[SQL("DEFAULT ''")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    updated_at = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'attributes_copy'

class Bar(BaseModel):

    class Meta:
        table_name = 'bar'

class BillException(BaseModel):
    channel_amount = IntegerField(null=True)
    channel_id = IntegerField(null=True)
    comment = CharField(null=True)
    created = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    date = CharField(null=True)
    error_type = IntegerField(null=True)
    order_amount = IntegerField(null=True)
    order_no = CharField(index=True, null=True)
    out_order_no = CharField(null=True)
    scene_id = IntegerField(null=True)
    updated = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'bill_exception'

class BillExceptionCopy(BaseModel):
    channel_amount = IntegerField(null=True)
    channel_id = IntegerField(null=True)
    comment = CharField(null=True)
    created = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    date = CharField(null=True)
    error_type = IntegerField(null=True)
    order_amount = IntegerField(null=True)
    order_no = CharField(null=True)
    out_order_no = CharField(null=True)
    scene_id = IntegerField(null=True)
    updated = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'bill_exception_copy'

class Channels(BaseModel):
    amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    app_id = CharField(constraints=[SQL("DEFAULT ''")])
    c_type = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    cap_no = CharField(constraints=[SQL("DEFAULT ''")], index=True, null=True)
    channel_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    created_at = IntegerField(constraints=[SQL("DEFAULT 0")])
    currency = CharField(constraints=[SQL("DEFAULT ''")])
    err_msg = CharField(constraints=[SQL("DEFAULT ''")])
    op_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    order_no = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    refund_no = CharField(constraints=[SQL("DEFAULT ''")])
    scene_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    sort = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    tp_trade_no = CharField(constraints=[SQL("DEFAULT ''")], index=True, null=True)
    type = IntegerField(constraints=[SQL("DEFAULT 0")])
    updated_at = IntegerField(constraints=[SQL("DEFAULT 0")])
    voucher = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'channels'
        indexes = (
            (('cap_no', 'op_type', 'channel_id'), False),
        )

class ChannelsBak(BaseModel):
    amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    app_id = CharField(constraints=[SQL("DEFAULT ''")])
    c_type = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    channel_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    created_at = IntegerField(constraints=[SQL("DEFAULT 0")])
    currency = CharField(constraints=[SQL("DEFAULT ''")])
    err_msg = CharField(constraints=[SQL("DEFAULT ''")])
    op_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    order_no = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    refund_no = CharField(constraints=[SQL("DEFAULT ''")])
    scene_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    sort = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    tp_trade_no = CharField(constraints=[SQL("DEFAULT ''")], index=True, null=True)
    type = IntegerField(constraints=[SQL("DEFAULT 0")])
    updated_at = IntegerField(constraints=[SQL("DEFAULT 0")])
    voucher = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'channels_bak'

class Contract(BaseModel):
    app_id = CharField(constraints=[SQL("DEFAULT ''")])
    app_os = CharField(constraints=[SQL("DEFAULT ''")])
    channel_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    channel_scene_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    contract_code = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    contract_display_account = CharField(constraints=[SQL("DEFAULT ''")])
    contract_expired_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    contract_termination_mode = IntegerField(constraints=[SQL("DEFAULT -1")])
    contract_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP(6)")])
    execute_time = CharField(constraints=[SQL("DEFAULT ''")])
    extra = CharField(constraints=[SQL("DEFAULT ''")])
    id = BigAutoField()
    is_pending = IntegerField(constraints=[SQL("DEFAULT 0")])
    notice_url = CharField(constraints=[SQL("DEFAULT ''")])
    open_id = CharField(constraints=[SQL("DEFAULT ''")])
    out_contract_code = CharField(constraints=[SQL("DEFAULT ''")])
    period = IntegerField(constraints=[SQL("DEFAULT 0")])
    period_type = CharField(constraints=[SQL("DEFAULT ''")])
    receipt = IntegerField(constraints=[SQL("DEFAULT 0")])
    request_serial = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    return_app = CharField(constraints=[SQL("DEFAULT ''")])
    return_web = CharField(constraints=[SQL("DEFAULT ''")])
    sign_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    single_amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    tp_contract_code = CharField(constraints=[SQL("DEFAULT ''")])
    tp_open_id = CharField(constraints=[SQL("DEFAULT ''")])
    tp_plan_id = CharField(constraints=[SQL("DEFAULT ''")])
    unsign_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP(6)")])
    valid_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])

    class Meta:
        table_name = 'contract'
        indexes = (
            (('out_contract_code', 'app_id'), True),
        )

class ContractWithholdTask(BaseModel):
    channel_id = IntegerField()
    channel_scene_id = IntegerField()
    contract_code = CharField(constraints=[SQL("DEFAULT ''")])
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    execute_time = DateTimeField(null=True)
    next_withhold_time = CharField(constraints=[SQL("DEFAULT ''")])
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    task_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    withhold_order = CharField(constraints=[SQL("DEFAULT ''")], unique=True)

    class Meta:
        table_name = 'contract_withhold_task'

class Foo(BaseModel):

    class Meta:
        table_name = 'foo'

class FooOrderDeduct(BaseModel):
    code = CharField(null=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    deduct_price = BigIntegerField(null=True)
    deduct_type = IntegerField(null=True)
    id = BigAutoField()
    is_delete = IntegerField(null=True)
    order_no = CharField(index=True, null=True)
    product_id = CharField(null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'foo_order_deduct'

class FooOrders(BaseModel):
    app_id = CharField(null=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    deal_fee = BigIntegerField(null=True)
    id = BigAutoField()
    old_status = IntegerField(null=True)
    order_no = CharField(null=True)
    order_type = IntegerField(null=True)
    out_order_no = CharField(null=True)
    status = IntegerField(null=True)
    total_fee = BigIntegerField(null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    user_id = BigIntegerField(null=True)
    user_type = IntegerField(null=True)

    class Meta:
        table_name = 'foo_orders'

class GoodsOrder(BaseModel):
    app = CharField(constraints=[SQL("DEFAULT 'midu'")])
    create_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    end_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], index=True)
    goods_id = IntegerField()
    goods_money = IntegerField(constraints=[SQL("DEFAULT 0")])
    goods_num = IntegerField(constraints=[SQL("DEFAULT 1")])
    info = TextField(null=True)
    is_contract = IntegerField(constraints=[SQL("DEFAULT 0")])
    need_pay_money = IntegerField(constraints=[SQL("DEFAULT 0")])
    order_company_no = CharField(constraints=[SQL("DEFAULT ''")])
    order_id = CharField(constraints=[SQL("DEFAULT ''")], unique=True)
    order_type = IntegerField(constraints=[SQL("DEFAULT 1")])
    origin_third_order_id = CharField(constraints=[SQL("DEFAULT ''")])
    pay_method = IntegerField()
    pay_money = IntegerField(constraints=[SQL("DEFAULT 0")])
    pay_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    platform = IntegerField(constraints=[SQL("DEFAULT 1")])
    start_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    third_order_id = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    uid = BigIntegerField(index=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], index=True)

    class Meta:
        table_name = 'goods_order'
        indexes = (
            (('create_time', 'platform'), False),
            (('status', 'order_id', 'update_time'), False),
            (('status', 'start_time', 'end_time'), False),
        )

class Iap(BaseModel):
    bundle_id = CharField(constraints=[SQL("DEFAULT ''")])
    cnt = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    is_in_intro_offer_period = CharField(constraints=[SQL("DEFAULT ''")])
    is_trial_period = CharField(constraints=[SQL("DEFAULT ''")])
    order_no = CharField(constraints=[SQL("DEFAULT ''")], unique=True)
    original_transaction_id = CharField(constraints=[SQL("DEFAULT ''")])
    product_id = CharField(constraints=[SQL("DEFAULT ''")])
    receipt = TextField()
    transaction_id = CharField(constraints=[SQL("DEFAULT ''")], unique=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    user_id = CharField()

    class Meta:
        table_name = 'iap'

class IapProducts(BaseModel):
    app_id = CharField(constraints=[SQL("DEFAULT ''")])
    apple_product_id = CharField(constraints=[SQL("DEFAULT ''")], unique=True)
    apple_product_type = IntegerField(constraints=[SQL("DEFAULT 1")])
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    intro_price = IntegerField(constraints=[SQL("DEFAULT 0")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    operator = CharField(constraints=[SQL("DEFAULT ''")])
    price = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'iap_products'

class IapProductsCopy(BaseModel):
    app_id = CharField(constraints=[SQL("DEFAULT ''")])
    apple_product_id = CharField(constraints=[SQL("DEFAULT ''")], unique=True)
    apple_product_type = IntegerField(constraints=[SQL("DEFAULT 1")])
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    intro_price = IntegerField(constraints=[SQL("DEFAULT 0")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    operator = CharField(constraints=[SQL("DEFAULT ''")])
    price = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'iap_products_copy'

class IapRetry(BaseModel):
    client_retry_cnt = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    order_no = CharField(constraints=[SQL("DEFAULT ''")], unique=True)
    receipt = TextField()
    remark = CharField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    test = IntegerField(constraints=[SQL("DEFAULT 2")])
    transaction_id = CharField(constraints=[SQL("DEFAULT ''")])
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'iap_retry'

class Logs(BaseModel):
    channel = IntegerField(constraints=[SQL("DEFAULT 0")])
    created_at = IntegerField(constraints=[SQL("DEFAULT 0")])
    data = CharField(constraints=[SQL("DEFAULT ''")])
    event = IntegerField(constraints=[SQL("DEFAULT 0")])
    order_no = CharField(constraints=[SQL("DEFAULT ''")], index=True)

    class Meta:
        table_name = 'logs'

class Luffy(BaseModel):
    a = IntegerField(constraints=[SQL("DEFAULT 0")])
    b = IntegerField(constraints=[SQL("DEFAULT 0")])
    c = IntegerField(constraints=[SQL("DEFAULT 0")])
    d = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    id = BigAutoField()

    class Meta:
        table_name = 'luffy'
        indexes = (
            (('b', 'c', 'a'), True),
        )

class MappingContractOrder(BaseModel):
    contract_code = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    id = BigAutoField()
    order_no = CharField(unique=True)

    class Meta:
        table_name = 'mapping_contract_order'

class NtbOrderDeduct(BaseModel):
    code = CharField(null=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    deduct_price = BigIntegerField(null=True)
    deduct_type = IntegerField(null=True)
    id = BigAutoField()
    is_delete = IntegerField(null=True)
    order_no = CharField(index=True, null=True)
    product_id = CharField(null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'ntb_order_deduct'

class NtbOrderExtraData(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    extra_data = TextField(null=True)
    id = BigAutoField()
    order_no = CharField(index=True, null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    user_extra = CharField(null=True)

    class Meta:
        table_name = 'ntb_order_extra_data'

class NtbOrderItem(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    id = BigAutoField()
    order_no = CharField(index=True, null=True)
    product_id = CharField(null=True)
    product_num = BigIntegerField(null=True)
    unit_price = BigIntegerField(null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'ntb_order_item'

class NtbOrderLog(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    desc = CharField(null=True)
    id = BigAutoField()
    new_status = IntegerField(null=True)
    new_status_desc = CharField(null=True)
    old_status = IntegerField(null=True)
    old_status_desc = CharField(null=True)
    order_no = CharField(index=True, null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'ntb_order_log'

class NtbOrderTimer(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    expire_at = DateTimeField(null=True)
    id = BigAutoField()
    notice = CharField(null=True)
    order_no = CharField(index=True, null=True)
    reason = CharField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'ntb_order_timer'

class NtbOrders(BaseModel):
    app_id = CharField(null=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    deal_fee = BigIntegerField(null=True)
    id = BigAutoField()
    old_status = IntegerField(null=True)
    order_no = CharField(index=True, null=True)
    order_type = IntegerField(null=True)
    out_order_no = CharField(null=True)
    pay_type = IntegerField(constraints=[SQL("DEFAULT -1")], null=True)
    place = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    status = IntegerField(null=True)
    third_part_id = IntegerField(null=True)
    total_fee = BigIntegerField(null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    user_id = BigIntegerField(index=True, null=True)
    user_type = IntegerField(null=True)

    class Meta:
        table_name = 'ntb_orders'

class NtbOrdersCheck(BaseModel):
    app_id = CharField(null=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    deal_fee = BigIntegerField(null=True)
    id = BigAutoField()
    old_status = IntegerField(null=True)
    order_no = CharField(index=True, null=True)
    order_type = IntegerField(null=True)
    out_order_no = CharField(null=True)
    pay_type = IntegerField(constraints=[SQL("DEFAULT -1")], null=True)
    place = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    status = IntegerField(null=True)
    third_part_id = IntegerField(null=True)
    total_fee = BigIntegerField(null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    user_id = BigIntegerField(index=True, null=True)
    user_type = IntegerField(null=True)

    class Meta:
        table_name = 'ntb_orders_check'

class OrderBill20191111(BaseModel):
    amount = IntegerField(null=True)
    channel_id = IntegerField(null=True)
    created = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    currency = CharField(null=True)
    date = CharField(null=True)
    order_no = CharField(index=True, null=True)
    refund_no = CharField(null=True)
    scene_id = IntegerField(null=True)

    class Meta:
        table_name = 'order_bill_20191111'

class OrderBill20191112(BaseModel):
    amount = IntegerField(null=True)
    channel_id = IntegerField(null=True)
    created = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    currency = CharField(null=True)
    date = CharField(null=True)
    order_no = CharField(null=True, unique=True)
    refund_no = CharField(null=True)
    scene_id = IntegerField(null=True)

    class Meta:
        table_name = 'order_bill_20191112'

class OrderBill20191113(BaseModel):
    amount = IntegerField(null=True)
    channel_id = IntegerField(null=True)
    created = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    currency = CharField(null=True)
    date = CharField(null=True)
    order_no = CharField(index=True, null=True)
    refund_no = CharField(null=True)
    scene_id = IntegerField(null=True)

    class Meta:
        table_name = 'order_bill_20191113'

class OrderBill20191115(BaseModel):
    amount = IntegerField(null=True)
    channel_id = IntegerField(null=True)
    created = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    currency = CharField(null=True)
    date = CharField(null=True)
    order_no = CharField(index=True, null=True)
    refund_no = CharField(null=True)
    scene_id = IntegerField(null=True)

    class Meta:
        table_name = 'order_bill_20191115'

class OrderBill20200210(BaseModel):
    amount = IntegerField(null=True)
    channel_id = IntegerField(null=True)
    created = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    currency = CharField(null=True)
    date = CharField(null=True)
    order_no = CharField(null=True, unique=True)
    refund_no = CharField(null=True)
    scene_id = IntegerField(null=True)

    class Meta:
        table_name = 'order_bill_20200210'

class OrderBill20200502(BaseModel):
    amount = IntegerField(null=True)
    channel_id = IntegerField(null=True)
    created = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    currency = CharField(null=True)
    date = CharField(null=True)
    order_no = CharField(null=True, unique=True)
    refund_no = CharField(null=True)
    scene_id = IntegerField(null=True)

    class Meta:
        table_name = 'order_bill_20200502'

class Orders(BaseModel):
    amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    app_id = CharField(constraints=[SQL("DEFAULT ''")])
    auditing = IntegerField(constraints=[SQL("DEFAULT 0")])
    body = CharField(constraints=[SQL("DEFAULT ''")])
    channel_scene_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    client_ip = CharField(constraints=[SQL("DEFAULT ''")])
    code = IntegerField(constraints=[SQL("DEFAULT 0")])
    coin_account_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    created_at = IntegerField(constraints=[SQL("DEFAULT 0")])
    display_coin = IntegerField(constraints=[SQL("DEFAULT 1")])
    extra = CharField(constraints=[SQL("DEFAULT ''")])
    goods_scene_id = CharField(constraints=[SQL("DEFAULT ''")])
    notice_url = CharField(constraints=[SQL("DEFAULT ''")])
    open_id = CharField(constraints=[SQL("DEFAULT ''")])
    order_no = CharField(constraints=[SQL("DEFAULT ''")], unique=True)
    org_id = CharField(constraints=[SQL("DEFAULT ''")])
    out_trade_no = CharField(constraints=[SQL("DEFAULT ''")])
    receipt = IntegerField(constraints=[SQL("DEFAULT 0")])
    return_url = CharField(constraints=[SQL("DEFAULT ''")])
    scene_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    title = CharField(constraints=[SQL("DEFAULT ''")])
    updated_at = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'orders'
        indexes = (
            (('app_id', 'out_trade_no'), True),
        )

class PProducts(BaseModel):
    app_id = CharField(constraints=[SQL("DEFAULT ''")])
    cfrom = CharField(constraints=[SQL("DEFAULT ''")])
    created_at = IntegerField(constraints=[SQL("DEFAULT 0")])
    platform = CharField(constraints=[SQL("DEFAULT ''")])
    product__desc = CharField(column_name='product_ desc', constraints=[SQL("DEFAULT ''")])
    product_id = CharField(constraints=[SQL("DEFAULT '0'")])
    product_name = CharField(constraints=[SQL("DEFAULT ''")])
    updated_at = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'p_products'
        indexes = (
            (('app_id', 'product_id'), True),
        )

class ProductAttributes(BaseModel):
    app_id = CharField(constraints=[SQL("DEFAULT ''")])
    attribute_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    created_at = IntegerField(constraints=[SQL("DEFAULT 0")])
    product_id = CharField(constraints=[SQL("DEFAULT '0'")])
    updated_at = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'product_attributes'
        indexes = (
            (('app_id', 'product_id', 'attribute_id'), False),
            (('app_id', 'product_id', 'attribute_id'), True),
        )

class Products(BaseModel):
    app_id = CharField(constraints=[SQL("DEFAULT ''")])
    created_at = IntegerField(constraints=[SQL("DEFAULT 0")])
    desc = CharField(constraints=[SQL("DEFAULT ''")])
    from_ = CharField(column_name='from', constraints=[SQL("DEFAULT ''")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    platform = CharField(constraints=[SQL("DEFAULT ''")])
    product_id = CharField(constraints=[SQL("DEFAULT '0'")])
    updated_at = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'products'
        indexes = (
            (('app_id', 'product_id'), False),
            (('app_id', 'product_id'), True),
        )

class ProductsCopy(BaseModel):
    app_id = CharField(constraints=[SQL("DEFAULT ''")])
    created_at = IntegerField(constraints=[SQL("DEFAULT 0")])
    desc = CharField(constraints=[SQL("DEFAULT ''")])
    from_ = CharField(column_name='from', constraints=[SQL("DEFAULT ''")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    platform = CharField(constraints=[SQL("DEFAULT ''")])
    product_id = CharField(constraints=[SQL("DEFAULT '0'")])
    updated_at = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'products_copy'
        indexes = (
            (('app_id', 'product_id'), False),
            (('app_id', 'product_id'), True),
        )

class QttCoin(BaseModel):
    amount = IntegerField(null=True)
    create_at = CharField(null=True)
    out_trade_no = CharField(null=True)
    user_id = IntegerField(null=True)

    class Meta:
        table_name = 'qtt_coin'

class QuappCoin(BaseModel):
    amount = IntegerField(null=True)
    create_at = CharField(null=True)
    out_trade_no = CharField(null=True)
    third_user_id = IntegerField(null=True)

    class Meta:
        table_name = 'quapp_coin'

class Records(BaseModel):
    amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    app_id = CharField(constraints=[SQL("DEFAULT ''")])
    business_no = CharField(constraints=[SQL("DEFAULT '0'")])
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP(6)")])
    id = BigAutoField()
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    sub_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    subject = IntegerField(constraints=[SQL("DEFAULT 0")])
    uid = CharField(constraints=[SQL("DEFAULT ''")])
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP(6)")])

    class Meta:
        table_name = 'records'
        indexes = (
            (('app_id', 'business_no'), False),
            (('app_id', 'business_no', 'uid', 'subject'), True),
            (('app_id', 'uid', 'created_at'), False),
        )

class Refunds(BaseModel):
    amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    app_id = CharField(constraints=[SQL("DEFAULT ''")])
    code = IntegerField(constraints=[SQL("DEFAULT 0")])
    created_at = IntegerField(constraints=[SQL("DEFAULT 0")])
    notice_url = CharField(constraints=[SQL("DEFAULT ''")])
    open_id = CharField(constraints=[SQL("DEFAULT ''")])
    order_no = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    org_id = CharField(constraints=[SQL("DEFAULT ''")])
    out_trade_no = CharField(constraints=[SQL("DEFAULT ''")])
    refund_no = CharField(constraints=[SQL("DEFAULT ''")])
    refund_operator = CharField(constraints=[SQL("DEFAULT ''")])
    refund_reason = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    updated_at = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'refunds'
        indexes = (
            (('order_no', 'refund_no'), True),
        )

class SkuValues(BaseModel):
    app_id = CharField(constraints=[SQL("DEFAULT ''")])
    created_at = IntegerField(constraints=[SQL("DEFAULT 0")])
    product_id = CharField(constraints=[SQL("DEFAULT '0'")])
    sku_id = CharField(constraints=[SQL("DEFAULT '0'")])
    updated_at = IntegerField(constraints=[SQL("DEFAULT 0")])
    value_id = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'sku_values'
        indexes = (
            (('app_id', 'product_id', 'sku_id', 'value_id'), False),
            (('app_id', 'product_id', 'sku_id', 'value_id'), True),
        )

class SkuValuesCopy(BaseModel):
    app_id = CharField(constraints=[SQL("DEFAULT ''")])
    created_at = IntegerField(constraints=[SQL("DEFAULT 0")])
    product_id = CharField(constraints=[SQL("DEFAULT '0'")])
    sku_id = CharField(constraints=[SQL("DEFAULT '0'")])
    updated_at = IntegerField(constraints=[SQL("DEFAULT 0")])
    value_id = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'sku_values_copy'
        indexes = (
            (('app_id', 'product_id', 'sku_id', 'value_id'), False),
            (('app_id', 'product_id', 'sku_id', 'value_id'), True),
        )

class Skus(BaseModel):
    app_id = CharField(constraints=[SQL("DEFAULT ''")])
    created_at = IntegerField(constraints=[SQL("DEFAULT 0")])
    desc = CharField(constraints=[SQL("DEFAULT ''")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    price = IntegerField(constraints=[SQL("DEFAULT 0")])
    product_id = CharField(constraints=[SQL("DEFAULT '0'")])
    sku_id = CharField(constraints=[SQL("DEFAULT '0'")])
    stock = IntegerField(constraints=[SQL("DEFAULT 0")])
    updated_at = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'skus'
        indexes = (
            (('app_id', 'product_id'), False),
            (('app_id', 'product_id', 'sku_id'), True),
        )

class SkusCopy(BaseModel):
    app_id = CharField(constraints=[SQL("DEFAULT ''")])
    created_at = IntegerField(constraints=[SQL("DEFAULT 0")])
    desc = CharField(constraints=[SQL("DEFAULT ''")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    price = IntegerField(constraints=[SQL("DEFAULT 0")])
    product_id = CharField(constraints=[SQL("DEFAULT '0'")])
    sku_id = CharField(constraints=[SQL("DEFAULT '0'")])
    stock = IntegerField(constraints=[SQL("DEFAULT 0")])
    updated_at = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'skus_copy'
        indexes = (
            (('app_id', 'product_id'), False),
            (('app_id', 'product_id', 'sku_id'), True),
        )

class SourceBatch(BaseModel):
    app_base = CharField(constraints=[SQL("DEFAULT ''")])
    app_compare = CharField(constraints=[SQL("DEFAULT ''")])
    batch_no = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    created_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], index=True)
    id = BigAutoField()
    status_base = IntegerField(constraints=[SQL("DEFAULT 0")])
    status_compare = IntegerField(constraints=[SQL("DEFAULT 0")])
    updated_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])

    class Meta:
        table_name = 'source_batch'

class TbActivityBaseInfo(BaseModel):
    activity_id = CharField(constraints=[SQL("DEFAULT '0'")], index=True, null=True)
    activity_name = CharField(constraints=[SQL("DEFAULT ''")])
    activity_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    add_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    add_user = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    app_id = CharField(constraints=[SQL("DEFAULT ''")])
    end_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    memo = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    start_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    update_user = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    user_type = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'tb_activity_base_info'

class TbActivityFetchCouponInfo(BaseModel):
    activity_id = CharField(constraints=[SQL("DEFAULT '0'")], unique=True)
    add_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    coupon_group_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    id = BigAutoField()
    people_file_address = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    people_id = CharField(constraints=[SQL("DEFAULT '0'")])
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'tb_activity_fetch_coupon_info'

class TbActivityPeopleInfo(BaseModel):
    activity_id = CharField(constraints=[SQL("DEFAULT '0'")])
    add_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    people_id = CharField(constraints=[SQL("DEFAULT '0'")])
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    user_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    user_type = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'tb_activity_people_info'
        indexes = (
            (('activity_id', 'people_id'), False),
        )

class TbActivityUserFetchInfo(BaseModel):
    activity_id = CharField(constraints=[SQL("DEFAULT '0'")])
    activity_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    add_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    coupon_code = CharField(constraints=[SQL("DEFAULT '0'")], null=True)
    coupon_group_id = CharField(constraints=[SQL("DEFAULT '0'")], null=True)
    fetch_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    memo = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    people_id = CharField(constraints=[SQL("DEFAULT '0'")])
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    user_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    user_type = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'tb_activity_user_fetch_info'
        indexes = (
            (('activity_id', 'user_id'), False),
        )

class TbCouponBaseInfo(BaseModel):
    add_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    app_id = CharField(constraints=[SQL("DEFAULT ''")])
    coupon_code = CharField(constraints=[SQL("DEFAULT '0'")], null=True)
    coupon_group_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    coupon_group_name = CharField(constraints=[SQL("DEFAULT ''")])
    coupon_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    coupon_type = IntegerField(constraints=[SQL("DEFAULT 1")])
    coupon_value = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    discount_value = IntegerField(constraints=[SQL("DEFAULT 0")])
    end_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    extra = CharField(constraints=[SQL("DEFAULT '""'")])
    extra1 = CharField(constraints=[SQL("DEFAULT ''")])
    issue_source = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    max_deduct_price = IntegerField(constraints=[SQL("DEFAULT 0")])
    price_limit = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    start_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    user_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    user_type = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'tb_coupon_base_info'
        indexes = (
            (('user_id', 'coupon_code'), False),
            (('user_id', 'coupon_value'), False),
        )

class TbCouponConsume(BaseModel):
    add_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    coupon_code = CharField(constraints=[SQL("DEFAULT ''")])
    operate_type = IntegerField()
    out_biz_id = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    user_id = BigIntegerField()
    user_type = IntegerField()

    class Meta:
        table_name = 'tb_coupon_consume'

class TbCouponGroupBaseInfo(BaseModel):
    add_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    add_user = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    app_id = CharField(constraints=[SQL("DEFAULT ''")])
    coupon_group_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], unique=True)
    coupon_group_name = CharField(constraints=[SQL("DEFAULT ''")])
    coupon_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    coupon_value = IntegerField(constraints=[SQL("DEFAULT 0")])
    discount_value = IntegerField(constraints=[SQL("DEFAULT 0")])
    effective_days = IntegerField(constraints=[SQL("DEFAULT 0")])
    end_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    instruction = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    max_deduct_price = IntegerField(constraints=[SQL("DEFAULT 0")])
    max_per_user = IntegerField(constraints=[SQL("DEFAULT 1")])
    memo = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    price_limit = IntegerField(constraints=[SQL("DEFAULT 0")])
    remain_stock_num = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    start_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    total_stock_num = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    update_user = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    use_rule_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    user_type = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'tb_coupon_group_base_info'

class TbCouponGroupProductRuleInfo(BaseModel):
    add_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    coupon_group_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    product_id = CharField(constraints=[SQL("DEFAULT ''")])
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'tb_coupon_group_product_rule_info'
        indexes = (
            (('coupon_group_id', 'product_id'), False),
        )

class TbOrderDeduct(BaseModel):
    code = CharField(null=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    deduct_price = BigIntegerField(null=True)
    deduct_type = IntegerField(null=True)
    id = BigAutoField()
    is_delete = IntegerField(null=True)
    order_id = BigIntegerField(null=True)
    order_item_id = BigIntegerField(null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'tb_order_deduct'

class TbOrderExtraData(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    extra_data = CharField(null=True)
    id = BigAutoField()
    order_id = BigIntegerField(null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'tb_order_extra_data'

class TbOrderItem(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    id = BigAutoField()
    old_status = IntegerField(null=True)
    order_id = BigIntegerField(null=True)
    product_id = CharField(null=True)
    product_num = BigIntegerField(null=True)
    status = IntegerField(null=True)
    unit_price = BigIntegerField(null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'tb_order_item'

class TbOrderLog(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    desc = CharField(null=True)
    id = BigAutoField()
    new_status = IntegerField(null=True)
    new_status_desc = CharField(null=True)
    old_status = IntegerField(null=True)
    old_status_desc = CharField(null=True)
    order_id = BigIntegerField(null=True)
    order_item_id = BigIntegerField(null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'tb_order_log'

class TbOrders(BaseModel):
    app_id = CharField(null=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    id = BigAutoField()
    old_status = IntegerField(null=True)
    order_no = CharField(null=True)
    order_type = IntegerField(null=True)
    out_order_no = CharField(null=True)
    status = IntegerField(null=True)
    total_fee = BigIntegerField(null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    user_id = BigIntegerField(null=True)
    user_type = IntegerField(null=True)

    class Meta:
        table_name = 'tb_orders'

class Timer(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    event = CharField(null=True)
    expire_at = DateTimeField(null=True)
    id = BigAutoField()
    notice = CharField(null=True)
    o_id = CharField(null=True)
    reason = CharField(null=True)
    status = IntegerField(null=True)
    times = IntegerField(null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    workflow_name = CharField(null=True)

    class Meta:
        table_name = 'timer'

class WechatBill20191111(BaseModel):
    amount = IntegerField(null=True)
    created = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    currency = CharField(null=True)
    date = CharField(null=True)
    order_no = CharField(index=True, null=True)
    out_order_no = CharField(null=True)
    out_refund_no = CharField(null=True)
    refund_amount = IntegerField(null=True)
    refund_no = CharField(null=True)
    scene_id = IntegerField(null=True)

    class Meta:
        table_name = 'wechat_bill_20191111'

class WechatBill20191112(BaseModel):
    amount = IntegerField(null=True)
    created = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    currency = CharField(null=True)
    date = CharField(null=True)
    order_no = CharField(index=True, null=True)
    out_order_no = CharField(null=True)
    out_refund_no = CharField(null=True)
    refund_amount = IntegerField(null=True)
    refund_no = CharField(null=True)
    scene_id = IntegerField(null=True)

    class Meta:
        table_name = 'wechat_bill_20191112'

class WechatBill20191113(BaseModel):
    amount = IntegerField(null=True)
    created = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    currency = CharField(null=True)
    date = CharField(null=True)
    order_no = CharField(index=True, null=True)
    out_order_no = CharField(null=True)
    out_refund_no = CharField(null=True)
    refund_amount = IntegerField(null=True)
    refund_no = CharField(null=True)
    scene_id = IntegerField(null=True)

    class Meta:
        table_name = 'wechat_bill_20191113'

class WechatBill20191115(BaseModel):
    amount = IntegerField(null=True)
    created = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    currency = CharField(null=True)
    date = CharField(null=True)
    order_no = CharField(index=True, null=True)
    out_order_no = CharField(null=True)
    out_refund_no = CharField(null=True)
    refund_amount = IntegerField(null=True)
    refund_no = CharField(null=True)
    scene_id = IntegerField(null=True)

    class Meta:
        table_name = 'wechat_bill_20191115'

class WechatBill20200210(BaseModel):
    amount = IntegerField(null=True)
    created = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    currency = CharField(null=True)
    date = CharField(null=True)
    order_no = CharField(null=True, unique=True)
    out_order_no = CharField(null=True)
    out_refund_no = CharField(null=True)
    refund_amount = IntegerField(null=True)
    refund_no = CharField(null=True)

    class Meta:
        table_name = 'wechat_bill_20200210'

class WechatBill20200502(BaseModel):
    amount = IntegerField(null=True)
    created = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    currency = CharField(null=True)
    date = CharField(null=True)
    order_no = CharField(null=True, unique=True)
    out_order_no = CharField(null=True)
    out_refund_no = CharField(null=True)
    refund_amount = IntegerField(null=True)
    refund_no = CharField(null=True)

    class Meta:
        table_name = 'wechat_bill_20200502'

class Withdraw(BaseModel):
    amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    app_id = CharField(constraints=[SQL("DEFAULT ''")])
    channel_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    channel_scene_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP(6)")])
    err_msg = CharField(constraints=[SQL("DEFAULT ''")])
    id = BigAutoField()
    mch_app_id = CharField(constraints=[SQL("DEFAULT ''")])
    open_id = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    order_no = CharField(constraints=[SQL("DEFAULT ''")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    tp_trade_no = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP(6)")])

    class Meta:
        table_name = 'withdraw'
        indexes = (
            (('app_id', 'order_no'), True),
        )

class Workflow(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    data = TextField(null=True)
    id = BigAutoField()
    is_delete = IntegerField(null=True)
    name = CharField(null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'workflow'

class WorkflowData(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    id = BigAutoField()
    out_id = CharField(null=True, unique=True)
    status = CharField(null=True)
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'workflow_data'
