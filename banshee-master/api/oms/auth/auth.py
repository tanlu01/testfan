from api.oms.oms_ import Oms


class Auth(Oms):
    method = 'post'
    api = '/login?system=1'
    data = {
        "username": "wenjie",
        "password": "a1a1a1",
        "redirect_uri":  "/"
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
            "code": {
                "type": "number"
            },
            "payload": {
                "type": "object",
                "required": ["redirect_uri"],
                "properties": {
                    "redirect_uri": {
                        "type": "string"
                    },
                }
            }
        }
    }
