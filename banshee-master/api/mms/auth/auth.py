from api.mms.mms_ import Mms


class Auth(Mms):
    method = 'post'
    api = '/api/auth'
    data = {
        "username": "18017752229",
        "password": "19660302,.cj",
        "captcha": "",
        "token": ""
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
                "required": ["userInfo", "session_id"],
                "properties": {
                    "userInfo": {
                        "type": "object",
                        "required": ["id", "username", "mobile", "nickname", "mall_id", "mall_owner", "password_status"],
                        "properties": {
                            "id": {"type": "number"},
                            "username": {"type": "string"},
                            "mobile": {"type": "string"},
                            "nickname": {"type": "string"},
                            "mall_id": {"type": "string"},
                            "mall_owner": {"type": "string"},
                            "password_status": {"type": "string"},
                        }
                    },
                    "session_id": {"type": "string"}
                }
            }
        }
    }
