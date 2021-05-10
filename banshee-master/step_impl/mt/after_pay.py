from getgauge.python import step, data_store
from api.mt.mt import Mt
from api.mt.after_pay.gold_return_check import Gold_return_check
from api.mt.after_pay.popup import Popup


@step("参加活动返回")
def gold_return_check():
    gold_return_check = Gold_return_check()
    gold_return_check.request()
    print(gold_return_check.resp.json())


@step("活动返推币")
def popup():
    popup = Popup()
    popup.request()
    print(popup.resp.json())