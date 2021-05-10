from getgauge.python import step, data_store
from api.mt.mt import Mt
from api.mt.order.aftersale_process import Process
from api.mt.order.aftersal_reason_tree import Reason_tree
from api.mt.order.get_v1_order import V1_Order
from api.mt.order.get_order_id import Get_Order_id
from api.mt.order.delete_v1_order_id import Delete_V1_Order_id
from api.mt.order.v1_order_id_cancel import V1_Order_id_Cancel
from api.mt.order.order_id_refund import OrderIdRefund
from api.mt.order.order_id_delaysign import Delaysign
from api.mt.order.order_id_discount import Discount
from api.mt.order.order_id_gift import Gift
from api.mt.order.order_id_goods_summary import Goods_Smmary
from api.mt.order.order_id_logistic import Logistic
from api.mt.order.order_id_lottery import Lottery
from api.mt.order.order_id_logistic_logistic_id import Logistic_Logistic_id
from api.mt.order.order_id_lottery_open import Lottery_Open
from api.mt.order.order_id_paystatus import Paystatus
from api.mt.order.v1_order_id_prepay import V1Prepay
from api.mt.order.order_id_urge import Urge
from api.mt.order.order_id_sign import Sign
from api.mt.order.order_id_rewards import Rewards
from api.mt.order.order_id_reviews import Reviews
from api.mt.order.compensation_expensive_info import Expensive_info
from api.mt.order.compensation_expensive_process import Expensive_process
from api.mt.order.order_update_real_name import Update_real_name
from api.mt.order.order_update_address import Update_address
from api.mt.order.add_order_review import Add_order_review
from api.mt.order.order_refund_popup import Refund_popup
from api.mt.order.order_detail import OrderDetail
from api.mt.order.review_order_sucess import ReviewSucess
from api.mt.pay.mock_order_pay import MockOrderPay
from models.mt.mt_payment import Payment as PaymentModel
from models.mt.pt_order import MtOrder as MtOrderModel
from api.mt.refund.mock_order_refund import MockOrderRefund
import time
refund_ID = []
order_ID = []
# aftersale_ID = '1'
# logistic_ID = '1'


@step("订单退货包运费进度信息, refund_id=<refund_id>")
def aftersal_reason_treefree_refund_exp_process(refund_id):
    process = Process()
    process.data['refund_id'] = refund_id
    process.request()
    print(process.resp.json())


@step("商品分类售后原因, refund_id=<refund_id>")
def aftersal_reason_tree(refund_id):
    reason_tree = Reason_tree()
    reason_tree.data['refund_id'] = refund_id
    reason_tree.request()
    print(reason_tree.resp.json())


@step("获取订单v1_get, order_status=<order_status>, size=<size>")
def get_v1_order(order_status, size):
    get_v1_order = V1_Order()
    get_v1_order.api = get_v1_order.api.replace("$order_status", order_status)
    get_v1_order.api = get_v1_order.api.replace("$size", size)
    resp = get_v1_order.request()
    # print(get_v1_order.resp.json())

    # 提取refund_id和id
    assert resp['code'] == 0
    for item in resp['data']['list']:
        refund_ID.append(item['refund_id'])
        order_ID.append(item['id'])


@step("查询订单详情, order_id=<order_id>")
def get_order_id(order_id):
    get_order_id = Get_Order_id()
    get_order_id.api = get_order_id.api.replace("$order_id", order_id)
    get_order_id.request()
    print(get_order_id.resp.json())


@step("删除订单v1, order_id=<order_id>")
def delete_v1_order_id(order_id):
    delete_order_id = Delete_V1_Order_id()
    delete_order_id.api = delete_order_id.api.replace("$order_id", order_id)
    resp = delete_order_id.request()
    print(delete_order_id.resp.json())

    assert resp['code'] == 0


