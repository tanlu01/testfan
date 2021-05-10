from api.mt.mt import Mt


class Category(Mt):
    method = 'get'
    api = '/v2/mall/$mall_id/category'
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
                    "cats"
                ],
                "properties": {
                    "cats": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "name": {
                                    "type": "string"
                                },
                                "link": {
                                    "type": "string"
                                },
                                "children": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {

                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
