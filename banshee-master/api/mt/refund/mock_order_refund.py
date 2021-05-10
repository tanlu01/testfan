from api.mt.mt import Mt


class MockOrderRefund(Mt):
    method = 'post'
    api = '/notify/mock/order_refund'
    data = {
        "payment_refund_id": "10828",
        "refund_id": "8549156126713757698",
        "status": 0
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
            "data",
            "time"
        ],
        "properties": {
            "code": {
                "type": "integer",
                "title": "The code schema"
            },
            "data": {
                "type": "object",
                "title": "The data schema",
                "required": [
                    "code"
                ],
                "properties": {
                    "code": {
                        "type": "integer",
                        "title": "The code schema"
                    }
                }
            },
            "time": {
                "type": "integer",
                "title": "The time schema"
            }
        }
    }
