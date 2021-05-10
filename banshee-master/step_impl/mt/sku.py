from getgauge.python import step, data_store

from api.mt.cart.cart_sku import CartSku
from api.mt.cart.delete_cart_sku import Delete_cart_sku
from api.mt.cart.shopping_cart import ShoppingCart
from api.mt.goods.goods_v2 import Goods_v2
from api.mt.order.order_check_tips import Tips
from api.mt.order.v1_order_check import OrderCheckV1



@step("得到goods=<goods_id>,尺码=<size>,颜色=<colour>商品的sku")
def get_sku(goods_id,size,colour):
    resp = data_store.suite["goods_detail"]
    data_store.spec["goods_id"] = goods_id
    data_store.spec["mall_id"] = resp['data']["mall_id"]
    for sku in resp['data']["skus"]:
        if sku["specs"][0]["spec_value"]==str(size) and sku["specs"][1]["spec_value"]==str(colour):
            data_store.spec["sku_id"]=sku["sku_id"]
            data_store.spec["sku_price"]= sku["normal_price"]
            data_store.spec["thumb_url"]=sku["thumb_url"]
            data_store.spec["size"]=str(size)
            data_store.spec["color"]=str(colour)


@step("移除购物车, goods_id=<goods_id>")
def delete_cart_sku(goods_id):
    delete_cart_sku = Delete_cart_sku()
    sku_id = data_store.spec["sku_id"]
    delete_cart_sku.data['goods_sku_ids'][0]['goods_id'] = goods_id
    delete_cart_sku.data['goods_sku_ids'][0]['sku_id'] = int(sku_id)
    delete_cart_sku.data['sku_ids'] = [int(sku_id)]
    resp=delete_cart_sku.request()
    assert resp["code"] == delete_cart_sku.success_resp['code']

@step("获取购物车数据, size_id=<size_id>")
def get_v1_cart(size_id):
    get_v1_cart = ShoppingCart()
    get_v1_cart.api = get_v1_cart.api.replace("$size_id",size_id)
    resp=get_v1_cart.request()
    assert resp["code"] == ShoppingCart.success_resp['code']
    data_store.spec["cart"]=resp


@step("判断购物车中商品规格、数量与选择一致，勾选商品结算价与商详页价格一致")
def check_cart():
    resp=data_store.spec["cart"]
    assert resp["data"]["items"][0]["goods"][0]['goods_id']==data_store.spec["goods_id"]
    desc=resp["data"]["items"][0]["goods"][0]['sku_desc']
    assert desc.find(data_store.spec["size"])>=0
    assert desc.find(data_store.spec["color"])>=0
    assert resp["data"]["items"][0]["goods"][0]['sku_price']==data_store.spec["sku_price"]
    assert int(resp["data"]["items"][0]["goods"][0]['quantity'])==int(data_store.spec['quantity'])


@step("订单校验,quantity=<quantity>")
def order_check(quantity):
    order_check_v1=OrderCheckV1()
    order_check_v1.data['address_id'] = data_store.suite['address_id']
    order_check_v1.data["goods_id"] = int(data_store.spec["goods_id"])
    order_check_v1.data['goods_sku_id'] = data_store.spec["sku_id"]
    order_check_v1.data['goods_quantity']= int(quantity)
    resp =order_check_v1.request()
    assert resp["data"]["order"]["goods_unit_price"]==data_store.spec["sku_price"]
    assert resp["data"]["order"]["goods_quantity"] == int(quantity)
















