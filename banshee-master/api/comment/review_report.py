from api.mms.mms_ import Mms


class Review_report(Mms):
    method = 'post'
    api = '/api/order/review/report'
    data = {
            "id":"1000096992",
            "reason_id":1,
            "evidence":[],
            "extra_note":"不能上传广告"
            }

    success_resp = {
        'code': 0
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
