from getgauge.python import step,data_store
from api.mms.activity.activity_list import ActivityList
from api.mms.activity.activity_detail import ActivityDetail
from api.mms.activity.activity_punish import ActivityPunish
from models.mt.pt_merchant import MallPunishmentLimit as MallModel


@step("获取商家端活动列表,更改更改act_type=<act_type>,act_cate=<act_cate>")
def activity_list(act_type,act_cate):
    activity_list = ActivityList()
    activity_list.data['act_type'] = int(act_type)
    activity_list.data['act_cate'] = int(act_cate)
    resp = activity_list.request()

    assert resp['code'] == 0 
    if resp['payload']['list']:
        data_store.suite['schedule_id'] = resp['payload']['list'][0]['schedule_id']


@step("商家端活动详情,schedule_id=<schedule_id>")
def activity_detail(schedule_id):
    schedule_id = data_store.suite['schedule_id'] if not schedule_id else schedule_id
    activity_detail = ActivityDetail()
    activity_detail.data['schedule_id'] = int(schedule_id)
    resp = activity_detail.request()

    assert resp['code'] == 0


@step("校验并更新商家资质参加活动")
def activity_punish():
    activity_punish = ActivityPunish()
    resp = activity_punish.request()

    assert resp['code'] == 0
    if resp['payload'].get('id', False):
        update_mall_status(data_store.suite['mall_id'])


@step('db更新店铺资质,用于添加商品参加活动,mall_id=<mall_id>')
def update_mall_status(mall_id):
    mall_id = data_store.suite['mall_id'] if not mall_id else int(mall_id)
    data = MallModel.filter(mall_id=mall_id)

    if len(data):
        for i in data:
            print(i.mall_id)
            i.mall_id = 0
            i.save()
    assert True
