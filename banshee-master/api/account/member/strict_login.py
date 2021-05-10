from api.account.account import Member
import os, time, json, uuid


class StrictLogin(Member):
    method = 'post'
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/58.0.3029.110",
        "Referer": "http://api.1sapp.com/doc/index.html"
    }
    host = os.getenv('MEMBER_HOST')
    api = '/member/strictLogin'
    data = Member.public_params.copy()
    data.update({
        'from': 'normal',
        'brand': 'Meizu',
        'manufacturer': 'Meizu',
        'model': '15 Plus',
        'clipboard_extend': '',
        'invite_code': '',
        'zfb_code': None,
        'captcha': 1234
    })

    def by_phone(self, phone):
        self.data.update({
            'strict_login_type': '101',
            'telephone': phone,
        })
    
    def by_wechat(self, wechat):
        self.data.update({
            'strict_login_type': '102',
            'weixin_code': wechat,
        })
    
    def by_alipay(self, alipay):
        self.data.update({
            'strict_login_type': '103',
            'zfb_code': alipay,
        })

    mock_status = 200
    mock_data = {
        'code': 60000,
        'message': 'from mock'
    }
