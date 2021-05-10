from api.mt.mt import Mt

 
class Complain(Mt):
    method = 'post'
    api = '/v1/refund/$refund_id/complain'
    data = {
        "reason_id": 0,
        "remark_imgs": [
            ""
        ],
        "remark_text": "",
        "tag_ids": [
            0
        ]
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
