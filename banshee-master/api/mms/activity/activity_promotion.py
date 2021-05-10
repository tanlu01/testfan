from api.mms.mms_ import Mms
from tools.generate_schema import GenerateSchema

class Activity_Promotion(Mms):

    method = 'get'
    api = '/api/promotion/schedule/list'
    data = {
        'page': 1,
        'page_size': 10,
        'module_type_id': '',
        'schedule_name': '',
        'participate_status': ''
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }

{
    "$schema":"http://json-schema.org/draft-06/schema#",
    "title":"expected_data",
    "type":"object",
    "required":[
        "code",
        "payload"
    ],
    "properties":{
        "code":{
            "type":"number"
        },
        "payload":{
            "type":"object",
            "required":[
                "count",
                "list"
            ],
            "properties":{
                "count":{
                    "type":"number"
                },
                "list":{
                    "type":"array",
                    "items":{
                        "type":"object",
                        "properties":{
                            "id":{
                                "type":"number"
                            },
                            "name":{
                                "type":"string"
                            },
                            "thumb":{
                                "type":"string"
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
                            "type":{
                                "type":"number"
                            },
                            "sub_type":{
                                "type":"number"
                            },
                            "desc":{
                                "type":"string"
                            },
                            "module_type_id":{
                                "type":"number"
                            },
                            "create_at":{
                                "type":"string"
                            },
                            "activity_tag":{
                                "type":"array",
                                "items":{
                                    "type":"object",
                                    "properties":{

                                    }
                                }
                            },
                            "schedule_status":{
                                "type":"number"
                            },
                            "schedule_status_text":{
                                "type":"string"
                            },
                            "participate_status":{
                                "type":"number"
                            },
                            "participate_status_text":{
                                "type":"string"
                            },
                            "act_cate":{
                                "type":"number"
                            }
                        }
                    }
                }
            }
        }
    }
}