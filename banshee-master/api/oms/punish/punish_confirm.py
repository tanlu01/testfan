from api.oms_new.oms_ import Oms
import time

class Punishment_confirm(Oms):
    method = 'post'
    api = '/omsapi/mall_punishment/batch_confirm'
    data = {
    "tab_id": "2",
    "reason": "确认",
    "selected":[
        {

        }
    ]
    }
    success_resp = {
        'code0': 0,
        'code1': 1,
    }
    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }