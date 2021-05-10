from getgauge.python import step, data_store
from api.mt.mt import Mt
from api.mt.order.order_category import Order_category
from api.mt.order.order_check_tips import Tips
from api.mt.order.tb_account_info import TB_account_info
from api.mt.order.v2_order_check import Order_check


@step("订单分类信息")
def order_category():
    order_category = Order_category()
    order_category.request()
    print(order_category.resp.json())


@step("获取订单页提示信息, goods_id=<goods_id>, sku_id=<sku_id>")
def order_check_tips(goods_id, sku_id):
    order_check_tips = Tips()
    goods_id=data_store.spec["goods_id"] if not goods_id else goods_id
    sku_id=data_store.spec["sku_id"] if not sku_id else sku_id
    order_check_tips.api = order_check_tips.api.replace("$goods_id", goods_id)
    order_check_tips.api = order_check_tips.api.replace("$sku_id", str(sku_id))
    order_check_tips.request()
    print(order_check_tips.resp.json())


@step("TB 账户获取, phone=<phone>")
def tb_account_info(phone):
    tb_account_info = TB_account_info()
    tb_account_info.api = tb_account_info.api.replace("$phone", phone)
    tb_account_info.request()
    print(tb_account_info.resp.json())


