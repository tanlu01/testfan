from api.mt.mt import Mt
import os
import datetime
from random import randint


class Recommend(Mt):
    method = 'get'
    api = '/v2/mall/$mall_id/recommend'
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
                    "coupon",
                    "enter_mall_btn_link",
                    "enter_mall_btn_title",
                    "mall_icon"
                ],
                "properties": {
                    "coupon": {
                        "type": "object",
                        "required": [
                            "id",
                            "name",
                            "sub_name",
                            "mall_id",
                            "discount",
                            "usetime",
                            "link",
                            "has_received",
                            "has_useable",
                            "should_prime",
                            "btn_status",
                            "type"
                        ],
                        "properties": {
                            "id": {
                                "type": "string"
                            },
                            "name": {
                                "type": "string"
                            },
                            "sub_name": {
                                "type": "string"
                            },
                            "mall_id": {
                                "type": "number"
                            },
                            "discount": {
                                "type": "object",
                                "required": [
                                    "type",
                                    "value",
                                    "value_uint"
                                ],
                                "properties": {
                                    "type": {
                                        "type": "number"
                                    },
                                    "value": {
                                        "type": "string"
                                    },
                                    "value_uint": {
                                        "type": "number"
                                    }
                                }
                            },
                            "usetime": {
                                "type": "object",
                                "required": [
                                    "begin",
                                    "end"
                                ],
                                "properties": {
                                    "begin": {
                                        "type": "number"
                                    },
                                    "end": {
                                        "type": "number"
                                    }
                                }
                            },
                            "link": {
                                "type": "string"
                            },
                            "has_received": {
                                "type": "boolean"
                            },
                            "has_useable": {
                                "type": "boolean"
                            },
                            "should_prime": {
                                "type": "number"
                            },
                            "btn_status": {
                                "type": "number"
                            },
                            "type": {
                                "type": "number"
                            }
                        }
                    },
                    "enter_mall_btn_link": {
                        "type": "string"
                    },
                    "enter_mall_btn_title": {
                        "type": "string"
                    },
                    "mall_icon": {
                        "type": "object",
                        "required": [
                            "url",
                            "ratio"
                        ],
                        "properties": {
                            "url": {
                                "type": "string"
                            },
                            "ratio": {
                                "type": "string"
                            }
                        }
                    }
                }
            }
        }
    }