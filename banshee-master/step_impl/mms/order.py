from getgauge.python import step, data_store
from api.mms.order.order_count import OrderCount
import time


@step("获取各订单状态的数量")
def order_count():
    order_count = OrderCount()

    time.sleep(10) if data_store.suite.get('order_count_wait_time', False) else ''

    resp = order_count.request()
    assert resp['code'] == 0

    wait_deliver = data_store.suite.get('wait_deliver', False)
    wait_sign = data_store.suite.get('wait_sign', False)
    # 前置操作，保存各状态数量
    if not wait_deliver:
        data_store.suite['wait_deliver'] = resp['payload']['wait_deliver']
        data_store.suite['wait_sign'] = resp['payload']['wait_sign']
        data_store.suite['order_count_wait_time'] = True
    else:
        times = 3
        while times > 0:
            try:
                # 调用mock_order_pay接口
                if data_store.suite.get('mock_order_pay', False):
                    assert resp['payload']['wait_deliver'] == wait_deliver + 1
                    assert resp['payload']['wait_sign'] == wait_sign
                    data_store.suite['wait_deliver'] += 1
                    del data_store.suite['mock_order_pay']
                # 调用发货接口
                elif data_store.suite.get('deliver', False):
                    assert resp['payload']['wait_deliver'] == wait_deliver - 1
                    assert resp['payload']['wait_sign'] == wait_sign + 1
                    del data_store.suite['deliver']
            except Exception as e:
                print(e)
                resp = order_count.request()
                assert resp['code'] == 0
                times -= 1
            else:
                times = 0
