from api.mt.mt import Mt
import os
import datetime
from random import randint


class Words(Mt):
    method = 'get'
    api = '/v1/search/words'
    data = {}

    success_resp = {'code': 0}
    error_resp = {
        'code': 400000,
        'message': '没有可以购买的商品'
    }
    #可以认为测试环境写死的数据是正确的数据
    words={
     '砍价':'1',
     '助力享免单':'0',
     '任务中心':'0',
     '888师徒':'0'
    }
    links={
     '砍价':'http://sx-kanjia.mengtuiapp.com/indexnew?dev=test\u0026exp=B',
     '助力享免单':'http://sx.app.mengtuiapp.com/activity/help_free_2.html?activity_id=215',
     '任务中心':'http://sx.mobile.mengtuiapp.com/x2/task.html',
     '888师徒':'http://sx.app.mengtuiapp.com/activity/mentorship.html'
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
                    "hot_words",
                    "activity_words"
                ],
                "properties": {
                    "hot_words": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "word": {
                                    "type": "string"
                                },
                                "style": {
                                    "type": "number"
                                }
                            }
                        }
                    },
                    "activity_words": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "link": {
                                    "type": "string"
                                },
                                "word": {
                                    "type": "string"
                                }
                            }
                        }
                    }
                }
            }
        }
    }
