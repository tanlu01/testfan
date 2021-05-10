from api.mms.mms_ import Mms


class GoodsMaterial(Mms):
    method = 'post'
    api = '/api/logistics/promote/goodsmaterial'
    data = {
        "goods_ids": ["37648412"],
        "material_id": "2"
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
                'payload': {
                    'type': 'array',
                    'items': {}
                }
            }
        }
