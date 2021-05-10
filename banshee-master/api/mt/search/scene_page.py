from api.mt.mt import Mt
import os
import datetime
from random import randint


class Scene_page(Mt):
    method = 'get'
    api = '/v1/search/scene/page?q=$search_keyword&cat=&sort=_default&offset&size=10'
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
                    "banner",
                    "banner_link",
                    "is_black",
                    "total",
                    "offset",
                    "qc",
                    "ctx",
                    "expand_filters",
                    "inject_filters"
                ],
                "properties": {
                    "items": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {

                            }
                        }
                    },
                    "banner": {
                        "type": "string"
                    },
                    "banner_link": {
                        "type": "string"
                    },
                    "is_black": {
                        "type": "boolean"
                    },
                    "total": {
                        "type": "number"
                    },
                    "offset": {
                        "type": "string"
                    },
                    "qc": {
                        "type": "string"
                    },
                    "ctx": {
                        "type": "string"
                    },
                    "expand_filters": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "key": {
                                    "type": "string"
                                },
                                "title": {
                                    "type": "string"
                                },
                                "is_expanded": {
                                    "type": "boolean"
                                },
                                "expand_style": {
                                    "type": "number"
                                },
                                "multi": {
                                    "type": "boolean"
                                }
                            }
                        }
                    },
                    "inject_filters": {
                        "type": "string"
                    }
                }
            }
        }
    }
