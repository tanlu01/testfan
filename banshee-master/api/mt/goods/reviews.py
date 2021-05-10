from api.mt.mt import Mt
import os
import datetime
from random import randint


class Reviews(Mt):
    method = 'get'
    api = '/v1/goods/$goods_id/reviews'
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
                "required": ["num", "num_text", 'labels', 'rec_labels', 'items', 'avatars',
                             'review_cnt', 'positive_rate'],
                "properties": {
                    "num": {"type": "number"},
                    "num_text": {"type": "string"},
                    "labels": {
                        "type": "array",
                        'item': {
                            'type': 'object',
                            'properties': {}
                        }
                    },
                    "rec_labels": {"type": "boolean"},
                    "items": {
                        "type": "array",
                        'items': {
                            'type': 'object',
                            'properties': {}
                        }
                    },
                    "avatars": {
                        "type": "array",
                        'item': {
                            'type': 'object',
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
                                "imgs": {
                                    "type": "array",
                                    'items': {
                                        'type': 'object',
                                        'properties': {}
                                    }
                                },
                                "medias": {
                                    "type": "array",
                                    'items': {
                                        'type': 'object',
                                        'properties': {}
                                    }
                                },
                                "response_text": {"type": "string"},
                                "appends": {
                                    "type": "array",
                                    'items': {
                                        'type': 'object',
                                        'properties': {}
                                    }
                                },
                                "special_stamp_image": {"type": None},
                                "link": {"type": "string"},
                            }
                        }
                    },
                    "review_cnt": {"type": "number"},
                    "positive_rate": {"type": "string"}
                }
            }
        }
    }
