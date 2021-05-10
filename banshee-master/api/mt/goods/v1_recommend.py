from api.mt.mt import Mt
import os
import datetime
from random import randint


class V1_recommend(Mt):
    method = 'get'
    api = '/v1/recommend?clue=$clue&offset=$offset&referer=$referer&size=$size'
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
            'code': {'type': 'number'},
            'time': {'type': 'number'},
            'data': {
                'type': 'object',
                'required': ['items', 'offset', 'title'],
                'properties': {
                    'items': {
                        'type': 'array',
                        'items': {
                            'properties': {}
                        }
                    },
                    'offset': {'type': 'string'},
                    'title': {'type': 'string'}
                    }
                }
            }
        }
    



   
