from api.mt.mt import Mt
import os
import datetime
from random import randint


class Match(Mt):
    method = 'get'
    api = '/v1/search/match?q=$search_keyword&cat=&offset=&sort=_default&size=10'
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
                    "items",
                    "is_black",
                    "total",
                    "offset",
                    "qc"
                ],
                "properties": {
                    "items": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {

                            }
                        }
                    },
                    "is_black": {
                        "type": "boolean"
                    },
                    "total": {
                        "type": "number"
                    },
                    "offset": {
                        "type": "string"
                    },
                    "qc": {
                        "type": "string"
                    }
                }
            }
        }
    }
