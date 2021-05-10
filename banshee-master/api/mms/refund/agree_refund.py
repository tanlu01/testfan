from api.mms.mms_ import Mms


class AgreeRefundV2(Mms):
    method = 'post'
    api = '/api/aftersale/agreeRefundV2'
    data = {
        "order_id": "1631439211248795650",
        "refund_desc": ""
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }

    expected_schema = {
        "$schema": "http://json-schema.org/draft-06/schema",
        "type": "object",
        "title": "The root schema",
        "required": [
            "code",
            "payload"
        ],
        "properties": {
            "code": {
                "type": "integer",
                "title": "The code schema"
            },
            "payload": {
                "type": "object",
                "title": "The payload schema",
                "required": [
                    "order_id",
                    "refund_status"
                ],
                "properties": {
                    "order_id": {
                        "type": "string",
                        "title": "The order_id schema"
                    },
                    "refund_status": {
                        "type": "integer",
                        "title": "The refund_status schema"
                    }
                }
            }
        }
    }
