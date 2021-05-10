from peewee import *

database = MySQLDatabase('pt_merchant', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': 'rm-uf6pec9k82nsk59o8.mysql.rds.aliyuncs.com', 'port': 3306, 'user': 'qa_rw_user', 'password': '8QoK6AjTvSMqs35lm4fwLuyPke0F'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class ActDeposit(BaseModel):
    account_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    charge_max_threshold = IntegerField(constraints=[SQL("DEFAULT -1")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    id = BigAutoField()
    mall_id = BigIntegerField(index=True)
    threshold_balance = IntegerField(constraints=[SQL("DEFAULT -1")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'act_deposit'

class AuditInfo(BaseModel):
    audit_content = CharField(constraints=[SQL("DEFAULT ''")])
    audit_msg = CharField(constraints=[SQL("DEFAULT ''")])
    audit_obj_id = BigIntegerField()
    audit_status = IntegerField()
    audit_submit_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    audit_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    audit_type = IntegerField()
    auditor_id = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'audit_info'
        indexes = (
            (('audit_type', 'audit_obj_id'), False),
        )

class BalanceChange(BaseModel):
    amount = BigIntegerField()
    balance_change_type = IntegerField()
    balance_new = IntegerField()
    batch_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    change_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    change_type = IntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    id = BigAutoField()
    mall_id = BigIntegerField()
    message = CharField()
    name = CharField(constraints=[SQL("DEFAULT ''")])
    op_name = CharField(constraints=[SQL("DEFAULT ''")])
    root_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    settle_begin_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    settle_end_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'balance_change'
        indexes = (
            (('mall_id', 'change_type'), False),
        )

class BdCatConf(BaseModel):
    bders = CharField(constraints=[SQL("DEFAULT ''")])
    cat_ids = CharField(constraints=[SQL("DEFAULT ''")])
    code = CharField(constraints=[SQL("DEFAULT ''")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    qq = CharField(constraints=[SQL("DEFAULT ''")])
    staple_category_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    summary = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'bd_cat_conf'

class BondedWarehouse(BaseModel):
    alipay_declare = CharField(constraints=[SQL("DEFAULT ''")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    customs_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    wechat_declare = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'bonded_warehouse'

class BrandAuth(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    image = CharField(constraints=[SQL("DEFAULT ''")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'brand_auth'

class BrandMallRef(BaseModel):
    brand_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'brand_mall_ref'
        indexes = (
            (('brand_id', 'mall_id'), True),
        )

class BrandRef(BaseModel):
    brand_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    category = CharField(constraints=[SQL("DEFAULT ''")])
    category_id = CharField(constraints=[SQL("DEFAULT '0'")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    operator_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    ref_brand_en_name = CharField(constraints=[SQL("DEFAULT ''")])
    ref_brand_full_name = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    ref_brand_log = CharField(constraints=[SQL("DEFAULT ''")])
    ref_brand_name = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    ref_source = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'brand_ref'

class Brands(BaseModel):
    brand_accept_cert = CharField(constraints=[SQL("DEFAULT ''")])
    brand_alias = CharField(constraints=[SQL("DEFAULT ''")])
    brand_cat_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    brand_cat_ids = CharField(constraints=[SQL("DEFAULT ''")])
    brand_customs_image = CharField(constraints=[SQL("DEFAULT ''")])
    brand_en_name = CharField(constraints=[SQL("DEFAULT ''")])
    brand_img = CharField(constraints=[SQL("DEFAULT ''")])
    brand_name = CharField(constraints=[SQL("DEFAULT ''")])
    brand_origin = IntegerField(constraints=[SQL("DEFAULT 0")])
    brand_owner = CharField(constraints=[SQL("DEFAULT ''")])
    brand_reg_cert = CharField(constraints=[SQL("DEFAULT ''")])
    brand_reg_number = CharField(constraints=[SQL("DEFAULT ''")])
    brand_reg_place = IntegerField(constraints=[SQL("DEFAULT 0")])
    brand_submit_phone = CharField(constraints=[SQL("DEFAULT ''")])
    brand_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    intro = CharField(constraints=[SQL("DEFAULT ''")])
    is_hot = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    is_international = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    is_mainstream = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    is_new_goods_detail = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    product_package_image = CharField(constraints=[SQL("DEFAULT ''")])
    rel_brand_name = CharField(constraints=[SQL("DEFAULT ''")])
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    slogan = CharField(constraints=[SQL("DEFAULT ''")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'brands'
        indexes = (
            (('brand_name', 'rel_brand_name'), False),
        )

class BrandsAssociation(BaseModel):
    brand_id = IntegerField()
    brand_pid = IntegerField(index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'brands_association'

class BrandsAudit(BaseModel):
    audit_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    audit_reason = CharField(constraints=[SQL("DEFAULT ''")])
    audit_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    brand_accept_cert = CharField(constraints=[SQL("DEFAULT ''")])
    brand_cat_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    brand_customs_image = CharField(constraints=[SQL("DEFAULT ''")])
    brand_en_name = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    brand_img = CharField(constraints=[SQL("DEFAULT ''")])
    brand_logo = CharField(constraints=[SQL("DEFAULT ''")])
    brand_name = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    brand_origin = IntegerField(constraints=[SQL("DEFAULT 0")])
    brand_owner = CharField(constraints=[SQL("DEFAULT ''")])
    brand_reg_cert = CharField(constraints=[SQL("DEFAULT ''")])
    brand_reg_number = CharField(constraints=[SQL("DEFAULT ''")])
    brand_reg_place = IntegerField(constraints=[SQL("DEFAULT 0")])
    brand_submit_phone = CharField(constraints=[SQL("DEFAULT ''")])
    brands_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    product_package_image = CharField(constraints=[SQL("DEFAULT ''")])
    rel_brand_name = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'brands_audit'

class Category(BaseModel):
    auto_sign = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_1 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_10 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_2 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_3 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_4 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_5 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_6 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_7 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_8 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_9 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_name = CharField(index=True)
    config = TextField(null=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    description = CharField(constraints=[SQL("DEFAULT ''")])
    dst_item = IntegerField(constraints=[SQL("DEFAULT 0")])
    example_picture_array = TextField(null=True)
    forbid_refund = IntegerField(constraints=[SQL("DEFAULT 0")])
    image_url = CharField(constraints=[SQL("DEFAULT ''")])
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_hidden = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_leaf = IntegerField(constraints=[SQL("DEFAULT 1")])
    is_review = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_review_image = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_support_wayward_return = IntegerField(constraints=[SQL("DEFAULT 0")])
    level = IntegerField(constraints=[SQL("DEFAULT 1")], index=True)
    max_price = IntegerField(constraints=[SQL("DEFAULT 0")])
    min_price = IntegerField(constraints=[SQL("DEFAULT 0")])
    parent_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    price_range_ratio = IntegerField(constraints=[SQL("DEFAULT 0")])
    priority = IntegerField()
    receiver_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'category'

class Category2(BaseModel):
    auto_sign = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_1 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_10 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_2 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_3 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_4 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_5 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_6 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_7 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_8 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_9 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_name = CharField(index=True)
    config = TextField(null=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    description = CharField(constraints=[SQL("DEFAULT ''")])
    dst_item = IntegerField(constraints=[SQL("DEFAULT 0")])
    example_picture_array = TextField(null=True)
    forbid_refund = IntegerField(constraints=[SQL("DEFAULT 0")])
    image_url = CharField(constraints=[SQL("DEFAULT ''")])
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_hidden = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_leaf = IntegerField(constraints=[SQL("DEFAULT 1")])
    is_review = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_review_image = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_support_wayward_return = IntegerField(constraints=[SQL("DEFAULT 0")])
    level = IntegerField(constraints=[SQL("DEFAULT 1")], index=True)
    max_price = IntegerField(constraints=[SQL("DEFAULT 0")])
    min_price = IntegerField(constraints=[SQL("DEFAULT 0")])
    parent_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    price_range_ratio = IntegerField(constraints=[SQL("DEFAULT 0")])
    priority = IntegerField()
    receiver_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'category2'

class Charge(BaseModel):
    amount = BigIntegerField()
    charge_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    goods_id = BigIntegerField()
    id = BigAutoField()
    mall_id = BigIntegerField(index=True)
    order_sn = BigIntegerField()
    reason = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'charge'

class CostTemplate(BaseModel):
    cost_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    default_express = CharField(constraints=[SQL("DEFAULT ''")])
    dispatch_cost = TextField(null=True)
    dispatch_free = TextField(null=True)
    dispatch_place = TextField(null=True)
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    mall_id = BigIntegerField(index=True)
    name = CharField()
    new_dispatch_cost = TextField(null=True)
    new_dispatch_free = TextField(null=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'cost_template'

class Country(BaseModel):
    name = CharField(null=True)

    class Meta:
        table_name = 'country'

class CredentialsAudit(BaseModel):
    audit_status = IntegerField(constraints=[SQL("DEFAULT 1")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    credential_id = IntegerField(index=True)
    deadline = DateField()
    images = CharField(constraints=[SQL("DEFAULT ''")])
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    mall_id = BigIntegerField(index=True)
    name = CharField()
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'credentials_audit'

class CredentialsCatConfig(BaseModel):
    cat_id = IntegerField(index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    credentials_id = CharField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    staple_id = IntegerField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'credentials_cat_config'

class CredentialsImgConfig(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    image = CharField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    staple_id = IntegerField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'credentials_img_config'

class Customs(BaseModel):
    alipay_name = CharField(constraints=[SQL("DEFAULT ''")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_open = IntegerField(constraints=[SQL("DEFAULT 1")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    wechat_name = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'customs'

class CutPayment(BaseModel):
    amount = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    desc = TextField(null=True)
    id = BigAutoField()
    mall_id = BigIntegerField()
    reason = TextField(null=True)
    type = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'cut_payment'

class Deposit(BaseModel):
    account_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    charge_max_threshold = IntegerField(constraints=[SQL("DEFAULT -1")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    id = BigAutoField()
    mall_id = BigIntegerField(index=True)
    threshold_balance = IntegerField(constraints=[SQL("DEFAULT -1")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'deposit'

class DepositConfig(BaseModel):
    charge_max_threshold = IntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    property_id = IntegerField()
    staple_id = IntegerField()
    threshold_balance = IntegerField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'deposit_config'
        indexes = (
            (('staple_id', 'property_id'), True),
        )

class DimBrand(BaseModel):
    brand_name = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    type = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'dim_brand'

class ExpensesDetail(BaseModel):
    amount = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    is_cost = IntegerField(constraints=[SQL("DEFAULT 0")])
    mall_id = BigIntegerField()
    order_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    type = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'expenses_detail'

class Feedback(BaseModel):
    content = CharField(constraints=[SQL("DEFAULT ''")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    image = CharField(constraints=[SQL("DEFAULT ''")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    mobile = CharField(constraints=[SQL("DEFAULT ''")])
    module = IntegerField(constraints=[SQL("DEFAULT 0")])
    qq = CharField(constraints=[SQL("DEFAULT ''")])
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'feedback'

class FrontendCat(BaseModel):
    cat_id_1 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_10 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_2 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_3 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_4 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_5 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_6 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_7 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_8 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_9 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_name = CharField(constraints=[SQL("DEFAULT ''")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    image = CharField(constraints=[SQL("DEFAULT ''")])
    is_leaf = IntegerField(constraints=[SQL("DEFAULT 1")])
    level = IntegerField(constraints=[SQL("DEFAULT 1")])
    parent_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    sort = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'frontend_cat'

class FrontendCatBack20200401(BaseModel):
    cat_id_1 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_10 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_2 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_3 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_4 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_5 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_6 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_7 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_8 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_9 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_name = CharField(constraints=[SQL("DEFAULT ''")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    image = CharField(constraints=[SQL("DEFAULT ''")])
    is_leaf = IntegerField(constraints=[SQL("DEFAULT 1")])
    level = IntegerField(constraints=[SQL("DEFAULT 1")])
    parent_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    sort = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'frontend_cat_back_20200401'

class FrontendCatRelated(BaseModel):
    backend_cat_id = IntegerField(constraints=[SQL("DEFAULT 0")], unique=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    frontend_cat_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'frontend_cat_related'

class FrontendCatRelated20200401(BaseModel):
    backend_cat_id = IntegerField(constraints=[SQL("DEFAULT 0")], unique=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    frontend_cat_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'frontend_cat_related_20200401'

class GlobalConfig(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    name = CharField(primary_key=True)
    namespace = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    title = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    value = TextField(null=True)

    class Meta:
        table_name = 'global_config'

class GoodsPackage(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    id = BigAutoField()
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    package_material_id = IntegerField(constraints=[SQL("DEFAULT 1")])
    state = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'goods_package'
        indexes = (
            (('mall_id', 'goods_id'), True),
        )

class GoodsTop(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    sort = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'goods_top'
        indexes = (
            (('mall_id', 'goods_id'), True),
        )

class HotInvestment(BaseModel):
    brand_name = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    cat_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    cat_id_1 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_10 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_2 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_3 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_4 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_5 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_6 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_7 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_8 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_9 = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    data_source = IntegerField(constraints=[SQL("DEFAULT 0")])
    data_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    goods_image = CharField(constraints=[SQL("DEFAULT ''")])
    goods_name = CharField(constraints=[SQL("DEFAULT ''")])
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    operator_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    operator_name = CharField(constraints=[SQL("DEFAULT ''")])
    other_platforms_link = CharField(constraints=[SQL("DEFAULT ''")])
    price_max = IntegerField(constraints=[SQL("DEFAULT 0")])
    price_min = IntegerField(constraints=[SQL("DEFAULT 0")])
    source_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    staple_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'hot_investment'
        indexes = (
            (('staple_id', 'cat_id_1', 'cat_id_2', 'cat_id_3'), False),
        )

class HotInvestmentGoods(BaseModel):
    cat_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], unique=True)
    hot_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    id = BigAutoField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'hot_investment_goods'

class InvestmentPlan(BaseModel):
    add_remark = TextField(null=True)
    brand_name = CharField(constraints=[SQL("DEFAULT ''")])
    brand_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    cat_id_1 = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    feedback_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    investment_user_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    investment_user_name = CharField(constraints=[SQL("DEFAULT ''")])
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_transfer_hot = IntegerField(constraints=[SQL("DEFAULT 0")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    mall_status = IntegerField(constraints=[SQL("DEFAULT -1")])
    manager_name = CharField(constraints=[SQL("DEFAULT ''")])
    operator_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    operator_name = CharField(constraints=[SQL("DEFAULT ''")])
    other_platforms_link = CharField(constraints=[SQL("DEFAULT ''")])
    price_range = CharField(constraints=[SQL("DEFAULT ''")])
    relate_name = CharField(constraints=[SQL("DEFAULT ''")])
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    staple_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    type = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'investment_plan'

class InvestmentPlanGoal(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    goal = IntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    investment_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    investment_user_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    investment_user_name = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'investment_plan_goal'

class InvestmentStats(BaseModel):
    cat_id_1 = IntegerField(constraints=[SQL("DEFAULT 0")])
    commission = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    investment_user_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    investment_user_name = CharField(constraints=[SQL("DEFAULT ''")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    service_charge = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    settled_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    staple_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'investment_stats'

class JdCatMap(BaseModel):
    cat_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    jd_cat_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'jd_cat_map'

class Mall(BaseModel):
    account_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    activation_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    chat_enable = IntegerField(constraints=[SQL("DEFAULT 0")])
    company_phone = CharField(constraints=[SQL("DEFAULT ''")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    default_refund_address_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    extra_conf = TextField(null=True)
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_freight_insurance = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_open = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_self_support = IntegerField(constraints=[SQL("DEFAULT 0")])
    logo = CharField(constraints=[SQL("DEFAULT ''")])
    mall_desc = CharField(constraints=[SQL("DEFAULT ''")])
    mall_name = CharField(index=True)
    mall_type = IntegerField()
    offline_note = CharField(constraints=[SQL("DEFAULT ''")])
    property_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    qq = CharField(constraints=[SQL("DEFAULT ''")])
    return_address = CharField(constraints=[SQL("DEFAULT ''")])
    staple_id = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    wallpaper = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'mall'

class MallAutoReplyGoods(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    goods_id = BigIntegerField(index=True)
    id = BigAutoField()
    mall_auto_reply_id = BigIntegerField(index=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'mall_auto_reply_goods'
        indexes = (
            (('mall_auto_reply_id', 'goods_id'), False),
        )

class MallAutoReplyText(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    id = BigAutoField()
    mall_id = BigIntegerField(index=True)
    reply_text = CharField(constraints=[SQL("DEFAULT ''")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'mall_auto_reply_text'
        indexes = (
            (('mall_id', 'status'), False),
        )

class MallBalance(BaseModel):
    activity_deposit_cash = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    goods_payment_expend = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    goods_payment_income = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    mall_id = BigIntegerField()
    shop_deposit_cash = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'mall_balance'

class MallBank(BaseModel):
    account_name = CharField(index=True)
    account_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    auth_pic_path = CharField(constraints=[SQL("DEFAULT ''")])
    bank_card_id = CharField()
    bank_id = BigAutoField()
    bank_name = CharField(index=True)
    bank_sub_name = CharField()
    city_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    city_name = CharField()
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id_card = CharField(index=True)
    is_del = IntegerField(constraints=[SQL("DEFAULT 0")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    mobile = CharField()
    province_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    province_name = CharField()
    settlement_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    state = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'mall_bank'
        indexes = (
            (('mall_id', 'state'), False),
            (('settlement_status', 'is_del'), False),
            (('state', 'update_at'), False),
        )

class MallBankAuthLog(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    handler_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    handler_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    mall_bank_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    state = IntegerField(constraints=[SQL("DEFAULT 1")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'mall_bank_auth_log'
        indexes = (
            (('mall_bank_id', 'state'), False),
        )

class MallBrand(BaseModel):
    audit_brand_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    brand_en_name = CharField(constraints=[SQL("DEFAULT ''")])
    brand_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    brand_imgs = TextField(null=True)
    brand_name = CharField(constraints=[SQL("DEFAULT ''")])
    brand_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    cate_id = CharField(constraints=[SQL("DEFAULT ''")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    deadline = DateField(null=True)
    detail_ids = CharField(constraints=[SQL("DEFAULT ''")])
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_longterm = IntegerField(constraints=[SQL("DEFAULT 0")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    other_sale_plt_link = CharField(constraints=[SQL("DEFAULT ''")])
    remark = TextField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'mall_brand'
        indexes = (
            (('brand_id', 'audit_brand_id'), False),
        )

class MallBrandAuth(BaseModel):
    brand_auth_cert = CharField(constraints=[SQL("DEFAULT ''")])
    brand_en_name = CharField(constraints=[SQL("DEFAULT ''")])
    brand_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    brand_img = CharField(constraints=[SQL("DEFAULT ''")])
    brand_logo = CharField(constraints=[SQL("DEFAULT ''")])
    brand_name = CharField(constraints=[SQL("DEFAULT ''")])
    brand_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    company_name = CharField(constraints=[SQL("DEFAULT ''")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    expire_date = DateField(null=True)
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'mall_brand_auth'
        indexes = (
            (('mall_id', 'brand_id'), True),
        )

class MallBrandDetail(BaseModel):
    brand_link_sort = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    expire_date = DateField(null=True)
    identity_cert = CharField(constraints=[SQL("DEFAULT ''")])
    image = TextField()
    mall_brand_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    num = CharField(constraints=[SQL("DEFAULT ''")])
    purchase_certs = CharField(constraints=[SQL("DEFAULT ''")])
    trademark_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    type = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'mall_brand_detail'

class MallBrandQualification(BaseModel):
    business_license = CharField(constraints=[SQL("DEFAULT ''")])
    business_license_term = DateField(constraints=[SQL("DEFAULT 0000-00-00")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    enter_country_date = DateField(constraints=[SQL("DEFAULT 0000-00-00")])
    entry_date = DateField(constraints=[SQL("DEFAULT 0000-00-00")])
    entry_declaration = CharField(constraints=[SQL("DEFAULT ''")])
    entry_exit_quarantine_cert = CharField(constraints=[SQL("DEFAULT ''")])
    is_abroad = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    mall_brand_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    produce_licence = CharField(constraints=[SQL("DEFAULT ''")])
    produce_licence_term = DateField(constraints=[SQL("DEFAULT 0000-00-00")])
    produce_proxy_statement = CharField(constraints=[SQL("DEFAULT ''")])
    type = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'mall_brand_qualification'
        indexes = (
            (('mall_brand_id', 'type'), True),
        )

class MallCategory(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    goods_ids = TextField(null=True)
    id = BigAutoField()
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    name = CharField()
    pos = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'mall_category'

class MallClear(BaseModel):
    clear_count_down = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    clear_end_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    deposit_fine = IntegerField(constraints=[SQL("DEFAULT 0")])
    goods_cash_refund_id = CharField(constraints=[SQL("DEFAULT ''")])
    goods_fine = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_end_shipped_order = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_end_unshipped_order = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_freeze_balance = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_refund = IntegerField(constraints=[SQL("DEFAULT 0")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], unique=True)
    reason = CharField(constraints=[SQL("DEFAULT ''")])
    shop_cash_refund_id = CharField(constraints=[SQL("DEFAULT ''")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'mall_clear'

class MallClearLog(BaseModel):
    clear_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    operator_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    step = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'mall_clear_log'
        indexes = (
            (('clear_id', 'mall_id'), False),
        )

class MallCustoms(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    customs_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    declare_type = IntegerField(constraints=[SQL("DEFAULT 2")])
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    mall_customs_name = CharField(constraints=[SQL("DEFAULT ''")])
    mall_customs_no = CharField(constraints=[SQL("DEFAULT ''")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'mall_customs'

class MallExtra(BaseModel):
    biz_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    biz_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    extra = CharField(constraints=[SQL("DEFAULT ''")])
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    set_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'mall_extra'
        indexes = (
            (('biz_type', 'biz_status', 'set_time'), False),
            (('mall_id', 'biz_type', 'biz_status'), True),
        )

class MallExtraAction(BaseModel):
    begin_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    end_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], index=True)
    id = BigAutoField()
    mall_extra_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'mall_extra_action'

class MallFactory(BaseModel):
    address = CharField(constraints=[SQL("DEFAULT ''")])
    area = IntegerField(constraints=[SQL("DEFAULT 0")])
    area_unit = IntegerField(constraints=[SQL("DEFAULT 1")])
    bl_expired_at = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    bl_img = CharField(constraints=[SQL("DEFAULT ''")])
    city_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    company = CharField(constraints=[SQL("DEFAULT ''")])
    company_img = TextField(null=True)
    concept = CharField(constraints=[SQL("DEFAULT ''")])
    country_id = IntegerField(constraints=[SQL("DEFAULT 1")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    district_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    employee_num = IntegerField(constraints=[SQL("DEFAULT 0")])
    establish_at = CharField(constraints=[SQL("DEFAULT ''")])
    factory_img = TextField(null=True)
    id = BigAutoField()
    is_bl_long_term = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 2")])
    is_long_term = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_same_company = IntegerField(constraints=[SQL("DEFAULT 1")])
    legal_person_name = CharField(constraints=[SQL("DEFAULT ''")])
    license_expire_at = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    license_img = TextField(null=True)
    lp_idcard_back_img = CharField(constraints=[SQL("DEFAULT ''")])
    lp_idcard_expired_at = CharField(constraints=[SQL("DEFAULT ''")])
    lp_idcard_front_img = CharField(constraints=[SQL("DEFAULT ''")])
    lp_idcard_no = CharField(constraints=[SQL("DEFAULT ''")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], unique=True)
    patent_img = TextField(null=True)
    province_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    uscc = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    volume = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'mall_factory'

class MallFactoryBrand(BaseModel):
    brand_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    factory_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    prove_img = TextField(null=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'mall_factory_brand'
        indexes = (
            (('mall_id', 'factory_id', 'brand_id'), True),
        )

class MallGoodsQualification(BaseModel):
    approval_at = DateField(constraints=[SQL("DEFAULT 0000-00-00")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    expired_at = DateField(constraints=[SQL("DEFAULT 0000-00-00")])
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    qualification = CharField(constraints=[SQL("DEFAULT ''")])
    qualification_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'mall_goods_qualification'
        indexes = (
            (('expired_at', 'is_deleted'), False),
            (('goods_id', 'qualification_type'), True),
        )

class MallGoodsRecommend(BaseModel):
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    sort = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'mall_goods_recommend'

class MallHistory(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    handler_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    merchant_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    modify_fields = TextField(null=True)
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'mall_history'

class MallHotInvestment(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    hot_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    id = BigAutoField()
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    type = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'mall_hot_investment'

class MallMenu(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    icon = CharField(constraints=[SQL("DEFAULT ''")])
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_show = IntegerField(constraints=[SQL("DEFAULT 1")])
    level = IntegerField(constraints=[SQL("DEFAULT 0")])
    name = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    parent_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    path = CharField(constraints=[SQL("DEFAULT ''")])
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    sort = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    uri = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'mall_menu'

class MallMenuGrayscale(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    menu_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    switch_conf = TextField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'mall_menu_grayscale'

class MallMenuResource(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    menu_id = IntegerField()
    resource_id = IntegerField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'mall_menu_resource'

class MallMobileChangeRecord(BaseModel):
    business_license = CharField(constraints=[SQL("DEFAULT ''")])
    commitment = CharField(constraints=[SQL("DEFAULT ''")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    new_mobile = CharField(constraints=[SQL("DEFAULT ''")])
    old_mobile = CharField(constraints=[SQL("DEFAULT ''")])
    reason = CharField(constraints=[SQL("DEFAULT ''")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'mall_mobile_change_record'

class MallPopup(BaseModel):
    biz_status = IntegerField(constraints=[SQL("DEFAULT 1")])
    biz_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    content = CharField(constraints=[SQL("DEFAULT ''")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    expire_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    img = CharField(constraints=[SQL("DEFAULT ''")])
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    link = CharField(constraints=[SQL("DEFAULT ''")])
    scope = IntegerField(constraints=[SQL("DEFAULT 0")])
    start_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    title = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], index=True)

    class Meta:
        table_name = 'mall_popup'
        indexes = (
            (('start_at', 'expire_at'), False),
        )

class MallPopupRel(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    mall_popup_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    msg_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'mall_popup_rel'

class MallPopupSeller(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    mall_popup_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    open_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    seller_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'mall_popup_seller'
        indexes = (
            (('mall_id', 'seller_id'), False),
            (('mall_popup_id', 'mall_id', 'seller_id'), True),
        )

class MallPunishmentBatchRecord(BaseModel):
    batch_num = CharField(constraints=[SQL("DEFAULT ''")], unique=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    handle_result = TextField(null=True)
    mall_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    punishment_text = TextField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'mall_punishment_batch_record'

class MallPunishmentLimit(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    detail = TextField(null=True)
    id = BigAutoField()
    limit_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    scene_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'mall_punishment_limit'

class MallPunishmentNodeRecord(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    node_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    node_score = IntegerField(constraints=[SQL("DEFAULT 0")])
    punishment_detail = TextField(null=True)
    punishment_year = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'mall_punishment_node_record'
        indexes = (
            (('mall_id', 'node_id', 'punishment_year', 'status'), True),
        )

class MallPunishmentRecord(BaseModel):
    annex = CharField(constraints=[SQL("DEFAULT ''")])
    appeal_detail = TextField(null=True)
    appeal_images = TextField(null=True)
    confirm_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    detail = TextField(null=True)
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    handle_detail = TextField(null=True)
    handle_images = TextField(null=True)
    handler_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    images = TextField(null=True)
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    order_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    punish_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    rule_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    source_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'mall_punishment_record'

class MallPunishmentRecordDetail(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    punishment_detail = TextField(null=True)
    punishment_result = TextField(null=True)
    punishment_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    record_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'mall_punishment_record_detail'
        indexes = (
            (('record_id', 'punishment_type'), True),
        )

class MallPunishmentRecordRelation(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    logistic_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    order_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    punishment_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    reason = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'mall_punishment_record_relation'

class MallPunishmentRule(BaseModel):
    appeal_status = IntegerField(constraints=[SQL("DEFAULT 1")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    detail = TextField(null=True)
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    rule = TextField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    title = CharField(constraints=[SQL("DEFAULT ''")])
    type = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'mall_punishment_rule'

class MallPunishmentScore(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], unique=True)
    normal_score = IntegerField(constraints=[SQL("DEFAULT 0")])
    serious_score = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'mall_punishment_score'

class MallQqGroup(BaseModel):
    contact_phone = CharField(constraints=[SQL("DEFAULT ''")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], unique=True)
    qq = CharField(constraints=[SQL("DEFAULT ''")])
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'mall_qq_group'

class MallQqGroupRelation(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    mall_qq_id = IntegerField()
    qq_group_id = IntegerField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'mall_qq_group_relation'

class MallReg(BaseModel):
    annual_output_value = CharField(constraints=[SQL("DEFAULT ''")])
    apply_at = DateTimeField(null=True)
    brand = CharField(constraints=[SQL("DEFAULT ''")])
    brand_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    company_name = CharField(constraints=[SQL("DEFAULT ''")])
    company_region_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    deliver_region_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    factory_people_num = IntegerField(constraints=[SQL("DEFAULT 0")])
    factory_region_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    goods_info = CharField(constraints=[SQL("DEFAULT ''")])
    grant_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    has_off_chl = IntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_owner_factory = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_weekend_deliver = IntegerField(constraints=[SQL("DEFAULT 1")])
    mall_type = CharField(constraints=[SQL("DEFAULT ''")])
    mobile = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    name = CharField(constraints=[SQL("DEFAULT ''")])
    off_annual_gmv = CharField(constraints=[SQL("DEFAULT ''")])
    off_main_chl = CharField(constraints=[SQL("DEFAULT ''")])
    official_website = CharField(constraints=[SQL("DEFAULT ''")])
    other_platform_info = TextField(null=True)
    other_plt_link = CharField(constraints=[SQL("DEFAULT ''")])
    qq = CharField(constraints=[SQL("DEFAULT ''")])
    remark = TextField(null=True)
    staple_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'mall_reg'
        indexes = (
            (('company_name', 'staple_id'), True),
        )

class MallResource(BaseModel):
    access_to_close = IntegerField(constraints=[SQL("DEFAULT 1")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    name = CharField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    uri = CharField()

    class Meta:
        table_name = 'mall_resource'

class MallRetreatApply(BaseModel):
    apply_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    audit_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    deposit_withdraw_id = CharField(constraints=[SQL("DEFAULT ''")])
    goods_withdraw_id = CharField(constraints=[SQL("DEFAULT ''")])
    handler_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    is_optimize = IntegerField(constraints=[SQL("DEFAULT 0")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    notice_end_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    notice_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    reason = CharField(constraints=[SQL("DEFAULT ''")])
    refund_day = IntegerField(constraints=[SQL("DEFAULT 0")])
    refund_remark = CharField(constraints=[SQL("DEFAULT ''")])
    refund_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    refund_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    step = IntegerField(constraints=[SQL("DEFAULT 1")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'mall_retreat_apply'
        indexes = (
            (('mall_id', 'status'), False),
        )

class MallRetreatLog(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    id = BigAutoField()
    retreat_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    step = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'mall_retreat_log'
        indexes = (
            (('retreat_id', 'step'), True),
        )

class MallRole(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    desc = CharField(constraints=[SQL("DEFAULT ''")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    operator_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'mall_role'

class MallRoleMenu(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    menu_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    role_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'mall_role_menu'

class Merchant(BaseModel):
    audit_content = CharField(constraints=[SQL("DEFAULT ''")])
    audit_status = IntegerField()
    audit_success_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    bd_code = CharField(constraints=[SQL("DEFAULT ''")])
    category_id = IntegerField()
    company_name = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    company_phone = CharField(constraints=[SQL("DEFAULT ''")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    enterprise = TextField(null=True)
    has_third = IntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    individuality = TextField(null=True)
    invite_code = CharField(constraints=[SQL("DEFAULT ''")])
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_new = IntegerField(constraints=[SQL("DEFAULT 1")])
    is_self_support = IntegerField(constraints=[SQL("DEFAULT 0")])
    main_cat_id_1 = IntegerField(constraints=[SQL("DEFAULT 0")])
    mall_desc = CharField(constraints=[SQL("DEFAULT ''")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    mall_logo = CharField(constraints=[SQL("DEFAULT ''")])
    mall_name = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    merchant_type = IntegerField()
    operator_backup_mobile = CharField(constraints=[SQL("DEFAULT ''")])
    operator_backup_name = CharField(constraints=[SQL("DEFAULT ''")])
    operator_email = CharField(constraints=[SQL("DEFAULT ''")])
    operator_mobile = CharField(constraints=[SQL("DEFAULT ''")])
    operator_name = CharField(constraints=[SQL("DEFAULT ''")])
    property_id = IntegerField()
    refund_info = TextField()
    reject_reason = CharField(constraints=[SQL("DEFAULT '0'")])
    submit_ip = CharField(constraints=[SQL("DEFAULT ''")])
    submit_mobile = CharField(constraints=[SQL("DEFAULT ''")])
    submit_step = IntegerField(constraints=[SQL("DEFAULT 0")])
    third_party_mall_link_list = TextField(null=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'merchant'

class MerchantClassify(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    enable = IntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    image = CharField(constraints=[SQL("DEFAULT ''")])
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    level = IntegerField(constraints=[SQL("DEFAULT 0")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    name = CharField(constraints=[SQL("DEFAULT ''")])
    parent_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    sort = IntegerField(constraints=[SQL("DEFAULT 0")])
    type = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'merchant_classify'

class MerchantClassifyGoods(BaseModel):
    classify_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'merchant_classify_goods'

class MerchantCommit(BaseModel):
    audit_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    audit_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    diff = TextField(null=True)
    id = BigAutoField()
    is_new = IntegerField(constraints=[SQL("DEFAULT 0")])
    merchant_id = BigIntegerField(index=True)
    reject_reason = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'merchant_commit'

class MerchantRetreat(BaseModel):
    audit_content = CharField(constraints=[SQL("DEFAULT ''")])
    audit_status = IntegerField()
    audit_success_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    bd_code = CharField(constraints=[SQL("DEFAULT ''")])
    category_id = IntegerField()
    company_name = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    company_phone = CharField(constraints=[SQL("DEFAULT ''")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    enterprise = TextField(null=True)
    has_third = IntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    individuality = TextField(null=True)
    invite_code = CharField(constraints=[SQL("DEFAULT ''")])
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_new = IntegerField(constraints=[SQL("DEFAULT 1")])
    is_self_support = IntegerField(constraints=[SQL("DEFAULT 0")])
    main_cat_id_1 = IntegerField(constraints=[SQL("DEFAULT 0")])
    mall_desc = CharField(constraints=[SQL("DEFAULT ''")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    mall_logo = CharField(constraints=[SQL("DEFAULT ''")])
    mall_name = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    merchant_type = IntegerField()
    operator_backup_mobile = CharField(constraints=[SQL("DEFAULT ''")])
    operator_backup_name = CharField(constraints=[SQL("DEFAULT ''")])
    operator_email = CharField(constraints=[SQL("DEFAULT ''")])
    operator_mobile = CharField(constraints=[SQL("DEFAULT ''")])
    operator_name = CharField(constraints=[SQL("DEFAULT ''")])
    property_id = IntegerField()
    refund_info = TextField()
    reject_reason = CharField(constraints=[SQL("DEFAULT '0'")])
    restore_count_down = DateTimeField(null=True)
    restore_remark = CharField(constraints=[SQL("DEFAULT ''")])
    retreat_reason = CharField(constraints=[SQL("DEFAULT ''")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    submit_ip = CharField(constraints=[SQL("DEFAULT ''")])
    submit_mobile = CharField(constraints=[SQL("DEFAULT ''")])
    submit_step = IntegerField(constraints=[SQL("DEFAULT 0")])
    third_party_mall_link_list = TextField(null=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'merchant_retreat'

class MerchantTask(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    introduction = CharField(constraints=[SQL("DEFAULT ''")])
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    unique_code = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'merchant_task'

class MerchantTaskActivation(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], unique=True)
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    task = IntegerField(constraints=[SQL("DEFAULT 1")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'merchant_task_activation'

class MerchantTaskThirdAuth(BaseModel):
    auth_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    background_screenshot = CharField(constraints=[SQL("DEFAULT ''")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    description_score = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    id = BigAutoField()
    is_exceed_5_ten_thousand = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_gmv_reach = IntegerField(constraints=[SQL("DEFAULT 0")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    month_sales_amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    month_sales_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    reason = CharField(constraints=[SQL("DEFAULT ''")])
    server_score = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    set_up_shop_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    shop = IntegerField(constraints=[SQL("DEFAULT 0")])
    shop_name = CharField(constraints=[SQL("DEFAULT ''")])
    shop_url = CharField(constraints=[SQL("DEFAULT ''")])
    transportation_score = DecimalField(constraints=[SQL("DEFAULT 0.00")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'merchant_task_third_auth'

class MerchantTaskThirdVerify(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    task_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'merchant_task_third_verify'
        indexes = (
            (('mall_id', 'task_id'), True),
        )

class Operater(BaseModel):
    code = CharField(constraints=[SQL("DEFAULT ''")], unique=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    user_id = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'operater'

class OrderQuickReply(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    mall_id = IntegerField()
    reply_text = CharField(constraints=[SQL("DEFAULT ''")])
    type = IntegerField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'order_quick_reply'
        indexes = (
            (('mall_id', 'type'), False),
        )

class PackageSubsidyDetail(BaseModel):
    amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    logistic_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    material_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    month = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    order_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], unique=True)
    pay_success_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], index=True)
    reason = CharField(constraints=[SQL("DEFAULT ''")])
    reject_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    subsidy_status = IntegerField(constraints=[SQL("DEFAULT 1")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'package_subsidy_detail'
        indexes = (
            (('mall_id', 'goods_id'), False),
        )

class PackageSubsidyRecord(BaseModel):
    amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    amount_arrive = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    id = BigAutoField()
    is_modify = IntegerField(constraints=[SQL("DEFAULT 0")])
    mall_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    month = CharField(constraints=[SQL("DEFAULT ''")])
    operator_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    order_num = IntegerField(constraints=[SQL("DEFAULT 0")])
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    rule = TextField(null=True)
    subsidy_order_num = IntegerField(constraints=[SQL("DEFAULT 0")])
    subsidy_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    violation_info = TextField(null=True)

    class Meta:
        table_name = 'package_subsidy_record'
        indexes = (
            (('mall_id', 'month'), True),
        )

class PropertyData(BaseModel):
    entity_type = CharField()
    name = CharField()
    staple_ids = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'property_data'

class QqGroup(BaseModel):
    available_qty = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    qq = CharField(constraints=[SQL("DEFAULT ''")])
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    staple_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    type = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'qq_group'

class Recharge(BaseModel):
    amount = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    arrive_amount = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    desc = TextField(null=True)
    id = BigAutoField()
    mall_id = BigIntegerField()
    out_trade_no = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    pay_desc = TextField(null=True)
    pay_source = IntegerField(constraints=[SQL("DEFAULT 0")])
    pay_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    pay_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    pay_trade_no = CharField(constraints=[SQL("DEFAULT '0'")])
    pay_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'recharge'
        indexes = (
            (('mall_id', 'pay_type'), False),
        )

class RefundAddress(BaseModel):
    city_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    city_name = CharField(constraints=[SQL("DEFAULT ''")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    district_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    district_name = CharField(constraints=[SQL("DEFAULT ''")])
    is_default = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    mall_id = BigIntegerField(index=True)
    province_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    province_name = CharField(constraints=[SQL("DEFAULT ''")])
    refund_address = CharField(constraints=[SQL("DEFAULT ''")])
    refund_mobile = CharField(constraints=[SQL("DEFAULT ''")])
    refund_name = CharField(constraints=[SQL("DEFAULT ''")])
    refund_phone = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'refund_address'

class Region(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    is_enabled = IntegerField()
    national_code = CharField(constraints=[SQL("DEFAULT ''")])
    parent_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    postcode = CharField(constraints=[SQL("DEFAULT ''")])
    region_name = CharField(constraints=[SQL("DEFAULT ''")])
    region_type = IntegerField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'region'

class RegionSp(BaseModel):
    national_code = CharField(constraints=[SQL("DEFAULT ''")])
    region_name = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'region_sp'

class RegionTencent(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    national_code = CharField()
    tencent_code = CharField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'region_tencent'

class Role(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    description = CharField(constraints=[SQL("DEFAULT ''")])
    display_name = CharField()
    name = CharField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'role'

class Seller(BaseModel):
    avatar = CharField(constraints=[SQL("DEFAULT ''")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_mobile_verification = IntegerField(constraints=[SQL("DEFAULT 0")])
    mobile = CharField(unique=True)
    nickname = CharField(constraints=[SQL("DEFAULT ''")])
    password = CharField()
    password_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    username = CharField(null=True, unique=True)

    class Meta:
        table_name = 'seller'

class SellerIllegalWord(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    illegal_word = TextField()
    mall_id = BigIntegerField(index=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'seller_illegal_word'

class SellerMall(BaseModel):
    config = TextField(null=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    cs_default = IntegerField(constraints=[SQL("DEFAULT 0")])
    cs_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    cs_weight = IntegerField(constraints=[SQL("DEFAULT 6")])
    im_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_owner = IntegerField(constraints=[SQL("DEFAULT 0")])
    mall_id = BigIntegerField(index=True)
    role_ids = CharField(constraints=[SQL("DEFAULT ''")])
    seller_id = IntegerField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'seller_mall'
        indexes = (
            (('seller_id', 'is_owner'), False),
        )

class SellerMallRole(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    role_id = IntegerField()
    seller_mall_id = IntegerField(index=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'seller_mall_role'

class SellerRetreat(BaseModel):
    avatar = CharField(constraints=[SQL("DEFAULT ''")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_mobile_verification = IntegerField(constraints=[SQL("DEFAULT 0")])
    mobile = CharField()
    nickname = CharField(constraints=[SQL("DEFAULT ''")])
    password = CharField()
    password_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    retreat_reason = CharField(constraints=[SQL("DEFAULT ''")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    username = CharField(null=True)

    class Meta:
        table_name = 'seller_retreat'

class ShopGroupOrder(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    import_alipay = TextField(null=True)
    import_purchase = TextField(null=True)
    incoming_outgoing = IntegerField(constraints=[SQL("DEFAULT 0")])
    order_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    pay_amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    platform = CharField(constraints=[SQL("DEFAULT ''")])
    purchase_amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    third_order_id = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    third_refund_amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'shop_group_order'

class StapleBd(BaseModel):
    code = CharField(constraints=[SQL("DEFAULT ''")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    include_cat = CharField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    owner_bd = CharField()
    qq = CharField(constraints=[SQL("DEFAULT ''")])
    qq_group = CharField(constraints=[SQL("DEFAULT ''")])
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    staple_cat_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    staple_name = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'staple_bd'

class StapleCategoryData(BaseModel):
    exclude_category_ids = CharField(constraints=[SQL("DEFAULT ''")])
    include_category_ids = CharField(constraints=[SQL("DEFAULT ''")])
    name = CharField()

    class Meta:
        table_name = 'staple_category_data'

class WithdrawReport(BaseModel):
    account_id = IntegerField()
    amount = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    desc = TextField(null=True)
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    service_fee = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    type = IntegerField(constraints=[SQL("DEFAULT 1")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'withdraw_report'

