from api.act.act_ import Act


class ApplySchedule(Act):
    method = 'get'
    api = '/api/sp/v1/apply/schedules'
    data = {
        'type': 2,
        '_sort': None,
        '_offset': 0,
        '_limit': 20,
        '_count': 1
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
                    "count"
                ],
                "properties": {
                    "list": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "number"
                                },
                                "name": {
                                    "type": "string"
                                },
                                "type": {
                                    "type": "number"
                                },
                                "sub_type": {
                                    "type": "number"
                                },
                                "is_longterm": {
                                    "type": "number"
                                },
                                "schedule_time": {
                                    "type": "array",
                                    "items": [
                                        {
                                            "type": "string"
                                        },
                                        {
                                            "type": "string"
                                        }
                                    ]
                                },
                                "apply_time": {
                                    "type": "array",
                                    "items": [
                                        {
                                            "type": "string"
                                        },
                                        {
                                            "type": "string"
                                        }
                                    ]
                                },
                                "apply_rate": {
                                    "type": "number"
                                },
                                "audit_rate": {
                                    "type": "number"
                                },
                                "creator": {
                                    "type": "string"
                                },
                                "last_operator": {
                                    "type": "string"
                                },
                                "reason": {
                                    "type": "string"
                                },
                                "apply_status": {
                                    "type": "number"
                                },
                                "create_at": {
                                    "type": "string"
                                },
                                "update_at": {
                                    "type": "string"
                                },
                                "act_rules": {
                                    "type": "array",
                                    "items": {
                                    }
                                },
                                "_actions": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "text": {
                                                "type": "string"
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "count": {
                        "type": "number"
                    }
                }
            }
        }
    }
