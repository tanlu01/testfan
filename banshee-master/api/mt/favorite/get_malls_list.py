from api.mt.mt import Mt
import os
import datetime
from random import randint


class Get_malls_list(Mt):
    method = 'get'
    api = '/v1/favorite/malls/list?offset=&size=20'
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
                "required": ["items", "offset"],
                "properties": {
                    "items": {
                        "type": "array",
                        'items': {
                            'type': 'object',
                            'properties': {
                                "mall_id": {"type": "number"},
                                "mall_name": {"type": "string"},
                                "logo": {"type": "string"},
                                "mall_sale": {"type": "number"},
                                "is_open": {"type": "boolean"},
                                "coupon_available": {"type": "boolean"}
                            }
                        }
                    },
                    "offset": {"type": "string"}
                }
            }
        }
    }
