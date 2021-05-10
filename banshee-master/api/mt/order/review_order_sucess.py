from api.mt.mt import Mt
import os
import datetime
from random import randint


class ReviewSucess(Mt):
    method = 'get'
    api = '/v1/review/$order_id/success'
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
                    "order_id",
                    "goods_id",
                    "description_rating",
                    "shipping_rating",
                    "service_rating",
                    "package_rating"
                ],
                "properties": {
                    "order_id": {
                        "type": "string"
                    },
                    "goods_id": {
                        "type": "string"
                    },
                    "description_rating": {
                        "type": "number"
                    },
                    "shipping_rating": {
                        "type": "number"
                    },
                    "service_rating": {
                        "type": "number"
                    },
                    "package_rating": {
                        "type": "number"
                    }
                }
            }
        }
    }