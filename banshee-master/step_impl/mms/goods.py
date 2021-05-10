from time import sleep

from getgauge.python import step, data_store

from api.mms.goods.ChangeQuantity import ChangeSkuQuantity
from api.mms.goods.goods_onsale import Batchonsale
from api.mms.goods.sku_detail import SkuDetail
from api.mms.products.goods_list import GoodsList


@step("获取上架状态商品数量")
def up_goods_list():
    search_goods = GoodsList()

    search_goods.data['status'] = 2
    resp = search_goods.request()

    assert resp['code'] == 0

    up_goods_count = data_store.suite.get('up_goods_count', False)
    if not up_goods_count:
        data_store.suite['up_goods_count'] = resp['payload']['count']
    else:
        assert resp['payload']['count'] == up_goods_count + 1
        data_store.suite['up_goods_count'] += 1


@step("获取下架状态商品数量")
def down_goods_list():
    search_goods = GoodsList()

    search_goods.data['status'] = 4
    resp = search_goods.request()

    assert resp['code'] == 0

    down_goods_count = data_store.suite.get('down_goods_count', False)
    if not down_goods_count:
        data_store.suite['down_goods_count'] = resp['payload']['count']
    else:
        assert resp['payload']['count'] == down_goods_count + 1
        data_store.suite['down_goods_count'] += 1


@step("查询商品,goods_id=<goods_id>,goods_status=<goods_status>")
def goods_search(goods_id, goods_status):
    goods_search = GoodsList()

    goods_search.data['status'] = int(goods_status)
    goods_id = data_store.suite['goods_id'] if not goods_id else goods_id
    goods_search.data['goods_id'] = int(goods_id)
    resp = goods_search.request()

    assert resp['payload']['count'] == 1

    quantity = data_store.suite.get('goods_quantity', False)
    if not quantity:
        data_store.suite['goods_quantity'] = resp['payload']['list'][0]['quantity']
    else:
        assert resp['payload']['list'][0]['quantity'] == quantity - 1
        data_store.suite['goods_quantity'] -= 1



@step("已上架商品,批量下架,已下架商品,批量上架")
def batch_goods():
    goods_list = GoodsList()
    resp = goods_list.request()
    assert resp["code"] == 0
    list = [item for item in resp["payload"]["list"] if item["is_onsale"] == "1"]
    if len(list) > 1:
        goods_id_list = [item["goods_id"] for item in list[0:2]]
        goods_ids = ",".join(goods_id_list)
        batchonsale = Batchonsale()
        batchonsale.data["is_onsale"] = "0"
        batchonsale.data["goods_ids"] = goods_ids
        resp = batchonsale.request()
        assert resp["code"] == 0
        sleep(10)
        batchonsale.data["is_onsale"] = "1"
        batchonsale.data["goods_ids"] = goods_ids
        resp = batchonsale.request()
        assert resp["code"] == 0






@step("检查下架商品状态不变")
def check_undercarriage():
    goods_list = GoodsList()
    resp = goods_list.request()
    assert resp["code"] == 0
    if len(resp["payload"]["list"])>0:
        for item in resp["payload"]["list"]:
            if item["goods_id"] in data_store.suite["undercarriage_id"]:
                assert item["is_onsale"]=="0"


@step("修改库存数值")
def update_quantity():
    goods_list = GoodsList()
    resp = goods_list.request()
    assert resp["code"] == 0
    goods_id=resp["payload"]["list"][0]["goods_id"]
    skuDetail=SkuDetail()
    skuDetail.api=skuDetail.api.replace("$goods_id",goods_id)
    resp=skuDetail.request()
    assert resp["code"] == 0
    stock=resp["payload"]["sku"][0]["stock"]
    sku_id=resp["payload"]["sku"][0]["sku_id"]
    changeSkuQuantity=ChangeSkuQuantity()
    changeSkuQuantity.data["change_quantity"]={sku_id:int(stock)+2}
    resp=changeSkuQuantity.request()
    assert resp["code"] == 0


