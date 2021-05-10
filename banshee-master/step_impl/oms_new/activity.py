from getgauge.python import step, data_store
from api.oms_new.activity.list import List
from api.oms_new.activity.detail import Detail


@step("获取已导入商品进行中状态的专题")
def list():
    list = List()

    resp = list.request()

    assert resp['code'] == 0

    for i in resp['payload']['list']:
        detail = Detail()
        detail.api = detail.api.replace('$activity_id', str(i['id']))
        resp = detail.request()

        assert resp['code'] == 0

        if resp['payload']['total'] > 0:
            data_store.suite['activity_id'] = i['id']
            data_store.suite['activity_desc'] = "{} | {}".format(i['id'], i['name'])
            break
