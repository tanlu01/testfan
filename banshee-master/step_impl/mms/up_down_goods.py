from getgauge.python import step, data_store

from api.mms.products.goods_list import GoodsList
from api.mms.products.up_down_goods import UpDownGoods


@step("<status1>状态商品<status2>,goods_id=<goods_id>,flag=<flag>")
def up_goods(status1,status2,goods_id,flag):
    up_down_goods = UpDownGoods()
    if status1=="上架" and status2=="下架":
        temp = "0"
    if status1 == "下架" and status2 == "上架":
        temp = "1"
    if flag=="1":
        goods_list = GoodsList()
        resp = goods_list.request()
        assert resp["code"] == 0
        goods_id = resp["payload"]["list"][0]["goods_id"]
    else:
        goods_id = data_store.suite['goods_id'] if not  goods_id else goods_id
    up_down_goods.data['goods_id'] = int(goods_id)
    up_down_goods.data['is_onsale'] = temp
    resp = up_down_goods.request()
    assert resp['code'] == 0



