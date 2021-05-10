from api.mt.mt import Mt
import os
import datetime
from random import randint


class LoginAnchor(Mt):
    method = 'post'
    headers = {'Content-Type': 'application/json'}
    host = os.getenv('API_GATEWAY_HOST')
    api = '/v1/accounts/login/anchor'
    data = {
        "type": 6,
        "account": "15223781978",
        "password": "123456",
        "platform": "",
        "source": "",
        "ref": ""
    }