@step("取消订单，仅在支付完成前可以取消v1, order_id=<order_id>")
def v1_order_id_cancel(order_id):
    v1_order_id_cancel = V1_Order_id_Cancel()
    v1_order_id_cancel.api = v1_order_id_cancel.api.replace(
        "$order_id", order_id)
    resp = v1_order_id_cancel.request()
    print(v1_order_id_cancel.resp.json())

    # 需要先下单
    assert resp['code'] == 0


@step("买家请求延迟确认收货, order_id=<order_id>")
def order_id_delaysign(order_id):
    order_id_delaysign = Delaysign()
    order_id_delaysign.api = order_id_delaysign.api.replace(
        "$order_id", order_id)
    order_id_delaysign.request()
    print(order_id_delaysign.resp.json())


@step("支付成功的订单用户使用的优惠，包含使用了推币省了多少钱, order_id=<order_id>")
def order_id_discount(order_id):
    order_id_discount = Discount()
    order_id_discount.api = order_id_discount.api.replace(
        "$order_id", order_id)
    order_id_discount.request()
    print(order_id_discount.resp.json())


@step("获取订单的支付后礼包信息, order_id=<order_id>")
def order_id_gift(order_id):
    order_id_gift = Gift()
    order_id_gift.api = order_id_gift.api.replace("$order_id", order_id)
    order_id_gift.request()
    print(order_id_gift.resp.json())


@step("获取订单的商品概要信息, order_id=<order_id>")
def order_id_goods_summary(order_id):
    goods_summary = Goods_Smmary()
    goods_summary.api = goods_summary.api.replace("$order_id", order_id)
    goods_summary.request()
    print(goods_summary.resp.json())


@step("订单的物流详情查询, order_id=<order_id>")
def order_id_logistic(order_id):
    order_id_logistic = Logistic()
    order_id_logistic.api = order_id_logistic.api.replace(
        "$order_id", order_id)
    resp = order_id_logistic.request()
    print(order_id_logistic.resp.json())

    # 提取id，即logistic_id
    assert resp['code'] == 0
    data_store.scenario.setdefault('logistic', {}).update(
        {'logistic_id': resp['data']['items'][0]['id']})
    # logistic_ID = resp['data']['items'][0]['id']


@step("订单物流详情查询-logistic_id, order_id=<order_id>, logistic_id=<logistic_id>")
def order_id_logistic_logistic_id(order_id, logistic_id):
    # 订单物流详情查询 传递
    data_store.scenario['logistic']['logistic_id'] = logistic_id
    logistic_logistic_id = Logistic_Logistic_id()
    logistic_logistic_id.api = logistic_logistic_id.api.replace(
        "$order_id", order_id)
    logistic_logistic_id.api = logistic_logistic_id.api.replace(
        "$logistic_id", logistic_id)
    logistic_logistic_id.request()
    print(logistic_logistic_id.resp.json())


@step("获取订单支付后礼包抽奖信息v1_get, order_id=<order_id>")
def order_id_lottery(order_id):
    order_id_lottery = Lottery()
    order_id_lottery.api = order_id_lottery.api.replace("$order_id", order_id)
    order_id_lottery.request()
    print(order_id_lottery.resp.json())


@step("获取订单支付后礼包抽奖信息v1_post, order_id=<order_id>")
def order_id_lottery_open(order_id):
    lottery_open = Lottery_Open()
    lottery_open.api = lottery_open.api.replace("$order_id", order_id)
    lottery_open.request()
    print(lottery_open.resp.json())


@step("获取订单的支付状态, order_id=<order_id>")
def order_id_paystatus(order_id):
    order_id_paystatus = Paystatus()
    order_id_paystatus.api = order_id_paystatus.api.replace(
        "$order_id", order_id)
    order_id_paystatus.request()
    print(order_id_paystatus.resp.json())


