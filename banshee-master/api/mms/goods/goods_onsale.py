from api.mms.mms_ import Mms


class Batchonsale(Mms):
    method = 'post'
    api = '/api/goods/goods/batchonsale'
    data = {
        "goods_ids":"",
         "is_onsale":1
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }