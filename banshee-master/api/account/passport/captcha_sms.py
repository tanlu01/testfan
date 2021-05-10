from api.account.account import Passport
import os, time, uuid, random, string

class CaptchaSms(Passport):
    method = 'post'
    headers = {'qtt_app_name': 'toutiao.oauth'}
    host = os.getenv('ACCOUNT_HOST')
    api = '/captcha/sms'
    data = {
        # 140开头的手机号，测试环境也会发短信到手机
        "telephone": "14853948999",
        "device_code": ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20)),
        # 短信验证码，不需要图形验证码的image_captcha和image_captcha_id
        "image_captcha": '',
        "image_captcha_id": '',
        # 用户注册: 1;
        # 找回密码: 2;
        # 修改密码: 3;
        # 通用: 4;
        # 微信授权绑定手机: 5;
        # 绑定手机: 6;
        "use_way": 1,
        "public_params": Passport.public_params.copy()
    }

    mock_status = 200
    mock_data = {
        'code': 0,
        'message': 'from mock'
    }