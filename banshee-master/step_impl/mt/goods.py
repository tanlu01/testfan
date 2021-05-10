from getgauge.python import step, data_store
from api.mt.goods.order_info import OrderInfo
from api.mt.goods.goods import Goods
from api.mt.goods.connect_share import Connect_share
from api.mt.goods.discount import Discount
from api.mt.goods.group_orders import Group_orders
from api.mt.goods.notice import Notice
from api.mt.goods.review_template import Review_template
from api.mt.goods.reviews import Reviews
from api.mt.goods.reviews_list import Reviews_list
from api.mt.goods.share_params import Share_params
from api.mt.goods.goods_v2 import Goods_v2
from api.mt.goods.brief import Brief
from api.mt.goods.extra import Extra
from api.mt.goods.reviews_v2 import Reviews_v2
from api.mt.goods.skus import Skus


@step("获取商品详情,商品id=<goods_id>")
def goods(goods_id):
    goods_id = data_store.suite['goods_id'] if not goods_id else goods_id
    data_store.suite['goods_id_punish'] = goods_id
    data_store.suite['goods_id'] = goods_id
    goods = Goods()
    goods.api = goods.api.replace('$goods_id', str(goods_id))
    resp = goods.request()

    assert resp['code'] == 0

    data_store.suite['goods_id_punish'] = goods_id
    data_store.suite.setdefault('sku_info', {}).update(
        {'sku_id': resp['data']['skus'][0]['sku_id'], 'normal_price': resp['data']['skus'][0]['normal_price']})


@step("获取商品下单时的信息, goods_id=<goods_id>")
def goods_order_info(goods_id):
    order_info = OrderInfo()
    order_info.api = order_info.api.replace('$goods_id', goods_id)
    resp=order_info.request()
    assert resp['code']==order_info.success_resp["code"]


@step("连接商品和mopenid, goods_id=<goods_id>")
def connect_share(goods_id):
    connect_share = Connect_share()
    connect_share.api = connect_share.api.replace("$goods_id", goods_id)
    connect_share.request()
    print(connect_share.resp.json())


@step("获取商品优惠详情, goods_id=<goods_id>")
def discount(goods_id):
    discount = Discount()
    discount.api = discount.api.replace("$goods_id", goods_id)
    discount.request()
    print(discount.resp.json())


@step("获取商品的最近N条订单, goods_id=<goods_id>")
def group_orders(goods_id):
    group_orders = Group_orders()
    group_orders.api = group_orders.api.replace("$goods_id", goods_id)
    group_orders.request()
    print(group_orders.resp.json())


@step("通知bar有交互时，需要刷新调用该接口, goods_id=<goods_id>")
def notice(goods_id):
    notice = Notice()
    notice.api = notice.api.replace("$goods_id", goods_id)
    notice.request()
    print(notice.resp.json())


@step("获取评论模板(配置)信息, goods_id=<goods_id>")
def review_template(goods_id):
    review_template = Review_template()
    review_template.api = review_template.api.replace("$goods_id", goods_id)
    review_template.request()
    print(review_template.resp.json())


@step("商品详情页获取商品评价情况信息, goods_id=<goods_id>")
def reviews(goods_id):
    reviews = Reviews()
    reviews.api = reviews.api.replace("$goods_id", goods_id)
    reviews.request()
    print(reviews.resp.json())


@step("商品评价情况信息列表, goods_id=<goods_id>")
def reviews_list(goods_id):
    reviews_list = Reviews_list()
    reviews_list.api = reviews_list.api.replace("$goods_id", goods_id)
    reviews_list.request()
    print(reviews_list.resp.json())


@step("获取分享图片的参数信息, goods_id=<goods_id>")
def share_params(goods_id):
    share_params = Share_params()
    share_params.api = share_params.api.replace("$goods_id", goods_id)
    share_params.request()
    print(share_params.resp.json())


@step("商品详情页的接口v2, goods_id=<goods_id>")
def goods_v2(goods_id):
    goods_v2 = Goods_v2()
    goods_v2.api = goods_v2.api.replace("$goods_id", goods_id)
    resp = goods_v2.request()
    assert resp['code'] == goods_v2.success_resp['code']
    data_store.suite["goods_detail"]= resp
    data_store.scenario.setdefault('goods_v2', {}).update(
        {"product_information": resp['data']['ui_elements']['product_information']})
    data_store.suite["settle_goods_name"]=resp["data"]["goods_name"]
    data_store.suite["settle_service_promise_mark"]=resp["data"]["service_promise_mark"]



@step("商品sku简化详情页的接口, goods_id=<goods_id>")
def brief(goods_id):
    brief = Brief()
    brief.api = brief.api.replace("$goods_id", goods_id)
    brief.request()
    print(brief.resp.json())


@step("获取商详扩展信息, goods_id=<goods_id>, activity_id=<activity_id>")
def extra(goods_id, activity_id):
    extra = Extra()
    extra.api = extra.api.replace("$goods_id", goods_id)
    extra.api = extra.api.replace("$activity_id", activity_id)
    extra.request()
    print(extra.resp.json())


@step("商品详情页获取商品评价情况信息v2, goods_id=<goods_id>")
def reviews_v2(goods_id):
    reviews_v2 = Reviews_v2()
    reviews_v2.api = reviews_v2.api.replace("$goods_id", goods_id)
    reviews_v2.request()
    print(reviews_v2.resp.json())


@step("商品skus的接口, goods_id=<goods_id>")
def skus(goods_id):
    skus = Skus()
    skus.api = skus.api.replace("$goods_id", goods_id)
    skus.request()
    print(skus.resp.json())
