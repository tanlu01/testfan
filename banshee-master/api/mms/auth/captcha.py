from api.mms.mms_ import Mms


class Captcha(Mms):
    method = 'get'
    api = '/api/captcha'
    data = {}

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
                "required": ["image", "token"],
                "properties": {
                    "image": {""
                              "type": "string"},
                    "token": {"type": "string"}
                }
            }
        }
    }
