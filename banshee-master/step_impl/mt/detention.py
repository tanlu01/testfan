from getgauge.python import step, data_store
from api.mt.mt import Mt
from api.mt.detention.detention import During_pay, Order_cancel


@step("订单取消挽留during_pay接口, goods_id=<goods_id>, sku_id=<sku_id>, order_id=<order_id>")
def during_pay(goods_id, sku_id, order_id):
    during_pay = During_pay()
    during_pay.data['goods_info']['goods_id'] = int(goods_id)
    during_pay.data['goods_info']['sku_id'] = int(sku_id)
    during_pay.data['order_id'] = order_id
    during_pay.request()
    print(during_pay.resp.json())
# 不是订单取消挽留接口，猜测是支付中接口


@step("订单取消挽留order_cancel接口, goods_id=<goods_id>, sku_id=<sku_id>, order_id=<order_id>")
def order_cancel(goods_id, sku_id, order_id):
    order_cancel = Order_cancel()
    order_cancel.data['goods_info']['goods_id'] = int(goods_id)
    order_cancel.data['goods_info']['sku_id'] = int(sku_id)
    order_cancel.data['order_id'] = order_id
    # print(order_cancel.data)
    order_cancel.request()
    print(order_cancel.resp.json())
