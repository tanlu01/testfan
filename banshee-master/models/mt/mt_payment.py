from peewee import *

database = MySQLDatabase('mt_payment', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': 'rm-uf6pec9k82nsk59o8.mysql.rds.aliyuncs.com', 'port': 3306, 'user': 'root', 'password': 'cFsc34^8pVm'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Contract(BaseModel):
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    contract_body = TextField(null=True)
    contract_code = CharField(constraints=[SQL("DEFAULT ''")], unique=True)
    contract_expired_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    contract_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], unique=True)
    contract_termination_mode = IntegerField(constraints=[SQL("DEFAULT 0")])
    contract_time = DateTimeField(null=True)
    contract_type = IntegerField(constraints=[SQL("DEFAULT 1")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    cycle_period = IntegerField(constraints=[SQL("DEFAULT 0")])
    cycle_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    delete_contract_body = TextField(null=True)
    delete_contract_time = DateTimeField(null=True)
    id = BigAutoField()
    out_contract_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    pap_expected_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    pap_template_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    pay_platform = IntegerField(constraints=[SQL("DEFAULT 0")])
    pay_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    payment_contract_id = CharField(constraints=[SQL("DEFAULT ''")])
    payment_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], unique=True)
    plan_id = CharField(constraints=[SQL("DEFAULT ''")])
    price = IntegerField(constraints=[SQL("DEFAULT 0")])
    request_serial = BigIntegerField(constraints=[SQL("DEFAULT 0")], unique=True)
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'contract'

class FailureRefundRecord(BaseModel):
    aftersale_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    bank_account = CharField(constraints=[SQL("DEFAULT ''")])
    bank_holder = CharField(constraints=[SQL("DEFAULT ''")])
    bank_name = CharField(constraints=[SQL("DEFAULT ''")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    failure_reason = CharField(constraints=[SQL("DEFAULT '0'")])
    finish_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    manual_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    operator_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    original_notification = TextField(null=True)
    original_response = TextField(null=True)
    other_account = CharField(constraints=[SQL("DEFAULT ''")])
    payee_qrcode_url = CharField(constraints=[SQL("DEFAULT ''")])
    payment_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    payment_order_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    payment_platform = IntegerField(constraints=[SQL("DEFAULT 0")])
    payment_receipt_url = CharField(constraints=[SQL("DEFAULT ''")])
    payment_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    real_name = CharField(constraints=[SQL("DEFAULT ''")])
    real_order_id = BigIntegerField(index=True)
    refund_amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    refund_method = IntegerField(constraints=[SQL("DEFAULT 0")])
    refund_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    retry_lock_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    type = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'failure_refund_record'
        indexes = (
            (('payment_order_id', 'refund_amount'), True),
        )

class MallTransfer(BaseModel):
    account_info_json = TextField(null=True)
    amount = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    failure_reason = CharField(constraints=[SQL("DEFAULT ''")])
    id = BigAutoField()
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    operator_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    original_body = TextField(null=True)
    original_notify = TextField(null=True)
    out_transfer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], unique=True)
    pay_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], index=True)
    query_response_body = TextField(null=True)
    t_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], unique=True)
    target_payment_buyer_id = CharField(constraints=[SQL("DEFAULT ''")])
    target_type = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    trade_id = CharField(constraints=[SQL("DEFAULT ''")])
    trade_platform = IntegerField(constraints=[SQL("DEFAULT 0")])
    transfer_desc = TextField(null=True)
    transfer_fee = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    transfer_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    transfer_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'mall_transfer'

class NaPayment(BaseModel):
    account_id = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    na_buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    order_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    order_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    original_notify = TextField(null=True)
    p_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    pay_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    payment_buyer_id = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    platform = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    price = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    refund_amount = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    trade_id = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    type = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    unified_body = TextField(null=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'na_payment'

class NaPaymentRefund(BaseModel):
    account_id = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    aftersale_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    id = BigAutoField()
    original_refund = TextField(null=True)
    original_response = TextField(null=True)
    p_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    price = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    refund_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    trade_id = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    type = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'na_payment_refund'

class NotificationTask(BaseModel):
    args_json = TextField(null=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    e_info_text = TextField(null=True)
    entity_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    entity_type = IntegerField(constraints=[SQL("DEFAULT 1")])
    eta = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    max_retries = IntegerField(constraints=[SQL("DEFAULT 0")])
    ret_val_json = TextField(null=True)
    retry_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    status_reason = CharField(constraints=[SQL("DEFAULT ''")])
    task_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], unique=True)
    type = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'notification_task'
        indexes = (
            (('entity_type', 'entity_id'), False),
        )

