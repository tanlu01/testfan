from getgauge.python import step, data_store
from api.mt.mt import Mt
from api.mt.favorite.post_goods_like import Post_goods_like
from api.mt.favorite.post_goods_id import Post_goods_id
from api.mt.favorite.delete_goods_id import Delete_goods_id
from api.mt.favorite.get_goods_list import Get_goods_list
from api.mt.favorite.get_goods_list_id import Goods_list_Id
from api.mt.favorite.post_malls_like import Post_malls_like
from api.mt.favorite.delete_malls_like import Delete_malls_like
from api.mt.favorite.get_malls_list import Get_malls_list
from api.mt.favorite.get_malls_list_id import Malls_list_Id


@step("批量收藏商品, goods_id=<goods_id>")
def post_goods_like(goods_id):
    post_goods_like = Post_goods_like()
    post_goods_like.data['goods_ids'] = [goods_id]
    # print(post_goods_like.data)
    post_goods_like.request()
    print(post_goods_like.resp.json())


@step("收藏商品, goods_id=<goods_id>")
def post_goods_id(goods_id):
    post_goods_id = Post_goods_id()
    post_goods_id.api = post_goods_id.api.replace("$goods_id", goods_id)
    post_goods_id.request()
    print(post_goods_id.resp.json())


@step("取消收藏商品, goods_id=<goods_id>")
def delete_goods_id(goods_id):
    delete_goods_id = Delete_goods_id()
    delete_goods_id.api = delete_goods_id.api.replace("$goods_id", goods_id)
    delete_goods_id.request()
    print(delete_goods_id.resp.json())


@step("收藏的商品列表接口")
def get_goods_list():
    get_goods_list = Get_goods_list()
    get_goods_list.request()
    print(get_goods_list.resp.json())


@step("收藏的商品id列表接口")
def get_goods_list_id():
    goods_list_id = Goods_list_Id()
    goods_list_id.request()
    print(goods_list_id.resp.json())


@step("收藏店铺, mall_id=<mall_id>")
def post_malls_like(mall_id):
    post_malls_like = Post_malls_like()
    post_malls_like.api = post_malls_like.api.replace("$mall_id", mall_id)
    post_malls_like.request()
    print(post_malls_like.resp.json())


@step("取消收藏店铺, mall_id=<mall_id>")
def delete_malls_like(mall_id):
    delete_malls_like = Delete_malls_like()
    delete_malls_like.api = delete_malls_like.api.replace("$mall_id", mall_id)
    delete_malls_like.request()
    print(delete_malls_like.resp.json())


@step("收藏的店铺列表接口")
def get_malls_list():
    get_malls_list = Get_malls_list()
    get_malls_list.request()
    print(get_malls_list.resp.json())


@step("收藏的店铺id列表接口")
def get_malls_list_id():
    malls_list_id = Malls_list_Id()
    malls_list_id.request()
    print(malls_list_id.resp.json())
