from getgauge.python import step, data_store
from api.mms.refund.agree_refund import AgreeRefundV2
from models.mt.pt_order import MtOrder as MtOrderModel
from models.mt.mt_payment import PaymentRefund as PaymentRefundModel


@step("MMS商家同意退款,order_id=<order_id>")
def agree_refund_v2(order_id):
    agree_refund_v2 = AgreeRefundV2()
    order_id = data_store.suite['order_id'] if not order_id else order_id
    agree_refund_v2.data['order_id'] = order_id
    resp = agree_refund_v2.request()
    # print('MMS商家同意退款,', resp)
    assert resp['code'] == 0


@step("获取aftersale_id和payment_refund_id参数用于mock接口退款,order_id=<order_id>")
def get_aftersaleId_refundId(order_id):
    if order_id:
        data = MtOrderModel.get(id=int(order_id))
        data_store.suite['aftersale_id'] = data.aftersale_id

    data = PaymentRefundModel.get(aftersale_id=data_store.suite['aftersale_id'])
    # print('payment_refund_id', data.id)
    data_store.suite['payment_refund_id'] = data.id
