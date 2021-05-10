from api.mms.mms_ import Mms

class Batch_apply(Mms):

    method = 'post'
    api = '/api/promotion/activity/batchApply'
    data = {
        "request_type":2,
        "schedule_id":1150,
        "goods":[]
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
