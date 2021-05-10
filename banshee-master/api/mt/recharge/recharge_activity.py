from api.mt.mt import Mt


class Recharge_Activity(Mt):
    method = 'get'
    api = '/v1/recharge/activity/$activity_id'
    data = {}


    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }

