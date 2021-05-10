from getgauge.python import step, data_store
from api.mt.mt import Mt
from api.mt.account.login_anchor import LoginAnchor


@step("登录主播")
def login_anchor():
    login_anchor = LoginAnchor()
    login_anchor.request()

    print(login_anchor.resp.json())
