from api.oms.oms_ import Oms
import time

class Mallpunishmentrecord(Oms):
    method = 'get'
    api = '/mallpunishmentrecord/search?mall_id=&type=&status=&detail=&create_at=$create_at&perpage=20&page=1'
    data   = {

    }
    success_resp = {
        'code': 0,
    }
    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }