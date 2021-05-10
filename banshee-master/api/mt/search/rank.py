from api.mt.mt import Mt
import os
import datetime
from random import randint


class Rank(Mt):
    method = 'get'
    api = '/v1/search/rank'
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
                    "items"
                ],
                "properties": {
                    "items": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "thumb_url": {
                                    "type": "string"
                                },
                                "query": {
                                    "type": "string"
                                },
                                "number": {
                                    "type": "number"
                                },
                                "goods_id": {
                                    "type": "string"
                                }
                            }
                        }
                    }
                }
            }
        }
    }
