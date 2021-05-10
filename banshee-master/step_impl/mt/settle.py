import json

from getgauge.python import step, data_store
from api.mt.goods.address import CreateAddress
from api.mt.order.v2_order_check import Order_check


@step("新增地址检查")
def check_add_address():
    create_address = CreateAddress()
    resp = create_address.request()
    data_store.suite["new_address_id"]=resp["data"]["address_id"]
    assert resp['code'] == create_address.success_resp["code"]


@step("进行地址切换,地址切换成功检查")
def shift_address_check():
    v2_order_check = Order_check()
    v2_order_check.data["address_id"]=data_store.suite["new_address_id"]
    resp=v2_order_check.request()
    assert resp['code'] == v2_order_check.success_resp["code"]
    assert resp["data"]["address"]["id"]==data_store.suite["new_address_id"]

@step("检查订单结算页正确展示店铺信息和商品信息")
def check_order():
    v2_order_check = Order_check()
    resp = v2_order_check.request()
    order_data=resp["data"]["check_order_items"][0]["goods"][0]["ext_data"]
    assert resp['code'] == v2_order_check.success_resp["code"]
    assert resp["data"]["check_order_items"][0]["mall_info"]["logo"].replace("avatar","") == data_store.suite["v1_logo"].replace("middle","")
    assert resp["data"]["check_order_items"][0]["mall_info"]["name"] == data_store.suite["v1_mall_name"]
    assert order_data["goods_name"]==data_store.suite["settle_goods_name"]
    assert order_data["service_promise_mark"]==data_store.suite["settle_service_promise_mark"]






