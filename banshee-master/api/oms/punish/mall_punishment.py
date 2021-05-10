from api.oms_new.oms_ import Oms
import time

class Mall_punishment(Oms):
    method = 'get'
    api = '/omsapi/mall_punishment/list?tab_id=2'
    data   = {

    }
    success_resp = {
        'code': 0
    }
    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }