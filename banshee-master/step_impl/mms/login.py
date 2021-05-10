from getgauge.python import step, data_store
from api.mms.auth.captcha import Captcha
from api.mms.auth.auth import Auth
from api.mms.mms_ import Mms


@step("获取登陆的token,然后从redis获取验证码")
def captcha():
    captcha = Captcha()
    resp = captcha.request()
    assert resp['code'] == 0
    data_store.scenario.setdefault('login_info', {}).update({'token': resp['payload']['token']})

    rd = captcha.rd()
    code = rd.get(f'captcha_{data_store.scenario["login_info"]["token"]}')
    assert len(code) == 4
    data_store.scenario.setdefault('login_info', {}).update({'code': code})


@step("mms登陆,username=<username>,password=<password>")
def auth(username, password):
    auth = Auth()
    auth.data['username'] = username
    auth.data['password'] = password
    auth.data['captcha'] = data_store.scenario['login_info']['code']
    auth.data['token'] = data_store.scenario['login_info']['token']

    resp = auth.request()

    assert resp['code'] == 0
    data_store.suite['mall_id'] = resp['payload']['userInfo']['mall_id']
    Mms.headers['Cookie'] = f'dev_session={resp["payload"]["session_id"]}'
