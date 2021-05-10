from api.account.account import Passport
import os, time, uuid

class WechatLogin(Passport):
    method = 'post'
    headers = {'qtt_app_name': 'toutiao.oauth'}
    host = os.getenv('ACCOUNT_HOST')
    api = '/account/weixin/login'
    data = {
        "code": "打开对应业务线APP，点微信登录时会通过sdk取到code",
        "is_auto_register": "1",
        "public_params": Passport.public_params
    }

    mock_status = 200
    mock_data = {
        'code': 0,
        'message': 'from mock'
    }