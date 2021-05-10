from api.mt.mt import Mt
import os
import datetime
from random import randint


class Result_page(Mt):
    method = 'get'
    api = '/v1/search/page?q=$search_keyword&sort=$sort&offset&size=10&min_price=$min_price&max_price=$max_price&expand_filters=$expand_filters&cat=$cat'
    data = {}

    success_resp = {
        'code': 0
    }

    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }

    # expected_schema = {
    #     "$schema": "http://json-schema.org/draft-06/schema#",
    #     "title": "expected_data",
    #     "type": "object",
    #     "required": [
    #         "code",
    #         "time",
    #         "data"
    #     ],
    #     "properties": {
    #         "code": {
    #             "type": "number"
    #         },
    #         "time": {
    #             "type": "number"
    #         },
    #         "data": {
    #             "type": "object",
    #             "required": [
    #                 "items",
    #                 "banner",
    #                 "banner_link",
    #                 "cats",
    #                 "is_black",
    #                 "total",
    #                 "offset",
    #                 "qc",
    #                 "ctx",
    #                 "expand_filters",
    #                 "inject_filters"
    #             ],
    #             "properties": {
    #                 "items": {
    #                     "type": "array",
    #                     "items": {
    #                         "type": "object",
    #                         "properties": {
    #                             "type": {
    #                                 "type": "number"
    #                             },
    #                             "pos_id": {
    #                                 "type": "string"
    #                             },
    #                             "goods": {
    #                                 "type": "object",
    #                                 "required": [
    #                                     "goods_id",
    #                                     "goods_name",
    #                                     "short_name",
    #                                     "thumb_url",
    #                                     "ethumb",
    #                                     "market_price",
    #                                     "min_group_price",
    #                                     "min_normal_price",
    #                                     "min_price",
    #                                     "sales",
    #                                     "sales_text",
    #                                     "sales_whole_text",
    #                                     "mall_id",
    #                                     "money_types",
    #                                     "footnote",
    #                                     "promotion_mark",
    #                                     "tdata",
    #                                     "import_mark",
    #                                     "marks_front",
    #                                     "marks_back",
    #                                     "marks_rear",
    #                                     "mall",
    #                                     "service_promise_mark",
    #                                     "dispatch_place",
    #                                     "fund",
    #                                     "show_price",
    #                                     "reward_mark",
    #                                     "show_cart",
    #                                     "main_gallery_carousel",
    #                                     "mark_recommend"
    #                                 ],
    #                                 "properties": {
    #                                     "goods_id": {
    #                                         "type": "string"
    #                                     },
    #                                     "goods_name": {
    #                                         "type": "string"
    #                                     },
    #                                     "short_name": {
    #                                         "type": "string"
    #                                     },
    #                                     "thumb_url": {
    #                                         "type": "string"
    #                                     },
    #                                     "ethumb": {
    #                                         "type": "object",
    #                                         "required": [
    #                                             "img",
    #                                             "ratio"
    #                                         ],
    #                                         "properties": {
    #                                             "img": {
    #                                                 "type": "string"
    #                                             },
    #                                             "ratio": {
    #                                                 "type": "string"
    #                                             }
    #                                         }
    #                                     },
    #                                     "market_price": {
    #                                         "type": "number"
    #                                     },
    #                                     "min_group_price": {
    #                                         "type": "number"
    #                                     },
    #                                     "min_normal_price": {
    #                                         "type": "number"
    #                                     },
    #                                     "min_price": {
    #                                         "type": "number"
    #                                     },
    #                                     "sales": {
    #                                         "type": "number"
    #                                     },
    #                                     "sales_text": {
    #                                         "type": "string"
    #                                     },
    #                                     "sales_whole_text": {
    #                                         "type": "string"
    #                                     },
    #                                     "mall_id": {
    #                                         "type": "number"
    #                                     },
    #                                     "money_types": {
    #                                         "type": "array",
    #                                         "items": [
    #                                             {
    #                                                 "type": "number"
    #                                             }
    #                                         ]
    #                                     },
    #                                     "footnote": {
    #                                         "type": "string"
    #                                     },
    #                                     "promotion_mark": {
    #                                         "type": "string"
    #                                     },
    #                                     "tdata": {
    #                                         "type": "string"
    #                                     },
    #                                     "import_mark": {
    #                                         "type": "string"
    #                                     },
    #                                     "marks_back": {
    #                                         "type": "array",
    #                                         "items": {
    #                                             "type": "object",
    #                                             "properties": {
    #                                                 "id": {
    #                                                     "type": "string"
    #                                                 },
    #                                                 "text": {
    #                                                     "type": "string"
    #                                                 },
    #                                                 "style": {
    #                                                     "type": "number"
    #                                                 },
    #                                                 "name": {
    #                                                     "type": "string"
    #                                                 },
    #                                                 "img_url": {
    #                                                     "type": "string"
    #                                                 },
    #                                                 "img_ratio": {
    #                                                     "type": "string"
    #                                                 },
    #                                                 "link": {
    #                                                     "type": "string"
    #                                                 },
    #                                                 "icon_url": {
    #                                                     "type": "string"
    #                                                 },
    #                                                 "icon_ratio": {
    #                                                     "type": "string"
    #                                                 }
    #                                             }
    #                                         }
    #                                     },
    #                                     "marks_rear": {
    #                                         "type": "array",
    #                                         "items": {
    #                                             "type": "object",
    #                                             "properties": {
    #
    #                                             }
    #                                         }
    #                                     },
    #                                     "mall": {
    #                                         "type": "object",
    #                                         "required": [
    #                                             "mall_id",
    #                                             "mall_name",
    #                                             "location",
    #                                             "labels"
    #                                         ],
    #                                         "properties": {
    #                                             "mall_id": {
    #                                                 "type": "string"
    #                                             },
    #                                             "mall_name": {
    #                                                 "type": "string"
    #                                             },
    #                                             "location": {
    #                                                 "type": "string"
    #                                             }
    #                                         }
    #                                     },
    #                                     "dispatch_place": {
    #                                         "type": "string"
    #                                     },
    #                                     "fund": {
    #                                         "type": "object",
    #                                         "required": [
    #                                             "fund_returns"
    #                                         ],
    #                                         "properties": {
    #                                             "fund_returns": {
    #                                                 "type": "number"
    #                                             }
    #                                         }
    #                                     },
    #                                     "show_price": {
    #                                         "type": "number"
    #                                     },
    #                                     "reward_mark": {
    #                                         "type": "string"
    #                                     },
    #                                     "show_cart": {
    #                                         "type": "boolean"
    #                                     },
    #                                     "main_gallery_carousel": {
    #                                         "type": "string"
    #                                     },
    #                                     "mark_recommend": {
    #                                         "type": "string"
    #                                     }
    #                                 }
    #                             },
    #                             "search_goods_type": {
    #                                 "type": "number"
    #                             }
    #                         }
    #                     }
    #                 },
    #                 "banner": {
    #                     "type": "string"
    #                 },
    #                 "banner_link": {
    #                     "type": "string"
    #                 },
    #                 "cats": {
    #                     "type": "array",
    #                     "items": {
    #                         "type": "object",
    #                         "properties": {
    #                             "title": {
    #                                 "type": "string"
    #                             },
    #                             "id": {
    #                                 "type": "string"
    #                             }
    #                         }
    #                     }
    #                 },
    #                 "is_black": {
    #                     "type": "boolean"
    #                 },
    #                 "total": {
    #                     "type": "number"
    #                 },
    #                 "offset": {
    #                     "type": "string"
    #                 },
    #                 "qc": {
    #                     "type": "string"
    #                 },
    #                 "ctx": {
    #                     "type": "string"
    #                 },
    #                 "expand_filters": {
    #                     "type": "array",
    #                     "items": {
    #                         "type": "object",
    #                         "properties": {
    #                             "key": {
    #                                 "type": "string"
    #                             },
    #                             "title": {
    #                                 "type": "string"
    #                             },
    #                             "is_expanded": {
    #                                 "type": "boolean"
    #                             },
    #                             "expand_style": {
    #                                 "type": "number"
    #                             },
    #                             "multi": {
    #                                 "type": "boolean"
    #                             },
    #                             "items": {
    #                                 "type": "array",
    #                                 "items": {
    #                                     "type": "object",
    #                                     "properties": {
    #                                         "id": {
    #                                             "type": "string"
    #                                         },
    #                                         "name": {
    #                                             "type": "string"
    #                                         },
    #                                         "sub_name": {
    #                                             "type": "string"
    #                                         },
    #                                         "icon": {
    #                                             "type": "string"
    #                                         }
    #                                     }
    #                                 }
    #                             }
    #                         }
    #                     }
    #                 },
    #                 "inject_filters": {
    #                     "type": "string"
    #                 }
    #             }
    #         }
    #     }
    # }

