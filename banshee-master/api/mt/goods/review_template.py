from api.mt.mt import Mt
import os
import datetime
from random import randint


class Review_template(Mt):
    method = 'get'
    api = '/v1/goods/$goods_id/review_template'
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
                "required": ["review_edit_label"],
                "properties": {
                    "review_edit_label": {
                        "type": "array",
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {"type": "string"},
                                'name': {"type": "string"}
                            }
                        }
                    }
                }
            }
        }
    }
