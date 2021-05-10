from getgauge.python import step, data_store

from api.mt.cart.cart_sku import CartSku
from api.mt.mt import Mt
from api.mt.cart.pre_order import GetPreOrder, PostPreOrder
from api.mt.cart.shopping_cart import ShoppingCart  # 获取购物车数据
from api.mt.cart.discount import Discount_v1, Discount_v2  # 计算购物车的商品优惠
from api.mt.cart.goods_promotion import Goods_promotion  # 修改购物车商品促销

from api.mt.cart.sku_count import Sku_count
from api.mt.cart.delete_cart_sku import Delete_cart_sku


@step("从购物车获取店铺和商品信息")
def get_pre_order():
    get_pre_order = GetPreOrder()
    get_pre_order.request()
    # TODO: 要先下单才能有返回店铺和商品信息
    print(get_pre_order.resp.json())


@step("购物车准备下单")
def post_pre_order():
    post_pre_order = PostPreOrder()
    post_pre_order.request()
    # TODO: 可以直接在req body里添加购买信息，直接支付，断开下单流程
    print(post_pre_order.resp.json())



@step("计算购物车的商品优惠v1")
def post_cart_discount():
    post_cart_discount = Discount_v1()
    post_cart_discount.request()
    print(post_cart_discount.resp.json())


@step("修改购物车商品促销")
def cart_goods_promotion():
    cart_goods_promotion = Goods_promotion()
    cart_goods_promotion.request()
    print(cart_goods_promotion.resp.json())

@step("加入购物车,mall_id=<mall_id>,goods_id=<goods_id>,sku_id=<sku_id>,quantity=<quantity>,flag=<flag>")
def post_cart_sku(mall_id,goods_id,sku_id,quantity,flag):
    cart_sku = CartSku()
    cart_sku.data['mall_id'] = data_store.spec["mall_id"] if not mall_id else int(mall_id)
    cart_sku.data['goods_id'] = goods_id
    cart_sku.data['sku_id'] = data_store.spec["sku_id"] if not sku_id else int(sku_id)
    if flag=="1":
        cart_sku.data["quantity"] = int(quantity)
        cart_sku.data["sku_price"]= data_store.spec["sku_price"]
        cart_sku.data["sku_thumb_url"] = data_store.spec["thumb_url"]
    resp=cart_sku.request()
    assert resp["code"] == cart_sku.success_resp['code']
    data_store.spec['quantity'] = quantity


@step("增减购物车")
def cart_sku_count():
    cart_sku_count = Sku_count()
    cart_sku_count.request()
    print(cart_sku_count.resp.json())


@step("计算购物车的商品优惠v2")
def post_cart_discount():
    post_cart_discount = Discount_v2()
    post_cart_discount.request()
    print(post_cart_discount.resp.json())
