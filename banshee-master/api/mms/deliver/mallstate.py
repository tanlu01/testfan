from api.mms.mms_ import Mms


class Mallstate(Mms):
    method = 'get'
    api = '/api/logistics/promote/mallstate'
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
                "required": ["is_sign_up", "material", 'reject_type', 'subsidy_status'],
                "properties": {
                    'is_sign_up': {"type": "number"},
                    "material": {
                        "type": "array",
                        "items": {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'number', "enum": [1, 2, 3]},
                                'name': {'type': 'string', "enum": ['纸箱', '气泡袋', '快递专用塑料袋']}
                            }
                        }
                    },
                    "reject_type": {
                        "type": "array",
                        "items": {
                            'type': 'object',
                            'properites': {
                                "id": {"type": "number", 'enum': [1, 2, 3, 4]},
                                "name": {"type": "string", 'enum': ['没有当日发货', '延迟发货', '虚假发货', '用户售后']}
                            },
                        }
                    },
                    "subsidy_status": {
                        "type": "array",
                        "items": {
                            'type': 'object',
                            'properites': {
                                "id": {"type": "number", "enum": [1, 2, 3]},
                                "name": {"type": "string", 'enum': ['待确认', '是', '否']}
                            }
                        }
                    }
                }
            }
        }
    }
