from api.oms_new.oms_ import Oms


class Detail(Oms):
    method = 'get'
    api = '/omsapi/specialgoods/goods/$activity_id'
    data = {
        'tab_id': 0,
        'status': None,
        '_page': 1,
        '_size': 20
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }

    expected_schema = {
        "$schema": "http://json-schema.org/draft-06/schema#",
        "title": "expected_data",
        "type": "object",
        "required": ["code", 'message', "payload"],
        "properties": {
            "code": {"type": "number"},
            "message": {"type": "string"},
            "payload": {
                "type": "object",
                "required": ['list', 'page', 'page_size', 'total'],
                "properties": {
                    'list': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {}
                        }
                    },
                    'page': {"type": 'string'},
                    'pageSize': {"type": 'string'},
                    'total': {"type": 'number'}
                }
            }
        }
    }
