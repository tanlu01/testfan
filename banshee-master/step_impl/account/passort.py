from getgauge.python import step, data_store
from api.account.passport.login_by_captcha import LoginByCaptcha
from api.account.passport.logout import Logout
from api.account.passport.one_step_login import OneStepLogin
from api.account.passport.wechat_login import WechatLogin
from api.account.passport.captcha_image import CaptchaImage
from api.account.passport.captcha_sms import CaptchaSms
from api.account.passport.login_by_pass import LoginByPass
import responses


@step("passport密码登录, phone=<phone>, password=<password>")
def login_by_pass(phone, password):
    login_by_pass = LoginByPass()
    login_by_pass.data['phone'] = phone
    login_by_pass.data['password'] = password
    resp = login_by_pass.request()
    data_store.spec["session"] = resp['data']['member_id'], resp['data']['token']
    # print(resp['data'])

@step("passport验证码登录, phone=<phone>")
def login_by_captcha(phone):
    login_by_captcha = LoginByCaptcha()
    login_by_captcha.data['phone'] = phone
    resp = login_by_captcha.request()
    data_store.spec["session"] = resp['data']['member_id'], resp['data']['token']
    # print(resp['data'])

@step("passport一步登录, geyan_token=<geyan_token>, tel_type=<tel_type>")
@responses.activate
# 打开对应业务线APP，点一键登录时会通过sdk取到geyan_token。
# 不清楚geyan_token的生产逻辑，需要抓包时设置断点，在sdk取到后加入接口参数中。
def one_step_login(geyan_token, tel_type):
    one_step_login = OneStepLogin()
    one_step_login['geyan_token'] = geyan_token
    one_step_login['tel_type'] = tel_type
    resp = one_step_login.request()
    # print(resp)

@step("passport微信登录, code=<code>")
@responses.activate
def weixin_login(code):
    weixin_login = WechatLogin()
    weixin_login.data['code'] = code
    resp = weixin_login.request()
    # print(resp)

@step("passport登出, token=<token>")
def passport_logout(token):
    logout = Logout()
    if token == 'from_data_store':
        logout.data['token'] = data_store.spec["session"][1]
    else:
        logout.data['token'] = token
    resp = logout.request()
    assert resp['code'] == 0

@step("获取验图片证码, phone=<phone>")
def captcha_image(phone):
    captcha_image = CaptchaImage()
    captcha_image.data['telephone'] = phone
    resp = captcha_image.request()
    print(resp)

@step("获取验短信证码, phone=<phone>")
def captcha_sms(phone):
    captcha_sms = CaptchaSms()
    captcha_sms.data['telephone'] = phone
    resp = captcha_sms.request()
    print(resp)