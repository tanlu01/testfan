from getgauge.python import step, data_store
from api.mms.activity.activity_promotion import Activity_Promotion
from tools.generate_schema import GenerateSchema

@step("查看活动列表,module_type_id=<module_type_id>,schedule_name=<schedule_name>,articipate_status=<articipate_status>")
def activity_promotion(module_type_id,schedule_name,articipate_status):
    
    activity_promotion = Activity_Promotion() 
    module_type_id = int(module_type_id) if module_type_id else None
    articipate_status = int(articipate_status) if articipate_status else None

    activity_promotion.data['module_type_id'] = module_type_id
    activity_promotion.data['schedule_name'] = schedule_name
    activity_promotion.data['articipate_status'] = articipate_status

    resp = activity_promotion.request()

    # print(GenerateSchema(resp).run())
    assert resp['code'] == 0
    
