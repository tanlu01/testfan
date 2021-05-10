from api.mt.mt import Mt
import os
import datetime
from random import randint


class Detail(Mt):
    method = 'get'
    api = '/v1/mall/$mall_id/detail'
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
                    "mall_id",
                    "master_name",
                    "company_phone",
                    "location",
                    "open_time",
                    "logo",
                    "mall_name",
                    "has_qualifications",
                    "qualification_params"
                ],
                "properties": {
                    "mall_id": {
                        "type": "number"
                    },
                    "master_name": {
                        "type": "string"
                    },
                    "company_phone": {
                        "type": "string"
                    },
                    "location": {
                        "type": "string"
                    },
                    "open_time": {
                        "type": "number"
                    },
                    "logo": {
                        "type": "string"
                    },
                    "mall_name": {
                        "type": "string"
                    },
                    "has_qualifications": {
                        "type": "object",
                        "required": [
                            "food_distribution_license",
                            "qualification"
                        ],
                        "properties": {
                            "food_distribution_license": {
                                "type": "boolean"
                            },
                            "qualification": {
                                "type": "boolean"
                            }
                        }
                    },
                    "qualification_params": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "license_type": {
                                    "type": "string"
                                },
                                "name": {
                                    "type": "string"
                                }
                            }
                        }
                    }
                }
            }
        }
    }
