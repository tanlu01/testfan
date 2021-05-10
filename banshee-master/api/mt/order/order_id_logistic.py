from api.mt.mt import Mt
import os
import datetime
from random import randint


class Logistic(Mt):
    method = 'get'
    api = '/v1/order/$order_id/logistic'
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
                    "items",
                    "tips"
                ],
                "properties": {
                    "items": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "number"
                                },
                                "type": {
                                    "type": "number"
                                },
                                "order_id": {
                                    "type": "string"
                                },
                                "aftersale_id": {
                                    "type": "string"
                                },
                                "status": {
                                    "type": "number"
                                },
                                "ship_time": {
                                    "type": "number"
                                },
                                "recv_time": {
                                    "type": "number"
                                },
                                "express_id": {
                                    "type": "number"
                                },
                                "express_name": {
                                    "type": "string"
                                },
                                "express_tel": {
                                    "type": "string"
                                },
                                "tracking_num": {
                                    "type": "string"
                                },
                                "tracking_detail": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "time": {
                                                "type": "string"
                                            },
                                            "title": {
                                                "type": "string"
                                            },
                                            "desc": {
                                                "type": "string"
                                            }
                                        }
                                    }
                                },
                                "home_link": {
                                    "type": "string"
                                }
                            }
                        }
                    }
                }
            }
        }
    }
