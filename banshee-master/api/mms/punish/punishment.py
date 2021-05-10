from api.mms.mms_ import Mms


class Punishment(Mms):
    method = 'get'
    api = '/goapi/violations/api/punishment?page=1&size=20&type={"value":$type}'
    data = {

           }
    success_resp = {
        'code': 0,
    }
    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }