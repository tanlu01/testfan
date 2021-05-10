from api.oms_new.oms_ import Oms


class Menu(Oms):
    method = 'get'
    api = '/omsapi/user/menu'
    data = {
        "module": "rock"
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
