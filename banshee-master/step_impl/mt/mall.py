from getgauge.python import step, data_store
from api.mt.mall.mall_goods import MallGoods
from api.mt.mall.goods_v2 import GoodsV2
from api.mt.order.order_v1 import OrderV1


@step("获取店铺商品, mall_id=<mall_id>")
def mall_goods(mall_id):
    mall_goods = MallGoods()
    mall_goods.api = mall_goods.api.replace('$mall_id', mall_id)
    resp = mall_goods.request()

    assert resp['code'] == 0
    data_store.scenario.setdefault('mall_goods_info', {}).update({'goods_id': resp['data']['items'][0]['goods_id']})


@step("获取店铺某一商品信息,goods_id=<goods_id>")
def goods_v2(goods_id):
    goods_v2 = GoodsV2()
    goods_id = data_store.scenario['mall_goods_info']['goods_id'] if not goods_id else goods_id
    goods_v2.api = goods_v2.api.replace('$goods_id', goods_id)
    resp = goods_v2.request()

    assert resp['code'] == 0
    data_store.scenario.setdefault('mall_goods_info', {}).update({'goods_sku_id': resp['data']['skus'][0]['sku_id']})
    data_store.scenario.setdefault('mall_goods_info', {}).update({'price': resp['data']['min_price']})


@step("直接下单")
def order_v1():
    order_v1 = OrderV1()
    order_v1.data['goods_id'] = int(data_store.scenario['mall_goods_info']['goods_id'])
    order_v1.data['goods_sku_id'] = int(data_store.scenario['mall_goods_info']['goods_sku_id'])
    order_v1.data['expected_payment_total'] = int(data_store.scenario['mall_goods_info']['price'])
    resp = order_v1.request()

    assert resp['code'] == 0
    assert resp['data']['order_id'] != ''
