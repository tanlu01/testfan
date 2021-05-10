from api.mt.mt import Mt
import os
import datetime
from random import randint


class Goods(Mt):
    method = 'get'
    api = '/v1/goods/$goods_id'
    data = {
        # 是否要额外获取类目上的配置，需要传1，不需要则不用携带
        # 'cat_conf': '99937'
    }