@step("生成订单预支付信息,用于接下来的订单支付v1, order_id=<order_id>,payment_method=<payment_method>,platform=<platform>")
def v1_order_id_paystatus(order_id, payment_method, platform):
    order_id_prepay = V1Prepay()

    order_id = data_store.suite['order_id'] if not order_id else order_id
    payment_method = data_store.suite['payment_method'] if not payment_method else int(payment_method)

    order_id_prepay.data['payment_method'] = payment_method
    order_id_prepay.data['platform'] = data_store.suite.get('platform', 0) if not platform else int(platform)
    order_id_prepay.api = order_id_prepay.api.replace("$order_id", order_id)

    # payment_method_json = order_id_prepay.payment_method_dict.get(payment_method, 0)
    # order_id_prepay.expected_schema['properties']['data']['required'].append(payment_method_json)
    # order_id_prepay.expected_schema['properties']['data']['properties'].update({payment_method_json: {'type': 'string'}})

    resp = order_id_prepay.request()

    assert resp['code'] == 0
    data_store.suite['platform'] = order_id_prepay.data['platform']


@step("db获取payment_id,order_id=<order_id>,flag=<flag>")
def get_payment_id(order_id, flag):
    #如果自己传不要传union
    if flag == "1":
        order_id = data_store.suite['union_order_id'] if not order_id else order_id
    else:
        order_id = data_store.suite['order_id'] if not order_id else order_id
    data = PaymentModel.get(order_id=order_id)
    data_store.suite['payment_id'] = data.id


@step("mock回调支付通知接口,order_id=<order_id>,flag=<flag>")
def mock_order_pay(order_id, flag):
    if flag == "1":
        order_id = data_store.suite['union_order_id'] if not order_id else order_id
        ##union为V2购物车下单的order
    else:
        order_id = data_store.suite['order_id'] if not order_id else order_id
    payment_id = data_store.suite['payment_id']
    mock_order_pay = MockOrderPay()
    mock_order_pay.data['order_id'] = order_id
    mock_order_pay.data['payment_id'] = str(payment_id)
    resp = mock_order_pay.request()
    assert resp['code'] == 0
    data_store.suite['mock_order_pay'] = True


@step("买家申请退款,order_id=<order_id>,refund_amount=<refund_amount>")
def order_id_refund(order_id, refund_amount):
    order_id = data_store.suite['order_id'] if not order_id else order_id

    order_detail() if not data_store.suite.get('payment_total', False) else ''

    order_id_refund = OrderIdRefund()

    refund_amount = data_store.suite['payment_total'] if not refund_amount else refund_amount
    order_id_refund.api = order_id_refund.api.replace("$order_id", order_id)
    order_id_refund.data['refund_amount'] = refund_amount

    times = 4
    while times > 0:
        try:
            resp = order_id_refund.request()
            assert resp['code'] == 0
        except Exception as e:
            print('买家申请退款:', e)
            times -= 1
            print(f'\n等待风控解除锁定状态,共尝试4次,剩余重试次数: {times}次')
            time.sleep(5)
        else:
            #print('买家申请退款:', resp)
            times = 0

    data_store.suite['aftersale_id'] = resp['data']['aftersale_id']
    data_store.suite['refund_amount'] = order_id_refund.data['refund_amount']


@step("mock回调退款通知接口")
def mock_order_refund():
    mock_order_refund = MockOrderRefund()
    mock_order_refund.data['refund_id'] = str(data_store.suite['aftersale_id'])
    mock_order_refund.data['payment_refund_id'] = str(data_store.suite['payment_refund_id'])
    resp = mock_order_refund.request()
    assert resp['code'] == 0


@step("查看订单的评价详情，包括追评, order_id=<order_id>")
def order_id_reviews(order_id):
    order_id_reviews = Reviews()
    order_id_reviews.api = order_id_reviews.api.replace("$order_id", order_id)
    order_id_reviews.request()
    print(order_id_reviews.resp.json())


