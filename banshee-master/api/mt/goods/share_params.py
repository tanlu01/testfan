from api.mt.mt import Mt
import os
import datetime
from random import randint


class Share_params(Mt):
    method = 'get'
    api = '/v1/goods/$goods_id/share_params'
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
                "required": ["on", "tpls_str", 'd', 'msg', 'normal', 'share_type'],
                "properties": {
                    "on": {"type": "boolean"},
                    "tpls_str": {
                        "type": "array",
                        'items': [{'type': 'string'}]
                    },
                    'd': {
                        'type': 'object',
                        'required': ['user', 'goods'],
                        'properties': {
                            'user': {
                                'type': 'object',
                                'required': ['avatar', 'nickname', 'review_star', 'review_content'],
                                'properties': {
                                    "avatar": {"type": "string"},
                                    "nickname": {"type": "string"},
                                    "review_star": {"type": "string"},
                                    "review_content": {"type": "string"}
                                }
                            },
                            'goods': {
                                'type': 'object',
                                'required': ['img', 'name', 'money_type', 'price', 'sales', 'market_price',
                                             'share_url', 'long_share_url', 'rcmd_text'],
                                'properties': {
                                    "img": {"type": "string"},
                                    "name": {"type": "string"},
                                    "money_type": {"type": "number"},
                                    "price": {"type": "string"},
                                    "sales": {"type": "number"},
                                    "market_price": {"type": "string"},
                                    "share_url": {"type": "string"},
                                    "long_share_url": {"type": "string"},
                                    "rcmd_text": {"type": "string"}
                                }
                            }
                        }
                    },
                    "msg": {"type": "string"},
                    "normal": {
                        "type": "object",
                        'required': ['img', 'link'],
                        'properties': {
                            "img": {"type": "string"},
                            "link": {"type": "string"}
                        }
                    },
                    "share_type": {"type": "string"},

                }
            }
        }
    }
