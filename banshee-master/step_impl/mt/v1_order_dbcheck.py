from getgauge.python import step, data_store
from api.mt.mt import Mt
from models.mt.mt_payment import Payment as PaymentModel
from models.mt.pt_order import MtOrder as MtOrderModel
from api.mt.refund.mock_order_refund import MockOrderRefund
import time
refund_ID = []
order_ID = []
# aftersale_ID = '1'
# logistic_ID = '1'

payment_method_dict = {
        0: [0,1,7,8,11,12,13,14,17,18,19,20], #20.mock pay
        9: [9],
        3: [3]
    }

platform_dict ={
    50: [1]
}

@step("支付成功后,订单表字段check,order_id=<order_id>")
def order_check(order_id):
    order_id = data_store.suite['order_id'] if not order_id else order_id
    mtorder = MtOrderModel.get(id=data_store.suite['order_id'])

    assert mtorder.platform in platform_dict[data_store.suite['platform']]
    #assert mtorder.payment_method in payment_method_dict[data_store.suite['payment_method']]
    assert mtorder.payment_method == 20 #mock的type

    assert mtorder.payment_total == data_store.suite['payment_total']
    assert mtorder.payment_fee == (int(data_store.suite['cost']))*0.006 #有结算价，商家实收=结算价;等于实收*0.6%
    assert mtorder.service_fee == int(data_store.suite['cost']) #有结算价，即结算价;无结算价,乘以佣金比例;无佣金，是0
    assert mtorder.process_status == 4  #4:待发货


@step("支付成功后,支付表字段check,order_id=<order_id>")
def payment_check(order_id):
    order_id = data_store.suite['order_id'] if not order_id else order_id
    payment = PaymentModel.get(order_id=data_store.suite['order_id'])
    
    #assert payment.type in payment_method_dict[data_store.suite['payment_method']]
    assert payment.type == 20  #mock的type
    assert payment.platform in platform_dict[data_store.suite['platform']]
    assert payment.status == 1  #1.支付成功
    

@step("发货成功后,订单表字段check,order_id=<order_id>")
def deliverorder_check(order_id):
    order_id = data_store.suite['order_id'] if not order_id else order_id
    mtorder = MtOrderModel.get(id=data_store.suite['order_id'])

    assert mtorder.process_status == 5 #5:待签收
