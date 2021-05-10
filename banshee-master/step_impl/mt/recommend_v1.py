from getgauge.python import step, data_store
from api.mt.mt import Mt
import urllib
from api.mt.goods.v1_recommend import V1_recommend


@step("获取订单v1_get, clue=<clue>,offset=<offset>,referer=<referer>,size=<size>")
def recommend_v1(clue,offset,referer,size):
    v1_recommend = V1_recommend()
    v1_recommend.api = v1_recommend.api.replace('$clue',clue).replace('$offse', offset).replace('$referer', referer).replace('$size', size)

    resp = v1_recommend.request()
    print(resp)