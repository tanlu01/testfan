from api.mms.mms_ import Mms


class ActivityPunish(Mms):
    method = 'get'
    api = '/api/promotion/schedule/activityPunish'
    data = {}

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
