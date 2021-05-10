from api.oms_new.oms_ import Oms


class Punishment_add_delay(Oms):
    method = 'post'
    api = '/omsapi/mall_punishment/add_test_delay'
    data = {
        "buyer_id":0,
        "goods_id": "",
        "mall_id": 0,
        "number": "",
        "order_id": "",
        "rule_id": "",
        "tab_id": ""
    }
    success_resp = {
        'code': 0,
    }
    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }