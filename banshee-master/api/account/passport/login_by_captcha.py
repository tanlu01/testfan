from api.account.account import Passport
import os, time, uuid

class LoginByCaptcha(Passport):
    method = 'post'
    headers = {'qtt_app_name': 'toutiao.oauth'}
    host = os.getenv('ACCOUNT_HOST')
    api = '/account/phone/loginbycaptcha'
    data = {
        "phone": "13809617804",
        "captcha": "1234",
        "is_auto_register": 1,
        "public_params": Passport.public_params
    }

    mock_status = 200
    mock_data = {
        'code': 60000,
        'message': 'from mock'
    }