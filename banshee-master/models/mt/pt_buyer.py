from peewee import *

database = MySQLDatabase('pt_buyer', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': 'rm-uf6pec9k82nsk59o8.mysql.rds.aliyuncs.com', 'port': 3306, 'user': 'root', 'password': 'cFsc34^8pVm'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class AppleAuth(BaseModel):
    authorization_code = CharField(constraints=[SQL("DEFAULT ''")])
    buyer_id = BigIntegerField(unique=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    email = CharField(constraints=[SQL("DEFAULT ''")])
    identity_token = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    member_id = CharField(constraints=[SQL("DEFAULT ''")], unique=True)
    nickname = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'apple_auth'

class AuditCoinSummary(BaseModel):
    buyer_id = BigIntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    date = CharField()
    details = TextField()
    id = BigAutoField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'audit_coin_summary'
        indexes = (
            (('buyer_id', 'date'), True),
        )

class AuditCoinSummaryBuffer(BaseModel):
    buyer_id = BigIntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    date = CharField()
    details = TextField()
    id = BigAutoField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'audit_coin_summary_buffer'
        indexes = (
            (('buyer_id', 'date'), True),
        )

class AuditCoinSummaryMap(BaseModel):
    action_types = CharField()
    description = CharField(null=True)
    field = CharField(unique=True)
    label = CharField()
    rank = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'audit_coin_summary_map'

class AuditCoinSummaryOplog(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    id = BigAutoField()
    op_id = BigIntegerField()
    op_type = IntegerField(unique=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'audit_coin_summary_oplog'

class Buyer(BaseModel):
    avatar = CharField(constraints=[SQL("DEFAULT ''")])
    birthday = DateField(null=True)
    city_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    country_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    district_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    ip = CharField(constraints=[SQL("DEFAULT ''")])
    is_cancel = IntegerField(constraints=[SQL("DEFAULT 0")])
    mobile = CharField(null=True, unique=True)
    nickname = CharField(constraints=[SQL("DEFAULT ''")])
    password = CharField(constraints=[SQL("DEFAULT ''")])
    province_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    sex = IntegerField(constraints=[SQL("DEFAULT 0")])
    sign = CharField(constraints=[SQL("DEFAULT ''")])
    source = IntegerField(constraints=[SQL("DEFAULT 0")])
    tags = TextField(null=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'buyer'

class BuyerAddr(BaseModel):
    address = CharField(null=True)
    address_id = BigAutoField()
    buyer_id = BigIntegerField()
    city_id = IntegerField()
    country_id = IntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    district_id = IntegerField()
    is_default = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    mobile = CharField()
    name = CharField()
    province_id = IntegerField()
    tag = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'buyer_addr'
        indexes = (
            (('buyer_id', 'address_id'), False),
        )

class BuyerMparkPack(BaseModel):
    buyer_id = BigIntegerField()
    chip_id = CharField(constraints=[SQL("DEFAULT ''")])
    config = TextField(null=True)
    count = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    item_id = CharField(constraints=[SQL("DEFAULT ''")])
    title = CharField(constraints=[SQL("DEFAULT ''")])
    trade_num = IntegerField(constraints=[SQL("DEFAULT 0")])
    type = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'buyer_mpark_pack'
        indexes = (
            (('buyer_id', 'item_id', 'type'), True),
        )

class BuyerRealName(BaseModel):
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True, null=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    id_card = CharField(constraints=[SQL("DEFAULT ''")], null=True)
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_hide = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_verified = IntegerField(constraints=[SQL("DEFAULT 0")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'buyer_real_name'

class BuyerStatistics(BaseModel):
    buyer_id = BigIntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    type = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    value = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'buyer_statistics'
        indexes = (
            (('buyer_id', 'type'), True),
        )

class BuyerTags(BaseModel):
    buyer_id = BigIntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    id = BigAutoField()
    tag = CharField()

    class Meta:
        table_name = 'buyer_tags'
        indexes = (
            (('buyer_id', 'tag'), True),
        )

class CancelBuyer(BaseModel):
    avatar = CharField(constraints=[SQL("DEFAULT ''")])
    buyer_id = BigIntegerField(unique=True)
    cancel_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    city_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    country_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    district_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    is_recover = IntegerField(constraints=[SQL("DEFAULT 0")])
    mobile = CharField(null=True, unique=True)
    nickname = CharField(constraints=[SQL("DEFAULT ''")])
    operator_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    province_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    recover_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    register_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    sex = IntegerField(constraints=[SQL("DEFAULT 0")])
    source = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'cancel_buyer'

class CommonAuth(BaseModel):
    app_id = CharField(constraints=[SQL("DEFAULT ''")])
    avatar = CharField(constraints=[SQL("DEFAULT ''")])
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT -1")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    id = BigAutoField()
    ip = CharField(constraints=[SQL("DEFAULT ''")])
    mobile = CharField(constraints=[SQL("DEFAULT ''")])
    nickname = CharField(constraints=[SQL("DEFAULT ''")])
    open_id = CharField(constraints=[SQL("DEFAULT ''")])
    platform = IntegerField(constraints=[SQL("DEFAULT -1")])
    sex = IntegerField(constraints=[SQL("DEFAULT 0")])
    source = CharField(constraints=[SQL("DEFAULT ''")])
    union_id = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'common_auth'
        indexes = (
            (('buyer_id', 'app_id'), True),
            (('mobile', 'app_id'), True),
            (('open_id', 'app_id'), True),
        )

class GoodsEvaluateBlacklist(BaseModel):
    buyer_id = BigIntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    goods_recommend_id = IntegerField()
    handler_id = IntegerField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'goods_evaluate_blacklist'

class GroupMessage(BaseModel):
    ae_uids = CharField(constraints=[SQL("DEFAULT ''")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    error = CharField(constraints=[SQL("DEFAULT ''")])
    media_id = IntegerField()
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    title = CharField(constraints=[SQL("DEFAULT ''")])
    type = CharField(null=True)
    type_value = TextField(null=True)

    class Meta:
        table_name = 'group_message'

class MiniappCustomMsg(BaseModel):
    content = TextField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    title = CharField(constraints=[SQL("DEFAULT ''")])
    type = CharField(null=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'miniapp_custom_msg'

class MiniappTplMsg(BaseModel):
    body = CharField(constraints=[SQL("DEFAULT ''")])
    data = CharField(constraints=[SQL("DEFAULT ''")])
    title = CharField(constraints=[SQL("DEFAULT ''")])
    tpl_id = CharField(constraints=[SQL("DEFAULT ''")])
    url = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'miniapp_tpl_msg'

class QttAuth(BaseModel):
    access_token = CharField(null=True)
    biz = TextField(null=True)
    buyer_id = BigIntegerField(index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    id = BigAutoField()
    memberid = CharField(unique=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'qtt_auth'

class Robot(BaseModel):
    avatar = CharField(constraints=[SQL("DEFAULT ''")])
    birthday = DateField(null=True)
    city_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    country_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    district_id = IntegerField()
    id = BigAutoField()
    mobile = CharField(null=True)
    nickname = CharField(constraints=[SQL("DEFAULT ''")])
    password = CharField(constraints=[SQL("DEFAULT ''")])
    province_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    sex = IntegerField(constraints=[SQL("DEFAULT 0")])
    sign = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'robot'

class RobotAddr(BaseModel):
    address = CharField(constraints=[SQL("DEFAULT ''")])
    address_id = BigAutoField()
    city_id = IntegerField()
    country_id = IntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    district_id = IntegerField()
    is_default = IntegerField(constraints=[SQL("DEFAULT 0")])
    mobile = CharField()
    name = CharField()
    province_id = IntegerField()
    robot_id = BigIntegerField(index=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'robot_addr'

class SrSuggest(BaseModel):
    answer = TextField(null=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    is_commit = IntegerField(constraints=[SQL("DEFAULT 0")])
    schedule = IntegerField(constraints=[SQL("DEFAULT 0")])
    source = IntegerField(constraints=[SQL("DEFAULT 0")])
    uid = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'sr_suggest'

class Suggestion(BaseModel):
    app_version = CharField(constraints=[SQL("DEFAULT ''")])
    biz = TextField()
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    clue1 = CharField(constraints=[SQL("DEFAULT ''")])
    clue2 = CharField(constraints=[SQL("DEFAULT ''")])
    clue3 = CharField(constraints=[SQL("DEFAULT ''")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    mobile = CharField(constraints=[SQL("DEFAULT ''")])
    platform = IntegerField(constraints=[SQL("DEFAULT -1")])
    ref = CharField(constraints=[SQL("DEFAULT 'no_ref'")], index=True)
    ref_kind = CharField(constraints=[SQL("DEFAULT ''")])
    remark_img = CharField(constraints=[SQL("DEFAULT ''")])
    suggestion = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'suggestion'

class Test(BaseModel):
    nickname = CharField(null=True)

    class Meta:
        table_name = 'test'

class ThirdpartyAuth(BaseModel):
    biz = TextField(null=True)
    buyer_id = BigIntegerField(index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    id = BigAutoField()
    oauth_access_token = CharField(null=True)
    oauth_expire_in = IntegerField(null=True)
    oauth_refresh_token = CharField(null=True)
    thirdparty_id = IntegerField()
    thirdparty_uid = CharField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'thirdparty_auth'
        indexes = (
            (('thirdparty_id', 'thirdparty_uid'), True),
        )

class UserMessageStat(BaseModel):
    buyer_id = BigIntegerField()
    month = CharField()
    msg_ids = CharField(constraints=[SQL("DEFAULT ''")])
    send_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'user_message_stat'
        indexes = (
            (('month', 'buyer_id'), True),
        )

class WeappCustomMsg(BaseModel):
    content = TextField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    title = CharField(constraints=[SQL("DEFAULT ''")])
    type = CharField(null=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'weapp_custom_msg'

class WeappTplMsg(BaseModel):
    body = CharField(constraints=[SQL("DEFAULT ''")])
    data = CharField(constraints=[SQL("DEFAULT ''")])
    title = CharField(constraints=[SQL("DEFAULT ''")])
    tpl_id = CharField(constraints=[SQL("DEFAULT ''")])
    url = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'weapp_tpl_msg'

class WechatAuth(BaseModel):
    app_type = IntegerField()
    appid = CharField()
    biz = TextField(null=True)
    buyer_id = BigIntegerField(index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    id = BigAutoField()
    is_subscribed = IntegerField(constraints=[SQL("DEFAULT 0")])
    oauth_access_token = CharField(null=True)
    oauth_expire_in = IntegerField(null=True)
    oauth_refresh_token = CharField(null=True)
    openid = CharField(unique=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'wechat_auth'

class WechatAuthUnionid(BaseModel):
    buyer_id = BigAutoField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    unionid = CharField(unique=True)

    class Meta:
        table_name = 'wechat_auth_unionid'

class WxCustomMsg(BaseModel):
    content = TextField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    title = CharField(constraints=[SQL("DEFAULT ''")])
    type = CharField(null=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'wx_custom_msg'

class WxMedia(BaseModel):
    content = TextField(null=True)
    image_url = CharField(constraints=[SQL("DEFAULT ''")])
    media_id = CharField(unique=True)
    name = CharField(constraints=[SQL("DEFAULT ''")])
    type = CharField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    url = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'wx_media'

class WxTplMsg(BaseModel):
    body = CharField(constraints=[SQL("DEFAULT ''")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    create_by = IntegerField(constraints=[SQL("DEFAULT 0")])
    creator_name = CharField(constraints=[SQL("DEFAULT ''")])
    data = TextField(null=True)
    miniprogram_url = CharField(constraints=[SQL("DEFAULT ''")])
    title = CharField(constraints=[SQL("DEFAULT ''")])
    tpl_id = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    url = CharField(constraints=[SQL("DEFAULT ''")])
    wx_tpl_title = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'wx_tpl_msg'

