from api.request import Request
import os, time, random, datetime

class NewCoin(Request):
    method = 'post'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    host = os.getenv('COIN_HOST')
    api = '/charging/newCoin'
    data = {
        "user_id": 747583,
        "amount": 1000,
        "scene_id": 2717,
        "out_trade_no": datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "".join([str(random.choice(range(10))) for _ in range(22)]),
        "update_cache": 1,
        "charge_time": int(time.time()),
        "op_user_id": 747583,
        "add_total": 1,
        "transaction": 1,
        "extra": "",
        "tk": "",
        "ip": ""
    }

    mock_status = 200
    mock_data = {
                    'code': 60000,
                    'message': 'from mock'
                }