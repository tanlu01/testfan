from api.oms_new.oms_ import Oms

class Salespecial_List(Oms):

    method = 'get'
    api = '/omsapi/salespecial/list'
    data = {}

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }

    expected_schema = {
        "$schema":"http://json-schema.org/draft-06/schema#",
        "title":"expected_data",
        "type":"object",
        "required":[
            "code",
            "message",
            "payload"
        ],
        "properties":{
            "code":{
                "type":"number"
            },
            "message":{
                "type":"string"
            },
            "payload":{
                "type":"object",
                "required":[
                    "list",
                    "total",
                    "page",
                    "pageSize"
                ],
                "properties":{
                    "list":{
                        "type":"array",
                        "items":{
                            "type":"object",
                            "properties":{
                                "id":{
                                    "type":"number"
                                },
                                "activity_name":{
                                    "type":"string"
                                },
                                "type":{
                                    "type":"number"
                                },
                                "schedule_id":{
                                    "type":"number"
                                },
                                "schedule_name":{
                                    "type":"string"
                                },
                                "create_at":{
                                    "type":"string"
                                },
                                "creator_name":{
                                    "type":"string"
                                },
                                "status":{
                                    "type":"number"
                                },
                                "start_time":{
                                    "type":"string"
                                },
                                "end_time":{
                                    "type":"string"
                                },
                                "remark":{
                                    "type":"string"
                                },
                                "activity_step":{
                                    "type":"number"
                                },
                                "act_time":{
                                    "type":"string"
                                },
                                "state":{
                                    "type":"number"
                                },
                                "special_id":{
                                    "type":"string"
                                },
                                "schedule":{
                                    "type":"string"
                                }
                            }
                        }
                    },
                    "total":{
                        "type":"number"
                    },
                    "page":{
                        "type":"number"
                    },
                    "pageSize":{
                        "type":"number"
                    }
                }
            }
        }
    }
