from getgauge.python import step, data_store
from  api.prime.experience_prime import Experience_prime
from api.prime.prime_buy import Prime_buy
from api.prime.prime_config import Prime_config
from api.prime.profile_prime import Profile_prime


@step("用户领取体验会员")
def receive_prime():
    exprience_prime=Experience_prime()
    resp=exprience_prime.request()
    assert resp['code']==exprience_prime.success_resp['code']

@step("验证个人中心变成体验会员")
def verificat_profile_prime():
    profile_prime=Profile_prime()
    resp=profile_prime.request()
    assert resp['code']==profile_prime.success_resp['code']
    assert resp['data']['prime_identity']==1

@step("验证会员中心成为体验会员")
def verificat_prime_center():
    prime_config=Prime_config()
    resp=prime_config.request()
    assert resp['code']==prime_config.success_resp['code']
    assert resp['data']['prime_info']['prime_identity']==1


@step("吊起支付面板,可成功支付,<identity>购买成为<card>会员")
def prime_buy_card(identity,card):
    prime_buy=Prime_buy()
    if card=="月卡" and identity=="非会员/体验会员":
        prime_buy.data['page_name']="{\"ref_page_name\":\"bottom_tabbar\",\"page_name\":\"prime\",\"page_id\":\"x.prime_1609334148267_oXqFxYzbB0\",\"key_param\":\"none\",\"layout\":\"{\\\"skin\\\":\\\"award_money\\\",\\\"channel\\\":\\\"mt_test\\\",\\\"package_id\\\":\\\"\\\"}\",\"mode\":\"prime_modules.payment_button_0.02\",\"from_pos\":\"\",\"action_type\":\"purchase\",\"payment_method\":3,\"channel\":\"mt_test\",\"platform\":\"android\"}"
        prime_buy.data['package_id']="163"
    if card=="年卡" and identity=="非会员/体验会员":
        prime_buy.data['page_name'] ="{\"ref_page_name\":\"bottom_tabbar\",\"page_name\":\"prime\",\"page_id\":\"x.prime_1609329493352_OdSud18Cs1\",\"key_param\":\"free\",\"layout\":\"{\\\"skin\\\":\\\"multiple_package\\\",\\\"channel\\\":\\\"mt_test\\\",\\\"package_id\\\":\\\"\\\"}\",\"mode\":\"prime_modules.payment_button_0.01\",\"from_pos\":\"\",\"action_type\":\"purchase\",\"payment_method\":3,\"channel\":\"mt_test\",\"platform\":\"android\"}"
        prime_buy.data['package_id'] = "164"
    if card=="年卡" and identity=="月卡会员":
        prime_buy.data['page_name']="{\"ref_page_name\":\"bottom_tabbar\",\"page_name\":\"prime\",\"page_id\":\"x.prime_1609399099194_0457vsiO0L\",\"key_param\":\"free\",\"layout\":\"{\\\"skin\\\":\\\"multiple_package\\\",\\\"channel\\\":\\\"mt_test\\\",\\\"package_id\\\":\\\"\\\"}\",\"mode\":\"prime_modules.payment_button\",\"from_pos\":\"\",\"action_type\":\"recharge\",\"payment_method\":0,\"channel\":\"mt_test\",\"platform\":\"android\"}"
        prime_buy.data['package_id'] = "157"
    resp=prime_buy.request()
    assert resp['code']==0
    assert resp['data']['reward']=="购买成功"
