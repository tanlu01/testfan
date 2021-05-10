from api.oms.oms_ import Oms
import time

class Handlepunishmenth(Oms):
    method = 'post'
    api = '/mallpunishmentrecord/handlepunishment'
    data = {
        "record_id":0,
        "status": "",
        "confirm": "yes",
        "info":"",
        "images": []
    }
    success_resp = {
        'code': 0,
    }
    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }