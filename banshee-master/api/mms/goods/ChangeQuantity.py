from api.mms.mms_ import Mms


class ChangeSkuQuantity(Mms):
    method = 'post'
    api = '/api/goods/changeSkuQuantity'
    data = {
        "change_quantity": {}
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }