from peewee import *

database = MySQLDatabase('pt_activity', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': 'rm-uf6pec9k82nsk59o8.mysql.rds.aliyuncs.com', 'port': 3306, 'user': 'qa_rw_user', 'password': '8QoK6AjTvSMqs35lm4fwLuyPke0F'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class ActRule(BaseModel):
    act_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    is_default = IntegerField(constraints=[SQL("DEFAULT 0")])
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    rule = TextField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'act_rule'

class Activity(BaseModel):
    act_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    banner = CharField(constraints=[SQL("DEFAULT ''")])
    brand_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    category_id = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    coin_discount = IntegerField(constraints=[SQL("DEFAULT 1")])
    config = TextField(null=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    end_time = DateTimeField(index=True, null=True)
    goods_source = IntegerField(constraints=[SQL("DEFAULT 1")])
    goods_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    group_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    index_show = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    layout = IntegerField(constraints=[SQL("DEFAULT 1")])
    lock_end_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    lock_start_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    mt_category_id = TextField(null=True)
    name = CharField(constraints=[SQL("DEFAULT ''")])
    rank = IntegerField(constraints=[SQL("DEFAULT 0")])
    remark = TextField(null=True)
    sort_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    start_time = DateTimeField(index=True, null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    system_discount = IntegerField(constraints=[SQL("DEFAULT 1")])
    title = CharField(constraints=[SQL("DEFAULT ''")])
    type = IntegerField(constraints=[SQL("DEFAULT 0")])
    unique_code = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(null=True)
    user_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    watermarker = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'activity'

class ActivityAlarm(BaseModel):
    activity_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_used = IntegerField(constraints=[SQL("DEFAULT 0")])
    notify_emails = CharField(constraints=[SQL("DEFAULT ''")])
    relation_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'activity_alarm'

class ActivityApply(BaseModel):
    act_intro = TextField()
    act_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    apply_time_text = CharField(constraints=[SQL("DEFAULT ''")])
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    summary = CharField(constraints=[SQL("DEFAULT ''")])
    thumb = CharField(constraints=[SQL("DEFAULT ''")])
    title = CharField(constraints=[SQL("DEFAULT ''")])
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'activity_apply'

class ActivityBaoxiang(BaseModel):
    action_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    coupons = TextField(null=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    expire_at = DateTimeField(null=True)
    get_amount = IntegerField()
    open_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    period_id = IntegerField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    uid = BigIntegerField(unique=True)

    class Meta:
        table_name = 'activity_baoxiang'

class ActivityBargain(BaseModel):
    activity_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    bargain_coupon_num = IntegerField(constraints=[SQL("DEFAULT 1")])
    bargain_coupons = TextField()
    bargain_step = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    end_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    goods_id = BigIntegerField(index=True)
    help_bargain_coupon_num = IntegerField(constraints=[SQL("DEFAULT 1")])
    help_bargain_coupons = TextField()
    lowest_price = IntegerField(constraints=[SQL("DEFAULT 0")])
    start_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    stock_warn_num = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    weight = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'activity_bargain'

class ActivityBargainHelp(BaseModel):
    activity_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    bargain_price = IntegerField(constraints=[SQL("DEFAULT 0")])
    bargain_rec_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    current_price = IntegerField()
    goods_id = BigIntegerField()
    owner_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'activity_bargain_help'

class ActivityBargainRecord(BaseModel):
    activity_bargain_id = IntegerField()
    activity_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    bargain_step = IntegerField()
    buyer_id = BigIntegerField(index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    fail_msg = CharField(constraints=[SQL("DEFAULT ''")])
    goods_id = BigIntegerField(index=True)
    lowest_price = IntegerField()
    order_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    pay_price = IntegerField(constraints=[SQL("DEFAULT 0")])
    remain_step = IntegerField(constraints=[SQL("DEFAULT 0")])
    sku_id = BigIntegerField()
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    succ_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'activity_bargain_record'

class ActivityCashReward(BaseModel):
    audit_second = IntegerField()
    coupon_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    daily_reward_limit = IntegerField()
    handler_id = IntegerField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    rule_type = IntegerField()
    sprint_status = IntegerField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    title = CharField(constraints=[SQL("DEFAULT ''")])
    type = IntegerField(constraints=[SQL("DEFAULT 1")])
    unique_code = CharField(constraints=[SQL("DEFAULT ''")], unique=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'activity_cash_reward'

class ActivityCashRewardRule(BaseModel):
    activity_cash_reward_id = IntegerField(index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    first_order_rate = IntegerField(constraints=[SQL("DEFAULT 0")])
    handler_id = IntegerField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    reward_amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    reward_amount_max = IntegerField()
    reward_rate = IntegerField()
    type = IntegerField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'activity_cash_reward_rule'

class ActivityCashgift(BaseModel):
    action_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    config_name = CharField(constraints=[SQL("DEFAULT 'plana'")])
    coupons = TextField(null=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    expire_at = DateTimeField(null=True)
    get_amount = IntegerField()
    period_id = IntegerField(constraints=[SQL("DEFAULT 1")])
    source_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    total_amount = IntegerField()
    uid = BigIntegerField()

    class Meta:
        table_name = 'activity_cashgift'
        indexes = (
            (('uid', 'period_id'), True),
        )

class ActivityCoinReward(BaseModel):
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    idx = IntegerField(constraints=[SQL("DEFAULT 1")])
    order_id = BigIntegerField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'activity_coin_reward'
        indexes = (
            (('buyer_id', 'order_id'), True),
        )

class ActivityCouponNew(BaseModel):
    config_version = IntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    uid = BigIntegerField(unique=True)
    user_coupon_ids = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'activity_coupon_new'

class ActivityEvaluate(BaseModel):
    apply_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    id = BigAutoField()
    order_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    recommend_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    use_card = IntegerField(constraints=[SQL("DEFAULT 0")])
    user_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    weight_count = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'activity_evaluate'

class ActivityEvaluateCardDetail(BaseModel):
    change_num = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    reason = IntegerField(constraints=[SQL("DEFAULT 0")])
    uid = BigIntegerField(index=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'activity_evaluate_card_detail'

class ActivityEvaluateCardTotal(BaseModel):
    card_total = IntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    uid = BigIntegerField(unique=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'activity_evaluate_card_total'

class ActivityEvaluateUserLiked(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    like_user_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    publish_user_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    recommend_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'activity_evaluate_user_liked'
        indexes = (
            (('recommend_id', 'like_user_id'), False),
        )

class ActivityGoods(BaseModel):
    activity_group_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    activity_id = IntegerField(index=True)
    config = TextField(null=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    goods_id = IntegerField(index=True)
    in_brick = IntegerField(constraints=[SQL("DEFAULT 0")])
    lock_end_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    lock_start_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    mall_id = IntegerField()
    rank = IntegerField(constraints=[SQL("DEFAULT 0")])
    rank_b = IntegerField(constraints=[SQL("DEFAULT 0")])
    rank_c = IntegerField(constraints=[SQL("DEFAULT 0")])
    schedule_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    score = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    tab_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'activity_goods'

class ActivityGoodsCloseAlarm(BaseModel):
    activity_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    alarm_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'activity_goods_close_alarm'

class ActivityGoodsEvaluation(BaseModel):
    activity_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    cat_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    end_time = DateTimeField(null=True)
    ext_goods_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    goods_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    mall_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    max_normal_price = IntegerField(constraints=[SQL("DEFAULT 0")])
    member_privilege = IntegerField(constraints=[SQL("DEFAULT 0")])
    min_normal_price = IntegerField(constraints=[SQL("DEFAULT 0")])
    rank = IntegerField(constraints=[SQL("DEFAULT 0")])
    schedule_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    start_time = DateTimeField(null=True)
    tab_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'activity_goods_evaluation'

class ActivityGoodsQuery(BaseModel):
    act_apply_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    act_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    activity_goods_is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    activity_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    activity_is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    activity_name = CharField(constraints=[SQL("DEFAULT ''")])
    activity_status = IntegerField(constraints=[SQL("DEFAULT 1")])
    add_at = DateTimeField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    extension_goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    goods_name = CharField(constraints=[SQL("DEFAULT ''")])
    group_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    is_onsale = IntegerField(constraints=[SQL("DEFAULT 1")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    old_schedule_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    old_schedule_name = CharField(constraints=[SQL("DEFAULT ''")])
    operator_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    operator_name = CharField(constraints=[SQL("DEFAULT ''")])
    pk_id = CharField()
    reason = TextField()
    schedule_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    schedule_name = CharField(constraints=[SQL("DEFAULT ''")])
    series_id = CharField(constraints=[SQL("DEFAULT ''")])
    source = IntegerField(constraints=[SQL("DEFAULT 0")])
    thumb_url = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'activity_goods_query'

class ActivityGoodsReview(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    extra = TextField(null=True)
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], unique=True)
    refs = TextField(null=True)
    skus = TextField(null=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'activity_goods_review'

class ActivityGoodsTabRelation(BaseModel):
    activity_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    auto = IntegerField(constraints=[SQL("DEFAULT 1")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    goods_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    lock_end_time = DateTimeField(constraints=[SQL("DEFAULT 1970-01-01 08:00:00")])
    lock_start_time = DateTimeField(constraints=[SQL("DEFAULT 1970-01-01 08:00:00")])
    mall_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    rank = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    tab_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'activity_goods_tab_relation'

class ActivityGroup(BaseModel):
    activity_name = CharField(constraints=[SQL("DEFAULT ''")])
    activity_step = IntegerField(constraints=[SQL("DEFAULT 1")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    creator_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    creator_name = CharField()
    end_time = DateTimeField(index=True, null=True)
    extra = CharField(constraints=[SQL("DEFAULT ''")])
    handler_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    remark = TextField()
    schedule_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    schedule_name = CharField(constraints=[SQL("DEFAULT ''")])
    sort_strategy = IntegerField(constraints=[SQL("DEFAULT 0")])
    sort_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    start_time = DateTimeField(index=True, null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    type = IntegerField(constraints=[SQL("DEFAULT 1")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'activity_group'

class ActivityHelpFree(BaseModel):
    address = TextField(null=True)
    award_limit = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    end_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    goods_id = IntegerField()
    group_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    group_limit = IntegerField(constraints=[SQL("DEFAULT 0")])
    init_succ_group_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    period = IntegerField(constraints=[SQL("DEFAULT 86400")])
    slogon = CharField(constraints=[SQL("DEFAULT ''")])
    start_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    succ_group_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    user_limit = IntegerField(constraints=[SQL("DEFAULT 0")])
    weight = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'activity_help_free'

class ActivityJackpotOrders(BaseModel):
    buyer_id = BigIntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    is_refund = IntegerField(constraints=[SQL("DEFAULT 0")])
    order_create_at = DateTimeField(index=True)
    order_id = BigIntegerField()
    payment_total = IntegerField(constraints=[SQL("DEFAULT 0")])
    period_id = BigIntegerField(index=True)
    rewarded = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'activity_jackpot_orders'
        indexes = (
            (('buyer_id', 'order_id'), True),
        )

class ActivityJackpotPeriod(BaseModel):
    begin_ts = BigIntegerField(unique=True)
    conf = TextField(null=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    description = CharField()
    end_ts = BigIntegerField()
    fake_total_coin = BigIntegerField()
    id = BigAutoField()
    lottery_at = DateTimeField()
    qualified_buyer_order_cnt = IntegerField()
    total_buyer = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    total_coin = BigIntegerField()
    total_gmv = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    total_reward_buyer = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    total_reward_gmv = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'activity_jackpot_period'

class ActivityJackpotPrize(BaseModel):
    buyer_id = BigIntegerField()
    cal_factor = TextField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    order_cnt = IntegerField()
    period_id = BigIntegerField(index=True)
    prize = IntegerField()
    prize_date = CharField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'activity_jackpot_prize'
        indexes = (
            (('buyer_id', 'period_id'), True),
        )

class ActivityJackpotSignup(BaseModel):
    buyer_id = BigIntegerField(unique=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    reward_factor = IntegerField(constraints=[SQL("DEFAULT 100")])

    class Meta:
        table_name = 'activity_jackpot_signup'

class ActivityJackpotUser(BaseModel):
    buyer_id = BigIntegerField(unique=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    reward_factor = IntegerField(constraints=[SQL("DEFAULT 100")])
    sign_up_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'activity_jackpot_user'

class ActivityLego(BaseModel):
    activity_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    activity_name = CharField(constraints=[SQL("DEFAULT ''")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    operator_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    schedule_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    source_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'activity_lego'

class ActivityMparkLotteryAudit(BaseModel):
    action_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    buyer_id = BigIntegerField(index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    id = BigAutoField()
    incr = IntegerField()
    msg_id = CharField(unique=True)

    class Meta:
        table_name = 'activity_mpark_lottery_audit'

class ActivityMparkPet(BaseModel):
    buyer_id = BigIntegerField(unique=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    current_exp = IntegerField(constraints=[SQL("DEFAULT 0")])
    honey_pot = IntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    inviter = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    last_feed_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    level = CharField(constraints=[SQL("DEFAULT '0'")])
    lottery_cnt = IntegerField(constraints=[SQL("DEFAULT 0")])
    source = IntegerField(constraints=[SQL("DEFAULT 0")])
    total_exp = IntegerField(constraints=[SQL("DEFAULT 0")])
    total_lottery_cnt = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    upgrade_exp = IntegerField()

    class Meta:
        table_name = 'activity_mpark_pet'

class ActivityMparkPotAudit(BaseModel):
    action_type = IntegerField()
    buyer_id = BigIntegerField(index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    id = BigAutoField()
    incr_exp = IntegerField()
    incr_pot = IntegerField()
    msg_id = CharField(unique=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'activity_mpark_pot_audit'

class ActivityMparkTimeLine(BaseModel):
    action_type = IntegerField()
    buyer_id = BigIntegerField(index=True)
    content = CharField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    friend_id = BigIntegerField()
    id = BigAutoField()

    class Meta:
        table_name = 'activity_mpark_time_line'

class ActivityPokerLotteryGame(BaseModel):
    buyer_id = BigIntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    expire_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    goods_id = BigIntegerField(null=True)
    goods_name = CharField(constraints=[SQL("DEFAULT ''")])
    id = BigAutoField()
    reborncard_quota = IntegerField(constraints=[SQL("DEFAULT 2")])
    round_info = TextField()
    round_poker = IntegerField(constraints=[SQL("DEFAULT 0")])
    round_result = IntegerField(constraints=[SQL("DEFAULT 0")])
    start_coin = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    thumb_url = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'activity_poker_lottery_game'
        indexes = (
            (('buyer_id', 'create_at'), False),
        )

class ActivityPokerLotteryReward(BaseModel):
    activate_expire_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    audit_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    buyer_id = BigIntegerField()
    coin_num = IntegerField(constraints=[SQL("DEFAULT 0")])
    coupon_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    coupon_msg = CharField(constraints=[SQL("DEFAULT ''")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    game_id = BigIntegerField(index=True)
    goods_id = BigIntegerField(index=True)
    id = BigAutoField()
    round = IntegerField()
    thumb_url = CharField(constraints=[SQL("DEFAULT ''")])
    type = IntegerField(constraints=[SQL("DEFAULT 1")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    user_coupon_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'activity_poker_lottery_reward'
        indexes = (
            (('buyer_id', 'id'), False),
        )

class ActivityPredict(BaseModel):
    activity_id = IntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    name_space = CharField(unique=True)
    predict_result = TextField()
    sort_desc = CharField()
    sort_param = CharField(constraints=[SQL("DEFAULT ''")])
    sort_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    tab_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'activity_predict'

class ActivityRef(BaseModel):
    activity_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    ref_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    ref_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'activity_ref'
        indexes = (
            (('activity_id', 'ref_id'), False),
        )

class ActivityReservation(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    goods_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    staging_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    uid = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'activity_reservation'
        indexes = (
            (('staging_id', 'uid'), True),
        )

class ActivityReservationStaging(BaseModel):
    activity_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    config = TextField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    creator_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    end_time = IntegerField(constraints=[SQL("DEFAULT 0")])
    last_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    lottery_end_time = IntegerField(constraints=[SQL("DEFAULT 0")])
    lottery_start_time = IntegerField(constraints=[SQL("DEFAULT 0")])
    round = IntegerField(constraints=[SQL("DEFAULT 1")])
    start_time = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    ticket_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    title = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'activity_reservation_staging'
        indexes = (
            (('activity_id', 'round'), False),
        )

class ActivityScene(BaseModel):
    activity_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    bak_msg_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    beauty_qrcode = CharField(constraints=[SQL("DEFAULT ''")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    expire_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    is_send = IntegerField(constraints=[SQL("DEFAULT 0")])
    msg_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    qrcode = CharField(constraints=[SQL("DEFAULT ''")])
    qrcode_type = IntegerField(constraints=[SQL("DEFAULT 1")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    valid_days = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'activity_scene'

class ActivitySchedule(BaseModel):
    act_end_time = DateField(constraints=[SQL("DEFAULT 0000-00-00")])
    act_intro = TextField()
    act_start_time = DateField(constraints=[SQL("DEFAULT 0000-00-00")])
    act_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    activity_apply_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    apply_end_time = DateField(constraints=[SQL("DEFAULT 0000-00-00")])
    apply_num_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    apply_start_time = DateField(constraints=[SQL("DEFAULT 0000-00-00")])
    apply_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    config = TextField(null=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    max_goods_apply_qty = IntegerField(constraints=[SQL("DEFAULT 0")])
    price_range = CharField(constraints=[SQL("DEFAULT ''")])
    sales_claim = CharField(constraints=[SQL("DEFAULT ''")])
    special_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    summary = CharField(constraints=[SQL("DEFAULT ''")])
    thumb = CharField(constraints=[SQL("DEFAULT ''")])
    title = CharField(constraints=[SQL("DEFAULT ''")])
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'activity_schedule'

class ActivityScheduleGoods(BaseModel):
    act_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    activity_schedule_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    biz = TextField(null=True)
    brand_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    brand_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_1 = IntegerField(constraints=[SQL("DEFAULT 0")])
    config = TextField(null=True)
    create_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    ext_goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    goods_name = CharField(constraints=[SQL("DEFAULT ''")])
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    min_normal_price = IntegerField(constraints=[SQL("DEFAULT 0")])
    reason = TextField(null=True)
    series_id = CharField(constraints=[SQL("DEFAULT ''")])
    skus = TextField()
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    thumb_url = CharField(constraints=[SQL("DEFAULT ''")])
    update_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'activity_schedule_goods'

class ActivityScheduleMallType(BaseModel):
    activity_schedule_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    mall_type = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'activity_schedule_mall_type'
        indexes = (
            (('activity_schedule_id', 'mall_type'), True),
        )

class ActivityScheduleStaple(BaseModel):
    activity_schedule_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    staple_id = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'activity_schedule_staple'
        indexes = (
            (('activity_schedule_id', 'staple_id'), True),
        )

class ActivitySeckillHelp(BaseModel):
    boost_cnt = IntegerField(constraints=[SQL("DEFAULT 0")])
    buyer_id = BigIntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    end_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    goods_id = BigIntegerField(index=True)
    id = BigAutoField()
    nick_name = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    qualified_cnt = CharField(constraints=[SQL("DEFAULT '0'")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    wx_id = CharField(constraints=[SQL("DEFAULT ''")], index=True)

    class Meta:
        table_name = 'activity_seckill_help'
        indexes = (
            (('buyer_id', 'goods_id'), True),
        )

class ActivitySeckillHelpAudit(BaseModel):
    buyer_id = BigIntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    help_id = BigIntegerField()
    id = BigAutoField()

    class Meta:
        table_name = 'activity_seckill_help_audit'
        indexes = (
            (('help_id', 'buyer_id'), True),
        )

class ActivitySeckillHelpAuditV2(BaseModel):
    avatar = CharField(constraints=[SQL("DEFAULT ''")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    help_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    nick_name = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    wx_id = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'activity_seckill_help_audit_v2'
        indexes = (
            (('help_id', 'wx_id'), True),
        )

class ActivitySeckillScoreStream(BaseModel):
    buyer_id = BigIntegerField(index=True, null=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    message_id = CharField(unique=True)
    score = IntegerField()
    type = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'activity_seckill_score_stream'

class ActivitySeckillUserScore(BaseModel):
    buyer_id = BigIntegerField(unique=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    last_message_id = BigIntegerField(null=True)
    score = IntegerField(null=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'activity_seckill_user_score'

class ActivityTab(BaseModel):
    activity_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_ids = CharField(constraints=[SQL("DEFAULT ''")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    end_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    icon = CharField(constraints=[SQL("DEFAULT ''")])
    id = BigAutoField()
    name = CharField(constraints=[SQL("DEFAULT ''")])
    sort = IntegerField(constraints=[SQL("DEFAULT 0")])
    sort_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    start_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    use_algorithm = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'activity_tab'
        indexes = (
            (('activity_id', 'name'), True),
        )

class ActivityTreasureBuyerPeriod(BaseModel):
    begin_ts = BigIntegerField()
    buyer_id = BigIntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    gmv = IntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    qualified_gmv = IntegerField(constraints=[SQL("DEFAULT 0")])
    refunded_gmv = IntegerField(constraints=[SQL("DEFAULT 0")])
    reward_coin = IntegerField()
    signed_gmv = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'activity_treasure_buyer_period'
        indexes = (
            (('buyer_id', 'begin_ts'), True),
        )

class ActivityTreasureOrders(BaseModel):
    buyer_id = BigIntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    is_refund = IntegerField(constraints=[SQL("DEFAULT 0")])
    order_create_at = DateTimeField()
    order_id = BigIntegerField(unique=True)
    payment_total = IntegerField(constraints=[SQL("DEFAULT 0")])
    period_id = BigIntegerField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'activity_treasure_orders'

class ActivityUserInvite(BaseModel):
    buyer_id_invite = BigIntegerField(index=True)
    buyer_id_join = BigIntegerField(index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    ip = CharField(null=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'activity_user_invite'

class AikucunCategoryMap(BaseModel):
    activity_ids = TextField(null=True)
    aikucun_category_ids = TextField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    mt_category = CharField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    weight = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'aikucun_category_map'

class AssistCoupon(BaseModel):
    conf = CharField(null=True)
    coupon_id = BigIntegerField(unique=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'assist_coupon'

class BaoxiangDetail(BaseModel):
    act_id = IntegerField()
    coupon_amount = IntegerField()
    coupon_id = BigIntegerField()
    coupon_index = IntegerField()
    coupon_name = CharField(constraints=[SQL("DEFAULT ''")])
    coupon_type = IntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    open_at = DateTimeField(null=True)
    pos_id = IntegerField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    uid = BigIntegerField(index=True)
    user_coupon_id = BigIntegerField()

    class Meta:
        table_name = 'baoxiang_detail'
        indexes = (
            (('act_id', 'coupon_index'), True),
            (('act_id', 'pos_id'), True),
        )

class BuyerValue(BaseModel):
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], unique=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    namespace = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    value = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'buyer_value'

class CashGiftWeapp(BaseModel):
    assist_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    coupon_amount = IntegerField()
    coupon_id = BigIntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    expire_ts = IntegerField()
    grant_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    need_assist_count = IntegerField()
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    uid = BigIntegerField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'cash_gift_weapp'
        indexes = (
            (('uid', 'status'), False),
        )

class CashGiftWeappDetail(BaseModel):
    assist_uid = BigIntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fetch_amount = IntegerField()
    record_id = IntegerField()
    remark = CharField()
    uid = BigIntegerField()

    class Meta:
        table_name = 'cash_gift_weapp_detail'
        indexes = (
            (('record_id', 'assist_uid', 'remark'), True),
        )

class CashgiftDetail(BaseModel):
    act_id = IntegerField()
    coupon_amount = IntegerField()
    coupon_id = BigIntegerField()
    coupon_index = IntegerField()
    coupon_type = IntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    uid = BigIntegerField(index=True)
    user_coupon_id = BigIntegerField()

    class Meta:
        table_name = 'cashgift_detail'
        indexes = (
            (('act_id', 'coupon_index'), True),
        )

class CheckinAuditMoney(BaseModel):
    base_incr = IntegerField()
    base_model_id = IntegerField()
    buyer_id = BigIntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    extra_incr = IntegerField(constraints=[SQL("DEFAULT 0")])
    extra_incr_id = BigIntegerField(index=True)
    id = BigAutoField()
    msg_id = CharField(unique=True)
    td = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    total_incr = IntegerField()
    type = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'checkin_audit_money'
        indexes = (
            (('buyer_id', 'id'), False),
        )

class CheckinBuyerMoney(BaseModel):
    buyer_id = BigIntegerField(unique=True)
    consecutive_times = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    deposit = IntegerField(constraints=[SQL("DEFAULT 0")])
    guide_times = IntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    interrupt_times = IntegerField(constraints=[SQL("DEFAULT 0")])
    last_checkin_at = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    last_checkin_period = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    program = IntegerField(constraints=[SQL("DEFAULT 0")])
    reveal_gift = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    withdraw_money = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'checkin_buyer_money'

class CheckinBuyerRewardPoint(BaseModel):
    buyer_id = BigIntegerField(unique=True)
    id = BigAutoField()
    last_points_period = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    order_count = IntegerField(constraints=[SQL("DEFAULT 1")])
    order_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    pending_reward_id = BigIntegerField()
    points = IntegerField(constraints=[SQL("DEFAULT 0")])
    score = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'checkin_buyer_reward_point'

class CheckinCash(BaseModel):
    amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    card_id = CharField(constraints=[SQL("DEFAULT ''")])
    card_name = CharField(constraints=[SQL("DEFAULT ''")])
    channel = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    reason = TextField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT -1")])
    td = IntegerField(constraints=[SQL("DEFAULT 0")])
    tuid = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'checkin_cash'

class CheckinCouponGoodsSales(BaseModel):
    coupon_id = BigIntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    generate_time = IntegerField()
    goods_id = BigIntegerField()
    quantity = IntegerField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'checkin_coupon_goods_sales'
        indexes = (
            (('coupon_id', 'generate_time'), False),
        )

class CheckinCpcRewards(BaseModel):
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    msg_id = CharField(constraints=[SQL("DEFAULT ''")], unique=True)
    reward_amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    reward_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    slot_id = CharField(constraints=[SQL("DEFAULT ''")])
    td = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    tuid = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'checkin_cpc_rewards'

class CheckinExpressConfig(BaseModel):
    addr_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    app_score = IntegerField(constraints=[SQL("DEFAULT 0")])
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    end_date = IntegerField(constraints=[SQL("DEFAULT 0")])
    game_score = IntegerField(constraints=[SQL("DEFAULT 0")])
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    msg_id = CharField(unique=True)
    step = IntegerField(constraints=[SQL("DEFAULT 0")])
    td = IntegerField(constraints=[SQL("DEFAULT 0")])
    terms = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'checkin_express_config'

class CheckinExpressReceive(BaseModel):
    addr_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    config_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    end_time = IntegerField(constraints=[SQL("DEFAULT 0")])
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    msg_id = CharField(null=True, unique=True)
    order_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    receive_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    td = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'checkin_express_receive'

class CheckinExpressRecord(BaseModel):
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    config_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    coupon_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    jewel_box = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    msg_id = CharField(null=True, unique=True)
    order_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    show_coupon = IntegerField(constraints=[SQL("DEFAULT 0")])
    sign_for_date = IntegerField(constraints=[SQL("DEFAULT 0")])
    sign_type = IntegerField(constraints=[SQL("DEFAULT 1")])
    step = IntegerField(constraints=[SQL("DEFAULT 0")])
    td = IntegerField(constraints=[SQL("DEFAULT 0")])
    terms = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'checkin_express_record'

class CheckinExpressScoreLog(BaseModel):
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    config_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    gain_date = IntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    msg_id = CharField(unique=True)
    order_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    score = IntegerField(constraints=[SQL("DEFAULT 0")])
    score_source = IntegerField(constraints=[SQL("DEFAULT 0")])
    td = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'checkin_express_score_log'
        indexes = (
            (('buyer_id', 'score_source'), False),
            (('config_id', 'order_id'), False),
        )

class CheckinFortuneRecord(BaseModel):
    award_amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    coupon_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    fortune_level = IntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    open_date = IntegerField(constraints=[SQL("DEFAULT 0")])
    td = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    words = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'checkin_fortune_record'

class CheckinFriend(BaseModel):
    buyer_id = BigIntegerField(index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    friend_id = BigIntegerField(index=True)
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    td = IntegerField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'checkin_friend'

class CheckinFriendRedPacket(BaseModel):
    amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    buyer_id = BigIntegerField(index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    current_date = IntegerField(index=True)
    from_id = BigIntegerField(index=True)
    id = BigAutoField()
    msg_id = CharField(constraints=[SQL("DEFAULT ''")], unique=True)
    td = IntegerField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'checkin_friend_red_packet'

class CheckinFrozenCapital(BaseModel):
    batch_number = CharField(constraints=[SQL("DEFAULT ''")])
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    frozen_funds = IntegerField(constraints=[SQL("DEFAULT 0")])
    message = CharField(constraints=[SQL("DEFAULT ''")])
    msg_id = CharField(constraints=[SQL("DEFAULT ''")], unique=True)
    remains_funds = IntegerField(constraints=[SQL("DEFAULT 0")])
    scene = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    td = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'checkin_frozen_capital'
        indexes = (
            (('buyer_id', 'batch_number'), True),
        )

class CheckinProgramReward(BaseModel):
    buyer_id = BigIntegerField()
    claimed = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    expire_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    msg_id = CharField(unique=True)
    program = IntegerField(constraints=[SQL("DEFAULT 0")])
    rank = IntegerField(constraints=[SQL("DEFAULT 0")])
    td = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'checkin_program_reward'
        indexes = (
            (('buyer_id', 'program', 'rank'), True),
        )

class CheckinRetainReport(BaseModel):
    contrast_first_num = IntegerField(constraints=[SQL("DEFAULT 0")])
    contrast_new = IntegerField(constraints=[SQL("DEFAULT 0")])
    contrast_new_retain = IntegerField(constraints=[SQL("DEFAULT 0")])
    contrast_old = IntegerField(constraints=[SQL("DEFAULT 0")])
    contrast_old_retain = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    exp_first_num = IntegerField(constraints=[SQL("DEFAULT 0")])
    exp_name = CharField(constraints=[SQL("DEFAULT ''")])
    exp_new = IntegerField(constraints=[SQL("DEFAULT 0")])
    exp_new_retain = IntegerField(constraints=[SQL("DEFAULT 0")])
    exp_old = IntegerField(constraints=[SQL("DEFAULT 0")])
    exp_old_retain = IntegerField(constraints=[SQL("DEFAULT 0")])
    td = IntegerField(index=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'checkin_retain_report'

class CheckinRewardPunish(BaseModel):
    buyer_id = BigIntegerField(index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    id = BigAutoField()
    msg_id = CharField(unique=True)
    order_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    score = IntegerField(constraints=[SQL("DEFAULT 0")])
    speed_card_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    td = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    type = IntegerField()

    class Meta:
        table_name = 'checkin_reward_punish'

class CheckinSpeedCard(BaseModel):
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    card_status = IntegerField(constraints=[SQL("DEFAULT 1")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    expire_at = IntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    msg_id = CharField(constraints=[SQL("DEFAULT ''")], unique=True)
    order_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    speed_rate = IntegerField(constraints=[SQL("DEFAULT 2")])
    start_at = IntegerField(constraints=[SQL("DEFAULT 0")])
    td = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'checkin_speed_card'
        indexes = (
            (('buyer_id', 'card_status'), False),
        )

class CheckinSpeedCardRedress(BaseModel):
    amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    expire_at = IntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    msg_id = CharField(constraints=[SQL("DEFAULT ''")], unique=True)
    speed_card_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    td = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'checkin_speed_card_redress'
        indexes = (
            (('buyer_id', 'speed_card_id'), False),
        )

class CheckinWeekly(BaseModel):
    buyer_id = BigIntegerField()
    checkin_list = CharField(constraints=[SQL("DEFAULT '签到列表'")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    current_week = IntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    msg_id = CharField(unique=True)
    repair_day = IntegerField(constraints=[SQL("DEFAULT 0")])
    serial_day = IntegerField(constraints=[SQL("DEFAULT 0")])
    td = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    total_day = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'checkin_weekly'
        indexes = (
            (('buyer_id', 'current_week'), False),
        )

class CheckinWeeklyAward(BaseModel):
    buyer_id = BigIntegerField()
    coupon_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    expire_at = IntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    msg_id = CharField(unique=True)
    serial_day = IntegerField(constraints=[SQL("DEFAULT 0")])
    start_at = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    td = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    week_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'checkin_weekly_award'
        indexes = (
            (('buyer_id', 'week_id'), False),
        )

class CheckinWeeklyRepair(BaseModel):
    buyer_id = BigIntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    msg_id = CharField(unique=True)
    order_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    repair_type = IntegerField(constraints=[SQL("DEFAULT 1")])
    td = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    week_day = IntegerField(constraints=[SQL("DEFAULT 0")])
    week_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'checkin_weekly_repair'
        indexes = (
            (('buyer_id', 'week_id', 'repair_type'), False),
        )

class CoinRewardPolicy(BaseModel):
    buyer_id = BigIntegerField(index=True)
    coins = IntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'coin_reward_policy'

class CollectCardDetail(BaseModel):
    activity_id = IntegerField()
    card_type = IntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    extra = CharField(constraints=[SQL("DEFAULT ''")])
    open_at = DateTimeField(null=True)
    source = IntegerField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    uid = BigIntegerField(index=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'collect_card_detail'

class CollectCardHelpDetail(BaseModel):
    activity_id = IntegerField()
    avatar = CharField()
    card_types = CharField(constraints=[SQL("DEFAULT ''")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    nickname = CharField(constraints=[SQL("DEFAULT ''")])
    owner_uid = BigIntegerField()
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    type = IntegerField(constraints=[SQL("DEFAULT 0")])
    uid = BigIntegerField(index=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'collect_card_help_detail'
        indexes = (
            (('owner_uid', 'activity_id'), False),
        )

class CollectCardPrize(BaseModel):
    activity_id = IntegerField()
    address_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    address_id = BigIntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    is_robot = IntegerField(constraints=[SQL("DEFAULT 0")])
    issued_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    prize = CharField()
    prize_type = IntegerField()
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    uid = BigIntegerField(index=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'collect_card_prize'

class CollectCardUser(BaseModel):
    activity_id = BigIntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    extra = CharField(constraints=[SQL("DEFAULT ''")])
    id = BigAutoField()
    key_card_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    key_card_time = IntegerField(constraints=[SQL("DEFAULT 0")])
    lottery_num = IntegerField(constraints=[SQL("DEFAULT 0")])
    lottery_state = IntegerField(constraints=[SQL("DEFAULT 0")])
    prize_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    uid = BigIntegerField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'collect_card_user'
        indexes = (
            (('uid', 'activity_id'), True),
        )

class CouponCenter(BaseModel):
    coupon_id = BigIntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    end_time = DateTimeField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    mall_id = BigIntegerField()
    rank = IntegerField(constraints=[SQL("DEFAULT 0")])
    start_time = DateTimeField()
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    type = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'coupon_center'

class CouponLink(BaseModel):
    config = TextField(null=True)
    create_at = DateTimeField(null=True)
    end_date = DateField(null=True)
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_enabled = IntegerField(constraints=[SQL("DEFAULT 1")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    start_date = DateField(null=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    url_type = IntegerField()
    url_value = CharField(null=True)

    class Meta:
        table_name = 'coupon_link'

class EnjoyFreeGroup(BaseModel):
    activity_id = IntegerField()
    address_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    buyer_id = IntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    end_ack = IntegerField(constraints=[SQL("DEFAULT 0")])
    end_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    expire_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    goods_id = IntegerField()
    goods_snapshot = CharField(constraints=[SQL("DEFAULT ''")])
    need_cnt = IntegerField(constraints=[SQL("DEFAULT 0")])
    order_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    reward_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    reward_fail_reason = CharField(constraints=[SQL("DEFAULT ''")])
    reward_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    success_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'enjoy_free_group'
        indexes = (
            (('buyer_id', 'activity_id'), False),
        )

class EnjoyFreeHelpCard(BaseModel):
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    expire_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    group_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    use_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    value = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'enjoy_free_help_card'

class FarmAudit(BaseModel):
    action_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    buyer_id = BigIntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    msg_id = CharField(constraints=[SQL("DEFAULT ''")])
    target_id = BigIntegerField()
    target_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'farm_audit'

class FarmUserPack(BaseModel):
    buyer_id = BigIntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    item_cnt = IntegerField()
    item_type = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'farm_user_pack'
        indexes = (
            (('buyer_id', 'item_type'), True),
        )

class FarmUserPet(BaseModel):
    buyer_id = BigIntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    feed_amount = IntegerField()
    id = BigAutoField()
    level = CharField(constraints=[SQL("DEFAULT ''")])
    pet_no = IntegerField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'farm_user_pet'
        indexes = (
            (('buyer_id', 'pet_no'), False),
        )

class FundCommission(BaseModel):
    amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    audit_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    balance = IntegerField(constraints=[SQL("DEFAULT 0")])
    batch_num = CharField(constraints=[SQL("DEFAULT '0'")])
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    entry_at = IntegerField(constraints=[SQL("DEFAULT 0")])
    extend_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    extend_info = TextField(null=True)
    id = BigAutoField()
    msg_id = CharField(constraints=[SQL("DEFAULT '0'")], unique=True)
    scene = IntegerField(constraints=[SQL("DEFAULT -1")])
    share_uid = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    status = IntegerField(constraints=[SQL("DEFAULT -1")], index=True)
    td = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    wx_group_id = CharField(constraints=[SQL("DEFAULT '0'")])

    class Meta:
        table_name = 'fund_commission'
        indexes = (
            (('share_uid', 'audit_type', 'scene'), False),
        )

class FundReturns(BaseModel):
    amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    audit_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    balance = IntegerField(constraints=[SQL("DEFAULT 0")])
    batch_num = CharField(constraints=[SQL("DEFAULT '0'")])
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    entry_at = IntegerField(constraints=[SQL("DEFAULT 0")])
    extend_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    extend_info = TextField(null=True)
    id = BigAutoField()
    msg_id = CharField(constraints=[SQL("DEFAULT '0'")], unique=True)
    scene = IntegerField(constraints=[SQL("DEFAULT -1")])
    status = IntegerField(constraints=[SQL("DEFAULT -1")])
    td = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'fund_returns'
        indexes = (
            (('buyer_id', 'audit_type', 'scene'), False),
        )

class FundReturnsCash(BaseModel):
    amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    card_id = CharField(constraints=[SQL("DEFAULT ''")])
    card_name = CharField(constraints=[SQL("DEFAULT ''")])
    channel = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    msg_id = CharField(constraints=[SQL("DEFAULT ''")], unique=True)
    reason = TextField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT -1")])
    td = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'fund_returns_cash'

class FundSubsidy(BaseModel):
    amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    audit_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    balance = IntegerField(constraints=[SQL("DEFAULT 0")])
    batch_num = CharField(constraints=[SQL("DEFAULT '0'")])
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    extend_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    msg_id = CharField(constraints=[SQL("DEFAULT '0'")], unique=True)
    scene = IntegerField(constraints=[SQL("DEFAULT -1")])
    status = IntegerField(constraints=[SQL("DEFAULT -1")])
    td = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'fund_subsidy'
        indexes = (
            (('buyer_id', 'audit_type', 'scene'), False),
        )

class GiftRing(BaseModel):
    buyer_id = BigIntegerField(unique=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    id = BigAutoField()
    need_cnt = IntegerField()
    process_cnt = IntegerField()
    ring_no = IntegerField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'gift_ring'

class GiftRingOrder(BaseModel):
    amount = IntegerField()
    buyer_id = BigIntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    message = CharField(constraints=[SQL("DEFAULT '订单状态变化的消息'")])
    order_id = CharField(constraints=[SQL("DEFAULT ''")], unique=True)
    ring_id = BigIntegerField()
    ring_idx = IntegerField()
    ring_no = IntegerField()
    status = IntegerField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'gift_ring_order'
        indexes = (
            (('buyer_id', 'ring_no'), False),
        )

class GoodsPool(BaseModel):
    activity_ids = TextField(null=True)
    config = TextField(null=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_reward_coin = IntegerField(constraints=[SQL("DEFAULT 0")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    type = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'goods_pool'

class GoodsPoolGoods(BaseModel):
    activity_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_1 = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    extension_goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    goods_name = CharField(constraints=[SQL("DEFAULT ''")])
    goods_pool_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    message = CharField(constraints=[SQL("DEFAULT ''")])
    parent_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'goods_pool_goods'

class GroupHelpDetail(BaseModel):
    act_id = IntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    group_id = IntegerField(index=True)
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    succ_time = DateTimeField(null=True)
    uid = IntegerField(index=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'group_help_detail'

class GroupHelpFree(BaseModel):
    act_id = IntegerField()
    address_id = BigIntegerField()
    address_snap = CharField(null=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    goods_id = BigIntegerField()
    goods_sku_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    order_id = BigIntegerField()
    owner_uid = BigIntegerField()
    platform = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    succ = IntegerField(constraints=[SQL("DEFAULT 0")])
    success_at = DateTimeField(null=True)
    update_at = DateTimeField(null=True)
    user_count = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'group_help_free'

class GroupHelpSucc(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    goods_id = BigIntegerField()
    help_free_id = IntegerField()
    owner_uid = BigIntegerField()
    receiver_address = CharField(constraints=[SQL("DEFAULT ''")])
    receiver_mobile = CharField(constraints=[SQL("DEFAULT ''")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    update_at = DateTimeField(null=True)

    class Meta:
        table_name = 'group_help_succ'

class LuckyGroup(BaseModel):
    avatar = CharField(constraints=[SQL("DEFAULT ''")])
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    capacity = IntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    is_robot = IntegerField(constraints=[SQL("DEFAULT 0")])
    lottery_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    nick = CharField(constraints=[SQL("DEFAULT ''")])
    point = IntegerField(constraints=[SQL("DEFAULT 0")])
    size = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    td = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'lucky_group'

class LuckyLottery(BaseModel):
    capacity = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    end_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    hd_thumb_url = CharField(constraints=[SQL("DEFAULT ''")])
    id = BigAutoField()
    img_url = CharField(constraints=[SQL("DEFAULT ''")])
    market_price = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    name = CharField(constraints=[SQL("DEFAULT ''")])
    price = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    prize_num = IntegerField(constraints=[SQL("DEFAULT 0")])
    rank = IntegerField()
    start_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    td = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    thumb_url = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'lucky_lottery'
        indexes = (
            (('goods_id', 'start_at'), True),
        )

class LuckyPoint(BaseModel):
    avatar = CharField(constraints=[SQL("DEFAULT ''")])
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    group_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    id = BigAutoField()
    incr = IntegerField(constraints=[SQL("DEFAULT 0")])
    lottery_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    nick = CharField(constraints=[SQL("DEFAULT ''")])
    order_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    td = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    type = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'lucky_point'

class LuckyPrize(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    goods_id = BigIntegerField()
    group_id = BigIntegerField(unique=True)
    id = BigAutoField()
    lottery_id = BigIntegerField(index=True)
    order_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    review_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    status = IntegerField(null=True)
    td = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    type = IntegerField(constraints=[SQL("DEFAULT 1")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'lucky_prize'

class MarketingPlan(BaseModel):
    buyer_group_rule_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    consume_token = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    expire_time = DateTimeField(null=True)
    filters = TextField(null=True)
    interval = IntegerField(constraints=[SQL("DEFAULT 0")])
    msgtpl = TextField()
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    timer = CharField(constraints=[SQL("DEFAULT ''")])
    title = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'marketing_plan'

class MarketingPlanBuyersRecord(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True, null=True)
    file_path = CharField(constraints=[SQL("DEFAULT ''")])
    plan_message = TextField(null=True)
    processed_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    thread_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'marketing_plan_buyers_record'

class MarketingPlanMessage(BaseModel):
    consume_token = CharField(constraints=[SQL("DEFAULT ''")], unique=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    plan_message = TextField(null=True)
    thread_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)

    class Meta:
        table_name = 'marketing_plan_message'

class MarketingPlanRunLog(BaseModel):
    buyer_group_rule_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    consume_token = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    execute_start_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    filters = TextField()
    msgtpl = TextField()
    num = IntegerField(constraints=[SQL("DEFAULT 0")])
    origin_num = IntegerField(constraints=[SQL("DEFAULT 0")])
    plan_id = IntegerField()

    class Meta:
        table_name = 'marketing_plan_run_log'

class MerchantPromotion(BaseModel):
    act_end_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    act_start_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    act_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    activity_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    activity_name = CharField(constraints=[SQL("DEFAULT ''")])
    apply_end_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    apply_start_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    config = CharField(constraints=[SQL("DEFAULT ''")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    creator_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    last_operator_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    reason = CharField(constraints=[SQL("DEFAULT ''")])
    schedule_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'merchant_promotion'

class MerchantPromotionApplication(BaseModel):
    audit_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    goods_name = CharField(constraints=[SQL("DEFAULT ''")])
    id = BigAutoField()
    last_reason = CharField(constraints=[SQL("DEFAULT ''")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    merchant_promotion_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    source = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'merchant_promotion_application'

class MerchantPromotionOpLog(BaseModel):
    application_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    op_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    operator_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    operator_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    reason = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'merchant_promotion_op_log'
        indexes = (
            (('application_id', 'goods_id'), False),
        )

class MparkFriend(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    initiative = IntegerField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    uid1 = BigIntegerField()
    uid2 = BigIntegerField(index=True)

    class Meta:
        table_name = 'mpark_friend'
        indexes = (
            (('uid1', 'uid2'), True),
        )

class MtBindQianshou(BaseModel):
    avatar = CharField(constraints=[SQL("DEFAULT ''")])
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], unique=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    nickname = CharField(constraints=[SQL("DEFAULT ''")])
    qs_wx_no = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    td = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'mt_bind_qianshou'

class OpenboxJoinDetail(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    current_level = IntegerField()
    openbox_id = IntegerField()
    uid = BigIntegerField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'openbox_join_detail'
        indexes = (
            (('uid', 'openbox_id', 'current_level'), False),
        )

class OpenboxRecords(BaseModel):
    buyer_gift_pack_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    current_level = IntegerField()
    end_date = DateField()
    giftpack_id = IntegerField()
    max_level = IntegerField()
    period = IntegerField()
    start_date = DateField()
    uid = BigIntegerField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'openbox_records'
        indexes = (
            (('uid', 'period'), True),
        )

class OrderBonus(BaseModel):
    act = CharField(null=True)
    activate_at = DateTimeField(null=True)
    activate_order_id = BigIntegerField(null=True)
    amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    assist_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    assist_rule = CharField()
    assister_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    audit_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    buyer_id = BigIntegerField()
    complete_at = DateTimeField(null=True)
    coupon_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    distribute_rule = CharField(constraints=[SQL("DEFAULT ''")])
    expire_at = DateTimeField(null=True)
    extra_bonus = IntegerField(constraints=[SQL("DEFAULT 0")])
    get_amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    goods_name = CharField(constraints=[SQL("DEFAULT ''")])
    id = BigAutoField()
    order_id = BigIntegerField(null=True)
    start_at = DateTimeField(index=True, null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    type = IntegerField(constraints=[SQL("DEFAULT 1")])
    user_coupon_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'order_bonus'
        indexes = (
            (('buyer_id', 'order_id'), True),
        )

class OrderBonusAssist(BaseModel):
    amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    assister = BigIntegerField()
    bonus_id = BigIntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    id = BigAutoField()
    self = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'order_bonus_assist'
        indexes = (
            (('assister', 'create_at'), False),
            (('bonus_id', 'assister'), True),
        )

class OrderPushTask(BaseModel):
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    coupon_amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    coupon_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    expire_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    pass_amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    task_rule_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    user_coupon_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'order_push_task'

class PoolGoodsActMap(BaseModel):
    activity_id = IntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    extension_goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'pool_goods_act_map'
        indexes = (
            (('extension_goods_id', 'activity_id'), True),
        )

class PrimeSubsidyAccount(BaseModel):
    buyer_id = BigIntegerField(unique=True)
    charges = IntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    deposit = IntegerField()
    id = BigAutoField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'prime_subsidy_account'

class PrimeSubsidyAudit(BaseModel):
    amount = IntegerField()
    audit_type = IntegerField()
    balance = IntegerField()
    batch_num = CharField(constraints=[SQL("DEFAULT ''")])
    benefit_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    buyer_id = BigIntegerField(index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    enter_status = IntegerField(constraints=[SQL("DEFAULT 1")])
    extend_id = BigIntegerField()
    id = BigAutoField()
    msg_id = CharField(constraints=[SQL("DEFAULT ''")], unique=True)
    scene = IntegerField()
    td = IntegerField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'prime_subsidy_audit'
        indexes = (
            (('buyer_id', 'audit_type', 'scene'), False),
        )

class Promotion(BaseModel):
    activity_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    business_costs = IntegerField(constraints=[SQL("DEFAULT 0")])
    category = IntegerField(constraints=[SQL("DEFAULT 0")])
    code = CharField(constraints=[SQL("DEFAULT ''")])
    config = CharField(constraints=[SQL("DEFAULT ''")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    created_by = CharField(constraints=[SQL("DEFAULT ''")])
    end_time = DateTimeField()
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    start_time = DateTimeField()
    state = IntegerField(constraints=[SQL("DEFAULT 2")])
    title = CharField(constraints=[SQL("DEFAULT ''")])
    title_rule = IntegerField()
    type = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    updated_by = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'promotion'

class PushTaskOrder(BaseModel):
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    payment_amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    payment_order_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    task_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'push_task_order'

class QianshouInviteRelation(BaseModel):
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    group_no = CharField(constraints=[SQL("DEFAULT ''")])
    id = BigAutoField()
    inviter_buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    inviter_wxid = CharField(constraints=[SQL("DEFAULT ''")])
    join_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    wxid = CharField(constraints=[SQL("DEFAULT ''")])

    class Meta:
        table_name = 'qianshou_invite_relation'

class QianshouWxGroup(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    group_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    group_name = CharField(constraints=[SQL("DEFAULT ''")])
    group_no = CharField(constraints=[SQL("DEFAULT ''")], unique=True)
    id = BigAutoField()
    owner_no = CharField(constraints=[SQL("DEFAULT ''")])
    td = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'qianshou_wx_group'

class QianshouWxMember(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    group_no = CharField(constraints=[SQL("DEFAULT ''")])
    id = BigAutoField()
    inviter_no = CharField(constraints=[SQL("DEFAULT ''")])
    member_avatar = CharField(constraints=[SQL("DEFAULT ''")])
    member_nick = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    member_no = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    td = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'qianshou_wx_member'
        indexes = (
            (('member_no', 'group_no'), False),
        )

class QttExchangeCoupon(BaseModel):
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    coupon_id = BigIntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    did = CharField(constraints=[SQL("DEFAULT ''")])
    id = BigAutoField()
    qid = CharField(constraints=[SQL("DEFAULT ''")])
    qtt_tk = CharField(unique=True)
    rid = CharField(constraints=[SQL("DEFAULT ''")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    tk = CharField(constraints=[SQL("DEFAULT ''")])
    tuid = CharField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    user_coupon_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'qtt_exchange_coupon'

class QttTimingRewardClickBakDel20191010(BaseModel):
    abs = CharField(constraints=[SQL("DEFAULT ''")])
    aid = CharField(constraints=[SQL("DEFAULT ''")], null=True, unique=True)
    buyer_create_at = DateTimeField(null=True)
    buyer_id = BigIntegerField(null=True, unique=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    device_create_at = DateTimeField(null=True)
    device_id = BigIntegerField(null=True, unique=True)
    did = CharField(constraints=[SQL("DEFAULT ''")], null=True, unique=True)
    feed_device_time = DateTimeField(index=True, null=True)
    id = BigAutoField()
    ip = CharField(constraints=[SQL("DEFAULT ''")])
    last_create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    order_create_at = DateTimeField(null=True)
    order_id = BigIntegerField(null=True, unique=True)
    order_payment_total = IntegerField(null=True)
    qid = CharField(constraints=[SQL("DEFAULT ''")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    topic = CharField(constraints=[SQL("DEFAULT ''")])
    ts = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'qtt_timing_reward_click_bak_del_20191010'

class Reborncard(BaseModel):
    buyer_id = BigAutoField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    quantity = IntegerField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'reborncard'

class ReborncardAudit(BaseModel):
    buyer_id = BigIntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    incr = IntegerField()
    msg_id = CharField(unique=True)

    class Meta:
        table_name = 'reborncard_audit'

class RechargeActivity(BaseModel):
    activity_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    goods_cate = TextField(null=True)
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    logo = CharField(constraints=[SQL("DEFAULT ''")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    recharge_way = CharField(constraints=[SQL("DEFAULT ''")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'recharge_activity'

class RechargeCate(BaseModel):
    activity_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'recharge_cate'
        indexes = (
            (('activity_id', 'name'), True),
        )

class RechargeGoods(BaseModel):
    activity_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    cate_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    daily_limit = IntegerField(constraints=[SQL("DEFAULT 0")])
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    option_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    priority = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    weights = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'recharge_goods'
        indexes = (
            (('option_id', 'goods_id'), True),
        )

class RechargeOption(BaseModel):
    cate_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    price = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'recharge_option'
        indexes = (
            (('cate_id', 'name'), True),
        )

class RedRain2020Audit(BaseModel):
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    curr_round_start_time = DateTimeField(constraints=[SQL("DEFAULT 1970-01-01 00:00:00")])
    curr_subsidy_amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    recv_cnt = IntegerField(constraints=[SQL("DEFAULT 0")])
    red_rain_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    total_subsidy_amount = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'red_rain_2020_audit'
        indexes = (
            (('buyer_id', 'curr_round_start_time'), True),
        )

class RedrainAuditCoins(BaseModel):
    buyer_id = BigIntegerField()
    coins = IntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    msg_id = CharField(unique=True)
    session = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'redrain_audit_coins'

class RedrainAuditCoinsV2(BaseModel):
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    coins = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    msg_id = CharField(constraints=[SQL("DEFAULT ''")], unique=True)
    namespace = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'redrain_audit_coins_v2'

class RedrainDeposit(BaseModel):
    buyer_id = BigIntegerField(unique=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    deposit = BigIntegerField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'redrain_deposit'

class RedrainDepositV2(BaseModel):
    buyer_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    deposit = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    namespace = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'redrain_deposit_v2'
        indexes = (
            (('buyer_id', 'namespace'), True),
        )

class SeckillGroup(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    date = DateTimeField()
    extra_conf = TextField(null=True)
    is_delete = IntegerField(constraints=[SQL("DEFAULT 0")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'seckill_group'

class SeckillSeries(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    end_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    goods_ids = TextField()
    is_delete = IntegerField(constraints=[SQL("DEFAULT 0")])
    start_time = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    updatt_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'seckill_series'

class T(BaseModel):
    k = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])

    class Meta:
        table_name = 't'

class TopicGroup(BaseModel):
    banner = CharField(constraints=[SQL("DEFAULT ''")])
    config = TextField(null=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    title = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'topic_group'

class TopicGroupGoods(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    goods_id = BigIntegerField(index=True)
    rank = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    topic_group_id = IntegerField(index=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'topic_group_goods'

class WalkCoinAccount(BaseModel):
    coin_num = IntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    uid = BigIntegerField(unique=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'walk_coin_account'

class WalkCoinDetail(BaseModel):
    coin_num = IntegerField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    date = CharField(constraints=[SQL("DEFAULT ''")])
    device = CharField(constraints=[SQL("DEFAULT ''")])
    period = IntegerField()
    status = IntegerField(constraints=[SQL("DEFAULT 1")])
    step_num = IntegerField()
    uid = BigIntegerField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'walk_coin_detail'
        indexes = (
            (('device', 'date'), False),
            (('uid', 'date'), False),
        )

class WalkCoinReward(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    money = IntegerField(constraints=[SQL("DEFAULT 0")])
    msg = CharField(constraints=[SQL("DEFAULT ''")])
    order_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    type = IntegerField(constraints=[SQL("DEFAULT 0")])
    uid = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'walk_coin_reward'

class WalkCoinStepreward(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    msg = CharField(constraints=[SQL("DEFAULT ''")])
    step = IntegerField(constraints=[SQL("DEFAULT 0")])
    type = IntegerField(constraints=[SQL("DEFAULT 0")])
    uid = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'walk_coin_stepreward'

class WelfareLog(BaseModel):
    address = CharField(constraints=[SQL("DEFAULT ''")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], null=True)
    goods_id = BigIntegerField()
    master_uid = BigIntegerField()
    member_uid = BigIntegerField()
    mobile = CharField(constraints=[SQL("DEFAULT ''")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    order_id = BigIntegerField()

    class Meta:
        table_name = 'welfare_log'

