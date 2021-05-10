from getgauge.python import step, data_store
from api.act.schedule.apply_schedule import ApplySchedule


@step("获取新报名系统的列表,类型=<type>")
def apply_schedule(type):
    apply_schedule = ApplySchedule()

    type = data_store.suite.get('act_type', 1) if not type else type
    apply_schedule.data['type'] = int(type)

    resp = apply_schedule.request()
    print(resp)
