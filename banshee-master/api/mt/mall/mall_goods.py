from api.mt.mt import Mt


class MallGoods(Mt):
    method = 'get'
    api = '/v1/mall/$mall_id/goods?offset=&size=20&sort=default'
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
                    "offset"
                ],
                "properties": {
                    "items": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "goods_id": {
                                    "type": "string"
                                },
                                "goods_name": {
                                    "type": "string"
                                },
                                "thumb_url": {
                                    "type": "string"
                                },
                                "market_price": {
                                    "type": "number"
                                },
                                "min_group_price": {
                                    "type": "number"
                                },
                                "min_normal_price": {
                                    "type": "number"
                                },
                                "min_price": {
                                    "type": "number"
                                },
                                "sales": {
                                    "type": "number"
                                },
                                "sales_text": {
                                    "type": "string"
                                },
                                "sales_whole_text": {
                                    "type": "string"
                                },
                                "mall_id": {
                                    "type": "number"
                                },
                                "money_types": {
                                    "type": "array",
                                    "items": [{'type': 'number'}]
                                },
                                "footnote": {
                                    "type": "string"
                                },
                                "footnote_position": {
                                    "type": "object",
                                    "required": [
                                        "x",
                                        "y"
                                    ],
                                    "properties": {
                                        "x": {
                                            "type": "number"
                                        },
                                        "y": {
                                            "type": "number"
                                        }
                                    }
                                },
                                "ethumb": {
                                    "type": "object",
                                    "required": [
                                        "img",
                                        "ratio"
                                    ],
                                    "properties": {
                                        "img": {
                                            "type": "string"
                                        },
                                        "ratio": {
                                            "type": "string"
                                        }
                                    }
                                },
                                "avatars": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {

                                        }
                                    }
                                },
                                "tdata": {
                                    "type": "string"
                                },
                                "break_payment_limit": {
                                    "type": "boolean"
                                },
                                "mark_coll": {
                                    "type": "object",
                                    "required": [

                                    ],
                                    "properties": {

                                    }
                                },
                                "marks_front": {
                                    "type": None
                                },
                                "marks_back": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "id": {
                                                "type": "string"
                                            },
                                            "text": {
                                                "type": "string"
                                            },
                                            "style": {
                                                "type": "number"
                                            },
                                            "name": {
                                                "type": "string"
                                            },
                                            "img_url": {
                                                "type": "string"
                                            },
                                            "img_ratio": {
                                                "type": "string"
                                            },
                                            "link": {
                                                "type": "string"
                                            },
                                            "icon_url": {
                                                "type": "string"
                                            },
                                            "icon_ratio": {
                                                "type": "string"
                                            }
                                        }
                                    }
                                },
                                "marks_rear": {
                                    "type": None
                                },
                                "sold_out": {
                                    "type": "boolean"
                                },
                                "dispatch_place": {
                                    "type": "string"
                                },
                                "mall": {
                                    "type": "object",
                                    "required": [
                                        "mall_id",
                                        "mall_name",
                                        "location",
                                        "labels"
                                    ],
                                    "properties": {
                                        "mall_id": {
                                            "type": "string"
                                        },
                                        "mall_name": {
                                            "type": "string"
                                        },
                                        "location": {
                                            "type": "string"
                                        },
                                        "labels": {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "type": {
                                                        "type": "string"
                                                    }
                                                }
                                            }
                                        }
                                    }
                                },
                                "show_price": {
                                    "type": "number"
                                },
                                "sku_extends": {
                                    "type": "object",
                                    "required": [

                                    ],
                                    "properties": {

                                    }
                                }
                            }
                        }
                    },
                    "offset": {
                        "type": "string"
                    }
                }
            }
        }
    }
