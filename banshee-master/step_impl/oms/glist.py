from getgauge.python import step,data_store
from api.oms.auth.auth import Auth
from api.oms.oms_ import Oms
import requests
from api.oms.glist.glist import Glist

@step("oms商品列表查询,a=<a>")
def glist(a):
    glist = Glist()
    glist.data['datatable[query][generalSearch]']=int(a)
    resp = glist.request()

    assert resp['data'][0]['goods_id'] ==glist.data['datatable[query][generalSearch]']
