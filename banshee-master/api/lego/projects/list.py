from api.lego.lego import Lego


class List(Lego):
    method = 'get'
    api = '/api/lego/projects'
    data = {
        'name': None,
        'start_time': 0,
        'end_time': 0,
        'creator': None,
        'page': 1,
        'size': 10
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
