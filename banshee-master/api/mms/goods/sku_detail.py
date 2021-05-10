from api.mms.mms_ import Mms


class SkuDetail(Mms):
    method = 'get'
    api = '/api/goods/getSkuDetail?goods_id=$goods_id'
    data = {

    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }