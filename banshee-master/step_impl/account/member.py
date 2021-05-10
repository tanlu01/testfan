from getgauge.python import step, data_store
from api.account.member.strict_login import StrictLogin
from api.account.member.login import Login
from api.account.member.logout import Logout
from api.account.member.captcha_picture import Captcha_picture
import operator


@step("微信/手机注册登录, <type>=<no>")
def member_strict_login(type, no):
    strict_login = StrictLogin()
    operator.methodcaller(f'by_{type}', no)(strict_login)
    resp = strict_login.request()
    data_store.spec['session'] = resp['data']['member_id'], resp['data']['token']
    # print(resp['data'])


@step("密码登录, phone=<phone> pwd=<pwd>")
def member_login(phone, pwd):
    login = Login()
    login.data['telephone'] = phone
    login.data['password'] = pwd
    resp = login.request()
    # print(resp)


@step("member登出, token=<token>")
def member_logout(token):
    logout = Logout()
    if token == 'from_data_store':
        logout.data['token'] = data_store.spec["session"][1]
    else:
        logout.data['token'] = token
    resp = logout.request()
    assert resp['code'] == 0


@step("get_captcha_picture")
def get_captcha_picture():
    captcha_picture = Captcha_picture()
    resp = captcha_picture.request()
    print(captcha_picture.resp.json())

    assert resp['code'] == 0
    data_store.scenario.setdefault('captcha_data', {}).update({'content_type': resp['data']['content_type']})
    data_store.scenario.setdefault('captcha_data', {}).update({'token': resp['data']['token']})
    data_store.scenario.setdefault('captcha_data', {}).update({'image': resp['data']['image']})
