from api.mt.mt import Mt


class Prime(Mt):
    method = 'get'
    api = '/v1/prime/profile'
    data = {}

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
