from api.mt.mt import Mt
import os
import datetime
from random import randint


class V1_mall_info(Mt):
    method = 'get'
    api = '/v1/mall/$mall_id/info'
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
            'data': {
                'type': 'object',
                "required": ["mall_id", "mall_name", 'logo', 'logo_origin', 'background_img',
                             'mall_sales', 'company_phone', 'chat_status', 'goods_num', 'mall_desc',
                             'offline_note', 'coupons', 'is_open'],
                'properties': {
                    "mall_id": {"type": "number"},
                    "mall_name": {"type": "string"},
                    "logo": {"type": "string"},
                    "logo_origin": {"type": "string"},
                    "background_img": {"type": "string"},
                    "mall_sales": {"type": "number"},
                    "company_phone": {"type": "string"},
                    "chat_status": {"type": "number"},
                    "goods_num": {"type": "number"},
                    "mall_desc": {"type": "string"},
                    "offline_note": {"type": "string"},
                    "is_open": {"type": "boolean"},
                    'coupons': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {"type": "string"},
                                "mall_id": {"type": "number"},
                                "name": {"type": "string"},
                                "amount": {"type": "number"},
                                "type": {"type": "number"},
                                "status": {"type": "number"},
                                "begin": {"type": "number"},
                                "end": {"type": "number"},
                                "is_taken_out": {"type": "boolean"},
                                "can_taken_count": {"type": "number"},
                                "remain": {"type": "number"}
                            }
                        }
                    }
                }
            }
        }
    }
