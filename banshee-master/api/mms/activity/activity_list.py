from api.mms.mms_ import Mms


class ActivityList(Mms):
    method = 'get'
    api = '/api/promotion/activity/list'
    data = {
        "act_type":"1",
        "page":"1",
        "size":"10",
        "act_cate":"4"
    }

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
            "code": {
                "type": "number"
            },
            "payload": {
                "type": "object",
                "required": ["count", "list"],
                "properties": {
                    "count": {
                        "type": "number"
                },
                    "list": {
                        "type": "array",
                        "items":{
                            "type": "object",
                                "properties": {
                                    "schedule_id":{
                                        "type": "string"
                                    },
                                    "apply_start_time": {
                                        "type": "string"
                                    },
                                    "apply_end_time": {
                                        "type": "string"
                                    },
                                    "schedule_start_time":{
                                        "type": "string"
                                    },
                                    "schedule_end_time":{
                                        "type": "string"
                                    },
                                    "status":{
                                        "type": "string"
                                    },
                                    "is_deleted":{
                                        "type": "string"
                                    },
                                    "reason":{
                                        "type": "string"
                                    },
                                    "is_longterm":{
                                        "type": "string"
                                    },
                                     "title":{
                                        "type": "string"
                                    },
                                    "summary":{
                                        "type": "string"
                                    },
                                     "thumb":{
                                        "type": "string"
                                    },
                                    "btn_info":{
                                        "type": "string"
                                    },
                                    "btn_status":{
                                        "type": "number"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    
