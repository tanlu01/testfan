from api.mt.mt import Mt


class Skus(Mt):
    method = 'get'
    api = '/v2/goods/$goods_id/skus'
    data = {}

    expected_schema = {
        "$schema": "http://json-schema.org/draft-06/schema#",
        "title": "expected_data",
        "type": "object",
        "required": ["code", "time", 'data'],
        "properties": {
            "code": {"type": "number"},
            "time": {"type": "number"},
            "data": {
                "type": "object",
                "required": ["skus", "single", 'money_types', 'goods_id', 'mall_id'],
                "properties": {
                    "skus": {
                        "type": "array",
                        'items': {
                            'type': 'object',
                            'properties': {
                                "sku_id": {"type": "number"},
                                "thumb_url": {"type": "string"},
                                "quantity": {"type": "number"},
                                "is_onsale": {"type": "boolean"},
                                "normal_price": {"type": "number"},
                                "group_price": {"type": "number"},
                                "cc": {"type": "number"},
                                "spec_combo": {"type": "string"},
                                "specs": {
                                    "type": "array",
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'spec_id': {"type": "number"},
                                            'spec_key': {"type": "string"},
                                            'spec_value': {"type": "string"}
                                        }
                                    }
                                },
                            }
                        }
                    },
                    'single': {
                        'type': 'object',
                        'required': ['buy_limit', 'order_limit', 'single_unity_limit'],
                        'properties': {
                            "buy_limit": {"type": "number"},
                            "order_limit": {"type": "number"},
                            "single_unity_limit": {"type": "number"}
                        }
                    },
                    'money_types': {
                        'object': 'array',
                        'items': [{'type': 'number'}]
                    },
                    "goods_id": {"type": "string"},
                    "mall_id": {"type": "string"},
                }
            }
        }
    }
