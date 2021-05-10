from getgauge.python import step, data_store
from api.oms_new.live.create_account import CreateAccount


@step("创建主播账号,手机号码=<phone>,密码=<psw>")
def create_account(phone, psw):
    create_account = CreateAccount()

    phone = data_store.suite['phone'] if not phone else phone
    create_account.data['mobile'] = phone

    create_account.data['passwd'] = psw

    resp = create_account.request()

    assert resp['code'] == 0

    print(resp)
