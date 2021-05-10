from api.mt.mt import Mt


class MockOrderPay(Mt):
    method = 'post'
    api = '/notify/mock/order_pay'
    data = {
        'order_id': '',
        'payment_id': ''
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
