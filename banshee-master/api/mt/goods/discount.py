from api.mt.mt import Mt
import os
import datetime
from random import randint


class Discount(Mt):
    method = 'get'
    api = '/v1/goods/$goods_id/discount'
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
                "required": ["discount_mark", 'coupons', 'promotions'],
                "properties": {
                    "discount_mark": {
                        "type": "array",
                        'items': {
                            'type': 'object',
                            'properites': {
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
                    },
                    'coupons': {
                        "type": "array",
                        'items': {
                            'type': 'object',
                            'properites': {
                                'id': {'type': 'string'},
                                'name': {'type': 'string'},
                                'sub_name': {'type': 'string'},
                                'mall_id': {'type': 'number'},
                                'link': {'type': 'string'},
                                'has_received': {'type': 'boolean'},
                                'has_useable': {'type': 'boolean'},
                                'min_price': {'type': 'number'},
                                'should_prime': {'type': 'number'},
                                'btn_status': {'type': 'number'},
                                'type': {'type': 'number'},
                                'discount': {
                                    'type': 'object',
                                    'required': ['type', 'value', 'value_uint'],
                                    'properites': {
                                        'type': {'type': 'number'},
                                        'value': {'type': 'string'},
                                        'value_uint': {'type': 'number'}
                                    }
                                },
                                'usetime': {
                                    'type': 'object',
                                    'required': ['begin', 'end'],
                                    'properites': {
                                        'begin': {'type': 'number'},
                                        'end': {'type': 'number'}
                                    }
                                }
                            }
                        }
                    },
                    'promotions': {'type': None}
                }
            }
        }
    }