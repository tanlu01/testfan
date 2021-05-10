from getgauge.python import step, data_store
from api.oms_new.order.order_list import OrderList


@step("获取新OMS订单列表")
def order_list():
    order_list = OrderList()

    resp = order_list.request()

    assert resp['code'] == 0

    print(resp)
