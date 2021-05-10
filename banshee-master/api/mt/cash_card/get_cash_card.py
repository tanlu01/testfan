from api.mt.mt import Mt
import os
import datetime
from random import randint


class Cash_card(Mt):
    method = 'get'
    api = '/v1/cash_card'
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
                "required": ["available", "used_and_expired"],
                "properties": {
                    "available": {
                        "type": "array",
                        'items': {
                            'type': 'object',
                            'properties': {}
                        }
                    },
                    "used_and_expired": {
                        "type": "array",
                        'items': {
                            'type': 'object',
                            'properties': {}
                        }
                    }
                }
            }
        }
    }
