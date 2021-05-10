from getgauge.python import step, data_store
from api.mt.mt import Mt
from api.mt.recharge.v1_recharge import Recharge
from api.mt.recharge.recharge_activity import Recharge_Activity
from api.mt.recharge.recharge_mobile_area import Mobile_area
from api.mt.recharge.recharge_order import Order
from api.mt.recharge.recharge_order_check import Order_check


@step("充值中心首页数据")
def v1_recharge():
    v1_recharge = Recharge()
    v1_recharge.request()
    # print(v1_recharge.resp.json())


@step("充值中心-查询活动信息, activity_id=<activity_id>")
def recharge_activity_info(activity_id):
    activity_info = Recharge_Activity()
    activity_info.api = activity_info.api.replace('$activity_id', activity_id)
    activity_info.request()
    print(activity_info.resp.json())


@step("充值中心-查询手机号归属")  # 与1请求返回重复
def recharge_mobile_area():
    mobile_area = Recharge()
    mobile_area.request()
    print(mobile_area.resp.json())


@step("充值中心创建一个新订单")  # data参数添加无信息
def recharge_order():
    recharge_order = Order()
    recharge_order.request()
    print(recharge_order.resp.json())


@step("充值中心-下单前检查")  # data参数添加无信息
def recharge_order_check():
    recharge_order_check = Order_check()
    recharge_order_check.request()
    print(recharge_order_check.resp.json())
