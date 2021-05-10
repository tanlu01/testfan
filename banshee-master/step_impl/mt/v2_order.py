from getgauge.python import step, data_store
from api.mt.mt import Mt
import random
from api.mt.order.get_v2_order import V2_Order
from api.mt.order.v2_union_order_order_id_paystatus import V2_Paystatus
from api.mt.order.delete_v2_order_id import Delete_V2_Order_id
from api.mt.order.v2_order_id_cancel import V2_Order_id_Cancel
from api.mt.order.v2_order_id_prepay import V2_Prepay
from api.mt.order.v2_union_order_order_id_detail import V2_Detail
refund_ID = []
order_ID = []


@step("获取订单v2_get, order_status=<order_status>, size=<size>")
def get_v2_order(order_status, size):
    get_v2_order = V2_Order()
    get_v2_order.api = get_v2_order.api.replace("$order_status", order_status)
    get_v2_order.api = get_v2_order.api.replace("$size", size)
    resp = get_v2_order.request()
    for item in resp["data"]["order_items"]:
        if item["goods_list"][0]["goods_sku_id"] == data_store.suite["order_sku_id"]:
            assert item["payment_total"]==data_store.suite['payment_total']
            break
    # 提取refund_id和id
    for item in resp['data']['order_items']:
        refund_ID.append(item['refund_id'])
        order_ID.append(item['id'])


@step("多商品订单根据订单ID获取订单信息, order_id=<order_id>")
def v2_union_order_order_id_detail(order_id):
    v2_order_id_detail = V2_Detail()
    v2_order_id_detail.api = v2_order_id_detail.api.replace(
        "$order_id", order_id)
    v2_order_id_detail.request()
    print(v2_order_id_detail.resp.json())


@step("获取订单的支付状态v2_union_order, order_id=<order_id>")
def v2_union_order_order_id_paystatus(order_id):
    v2_order_id_paystatus = V2_Paystatus()
    v2_order_id_paystatus.api = v2_order_id_paystatus.api.replace(
        "$order_id", order_id)
    v2_order_id_paystatus.request()
    print(v2_order_id_paystatus.resp.json())


@step("删除订单v2, order_id=<order_id>")
def delete_v2_order_id(order_id):
    delete_order_id = Delete_V2_Order_id()
    delete_order_id.api = delete_order_id.api.replace("$order_id", order_id)
    delete_order_id.request()
    print(delete_order_id.resp.json())


@step("取消订单，仅在支付完成前可以取消v2, order_id=<order_id>")
def v2_order_id_cancel(order_id):
    v2_order_id_cancel = V2_Order_id_Cancel()
    v2_order_id_cancel.api = v2_order_id_cancel.api.replace(
        "$order_id", order_id)
    v2_order_id_cancel.request()
    print(v2_order_id_cancel.resp.json())


@step("生成订单预支付信息, 用于接下来的订单支付v2,order_id=<order_id>,platform=<platform>,payment_method=<payment_method>")
def v2_order_id_paystatus(order_id,platform,payment_method):
    order_id_prepay = V2_Prepay()
    order_id= data_store.suite["order_id"] if not order_id else order_id
    order_id_prepay.api = order_id_prepay.api.replace("$order_id", order_id)
    if platform:
        order_id_prepay.data["platform"]=int(platform)
    if payment_method:
        order_id_prepay.data["payment_method"]=int(payment_method)
    resp=order_id_prepay.request()
    assert resp['code'] == 0

## 聊天界面获取订单列表(这里返回的是单个订单列表)    /v2/order/im/order_list
## 聊天界面获取订单列表(这里返回的是15天内的多个订单列表,过滤售后订单)    /v2/order/im/order_list_v2
## 根据某个商品某个地址的邮费    /v2/order/express_