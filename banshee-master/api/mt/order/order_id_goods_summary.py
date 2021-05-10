from api.mt.mt import Mt
import os
import datetime
from random import randint


class Goods_Smmary(Mt):
    method = 'get'
    api = '/v1/order/$order_id/goods/summary'
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
                    "goods_name",
                    "goods_desc",
                    "goods_icon",
                    "goods_specs",
                    "goods_prime_price",
                    "goods_contrast_price",
                    "has_prime_price"
                ],
                "properties": {
                    "goods_name": {
                        "type": "string"
                    },
                    "goods_desc": {
                        "type": "string"
                    },
                    "goods_icon": {
                        "type": "string"
                    },
                    "goods_specs": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "spec_id": {
                                    "type": "number"
                                },
                                "spec_key": {
                                    "type": "string"
                                },
                                "spec_value": {
                                    "type": "string"
                                }
                            }
                        }
                    },
                    "goods_prime_price": {
                        "type": "number"
                    },
                    "goods_contrast_price": {
                        "type": "number"
                    },
                    "has_prime_price": {
                        "type": "boolean"
                    }
                }
            }
        }
    }