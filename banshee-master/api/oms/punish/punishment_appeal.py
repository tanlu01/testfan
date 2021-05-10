from api.mms.mms_ import Mms


class Punish_appeal(Mms):
    method = 'post'
    api = '/goapi/violations/api/punishment_appeal'
    data = {
        "appeal_images": "",
        "appeal_reason": "",
        "id": 0
    }
    success_resp = {
        'code': 0,
    }
    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }