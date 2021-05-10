from api.oms_new.oms_ import Oms
import datetime


class CouponList(Oms):
    method = 'get'
    api = '/omsapi/coupon/list?create_at[]=$create_at1&create_at[]=$create_at2'
    data = {
        
    }
  
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
            "message",
            "payload"
        ],
        "properties": {
            "code": {
                "type": "number"
            },
            "message": {
                "type": "string"
            },
            "payload": {
                "type": "object",
                "required": [
                    "list",
                    "total",
                    "page",
                    "pagesize"
                    ],
                    "properties": {
                    "list": {
                        "type": "array",
                        "items":{
                          "type":"object",
                          "properties":{
                            "id":{"type":"string"},
                            "sub_name":{"type":"string"},
                            "count":{"type":"number"},
                            "status":{"type":"number"},
                            "is_deleted":{"type":"number"},
                            "name":{"type":"string"},
                            "biz_title":{"type":"string"},
                            "min_price":{"type":"number"},
                            "amount":{"type":"number"},
                            "operator_id":{"type":"number"},  
                            "create_at":{"type":"string"},
                            "use_relative":{"type":"number"},
                            "use_relative_start_day":{"type":"number"},
                            "use_relative_end_day":{"type":"number"},
                            "use_start_time":{"type":"string"},
                            "use_end_time":{"type":"string"},
                            "cannot_self_take":{"type":"number"},
                            "get_start_time":{"type":"string"},
                            "get_end_time":{"type":"string"},
                            "mall_amount":{"type":"number"},
                            "mall_id":{"type":"number"},  
                            "type":{"type":"number"},
                            "scene_type":{"type":"number"},
                            "scene_text":{"type":"string"},
                            "rule_id":{"type":"number"},
                            "title":{"type":"string"},
                            "price_info":{"type":"string"},
                            "rule_id_type":{"type":"string"}, 
                            "get_time":{"type":"string"},
                            "use_time":{"type":"string"},
                            "operator_info":{"type":"string"},
                            "mall_name":{"type":"string"},
                            "scene_title":{"type":"string"},
                            "coupon_rule_info":{"type":"string"}
                          }
                        }
                    },
                    "total": {
                        "type": "number"
                    },
                    "page": {
                        "type": "number"
                    },
                    "pagesize": {
                        "type": "number"
                    }
                }
            
            }
        }
    }
    