@step("买家订单评价成功页面，不包含追评, order_id=<order_id>")
def review_order_sucess(order_id):
    review_sucess = ReviewSucess()
    review_sucess.api = review_sucess.api.replace("$order_id", order_id)
    review_sucess.request()
    print(review_sucess.resp.json())


@step("支付成功后给用户的全家桶奖励, order_id=<order_id>")
def order_id_rewards(order_id):
    order_id_rewards = Rewards()
    order_id_rewards.api = order_id_rewards.api.replace("$order_id", order_id)
    order_id_rewards.request()
    print(order_id_rewards.resp.json())


@step("买家确认订单收货, order_id=<order_id>")
def order_id_sign(order_id):
    order_id_sign = Sign()
    order_id = data_store.suite['order_id'] if not order_id else order_id
    order_id_sign.api = order_id_sign.api.replace("$order_id", order_id)
    resp=order_id_sign.request()
    assert resp['code']==order_id_sign.success_resp['code']


@step("买家订单催发货, order_id=<order_id>")
def order_id_urge(order_id):
    order_id_urge = Urge()
    order_id_urge.api = order_id_urge.api.replace("$order_id", order_id)
    order_id_urge.request()
    print(order_id_urge.resp.json())


@step("获取贵必赔服务信息, order_id=<order_id>")
def compensation_expensive_info(order_id):
    expensive_info = Expensive_info()
    expensive_info.api = expensive_info.api.replace("$order_id", order_id)
    expensive_info.request()
    print(expensive_info.resp.json())


@step("获取贵必赔进程信息, order_id=<order_id>")
def compensation_expensive_process(order_id):
    expensive_process = Expensive_process()
    expensive_process.api = expensive_process.api.replace(
        "$order_id", order_id)
    # print(expensive_process.api)
    # print(expensive_process.data)
    expensive_process.request()
    print(expensive_process.resp.json())
    # print(expensive_process.loading_params())


@step("买家更新订单的实名信息，仅报关失败时且在有效期内才能修改, order_id=<order_id>")
def order_update_real_name(order_id):
    update_real_name = Update_real_name()
    update_real_name.api = update_real_name.api.replace("$order_id", order_id)
    update_real_name.request()
    print(update_real_name.resp.json())


@step("买家更新订单的送货地址, order_id=<order_id>")
def order_update_address(order_id):
    update_address = Update_address()
    update_address.api = update_address.api.replace("$order_id", order_id)
    update_address.request()
    print(update_address.resp.json())


@step("买家/卖家添加订单评论, order_id=<order_id>")
def add_order_review(order_id):
    add_order_review = Add_order_review()
    order_id = data_store.suite['order_id'] if not order_id else order_id
    add_order_review.api = add_order_review.api.replace("$order_id", order_id)
    resp=add_order_review.request()
    assert resp['code']==add_order_review.success_rsp['code']


@step("申请售后弹窗, order_id=<order_id>")
def order_refund_popup(order_id):
    refund_popup = Refund_popup()
    refund_popup.api = refund_popup.api.replace("$order_id", order_id)
    refund_popup.request()
    print(refund_popup.resp.json())


@step("获取订单基本信息,order_id=<order_id>")
def order_detail(order_id):
    order_detail = OrderDetail()
    order_id = data_store.suite['order_id'] if not order_id else order_id
    order_detail.api = order_detail.api.replace("$order_id", order_id)
    resp = order_detail.request()
    assert resp['code'] == 0
    data_store.suite['payment_total'] = resp['data']['payment_total']

## 申请贵必赔服务    /v1/order/{order_id}/compensation/expensive/apply
## 获取汇潮支付prepay_id接口    /v1/order/{order_id}/pandora
## 支付成功后给用户的全家桶奖励对应的商品列表的导航栏    /v1/order/{order_id}/reward_goods/nav
# 支付成功后给用户的全家桶奖励对应的商品列表, coupon_id 优惠券id；若不传，则转至 订单推荐 逻辑    /v1​/order​/{order_id}​/reward_goods
