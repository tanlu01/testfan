from api.oms.oms_ import Oms
import time

class Mallpunishmentrule(Oms):
    method = 'post'
    api = '/mallpunishmentrule/addOrEdit'
    data = {
        "id":"",
        "type":0,
        "appeal_status": 1,
        "title": "",
        "detail": "",
        "rule":"",
        "status": 1
    }
    success_resp = {
        'code': 0,
    }
    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }