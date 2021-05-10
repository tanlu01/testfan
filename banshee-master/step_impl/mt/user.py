from getgauge.python import step, data_store
from api.mt.mt import Mt
from api.mt.user.login import Login
from api.mt.user.prime import Prime
from models.mt.pt_buyer import Buyer as BuyerModel


@step("获取qa_login_token,phone=<phone>")
def qa_token(phone):
    login = Login()
    login.data['mobile'] = phone
    resp = login.request()

    assert resp['code'] == 0

    data_store.suite["token"] = resp['data']['token']
    data_store.suite['login_phone'] = phone


@step("注入token到MtApiHeaders")
def inject_login_token_to_mt_api_header():
    Mt.headers['X-Token'] = data_store.suite["token"]


@step("获取登陆用户id")
def get_user_id():
    buyer = BuyerModel.get(mobile=data_store.suite['login_phone'])

    data_store.suite['user_id'] = buyer.id


@step('获取登陆用户是否开通会员')
def get_user_prime():
    prime = Prime()
    resp = prime.request()

    assert resp['code'] == 0

    data_store.suite['prime'] = resp['data']['prime_identity']
