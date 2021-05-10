from getgauge.python import step
from api.oms.category.category import Category


@step("oms获取categoryurl")
def category():
    category = Category()
    resp = category.request()

    assert resp['code'] == 0
