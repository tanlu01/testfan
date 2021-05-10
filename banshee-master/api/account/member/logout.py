from api.account.account import Member
import os, time, json, uuid


class Logout(Member):
    method = 'get'
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/58.0.3029.110",
        "Referer": "http://api.1sapp.com/doc/index.html"
    }
    host = os.getenv('MEMBER_HOST')
    api = '/member/logout'
    data = Member.public_params.copy()
    data.update({
        'deviceCode': '869963021640650',
        'device_code': '869963021640650',
        'distinct_id': '3df9e7dcbe141f65',
        'guid': '87ad2b9d374275c3c555c4d9150.24227777',
        'token': '93e3of5gT8Pd6-576HSIcif9n-OljHwxprDQljKCmNgO_ZN36JRLh_Zaxvt7GEY1k_9EYxXnxMucelVTxg',
        'env': 'qukan_qa',
        'sign': 'bf6b00154ebc1446e34d4be3adcabd00'
    })

    mock_status = 200
    mock_data = {
        'code': 60000,
        'message': 'from mock'
    }

    # 这个接口不用加密，我猜测是GET请求不需要加密
    # 这个接口似乎只关心token一个参数
    def request(self):
        return super(Member, self).request()
