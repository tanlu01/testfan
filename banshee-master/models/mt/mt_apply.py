from peewee import *

database = MySQLDatabase('mt_apply', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': 'rm-uf6pec9k82nsk59o8.mysql.rds.aliyuncs.com', 'port': 3306, 'user': 'qa_rw_user', 'password': '8QoK6AjTvSMqs35lm4fwLuyPke0F'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Application(BaseModel):
    activity_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    activity_stock = IntegerField(constraints=[SQL("DEFAULT 0")])
    audit_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    biz = TextField(null=True)
    cat_id_1 = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    goods_name = CharField(constraints=[SQL("DEFAULT ''")])
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    last_reason = CharField(constraints=[SQL("DEFAULT ''")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    reason_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    schedule_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    schedule_sub_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    schedule_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    series_id = CharField(constraints=[SQL("DEFAULT ''")])
    source = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'application'
        indexes = (
            (('goods_id', 'goods_name'), False),
            (('schedule_id', 'goods_id'), True),
        )

class ApplicationEliminated(BaseModel):
    activity_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    application_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    eliminate_info = UnknownField()  # json
    gmv_7days = UnknownField(null=True)  # json
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    goods_name = CharField(constraints=[SQL("DEFAULT ''")])
    goods_url = CharField(constraints=[SQL("DEFAULT ''")])
    id = BigAutoField()
    schedule_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    schedule_name = CharField(constraints=[SQL("DEFAULT ''")])
    source = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'application_eliminated'

class ApplicationOpLog(BaseModel):
    application_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    op_status = IntegerField(constraints=[SQL("DEFAULT 0")])
    operator_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    operator_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    reason = CharField(constraints=[SQL("DEFAULT ''")])
    reason_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'application_op_log'
        indexes = (
            (('application_id', 'goods_id'), False),
        )

class ApplicationSku(BaseModel):
    activity_stock = IntegerField(constraints=[SQL("DEFAULT 0")])
    application_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    config = TextField(null=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    sku_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)

    class Meta:
        table_name = 'application_sku'

class ApplyExportTask(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    file_path = CharField(constraints=[SQL("DEFAULT ''")])
    filters = TextField(null=True)
    name = CharField(constraints=[SQL("DEFAULT ''")])
    operator_id = IntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'apply_export_task'

class ApplyGoodsBlacklist(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    creator_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    goods_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    last_operator_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    mall_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    schedule_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'apply_goods_blacklist'
        indexes = (
            (('schedule_id', 'goods_id'), True),
        )

class LegoGmvThreshold(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    lego_code = CharField(constraints=[SQL("DEFAULT ''")])
    lego_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    lego_name = CharField(constraints=[SQL("DEFAULT ''")])
    threshold = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'lego_gmv_threshold'

class ModuleType(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    creator_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    desc = CharField(constraints=[SQL("DEFAULT ''")])
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    last_operator_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    last_reason = CharField(constraints=[SQL("DEFAULT ''")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    sort = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'module_type'

class Schedule(BaseModel):
    act_rules = CharField(constraints=[SQL("DEFAULT ''")])
    apply_end_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    apply_start_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    config = TextField(null=True)
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")], index=True)
    creator_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    desc = CharField(constraints=[SQL("DEFAULT ''")])
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    is_longterm = IntegerField(constraints=[SQL("DEFAULT 0")])
    last_operator_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    module_type_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    name = CharField(constraints=[SQL("DEFAULT ''")])
    reason = CharField(constraints=[SQL("DEFAULT ''")])
    relation_ids = TextField(null=True)
    rule = TextField(null=True)
    schedule_end_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    schedule_start_time = DateTimeField(constraints=[SQL("DEFAULT 0000-00-00 00:00:00")])
    schedule_type_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    sub_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    thumb = CharField(constraints=[SQL("DEFAULT ''")])
    type = IntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'schedule'

class ScheduleRef(BaseModel):
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")])
    ref_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    ref_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    schedule_id = BigIntegerField(constraints=[SQL("DEFAULT 0")])
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'schedule_ref'
        indexes = (
            (('schedule_id', 'ref_id'), False),
        )

class ScheduleStat(BaseModel):
    apply_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    apply_mall_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    apply_pass_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    exit_apply_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    exit_apply_pass_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    id = BigAutoField()
    is_ended = IntegerField(constraints=[SQL("DEFAULT 0")])
    satisfied_mall_count = IntegerField(constraints=[SQL("DEFAULT 0")])
    schedule_id = BigIntegerField(constraints=[SQL("DEFAULT 0")], index=True)
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'schedule_stat'

class ScheduleType(BaseModel):
    backend_config = TextField()
    create_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])
    display_config = TextField()
    name = CharField(constraints=[SQL("DEFAULT ''")])
    operator_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    pid = IntegerField(constraints=[SQL("DEFAULT 0")])
    status = IntegerField(constraints=[SQL("DEFAULT 0")])
    sub_type = IntegerField()
    type = IntegerField()
    update_at = DateTimeField(constraints=[SQL("DEFAULT CURRENT_TIMESTAMP")])

    class Meta:
        table_name = 'schedule_type'
        indexes = (
            (('type', 'sub_type'), True),
        )

