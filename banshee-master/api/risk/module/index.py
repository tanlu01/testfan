from api.risk.risk import Risk


class Index(Risk):
    method = 'get'
    api = '/api/risk/strategyGroupModule/index'
    data = {
        '_sort': None,
        '_offset': 0,
        '_limit': 20,
        '_count': 1
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }

    expected_schema1 = {
        "$schema": "http://json-schema.org/draft-06/schema#",
        "title": "expected_data",
        "type": "object",
        "required": ["code", "payload"],
        "properties": {
            "code": {
                "type": "number"
            },
            "payload": {
                "type": "object",
                "required": ["count", "list","act_info","act_require"],
                "properties": {
                    "count": {
                        "type": "number"
                },
                    "list": {
                        "type": "array",
                        "items":{
                            "type": "object",
                                "properties": {
                                    }
                            }
                        },
                    "act_info": {
                        "type": "object",
                        "required": ["schedule_id", "apply_start_time","apply_end_time","schedule_start_time","schedule_end_time","status","is_deleted","sub_type","type","summary","thumb","act_intro","title","is_longterm","activity_tag","btn_status","act_status_val","schedule_status","schedule_status_text","is_can_apply"],
                        "properties":{
                            "schedule_id":{
                                "type":"number"
                            },
                            "apply_start_time":{
                                "type":"string"
                            },
                            "apply_end_time":{
                                "type":"string"
                            },
                            "schedule_start_time":{
                                "type":"string"
                            },
                            "schedule_end_time":{
                                "type":"string"
                            },
                            "status":{
                                "type":"number"
                            },
                            "is_deleted":{
                                "type":"number"
                            },
                            "sub_type":{
                                "type":"number"
                            },
                            "type":{
                                "type":"number"
                            },
                            "summary":{
                                "type":"string"
                            },
                            "thumb":{
                                "type":"string"
                            },
                            "act_intro":{
                                "type":"string"
                            }, 
                            "title":{
                                "type":"string"
                            }, 
                            "is_longterm":{
                                "type":"number"
                            }, 
                            "activity_tag":{
                                "type":"array",
                                "items":{
                                    "type":"object",
                                    "properties":{
                                    }
                                }
                            }, 
                           "btn_status":{
                                "type":"number"
                            },
                            "act_status_val":{
                                "type":"string"
                            },
                           "schedule_status":{
                                "type":"number"
                            },
                            "schedule_status_text":{
                                "type":"string"
                            },
                            "is_can_apply":{
                                "type":"number"
                            }     
                        }
                },
                "act_require":{
                    "type": "object",
                    "required": ["mall_require", "goods_require"],
                    "properties": {
                        "mall_require": {
                            "type": "array",
                            "items":{
                                "type": "object",
                                "required": ["name", "specification","is_satisfy"],
                                "properties":{
                                    "name":{
                                        "type": "string",
                                    },
                                    "specification":{
                                        "type": "string",
                                    },
                                    "is_satisfy":{
                                        "type": "number",
                                    }
                                }
                                
                            }
                        },
                        "goods_require":{
                            "type": "array",
                            "items":{
                                "type":"object",
                                "properties":{

                                }
                            }
                        }
                    }
                }
            }
        }
    }
}