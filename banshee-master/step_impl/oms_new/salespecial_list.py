from getgauge.python import step, data_store
from api.oms_new.salespecial.salespecial_list import Salespecial_List


@step("获取新OMS促销专题列表")
def salespecial_list():
    salespecial_list = Salespecial_List()

    resp = salespecial_list.request()

    print(resp)

    assert resp['code'] == 0