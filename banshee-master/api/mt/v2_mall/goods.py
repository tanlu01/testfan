from api.mt.mt import Mt


class Goods(Mt):
    method = 'get'
    api = '/v2/mall/$mall_id/goods?offset=0&size=20&cat_id=88,89,90,91,92,93'
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
                    "offset"
                ],
                "properties": {
                    "items": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {}
                        }
                    },
                    "offset": {
                        "type": "string"
                    }
                }
            }
        }
    }