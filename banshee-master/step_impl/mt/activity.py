from getgauge.python import step, data_store
from api.mt.activity.seckill import Seckill


@step("获取秒杀活动详情,activity_id=<activity_id>")
def seckill(activity_id):
    activity_id = data_store.suite['oms_new_activity_id'] if not activity_id else activity_id

    seckill = Seckill()
    seckill.api = seckill.api.replace('$activity_id', str(activity_id))

    resp = seckill.request()
    assert resp['code'] == 0
    resp = resp['data']['goods'][0]

    flag = data_store.suite.get('activity_goods_detail', False)
    if not flag:
        data_store.suite.setdefault('activity_goods_detail', {}).update({
            'stocks': resp['stocks'],
            'sales_percent': resp['sales_percent']
        })
        data_store.suite['goods_id'] = resp['goods_id']
    else:
        if resp['stocks'] == 0:
            assert resp['sales_percent'] == 100
        else:
            assert resp['sales_percent'] == resp['stocks']/flag['stocks']*100
        assert resp['stocks'] == flag['stocks'] - 1
