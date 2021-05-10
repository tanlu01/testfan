from api.mt.mt import Mt
import os
import datetime
from random import randint


class V2_mall_info(Mt):
    method = 'get'
    api = '/v2/mall/$mall_id/info'
    data = {}

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
    success_resp = {
        'code': 0,
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
                    "mall_name",
                    "logo",
                    "logo_origin",
                    "background_img",
                    "mall_sales",
                    "company_phone",
                    "goods_num",
                    "mall_desc",
                    "coupons",
                    "is_open",
                    "mall_share",
                    "mall_icon",
                    "followers",
                    "wallpaper",
                    "category_link",
                    "mall_score",
                    "mall_score_int",
                    "mall_labels"
                ],
                "properties": {
                    "mall_id": {
                        "type": "number"
                    },
                    "mall_name": {
                        "type": "string"
                    },
                    "logo": {
                        "type": "string"
                    },
                    "logo_origin": {
                        "type": "string"
                    },
                    "background_img": {
                        "type": "string"
                    },
                    "mall_sales": {
                        "type": "number"
                    },
                    "company_phone": {
                        "type": "string"
                    },
                    "goods_num": {
                        "type": "number"
                    },
                    "mall_desc": {
                        "type": "string"
                    },
                    "coupons": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {

                            }
                        }
                    },
                    "is_open": {
                        "type": "boolean"
                    },
                    "mall_share": {
                        "type": "object",
                        "required": [
                            "desc",
                            "link",
                            "img"
                        ],
                        "properties": {
                            "desc": {
                                "type": "string"
                            },
                            "link": {
                                "type": "string"
                            },
                            "img": {
                                "type": "string"
                            }
                        }
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
                    },
                    "followers": {
                        "type": "number"
                    },
                    "wallpaper": {
                        "type": "string"
                    },
                    "category_link": {
                        "type": "string"
                    },
                    "mall_score": {
                        "type": "object",
                        "required": [
                            "shipping_rating",
                            "description_rating",
                            "service_rating"
                        ],
                        "properties": {
                            "shipping_rating": {
                                "type": "boolean"
                            },
                            "description_rating": {
                                "type": "boolean"
                            },
                            "service_rating": {
                                "type": "boolean"
                            }
                        }
                    },
                    "mall_score_int": {
                        "type": "object",
                        "required": [
                            "shipping_rating",
                            "description_rating",
                            "service_rating"
                        ],
                        "properties": {
                            "shipping_rating": {
                                "type": "number"
                            },
                            "description_rating": {
                                "type": "number"
                            },
                            "service_rating": {
                                "type": "number"
                            }
                        }
                    },
                    "mall_labels": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {

                            }
                        }
                    }
                }
            }
        }
    }

class Info_Goods_id(Mt):
    method ='get'
    api = '/v2/mall/$mall_id/info?goods_id=$goods_id'
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
                    "mall_name",
                    "logo",
                    "logo_origin",
                    "background_img",
                    "mall_sales",
                    "company_phone",
                    "goods_num",
                    "mall_desc",
                    "coupons",
                    "is_open",
                    "mall_share",
                    "mall_icon",
                    "followers",
                    "wallpaper",
                    "category_link",
                    "mall_score",
                    "mall_score_int",
                    "mall_labels"
                ],
                "properties": {
                    "mall_id": {
                        "type": "number"
                    },
                    "mall_name": {
                        "type": "string"
                    },
                    "logo": {
                        "type": "string"
                    },
                    "logo_origin": {
                        "type": "string"
                    },
                    "background_img": {
                        "type": "string"
                    },
                    "mall_sales": {
                        "type": "number"
                    },
                    "company_phone": {
                        "type": "string"
                    },
                    "goods_num": {
                        "type": "number"
                    },
                    "mall_desc": {
                        "type": "string"
                    },
                    "coupons": {
                        "type": "array",
                        "items": {
                            "type": "object",
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
                        }
                    },
                    "is_open": {
                        "type": "boolean"
                    },
                    "mall_share": {
                        "type": "object",
                        "required": [
                            "desc",
                            "link",
                            "img"
                        ],
                        "properties": {
                            "desc": {
                                "type": "string"
                            },
                            "link": {
                                "type": "string"
                            },
                            "img": {
                                "type": "string"
                            }
                        }
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
                    },
                    "followers": {
                        "type": "number"
                    },
                    "wallpaper": {
                        "type": "string"
                    },
                    "category_link": {
                        "type": "string"
                    },
                    "mall_score": {
                        "type": "object",
                        "required": [
                            "shipping_rating",
                            "description_rating",
                            "service_rating"
                        ],
                        "properties": {
                            "shipping_rating": {
                                "type": "boolean"
                            },
                            "description_rating": {
                                "type": "boolean"
                            },
                            "service_rating": {
                                "type": "boolean"
                            }
                        }
                    },
                    "mall_score_int": {
                        "type": "object",
                        "required": [
                            "shipping_rating",
                            "description_rating",
                            "service_rating"
                        ],
                        "properties": {
                            "shipping_rating": {
                                "type": "number"
                            },
                            "description_rating": {
                                "type": "number"
                            },
                            "service_rating": {
                                "type": "number"
                            }
                        }
                    },
                    "mall_labels": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {

                            }
                        }
                    }
                }
            }
        }
    }
