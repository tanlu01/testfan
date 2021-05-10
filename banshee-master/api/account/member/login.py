from api.account.account import Member
from api.encrypt import account_sign
import os, time, json, uuid


class Login(Member):
    method = 'get'
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/58.0.3029.110",
        "Referer": "http://api.1sapp.com/doc/index.html"
    }
    host = os.getenv('MEMBER_HOST')
    api = '/member/loginV2'
    data = Member.public_params.copy()
    data.update({
        'telephone': '13764964838',
        'password': '123456',
        'tk': 'ACAvKAJEZnFFkKfRjRzJULP9t_CU6r7LrfM0NzUxNDk1MDg5NTIyNQ',
        'from': 'normal',
        'manufacturer': 'HUAWEI',
        'clipboard_extend': ''
    })

    mock_status = 200
    mock_data = {
        'code': 60000,
        'message': 'from mock'
    }

    def request(self):
        # sign = account_sign(params=self.data, ingnored_keys=(), filter_falsy=False)
        # self.data['sign'] = sign
        return super().request()