from api.mt.mt import Mt
import os
import datetime
from random import randint


class Rewards(Mt):
    method = 'get'
    api = '/v1/order/$order_id/rewards'
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
                    "coins",
                    "coupons",
                    "activities",
                    "back_url"
                ],
                "properties": {
                    "coins": {
                        "type": "number"
                    },
                    "coupons": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {}
                        }
                    },
                    "activities": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {}
                        }
                    },
                    "back_url": {
                        "type": "string"
                    }
                }
            }
        }
    }