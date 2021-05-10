from api.oms.oms_ import Oms


class Category(Oms):
    method = 'get'
    api = '/category/categoryurl'
    data = {}

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }

    expected_schema = {
        "$schema": "http://json-schema.org/draft-06/schema#",
        "title": "expected_data",
        "type": "object",
        "required": ["code", "payload"],
        "properties": {
            "code": {"type": "number"},
            "payload": {
                "type": "object",
                "required": ["categoryurl"],
                "properties": {
                    "categoryurl": {"type": "string"}
                }
            }
        }
    }
