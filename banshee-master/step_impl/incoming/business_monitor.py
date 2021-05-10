from getgauge.python import step, data_store
from api.incoming.business_monitor.info_appid import InfoAppid
from api.incoming.business_monitor.info_productid import InfoProductid

@step("<arg> 的 AppId")
def get_app_id(arg):
    info_appid = InfoAppid()
    resp = info_appid.request()
    assert resp['code'] == 0
    for app in resp['data']:
        if app['value']==arg or app['label']==arg:
            data_store.scenario['app_id'] = app

@step("<arg> 的 ProductId")
def get_product_id(arg):
    info_productid = InfoProductid()
    resp = info_productid.request()
    assert resp['code'] == 0
    for product in resp['data']:
        if product['value']==arg or product['label']==arg:
            data_store.scenario['product_id'] = product