from api.lego.lego import Lego


class Create(Lego):
    method = 'post'
    api = '/api/lego/project'
    data = {
        "project_name": "12345",
        "start_time": 1610366463328,
        "end_time": 1610380800000,
        "project_code": "",
        "type": 1,
        "model_style": 0
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }


class AddItems(Lego):
    method = 'post'
    api = '/api/lego/brick'
    data = {
        "page_id": 600,
        "brick_type_code": "marketing_coupon",
        "category": 1,
        "is_temp": True
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }


class SaveItems(Lego):
    method = 'put'
    api = '/api/lego/page/$project_id/save'
    data = {
        "conf": {
            "category": 0,
            "brick_name": "标题栏",
            "config": {
                "show_car": 1,
                "open_modal": 0,
                "open_exps": 0,
                "exps_name": "",
                "page_background_color": "#FFFFFF",
                "page_background_image": {
                    "url": "",
                    "ratio": 0,
                    "width": 0,
                    "height": 0
                },
                "page_background_attachment": 0,
                "open_prime_first_price": 0,
                "open_back_modal": 0,
                "redirect_url": "",
                "redirect_replace": 0,
                "scene_value": {
                    "id": "",
                    "name": "",
                    "key": ""
                },
                "custom_key": {},
                "open_gql": 0,
                "title": {
                    "text": "123456",
                    "color": "#333333",
                    "background_color": "#FFFFFF",
                    "background_image": {
                        "url": "",
                        "ratio": 0,
                        "width": 0,
                        "height": 0
                    }
                },
                "no_title_text_in_app": 0,
                "share_data": {
                    "is_open": 0,
                    "share_title": "",
                    "share_link": "",
                    "share_pic": {
                        "url": "",
                        "ratio": 0,
                        "width": 0,
                        "height": 0
                    },
                    "share_pic_mini": {
                        "url": "",
                        "ratio": 0,
                        "width": 0,
                        "height": 0
                    },
                    "share_desc": ""
                },
                "custom_code": ""
            },
            "id": 8864,
            "brick_type": "title"
        },
        "bricks": [
            {
                "category": 1,
                "brick_name": "优惠券",
                "config": {
                    "layout": 1,
                    "surface": 1,
                    "type_style": 1,
                    "normal_img": {
                        "url": "",
                        "ratio": 0,
                        "width": 0,
                        "height": 0
                    },
                    "claim_again_img": {
                        "url": "",
                        "ratio": 0,
                        "width": 0,
                        "height": 0
                    },
                    "received_img": {
                        "url": "",
                        "ratio": 0,
                        "width": 0,
                        "height": 0
                    },
                    "disabled_img": {
                        "url": "",
                        "ratio": 0,
                        "width": 0,
                        "height": 0
                    },
                    "has_vip": 1,
                    "coupon_source": 1,
                    "vip_normal_img": {
                        "url": "",
                        "ratio": 0,
                        "width": 0,
                        "height": 0
                    },
                    "vip_claim_again_img": {
                        "url": "",
                        "ratio": 0,
                        "width": 0,
                        "height": 0
                    },
                    "vip_received_img": {
                        "url": "",
                        "ratio": 0,
                        "width": 0,
                        "height": 0
                    },
                    "vip_disabled_img": {
                        "url": "",
                        "ratio": 0,
                        "width": 0,
                        "height": 0
                    },
                    "show_countdown": 0,
                    "countdown_background_color": "#ffffff",
                    "countdown_font_color": "#FF0E48",
                    "is_jump": 0,
                    "sign": "50adffcae01b24b5a768194bec867625",
                    "auto_receive": 0,
                    "items": [
                        {
                            "target_type": "7",
                            "target_val": "8610348904537440256",
                            "target_text": "8610348904537440256 | 满11减5",
                            "normal_img": {
                                "url": "",
                                "ratio": 0,
                                "width": 0,
                                "height": 0
                            },
                            "received_img": {
                                "url": "",
                                "ratio": 0,
                                "width": 0,
                                "height": 0
                            },
                            "disabled_img": {
                                "url": "",
                                "ratio": 0,
                                "width": 0,
                                "height": 0
                            },
                            "claim_again_img": {
                                "url": "",
                                "ratio": 0,
                                "width": 0,
                                "height": 0
                            },
                            "vip_claim_again_img": {
                                "url": "",
                                "ratio": 0,
                                "width": 0,
                                "height": 0
                            },
                            "vip_normal_img": {
                                "url": "",
                                "ratio": 0,
                                "width": 0,
                                "height": 0
                            },
                            "vip_received_img": {
                                "url": "",
                                "ratio": 0,
                                "width": 0,
                                "height": 0
                            },
                            "vip_disabled_img": {
                                "url": "",
                                "ratio": 0,
                                "width": 0,
                                "height": 0
                            }
                        }
                    ],
                    "validate_pic_vip": False,
                    "validate_vip": False
                },
                "style": {
                    "url_floor": "",
                    "content_background_color": "",
                    "content_background_image": {
                        "url": "",
                        "ratio": 0,
                        "width": 0,
                        "height": 0
                    },
                    "show_content_padding": 0,
                    "show_border_radius_top": 0,
                    "show_border_radius_bottom": 0,
                    "show_floor_padding": 0,
                    "floor_background_color": "",
                    "content_color": ""
                },
                "filter": {
                    "is_open": 0,
                    "data": []
                },
                "id": 8865,
                "brick_type": "marketing_coupon"
            },
            {
                "category": 1,
                "brick_name": "瀑布流商品",
                "config": {
                    "layout": 2,
                    "is_landing_page_pingoods": 0,
                    "tab": 0,
                    "pin_tags": [
                        "coupon",
                        "mall_coupon",
                        "rank",
                        "selling",
                        "coin",
                        "promote",
                        "service",
                        "sec_kill",
                        "mn_quality_odm_footnote"
                    ],
                    "show_prime_price": 1,
                    "line_price": 0,
                    "shop_car": 2,
                    "shop_car_icon": {
                        "url": "",
                        "ratio": 0,
                        "width": 0,
                        "height": 0
                    },
                    "superscript": 1,
                    "superscript_size": 3,
                    "superscript_pos": 1,
                    "superscript_img": {
                        "url": "",
                        "ratio": 0,
                        "width": 0,
                        "height": 0
                    },
                    "show_soldout": 1,
                    "belt": 1,
                    "page_sign": 2,
                    "title_mark": 0,
                    "title_mark_img": {
                        "url": "",
                        "ratio": 0,
                        "width": 0,
                        "height": 0
                    },
                    "price_mark": 0,
                    "price_mark_img": {
                        "url": "",
                        "ratio": 0,
                        "width": 0,
                        "height": 0
                    },
                    "jump_type": 1,
                    "show_more": 1,
                    "show_today_fire": 2,
                    "show_goods_mn": 0,
                    "items": [
                        {
                            "title": "",
                            "icon": {
                                "url": "",
                                "ratio": 0,
                                "width": 0,
                                "height": 0
                            },
                            "select_icon": {
                                "url": "",
                                "ratio": 0,
                                "width": 0,
                                "height": 0
                            },
                            "target_type": "2",
                            "target_val": "4047",
                            "target_text": "4047 | 劲霸K-BOXING",
                            "extend": "",
                            "relation_coupon": ""
                        }
                    ],
                    "title_lines": 1,
                    "sale_type": 0,
                    "sale_attrs_color": "#666666",
                    "sale_attrs_type": 1,
                    "sale_attrs_background_color": "#ffffff",
                    "sale_attrs_background_img": {
                        "url": "",
                        "ratio": 0,
                        "width": 0,
                        "height": 0
                    },
                    "price_attrs": {
                        "show_price_attrs": 0,
                        "pre": "",
                        "type": 1,
                        "img": {
                            "url": "",
                            "ratio": 0,
                            "width": 0,
                            "height": 0
                        },
                        "color": "#ffffff",
                        "background_color": "#FF0E48"
                    },
                    "action_btn": {
                        "type": 1,
                        "position": 1,
                        "img": {
                            "url": "",
                            "ratio": 0,
                            "width": 0,
                            "height": 0
                        }
                    },
                    "show_belt": 1,
                    "is_tab_fix": 0,
                    "tab_margin": 1,
                    "img_size": 2,
                    "image_text_position": 1,
                    "verification": True,
                    "verification_coupon": False,
                    "pin_tags_lines": 1,
                    "price": 2
                },
                "style": {
                    "url_floor": "",
                    "content_background_color": "",
                    "content_background_image": {
                        "url": "",
                        "ratio": 0,
                        "width": 0,
                        "height": 0
                    },
                    "show_content_padding": 0,
                    "show_border_radius_top": 0,
                    "show_border_radius_bottom": 0,
                    "show_floor_padding": 0,
                    "floor_background_color": "",
                    "content_color": ""
                },
                "filter": {
                    "is_open": 0,
                    "data": []
                },
                "content": {
                    "group": ""
                },
                "ext_style": {
                    "selected_color": "#FF6565",
                    "selected_background_color": "",
                    "unselected_color": "#666666",
                    "background_color": "",
                    "selected_background_image": {
                        "url": "",
                        "ratio": 0,
                        "width": 0,
                        "height": 0
                    },
                    "unselected_background_image": {
                        "url": "",
                        "ratio": 0,
                        "width": 0,
                        "height": 0
                    },
                    "page_sign_selected_color": "#FF6565",
                    "page_sign_selected_background_color": "#FFFFFF",
                    "page_sign_unselected_color": "#666666",
                    "page_sign_background_color": "#FFFFFF",
                    "selected_underline": True,
                    "tab_selected_underline": True,
                    "background_image": {
                        "url": "",
                        "ratio": 0,
                        "width": 0,
                        "height": 0
                    },
                    "tab_height": 30,
                    "selected_font_weight": 1
                },
                "id": 8866,
                "brick_type": "goods_waterfall"
            }
        ],
        "nav_footer": {},
        "first_screen_bricks_num": 2
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }


class PublishItems(Lego):
    method = 'put'
    api = '/api/lego/page/$project_id/publish'
    data = {}

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
