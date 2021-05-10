from api.oms.oms_ import Oms
import time

class Punishmentrule_search(Oms):
    method = 'get'
    api = '/mallpunishmentrule/search?title=&type=&status=&perpage=20&page=1'
    data   = {
    }
    success_resp = {
        'code': 0,
    }
    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }