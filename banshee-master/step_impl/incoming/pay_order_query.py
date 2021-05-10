from getgauge.python import data_store, step
from api.incoming.pay.pay_order_query import PayOrderQuery
import responses

@step("requestit <api>")
@responses.activate
def requestit(api):
    req = PayOrderQuery()
    req.data['code'] = 1
    resp = req.request()
    data_store.scenario["resp"] = resp

@step("checkit, response code = <code>")
def checkit(code):
    assert data_store.scenario["resp"]["code"] == int(code)