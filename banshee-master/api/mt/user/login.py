from api.mt.mt import Mt
import os


class Login(Mt):
    method = 'post'
    headers = {'Content-Type': 'application/json'}
    host = os.getenv('API_GATEWAY_HOST')
    api = '/v1/users/login'
    data = {
        "code": "9876",
        "mobile": "15021721254",
        "platform": 50,
        "type": 1
    }
