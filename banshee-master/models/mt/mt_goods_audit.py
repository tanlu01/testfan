from peewee import *
import os

database = MySQLDatabase('mt_goods_audit', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': os.getenv('MT_MYSQL_HOST'), 'user': os.getenv('MT_MYSQL_USER'), 'password': os.getenv('MT_MYSQL_PASSWORD')})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class AliIllegalWorldsRaw(BaseModel):
    commit_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    id = BigAutoField()
    illegal_worlds = CharField(constraints=[SQL("DEFAULT ''")])
    lock_time = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    lock_uid = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    params = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'ali_illegal_worlds_raw'

class AuditCheck(BaseModel):
    audit_score = IntegerField(constraints=[SQL("DEFAULT 0")])
    audit_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    audit_uid = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    cat_id_1 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_2 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_3 = IntegerField(constraints=[SQL("DEFAULT 0")])
    category = IntegerField(constraints=[SQL("DEFAULT 0")])
    check_score = IntegerField(constraints=[SQL("DEFAULT 0")])
    check_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    check_uid = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    commit_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    content = CharField(constraints=[SQL("DEFAULT ''")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    goods_name = CharField(constraints=[SQL("DEFAULT ''")])
    id = BigAutoField()
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    result = CharField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'audit_check'
        indexes = (
            (('cat_id_1', 'cat_id_2', 'cat_id_3'), False),
        )

class AuditRule(BaseModel):
    audit_func = CharField(constraints=[SQL("DEFAULT ''")])
    cat_id = TextField(index=True, null=True)
    category = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    creator = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    desc = CharField(constraints=[SQL("DEFAULT ''")])
    name = CharField(unique=True)
    score_map = TextField(null=True)
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'audit_rule'

class AuditSnapshot(BaseModel):
    commit_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    created_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    id = BigAutoField()
    results = TextField()
    updated_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'audit_snapshot'

class BgCatPredictRaw(BaseModel):
    commit_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    id = BigAutoField()
    lock_time = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    lock_uid = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    params = CharField(constraints=[SQL("DEFAULT ''")])
    prediction = TextField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'bg_cat_predict_raw'

class BgImageBrandRaw(BaseModel):
    commit_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    goods_brand_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    job_id = CharField(unique=True)
    lock_time = IntegerField(constraints=[SQL("DEFAULT 0")])
    lock_uid = IntegerField(constraints=[SQL("DEFAULT 0")])
    name = CharField()
    result_brand_id = IntegerField()
    result_brand_name = CharField(constraints=[SQL("DEFAULT ''")])
    result_score = CharField(constraints=[SQL("DEFAULT ''")])
    thumb_res = TextField()
    thumb_url = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'bg_image_brand_raw'

class BgImagePsoRaw(BaseModel):
    commit_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    id = BigAutoField()
    lock_time = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    lock_uid = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    name = CharField()
    rotation_result = TextField()
    rotation_urls = CharField()
    thumb_result = TextField()
    thumb_url = CharField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'bg_image_pso_raw'

class BgImageUrlRaw(BaseModel):
    commit_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], unique=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    id = BigAutoField()
    image_url = CharField(constraints=[SQL("DEFAULT ''")])
    image_url_md5 = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    image_url_res = TextField(null=True)
    lock_time = IntegerField(constraints=[SQL("DEFAULT 0")])
    lock_uid = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'bg_image_url_raw'

class BgTitleBrandRaw(BaseModel):
    commit_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    goods_brand_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    job_id = CharField(unique=True)
    lock_time = IntegerField(constraints=[SQL("DEFAULT 0")])
    lock_uid = IntegerField(constraints=[SQL("DEFAULT 0")])
    name = CharField()
    result_brand_id = IntegerField()
    result_brand_name = CharField(constraints=[SQL("DEFAULT ''")])
    result_res = TextField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'bg_title_brand_raw'

class BjImageCensorRaw(BaseModel):
    commit_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    id = BigAutoField()
    lock_time = IntegerField(constraints=[SQL("DEFAULT 0")])
    lock_uid = IntegerField(constraints=[SQL("DEFAULT 0")])
    name = CharField()
    rotation_result = TextField()
    rotation_urls = CharField()
    thumb_result = TextField()
    thumb_url = CharField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'bj_image_censor_raw'

class Commit(BaseModel):
    audit_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    audit_status = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    auditor = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    auto_audit_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    cat_id_1 = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    cat_id_2 = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    cat_id_3 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cost_template_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    first_commit_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    goods_name = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    id = BigAutoField()
    in_act = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_new = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_standard_sample = IntegerField(constraints=[SQL("DEFAULT 0")])
    mall_id = BigIntegerField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'commit'
        indexes = (
            (('goods_id', 'audit_status', 'mall_id'), False),
            (('mall_id', 'goods_id'), False),
            (('mall_id', 'is_deleted'), False),
        )

class CommitExtend(BaseModel):
    audit_info = TextField(null=True)
    commit_id = BigAutoField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    diff = TextField(null=True)
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    reject_reason = TextField(null=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'commit_extend'

class CommitJob(BaseModel):
    category_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    commit_id = IntegerField(index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    is_completed = IntegerField(constraints=[SQL("DEFAULT 0")])
    job_id = CharField(constraints=[SQL("DEFAULT ''")], index=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'commit_job'

class CommitReject(BaseModel):
    commit_id = BigIntegerField(index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    reason_uniqid = CharField(constraints=[SQL("DEFAULT ''")])
    reject_enum_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    reject_enum_type_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'commit_reject'

class CommitRemainTime(BaseModel):
    auditor = IntegerField(constraints=[SQL("DEFAULT 0")])
    commit_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    open_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    over_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    seconds = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'commit_remain_time'

class CommitThirdService(BaseModel):
    commit_id = BigAutoField()
    completed_num = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    service_num = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'commit_third_service'

class DtAuditBrand(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    goods_appeal_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    goods_name = CharField(constraints=[SQL("DEFAULT ''")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    new_brand_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    old_brand_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    oms_state = IntegerField(constraints=[SQL("DEFAULT 0")])
    raw = TextField(null=True)
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    state = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    user_id = IntegerField(constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'dt_audit_brand'
        indexes = (
            (('goods_id', 'mall_id', 'state'), False),
        )

class DtAuditGoodsCat(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    deleted_at = IntegerField(constraints=[SQL("DEFAULT 0")])
    goods_appeal_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    human_cat_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    new_cat_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    old_cat_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    oms_state = IntegerField(constraints=[SQL("DEFAULT 0")])
    params = TextField()
    prediction = TextField()
    prediction_cat_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    state = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'dt_audit_goods_cat'

class DtAuditImage(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    goods_appeal_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], unique=True)
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    goods_name = CharField(constraints=[SQL("DEFAULT ''")])
    id = BigAutoField()
    job_id = CharField(constraints=[SQL("DEFAULT ''")], unique=True)
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    oms_state = IntegerField(constraints=[SQL("DEFAULT 0")])
    remark = CharField(constraints=[SQL("DEFAULT ''")])
    rotation_result = CharField(constraints=[SQL("DEFAULT ''")])
    rotation_urls = CharField(constraints=[SQL("DEFAULT ''")])
    state = IntegerField(constraints=[SQL("DEFAULT -1")])
    thumb_result = CharField(constraints=[SQL("DEFAULT ''")])
    thumb_url = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'dt_audit_image'

class DtGoodsAppeal(BaseModel):
    appeal_total = IntegerField(constraints=[SQL("DEFAULT 0")])
    audit_brand_state = IntegerField(constraints=[SQL("DEFAULT 0")])
    audit_cat_state = IntegerField(constraints=[SQL("DEFAULT 0")])
    audit_image_state = IntegerField(constraints=[SQL("DEFAULT 0")])
    brand_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_1 = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    cat_id_2 = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    cat_id_3 = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    expire_at = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    goods_name = CharField(constraints=[SQL("DEFAULT ''")])
    id = BigAutoField()
    is_hit_brand = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_hit_cat = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_hit_image = IntegerField(constraints=[SQL("DEFAULT 0")])
    mall_id = IntegerField(index=True)
    mall_name = CharField(index=True)
    mms_estate = IntegerField(constraints=[SQL("DEFAULT 0")])
    oms_state = IntegerField(constraints=[SQL("DEFAULT 10")], index=True)
    oper_user_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    order7days = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    queue_brand_state = IntegerField(constraints=[SQL("DEFAULT 2")])
    queue_goods_cat_state = IntegerField(constraints=[SQL("DEFAULT 2")])
    queue_image_state = IntegerField(constraints=[SQL("DEFAULT 2")])
    scan_task_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    state = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    total = IntegerField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'dt_goods_appeal'

class DtImageBrand(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    goods_appeal_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    goods_brand_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    job_id = CharField(constraints=[SQL("DEFAULT ''")], unique=True)
    name = CharField(constraints=[SQL("DEFAULT '0'")])
    result_brand_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    result_brand_name = CharField(constraints=[SQL("DEFAULT '0'")])
    result_res = TextField(null=True)
    result_score = CharField(constraints=[SQL("DEFAULT '0'")])
    scan_task_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    state = IntegerField(constraints=[SQL("DEFAULT 0")])
    thumb_url = CharField(constraints=[SQL("DEFAULT '0'")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'dt_image_brand'

class DtReason(BaseModel):
    audit_brand_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    audit_goods_cat_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    audit_image_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    content = TextField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    pics = TextField()
    remark = TextField(null=True)
    state = IntegerField(constraints=[SQL("DEFAULT 0")])
    type = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'dt_reason'

class DtScanTask(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    finish_at = IntegerField(constraints=[SQL("DEFAULT 0")])
    goods_cat_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    goods_id = TextField(null=True)
    goods_reveiw_state = IntegerField(constraints=[SQL("DEFAULT 0")])
    goods_state = IntegerField(constraints=[SQL("DEFAULT 0")])
    mall_id = TextField(null=True)
    state = IntegerField(constraints=[SQL("DEFAULT 0")])
    task_type = CharField(constraints=[SQL("DEFAULT '0'")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    valid_hours = IntegerField(constraints=[SQL("DEFAULT 168")])

    class Meta:
        table_name = 'dt_scan_task'

class DtTitleBrand(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    goods_appeal_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    goods_brand_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    job_id = CharField(constraints=[SQL("DEFAULT ''")], unique=True)
    name = CharField(constraints=[SQL("DEFAULT '0'")])
    result_brand_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    result_brand_name = CharField(constraints=[SQL("DEFAULT '0'")])
    result_res = TextField(null=True)
    scan_task_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    state = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'dt_title_brand'
        indexes = (
            (('goods_appeal_id', 'scan_task_id'), False),
        )

class HumanReview(BaseModel):
    audit_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    bar_code_state = TextField(null=True)
    brand_predict_state = IntegerField(constraints=[SQL("DEFAULT 0")])
    commit_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], unique=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    image_url_state = IntegerField(constraints=[SQL("DEFAULT 0")])
    old_brand_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    old_leaf_cat_id = IntegerField()
    prediction_state = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    pso_rotation_state = TextField()
    pso_thumb_machine_state = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    pso_thumb_state = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    rule_brand_state = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'human_review'

class InspCommit(BaseModel):
    audit_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    audit_auditor = IntegerField(constraints=[SQL("DEFAULT 0")])
    audit_info = CharField(constraints=[SQL("DEFAULT '[]'")])
    audit_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_1 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_2 = IntegerField(constraints=[SQL("DEFAULT 0")])
    cat_id_3 = IntegerField(constraints=[SQL("DEFAULT 0")])
    commit_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    hit_service = CharField(constraints=[SQL("DEFAULT '[]'")])
    id = BigAutoField()
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    review_audit_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    review_audit_auditor = IntegerField(constraints=[SQL("DEFAULT 0")])
    review_audit_result = IntegerField(constraints=[SQL("DEFAULT 0")])
    review_audit_status = IntegerField(constraints=[SQL("DEFAULT 10")])
    review_offline_reason = CharField(constraints=[SQL("DEFAULT '[]'")])
    review_reject_reason = TextField(null=True)
    rule_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    snapshot_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    task_uniqid = CharField(constraints=[SQL("DEFAULT '0'")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")], index=True)

    class Meta:
        table_name = 'insp_commit'
        indexes = (
            (('audit_status', 'update_at'), False),
            (('goods_id', 'audit_status', 'mall_id'), False),
            (('mall_id', 'goods_id'), False),
        )

class InspCommitRule(BaseModel):
    auditor = IntegerField(constraints=[SQL("DEFAULT 0")])
    case_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    delete_at = IntegerField(constraints=[SQL("DEFAULT 0")])
    gen_audit_at = IntegerField(constraints=[SQL("DEFAULT 0")])
    hm_case_one = CharField(constraints=[SQL("DEFAULT ' '")])
    hm_case_two = IntegerField(constraints=[SQL("DEFAULT 0")])
    hm_gmv7days = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    hm_order7days = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    hm_pv7days = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    hm_ratio = IntegerField(constraints=[SQL("DEFAULT 0")])
    mc_audit_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    mc_gmv7days = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    mc_order7days = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    mc_pv7days = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    mc_ratio = IntegerField(constraints=[SQL("DEFAULT 0")])
    rule_name = CharField(constraints=[SQL("DEFAULT ' '")])
    state = IntegerField(constraints=[SQL("DEFAULT 20")])
    tmp_end_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    tmp_start_at = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    type_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'insp_commit_rule'

class MtIllegalWorldsRaw(BaseModel):
    commit_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    id = BigAutoField()
    illegal_worlds = CharField()
    params = CharField(constraints=[SQL("DEFAULT ''")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'mt_illegal_worlds_raw'

