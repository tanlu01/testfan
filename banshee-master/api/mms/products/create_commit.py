from api.mms.mms_ import Mms


class CreateCommit(Mms):
    method = 'post'
    api = '/api/goods/createCommit'
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
            "code": {
                "type": "number"
            },
            "payload": {
                "type": "object",
                "required": ["commit_id"],
                "properties": {
                    "commit_id": {
                        "type": "string"
                    },
                }
            }
        }
    }
