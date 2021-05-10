from api.mt.mt import Mt
import os
import datetime
from random import randint


class Reviews(Mt):
    method = 'get'
    api = '/v1/order/$order_id/reviews'
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
                    "review",
                    "append_review"
                ],
                "properties": {
                    "review": {
                        "type": "object",
                        "required": [
                            "nickname",
                            "avatar",
                            "member",
                            "member_badge",
                            "title",
                            "text",
                            "medias",
                            "is_member",
                            "member_expire_at",
                            "goods_id",
                            "goods_thumb",
                            "goods_name",
                            "ext_goods_id",
                            "goods_unit_price"
                        ],
                        "properties": {
                            "nickname": {
                                "type": "string"
                            },
                            "avatar": {
                                "type": "string"
                            },
                            "member": {
                                "type": "number"
                            },
                            "member_badge": {
                                "type": "string"
                            },
                            "title": {
                                "type": "string"
                            },
                            "text": {
                                "type": "string"
                            },
                            "is_member": {
                                "type": "boolean"
                            },
                            "member_expire_at": {
                                "type": "number"
                            },
                            "goods_id": {
                                "type": "number"
                            },
                            "goods_thumb": {
                                "type": "string"
                            },
                            "goods_name": {
                                "type": "string"
                            },
                            "ext_goods_id": {
                                "type": "number"
                            },
                            "goods_unit_price": {
                                "type": "number"
                            }
                        }
                    },
                    "append_review": {
                        "type": "object",
                        "required": [
                            "nickname",
                            "avatar",
                            "member",
                            "member_badge",
                            "title",
                            "text",
                            "medias",
                            "is_member",
                            "member_expire_at",
                            "goods_id",
                            "goods_thumb",
                            "goods_name",
                            "ext_goods_id",
                            "goods_unit_price"
                        ],
                        "properties": {
                            "nickname": {
                                "type": "string"
                            },
                            "avatar": {
                                "type": "string"
                            },
                            "member": {
                                "type": "number"
                            },
                            "member_badge": {
                                "type": "string"
                            },
                            "title": {
                                "type": "string"
                            },
                            "text": {
                                "type": "string"
                            },
                            "is_member": {
                                "type": "boolean"
                            },
                            "member_expire_at": {
                                "type": "number"
                            },
                            "goods_id": {
                                "type": "number"
                            },
                            "goods_thumb": {
                                "type": "string"
                            },
                            "goods_name": {
                                "type": "string"
                            },
                            "ext_goods_id": {
                                "type": "number"
                            },
                            "goods_unit_price": {
                                "type": "number"
                            }
                        }
                    }
                }
            }
        }
    }