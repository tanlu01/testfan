from getgauge.python import step,data_store
from api.mms.skudetail.sku_detail import SkuDetail


@step("mms查看商品结算价,goods_id=<goods_id>")
def sku_detail(goods_id):
    sku_detail = SkuDetail()
    sku_detail.data['goods_id'] = int(goods_id)
    resp = sku_detail.request()

    assert resp['code'] == 0
    assert resp['payload']['sku'][0]['goods_id'] == '107807'
    data_store.suite['cost'] = resp['payload']['sku'][0]['cost']
    data_store.suite['goods_id'] = sku_detail.data['goods_id']


    
    

