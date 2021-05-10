from api.mt.mt import Mt


class  GoodsV2(Mt):
    method = 'get'
    api = '/v2/goods/$goods_id'
    data = {
        'ui_version': 10005
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
                    "goods_id",
                    "goods_name",
                    "short_name",
                    "thumb_url",
                    "ethumb",
                    "market_price",
                    "min_group_price",
                    "min_normal_price",
                    "min_price",
                    "sales",
                    "sales_text",
                    "sales_whole_text",
                    "mall_id",
                    "money_types",
                    "footnote",
                    "promotion_mark",
                    "import_mark",
                    "marks_front",
                    "marks_back",
                    "marks_rear",
                    "mall",
                    "service_promise_mark",
                    "rdata",
                    "show_price",
                    "goods_desc",
                    "gallery_carousel",
                    "gallery_detail",
                    "no_order",
                    "order_mode",
                    "group_buy_label",
                    "overlap",
                    "type",
                    "is_refundable",
                    "core_specs",
                    "skus",
                    "single",
                    "service_promises",
                    "cat_conf",
                    "share",
                    "deduction",
                    "coin_marks",
                    "promotion_marks",
                    "price_hint",
                    "promotions",
                    "price_bar",
                    "service_assurance",
                    "goods_marks",
                    "delivery_info",
                    "ui_elements"
                ],
                "properties": {
                    "goods_id": {
                        "type": "string"
                    },
                    "goods_name": {
                        "type": "string"
                    },
                    "short_name": {
                        "type": "string"
                    },
                    "thumb_url": {
                        "type": "string"
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
                        "items": [
                            {
                                "type": "number"
                            }
                        ]
                    },
                    "footnote": {
                        "type": "string"
                    },
                    "promotion_mark": {
                        "type": "string"
                    },
                    "import_mark": {
                        "type": "string"
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
                            }
                        }
                    },
                    "service_promise_mark": {
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
                    "rdata": {
                        "type": "object",
                        "required": [
                            "ext1"
                        ],
                        "properties": {
                            "ext1": {
                                "type": "string"
                            }
                        }
                    },
                    "show_price": {
                        "type": "number"
                    },
                    "goods_desc": {
                        "type": "string"
                    },
                    "gallery_carousel": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "type": {
                                    "type": "number"
                                },
                                "url": {
                                    "type": "string"
                                }
                            }
                        }
                    },
                    "gallery_detail": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "type": {
                                    "type": "number"
                                },
                                "url": {
                                    "type": "string"
                                }
                            }
                        }
                    },
                    "no_order": {
                        "type": "number"
                    },
                    "order_mode": {
                        "type": "number"
                    },
                    "group_buy_label": {
                        "type": "string"
                    },
                    "overlap": {
                        "type": "object",
                        "required": [],
                        "properties": {}
                    },
                    "type": {
                        "type": "number"
                    },
                    "is_refundable": {
                        "type": "boolean"
                    },
                    "skus": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "sku_id": {
                                    "type": "number"
                                },
                                "thumb_url": {
                                    "type": "string"
                                },
                                "quantity": {
                                    "type": "number"
                                },
                                "is_onsale": {
                                    "type": "boolean"
                                },
                                "normal_price": {
                                    "type": "number"
                                },
                                "group_price": {
                                    "type": "number"
                                },
                                "cc": {
                                    "type": "number"
                                },
                                "spec_combo": {
                                    "type": "string"
                                },
                                "specs": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "spec_id": {
                                                "type": "number"
                                            },
                                            "spec_key": {
                                                "type": "string"
                                            },
                                            "spec_value": {
                                                "type": "string"
                                            }
                                        }
                                    }
                                },
                                "sku_price_bar": {
                                    "type": "object",
                                    "required": [
                                        "t_min_price",
                                        "react_values"
                                    ],
                                    "properties": {
                                        "t_min_price": {
                                            "type": "string"
                                        },
                                        "react_values": {
                                            "type": "object",
                                            "required": [
                                                "final_price",
                                                "line_price",
                                                "price_currency",
                                                "sold_text"
                                            ],
                                            "properties": {
                                                "final_price": {
                                                    "type": "string"
                                                },
                                                "line_price": {
                                                    "type": "string"
                                                },
                                                "price_currency": {
                                                    "type": "string"
                                                },
                                                "sold_text": {
                                                    "type": "string"
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "single": {
                        "type": "object",
                        "required": [
                            "buy_limit",
                            "order_limit",
                            "single_unity_limit"
                        ],
                        "properties": {
                            "buy_limit": {
                                "type": "number"
                            },
                            "order_limit": {
                                "type": "number"
                            },
                            "single_unity_limit": {
                                "type": "number"
                            }
                        }
                    },
                    "service_promises": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "type": {
                                    "type": "string"
                                },
                                "desc": {
                                    "type": "string"
                                },
                                "html_desc": {
                                    "type": "string"
                                },
                                "link": {
                                    "type": "string"
                                },
                                "img_ratio": {
                                    "type": "string"
                                },
                                "img_url": {
                                    "type": "string"
                                },
                                "icon": {
                                    "type": "string"
                                },
                                "id": {
                                    "type": "string"
                                }
                            }
                        }
                    },
                    "cat_conf": {
                        "type": "object",
                        "required": [
                            "receiver_type"
                        ],
                        "properties": {
                            "receiver_type": {
                                "type": "number"
                            }
                        }
                    },
                    "share": {
                        "type": "object",
                        "required": [
                            "img",
                            "link"
                        ],
                        "properties": {
                            "img": {
                                "type": "string"
                            },
                            "link": {
                                "type": "string"
                            }
                        }
                    },
                    "deduction": {
                        "type": "string"
                    },
                    "coin_marks": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "name": {
                                    "type": "string"
                                },
                                "text": {
                                    "type": "string"
                                }
                            }
                        }
                    },
                    "price_hint": {
                        "type": "string"
                    },
                    "promotions": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {}
                        }
                    },
                    "price_bar": {
                        "type": "object",
                        "required": [
                            "styles",
                            "values"
                        ],
                        "properties": {
                            "styles": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "timestamp": {
                                            "type": "number"
                                        },
                                        "id": {
                                            "type": "string"
                                        }
                                    }
                                }
                            },
                            "values": {
                                "type": "object",
                                "required": [
                                    "start_time",
                                    "end_time",
                                    "price_desc",
                                    "prime_currency",
                                    "prime_price",
                                    "final_price",
                                    "final_desc",
                                    "final_currency",
                                    "market_currency",
                                    "tp_market_price",
                                    "react_values"
                                ],
                                "properties": {
                                    "start_time": {
                                        "type": "number"
                                    },
                                    "end_time": {
                                        "type": "number"
                                    },
                                    "price_desc": {
                                        "type": "string"
                                    },
                                    "prime_currency": {
                                        "type": "string"
                                    },
                                    "prime_price": {
                                        "type": "string"
                                    },
                                    "final_price": {
                                        "type": "string"
                                    },
                                    "final_desc": {
                                        "type": "string"
                                    },
                                    "final_currency": {
                                        "type": "string"
                                    },
                                    "market_currency": {
                                        "type": "string"
                                    },
                                    "tp_market_price": {
                                        "type": "string"
                                    },
                                    "react_values": {
                                        "type": "object",
                                        "required": [
                                            "final_price",
                                            "line_price",
                                            "price_currency",
                                            "sold_text"
                                        ],
                                        "properties": {
                                            "final_price": {
                                                "type": "string"
                                            },
                                            "line_price": {
                                                "type": "string"
                                            },
                                            "price_currency": {
                                                "type": "string"
                                            },
                                            "sold_text": {
                                                "type": "string"
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "service_assurance": {
                        "type": "object",
                        "required": [
                            "icon",
                            "text",
                            "link"
                        ],
                        "properties": {
                            "icon": {
                                "type": "string"
                            },
                            "text": {
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
                            "link": {
                                "type": "string"
                            }
                        }
                    },
                    "delivery_info": {
                        "type": "object",
                        "required": [
                            "express",
                            "time_text",
                            "img",
                            "show_source_loc_icon"
                        ],
                        "properties": {
                            "express": {
                                "type": "string"
                            },
                            "time_text": {
                                "type": "string"
                            },
                            "img": {
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
                            },
                            "show_source_loc_icon": {
                                "type": "boolean"
                            }
                        }
                    },
                    "ui_elements": {
                        "type": "object",
                        "required": [
                            "sku_desc_link",
                            "show_sku_pic",
                            "sku_pic_style",
                            "swap_review_module",
                            "horizontally_review_style",
                            "button_color_type",
                            "brand_banner",
                            "product_banner_type",
                            "product_information"
                        ],
                        "properties": {
                            "sku_desc_link": {
                                "type": "object",
                                "required": [
                                    "name",
                                    "link"
                                ],
                                "properties": {
                                    "name": {
                                        "type": "string"
                                    },
                                    "link": {
                                        "type": "string"
                                    }
                                }
                            },
                            "show_sku_pic": {
                                "type": "boolean"
                            },
                            "sku_pic_style": {
                                "type": "number"
                            },
                            "swap_review_module": {
                                "type": "number"
                            },
                            "horizontally_review_style": {
                                "type": "number"
                            },
                            "button_color_type": {
                                "type": "number"
                            },
                            "product_banner_type": {
                                "type": "number"
                            },
                            "product_information": {
                                "type": "string"
                            }
                        }
                    }
                }
            }
        }
    }
