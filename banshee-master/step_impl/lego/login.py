from getgauge.python import step
from api.lego.lego import Lego
from api.token import generate_token


@step("Lego平台登录,注入token到LegoApiHeaders")
def get_token():
    Lego.headers['X-Token'] = generate_token()
