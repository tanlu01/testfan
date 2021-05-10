from getgauge.python import step, data_store
from api.mt.mt import Mt
import random
from api.mt.refund.v1_refund import Refund
from api.mt.refund.refund_id import Refund_id
from api.mt.refund.complain import Complain
from api.mt.refund.revoke import Revoke
from api.mt.refund.trace import Trace
from api.mt.refund.update import Update
from api.mt.refund.refund_category import Refund_category
a = []  # 存储refund_id


@step("获取退款列表")
def refund():
    refund = Refund()
    resp = refund.request()
    for item in resp['data']['list']:
        a.append(item['id'])
    print(refund.resp.json())


@step("查询退款售后详情, refund_id=<refund_id>")
def select_refund_id(refund_id):
    select_refund_id = Refund_id()
    if refund_id not in a:
        n = random.randint(0, len(a)-1)  # 随机其中之一退款refund_id
        refund_id = a[n]
    select_refund_id.api = select_refund_id.api.replace(
        "$refund_id", refund_id)
    select_refund_id.request()
    print(select_refund_id.resp.json())


@step("查询退款钱款去向, refund_id=<refund_id>")
def trace(refund_id):
    trace = Trace()
    if refund_id not in a:
        n = random.randint(0, len(a)-1)  # 随机其中之一退款refund_id
        refund_id = a[n]
    trace.api = trace.api.replace("$refund_id", refund_id)
    trace.request()
    print(trace.resp.json())


@step("申请平台介入, refund_id=<refund_id>")
def complain(refund_id):
    complain = Complain()
    complain.api = complain.api.replace("$refund_id", refund_id)
    complain.request()
    print(complain.resp.json())


@step("买家修改退款申请, refund_id=<refund_id>")
def update(refund_id):
    # try:
    #     data_store.scenario['refund']['aftersale_id'] = refund_id
    update = Update()
    update.api = update.api.replace("$refund_id", refund_id)
    update.request()
    print(update.resp.json())


@step("买家撤销退款申请, refund_id=<refund_id>")
def revoke(refund_id):
    revoke = Revoke()
    revoke.api = revoke.api.replace("$refund_id", refund_id)
    revoke.request()
    print(revoke.resp.json())


@step("获取退款类别列表，获得各种类型的退款的数量")
def refund_category():
    refund_category = Refund_category()
    refund_category.request()
    print(refund_category.resp.json())
