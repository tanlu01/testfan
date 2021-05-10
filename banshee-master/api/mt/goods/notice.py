from api.mt.mt import Mt


class Notice(Mt):
    method = 'get'
    api = '/v1/goods/$goods_id/notice'
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
            "code": {"type": "number"},
            "time": {"type": "number"},
            "data": {
                "type": "object",
                "required": ["on", "cookie", 'title', 'button_title', 'progress', 'hint'],
                "properties": {
                    "on": {"type": "boolean"},
                    "cookie": {"type": "string"},
                    "title": {"type": "string"},
                    "button_title": {"type": "string"},
                    "progress": {"type": "process"},
                    "hint": {"type": "string"},
                }
            }
        }
    }
