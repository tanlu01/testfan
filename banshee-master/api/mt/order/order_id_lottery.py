from api.mt.mt import Mt
import os
import datetime
from random import randint


class Lottery(Mt):
    method = 'get'
    api = '/v1/order/$order_id/lottery'
    data = {}

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
            "time",
            "data"
        ],
        "properties": {
            "code": {
                "type": "number"
            },
            "time": {
                "type": "number"
            },
            "data": {
                "type": "object",
                "required": [
                    "gift_code",
                    "gift_cnt",
                    "gift_icon",
                    "status",
                    "items",
                    "show_tiger_machine",
                    "animation",
                    "gift_ring"
                ],
                "properties": {
                    "gift_code": {
                        "type": "string"
                    },
                    "gift_cnt": {
                        "type": "number"
                    },
                    "gift_icon": {
                        "type": "string"
                    },
                    "status": {
                        "type": "number"
                    },
                    "show_tiger_machine": {
                        "type": "boolean"
                    },
                    "gift_ring": {
                        "type": "object",
                        "required": [
                            "title",
                            "process_cnt",
                            "need_cnt",
                            "lottery_prob",
                            "show_lottery",
                            "hidden",
                            "enable_order_push_task"
                        ],
                        "properties": {
                            "title": {
                                "type": "string"
                            },
                            "process_cnt": {
                                "type": "number"
                            },
                            "need_cnt": {
                                "type": "number"
                            },
                            "lottery_prob": {
                                "type": "number"
                            },
                            "show_lottery": {
                                "type": "boolean"
                            },
                            "hidden": {
                                "type": "boolean"
                            },
                            "enable_order_push_task": {
                                "type": "boolean"
                            }
                        }
                    }
                }
            }
        }
    }