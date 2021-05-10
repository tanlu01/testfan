from api.oms.oms_ import Oms


class Audit(Oms):
    method = 'post'
    api = '/goodsaudit/audit'
    data = {
        'id': 100005506,
        'audit_status': 15,
        'pso_thumb_machine_state': 10,
        'old_leaf_cat_id': 10034,
        'old_brand_id': 147,
        'rule_brand_state': 1,
        'third_url': '',
        'goods_commit': '',
        'judge_result': {},
        'remain_seconds': 22,
        'remain_open_time': 1606128800134,
        'remain_over_time': 1606128822147
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }

    expected_schema = {
        "$schema": "http://json-schema.org/draft-06/schema",
        "type": "object",
        "title": "The root schema",
        "required": [
            "code",
            "payload"
        ],
        "properties": {
            "code": {
                "type": "integer",
                "title": "The code schema"
            },
            "payload": {
                "type": "object",
                "title": "The payload schema",
                "required": [
                    "auto_dispatch",
                    "next",
                    "status"
                ],
                "properties": {
                    "auto_dispatch": {
                        "type": "integer",
                        "title": "The auto_dispatch schema"
                    },
                    "next": {
                        "type": "string",
                        "title": "The next schema"
                    },
                    "status": {
                        "type": "object",
                        "title": "The status schema",
                        "required": [
                            "audit_status",
                            "goods_commit",
                            "id",
                            "judge_result",
                            "old_brand_id",
                            "old_leaf_cat_id",
                            "pso_thumb_machine_state",
                            "remain_open_time",
                            "remain_over_time",
                            "remain_seconds",
                            "rule_brand_state",
                            "third_url"
                        ],
                        "properties": {
                            "audit_status": {
                                "type": "integer",
                                "title": "The audit_status schema"
                            },
                            "goods_commit": {
                                "type": "object",
                                "title": "The goods_commit schema",
                                "required": [
                                    "biz",
                                    "brand_id",
                                    "brand_name",
                                    "brands",
                                    "carousel_pics",
                                    "cat_id",
                                    "cost_template_id",
                                    "custom_specs",
                                    "detail_pics",
                                    "ethumb_url",
                                    "event_type",
                                    "features",
                                    "food_safety",
                                    "footnote",
                                    "goods_desc_json",
                                    "goods_tags",
                                    "id",
                                    "image_url",
                                    "is_new",
                                    "is_onsale",
                                    "is_original_auth",
                                    "is_pre_sale",
                                    "is_pulish",
                                    "is_refundable",
                                    "market_price",
                                    "name",
                                    "normal_price",
                                    "out_goods_sn",
                                    "second_hand_goods",
                                    "shipment_limit_second",
                                    "single_meta",
                                    "sku",
                                    "spec_tpl_id",
                                    "thumb_url",
                                    "total_stock",
                                    "type",
                                    "use_new_tpl",
                                    "video_id",
                                    "video_url",
                                    "weight"
                                ],
                                "properties": {
                                    "biz": {
                                        "type": "object",
                                        "title": "The biz schema",
                                        "required": [
                                            "expiration_date",
                                            "goods_images",
                                            "produced_date",
                                            "product_licence",
                                            "product_standard_num"
                                        ],
                                        "properties": {
                                            "expiration_date": {
                                                "type": "string",
                                                "title": "The expiration_date schema"
                                            },
                                            "goods_images": {
                                                "type": "array",
                                                "title": "The goods_images schema",
                                                "items": {
                                                    "anyOf": [
                                                        {
                                                            "type": "string",
                                                            "title": "The first anyOf schema"
                                                        }
                                                    ]
                                                }
                                            },
                                            "produced_date": {
                                                "type": "array",
                                                "title": "The produced_date schema",
                                                "items": {
                                                    "anyOf": [
                                                        {
                                                            "type": "string",
                                                            "title": "The first anyOf schema"
                                                        }
                                                    ]
                                                }
                                            },
                                            "product_licence": {
                                                "type": "string",
                                                "title": "The product_licence schema"
                                            },
                                            "product_standard_num": {
                                                "type": "string",
                                                "title": "The product_standard_num schema"
                                            }
                                        }
                                    },
                                    "brand_id": {
                                        "type": "string",
                                        "title": "The brand_id schema"
                                    },
                                    "brand_name": {
                                        "type": "string",
                                        "title": "The brand_name schema"
                                    },
                                    "brands": {
                                        "type": "array",
                                        "title": "The brands schema",
                                        "items": {}
                                    },
                                    "carousel_pics": {
                                        "type": "array",
                                        "title": "The carousel_pics schema",
                                        "items": {
                                            "anyOf": [
                                                {
                                                    "type": "string",
                                                    "title": "The first anyOf schema"
                                                }
                                            ]
                                        }
                                    },
                                    "cat_id": {
                                        "type": "array",
                                        "title": "The cat_id schema",
                                        "items": {
                                            "anyOf": [
                                                {
                                                    "type": "string",
                                                    "title": "The first anyOf schema"
                                                }
                                            ]
                                        }
                                    },
                                    "cost_template_id": {
                                        "type": "string",
                                        "title": "The cost_template_id schema"
                                    },
                                    "custom_specs": {
                                        "type": "array",
                                        "title": "The custom_specs schema",
                                        "items": {}
                                    },
                                    "detail_pics": {
                                        "type": "array",
                                        "title": "The detail_pics schema",
                                        "items": {
                                            "anyOf": [
                                                {
                                                    "type": "string",
                                                    "title": "The first anyOf schema"
                                                }
                                            ]
                                        }
                                    },
                                    "ethumb_url": {
                                        "type": "string",
                                        "title": "The ethumb_url schema"
                                    },
                                    "event_type": {
                                        "type": "string",
                                        "title": "The event_type schema"
                                    },
                                    "features": {
                                        "type": "string",
                                        "title": "The features schema"
                                    },
                                    "food_safety": {
                                        "type": "object",
                                        "title": "The food_safety schema",
                                        "required": [
                                            "quality_guarantee_period"
                                        ],
                                        "properties": {
                                            "quality_guarantee_period": {
                                                "type": "string",
                                                "title": "The quality_guarantee_period schema"
                                            }
                                        }
                                    },
                                    "footnote": {
                                        "type": "string",
                                        "title": "The footnote schema"
                                    },
                                    "goods_desc_json": {
                                        "type": "array",
                                        "title": "The goods_desc_json schema",
                                        "items": {}
                                    },
                                    "goods_tags": {
                                        "type": "array",
                                        "title": "The goods_tags schema",
                                        "items": {}
                                    },
                                    "id": {
                                        "type": "string",
                                        "title": "The id schema"
                                    },
                                    "image_url": {
                                        "type": "string",
                                        "title": "The image_url schema"
                                    },
                                    "is_new": {
                                        "type": "string",
                                        "title": "The is_new schema"
                                    },
                                    "is_onsale": {
                                        "type": "string",
                                        "title": "The is_onsale schema"
                                    },
                                    "is_original_auth": {
                                        "type": "string",
                                        "title": "The is_original_auth schema"
                                    },
                                    "is_pre_sale": {
                                        "type": "string",
                                        "title": "The is_pre_sale schema"
                                    },
                                    "is_pulish": {
                                        "type": "boolean",
                                        "title": "The is_pulish schema"
                                    },
                                    "is_refundable": {
                                        "type": "string",
                                        "title": "The is_refundable schema"
                                    },
                                    "market_price": {
                                        "type": "integer",
                                        "title": "The market_price schema"
                                    },
                                    "name": {
                                        "type": "string",
                                        "title": "The name schema"
                                    },
                                    "normal_price": {
                                        "type": "integer",
                                        "title": "The normal_price schema"
                                    },
                                    "out_goods_sn": {
                                        "type": "string",
                                        "title": "The out_goods_sn schema"
                                    },
                                    "second_hand_goods": {
                                        "type": "string",
                                        "title": "The second_hand_goods schema"
                                    },
                                    "shipment_limit_second": {
                                        "type": "integer",
                                        "title": "The shipment_limit_second schema"
                                    },
                                    "single_meta": {
                                        "type": "object",
                                        "title": "The single_meta schema",
                                        "required": [
                                            "buy_limit",
                                            "order_limit"
                                        ],
                                        "properties": {
                                            "buy_limit": {
                                                "type": "integer",
                                                "title": "The buy_limit schema"
                                            },
                                            "order_limit": {
                                                "type": "integer",
                                                "title": "The order_limit schema"
                                            }
                                        }
                                    },
                                    "sku": {
                                        "type": "object",
                                        "title": "The sku schema",
                                        "required": [
                                            "detail",
                                            "spec_one",
                                            "spec_one_sub",
                                            "spec_two",
                                            "spec_two_sub",
                                            "spec_type"
                                        ],
                                        "properties": {
                                            "detail": {
                                                "type": "array",
                                                "title": "The detail schema",
                                                "items": {
                                                    "anyOf": [
                                                        {
                                                            "type": "object",
                                                            "title": "The first anyOf schema",
                                                            "required": [
                                                                "bar_codes",
                                                                "cost",
                                                                "is_onsale",
                                                                "key",
                                                                "normal_price",
                                                                "out_sku_sn",
                                                                "prime_price",
                                                                "spec_one_sub",
                                                                "spec_one_sub_remark",
                                                                "spec_two_sub",
                                                                "spec_two_sub_remark",
                                                                "stock",
                                                                "thumb_url",
                                                                "type"
                                                            ],
                                                            "properties": {
                                                                "bar_codes": {
                                                                    "type": "array",
                                                                    "title": "The bar_codes schema",
                                                                    "items": {}
                                                                },
                                                                "cost": {
                                                                    "type": "integer",
                                                                    "title": "The cost schema"
                                                                },
                                                                "is_onsale": {
                                                                    "type": "string",
                                                                    "title": "The is_onsale schema"
                                                                },
                                                                "key": {
                                                                    "type": "string",
                                                                    "title": "The key schema"
                                                                },
                                                                "normal_price": {
                                                                    "type": "integer",
                                                                    "title": "The normal_price schema"
                                                                },
                                                                "out_sku_sn": {
                                                                    "type": "string",
                                                                    "title": "The out_sku_sn schema"
                                                                },
                                                                "prime_price": {
                                                                    "type": "integer",
                                                                    "title": "The prime_price schema"
                                                                },
                                                                "spec_one_sub": {
                                                                    "type": "integer",
                                                                    "title": "The spec_one_sub schema"
                                                                },
                                                                "spec_one_sub_remark": {
                                                                    "type": "string",
                                                                    "title": "The spec_one_sub_remark schema"
                                                                },
                                                                "spec_two_sub": {
                                                                    "type": "integer",
                                                                    "title": "The spec_two_sub schema"
                                                                },
                                                                "spec_two_sub_remark": {
                                                                    "type": "string",
                                                                    "title": "The spec_two_sub_remark schema"
                                                                },
                                                                "stock": {
                                                                    "type": "integer",
                                                                    "title": "The stock schema"
                                                                },
                                                                "thumb_url": {
                                                                    "type": "string",
                                                                    "title": "The thumb_url schema"
                                                                },
                                                                "type": {
                                                                    "type": "integer",
                                                                    "title": "The type schema"
                                                                }
                                                            }
                                                        }
                                                    ]
                                                }
                                            },
                                            "spec_one": {
                                                "type": "integer",
                                                "title": "The spec_one schema"
                                            },
                                            "spec_one_sub": {
                                                "type": "array",
                                                "title": "The spec_one_sub schema",
                                                "items": {
                                                    "anyOf": [
                                                        {
                                                            "type": "integer",
                                                            "title": "The first anyOf schema"
                                                        }
                                                    ]
                                                }
                                            },
                                            "spec_two": {
                                                "type": "integer",
                                                "title": "The spec_two schema"
                                            },
                                            "spec_two_sub": {
                                                "type": "array",
                                                "title": "The spec_two_sub schema",
                                                "items": {
                                                    "anyOf": [
                                                        {
                                                            "type": "integer",
                                                            "title": "The first anyOf schema"
                                                        }
                                                    ]
                                                }
                                            },
                                            "spec_type": {
                                                "type": "integer",
                                                "title": "The spec_type schema"
                                            }
                                        }
                                    },
                                    "spec_tpl_id": {
                                        "type": "integer",
                                        "title": "The spec_tpl_id schema"
                                    },
                                    "thumb_url": {
                                        "type": "string",
                                        "title": "The thumb_url schema"
                                    },
                                    "total_stock": {
                                        "type": "integer",
                                        "title": "The total_stock schema"
                                    },
                                    "type": {
                                        "type": "string",
                                        "title": "The type schema"
                                    },
                                    "use_new_tpl": {
                                        "type": "integer",
                                        "title": "The use_new_tpl schema"
                                    },
                                    "video_id": {
                                        "type": "string",
                                        "title": "The video_id schema"
                                    },
                                    "video_url": {
                                        "type": "string",
                                        "title": "The video_url schema"
                                    },
                                    "weight": {
                                        "type": "string",
                                        "title": "The weight schema"
                                    }
                                }
                            },
                            "id": {
                                "type": "integer",
                                "title": "The id schema"
                            },
                            "judge_result": {
                                "type": "array",
                                "title": "The judge_result schema",
                                "items": {}
                            },
                            "old_brand_id": {
                                "type": "integer",
                                "title": "The old_brand_id schema"
                            },
                            "old_leaf_cat_id": {
                                "type": "integer",
                                "title": "The old_leaf_cat_id schema"
                            },
                            "pso_thumb_machine_state": {
                                "type": "integer",
                                "title": "The pso_thumb_machine_state schema"
                            },
                            "remain_open_time": {
                                "type": "integer",
                                "title": "The remain_open_time schema"
                            },
                            "remain_over_time": {
                                "type": "integer",
                                "title": "The remain_over_time schema"
                            },
                            "remain_seconds": {
                                "type": "integer",
                                "title": "The remain_seconds schema"
                            },
                            "rule_brand_state": {
                                "type": "integer",
                                "title": "The rule_brand_state schema"
                            },
                            "third_url": {
                                "type": "string",
                                "title": "The third_url schema"
                            }
                        }
                    }
                }
            }
        }
    }
