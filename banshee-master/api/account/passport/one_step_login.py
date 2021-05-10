from api.account.account import Passport
import os, time, uuid

class OneStepLogin(Passport):
    method = 'post'
    headers = {'qtt_app_name': 'toutiao.oauth'}
    host = os.getenv('ACCOUNT_HOST')
    api = '/account/phone/oneStepLogin'
    data = {
        "geyan_token": "打开对应业务线APP，点一键登录时会通过sdk取到geyan_token",
        # chinaunicom：联通
        # chinamobile：移动
        # chinatel：电信
        "tel_type": "chinaunicom",
        "public_params": Passport.public_params
    }

    mock_status = 200
    mock_data = {
        'code': 0,
        'message': 'from mock'
    }