class PapLog(BaseModel):
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    contract_code = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    contract_id = BigIntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    notify_body = TextField(null=True)
    pap_expected_time = DateTimeField(null=True)
    pap_success_time = DateTimeField(null=True)
    pay_platform = IntegerField(constraints=[SQL("DEFAULT 0")])
    pay_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    payment_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    plan_id = CharField(constraints=[SQL("DEFAULT ''")])
    price = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'pap_log'

class PapTemplate(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    cycle_period = IntegerField(constraints=[SQL("DEFAULT 0")])
    cycle_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    name = CharField(constraints=[SQL("DEFAULT ''")])
    plan_id_alipay = CharField(constraints=[SQL("DEFAULT ''")])
    plan_id_wx = CharField(constraints=[SQL("DEFAULT ''")])
    plan_id_wxapp = CharField(constraints=[SQL("DEFAULT ''")])
    plan_id_wxmp = CharField(constraints=[SQL("DEFAULT ''")])
    price = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'pap_template'

class Payment(BaseModel):
    account_id = CharField(constraints=[SQL("DEFAULT ''")])
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    order_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    order_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    original_notify = TextField(null=True)
    pay_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    payment_buyer_id = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    platform = IntegerField(constraints=[SQL("DEFAULT 0")])
    price = IntegerField(constraints=[SQL("DEFAULT 0")])
    refund_amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    trade_id = CharField(constraints=[SQL("DEFAULT ''")])
    type = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    unified_body = TextField(null=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'payment'
        indexes = (
            (('order_type', 'order_id'), False),
        )

class PaymentAssistant(BaseModel):
    assistant_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    order_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    out_trade_no = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    payment_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], unique=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'payment_assistant'

class PaymentConfig(BaseModel):
    author = CharField(constraints=[SQL("DEFAULT '管理员'")])
    config = TextField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    version = CharField(unique=True)

    class Meta:
        table_name = 'payment_config'

class PaymentRefund(BaseModel):
    account_id = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    aftersale_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    id = BigAutoField()
    original_refund = TextField(null=True)
    original_response = TextField(null=True)
    payment_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    price = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    refund_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    sub_payment_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    trade_id = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    type = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'payment_refund'

class Separate(BaseModel):
    amount = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    description = CharField(constraints=[SQL("DEFAULT ''")])
    fail_reason = CharField(constraints=[SQL("DEFAULT ''")])
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    mall_sep_no = CharField(constraints=[SQL("DEFAULT ''")], unique=True)
    mch_id = CharField(constraints=[SQL("DEFAULT ''")])
    notify_body = TextField(null=True)
    order_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    sub_payment_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    success_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    type = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    wx_sep_no = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'separate'
        indexes = (
            (('order_id', 'mall_id'), False),
        )

class SubPayment(BaseModel):
    amount = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_union = IntegerField(constraints=[SQL("DEFAULT 0")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    mch_id = CharField(constraints=[SQL("DEFAULT ''")])
    order_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    out_trade_no = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    payment_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    transaction_id = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'sub_payment'
        indexes = (
            (('order_id', 'mall_id'), False),
        )

class Transfer(BaseModel):
    account_id = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    amount = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    id = BigAutoField()
    original_body = TextField(null=True)
    original_notify = TextField(null=True)
    out_transfer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    pay_platform = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    pay_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    pay_type = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    payment_buyer_id = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    status = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    t_id = BigIntegerField(unique=True)
    trade_id = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    transfer_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'transfer'
        indexes = (
            (('transfer_type', 'out_transfer_id'), True),
        )

class Withdraw(BaseModel):
    amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fail_reason = CharField(constraints=[SQL("DEFAULT ''")])
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    mch_id = CharField(constraints=[SQL("DEFAULT ''")])
    out_trade_id = CharField(constraints=[SQL("DEFAULT ''")])
    status = IntegerField(index=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    withdraw_id = CharField(constraints=[SQL("DEFAULT ''")], unique=True)

    class Meta:
        table_name = 'withdraw'

