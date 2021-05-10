from api.oms_new.oms_ import Oms


class Auth(Oms):
    method = 'post'
    api = '/omsapi/user/login'
    data = {
        "username": "wenjie",
        "password": "a1a1a1",
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }

    expected_schema = {
        "$schema": "http://json-schema.org/draft-06/schema#",
        "title": "expected_data",
        "type": "object",
        "required": [
            "code",
            "message",
            "payload"
        ],
        "properties": {
            "code": {
                "type": "number"
            },
            "message": {
                "type": "string"
            },
            "payload": {
                "type": "object",
                "required": [
                    "id",
                    "mobile",
                    "name",
                    "avatar",
                    "token"
                ],
                "properties": {
                    "id": {
                        "type": "number"
                    },
                    "mobile": {
                        "type": "string"
                    },
                    "name": {
                        "type": "string"
                    },
                    "avatar": {
                        "type": "string"
                    },
                    "token": {
                        "type": "string"
                    }
                }
            }
        }
    }
