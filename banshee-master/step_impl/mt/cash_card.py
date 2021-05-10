from getgauge.python import step, data_store
from api.mt.mt import Mt
from api.mt.cash_card.get_cash_card import Cash_card
from api.mt.cash_card.cash_card_activate import Activate


@step("用户礼品卡")
def cash_card():
    cash_card = Cash_card()
    cash_card.request()
    print(cash_card.resp.json())


@step("激活礼品卡, card_secret=<card_secret>")
def cash_card_activate(card_secret):
    activate = Activate()
    activate.data['card_secret'] = card_secret
    print(activate.data)
    activate.request()
    print(activate.resp.json())
