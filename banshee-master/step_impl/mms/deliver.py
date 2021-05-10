import time

from getgauge.python import step, data_store
from api.mms.deliver.mallstate import Mallstate
from api.mms.deliver.goods_material import GoodsMaterial
from api.mms.deliver.deliver import Deliver
import time

@step("校验当前店铺是否参加物流提升计划")
def mallstate():
    mallstate = Mallstate()
    resp = mallstate.request()
    assert resp['code'] == 0
    data_store.suite['mallstate'] = resp['payload']['is_sign_up']


@step("设置商品包装材质,goods_id=<goods_id>")
def goodsmaterial(goods_id):
    if data_store.suite['mallstate']:
        goodsmaterial = GoodsMaterial()

        goods_id = data_store.suite['goods_id'] if not goods_id else goods_id
        goodsmaterial.data['goods_ids'] = [goods_id]

        resp = goodsmaterial.request()

        assert resp['code'] == 0


@step("订单发货,order_id=<order_id>")
def deliver(order_id):
    deliver = Deliver()
    time.sleep(10)
    order_id = data_store.suite['order_id'] if not order_id else order_id
    deliver.data['order_id'] = order_id
    data_store.suite['order_id']=order_id
    resp = deliver.request()
    assert resp['code'] == 0
    data_store.suite['deliver'] = True

