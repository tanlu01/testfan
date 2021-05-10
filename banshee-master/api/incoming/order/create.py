from api.request import Request
import os, datetime
from random import randint

class Create(Request):
    method = 'post'
    headers = {'Content-Type': 'application/json'}
    host = os.getenv('ORDER_HOST')
    api = '/v2/order/create'
    data = {
        "app_id": "bt8dot25xwfc",
        "pay": {
            "amount": 95,
            #"app_id": "btm50dpy7zlt", # bt8dot25xwfc 游戏  btm50dpy7zlt 米读
            "from": "H5",
            "ishidetitle": "undefined",
            "land": "0",
            "notice_url": "https://newidea4-gamecenter-backend.1sapp.com/x/pay/notice",
            "open_id": "123",
            "pl": "qtt",
            "quit_url": "https://qttpay.1sapp.com/pay2",
            "receipt": 1,
            "return_url": "https://qttpay.1sapp.com/pay2",
            "scene_id": 1,
            "title": "趣头条",
            "channel_scene_id":2,
            "channel_id":1
        },
        "product":
            {
                "id": "20101",
                "price": 2801
            }
        ,
        "out_trade_no": datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "-union-qtt-" + str(randint(0, 99999)),
        "user_id": 33333,
        "user_type": 1,
        "coin":{
                "third_part_id":1,
                "new_coin":10,
                "is_sub_account":False
        },
        "coupon":
        {"code":""}
    }

    mock_status = 200
    mock_data = {
                    'code': 60000,
                    'message': 'from mock'
                }