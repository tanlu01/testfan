from api.mt.mt import Mt
import os
import datetime
from random import randint


class Brief(Mt):
    method = 'get'
    api = '/v2/goods/$goods_id/brief'
    data = {}

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }

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
                "required": ["goods_id", "goods_name", 'thumb_url', 'skus', 'service_promise_mark'],
                "properties": {
                    'goods_id': {'type': 'string'},
                    'goods_name': {'type': 'string'},
                    'thumb_url': {'type': 'string'},
                    'skus': {'type': None},
                    "service_promise_mark": {
                        "type": "array",
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'string'},
                                'text': {'type': 'string'},
                                'style': {'type': 'number'},
                                'name': {'type': 'string'},
                                'img_url': {'type': 'string'},
                                'img_ratio': {'type': 'string'},
                                'link': {'type': 'string'},
                                'icon_url': {'type': 'string'},
                                'icon_ratio': {'type': 'string'}
                            }
                        }
                    }
                }
            }
        }
    }
