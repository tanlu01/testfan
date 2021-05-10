from api.account.account import Passport
import os, time, uuid, random, string

class LoginByPass(Passport):
    method = 'post'
    headers = {'qtt_app_name': 'toutiao.oauth'}
    host = os.getenv('ACCOUNT_HOST')
    api = '/account/phone/loginbypass'
    data = {
        "phone": "18601785687",
        "password": '123456',
        "public_params": Passport.public_params.copy()
    }

    mock_status = 200
    mock_data = {
        'code': 0,
        'message': 'from mock'
    }