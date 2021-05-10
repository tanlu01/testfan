from api.mms.mms_ import Mms


class OrderCount(Mms):
    method = 'get'
    api = '/api/order/orderListTab'
    data = {}

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
