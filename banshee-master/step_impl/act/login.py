from getgauge.python import step
from api.act.act_ import Act
from api.token import generate_token


@step("Act平台登录,注入token到ActApiHeaders")
def get_token():
    token = str(generate_token(), encoding='utf-8')

    Act.headers['X-Token'] = token
    Act.cookies['X-Token'] = token
