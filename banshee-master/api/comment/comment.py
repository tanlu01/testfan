from api.mms.mms_ import Mms


class Mms_comment(Mms):
    method = 'post'
    api = '/goapi/gomms/api/comment/list'
    data = {
            "page":1,
            "size":20,
            "from_review_time":"",
            "to_review_time":"",
            "tag_ids":[],
            "review_text":"",
            "goods_id":0,
            "order_id":"",
            "auto":{"value":3}
            }

    message={
            "buyer_name": "150****5258",
            "review_text": "好",
            "description_rating": 5,
            "response_text": "哈哈哈"
    }
    success_resp = {
        'code': 0
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
