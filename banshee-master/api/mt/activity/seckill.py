from api.mt.mt import Mt


class Seckill(Mt):
    method = 'get'
    api = '/v1/activity/seckill/$activity_id'
    data = {
        'serie_id': '',
        'act_type': 3
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
