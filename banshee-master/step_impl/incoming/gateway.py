from getgauge.python import step, data_store
from api.incoming.gateway.iap_verify import IapVerify
from api.incoming.gateway.iap_order import IapOrder
from api.incoming.gateway.coupon_pay import CouponPay

@step("iap-预支付订单, order_no=<order_no> transaction_id=<transaction_id> receipt_data=<receipt_data>")
def iap_verify(order_no, transaction_id, receipt_data):
    iap_order = IapOrder()
    resp = iap_order.request()

@step("iap-验证票据, order_no=<order_no> transaction_id=<transaction_id> receipt_data=<receipt_data>")
def iap_verify(order_no, transaction_id, receipt_data):
    iap_verify = IapVerify()
    resp = iap_verify.request()

@step("优惠支付")
def coupon_pay():
    coupon_pay = CouponPay()
    coupon_pay.data['token'] = '4896yi4ZtqJGz0MDFcS8ZX4APcqRbvJyJic_7a-V2bWgp6hA4KnKwLuqQrVIYBwta7dFLXPDojPDxWBNqWCE9FDaM3sjYUFfnD7GDtBtfl_vZAJTFIM'
    resp = coupon_pay.request()
    # print(resp)