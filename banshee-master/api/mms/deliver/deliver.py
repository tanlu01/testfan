from api.mms.mms_ import Mms


class Deliver(Mms):
    method = 'post'
    api = '/api/deliver'
    data = {
        "logistic_id": 0,
        "order_id": "",
        "express_id": "3",
        "tracking_num": "23545466"
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }

    expected_schema = {
            "$schema": "http://json-schema.org/draft-06/schema#",
            "title": "expected_data",
            "type": "object",
            "required": ["code", "payload"],
            "properties": {
                "code": {"type": "number"},
                "payload": {
                    "type": "object",
                    "required": ["code", "data", "time"],
                    "properties": {
                        "code": {"type": "number"},
                        "data": {
                            "type": "object",
                            "required": ["list"],
                            "properties": {
                                "list": {
                                    "type": "array",
                                    "items": {
                                        'type': 'object',
                                        'properties': {}
                                    }
                                }
                            }
                        },
                        "time": {"type": "number"}
                    }
                }
            }
        }
