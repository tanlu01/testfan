from api.mt.mt import Mt


class Add_order_review(Mt):
    method = 'post'
    api = '/v1/order/$order_id/review'
    data = {
        "description_rating":5,
        "is_anonymous":False,
        "is_default":False,
        "package_rating":5,
        "review_imgs":[],
        "review_text":"好",
        "review_type":0,
        "review_videos":[],
        "service_rating":5,
        "shipping_rating":5
    }
    success_rsp={
        "code":0
    }
    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }

    # expected_schema = {
    #     "$schema": "http://json-schema.org/draft-06/schema#",
    #     "title": "expected_data",
    #     "type": "object",
    #     "required": [
    #         "code",
    #         "time",
    #         "data"
    #     ],
    #     "properties": {
    #         "code": {
    #             "type": "number"
    #         },
    #         "time": {
    #             "type": "number"
    #         },
    #         "data": {
    #             "type": "object",
    #             "required": [
    #                 "order_id",
    #                 "order_status",
    #                 "activity_id"
    #             ],
    #             "properties": {
    #                 "order_id": {
    #                     "type": "string"
    #                 },
    #                 "order_status": {
    #                     "type": "number"
    #                 },
    #                 "activity_id": {
    #                     "type": "number"
    #                 }
    #             }
    #         }
    #     }
    # }
