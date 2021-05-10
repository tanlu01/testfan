from getgauge.python import step
from api.risk.risk import Risk
from api.token import generate_token


@step("注入token到RiskApiHeaders")
def get_token():
    Risk.headers['X-Token'] = generate_token()
