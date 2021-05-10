from getgauge.python import step, data_store
from api.oms.auth.auth import Auth
from api.oms.oms_ import Oms
import requests


@step("oms登陆,phone=<phone>,password=<password>")
def auth(phone, password):
    auth = Auth()
    auth.data['username'] = phone
    auth.data['password'] = password

    result = auth.request()

    assert result['code'] == 0

    data_store.spec.setdefault('cookies_info', {}).update(requests.utils.dict_from_cookiejar(auth.resp.cookies))


@step("注入cookies到OmsApiHeaders")
def inject_cookies_to_Oms_api_header():
    for k, v in data_store.spec['cookies_info'].items():
        Oms.headers['Cookie'] += f'{k}={v}'
