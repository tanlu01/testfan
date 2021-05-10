from api.oms_new.oms_ import Oms


class List(Oms):
    method = 'get'
    api = '/omsapi/special/list'
    data = {'state': 2}

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
