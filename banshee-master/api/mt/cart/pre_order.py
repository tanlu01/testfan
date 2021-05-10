from api.mt.mt import Mt


class GetPreOrder(Mt):
    method = 'get'
    api = '/v1/cart/pre_order'
    data = {}

    expected_schema = {
        "$schema": "http://json-schema.org/draft-06/schema#",
        "title": "expected_data",
        "type": "object",
        "required": ["code", "time", 'data'],
        "properties": {
            "code": {"type": "number"},
            "time": {"type": "number"},
            'data': {
                'type': 'object',
                "required": ["malls", 'sku_quantity', 'cart_skus'],
                'properties': {
                    'malls': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'mall_id': {"type": "number"},
                                'mall_name': {"type": "string"},
                                'logo': {"type": "string"},
                                'logo_origin': {"type": "string"},
                                'background_img': {"type": "string"},
                                'mall_sales': {"type": "number"},
                                'company_phone': {"type": "string"},
                                'goods_num': {"type": "number"},
                                'mall_desc': {"type": "number"},
                                'coupons': {
                                    "type": "array",
                                    'items': {
                                        'type': 'object',
                                        'properties': {}
                                    }
                                },
                                'is_open': {"type": "boolean"},
                                'mall_share': {
                                    'type': 'object',
                                    "required": ["link", "img"],
                                    'properties': {
                                        'link': {"type": "string"},
                                        'img': {"type": "string"}
                                    }
                                },
                                'mall_icon': {
                                    'type': 'object',
                                    "required": ["url", "ratio"],
                                    'properties': {
                                        'url': {"type": "string"},
                                        'ratio': {"type": "string"}
                                    }
                                },
                                'followers': {"type": "number"},
                                'wallpaper': {"type": "string"},
                                'category_link': {"type": "string"},
                                'mall_score': {
                                    'type': 'object',
                                    "required": ["shipping_rating", "description_rating", 'service_rating'],
                                    'properties': {
                                        'shipping_rating': {"type": "boolean"},
                                        'description_rating': {"type": "boolean"},
                                        'service_rating': {"type": "boolean"}
                                    }
                                },
                                'mall_score_int': {
                                    'type': 'object',
                                    "required": ["shipping_rating", "description_rating", 'service_rating'],
                                    'properties': {
                                        'shipping_rating': {"type": "number"},
                                        'description_rating': {"type": "number"},
                                        'service_rating': {"type": "number"}
                                    }
                                },
                                'mall_labels': {"type": None},
                                'goods': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'goods_id': {'type': 'string'},
                                            'goods_name': {'type': 'string'},
                                            'store_name': {'type': 'string'},
                                            'thumb_url': {'type': 'string'},
                                            'ethumb': {
                                                'type': 'object',
                                                "required": ["img", "ratio"],
                                                'properties': {
                                                    'img': {"type": "string"},
                                                    'ratio': {"type": "string"}
                                                }
                                            },
                                            'market_price': {'type': 'number'},
                                            'min_group_price': {'type': 'number'},
                                            'min_normal_price': {'type': 'number'},
                                            'min_price': {'type': 'number'},
                                            'sale': {'type': 'number'},
                                            'sale_text': {'type': 'string'},
                                            'sale_whole_text': {'type': 'string'},
                                            'mall_id': {'type': 'number'},
                                            'money_types': {
                                                'type': 'array',
                                                'items': {
                                                    'type': 'object',
                                                    'properties': {}
                                                }
                                            },
                                            'footnote': {'type': 'string'},
                                            'promotion_mark': {'type': 'string'},
                                            'import_mark': {'type': 'string'},
                                            'marks_font': {'type': None},
                                            'marks_back': {'type': None},
                                            'marks_rear': {'type': None},
                                            'mall': {
                                                'type': 'object',
                                                "required": ["mall_id", "mall_name", 'location', 'labels'],
                                                'properties': {
                                                    'mall_id': {"type": "string"},
                                                    'mall_name': {"type": "string"},
                                                    'location': {"type": "string"},
                                                    'labels': {"type": None}
                                                }
                                            },
                                            'service_promise_mark': {
                                                'type': 'array',
                                                'items': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'id': {"type": "string"},
                                                        'text': {"type": "string"},
                                                        'style': {"type": "number"},
                                                        'name': {"type": "string"},
                                                        'img_url': {"type": "string"},
                                                        'img_ratio': {"type": "string"},
                                                        'link': {"type": "string"},
                                                        'icon_url': {"type": "string"},
                                                        'icon_ratio': {"type": "string"},
                                                    }
                                                }
                                            },
                                            'show_price': {"type": "number"},
                                            'goods_desc': {"type": "number"},
                                            'gallery_carousel': {
                                                'type': 'array',
                                                'items': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'type': {"type": "number"},
                                                        'url': {"type": "string"}
                                                    }
                                                }
                                            },
                                            'gallery_detail': {
                                                'type': 'array',
                                                'items': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'type': {"type": "number"},
                                                        'url': {"type": "string"}
                                                    }
                                                }
                                            },
                                            'order_mode': {"type": "number"},
                                            'group_buy_label': {"type": "string"},
                                            'overlap': {
                                                'type': 'object',
                                                "required": [],
                                                'properties': {}
                                            },
                                            'type': {"type": "number"},
                                            'is_refundable': {"type": "boolean"},
                                            'core_specs': {"type": None},
                                            'skus': {
                                                'type': 'array',
                                                'items': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'sku_id': {"type": "number"},
                                                        'thumb_url': {"type": "string"},
                                                        'quantity': {"type": "number"},
                                                        'is_onsale': {"type": 'boolean'},
                                                        'normal_price': {"type": 'number'},
                                                        'group_price': {"type": 'number'},
                                                        'cc': {"type": 'number'},
                                                        'spec_combo': {"type": 'string'},
                                                        'specs': {
                                                            'type': 'array',
                                                            'items': {
                                                                'type': 'object',
                                                                'properties': {
                                                                    'spec_id': {"type": "number"},
                                                                    'spec_key': {"type": "string"},
                                                                    'spec_value': {"type": "string"}
                                                                }
                                                            }
                                                        }
                                                    }
                                                }
                                            },
                                            'single': {
                                                'type': 'object',
                                                "required": ["buy_limit", "order_limit", 'single_unity_limit'],
                                                'properties': {
                                                    'buy_limit': {"type": "number"},
                                                    'order_limit': {"type": "number"},
                                                    'single_unity_limit': {"type": "number"}
                                                }
                                            },
                                            'service_promises': {
                                                'type': 'array',
                                                'items': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'type': {"type": "string"},
                                                        'desc': {"type": "string"},
                                                        'html_desc': {"type": "string"},
                                                        'link': {"type": "string"},
                                                        'img_ratio': {"type": "string"},
                                                        'img_url': {"type": "string"},
                                                        'icon': {"type": "string"},
                                                        'id': {"type": "string"}
                                                    }
                                                }
                                            },
                                            'cat_conf': {
                                                'type': 'object',
                                                "required": ["receiver_type"],
                                                'properties': {
                                                    'receiver_type': {"type": "number"}
                                                }
                                            },
                                            'share': {
                                                'type': 'object',
                                                "required": ["img", 'link'],
                                                'properties': {
                                                    'img': {"type": "string"},
                                                    'link': {"type": "string"}
                                                }
                                            },
                                            'deduction': {"type": "string"},
                                            'coin_marks': {
                                                'type': 'array',
                                                'items': {
                                                    'type': 'object',
                                                    'properties': {
                                                        'name': {"type": "string"},
                                                        'text': {"type": "string"}
                                                    }
                                                }
                                            },
                                            'promotion_marks': {"type": None},
                                            'goods_marks': {"type": None},
                                            'price_hint': {"type": "string"},
                                            'promotions': {
                                                'type': 'array',
                                                'items': {
                                                    'type': 'object',
                                                    'properties': {}
                                                }
                                            },
                                            'service_assurance': {
                                                'type': 'object',
                                                'required': ['icon', 'text', 'link'],
                                                'properties': {
                                                    'icon': {"type": "string"},
                                                    'link': {"type": "string"},
                                                    'text': {
                                                        "type": "array",
                                                        'items': [
                                                            {'type': 'string'},
                                                            {'type': 'string'}
                                                        ]
                                                    },
                                                }
                                            },
                                            'delivery_info': {
                                                'type': 'object',
                                                'required': ['express', 'time_text', 'img', 'show_source_loc_icon'],
                                                'properties': {
                                                    'express': {"type": "string"},
                                                    'time_text': {"type": "string"},
                                                    'show_source_loc_icon': {"type": "boolean"},
                                                    'img': {
                                                        'type': 'object',
                                                        'required': ['url', 'ratio'],
                                                        'properties': {
                                                            'url': {"type": "string"},
                                                            'ratio': {"type": "string"}
                                                        }
                                                    }
                                                }
                                            },
                                            'ui_elements': {
                                                'type': 'object',
                                                'required': ['sku_desc_link', 'show_sku_pic', 'sku_pic_style',
                                                             'swap_review_module', 'horizontally_review_style',
                                                             'button_color_type', 'brand_banner', 'product_banner_type',
                                                             'product_information'],
                                                'properties': {
                                                    'sku_desc_link': {"type": None},
                                                    'show_sku_pic': {"type": "boolean"},
                                                    'sku_pic_style': {"type": "number"},
                                                    'swap_review_module': {"type": "number"},
                                                    'horizontally_review_style': {"type": "number"},
                                                    'button_color_type': {"type": "number"},
                                                    'brand_banner': {"type": None},
                                                    'product_banner_type': {"type": 'number'},
                                                    'product_information': {"type": 'string'}
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    'sku_quantity': {
                        'type': 'object',
                        'required': ['goods_id', 'sku_id', 'quantity'],
                        'properties': {
                            'goods_id': {"type": 'string'},
                            'sku_id': {"type": 'number'},
                            'quantity': {"type": 'number'}
                        }
                    },
                    'cart_skus': {
                        'type': 'object',
                        'required': ['goods_id', 'sku_id', 'quantity'],
                        'properties': {
                            'goods_id': {"type": 'string'},
                            'sku_id': {"type": 'number'},
                            'quantity': {"type": 'number'}
                        }
                    }
                }
            }
        }
    }


class PostPreOrder(Mt):
    method = 'post'
    api = '/v1/cart/pre_order'
    data = {
        "sku_ids": [],
        "goods_sku_ids": [
            {
                "sku_id": 99937,
                "goods_id": "102858"
            }
        ]
    }

    expected_schema = {
        "$schema": "http://json-schema.org/draft-06/schema#",
        "title": "expected_data",
        "type": "object",
        "required": ["code", "time"],
        "properties": {
            "code": {"type": "number"},
            "time": {"type": "number"}
        }
    }
