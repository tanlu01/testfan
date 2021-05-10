from getgauge.python import step, data_store
from api.mt.pay.order import OrderV2
from api.mt.pay.payment_channel_status import PaymentChannelStatus
from api.mt.pay.ali_marketing_consult import AliMarketingConsult


@step("获取订单列表,获取<num>条数据")
def v2_order(num):
    order_v2 = OrderV2()
    order_v2.data['size'] = num
    order_v2.request()
    assert order_v2.error_resp.items() <= order_v2.resp.json().items()


@step("商品支付页面,通过商品id=<goods_id>获取支付通道")
def payment_channel_status(goods_id):
    payment_channel_status = PaymentChannelStatus()
    goods_id = data_store.suite['goods_id'] if not goods_id else goods_id
    payment_channel_status.data['goods_id'] = int(goods_id)
    payment_channel_status.data['goods_list'].append(int(goods_id))
    resp = payment_channel_status.request()
    assert resp['code'] == payment_channel_status.success_resp['code']
    for method in resp['data']['payment_methods']:
        assert method['title'] == payment_channel_status.payment_method[method['payment_method']]

    data_store.suite['payment_method'] = resp['data']['payment_methods'][0]['payment_method']


@step("查询支付营销文案等信息,通过<mobile>和<price>")
def ali_marketing_consult(mobile, price):
    ali_marketing_consult = AliMarketingConsult()
    ali_marketing_consult.data['mobile'] = mobile
    ali_marketing_consult.data['order_payment_total'] = int(price)

    resp = ali_marketing_consult.request()

    assert resp['code'] == ali_marketing_consult.success_resp['code']
