from getgauge.python import step, data_store
from api.lego.projects.list import List


@step("获取项目管理列表")
def projects_list():
    projects_list = List()

    resp = projects_list.request()
    print(resp)
    assert resp['code'] == 0
