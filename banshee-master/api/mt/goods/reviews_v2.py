from api.mt.mt import Mt
import os
import datetime
from random import randint


class Reviews_v2(Mt):
    method = 'get'
    api = '/v2/goods/$goods_id/reviews'
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
                "required": ["num", 'num_text', 'labels', 'rec_labels',
                             'items', 'avatars', 'review_cnt', 'positive_rate', 'breviate'],
                "properties": {
                    "num": {"type": "number"},
                    "num_text": {"type": "string"},
                    "review_cnt": {"type": "number"},
                    "positive_rate": {"type": "string"},
                    "breviate": {"type": "number"},
                    "labels": {
                        "type": 'array',
                        'items': 'object',
                        'properties': {}
                    },
                    "rec_labels": {
                        "type": 'array',
                        'items': 'object',
                        'properties': {
                            'id': {"type": "number"},
                            'positive': {"type": "boolean"},
                            'name': {"type": "string"},
                            'num': {"type": "number"},
                            'has_num': {"type": "boolean"},
                            'style_type': {"type": "number"}
                        }
                    },
                    'items': {
                        "type": 'array',
                        'items': 'object',
                        'properties': {
                            'goods_id': {"type": "number"},
                            'review_id': {"type": "string"},
                            'mall_id': {"type": "string"},
                            'sku_id': {"type": "number"},
                            'name': {"type": "string"},
                            'avatar': {"type": "string"},
                            'is_prime': {"type": "boolean"},
                            'is_chosen': {"type": "boolean"},
                            'text': {"type": "string"},
                            'desc_rating': {"type": "number"},
                            'logistic_rating': {"type": "number"},
                            'service_rating': {"type": "number"},
                            'package_rating': {"type": "number"},
                            'average_rating': {"type": "number"},
                            'specs': {"type": "string"},
                            'time': {"type": "number"},
                            'response_text': {"type": "string"},
                            'link': {"type": "string"},
                            'special_stamp_image': {"type": None},
                            'imgs': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {}
                                }
                            },
                            'medias': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {}
                                }
                            },
                            'appends': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {}
                                }
                            }
                        }
                    },
                    'avatars': {
                        'type': 'array',
                        'items': [
                            {'type': 'string'},
                            {'type': 'string'},
                            {'type': 'string'}
                        ]
                    }
                }
            }
        }
    }

