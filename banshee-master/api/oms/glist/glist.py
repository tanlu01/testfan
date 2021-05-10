from api.oms.oms_ import Oms


class Glist(Oms):
    method = 'get'
    api = '/glist/datatablejson'
    data = {
        "adjust_page":"1",
        "datatable[pagination][page]":"1",
        "datatable[pagination][pages]":"1",
        "datatable[pagination][perpage]":"10",
        "datatable[pagination][total]":"1",
        "datatable[pagination][sort]":"",
        "datatable[pagination][field]":"",
        "datatable[sort][sort]":"",
        "datatable[sort][field]":"",
        "datatable[query][generalSearch]":"109513"
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }

    
    expected_schema = {
        "$schema": "http://json-schema.org/draft-06/schema#",
        "title": "expected_data",
        "type": "object",
        "required": ["data", "meta","is_es","is_service"],
        "properties": {
            "data": {
                "type": "array",
                "items":{
                    "type":"object",
                    "properties":{
                        "ethumb_url":{"type":"string"},
                        "carousel_pics":{
                            "type":"string"
                        },
                        "mall_id":{"type":"number"},
                        "goods_id":{"type":"number"}
                    }
                }
                },
            "meta": {
                "type": "object",
                "required": ["page", "pages","perpage","total","sort","field"],
                "properties": {
                    "page": {"type": "number"},
                    "pages": {"type": "number"},
                    "perpage": {"type": "number"},
                    "total": {"type": "number"},
                    "sort": {"type": "string"},
                    "field": {"type": "string"}
                }
            },
            "is_es": {"type": "number",},
            "is_service": {"type": "number",}
        }
    }