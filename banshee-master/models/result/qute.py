from peewee import *
import os

database = MySQLDatabase('qute', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': os.getenv('QUTE_MYSQL_HOST'), 'user': os.getenv('QUTE_MYSQL_USER'), 'password': os.getenv('QUTE_MYSQL_PWD')})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class JenkinsCoverageJob(BaseModel):
    app = CharField(null=True)
    create_time = DateTimeField(null=True)
    dept = CharField(null=True)
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    job_name = CharField(null=True)
    language = CharField(null=True)
    module = CharField(null=True)
    owner = CharField(null=True)
    update_time = DateTimeField(null=True)

    class Meta:
        table_name = 'jenkins_coverage_job'

class TestProject(BaseModel):
    app = CharField(null=True)
    create_by = CharField(null=True)
    create_time = DateTimeField(null=True)
    dept = CharField(index=True, null=True)
    id = BigAutoField()
    module = CharField(null=True)
    name = CharField(null=True)
    owner = CharField(null=True)
    update_time = DateTimeField(null=True)

    class Meta:
        table_name = 'test_project'

class JenkinsDailyRunJob(BaseModel):
    create_time = DateTimeField(null=True)
    id = BigAutoField()
    job_name = CharField(null=True)
    job_url = CharField(null=True)
    owner = CharField(null=True)
    project = ForeignKeyField(column_name='project_id', field='id', model=TestProject, null=True)
    project_name = CharField(null=True)
    update_time = DateTimeField(null=True)

    class Meta:
        table_name = 'jenkins_daily_run_job'

class Member(BaseModel):
    create_time = DateTimeField(null=True)
    department_name = CharField(null=True)
    email = CharField(null=True)
    email_name = CharField(unique=True)
    id = BigIntegerField(index=True)
    position = CharField(null=True)
    role_name = CharField(null=True)
    status = IntegerField(null=True)
    update_time = DateTimeField(null=True)
    username = CharField(null=True)

    class Meta:
        table_name = 'member'
        indexes = (
            (('id', 'email_name'), True),
        )
        primary_key = CompositeKey('email_name', 'id')

class TestCase(BaseModel):
    active_count = BigIntegerField(null=True)
    api_path = CharField(null=True)
    app = CharField(null=True)
    case_full_path = CharField(null=True)
    case_name = CharField(null=True)
    category = CharField(null=True)
    create_by = CharField(null=True)
    create_time = DateTimeField(null=True)
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    owner = CharField(index=True, null=True)
    project = ForeignKeyField(column_name='project_id', field='id', model=TestProject, null=True)
    src_from = CharField(null=True)
    testlink_id = IntegerField(null=True)
    update_time = DateTimeField(null=True)

    class Meta:
        table_name = 'test_case'

class TestCaseTrend(BaseModel):
    api_num = BigIntegerField(null=True)
    app = CharField(null=True)
    case_num = BigIntegerField(null=True)
    created_date = CharField(null=True)
    dept = CharField(null=True)
    id = BigAutoField()
    line_rate = BigIntegerField(null=True)
    module = CharField(null=True)

    class Meta:
        table_name = 'test_case_trend'

class TestCaseTrendSum(BaseModel):
    api_num = BigIntegerField(null=True)
    app = CharField(null=True)
    case_num = BigIntegerField(null=True)
    created_date = CharField(null=True)
    dept = CharField(null=True)
    id = BigAutoField()
    line_rate = BigIntegerField(null=True)
    module = CharField(null=True)

    class Meta:
        table_name = 'test_case_trend_sum'

class TestCoverage(BaseModel):
    classes_rate = FloatField(null=True)
    conditionals_rate = FloatField(null=True)
    coverage_job_id = IntegerField(null=True)
    create_time = DateTimeField(null=True)
    files_rate = FloatField(null=True)
    id = BigAutoField()
    is_deleted = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    job_build_num = IntegerField(null=True)
    lines_rate = FloatField(null=True)
    methods_rate = FloatField(null=True)
    packages_rate = FloatField(null=True)

    class Meta:
        table_name = 'test_coverage'

class TestRun(BaseModel):
    cost_time = BigIntegerField(null=True)
    create_time = DateTimeField(null=True)
    id = BigAutoField()
    job_build_num = BigIntegerField(null=True)
    job = ForeignKeyField(column_name='job_id', field='id', model=JenkinsDailyRunJob, null=True)
    trigger = IntegerField(null=True)

    class Meta:
        table_name = 'test_run'

class TestRunDetails(BaseModel):
    case_end = DateTimeField(null=True)
    case = ForeignKeyField(column_name='case_id', field='id', model=TestCase, null=True)
    case_start = DateTimeField(index=True, null=True)
    cost_time = FloatField(null=True)
    domain = CharField(null=True)
    env = CharField(null=True)
    error_message = CharField(null=True)
    id = BigAutoField()
    result = CharField(null=True)
    run = ForeignKeyField(column_name='run_id', field='id', model=TestRun, null=True)

    class Meta:
        table_name = 'test_run_details'

class TestlinkData(BaseModel):
    app = CharField(null=True)
    is_delete = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    tl_case_id = IntegerField(null=True)
    tl_case_name = CharField(null=True)
    tl_project_id = IntegerField(null=True)
    tl_project_name = CharField(null=True)
    tl_project_prefix = CharField(null=True)
    tl_suit_id = IntegerField(null=True)
    tl_suit_name = CharField(null=True)

    class Meta:
        table_name = 'testlink_data'

