from getgauge.python import step, data_store
from api.oms_new.menu import Menu


@step("获取新OMS菜单")
def menu():
    menu = Menu()

    resp = menu.request()

    assert resp['code'] == 0

    print(resp)
