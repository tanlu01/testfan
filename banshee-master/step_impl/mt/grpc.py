from getgauge.python import step, data_store
from rpc.mt.user.user import User
import logging


@step("try_grpc")
def try_grpc():
    s = User()
    r = s.user_by_id('36049841')
    logging.log('r')
