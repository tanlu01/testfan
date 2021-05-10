from getgauge.python import step, data_store
from api.risk.module.index import Index


@step("模块管理首页")
def module_index():
    module_index = Index()

    resp = module_index.request()
    assert resp['code'] == 0

