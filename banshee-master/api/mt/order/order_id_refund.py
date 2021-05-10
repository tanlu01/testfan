from api.mt.mt import Mt


class OrderIdRefund(Mt):
    method = 'post'
    api = '/v1/order/$order_id/refund'
    data = {
        "operator_type": 1,
        "mobile_num": "15021721254",
        "refund_amount": 1,
        "reason_id": 116,
        "refund_type": 0,
        "received": 0,
        "tag_ids": [],
        "remark_text": "",
        "remark_imgs": []
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }

    # expected_schema = {
    #     "$schema": "http://json-schema.org/draft-06/schema",
    #     "type": "object",
    #     "title": "The root schema",
    #     "required": [
    #         "code",
    #         "data",
    #         "time"
    #     ],
    #     "properties": {
    #         "code": {
    #             "type": "integer",
    #             "title": "The code schema"
    #         },
    #         "data": {
    #             "type": "object",
    #             "title": "The data schema",
    #             "required": [
    #                 "aftersale_id",
    #                 "aftersale_status",
    #                 "free_refund_amount",
    #                 "free_refund_exp_status",
    #                 "order_id",
    #                 "order_lock_status",
    #                 "order_process_status",
    #                 "order_refund_status"
    #             ],
    #             "properties": {
    #                 "aftersale_id": {
    #                     "type": "string",
    #                     "title": "The aftersale_id schema"
    #                 },
    #                 "aftersale_status": {
    #                     "type": "integer",
    #                     "title": "The aftersale_status schema"
    #                 },
    #                 "free_refund_amount": {
    #                     "type": "integer",
    #                     "title": "The free_refund_amount schema"
    #                 },
    #                 "free_refund_exp_status": {
    #                     "type": "integer",
    #                     "title": "The free_refund_exp_status schema"
    #                 },
    #                 "order_id": {
    #                     "type": "string",
    #                     "title": "The order_id schema"
    #                 },
    #                 "order_lock_status": {
    #                     "type": "integer",
    #                     "title": "The order_lock_status schema"
    #                 },
    #                 "order_process_status": {
    #                     "type": "integer",
    #                     "title": "The order_process_status schema"
    #                 },
    #                 "order_refund_status": {
    #                     "type": "integer",
    #                     "title": "The order_refund_status schema"
    #                 }
    #             }
    #         },
    #         "time": {
    #             "type": "integer",
    #             "title": "The time schema"
    #         }
    #     }
    # }
