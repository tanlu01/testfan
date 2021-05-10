from getgauge.python import step, data_store
from api.mms.balance.mall_balance import MallBalance


@step("获取商家店铺基本信息")
def mall_balance():
    mall_balance = MallBalance()
    resp = mall_balance.request()
    assert resp['code'] == 0
    data_store.suite['mall_id'] = resp['payload']['mall_id']
