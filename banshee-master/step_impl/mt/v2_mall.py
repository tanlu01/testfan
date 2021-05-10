from getgauge.python import step, data_store
from api.mt.mt import Mt
import urllib
from api.mt.v2_mall.category import Category
from api.mt.v2_mall.coupons import Coupons
from api.mt.v2_mall.expo import Expo
from api.mt.v2_mall.goods import Goods
from api.mt.v2_mall.info import Info_Goods_id, V2_mall_info
from api.mt.v2_mall.recommend import Recommend


@step("获取宝贝分类, mall_id=<mall_id>")
def category(mall_id):
    category = Category()
    category.api = category.api.replace("$mall_id", mall_id)
    category.request()
    print(category.resp.json())


@step("获取当前店铺所有优惠券v2, mall_id=<mall_id>")
def coupons(mall_id):
    coupons = Coupons()
    coupons.api = coupons.api.replace("$mall_id", mall_id)
    coupons.request()
    print(coupons.resp.json())


@step("店铺博览, mall_id=<mall_id>")
def expo(mall_id):
    expo = Expo()
    expo.api = expo.api.replace("$mall_id", mall_id)
    # product_information参数编码
    expo.api = expo.api.replace("$product_information", urllib.parse.quote(
        data_store.scenario['goods_v2']['product_information']))
    expo.request()
    print(expo.resp.json())


@step("获取宝贝分类的商品列表, mall_id=<mall_id>")
def goods(mall_id):
    goods = Goods()
    goods.api = goods.api.replace("$mall_id", mall_id)
    goods.request()
    print(goods.resp.json())


@step("店铺信息v2, mall_id=<mall_id>")
def mall_info(mall_id):
    mall_info = V2_mall_info()
    mall_info.api = mall_info.api.replace("$mall_id", mall_id)
    resp=mall_info.request()
    assert resp['code'] ==mall_info.success_resp["code"]
    data_store.suite["v1_mall_name"]=resp["data"]["mall_name"]
    data_store.suite["v1_logo"] = resp["data"]["logo"]



@step("店铺信息v2_goods_id, mall_id=<mall_id>, goods_id=<goods_id>")
def info_goods_id(mall_id, goods_id):
    info_goods_id = Info_Goods_id()
    info_goods_id.api = info_goods_id.api.replace("$mall_id", mall_id)
    info_goods_id.api = info_goods_id.api.replace("$goods_id", goods_id)
    info_goods_id.request()
    print(info_goods_id.resp.json())


@step("客服物流详情商品推荐, mall_id=<mall_id>")
def recommend(mall_id):
    recommend = Recommend()
    recommend.api = recommend.api.replace("$mall_id", mall_id)
    recommend.request()
    print(recommend.resp.json())
