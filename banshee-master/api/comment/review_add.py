from api.mms.mms_ import Mms


class Review_add(Mms):
    method = 'post'
    api = '/api/Reviews/add'
    data = {
        "review_id":"",
        "merchant_views":""
        }

    success_resp = {
        'code': 0
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
