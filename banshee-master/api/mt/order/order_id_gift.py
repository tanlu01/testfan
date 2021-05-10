from api.mt.mt import Mt
import os
import datetime
from random import randint


class Gift(Mt):
    method = 'get'
    api = '/v1/order/$order_id/gift'
    data = {}

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }

    expected_schema = {
        "$schema": "http://json-schema.org/draft-06/schema#",
        "title": "expected_data",
        "type": "object",
        "required": [
            "code",
            "time",
            "data"
        ],
        "properties": {
            "code": {
                "type": "number"
            },
            "time": {
                "type": "number"
            },
            "data": {
                "type": "object",
                "required": [
                    "bonus_id",
                    "order_id",
                    "gift_type",
                    "amount",
                    "get_amount",
                    "gift_status",
                    "expire_at",
                    "assister_count",
                    "share_title",
                    "share_desc",
                    "share_icon",
                    "share_link"
                ],
                "properties": {
                    "bonus_id": {
                        "type": "string"
                    },
                    "order_id": {
                        "type": "string"
                    },
                    "gift_type": {
                        "type": "number"
                    },
                    "amount": {
                        "type": "number"
                    },
                    "get_amount": {
                        "type": "number"
                    },
                    "gift_status": {
                        "type": "number"
                    },
                    "expire_at": {
                        "type": "number"
                    },
                    "assister_count": {
                        "type": "number"
                    },
                    "share_title": {
                        "type": "string"
                    },
                    "share_desc": {
                        "type": "string"
                    },
                    "share_icon": {
                        "type": "string"
                    },
                    "share_link": {
                        "type": "string"
                    }
                }
            }
        }
    }