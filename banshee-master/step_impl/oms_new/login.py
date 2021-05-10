from getgauge.python import step, data_store
from api.oms_new.auth.auth import Auth
from api.oms_new.oms_ import Oms


@step("新oms登陆,用户名=<username>,密码=<password>")
def auth(username, password):
    auth = Auth()
    auth.data['username'] = username
    auth.data['password'] = password

    result = auth.request()

    assert result['code'] == 0

    data_store.spec['token'] = result['payload']['token']


@step("注入token到OmsApiHeaders")
def inject_cookies_to_Oms_api_header():
    Oms.headers['X-Token'] = data_store.spec['token']
